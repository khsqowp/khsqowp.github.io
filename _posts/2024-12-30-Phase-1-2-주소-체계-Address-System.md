---
layout: post
title: "Phase 1-2: 주소 체계 (Address System)"
date: 2024-12-30 09:00:01 +0900
categories: [general]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 1-2: 주소 체계 (Address System)

## 학습 목표
- MAC, IP, Port의 3계층 주소 체계 완전 이해
- IPv4 주소 구조와 서브넷팅 계산 능력 습득
- ARP 프로토콜의 동작 원리와 보안 취약점 파악
- NAT의 동작 방식과 보안 영향 이해
- DHCP를 통한 동적 IP 할당 과정 학습

---

## 1. 네트워크 3계층 주소 체계

### 1.1 주소 계층 구조

```
계층                주소 타입          크기              범위                용도
─────────────────────────────────────────────────────────────────────────
L2 (Data Link)     MAC Address       48비트 (6바이트)   로컬 네트워크       물리적 기기 식별
L3 (Network)       IP Address        32비트 (IPv4)      전 세계            논리적 네트워크 식별
L4 (Transport)     Port Number       16비트            0~65535            프로세스/서비스 식별
```

### 1.2 주소의 역할

**MAC Address (Layer 2)**
- 같은 네트워크 내에서 통신
- 하드웨어 고유 주소 (NIC 제조 시 할당)
- 라우터를 넘어가지 않음

**IP Address (Layer 3)**
- 다른 네트워크 간 통신
- 논리적 주소 (관리자가 할당)
- 라우팅 가능

**Port Number (Layer 4)**
- 하나의 IP에서 여러 서비스 구분
- 애플리케이션 식별

### 1.3 통신 예시

```
PC-A (192.168.1.10) → 웹 서버 (8.8.8.8:80)

[PC-A 내부]
Application:  "GET / HTTP/1.1"
Transport:    Source Port=50234, Dest Port=80
Network:      Source IP=192.168.1.10, Dest IP=8.8.8.8
Data Link:    Source MAC=PC-A, Dest MAC=Gateway

[Gateway]
Network:      Dest IP=8.8.8.8 → 라우팅 테이블 확인
Data Link:    Source MAC=Gateway, Dest MAC=Next-Hop

[웹 서버]
Data Link:    Dest MAC=Server → 프레임 수락
Network:      Dest IP=8.8.8.8 → 자신의 IP 확인
Transport:    Dest Port=80 → 웹 서버 프로세스로 전달
Application:  HTTP 요청 처리
```

---

## 2. MAC Address (Media Access Control Address)

### 2.1 구조

**48비트 = 6바이트 = 12자리 16진수**

```
표기법:
- Colon 표기: 00:1A:2B:3C:4D:5E
- Hyphen 표기: 00-1A-2B-3C-4D-5E
- Dot 표기 (Cisco): 001A.2B3C.4D5E
```

**구성**
```
00    :    1A    :    2B    :    3C    :    4D    :    5E
└──────┬──────┘    └──────────────┬──────────────┘
   OUI (24비트)          NIC Specific (24비트)
 제조사 코드            고유 일련번호
```

**OUI (Organizationally Unique Identifier)**
- IEEE가 제조사에 할당
- 제조사별 고유 코드
- 예시:
  - 00:1A:2B → Intel Corporation
  - 00:50:56 → VMware
  - 08:00:27 → VirtualBox

**확인 방법**
```bash
# Linux
ip link show
ifconfig

# Windows
ipconfig /all
getmac

# macOS
ifconfig
```

### 2.2 MAC Address 종류

**Unicast MAC**
- 특정 단일 기기 주소
- LSB (최하위 비트) = 0
- 예: 00:1A:2B:3C:4D:5E

**Broadcast MAC**
- 네트워크 내 모든 기기
- FF:FF:FF:FF:FF:FF
- ARP Request, DHCP Discover 등에 사용

**Multicast MAC**
- 특정 그룹 기기
- LSB = 1
- 예: 01:00:5E:XX:XX:XX (IPv4 Multicast)

### 2.3 MAC Address Table (Switch)

**동작 원리**
```
1. Switch는 수신 프레임의 Source MAC을 포트와 매핑
2. MAC Address Table 구축
3. Destination MAC을 테이블에서 검색
4. 해당 포트로만 전송 (Unicast)
5. 테이블에 없으면 모든 포트로 전송 (Flooding)
```

**MAC Table 예시**
```
Port    MAC Address         VLAN    Age
────────────────────────────────────────
Gi0/1   00:1A:2B:3C:4D:5E   1       60
Gi0/2   00:50:56:AB:CD:EF   1       45
Gi0/3   08:00:27:12:34:56   1       120
```

**확인 명령어**
```bash
# Cisco
show mac address-table

# Linux Bridge
brctl showmacs br0
```

**Aging Time**
- 기본값: 300초 (5분)
- 트래픽 없으면 엔트리 삭제
- 동적 학습 반복

### 2.4 MAC Flooding 공격

**원리**
1. 공격자가 대량의 가짜 MAC 주소 프레임 전송
2. Switch MAC Table 포화
3. Switch가 Hub처럼 동작 (Fail-Open)
4. 모든 트래픽이 모든 포트로 전송
5. 공격자가 Sniffing 가능

**방어**
```cisco
# Port Security
switchport port-security
switchport port-security maximum 2
switchport port-security violation shutdown
switchport port-security mac-address sticky
```

---

## 3. IP Address (Internet Protocol Address)

### 3.1 IPv4 주소 구조

**32비트 = 4바이트 = 4개 옥텟**

```
192     .     168     .     1       .     100
11000000    10101000    00000001    01100100

옥텟1 (8비트) . 옥텟2 (8비트) . 옥텟3 (8비트) . 옥텟4 (8비트)
```

**점으로 구분된 10진수 표기 (Dotted Decimal Notation)**
- 각 옥텟을 10진수로 변환
- 0~255 범위

### 3.2 네트워크 부분과 호스트 부분

**서브넷 마스크 (Subnet Mask)**
- 32비트
- 1: 네트워크 부분
- 0: 호스트 부분

```
IP 주소:       192.168.1.100
서브넷 마스크:  255.255.255.0

2진수 변환:
IP:         11000000.10101000.00000001.01100100
Mask:       11111111.11111111.11111111.00000000
            └──────────네트워크──────────┘└호스트┘

네트워크 주소: 192.168.1.0   (호스트 부분 모두 0)
브로드캐스트:  192.168.1.255 (호스트 부분 모두 1)
사용 가능 IP:  192.168.1.1 ~ 192.168.1.254 (254개)
```

**네트워크 주소 계산 (AND 연산)**
```
IP:         192.168.1.100   = 11000000.10101000.00000001.01100100
Mask:       255.255.255.0   = 11111111.11111111.11111111.00000000
                              ─────────────────────────────────────
Network:    192.168.1.0     = 11000000.10101000.00000001.00000000
```

### 3.3 Classful Addressing (구식)

```
Class   시작 비트   범위                    기본 Mask       호스트 수
───────────────────────────────────────────────────────────────────
A       0           1.0.0.0 ~ 126.255.255.255   /8 (255.0.0.0)          16,777,214
B       10          128.0.0.0 ~ 191.255.255.255 /16 (255.255.0.0)       65,534
C       110         192.0.0.0 ~ 223.255.255.255 /24 (255.255.255.0)     254
D       1110        224.0.0.0 ~ 239.255.255.255 (Multicast)             -
E       1111        240.0.0.0 ~ 255.255.255.255 (Reserved)              -
```

**특수 주소**
- 0.0.0.0: 모든 네트워크
- 127.0.0.0/8: Loopback (자기 자신)
- 255.255.255.255: Limited Broadcast

**문제점**
- IP 주소 낭비 (유연성 부족)
- 예: 300개 호스트 필요 → Class B (65,534개) 할당

### 3.4 CIDR (Classless Inter-Domain Routing)

**표기법**
```
IP주소/프리픽스 길이

예: 192.168.1.0/24
    └─────────┬─────────┘└┬┘
         IP 주소      네트워크 비트 수
```

**프리픽스 길이와 서브넷 마스크 대응**
```
/24 = 255.255.255.0   → 256개 IP (254개 사용 가능)
/25 = 255.255.255.128 → 128개 IP (126개 사용 가능)
/26 = 255.255.255.192 → 64개 IP  (62개 사용 가능)
/27 = 255.255.255.224 → 32개 IP  (30개 사용 가능)
/28 = 255.255.255.240 → 16개 IP  (14개 사용 가능)
/29 = 255.255.255.248 → 8개 IP   (6개 사용 가능)
/30 = 255.255.255.252 → 4개 IP   (2개 사용 가능, P2P)
/31 = 255.255.255.254 → 2개 IP   (RFC 3021, P2P 전용)
/32 = 255.255.255.255 → 1개 IP   (호스트 라우트)
```

**서브넷 마스크 계산**
```
/24:
1111 1111 . 1111 1111 . 1111 1111 . 0000 0000
255       . 255       . 255       . 0

/26:
1111 1111 . 1111 1111 . 1111 1111 . 1100 0000
255       . 255       . 255       . 192
```

### 3.5 서브넷팅 (Subnetting)

**목적**
- 큰 네트워크를 작은 네트워크로 분할
- IP 주소 효율적 사용
- 브로드캐스트 도메인 분리 (성능 향상)
- 보안 (네트워크 분리)

**서브넷팅 공식**
```
서브넷 개수:    2^n (n=빌린 호스트 비트 수)
호스트 개수:    2^h - 2 (h=남은 호스트 비트 수)
서브넷 증가값:  256 - 서브넷 마스크 값
```

**예제 1: 192.168.1.0/24 → /26으로 서브넷팅**
```
원본:
192.168.1.0/24 → 256개 IP (1개 네트워크)

목표:
/26 → 64개 IP씩 4개 네트워크

계산:
/24 → /26: 2비트 빌림
서브넷 개수: 2^2 = 4개
호스트 개수: 2^6 - 2 = 62개

결과:
서브넷 1: 192.168.1.0/26   (192.168.1.0 ~ 192.168.1.63)
  - 네트워크:      192.168.1.0
  - 사용 가능:     192.168.1.1 ~ 192.168.1.62
  - 브로드캐스트:  192.168.1.63

서브넷 2: 192.168.1.64/26  (192.168.1.64 ~ 192.168.1.127)
  - 네트워크:      192.168.1.64
  - 사용 가능:     192.168.1.65 ~ 192.168.1.126
  - 브로드캐스트:  192.168.1.127

서브넷 3: 192.168.1.128/26 (192.168.1.128 ~ 192.168.1.191)
서브넷 4: 192.168.1.192/26 (192.168.1.192 ~ 192.168.1.255)
```

**예제 2: 특정 IP가 속한 서브넷 찾기**
```
질문: 192.168.1.25/28은 어느 서브넷?

/28 = 255.255.255.240
호스트 비트: 4비트 (2^4 = 16개 IP)
서브넷 증가값: 256 - 240 = 16

서브넷 범위:
192.168.1.0    ~ 192.168.1.15   (/28)
192.168.1.16   ~ 192.168.1.31   (/28) ← 25는 여기!
192.168.1.32   ~ 192.168.1.47   (/28)
...

답:
네트워크 주소:   192.168.1.16
브로드캐스트:    192.168.1.31
사용 가능 IP:    192.168.1.17 ~ 192.168.1.30
```

**빠른 계산법**
```
IP: 192.168.1.25
Mask: /28 (240)

Step 1: 증가값 계산
256 - 240 = 16

Step 2: 25를 16으로 나눔
25 ÷ 16 = 1 나머지 9
→ 두 번째 서브넷 (1번 인덱스)

Step 3: 네트워크 주소
16 × 1 = 16
→ 192.168.1.16

Step 4: 브로드캐스트
16 + 16 - 1 = 31
→ 192.168.1.31
```

### 3.6 VLSM (Variable Length Subnet Mask)

**개념**
- 서브넷마다 다른 크기의 마스크 사용
- IP 주소 낭비 최소화

**예제: 네트워크 설계**
```
요구사항:
- 본사: 100개 호스트
- 지사A: 50개 호스트
- 지사B: 20개 호스트
- P2P 링크 3개 (라우터 간): 2개씩

할당된 주소: 192.168.1.0/24

설계:
1. 본사: 192.168.1.0/25   (126개) → 100개 수용
2. 지사A: 192.168.1.128/26 (62개)  → 50개 수용
3. 지사B: 192.168.1.192/27 (30개)  → 20개 수용
4. P2P 1: 192.168.1.224/30 (2개)
5. P2P 2: 192.168.1.228/30 (2개)
6. P2P 3: 192.168.1.232/30 (2개)
7. 예비: 192.168.1.236/30 ~ 192.168.1.252/30
```

### 3.7 공인 IP vs 사설 IP

**공인 IP (Public IP)**
- 전 세계적으로 유일
- IANA/RIR에서 관리
- 인터넷 통신 가능
- 비용 발생

**사설 IP (Private IP) - RFC 1918**
```
Class A:  10.0.0.0      ~ 10.255.255.255    (/8)
Class B:  172.16.0.0    ~ 172.31.255.255    (/12)
Class C:  192.168.0.0   ~ 192.168.255.255   (/16)
```

**특징**
- 조직 내부에서 자유롭게 사용
- 인터넷 직접 통신 불가
- NAT 필요

**Carrier-Grade NAT (CGN) - RFC 6598**
```
100.64.0.0 ~ 100.127.255.255 (/10)
```
- ISP의 대규모 NAT용

### 3.8 특수 IP 주소

```
주소                     용도
──────────────────────────────────────────────
0.0.0.0/8              "This Network" (출발지 IP로만 사용)
0.0.0.0/0              Default Route (모든 네트워크)
127.0.0.0/8            Loopback (자기 자신)
169.254.0.0/16         APIPA (자동 사설 IP, DHCP 실패 시)
224.0.0.0/4            Multicast (D Class)
255.255.255.255/32     Limited Broadcast
```

**Loopback 활용**
```bash
# 자신의 TCP/IP 스택 테스트
ping 127.0.0.1
ping localhost

# 로컬 서비스 테스트
curl http://127.0.0.1:8080
```

---

## 4. ARP (Address Resolution Protocol)

### 4.1 목적

**문제**
- IP 주소는 알지만 MAC 주소를 모름
- L2에서는 MAC 주소 필요

**해결**
- ARP로 IP → MAC 변환

### 4.2 ARP 동작 과정

```
시나리오: PC-A (192.168.1.10) → PC-B (192.168.1.20)

Step 1: ARP Request (Broadcast)
PC-A → All:
"192.168.1.20의 MAC 주소는?"

Ethernet Frame:
  Src MAC:  AA:AA:AA:AA:AA:AA (PC-A)
  Dst MAC:  FF:FF:FF:FF:FF:FF (Broadcast)
  Type:     0x0806 (ARP)

ARP Packet:
  Operation:        Request (1)
  Sender MAC:       AA:AA:AA:AA:AA:AA
  Sender IP:        192.168.1.10
  Target MAC:       00:00:00:00:00:00 (unknown)
  Target IP:        192.168.1.20

Step 2: ARP Reply (Unicast)
PC-B → PC-A:
"내 MAC은 BB:BB:BB:BB:BB:BB야"

Ethernet Frame:
  Src MAC:  BB:BB:BB:BB:BB:BB (PC-B)
  Dst MAC:  AA:AA:AA:AA:AA:AA (PC-A)
  Type:     0x0806 (ARP)

ARP Packet:
  Operation:        Reply (2)
  Sender MAC:       BB:BB:BB:BB:BB:BB
  Sender IP:        192.168.1.20
  Target MAC:       AA:AA:AA:AA:AA:AA
  Target IP:        192.168.1.10

Step 3: ARP Cache 저장
PC-A의 ARP Table:
192.168.1.20  →  BB:BB:BB:BB:BB:BB

Step 4: 실제 데이터 전송
PC-A → PC-B:
Ethernet Frame:
  Src MAC:  AA:AA:AA:AA:AA:AA
  Dst MAC:  BB:BB:BB:BB:BB:BB (이제 알고 있음!)
  Type:     0x0800 (IPv4)
IP Packet:
  Src IP:   192.168.1.10
  Dst IP:   192.168.1.20
```

### 4.3 ARP Cache (ARP Table)

**확인 명령어**
```bash
# Linux
arp -a
ip neigh

# Windows
arp -a

# macOS
arp -a
```

**출력 예시**
```
? (192.168.1.1) at 00:11:22:33:44:55 [ether] on eth0
? (192.168.1.20) at aa:bb:cc:dd:ee:ff [ether] on eth0
```

**Cache Timeout**
- Linux: 기본 60~300초
- Windows: 2~10분
- 트래픽 있으면 갱신

**수동 관리**
```bash
# 엔트리 추가 (Static)
sudo arp -s 192.168.1.100 00:11:22:33:44:55

# 엔트리 삭제
sudo arp -d 192.168.1.100

# 전체 삭제
sudo ip -s neigh flush all
```

### 4.4 Gratuitous ARP

**정의**
- 자신의 IP 주소로 ARP Request 전송
- 요청자 = 대상

**목적**
1. **IP 충돌 감지**
   - 같은 IP를 사용하는 기기가 있으면 응답
2. **ARP Cache 갱신**
   - MAC 주소 변경 시 (예: NIC 교체)
   - 모든 호스트의 ARP Table 업데이트
3. **Failover**
   - 가상 IP 이동 시 (VRRP, HSRP)

**보안 문제**
- ARP Spoofing에 악용 가능

### 4.5 Proxy ARP

**시나리오**
```
PC (192.168.1.10/24, Gateway 미설정)
  |
Router (192.168.1.1 & 192.168.2.1)
  |
Server (192.168.2.100)
```

**동작**
1. PC가 192.168.2.100으로 패킷 전송 시도
2. Gateway 설정 없음 → 같은 네트워크로 착각
3. ARP Request: "192.168.2.100의 MAC은?"
4. **Router가 대신 응답**: "내 MAC으로 보내"
5. PC → Router (Router의 MAC 사용)
6. Router → Server (정상 라우팅)

**문제**
- 네트워크 설계 오류 은폐
- 보안 정책 우회 가능

**비활성화 권장**
```bash
# Linux
echo 0 > /proc/sys/net/ipv4/conf/all/proxy_arp
```

### 4.6 ARP Spoofing (공격)

**Phase 2-2에서 상세 다룸**

**기본 원리**
```
정상 상황:
PC → Gateway
ARP Table: 192.168.1.1 = AA:AA:AA:AA:AA:AA

공격:
Attacker가 Gratuitous ARP 전송:
"192.168.1.1의 MAC은 BB:BB:BB:BB:BB:BB (공격자)"

PC의 ARP Table 오염:
192.168.1.1 = BB:BB:BB:BB:BB:BB

결과:
PC → Attacker → Gateway (MITM 성공)
```

**방어**
- Static ARP Entry
- Dynamic ARP Inspection (DAI)
- ARP Spoofing 탐지 도구

---

## 5. Port Number

### 5.1 구조

**16비트 = 0 ~ 65535**

```
범위               용도
───────────────────────────────────────────────
0                예약됨 (사용 불가)
1 ~ 1023         Well-Known Ports (시스템 포트)
1024 ~ 49151     Registered Ports (사용자 포트)
49152 ~ 65535    Dynamic/Private Ports (임시 포트)
```

### 5.2 Well-Known Ports (주요)

```
포트    프로토콜        서비스
──────────────────────────────────────
20      TCP           FTP Data
21      TCP           FTP Control
22      TCP           SSH
23      TCP           Telnet
25      TCP           SMTP
53      TCP/UDP       DNS
67      UDP           DHCP Server
68      UDP           DHCP Client
69      UDP           TFTP
80      TCP           HTTP
110     TCP           POP3
123     UDP           NTP
143     TCP           IMAP
161     UDP           SNMP
162     UDP           SNMP Trap
389     TCP           LDAP
443     TCP           HTTPS
445     TCP           SMB/CIFS
514     UDP           Syslog
587     TCP           SMTP (Submission)
993     TCP           IMAPS
995     TCP           POP3S
1433    TCP           MS SQL Server
1521    TCP           Oracle DB
3306    TCP           MySQL
3389    TCP           RDP
5432    TCP           PostgreSQL
8080    TCP           HTTP Proxy
```

**확인**
```bash
# Linux
cat /etc/services | grep " 80/"

# Windows
type C:\Windows\System32\drivers\etc\services | findstr "80/"
```

### 5.3 Dynamic Ports (Ephemeral Ports)

**클라이언트 측 임시 포트**
```
OS별 범위:
- Linux (kernel 4.18+): 32768 ~ 60999
- Windows: 49152 ~ 65535
- FreeBSD: 49152 ~ 65535
```

**예시**
```
웹 브라우저 → 웹 서버

Client:
  IP:   192.168.1.100
  Port: 52341 (임시 할당)

Server:
  IP:   8.8.8.8
  Port: 80 (Well-Known)

연결 식별:
192.168.1.100:52341 ↔ 8.8.8.8:80
(Source IP:Port ↔ Dest IP:Port)

4-Tuple: (Src IP, Src Port, Dst IP, Dst Port)
→ 각 TCP 연결을 고유하게 식별
```

### 5.4 포트 확인

```bash
# 리스닝 포트 확인
# Linux
ss -tuln
netstat -tuln
lsof -i -P

# Windows
netstat -an

# 특정 포트 확인
ss -tuln | grep :80
netstat -an | findstr :80

# 프로세스까지 확인
sudo ss -tulnp
sudo netstat -tulnp
sudo lsof -i :80
```

**출력 예시**
```
Proto  Local Address    Foreign Address   State        PID/Program
tcp    0.0.0.0:22       0.0.0.0:*         LISTEN       1234/sshd
tcp    0.0.0.0:80       0.0.0.0:*         LISTEN       5678/apache2
tcp    127.0.0.1:3306   0.0.0.0:*         LISTEN       9012/mysqld
```

---

## 6. DHCP (Dynamic Host Configuration Protocol)

### 6.1 목적

**문제**
- 수동 IP 설정: 시간 소모, 오류 가능성
- 대규모 네트워크에서 비효율

**해결**
- 자동 IP 할당
- 중앙 집중 관리

### 6.2 DHCP 4-Way Handshake (DORA)

```
Client                          DHCP Server
  |                                  |
  | 1. DHCP Discover (Broadcast)    |
  |  Src: 0.0.0.0:68                |
  |  Dst: 255.255.255.255:67        |
  |  "IP 주소 주세요!"              |
  |--------------------------------->|
  |                                  |
  | 2. DHCP Offer (Broadcast/Unicast)|
  |  Src: 192.168.1.254:67          |
  |  Dst: 255.255.255.255:68        |
  |  "192.168.1.100 어때요?"        |
  |<---------------------------------|
  |                                  |
  | 3. DHCP Request (Broadcast)     |
  |  Src: 0.0.0.0:68                |
  |  Dst: 255.255.255.255:67        |
  |  "192.168.1.100 사용할게요!"    |
  |--------------------------------->|
  |                                  |
  | 4. DHCP Ack (Broadcast/Unicast) |
  |  Src: 192.168.1.254:67          |
  |  Dst: 192.168.1.100:68 or Broadcast |
  |  "확인! 사용하세요."            |
  |<---------------------------------|
  |                                  |
```

**각 단계 상세**

**1. DHCP Discover**
```
Ethernet:
  Src MAC: Client MAC
  Dst MAC: FF:FF:FF:FF:FF:FF (Broadcast)

IP:
  Src IP:  0.0.0.0 (아직 IP 없음)
  Dst IP:  255.255.255.255 (Limited Broadcast)

UDP:
  Src Port: 68 (DHCP Client)
  Dst Port: 67 (DHCP Server)

DHCP:
  Message Type: Discover
  Transaction ID: 0x12345678 (임의)
  Client MAC: AA:BB:CC:DD:EE:FF
```

**2. DHCP Offer**
```
DHCP:
  Message Type: Offer
  Transaction ID: 0x12345678 (동일)
  Your IP: 192.168.1.100 (제안 IP)
  Server IP: 192.168.1.254
  Subnet Mask: 255.255.255.0
  Gateway: 192.168.1.1
  DNS: 8.8.8.8, 8.8.4.4
  Lease Time: 86400초 (24시간)
```

**3. DHCP Request**
```
DHCP:
  Message Type: Request
  Requested IP: 192.168.1.100
  Server Identifier: 192.168.1.254
  (여러 서버가 Offer했을 때 선택)
```

**4. DHCP Ack**
```
DHCP:
  Message Type: Ack
  Your IP: 192.168.1.100
  (Offer와 동일한 정보 재전송)
```

### 6.3 DHCP Lease

**Lease Time (임대 시간)**
- 일반적: 24시간 (86400초)
- 짧게: 1시간 (이동 기기 많은 환경)
- 길게: 1주일 (고정 네트워크)

**Lease Renewal**
```
T1 (50% 시점, 12시간):
  Client → 원래 Server: DHCP Request (Unicast)
  Server → Client: DHCP Ack (갱신)

T2 (87.5% 시점, 21시간):
  (T1 실패 시)
  Client → Any Server: DHCP Request (Broadcast)
  Server → Client: DHCP Ack

Lease 만료:
  Client → 다시 DORA 과정
```

**수동 Release**
```bash
# Linux
sudo dhclient -r eth0  # Release
sudo dhclient eth0     # Renew

# Windows
ipconfig /release
ipconfig /renew
```

### 6.4 DHCP Relay Agent

**문제**
- DHCP는 Broadcast 사용
- 라우터는 Broadcast 전달 안 함
- 다른 네트워크의 DHCP 서버 사용 불가

**해결**
- DHCP Relay Agent (IP Helper)
- Broadcast → Unicast 변환

```
Client (192.168.1.0/24)
  |
  | DHCP Discover (Broadcast)
  |
Router (Relay Agent)
  |
  | DHCP Discover (Unicast to Server)
  | Gateway: 192.168.1.1 (추가)
  |
DHCP Server (10.0.0.100)
```

**설정 (Cisco)**
```cisco
interface GigabitEthernet0/0
 ip helper-address 10.0.0.100
```

### 6.5 DHCP Snooping (보안)

**DHCP Rogue Server 공격**
```
공격자가 가짜 DHCP Server 운영:
- 잘못된 Gateway 제공 → MITM
- 잘못된 DNS → 피싱
```

**DHCP Snooping 동작**
```cisco
ip dhcp snooping
ip dhcp snooping vlan 10

interface GigabitEthernet0/1
 ip dhcp snooping trust  # DHCP Server 연결 포트

interface range GigabitEthernet0/2-24
 # Untrusted (기본값)
```

**결과**
- Untrusted 포트에서 DHCP Offer/Ack 차단
- DHCP Binding Table 구축 (IP-MAC-Port 매핑)

---

## 7. NAT (Network Address Translation)

### 7.1 목적

- **IP 주소 절약**: 하나의 공인 IP로 여러 사설 IP 사용
- **보안**: 내부 네트워크 구조 은폐

### 7.2 Static NAT (1:1)

```
내부: 192.168.1.100
외부: 203.0.113.10

변환 테이블:
Inside Local      Inside Global
192.168.1.100  →  203.0.113.10

통신:
Client (192.168.1.100) → 외부 (8.8.8.8)

패킷 (NAT 전):
  Src: 192.168.1.100
  Dst: 8.8.8.8

패킷 (NAT 후):
  Src: 203.0.113.10
  Dst: 8.8.8.8

응답 (NAT 전):
  Src: 8.8.8.8
  Dst: 203.0.113.10

응답 (NAT 후):
  Src: 8.8.8.8
  Dst: 192.168.1.100
```

### 7.3 Dynamic NAT (Pool)

```
내부: 192.168.1.0/24
외부 Pool: 203.0.113.10 ~ 203.0.113.20 (11개)

최대 11개 동시 연결
```

### 7.4 PAT (Port Address Translation) = NAT Overload

**가장 일반적인 NAT**

```
내부 네트워크:
- PC-A: 192.168.1.10
- PC-B: 192.168.1.20
- PC-C: 192.168.1.30

공인 IP: 203.0.113.10 (1개)

NAT Table:
Inside              Outside
192.168.1.10:50234  203.0.113.10:50234  → 8.8.8.8:80
192.168.1.20:51023  203.0.113.10:51023  → 1.1.1.1:443
192.168.1.30:52341  203.0.113.10:52341  → 9.9.9.9:80

키: (Inside IP, Inside Port) ↔ (Outside IP, Outside Port)
```

**포트 충돌 처리**
```
PC-A: 192.168.1.10:50000 → 8.8.8.8:80
PC-B: 192.168.1.20:50000 → 1.1.1.1:80

NAT Table:
192.168.1.10:50000  203.0.113.10:50000  → 8.8.8.8:80
192.168.1.20:50000  203.0.113.10:50001  → 1.1.1.1:80
                                  ↑ 자동 변경
```

### 7.5 NAT 용어

```
Inside Local:   내부 네트워크에서 본 내부 주소 (사설 IP)
Inside Global:  외부 네트워크에서 본 내부 주소 (공인 IP)
Outside Local:  내부 네트워크에서 본 외부 주소
Outside Global: 외부 네트워크에서 본 외부 주소

일반적으로:
Outside Local = Outside Global (외부는 변환 안 함)
```

### 7.6 NAT의 문제점

**End-to-End 연결 깨짐**
- P2P 통신 어려움
- VoIP 품질 저하

**프로토콜 호환성**
- FTP Active Mode 문제
- IPsec ESP 문제

**Port Forwarding 필요**
```
외부 → 내부 서버 접근 시

포트 포워딩 설정:
203.0.113.10:80 → 192.168.1.100:80 (웹 서버)
203.0.113.10:22 → 192.168.1.101:22 (SSH)
```

---

## 8. 실습 과제

### 과제 1: 서브넷팅 계산
```
문제 1: 192.168.10.0/24를 /27로 서브넷팅
  - 서브넷 개수는?
  - 각 서브넷의 사용 가능 IP 개수는?
  - 첫 3개 서브넷의 범위는?

문제 2: IP 192.168.5.137/26
  - 네트워크 주소는?
  - 브로드캐스트 주소는?
  - 사용 가능 IP 범위는?

문제 3: 500개 호스트 네트워크 설계
  - 필요한 최소 서브넷 마스크는?
  - /23을 사용한다면 낭비되는 IP는 몇 개?
```

### 과제 2: ARP 관찰
```bash
# 1. ARP Cache 초기화
sudo ip -s neigh flush all

# 2. Ping
ping -c 1 192.168.1.1

# 3. ARP Table 확인
arp -a

# 4. Wireshark로 ARP 패킷 캡처
# Filter: arp
# Request와 Reply 구조 분석
```

### 과제 3: DHCP 과정 캡처
```bash
# 1. Wireshark 시작 (Filter: bootp or dhcp)

# 2. DHCP Release
sudo dhclient -r eth0

# 3. DHCP Renew
sudo dhclient eth0

# 4. Wireshark 분석
# - Discover, Offer, Request, Ack 확인
# - Transaction ID 동일 여부
# - 할당된 IP, Gateway, DNS 확인
```

### 과제 4: NAT 동작 확인
```bash
# 공유기 환경에서

# 1. 내부 IP 확인
ip addr show
# 또는 Windows: ipconfig

# 2. 외부 IP 확인
curl ifconfig.me
# 또는
curl icanhazip.com

# 3. 비교
# 내부 IP: 192.168.x.x (사설)
# 외부 IP: 공인 IP
# → NAT 동작 확인
```

---

## 9. 연결 포인트

### Phase 1.1: Network Architecture
→ **TCP/UDP 포트**: Well-Known Ports의 용도
→ **캡슐화**: IP 주소와 MAC 주소가 각각 L3, L2에 추가

### Phase 2.1: Scanning/Sniffing
→ **Port Scanning**: Port Number 개념 기반
→ **ARP Scan**: ARP 프로토콜 악용

### Phase 2.2: Spoofing
→ **ARP Spoofing**: ARP의 취약점 (인증 없음)
→ **IP Spoofing**: IP 주소 위조

### Phase 2.3: Session Hijacking
→ **IP/Port 4-Tuple**: 세션 식별자

### Phase 3.1: Firewall
→ **ACL**: IP 주소 및 포트 기반 필터링
→ **NAT**: 방화벽에 통합

### Phase 3.2: IDS/IPS
→ **ARP Spoofing 탐지**: ARP Table 모니터링

### Phase 4.1: Packet Analysis
→ **ARP 패킷**: Wireshark로 구조 분석
→ **DHCP 패킷**: 4-Way Handshake 관찰

---

## 10. 핵심 요약

**3계층 주소**
- MAC (L2): 48비트, 로컬 네트워크
- IP (L3): 32비트, 글로벌 라우팅
- Port (L4): 16비트, 프로세스 식별

**IP 주소**
- 서브넷팅: 큰 네트워크 분할
- CIDR: /프리픽스 표기
- 공인 vs 사설 (RFC 1918)

**ARP**
- IP → MAC 변환
- Broadcast Request, Unicast Reply
- ARP Cache 저장 (Timeout)

**DHCP**
- DORA: Discover, Offer, Request, Ack
- 자동 IP 할당
- Lease Renewal

**NAT**
- 사설 IP ↔ 공인 IP 변환
- PAT: 포트 기반 다중 변환
- IP 절약 + 보안

---

**다음 학습**: Phase 1-3 Information Security
