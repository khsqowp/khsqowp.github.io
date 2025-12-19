---
layout: post
title: "Phase 2-1: 스캐닝과 스니핑 (Scanning & Sniffing)"
date: 2024-12-30 09:00:02 +0900
categories: [general]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 2-1: 스캐닝과 스니핑 (Scanning & Sniffing)

## 학습 목표
- 네트워크 정찰(Reconnaissance)의 목적과 단계 이해
- Port Scanning 기법별 동작 원리와 탐지 회피 방법 습득
- Sniffing의 원리와 네트워크 환경별 가능 조건 파악
- Nmap, Wireshark 등 주요 도구의 실전 활용법 학습
- 방어 관점에서 Scanning/Sniffing 탐지 및 대응 방법 이해

---

## 1. 네트워크 정찰 개요 (Network Reconnaissance)

### 1.1 정찰의 정의와 목적

**정찰 (Reconnaissance)**
- 공격 대상에 대한 정보를 수집하는 사전 단계
- 공격자: 취약점 발견, 공격 경로 파악
- 관리자: 네트워크 인벤토리 관리, 보안 점검

**정보 수집 유형**
- **Passive Reconnaissance (수동적 정찰)**
  - 대상 시스템과 직접 접촉 없음
  - 공개 정보 활용: WHOIS, DNS, Google Search
  - 탐지 불가능
  
- **Active Reconnaissance (능동적 정찰)**
  - 대상 시스템과 직접 상호작용
  - Port Scanning, Ping Sweep
  - 로그에 기록됨 (탐지 가능)

### 1.2 공격 단계 (Kill Chain)

```
1. Reconnaissance (정찰)
   ↓
2. Scanning (스캐닝)
   ↓
3. Gaining Access (접근 획득)
   ↓
4. Maintaining Access (접근 유지)
   ↓
5. Covering Tracks (흔적 제거)
```

**Scanning이 중요한 이유**
- 공격 대상 선정의 핵심 단계
- 열린 포트 = 잠재적 공격 진입점
- 서비스 버전 = 취약점 매칭 가능

---

## 2. Footprinting (발자국 조사)

### 2.1 정의
- 공격 전 대상 조직의 정보를 최대한 수집
- 기업 정보, 네트워크 구조, 사용 기술 파악

### 2.2 정보 수집 방법

**WHOIS 조회**
```bash
# 도메인 소유자 정보 확인
whois example.com

# 결과 예시
Domain Name: EXAMPLE.COM
Registry Domain ID: 2336799_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.iana.org
Updated Date: 2024-08-14T07:01:00Z
Creation Date: 1995-08-14T04:00:00Z
Registrar: RESERVED-Internet Assigned Numbers Authority
Registrant Organization: Internet Assigned Numbers Authority
```

**수집 가능 정보**
- 도메인 소유자 (조직명, 담당자)
- 등록 일자, 만료 일자
- 네임서버 (DNS 서버)
- 등록 대행사 (Registrar)
- IP 주소 범위 (ARIN, RIPE 등)

**DNS 정보 수집**
```bash
# A 레코드 (IPv4 주소)
dig example.com A
nslookup example.com

# MX 레코드 (메일 서버)
dig example.com MX

# NS 레코드 (네임서버)
dig example.com NS

# TXT 레코드 (SPF, DKIM 등)
dig example.com TXT

# Zone Transfer 시도 (설정 오류 시)
dig @ns1.example.com example.com AXFR
```

**Zone Transfer 취약점**
- DNS 서버 설정 오류 시 전체 DNS 레코드 노출
- 내부 호스트 이름, IP 주소 일괄 획득
- **방어**: Allow-Transfer 설정으로 신뢰 서버만 허용

**Google Hacking (Google Dorking)**
```
# 특정 사이트의 PDF 파일 검색
site:example.com filetype:pdf

# 디렉토리 인덱싱 노출 검색
intitle:"index of" site:example.com

# 관리자 페이지 검색
inurl:admin site:example.com

# 비밀번호 파일 검색
inurl:passwords.txt

# SQL 오류 메시지 검색
intext:"sql syntax near" | intext:"syntax error has occurred"

# 카메라/IoT 장치 검색
intitle:"webcamXP 5"
inurl:":8080" intitle:"Live View"
```

**Shodan (IoT/서비스 검색 엔진)**
- 인터넷 연결 기기 검색
- 취약한 웹캠, 라우터, SCADA 시스템 발견
- 예시 쿼리:
  - `port:3389` : RDP 포트 열린 시스템
  - `os:"Windows Server 2008"` : 구버전 OS
  - `http.title:"Dashboard" country:"KR"` : 한국의 대시보드

**Social Engineering (사회공학)**
- LinkedIn: 직원 정보, 조직도, 사용 기술
- 채용 공고: 사용 기술 스택 파악
- 회사 홈페이지: 연락처, 사무실 위치

### 2.3 Footprinting 방어

- **정보 최소화**: 공개 정보 통제
- **WHOIS 프라이버시**: 등록자 정보 보호 서비스 사용
- **DNS 보안**: Zone Transfer 차단, DNSSEC 적용
- **robots.txt**: 검색 엔진 크롤링 제한 (완전한 차단 아님)
- **직원 교육**: 소셜 미디어 정보 공유 주의

---

## 3. Host Discovery (호스트 탐색)

### 3.1 정의
- 네트워크에서 활성화된 호스트 찾기
- "살아있는" 시스템 식별

### 3.2 탐색 기법

**ICMP Echo Request (Ping Sweep)**
```bash
# 단일 호스트 Ping
ping 192.168.1.100

# Nmap을 이용한 Ping Sweep
nmap -sn 192.168.1.0/24
# -sn: Ping Only (Port Scan 생략)

# fping (다중 호스트 병렬 Ping)
fping -a -g 192.168.1.0/24
# -a: alive hosts only
# -g: range 지정
```

**ICMP Echo 동작**
```
Client                    Server
  |                         |
  | ICMP Echo Request       |
  | Type=8, Code=0          |
  |------------------------>|
  |                         |
  |   ICMP Echo Reply       |
  |   Type=0, Code=0        |
  |<------------------------|
  |                         |
```

**장점**: 빠르고 간단
**단점**: 방화벽에서 ICMP 차단 시 탐지 불가

**TCP SYN Ping**
```bash
# Nmap TCP SYN Ping
nmap -PS80,443 192.168.1.0/24
# -PS: SYN Ping
# 80,443: 대상 포트 (일반적으로 열려있을 가능성 높음)
```

**동작 원리**
```
Client                    Server
  |                         |
  | TCP SYN (Port 80)       |
  |------------------------>|
  |                         |
  |   SYN+ACK (Port Open)   |
  |<------------------------| → 호스트 활성!
  |                         |
  | RST (연결 중단)         |
  |------------------------>|
  |                         |
```

- SYN+ACK 또는 RST 응답 → 호스트 존재
- 응답 없음 → 호스트 없음 또는 필터링
- **장점**: ICMP 차단 우회, 방화벽 통과 가능성 높음

**TCP ACK Ping**
```bash
nmap -PA80,443 192.168.1.0/24
# -PA: ACK Ping
```

**동작**
- Stateful Firewall 우회 시도
- RST 응답 → 호스트 존재

**UDP Ping**
```bash
nmap -PU53 192.168.1.0/24
# -PU: UDP Ping
# 53: DNS 포트
```

**ARP Scan (로컬 네트워크)**
```bash
# Nmap ARP Scan
sudo nmap -PR 192.168.1.0/24
# -PR: ARP Ping

# arp-scan (전용 도구)
sudo arp-scan --localnet
sudo arp-scan 192.168.1.0/24
```

**ARP Scan이 최선인 이유 (로컬 네트워크)**
- L2 레벨 동작 (방화벽 우회)
- 가장 정확
- 빠름

### 3.3 Host Discovery 방어

- **ICMP Rate Limiting**: Ping Flooding 방지
- **방화벽 규칙**: 외부 ICMP 차단
- **호스트 기반 방화벽**: Windows Firewall, iptables
- **IDS/IPS 탐지**: 대량 스캔 패턴 감지

---

## 4. Port Scanning (포트 스캐닝)

### 4.1 정의와 목적

**Port Scanning**
- 대상 호스트의 열린 포트 찾기
- 서비스 식별 및 취약점 매핑

**Port 상태**
- **Open**: 서비스 리스닝 중 (접근 가능)
- **Closed**: 포트는 접근 가능하나 서비스 없음
- **Filtered**: 방화벽이 응답 차단 (상태 알 수 없음)

### 4.2 TCP Port Scanning 기법

#### 4.2.1 TCP Connect Scan (-sT)

**특징**
- 완전한 3-Way Handshake 수행
- 가장 정확하고 확실함
- Root 권한 불필요
- **단점**: 느림, 로그에 기록됨

**동작 과정**
```
Nmap                     Target
  |                         |
  | SYN (Port 80)           |
  |------------------------>|
  |                         |
  | SYN+ACK                 | → Port OPEN
  |<------------------------|
  |                         |
  | ACK                     |
  |------------------------>|
  |                         |
  | RST (연결 종료)         |
  |------------------------>|
```

**Port Closed 시**
```
Nmap                     Target
  |                         |
  | SYN (Port 25)           |
  |------------------------>|
  |                         |
  | RST+ACK                 | → Port CLOSED
  |<------------------------|
```

**명령어**
```bash
nmap -sT 192.168.1.100
# -sT: TCP Connect Scan
```

#### 4.2.2 TCP SYN Scan (-sS, Stealth Scan)

**특징**
- Half-Open Scan (Handshake 미완료)
- 가장 널리 사용
- Root 권한 필요 (Raw Socket)
- 빠르고 은밀함

**동작 과정**
```
Nmap                     Target
  |                         |
  | SYN (Port 22)           |
  |------------------------>|
  |                         |
  | SYN+ACK                 | → Port OPEN
  |<------------------------|
  |                         |
  | RST (Handshake 중단!)   |
  |------------------------>|  ← 연결 미수립! (로그 회피 가능)
```

**왜 "Stealth"인가?**
- 과거: 일부 오래된 시스템은 완전한 연결만 로그 기록
- 현재: 대부분 시스템이 SYN만으로도 로그 기록
- 여전히 "상대적으로" 조용함

**명령어**
```bash
sudo nmap -sS 192.168.1.100
# -sS: SYN Scan (기본값)
```

#### 4.2.3 TCP FIN Scan (-sF)

**원리**
- RFC 793 규칙 악용
  - Closed Port: FIN 수신 → RST 응답
  - Open Port: FIN 수신 → 무시 (응답 없음)

**동작**
```
Nmap                     Target
  |                         |
  | FIN (Port 80)           |
  |------------------------>|
  |                         |
  | (응답 없음)             | → Port OPEN 추정
  |                         |

Nmap                     Target
  |                         |
  | FIN (Port 25)           |
  |------------------------>|
  |                         |
  | RST                     | → Port CLOSED
  |<------------------------|
```

**장점**: 일부 방화벽 우회 가능
**단점**: 
- Windows는 모든 포트에 RST 응답 (RFC 미준수)
- Open|Filtered 구분 불가

**명령어**
```bash
nmap -sF 192.168.1.100
```

#### 4.2.4 TCP Xmas Scan (-sX)

**특징**
- FIN, PSH, URG 플래그 모두 설정
- "크리스마스 트리처럼 불빛이 켜진" 패킷
- FIN Scan과 동일한 원리

**동작**
```
TCP Flags: FIN=1, PSH=1, URG=1

Closed Port → RST 응답
Open Port → 응답 없음
```

**명령어**
```bash
nmap -sX 192.168.1.100
```

#### 4.2.5 TCP NULL Scan (-sN)

**특징**
- 모든 플래그를 0으로 설정
- 비정상 패킷 (정상 TCP에는 없는 형태)

**동작**
```
TCP Flags: 모두 0

Closed Port → RST 응답
Open Port → 응답 없음
```

**명령어**
```bash
nmap -sN 192.168.1.100
```

#### 4.2.6 TCP ACK Scan (-sA)

**목적**
- Port 상태 구분 불가
- **방화벽 규칙 매핑**용

**동작**
```
Nmap                     Target/Firewall
  |                         |
  | ACK (Port 80)           |
  |------------------------>|
  |                         |
  | RST                     | → Unfiltered
  |<------------------------|

  | ACK (Port 443)          |
  |------------------------>|
  |                         |
  | (응답 없음)             | → Filtered (방화벽 차단)
```

**활용**
- Stateful Firewall 여부 판단
- 필터링되는 포트 파악

**명령어**
```bash
nmap -sA 192.168.1.100
```

#### 4.2.7 TCP Window Scan (-sW)

- ACK Scan과 유사
- RST 패킷의 Window Size 값 분석
- Open/Closed 구분 시도
- 시스템마다 동작 다름 (신뢰성 낮음)

### 4.3 UDP Port Scanning (-sU)

**특징**
- UDP는 비연결 프로토콜
- 응답 없을 수 있음 (Open|Filtered)
- **매우 느림**: ICMP Rate Limiting

**동작 과정**
```
Nmap                     Target
  |                         |
  | UDP Packet (Port 53)    |
  |------------------------>|
  |                         |
  | UDP Response            | → Port OPEN
  |<------------------------|

  | UDP Packet (Port 123)   |
  |------------------------>|
  |                         |
  | (응답 없음)             | → Port OPEN|Filtered
  |                         |

  | UDP Packet (Port 99)    |
  |------------------------>|
  |                         |
  | ICMP Port Unreachable   | → Port CLOSED
  | (Type 3, Code 3)        |
  |<------------------------|
```

**중요 UDP 포트**
- 53: DNS
- 67/68: DHCP
- 69: TFTP
- 123: NTP
- 161/162: SNMP
- 514: Syslog

**명령어**
```bash
sudo nmap -sU 192.168.1.100
# 매우 느림!

# 상위 1000개 포트만
sudo nmap -sU --top-ports 1000 192.168.1.100

# 특정 포트만
sudo nmap -sU -p 53,161,514 192.168.1.100
```

**최적화 팁**
```bash
# TCP와 UDP 동시 스캔
sudo nmap -sS -sU -p T:80,443,U:53,161 192.168.1.100
```

### 4.4 Service/Version Detection

**목적**
- 열린 포트에서 실행 중인 서비스 식별
- 서비스 버전 확인 → 취약점 매칭

**Banner Grabbing**
```bash
# 수동 Banner Grabbing
nc 192.168.1.100 22
# SSH-2.0-OpenSSH_7.4

telnet 192.168.1.100 80
GET / HTTP/1.0
# Server: Apache/2.4.6 (CentOS)

# Nmap Version Detection
nmap -sV 192.168.1.100
# -sV: Service Version Detection
```

**심화 버전 탐지**
```bash
# 강도 조절 (0~9, 기본 7)
nmap -sV --version-intensity 9 192.168.1.100
# 9: 모든 프로브 전송 (가장 정확, 가장 느림)

# 가벼운 탐지
nmap -sV --version-light 192.168.1.100
# intensity 2와 동일
```

**동작 원리**
1. 포트 연결
2. NULL Probe 전송 (아무 데이터도 보내지 않고 대기)
3. 응답 분석 (Banner)
4. 특정 프로브 전송 (서비스별 쿼리)
5. nmap-service-probes DB와 매칭

### 4.5 OS Fingerprinting

**목적**
- 대상 시스템의 운영체제 식별
- TCP/IP Stack 구현 차이 이용

**능동적 방식 (Active)**
```bash
sudo nmap -O 192.168.1.100
# -O: OS Detection
```

**판단 근거**
- **TTL 기본값**
  - Linux: 64
  - Windows: 128
  - Cisco: 255
- **TCP Window Size**: OS마다 다른 초기값
- **TCP Options**: MSS, Window Scale, Timestamp 등
- **ICMP 응답**: Error 메시지 구조
- **IP ID Sequence**: 증가 패턴

**예시 응답**
```
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
Network Distance: 1 hop
```

**수동적 방식 (Passive)**
```bash
# p0f (Passive OS Fingerprinting)
sudo p0f -i eth0

# 장점
- 공격 흔적 없음
- 트래픽 관찰만으로 판단

# 단점
- 트래픽이 있어야 함
- 정확도 낮음
```

### 4.6 Nmap 고급 옵션

#### 타이밍 템플릿 (-T)
```bash
# T0: Paranoid (5분마다 1개 패킷) - IDS 회피
nmap -T0 192.168.1.100

# T1: Sneaky (15초마다 1개 패킷)
nmap -T1 192.168.1.100

# T2: Polite (0.4초 간격) - 대역폭 배려
nmap -T2 192.168.1.100

# T3: Normal (기본값)
nmap -T3 192.168.1.100
nmap 192.168.1.100  # 동일

# T4: Aggressive (빠름)
nmap -T4 192.168.1.100

# T5: Insane (매우 빠름, 부정확할 수 있음)
nmap -T5 192.168.1.100
```

#### 패킷 조각화 (Fragmentation)
```bash
# 8바이트 단위로 조각화
nmap -f 192.168.1.100

# 16바이트 단위
nmap -ff 192.168.1.100

# 사용자 정의 MTU
nmap --mtu 24 192.168.1.100
# MTU는 8의 배수여야 함
```

**목적**: 방화벽/IDS 우회

#### Decoy Scan (디코이 스캔)
```bash
# 무작위 10개 IP와 함께 스캔
nmap -D RND:10 192.168.1.100

# 특정 IP로 위장
nmap -D 1.1.1.1,2.2.2.2,ME,3.3.3.3 192.168.1.100
# ME: 실제 내 IP 위치

# 효과: 로그에 여러 IP가 기록되어 실제 공격자 IP 숨김
```

#### Idle Scan (좀비 호스트 스캔)
```bash
nmap -sI zombie_host target_host
# zombie_host: IP ID가 예측 가능하게 증가하는 호스트
```

**원리**
1. Zombie의 IP ID 확인
2. Zombie가 Target에 SYN 전송 (Spoofing)
3. Target 응답 → Zombie의 IP ID 증가
4. 다시 Zombie의 IP ID 확인
5. 증가량으로 Port 상태 판단

**효과**: 실제 공격자 IP 완전 은폐

#### NSE (Nmap Scripting Engine)
```bash
# 기본 스크립트 실행
nmap -sC 192.168.1.100
# 또는
nmap --script=default 192.168.1.100

# 취약점 스캔
nmap --script vuln 192.168.1.100

# 특정 스크립트
nmap --script http-title 192.168.1.100
nmap --script smb-os-discovery 192.168.1.100

# 여러 스크립트
nmap --script "http-* and not http-brute" 192.168.1.100

# 스크립트 인자 전달
nmap --script http-form-brute --script-args userdb=users.txt 192.168.1.100
```

**유용한 NSE 스크립트**
- `http-title`: 웹 페이지 제목
- `smb-os-discovery`: Windows SMB OS 정보
- `ssh-hostkey`: SSH 호스트 키
- `ssl-cert`: SSL 인증서 정보
- `dns-brute`: DNS 서브도메인 브루트포스

### 4.7 Port Scanning 종합 예제

**기본 스캔**
```bash
# 빠른 스캔 (상위 100개 포트)
nmap -F 192.168.1.100

# 모든 포트 스캔
nmap -p- 192.168.1.100
# 또는
nmap -p 1-65535 192.168.1.100

# 특정 포트
nmap -p 80,443,8080 192.168.1.100

# 포트 범위
nmap -p 1-1000 192.168.1.100

# 상위 N개 포트
nmap --top-ports 1000 192.168.1.100
```

**종합 스캔 (공격자 관점)**
```bash
# Phase 1: Host Discovery
nmap -sn 192.168.1.0/24 -oG - | grep "Up" > live_hosts.txt

# Phase 2: Port Scan (TCP)
nmap -sS -p- -T4 --open 192.168.1.0/24 -oA tcp_scan

# Phase 3: Service Version
nmap -sV -sC -p $(cat tcp_scan.gnmap | grep open | cut -d" " -f5 | tr '\n' ',') 192.168.1.0/24 -oA service_scan

# Phase 4: OS Detection
sudo nmap -O --osscan-guess 192.168.1.0/24 -oA os_scan

# Phase 5: UDP Scan (주요 포트)
sudo nmap -sU -p 53,67,68,69,123,161,162,514 192.168.1.0/24 -oA udp_scan

# Phase 6: Vulnerability Scan
nmap --script vuln 192.168.1.0/24 -oA vuln_scan
```

**출력 형식**
```bash
# Normal Output
nmap 192.168.1.100 -oN scan.txt

# XML Output
nmap 192.168.1.100 -oX scan.xml

# Grepable Output
nmap 192.168.1.100 -oG scan.gnmap

# 모든 형식 동시 저장
nmap 192.168.1.100 -oA scan
# → scan.nmap, scan.xml, scan.gnmap
```

---

## 5. Sniffing (스니핑)

### 5.1 정의와 원리

**Sniffing**
- 네트워크 트래픽을 캡처하여 분석
- "도청"의 디지털 버전
- 패킷의 내용을 읽음

**합법적 사용**
- 네트워크 문제 진단
- 성능 분석
- 보안 모니터링

**불법적 사용**
- 비밀번호 탈취
- 개인정보 수집
- 세션 하이재킹 준비

### 5.2 NIC 동작 모드

**Normal Mode (비혼잡 모드)**
- 자신의 MAC 주소로 온 패킷만 수신
- Broadcast MAC (FF:FF:FF:FF:FF:FF)도 수신
- 다른 호스트의 Unicast 패킷은 무시

**Promiscuous Mode (무차별 모드)**
- NIC가 모든 패킷 수신
- MAC 주소 무관하게 캡처
- Sniffing 필수 설정

**설정 방법**
```bash
# Linux
sudo ifconfig eth0 promisc
# 또는
sudo ip link set eth0 promisc on

# 확인
ifconfig eth0
# UP BROADCAST RUNNING PROMISC MULTICAST

# 해제
sudo ifconfig eth0 -promisc

# Windows (Wireshark 사용 시 자동)
```

### 5.3 네트워크 환경별 Sniffing 가능성

#### Hub 환경 (매우 취약)

**Hub 동작**
- 수신한 패킷을 모든 포트로 복제 전송
- Collision Domain 공유
- 모든 호스트가 모든 트래픽 확인 가능

```
    [Hub]
     /|\\ 
    / | \\
   A  B  C  D

A → B 통신:
Hub가 B, C, D 모든 포트로 전송
→ C, D도 패킷 수신 가능 (Promiscuous Mode 시)
```

**Sniffing 조건**: Promiscuous Mode만 활성화

#### Switch 환경 (기본적으로 안전)

**Switch 동작**
- MAC Address Table로 트래픽 필터링
- Unicast는 목적지 포트로만 전송
- Broadcast, Multicast는 모든 포트로 전송

```
    [Switch]
     /|\\ 
    / | \\
   A  B  C  D

Switch MAC Table:
Port 1: MAC-A
Port 2: MAC-B
Port 3: MAC-C
Port 4: MAC-D

A → B 통신:
Switch는 Port 2로만 전송
→ C, D는 패킷 수신 불가
```

**Sniffing 방법 (Switch 환경)**

**1. MAC Flooding (CAM Table Overflow)**
```
원리:
1. 대량의 가짜 MAC 주소 프레임 전송
2. Switch의 MAC Address Table 오버플로우
3. Switch가 Hub처럼 동작 (Fail-Open Mode)
4. 모든 포트로 Flooding → Sniffing 가능

도구:
- macof (dsniff 패키지)
- Yersinia
```

```bash
# macof 실행
sudo macof -i eth0 -n 1000
# -n: 전송할 패킷 수

# 초당 수천 개의 랜덤 MAC 주소 생성
# 몇 초 내 Switch CAM Table 포화
```

**방어**:
- Port Security (MAC 주소 개수 제한)
```cisco
switchport port-security
switchport port-security maximum 2
switchport port-security violation shutdown
```

**2. ARP Spoofing (MITM)**
- Phase 2-2에서 상세 다룸
- ARP Cache 조작으로 트래픽 중간에서 가로챔

**3. Port Mirroring (SPAN)**
- Switch 관리자 권한 필요
- 특정 포트 트래픽을 모니터링 포트로 복제
- 합법적 네트워크 모니터링용

```cisco
# Cisco SPAN 설정
monitor session 1 source interface Gi0/1
monitor session 1 destination interface Gi0/24
```

### 5.4 Sniffing 도구

#### Wireshark (GUI)

**설치**
```bash
# Ubuntu/Debian
sudo apt install wireshark

# Windows/macOS: wireshark.org에서 다운로드
```

**기본 사용법**
1. 네트워크 인터페이스 선택
2. Start Capture
3. Display Filter로 필터링
4. 패킷 상세 분석

**Display Filter 예시**
```
# IP 주소 필터
ip.addr == 192.168.1.100
ip.src == 192.168.1.100
ip.dst == 192.168.1.200

# 프로토콜 필터
http
tcp
udp
dns
arp

# 포트 필터
tcp.port == 80
tcp.dstport == 443
udp.port == 53

# HTTP 메서드
http.request.method == "POST"
http.request.method == "GET"

# 조합
ip.addr == 192.168.1.100 && tcp.port == 80
http && ip.src == 192.168.1.100
!(arp or dns)  # ARP, DNS 제외
```

**Capture Filter (BPF 문법)**
```
# 호스트
host 192.168.1.100

# 포트
port 80
dst port 443

# 프로토콜
tcp
udp

# 조합
tcp and port 80
host 192.168.1.100 and not port 22
```

**Follow TCP Stream**
- 전체 TCP 세션 재구성
- HTTP 요청/응답 전체 확인
- 우클릭 → Follow → TCP Stream

**패킷 저장**
```
File → Save As → .pcap or .pcapng
```

#### tcpdump (CLI)

**기본 사용법**
```bash
# 기본 캡처
sudo tcpdump -i eth0

# 특정 호스트
sudo tcpdump -i eth0 host 192.168.1.100

# 특정 포트
sudo tcpdump -i eth0 port 80

# TCP 트래픽만
sudo tcpdump -i eth0 tcp

# 파일 저장
sudo tcpdump -i eth0 -w capture.pcap

# 파일 읽기
tcpdump -r capture.pcap

# 패킷 내용 출력 (ASCII)
sudo tcpdump -i eth0 -A

# 패킷 내용 출력 (HEX)
sudo tcpdump -i eth0 -X

# 특정 개수만 캡처
sudo tcpdump -i eth0 -c 100
```

**고급 필터**
```bash
# SYN 패킷만
sudo tcpdump 'tcp[tcpflags] & tcp-syn != 0'

# HTTP GET 요청
sudo tcpdump -i eth0 -A 'tcp port 80 and (tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420)'

# ICMP Echo Request
sudo tcpdump 'icmp[icmptype] == 8'

# 특정 서브넷
sudo tcpdump net 192.168.1.0/24

# 제외
sudo tcpdump not port 22
```

#### Ettercap (MITM 특화)

**기능**
- ARP Spoofing 자동화
- DNS Spoofing
- SSL/TLS Stripping
- 패킷 변조

**사용 예시**
```bash
# ARP Spoofing MITM
sudo ettercap -T -M arp:remote /192.168.1.1// /192.168.1.100//
# -T: Text mode
# -M arp:remote: ARP Spoofing 활성화
# /192.168.1.1//: Gateway
# /192.168.1.100//: Target

# GUI 모드
sudo ettercap -G
```

#### Cain & Abel (Windows, 개발 중단)

**기능**
- ARP Spoofing
- Password Sniffing
- Wireless Sniffing

### 5.5 Sniffing으로 탈취 가능한 정보

#### HTTP 기본 인증 (Basic Auth)
```
Authorization: Basic dXNlcjpwYXNz

Base64 디코딩:
echo "dXNlcjpwYXNz" | base64 -d
# user:pass
```

**취약점**: Base64는 인코딩일 뿐 암호화 아님

#### FTP 인증
```
USER admin
PASS password123
```

**완전 평문 전송**

#### Telnet
```
모든 입력이 평문
키 하나하나가 별도 패킷
```

#### HTTP POST 데이터
```http
POST /login HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

username=admin&password=secret123
```

**Wireshark Filter**: `http.request.method == "POST"`

#### 쿠키 (Session ID)
```http
Set-Cookie: SESSIONID=abc123def456; Path=/; HttpOnly
```

**탈취 → Session Hijacking 가능**

### 5.6 Sniffing 방어

**암호화**
- **HTTPS** (HTTP over TLS)
- **SSH** (Telnet/FTP 대체)
- **SFTP/SCP** (파일 전송)
- **VPN** (전체 통신 암호화)

**네트워크 분리**
- VLAN으로 트래픽 격리
- 중요 시스템은 별도 세그먼트

**Switch 보안 설정**
```cisco
# Port Security
switchport port-security
switchport port-security maximum 2
switchport port-security violation shutdown
switchport port-security mac-address sticky

# DHCP Snooping
ip dhcp snooping
ip dhcp snooping vlan 10

# Dynamic ARP Inspection
ip arp inspection vlan 10
```

**Promiscuous Mode 탐지**
- 비정상 NIC 모드 감지 도구
- 네트워크 모니터링

**교육**
- 사용자에게 HTTPS 확인 교육
- VPN 사용 권장

---

## 6. 실습 과제

### 과제 1: Nmap Port Scanning
```bash
# 1. 로컬 네트워크 Host Discovery
sudo nmap -sn 192.168.1.0/24

# 2. TCP SYN Scan
sudo nmap -sS -p 1-1000 192.168.1.100

# 3. Service Version Detection
sudo nmap -sV -p 80,443,22 192.168.1.100

# 4. OS Detection
sudo nmap -O 192.168.1.100

# 5. 종합 스캔
sudo nmap -A -T4 192.168.1.100
```

**확인 사항**
- [ ] 열린 포트 목록
- [ ] 각 포트에서 실행 중인 서비스
- [ ] 서비스 버전 정보
- [ ] 추정 운영체제

### 과제 2: Wireshark HTTP 트래픽 분석
```
1. Wireshark 실행
2. http://example.com 접속
3. Display Filter: http
4. POST 요청 찾기
5. 요청 데이터 추출
```

**확인 사항**
- [ ] HTTP GET/POST 요청 구조
- [ ] User-Agent 헤더
- [ ] Cookie 헤더
- [ ] POST 데이터 내용

### 과제 3: tcpdump 패킷 캡처
```bash
# 1. HTTP 트래픽 캡처
sudo tcpdump -i eth0 port 80 -w http.pcap

# 2. DNS 쿼리 캡처
sudo tcpdump -i eth0 port 53 -w dns.pcap

# 3. Wireshark로 분석
wireshark http.pcap
wireshark dns.pcap
```

### 과제 4: Nmap Stealth Scan 비교
```bash
# TCP Connect Scan
sudo nmap -sT -p 80,443 192.168.1.100 -v

# SYN Scan
sudo nmap -sS -p 80,443 192.168.1.100 -v

# FIN Scan
sudo nmap -sF -p 80,443 192.168.1.100 -v
```

**비교 항목**
- 스캔 속도
- 결과 정확도
- 대상 서버 로그 확인 (가능한 경우)

---

## 7. 연결 포인트

### Phase 1.1: Network Architecture
→ **TCP 3-Way Handshake**: SYN Scan 원리의 기초
→ **Port 번호**: Well-Known, Registered, Dynamic 개념

### Phase 1.2: Address System
→ **ARP**: ARP Spoofing으로 Switch 환경에서 Sniffing

### Phase 2.2: Spoofing
→ **ARP Spoofing**: Sniffing을 위한 MITM 구성
→ **IP Spoofing**: Idle Scan, Decoy Scan

### Phase 2.3: Session Hijacking
→ **Sniffing**: Session ID 탈취의 선행 단계
→ **Cookie Sniffing**: HTTP 세션 하이재킹

### Phase 2.4: DoS/DDoS
→ **Port Scanning**: 공격 대상 선정
→ **SYN Scan 원리**: SYN Flooding과 연관

### Phase 3.1: Firewall
→ **Port Scanning 탐지**: 비정상 연결 시도 패턴
→ **ACK Scan**: 방화벽 규칙 매핑

### Phase 3.2: IDS/IPS
→ **Scanning Pattern 탐지**: 대량 포트 스캔 감지
→ **Sniffing 탐지**: Promiscuous Mode 감지

### Phase 4.1: Packet Analysis
→ **Wireshark 실전**: 각 프로토콜 패킷 구조 분석
→ **TCP Flags**: SYN, FIN, ACK 등 실제 확인

---

## 8. 핵심 요약

**Scanning**
- Host Discovery: Ping Sweep, TCP SYN Ping, ARP Scan
- Port Scanning: SYN, Connect, FIN, Xmas, NULL, ACK, UDP
- Nmap: 가장 강력한 Port Scanner
- 목적: 공격 진입점 발견

**Sniffing**
- Promiscuous Mode: 모든 패킷 수신
- Hub: 쉬움, Switch: 어려움 (MITM 필요)
- Wireshark: GUI, tcpdump: CLI
- 목적: 평문 데이터 탈취

**방어**
- Scanning: 방화벽, IDS, Port 최소화
- Sniffing: 암호화 (HTTPS, SSH, VPN)

---

**다음 학습**: Phase 2-2 Spoofing (스푸핑)
