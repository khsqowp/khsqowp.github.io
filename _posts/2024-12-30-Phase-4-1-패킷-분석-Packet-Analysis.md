---
layout: post
title: "Phase 4-1: 패킷 분석 (Packet Analysis)"
date: 2024-12-30 09:00:04 +0900
categories: [general]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 4-1: 패킷 분석 (Packet Analysis)

## 학습 목표
- Wireshark 고급 필터링 기법 습득
- 프로토콜별 패킷 구조 심층 분석
- 네트워크 문제 진단 방법론 학습
- 공격 패턴 식별 및 분석 능력 향상
- pcap 파일 분석 및 증거 수집 방법 이해

---

## 1. Wireshark 고급 필터링

### 1.1 Display Filter vs Capture Filter

**Capture Filter (Berkeley Packet Filter)**
```
캡처 시점에 적용
→ 필터링된 패킷만 저장
→ 디스크 공간 절약

문법: tcpdump 스타일

예:
host 192.168.1.100
tcp port 80
not arp

단점: 나중에 변경 불가
```

**Display Filter**
```
캡처 후 적용
→ 모든 패킷 저장
→ 표시만 필터링

문법: Wireshark 전용

예:
ip.addr == 192.168.1.100
tcp.port == 80
!(arp)

장점: 반복 분석 가능
```

### 1.2 고급 Display Filter

**논리 연산자**
```
AND: &&, and
OR:  ||, or
NOT: !, not

예:
ip.src == 192.168.1.10 && tcp.dport == 80
http || dns
!icmp
```

**비교 연산자**
```
==  같음
!=  다름
>   크다
<   작다
>=  크거나 같다
<=  작거나 같다
contains  포함
matches   정규표현식

예:
tcp.len > 1000
http.request.uri contains "admin"
http.host matches ".*\.evil\.com"
```

**필터 예시**

**HTTP POST 요청**
```
http.request.method == "POST"
```

**특정 IP 대역 제외**
```
!(ip.addr == 192.168.1.0/24)
```

**SYN 패킷만**
```
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

**재전송 패킷**
```
tcp.analysis.retransmission
```

**느린 응답 (>1초)**
```
http.time > 1
```

**SQL Injection 의심**
```
http.request.uri contains "UNION SELECT"
```

**암호화되지 않은 비밀번호**
```
http.request.method == "POST" && (http contains "password=" || http contains "pwd=")
```

### 1.3 필터 조합 예시

**웹 트래픽 분석**
```
# HTTP 트래픽 중 에러만
http.response.code >= 400

# 특정 도메인의 HTTP
http.host == "example.com"

# Cookie 포함 요청
http.cookie
```

**네트워크 문제 진단**
```
# TCP 재전송
tcp.analysis.retransmission

# TCP Window Full
tcp.analysis.window_full

# Duplicate ACK
tcp.analysis.duplicate_ack

# Out of Order
tcp.analysis.out_of_order
```

**공격 탐지**
```
# Port Scan (SYN만)
tcp.flags.syn == 1 && tcp.flags.ack == 0 && tcp.window_size < 1024

# ARP Spoofing
arp.duplicate-address-detected

# DNS Tunneling (긴 쿼리)
dns.qry.name.len > 50

# ICMP Flooding
icmp && frame.time_delta < 0.001
```

---

## 2. 프로토콜별 분석

### 2.1 TCP 분석

**3-Way Handshake 추적**
```
Filter: tcp.stream eq 0

1. SYN
   Flags: 0x002 (SYN)
   Seq: 0 (relative)
   
2. SYN+ACK
   Flags: 0x012 (SYN, ACK)
   Seq: 0
   Ack: 1
   
3. ACK
   Flags: 0x010 (ACK)
   Seq: 1
   Ack: 1
```

**연결 문제 진단**
```
증상: 연결 지연

확인:
1. SYN → SYN+ACK 시간
   - >1초: 서버 문제 또는 네트워크 지연

2. SYN+ACK → ACK 시간
   - >1초: 클라이언트 문제

3. 재전송 확인
   tcp.analysis.retransmission
   
4. Window Size
   tcp.window_size_value
   - 0: Flow Control 발동
```

**성능 분석**
```
Statistics → TCP Stream Graphs

- Time Sequence (Stevens)
  - 패킷 전송 패턴
  - 재전송 시각화

- Throughput
  - 처리량 그래프

- Round Trip Time
  - RTT 측정
  
- Window Scaling
  - 윈도우 크기 변화
```

### 2.2 HTTP 분석

**Follow HTTP Stream**
```
우클릭 → Follow → HTTP Stream

요청:
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Cookie: session=abc123

응답:
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: newsession=def456

<!DOCTYPE html>...
```

**HTTP 통계**
```
Statistics → HTTP → Requests

- 가장 많이 요청된 URL
- Response Code 분포
- Request Method 분포

활용:
- 200 OK: 정상
- 404 Not Found: 존재하지 않는 리소스
- 500 Internal Server Error: 서버 오류
- 403 Forbidden: 권한 없음
```

**객체 추출**
```
File → Export Objects → HTTP

- 이미지, 스크립트, 문서 추출
- Malware 샘플 획득 (분석용)
```

### 2.3 DNS 분석

**DNS 쿼리/응답**
```
Filter: dns

Query:
Standard query A www.example.com

Response:
Standard query response A www.example.com
Answer: 93.184.216.34
TTL: 3600
```

**DNS Tunneling 탐지**
```
Filter:
dns.qry.name.len > 50

또는:
dns && dns.flags.response == 0 && dns.qry.type == 1

확인:
- 비정상적으로 긴 도메인
- 빈번한 TXT 레코드 쿼리
- 랜덤 서브도메인
```

**DNS 통계**
```
Statistics → DNS

- 쿼리 타입 분포 (A, AAAA, MX, TXT)
- Response Code 분포
- 가장 많이 조회된 도메인
```

### 2.4 TLS/SSL 분석

**Handshake 추적**
```
Filter: tls.handshake

1. Client Hello
   - TLS Version
   - Cipher Suites
   - Extensions (SNI)

2. Server Hello
   - Selected Cipher
   - Certificate

3. Certificate
   - 서버 인증서

4. Server Key Exchange (선택)

5. Client Key Exchange
   - Pre-Master Secret (암호화됨)

6. Change Cipher Spec (양방향)

7. Encrypted Handshake Message
```

**암호화된 트래픽 복호화**
```
전제: Private Key 보유

Edit → Preferences → Protocols → TLS
→ RSA keys list
→ Add:
   IP: 192.168.1.100
   Port: 443
   Protocol: http
   Key File: /path/to/private.key

또는:
환경변수 SSLKEYLOGFILE 사용 (Firefox/Chrome)
```

**인증서 검증**
```
Packet Details → TLS → Certificate

확인:
- Issuer (발급자)
- Subject (주체)
- Validity (유효기간)
- Public Key
- Signature Algorithm
```

---

## 3. 네트워크 문제 진단

### 3.1 지연 (Latency) 분석

**RTT 측정**
```
Filter: icmp

1. Echo Request (Time: T1)
2. Echo Reply (Time: T2)

RTT = T2 - T1

Wireshark 자동 표시:
icmp.resptime
```

**TCP Handshake 지연**
```
Filter: tcp.flags.syn == 1

Time Delta:
1. SYN → SYN+ACK
2. SYN+ACK → ACK

Statistics → TCP Stream Graphs → Round Trip Time
```

**DNS 응답 시간**
```
Filter: dns

dns.time
→ 쿼리 ~ 응답 시간

정상: <100ms
느림: >500ms
```

### 3.2 패킷 손실 (Packet Loss)

**재전송 확인**
```
Filter:
tcp.analysis.retransmission

개수 확인:
Statistics → Conversations → TCP
→ Retransmission 컬럼

손실률:
재전송 / 전체 패킷 * 100
```

**Expert Info**
```
Analyze → Expert Information

Warning:
- TCP Retransmission
- TCP Out-of-Order
- TCP Dup ACK

해석:
- 많은 재전송: 패킷 손실
- Out-of-Order: 경로 변경 또는 손실
```

### 3.3 대역폭 (Bandwidth) 분석

**IO Graph**
```
Statistics → I/O Graph

설정:
- Y Axis: Bits/s
- Style: Line

분석:
- 평균 대역폭
- 피크 시간
- 급증 구간 (공격?)
```

**Conversations**
```
Statistics → Conversations → TCP

정렬: Bytes 내림차순

확인:
- 가장 많은 트래픽 사용 연결
- 비정상 대용량 전송
```

### 3.4 응용 프로그램 성능

**HTTP 응답 시간**
```
Filter: http

http.time

정상: <500ms
느림: >2초

Statistics → HTTP → Load Distribution
```

**Database Query 성능**
```
Filter: mysql || pgsql

응답 시간 확인
→ 느린 쿼리 식별
```

---

## 4. 공격 패턴 분석

### 4.1 Port Scan 탐지

**SYN Scan**
```
Filter:
tcp.flags.syn == 1 && tcp.flags.ack == 0

확인:
- 짧은 시간 내 다수 목적지 포트
- 응답: RST (Close), SYN+ACK (Open)

Statistics → Conversations → TCP
→ 단일 출발지, 다수 목적지 포트
```

**NULL/FIN/Xmas Scan**
```
# NULL Scan
tcp.flags == 0x000

# FIN Scan
tcp.flags.fin == 1 && tcp.flags.ack == 0

# Xmas Scan
tcp.flags.fin == 1 && tcp.flags.push == 1 && tcp.flags.urg == 1
```

### 4.2 ARP Spoofing 탐지

**Duplicate IP**
```
Filter:
arp.duplicate-address-detected

확인:
- 같은 IP, 다른 MAC
```

**Gratuitous ARP**
```
Filter:
arp.isgratuitous == 1

빈도 확인:
- 짧은 시간 내 반복
- 의심스러운 출발지
```

### 4.3 DDoS 공격 분석

**SYN Flooding**
```
Filter:
tcp.flags.syn == 1 && tcp.flags.ack == 0

Statistics → I/O Graph
→ SYN 패킷 급증

확인:
- 초당 수천 개 SYN
- 다양한 출발지 IP (위조)
```

**HTTP Flooding**
```
Filter:
http.request

Statistics → HTTP → Requests
→ 짧은 시간 내 대량 요청

확인:
- 동일 URI 반복
- 단일 또는 소수 출발지
```

### 4.4 Malware 통신

**C&C (Command & Control) 탐지**
```
의심 패턴:
- 주기적 비콘 (Beacon)
- 비정상 포트
- 알려진 악성 도메인/IP

Filter:
http.request.uri contains "bot" || http.request.uri contains "cmd"

또는:
dns.qry.name matches ".*[0-9]{10,}.*"
(랜덤 DGA 도메인)
```

**데이터 유출 (Exfiltration)**
```
의심 패턴:
- 대량 업로드 (외부로)
- 비정상 시간대
- 압축 파일 전송

Filter:
http.request.method == "POST" && http.content_length > 1000000

확인:
- Content-Type: application/octet-stream
- 대용량 POST
```

---

## 5. 포렌식 분석

### 5.1 증거 수집

**pcap 파일 저장**
```
File → Save As
→ Wireshark/pcapng

옵션:
- All packets
- Displayed packets only (필터 적용)
- Selected packet range
```

**타임스탬프 확인**
```
View → Time Display Format

- Seconds Since Beginning of Capture
- Date and Time of Day
- UTC Date and Time

중요: 시간 동기화 확인 (NTP)
```

**체크섬 무결성**
```
메타데이터 기록:
- 파일 크기
- MD5/SHA-256 해시

md5sum capture.pcap
sha256sum capture.pcap

→ 증거 변조 방지
```

### 5.2 스트림 재구성

**TCP Stream**
```
우클릭 → Follow → TCP Stream

활용:
- 파일 전송 내용 확인
- 채팅 기록
- 명령어 실행 로그

저장:
- Raw: 원본 바이너리
- ASCII: 텍스트
- Hex Dump: 16진수
```

**HTTP Object 추출**
```
File → Export Objects → HTTP

추출:
- 이미지, 문서
- 악성 스크립트
- 실행 파일

주의: Malware 가능성 (격리 환경)
```

### 5.3 타임라인 분석

**이벤트 순서 재구성**
```
1. 최초 연결 시간
   tcp.stream eq 0

2. 주요 활동
   - 로그인
   - 파일 접근
   - 데이터 전송

3. 의심 행위
   - 비정상 접근
   - 권한 상승

4. 종료 시간
```

**IP 추적**
```
Statistics → Endpoints → IPv4

확인:
- 연결된 모든 IP
- 송수신 데이터량
- 지리적 위치 (GeoIP)
```

---

## 6. 실습 과제

### 과제 1: HTTP 분석
```
1. Wireshark 캡처 시작
2. 웹 브라우저로 http://testphp.vulnweb.com 접속
3. 캡처 중지
4. 필터 적용: http
5. Follow HTTP Stream
6. 요청/응답 분석
```

### 과제 2: TCP 문제 진단
```
1. 캡처 파일 열기
2. 필터: tcp.analysis.flags
3. Expert Information 확인
4. 재전송 원인 분석
5. RTT 그래프 생성
```

### 과제 3: 공격 탐지
```
시나리오: Port Scan

1. Nmap 스캔 실행
   nmap -sS 192.168.1.100

2. Wireshark 캡처

3. 필터: tcp.flags.syn == 1 && tcp.flags.ack == 0

4. Statistics → Conversations
   → 단일 출발지, 다수 포트 확인
```

---

## 7. 유용한 도구

### 7.1 tshark (CLI Wireshark)

**기본 사용**
```bash
# 인터페이스 캡처
tshark -i eth0

# 파일 읽기
tshark -r capture.pcap

# 필터 적용
tshark -r capture.pcap -Y "http.request"

# 특정 필드만 출력
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.port
```

**통계**
```bash
# Protocol Hierarchy
tshark -r capture.pcap -q -z io,phs

# Conversations
tshark -r capture.pcap -q -z conv,tcp

# HTTP 통계
tshark -r capture.pcap -q -z http,tree
```

### 7.2 tcpdump

**캡처**
```bash
# 기본 캡처
sudo tcpdump -i eth0

# 파일 저장
sudo tcpdump -i eth0 -w capture.pcap

# 필터
sudo tcpdump -i eth0 'tcp port 80'

# 패킷 내용 출력
sudo tcpdump -i eth0 -X -s 0
```

### 7.3 NetworkMiner

**특징**
```
- 포렌식 도구
- 자동 파일 추출
- OS Fingerprinting
- Session 재구성

GUI 기반
Windows/Linux
```

---

## 8. 연결 포인트

### Phase 2.1: Scanning/Sniffing
→ **Wireshark**: 스니핑 도구

### Phase 2.2: Spoofing
→ **ARP Spoofing 탐지**: arp.duplicate-address-detected

### Phase 2.3: Session Hijacking
→ **Cookie 탈취 분석**: HTTP Stream

### Phase 2.4: DoS/DDoS
→ **SYN Flood 탐지**: TCP 플래그 분석

### Phase 3.2: IDS/IPS
→ **IDS 알림 검증**: 패킷 분석으로 확인

---

## 9. 핵심 요약

**필터링**
- Display Filter: 분석 시
- Capture Filter: 캡처 시 (tcpdump 문법)

**프로토콜 분석**
- TCP: Stream, RTT, Retransmission
- HTTP: Follow Stream, Object Export
- DNS: 쿼리/응답, Tunneling
- TLS: Handshake, 인증서

**문제 진단**
- 지연: RTT, Time Delta
- 손실: Retransmission, Expert Info
- 대역폭: I/O Graph, Conversations

**공격 탐지**
- Port Scan: SYN 패턴
- ARP Spoofing: Duplicate Address
- DDoS: 패킷 급증
- Malware: C&C 통신, Exfiltration

**포렌식**
- 증거 수집: pcap 저장, 해시
- 스트림 재구성: Follow TCP/HTTP
- 타임라인: 이벤트 순서

---

**다음 학습**: Phase 4-2 Network Monitoring
