---
layout: post
title: "Phase 3-1: 방화벽 (Firewall)"
date: 2024-12-30 09:00:03 +0900
categories: [network, security]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 3-1: 방화벽 (Firewall)

## 학습 목표
- 방화벽의 개념과 기본 동작 원리 이해
- Packet Filtering, Stateful Inspection, Application Gateway의 차이점 파악
- ACL (Access Control List) 설정 방법 습득
- Linux iptables/nftables 실전 활용
- 차세대 방화벽(NGFW)의 고급 기능 이해
- 방화벽 우회 기법과 대응 방안 학습

---

## 1. 방화벽 개요

### 1.1 정의

**Firewall (방화벽)**
- 네트워크 간 트래픽을 제어하는 보안 시스템
- 허용된 트래픽만 통과, 나머지 차단
- 내부 네트워크를 외부 위협으로부터 보호

**비유**
```
건물의 경비원:
- 출입증 확인 (인증)
- 허가된 사람만 통과
- 의심스러운 사람 차단

방화벽:
- 패킷 헤더 확인
- 정책(Policy)에 따라 허용/차단
- 로그 기록
```

### 1.2 방화벽의 위치

**네트워크 경계**
```
Internet
   |
   | (외부 인터페이스)
[Firewall]
   | (내부 인터페이스)
   |
Internal Network
```

**DMZ (Demilitarized Zone)**
```
Internet
   |
[Firewall 1] ← External Firewall
   |
DMZ (Web Server, Mail Server)
   |
[Firewall 2] ← Internal Firewall
   |
Internal Network (DB, File Server)
```

### 1.3 방화벽의 기본 정책

**Default Deny**
```
기본값: 모두 차단
명시적 허용 규칙만 통과

장점: 보안성 높음
단점: 관리 복잡

권장: 대부분의 환경
```

**Default Allow**
```
기본값: 모두 허용
명시적 차단 규칙만 차단

장점: 편의성
단점: 보안 취약

사용: 테스트 환경만
```

---

## 2. 방화벽 유형

### 2.1 Packet Filtering Firewall (1세대)

**동작 원리**
```
패킷 헤더 정보로 필터링:
- Source IP
- Destination IP
- Source Port
- Destination Port
- Protocol (TCP/UDP/ICMP)
```

**예시 규칙**
```
Rule 1: 외부 → 내부 웹 서버 (80) 허용
  Src: Any
  Dst: 192.168.1.100
  Port: 80
  Protocol: TCP
  Action: ALLOW

Rule 2: 외부 → 내부 SSH 차단
  Src: Any
  Dst: 192.168.1.0/24
  Port: 22
  Protocol: TCP
  Action: DENY

Rule 3: 나머지 모두 차단 (Default Deny)
  Src: Any
  Dst: Any
  Action: DENY
```

**장점**
```
- 빠름 (헤더만 확인)
- 단순함
- 하드웨어 가속 가능
```

**단점**
```
- Stateless (상태 추적 안 함)
- Application Layer 공격 방어 불가
- IP Spoofing 취약
```

**Stateless 문제 예시**
```
정상 통신:
Client → Server: SYN (Port 80)
Server → Client: SYN+ACK (Port 80)

공격:
Attacker → Client: SYN+ACK (Port 80)
(연결 없이 직접 SYN+ACK 전송)

Packet Filtering:
- "Port 80, TCP" → 허용
- 문제: 정상 응답인지 악의적 패킷인지 구분 못 함
```

### 2.2 Stateful Inspection Firewall (2세대)

**상태 추적 (State Table)**
```
연결 테이블 유지:

Connection Table:
Src IP       Dst IP       Src Port  Dst Port  Protocol  State
192.168.1.10 8.8.8.8      50234     80        TCP       ESTABLISHED
192.168.1.20 1.1.1.1      51234     443       TCP       SYN_SENT
```

**동작 과정**
```
1. 외부 → 내부 연결 시도 (차단)
   Src: 8.8.8.8:80
   Dst: 192.168.1.10:50234
   SYN+ACK
   
   상태 테이블 확인:
   - 192.168.1.10:50234 → 8.8.8.8:80 연결 존재?
   - 없음 → DROP (Unsolicited)

2. 내부 → 외부 연결 시작 (허용)
   Src: 192.168.1.10:50234
   Dst: 8.8.8.8:80
   SYN
   
   상태 테이블 추가:
   192.168.1.10:50234 ↔ 8.8.8.8:80 (SYN_SENT)

3. 외부 → 내부 응답 (허용)
   Src: 8.8.8.8:80
   Dst: 192.168.1.10:50234
   SYN+ACK
   
   상태 테이블 확인:
   - 연결 존재 → ALLOW
   - 상태 업데이트: ESTABLISHED
```

**장점**
```
- Spoofing 방어 (상태 확인)
- 효율적 (응답 패킷 자동 허용)
- TCP/UDP 세션 추적
```

**예시: FTP Active Mode**
```
Packet Filtering:
- 서버 → 클라이언트 Port 20 연결 차단
- FTP 작동 안 함

Stateful Inspection:
- PORT 명령 감지
- 서버 → 클라이언트 Port 20 연결 허용 (Related)
- FTP 정상 작동
```

### 2.3 Application Gateway (Proxy Firewall, 3세대)

**Application Layer 검사**
```
L7까지 분석:
- HTTP Method, URL, Header
- FTP 명령어
- SMTP 내용
```

**동작 (Proxy 방식)**
```
Direct Connection:
Client ───────────> Server

Proxy Firewall:
Client ───> Proxy ───> Server
         ↑          ↑
     L7 검사    새 연결 생성
```

**예시: HTTP Proxy**
```
1. Client → Proxy: GET /admin
2. Proxy 검사:
   - URL 필터링: "/admin" 차단 목록?
   - 사용자 인증 확인
   - Malware 스캔
3. 허용 시: Proxy → Server (Client 대신)
4. Server → Proxy: 응답
5. Proxy 검사:
   - Content 필터링
   - Virus 스캔
6. 허용 시: Proxy → Client
```

**장점**
```
- 완전한 L7 가시성
- Content Filtering
- DLP (Data Loss Prevention)
- Malware 차단
```

**단점**
```
- 느림 (모든 연결 Proxy)
- CPU/메모리 많이 사용
- Application별 Proxy 필요
```

### 2.4 차세대 방화벽 (NGFW, Next-Generation Firewall)

**통합 기능**
```
NGFW = Stateful Firewall + IPS + Application Control + 더 많은 기능

주요 기능:
1. Deep Packet Inspection (DPI)
   - L7 프로토콜 식별 (포트 무관)
   - 예: HTTP가 Port 8080에서 실행 → 탐지

2. Application Awareness
   - Facebook, YouTube, BitTorrent 식별
   - Application별 정책 (차단/허용/제한)

3. Integrated IPS
   - Signature 기반 공격 탐지
   - 자동 차단

4. User Identity
   - IP가 아닌 사용자 기반 정책
   - Active Directory 연동

5. SSL Inspection
   - HTTPS 트래픽 복호화 검사
   - Man-in-the-Middle (정당한 목적)

6. Advanced Threat Protection
   - Sandboxing
   - Machine Learning
   - Threat Intelligence
```

**예시: Application Control**
```
전통적 방화벽:
- "Port 443 차단" → 모든 HTTPS 차단

NGFW:
- "YouTube 차단, Gmail 허용"
- 둘 다 443 사용하지만 Application 식별
```

**주요 제품**
```
- Palo Alto Networks (선도 기업)
- Fortinet FortiGate
- Cisco Firepower
- Check Point
- Juniper SRX
```

---

## 3. ACL (Access Control List)

### 3.1 개념

**ACL**
- 순차적 규칙 목록
- 패킷이 규칙과 매칭되면 즉시 처리
- 첫 매칭 규칙 적용 (First Match)

**구조**
```
ACL Entry:
  - Sequence Number
  - Source IP/Subnet
  - Destination IP/Subnet
  - Protocol
  - Source Port
  - Destination Port
  - Action (Permit/Deny)
```

### 3.2 Cisco ACL

**Standard ACL (1-99)**
```
출발지 IP만 확인

access-list 10 permit 192.168.1.0 0.0.0.255
access-list 10 deny any

interface GigabitEthernet0/0
 ip access-group 10 in
```

**Extended ACL (100-199)**
```
출발지/목적지 IP, 프로토콜, 포트

access-list 100 permit tcp 192.168.1.0 0.0.0.255 any eq 80
access-list 100 permit tcp 192.168.1.0 0.0.0.255 any eq 443
access-list 100 deny ip any any

interface GigabitEthernet0/1
 ip access-group 100 out
```

**Named ACL**
```
ip access-list extended WEB_FILTER
 10 permit tcp 192.168.1.0 0.0.0.255 any eq 80
 20 permit tcp 192.168.1.0 0.0.0.255 any eq 443
 30 deny tcp any any eq 22
 40 permit ip any any

interface GigabitEthernet0/0
 ip access-group WEB_FILTER in
```

**주의: Wildcard Mask**
```
Subnet Mask와 반대:
Subnet Mask: 255.255.255.0
Wildcard Mask: 0.0.0.255

0 = Match (확인)
1 = Don't Care (무시)

예:
192.168.1.0 0.0.0.255
→ 192.168.1.0~192.168.1.255
```

### 3.3 ACL 설계 원칙

**1. 순서 중요**
```
잘못된 예:
  10 deny ip any any          ← 모두 차단
  20 permit tcp any any eq 80 ← 도달 안 함 (Dead Rule)

올바른 예:
  10 permit tcp any any eq 80
  20 deny ip any any
```

**2. 가장 구체적인 것 먼저**
```
올바른 순서:
  10 deny tcp 192.168.1.100 0.0.0.0 any eq 22 (특정 호스트)
  20 permit tcp 192.168.1.0 0.0.0.255 any eq 22 (서브넷)
  30 permit tcp any any eq 80 (전체)
  40 deny ip any any (기본 거부)
```

**3. 묵시적 Deny**
```
Cisco ACL 끝에 자동 추가:
  deny ip any any

명시적으로 작성 권장:
  999 deny ip any any log
  (로그 기록)
```

**4. 방향 고려**
```
Inbound (in):
  - 인터페이스로 들어오는 트래픽
  
Outbound (out):
  - 인터페이스에서 나가는 트래픽

보통: 외부 인터페이스 Inbound에 적용
```

---

## 4. Linux Firewall (iptables/nftables)

### 4.1 iptables 구조

**Tables**
```
filter (기본):
  - INPUT: 로컬로 들어오는 패킷
  - OUTPUT: 로컬에서 나가는 패킷
  - FORWARD: 라우팅되는 패킷

nat:
  - PREROUTING: DNAT
  - POSTROUTING: SNAT/MASQUERADE

mangle:
  - 패킷 헤더 수정

raw:
  - Connection Tracking 예외
```

**Chains 흐름**
```
Incoming Packet
   |
   v
PREROUTING (nat, mangle, raw)
   |
   v
Routing Decision
   |
   +----> Local Process? -----> INPUT (filter) ----> Local Application
   |
   +----> Forward? -----> FORWARD (filter) ----> POSTROUTING (nat, mangle)
                                                        |
                                                        v
                                                   Outgoing Packet
```

### 4.2 iptables 기본 명령

**확인**
```bash
# 규칙 확인
sudo iptables -L -v -n
# -L: List
# -v: Verbose (패킷/바이트 수)
# -n: Numeric (IP 주소 그대로)

# NAT 테이블
sudo iptables -t nat -L -v -n

# 줄 번호 포함
sudo iptables -L --line-numbers
```

**추가**
```bash
# 끝에 추가 (-A)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 특정 위치 삽입 (-I)
sudo iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT
# 1번 위치에 삽입

# 출발지 IP 지정
sudo iptables -A INPUT -s 192.168.1.0/24 -p tcp --dport 22 -j ACCEPT

# 목적지 IP 지정
sudo iptables -A FORWARD -d 10.0.0.100 -p tcp --dport 80 -j ACCEPT
```

**삭제**
```bash
# 번호로 삭제
sudo iptables -D INPUT 3

# 규칙 내용으로 삭제
sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT

# 체인 전체 삭제
sudo iptables -F INPUT

# 모든 체인 초기화
sudo iptables -F
```

**정책 변경**
```bash
# 기본 정책 설정
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT
```

### 4.3 iptables 실전 예시

**기본 방화벽 (웹 서버)**
```bash
#!/bin/bash

# 초기화
iptables -F
iptables -X

# 기본 정책: 거부
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Loopback 허용
iptables -A INPUT -i lo -j ACCEPT

# Established/Related 허용 (응답 패킷)
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# SSH 허용 (특정 IP만)
iptables -A INPUT -s 192.168.1.0/24 -p tcp --dport 22 -j ACCEPT

# HTTP/HTTPS 허용
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# ICMP (Ping) 허용
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

# 로그 (거부된 패킷)
iptables -A INPUT -j LOG --log-prefix "iptables-DROP: "

# 저장
iptables-save > /etc/iptables/rules.v4
```

**NAT (인터넷 공유)**
```bash
# IP Forwarding 활성화
echo 1 > /proc/sys/net/ipv4/ip_forward

# MASQUERADE (동적 SNAT)
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# 또는 고정 IP SNAT
iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to-source 203.0.113.10
```

**Port Forwarding (DNAT)**
```bash
# 외부 80 → 내부 192.168.1.100:8080
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 \
  -j DNAT --to-destination 192.168.1.100:8080

# FORWARD 체인도 허용 필요
iptables -A FORWARD -d 192.168.1.100 -p tcp --dport 8080 -j ACCEPT
```

**Rate Limiting (DoS 방어)**
```bash
# SYN Flooding 방어
iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP

# SSH Brute-Force 방어
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent \
  --update --seconds 60 --hitcount 4 -j DROP
# 60초 내 4번 이상 연결 시도 → 차단
```

### 4.4 nftables (최신)

**특징**
```
- iptables 후속
- 더 빠르고 효율적
- 단일 프레임워크 (iptables/ip6tables/arptables 통합)
- 더 나은 문법
```

**기본 설정**
```bash
# 테이블 생성
nft add table inet filter

# 체인 생성
nft add chain inet filter input { type filter hook input priority 0 \; policy drop \; }
nft add chain inet filter forward { type filter hook forward priority 0 \; policy drop \; }
nft add chain inet filter output { type filter hook output priority 0 \; policy accept \; }

# 규칙 추가
nft add rule inet filter input iif lo accept
nft add rule inet filter input ct state established,related accept
nft add rule inet filter input tcp dport 22 accept
nft add rule inet filter input tcp dport { 80, 443 } accept

# 확인
nft list ruleset

# 저장
nft list ruleset > /etc/nftables.conf
```

---

## 5. 방화벽 우회 기법

### 5.1 Tunneling

**SSH Tunneling**
```bash
# Local Port Forwarding
ssh -L 8080:blocked-site.com:80 user@jump-server

# 사용
curl http://localhost:8080
→ blocked-site.com:80으로 전달
```

**VPN**
```
IPsec, OpenVPN, WireGuard
→ 모든 트래픽 암호화
→ 방화벽이 내용 확인 불가
```

### 5.2 Protocol Encapsulation

**HTTP Tunneling**
```
DNS, ICMP를 HTTP로 위장
→ HTTP만 허용하는 방화벽 우회
```

**예: Iodine (DNS Tunneling)**
```bash
# 서버
iodined -f -c -P password 10.0.0.1 tunnel.example.com

# 클라이언트
iodine -f -P password tunnel.example.com
```

### 5.3 Port Hopping

**원리**
```
특정 포트 차단 시 다른 포트 사용
예: SSH Port 22 차단 → Port 443 (HTTPS)로 변경

/etc/ssh/sshd_config:
Port 443

방화벽:
- Port 443 허용 (HTTPS로 착각)
- 실제로는 SSH
```

### 5.4 Fragmentation

**IP Fragmentation**
```
패킷을 작게 조각
→ 방화벽이 재조립하지 못하면 통과

Nmap:
nmap -f target.com
# Fragmentation

방어: Fragment 재조립 후 검사
```

### 5.5 방어 방법

**1. Deep Packet Inspection**
```
NGFW 사용
→ Port가 아닌 Protocol 실제 내용 확인
```

**2. Encrypted Traffic Inspection**
```
SSL/TLS Interception
→ HTTPS 복호화 검사

주의: Privacy 이슈, 인증서 관리
```

**3. Egress Filtering**
```
나가는 트래픽도 제어
→ 허용된 프로토콜만
```

**4. Behavior Analysis**
```
비정상 패턴 탐지
→ Tunneling, Exfiltration
```

---

## 6. 실습 과제

### 과제 1: iptables 기본 방화벽
```bash
#!/bin/bash
# 1. 모든 규칙 초기화
sudo iptables -F

# 2. 기본 정책: DROP
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# 3. Loopback 허용
sudo iptables -A INPUT -i lo -j ACCEPT

# 4. Established 허용
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# 5. SSH 허용
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 6. 테스트
# 다른 PC에서 SSH 접속 시도
```

### 과제 2: Port Forwarding
```bash
# 시나리오: 외부 8080 → 내부 웹서버 80

# 1. IP Forwarding
sudo sysctl -w net.ipv4.ip_forward=1

# 2. DNAT
sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 \
  -j DNAT --to-destination 192.168.1.100:80

# 3. FORWARD 허용
sudo iptables -A FORWARD -d 192.168.1.100 -p tcp --dport 80 -j ACCEPT

# 4. 테스트
curl http://firewall-ip:8080
```

### 과제 3: Rate Limiting
```bash
# SSH Brute-Force 방어
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW \
  -m recent --set --name SSH

sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW \
  -m recent --update --seconds 60 --hitcount 4 --name SSH -j DROP

# 테스트: 60초 내 4번 이상 SSH 접속 시도
# → 차단됨
```

---

## 7. 연결 포인트

### Phase 2.2: Spoofing
→ **IP Spoofing 방어**: uRPF, Ingress Filtering

### Phase 2.4: DoS/DDoS
→ **SYN Flooding**: SYN Cookies, Rate Limiting
→ **Application Flood**: L7 Firewall (WAF)

### Phase 3.2: IDS/IPS
→ **NGFW**: IPS 통합
→ **Signature Detection**: 방화벽 + IPS

### Phase 4.1: Packet Analysis
→ **Wireshark**: 방화벽 로그 분석
→ **차단 패킷**: DROP vs REJECT

---

## 8. 핵심 요약

**방화벽 유형**
- Packet Filtering: L3/L4 헤더만
- Stateful: 연결 상태 추적
- Application Gateway: L7 Proxy
- NGFW: DPI + IPS + Application Control

**ACL**
- 순차적 규칙 목록
- First Match
- 구체적 → 일반적 순서

**iptables**
- Tables: filter, nat, mangle, raw
- Chains: INPUT, OUTPUT, FORWARD
- State: NEW, ESTABLISHED, RELATED

**방어**
- Default Deny
- Egress Filtering
- DPI (Deep Packet Inspection)
- Rate Limiting

---

**다음 학습**: Phase 3-2 IDS/IPS
