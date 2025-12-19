---
layout: post
title: "Phase 1-3: 정보보안 기초 (Information Security Basics)"
date: 2024-12-30 09:00:01 +0900
categories: [network, security]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 1-3: 정보보안 기초 (Information Security Basics)

## 학습 목표
- CIA Triad (기밀성, 무결성, 가용성) 완전 이해
- 대칭키/비대칭키 암호화의 차이와 활용 방법 습득
- 해시 함수의 특성과 무결성 검증 원리 파악
- 인증(Authentication)과 인가(Authorization) 구분
- SSL/TLS의 동작 원리와 보안 통신 이해

---

## 1. 정보보안의 3요소 (CIA Triad)

### 1.1 Confidentiality (기밀성)

**정의**
- 인가되지 않은 사용자의 정보 접근 차단
- "보아서는 안 될 사람이 보지 못하게"

**위협**
- 도청 (Eavesdropping)
- 스니핑 (Sniffing)
- 소셜 엔지니어링

**대응 방법**
```
암호화 (Encryption)
  - 데이터 암호화: 파일, 디스크, 데이터베이스
  - 통신 암호화: HTTPS, VPN, SSH

접근 제어 (Access Control)
  - 인증: 사용자 신원 확인
  - 인가: 권한 부여
  - 최소 권한 원칙 (Principle of Least Privilege)

물리적 보안
  - 출입 통제
  - 화면 필터
  - 문서 파쇄
```

**예시**
```
위반 사례:
- 평문 HTTP로 로그인 정보 전송
- 암호화되지 않은 USB 분실
- 공용 WiFi에서 중요 정보 전송

올바른 예:
- HTTPS 사용
- 디스크 암호화 (BitLocker, LUKS)
- VPN 사용
```

### 1.2 Integrity (무결성)

**정의**
- 데이터가 무단으로 변경되지 않음을 보장
- "허가되지 않은 수정 방지"

**위협**
- MITM (Man-In-The-Middle) 공격
- 데이터 변조
- 악성코드

**대응 방법**
```
해시 함수 (Hash Function)
  - 파일 무결성 검증 (MD5, SHA-256)
  - 디지털 서명

체크섬 (Checksum)
  - TCP Checksum
  - CRC (Cyclic Redundancy Check)

버전 관리
  - Git, SVN
  - 변경 이력 추적

백업
  - 정기 백업
  - 스냅샷
```

**예시**
```
위반 사례:
- ARP Spoofing으로 패킷 변조
- 악성코드가 시스템 파일 수정
- SQL Injection으로 DB 수정

올바른 예:
- 파일 다운로드 시 SHA-256 해시 검증
  $ sha256sum ubuntu.iso
  $ compare with official hash

- Git Commit Hash
  $ git log
  commit abc123... (각 커밋이 해시로 검증)

- 디지털 서명
  소프트웨어 서명 검증 (Code Signing)
```

### 1.3 Availability (가용성)

**정의**
- 필요할 때 정보에 접근 가능
- "필요한 때에 사용할 수 있어야"

**위협**
- DoS/DDoS 공격
- 랜섬웨어
- 하드웨어 고장
- 자연 재해

**대응 방법**
```
이중화 (Redundancy)
  - 서버 이중화 (Active-Standby, Active-Active)
  - 네트워크 이중화 (이중 회선)
  - 전원 이중화 (UPS, 발전기)

백업
  - 3-2-1 규칙:
    - 3개의 복사본
    - 2종류의 미디어
    - 1개는 오프사이트

확장성 (Scalability)
  - 로드 밸런싱
  - 오토 스케일링 (Auto Scaling)

DDoS 방어
  - Rate Limiting
  - Anti-DDoS 솔루션
  - CDN (Cloudflare, Akamai)

재해 복구 (Disaster Recovery)
  - DR 센터
  - RPO (Recovery Point Objective)
  - RTO (Recovery Time Objective)
```

**예시**
```
위반 사례:
- DDoS 공격으로 웹사이트 다운
- 랜섬웨어로 데이터 암호화
- 단일 서버 장애로 서비스 중단

올바른 예:
- 웹 서버 3대 + 로드 밸런서
- 매일 백업 + 주간 오프사이트 백업
- CloudFront CDN으로 DDoS 완화
```

### 1.4 추가 보안 원칙

**Non-Repudiation (부인 방지)**
- 행위를 부인할 수 없음
- 디지털 서명, 로그 기록

**Authentication (인증)**
- 사용자 신원 확인
- 3가지 방식:
  - Something you know (비밀번호)
  - Something you have (OTP, 스마트카드)
  - Something you are (지문, 홍채)

**Authorization (인가)**
- 권한 부여
- RBAC (Role-Based Access Control)
- ACL (Access Control List)

---

## 2. 암호화 기초 (Cryptography)

### 2.1 암호화의 목적

```
평문 (Plaintext) → [암호화] → 암호문 (Ciphertext) → [복호화] → 평문

목적:
1. 기밀성: 제3자가 읽을 수 없음
2. 무결성: 변조 탐지 (MAC, 서명)
3. 인증: 송신자 신원 확인
```

### 2.2 대칭키 암호화 (Symmetric Encryption)

**특징**
- 암호화 키 = 복호화 키
- 빠름 (하드웨어 가속 가능)
- 키 배포 문제 (Key Distribution Problem)

**동작**
```
Alice                             Bob
  |                                 |
  | [공유 비밀키: K]                 | [공유 비밀키: K]
  |                                 |
  | 평문: "Hello"                   |
  | 암호화(평문, K) → 암호문: "X7@2" |
  |--------------------------------->|
  |                                 | 복호화(암호문, K) → "Hello"
```

**주요 알고리즘**

**DES (Data Encryption Standard)**
- 키 길이: 56비트 (너무 짧음)
- 블록 크기: 64비트
- 현재: 취약 (Brute-force 가능)
- 사용 금지

**3DES (Triple DES)**
- DES를 3번 적용
- 키 길이: 168비트 (실제 112비트)
- 느림
- 레거시 시스템에서 사용

**AES (Advanced Encryption Standard)**
- 현재 표준
- 키 길이: 128, 192, 256비트
- 블록 크기: 128비트
- 매우 빠르고 안전
- 사용 예: WiFi (WPA2/3), VPN, 디스크 암호화

**암호화 모드**
```
ECB (Electronic Codebook)
  - 블록별 독립 암호화
  - 패턴 노출 (취약)
  - 사용 금지

CBC (Cipher Block Chaining)
  - 이전 블록과 XOR
  - IV (Initialization Vector) 필요
  - 일반적 사용

CTR (Counter)
  - 스트림 암호처럼 동작
  - 병렬 처리 가능
  - 빠름

GCM (Galois/Counter Mode)
  - CTR + 인증 (AEAD)
  - TLS 1.3에서 권장
  - 현대적 선택
```

**사용 예시**
```bash
# OpenSSL로 파일 암호화 (AES-256-CBC)
openssl enc -aes-256-cbc -salt -in file.txt -out file.enc
# 비밀번호 입력

# 복호화
openssl enc -aes-256-cbc -d -in file.enc -out file.txt

# 키 파일 사용
openssl enc -aes-256-cbc -in file.txt -out file.enc -K $(openssl rand -hex 32) -iv $(openssl rand -hex 16)
```

### 2.3 비대칭키 암호화 (Asymmetric Encryption)

**특징**
- 공개키 (Public Key) + 개인키 (Private Key)
- 느림 (대칭키 대비 100~1000배)
- 키 배포 문제 해결
- 디지털 서명 가능

**원리**
```
공개키로 암호화 → 개인키로만 복호화 (암호화)
개인키로 서명 → 공개키로 검증 (서명)
```

**동작 (암호화)**
```
Alice                                   Bob
  |                                       |
  |                        [공개키 Pub-B] |
  |<--------------------------------------|
  |                                       | [개인키 Pri-B] (비밀)
  | 평문: "Hello"                         |
  | 암호화(평문, Pub-B) → 암호문          |
  |-------------------------------------->|
  |                                       | 복호화(암호문, Pri-B) → "Hello"
  |                                       | (개인키로만 복호화 가능!)
```

**동작 (서명)**
```
Alice                                   Bob
  |                                       |
  | [개인키 Pri-A] (비밀)                  |
  | 문서: "Contract"                      |
  | 서명 = Sign(Hash(문서), Pri-A)        |
  |                                       |
  | [문서 + 서명 + 공개키 Pub-A] --------->|
  |                                       |
  |                                       | Verify(Hash(문서), 서명, Pub-A)
  |                                       | → True (Alice가 서명함)
```

**주요 알고리즘**

**RSA (Rivest-Shamir-Adleman)**
- 가장 널리 사용
- 키 길이: 2048, 3072, 4096비트
- 용도: 암호화, 서명
- 소인수분해 문제 기반
- 느림

**DSA (Digital Signature Algorithm)**
- 서명 전용
- 키 길이: 1024, 2048, 3072비트
- 미국 정부 표준 (FIPS)

**ECC (Elliptic Curve Cryptography)**
- 타원곡선 기반
- 작은 키로 높은 보안 (256비트 ECC ≈ 3072비트 RSA)
- 빠름, 효율적
- ECDSA (서명), ECDH (키 교환)
- 현대적 선택 (모바일, IoT)

**사용 예시**
```bash
# RSA 키 쌍 생성
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem

# 공개키로 암호화
openssl rsautl -encrypt -pubin -inkey public.pem -in file.txt -out file.enc

# 개인키로 복호화
openssl rsautl -decrypt -inkey private.pem -in file.enc -out file.txt

# 서명 생성
openssl dgst -sha256 -sign private.pem -out signature.bin file.txt

# 서명 검증
openssl dgst -sha256 -verify public.pem -signature signature.bin file.txt
```

### 2.4 하이브리드 암호화

**실전 사용**
- 대칭키의 속도 + 비대칭키의 키 분배 해결
- TLS/SSL, PGP, SSH 등에서 사용

**과정**
```
1. 세션키 생성 (대칭키, 임의)
   - 예: AES-256 키 (32바이트)

2. 세션키를 수신자 공개키로 암호화
   - RSA(세션키, 공개키) → 암호화된 세션키

3. 실제 데이터는 세션키로 암호화
   - AES(데이터, 세션키) → 암호화된 데이터

4. 전송
   - 암호화된 세션키 + 암호화된 데이터

5. 수신자
   - 개인키로 세션키 복호화
   - 세션키로 데이터 복호화
```

**장점**
- 빠름 (대부분 대칭키 사용)
- 안전한 키 교환 (비대칭키)
- 각 세션마다 새 세션키 (Forward Secrecy)

---

## 3. 해시 함수 (Hash Function)

### 3.1 정의와 특성

**해시 함수**
```
입력 (임의 길이) → Hash Function → 출력 (고정 길이)

예:
"Hello World" → SHA-256 → a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```

**특성**
```
1. 결정적 (Deterministic)
   - 같은 입력 → 항상 같은 출력

2. 빠른 계산
   - 해시 계산이 빠름

3. 일방향 (One-way)
   - 출력 → 입력 계산 불가능
   - "Preimage Resistance"

4. 눈사태 효과 (Avalanche Effect)
   - 입력 1비트만 변경 → 출력 완전히 변경
   - "Hello" vs "hello" → 완전히 다른 해시

5. 충돌 저항성 (Collision Resistance)
   - 같은 출력을 내는 2개 입력 찾기 어려움
```

### 3.2 주요 해시 알고리즘

**MD5 (Message Digest 5)**
- 출력: 128비트 (32자리 16진수)
- 상태: 취약 (충돌 발견)
- 용도: 레거시, 파일 무결성 (비보안)
- 사용 금지 (보안 목적)

**SHA-1 (Secure Hash Algorithm 1)**
- 출력: 160비트 (40자리 16진수)
- 상태: 취약 (2017년 충돌 성공)
- 용도: Git (역사적), 레거시
- 사용 금지 (보안 목적)

**SHA-256 (SHA-2 family)**
- 출력: 256비트 (64자리 16진수)
- 상태: 안전 (현재 표준)
- 용도: 파일 무결성, 블록체인, 인증서
- **권장**

**SHA-512**
- 출력: 512비트 (128자리 16진수)
- 더 높은 보안

**SHA-3**
- 2015년 표준화
- 다른 구조 (Keccak)
- SHA-2와 함께 사용

### 3.3 해시 활용

**파일 무결성 검증**
```bash
# SHA-256 해시 계산
sha256sum ubuntu-22.04.iso
# 출력: a1b2c3d4...

# 공식 웹사이트의 해시와 비교
# 일치 → 파일 무변조
# 불일치 → 파일 손상 또는 변조

# 여러 파일
sha256sum *.iso > checksums.txt
sha256sum -c checksums.txt
```

**비밀번호 저장**
```
잘못된 방법:
DB에 평문 저장 → DB 탈취 시 즉시 노출

올바른 방법:
1. 사용자 등록:
   비밀번호 "mypassword123"
   → Hash("mypassword123") → "a1b2c3..."
   → DB에 "a1b2c3..." 저장

2. 로그인:
   입력 비밀번호 "mypassword123"
   → Hash("mypassword123") → "a1b2c3..."
   → DB의 해시와 비교 → 일치하면 인증

3. DB 탈취되어도:
   해시만 노출 → 원본 비밀번호 알 수 없음
   (Rainbow Table 공격 대비: Salt 사용)
```

**Salt & Pepper**
```
Salt (공개된 임의값):
Hash(비밀번호 + Salt)

예:
사용자1: Hash("password123" + "random123") → 해시1
사용자2: Hash("password123" + "xyz789")   → 해시2
→ 같은 비밀번호도 다른 해시

Pepper (비공개 고정값):
Hash(비밀번호 + Salt + Pepper)
→ DB 탈취되어도 Pepper 모름
```

**HMAC (Hash-based Message Authentication Code)**
```
HMAC(메시지, 비밀키) = Hash(비밀키 + 메시지)

용도:
- 메시지 무결성 + 인증
- API 요청 서명
- JWT 토큰

예:
Client → Server: 메시지 + HMAC(메시지, SharedKey)
Server: HMAC 재계산 → 비교 → 검증
```

### 3.4 해시 실습

```bash
# 문자열 해시
echo -n "Hello World" | sha256sum
# a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

echo -n "hello world" | sha256sum
# b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
# → 완전히 다름 (대소문자 1글자 차이)

# 파일 해시
sha256sum file.txt

# MD5 (비교용)
md5sum file.txt

# 모든 알고리즘
openssl dgst -md5 file.txt
openssl dgst -sha1 file.txt
openssl dgst -sha256 file.txt
openssl dgst -sha512 file.txt
```

---

## 4. 디지털 인증서와 PKI

### 4.1 디지털 인증서 (Digital Certificate)

**문제**
- 공개키를 받았는데 진짜 Alice의 공개키인가?
- MITM이 자신의 공개키를 Alice라고 속일 수 있음

**해결**
- 신뢰할 수 있는 제3자 (CA)가 보증
- 디지털 인증서 발급

**인증서 구조 (X.509)**
```
인증서 내용:
  - 버전: v3
  - 일련번호: 12345678
  - 서명 알고리즘: RSA-SHA256
  - 발급자 (Issuer): DigiCert
  - 유효기간: 2024-01-01 ~ 2025-01-01
  - 주체 (Subject): CN=example.com
  - 공개키: [RSA 2048-bit Public Key]
  - 확장: SAN (Subject Alternative Names)

CA의 서명:
  Hash(인증서 내용) → CA 개인키로 서명
```

**검증 과정**
```
1. 서버가 인증서 제시
2. 브라우저가 CA 공개키로 서명 검증
   - CA 공개키는 OS/브라우저에 사전 설치
3. 서명 유효 → 공개키 신뢰
4. 공개키로 통신 시작
```

### 4.2 PKI (Public Key Infrastructure)

**구성 요소**
```
CA (Certificate Authority)
  - 인증서 발급
  - 예: DigiCert, Let's Encrypt

RA (Registration Authority)
  - 신원 확인
  - CA의 대리인

인증서 저장소
  - LDAP, DB

CRL (Certificate Revocation List)
  - 폐기된 인증서 목록

OCSP (Online Certificate Status Protocol)
  - 실시간 인증서 상태 확인
```

**인증서 체인**
```
Root CA
  └─ Intermediate CA
       └─ End-Entity Certificate (example.com)

검증:
1. example.com 인증서 확인
2. Intermediate CA가 서명했는지 확인
3. Intermediate CA 인증서 확인
4. Root CA가 서명했는지 확인
5. Root CA는 신뢰됨 (OS에 사전 설치)
```

**인증서 확인**
```bash
# 웹사이트 인증서 확인
openssl s_client -connect example.com:443 -showcerts

# 인증서 파일 내용 확인
openssl x509 -in cert.pem -text -noout

# 유효기간 확인
openssl x509 -in cert.pem -noout -dates

# 발급자/주체 확인
openssl x509 -in cert.pem -noout -issuer -subject
```

---

## 5. SSL/TLS 프로토콜

### 5.1 개요

**SSL (Secure Sockets Layer)**
- Netscape가 개발 (1994)
- SSL 3.0까지 개발
- 현재 사용 금지 (취약점)

**TLS (Transport Layer Security)**
- SSL의 후속 표준 (IETF)
- TLS 1.0 (1999) = SSL 3.1
- TLS 1.1 (2006)
- TLS 1.2 (2008) ← 현재 주로 사용
- TLS 1.3 (2018) ← 최신 권장

**용도**
- HTTPS (HTTP over TLS)
- SMTPS, IMAPS, FTPS
- VPN (OpenVPN)

### 5.2 TLS Handshake (TLS 1.2)

```
Client                                Server
  |                                     |
  | 1. ClientHello                      |
  |   - TLS 버전: 1.2                   |
  |   - Cipher Suites 목록              |
  |   - Random Nonce                    |
  |------------------------------------>|
  |                                     |
  |              2. ServerHello         |
  |                - TLS 버전: 1.2      |
  |                - 선택 Cipher Suite  |
  |                - Random Nonce       |
  |                                     |
  |              3. Certificate         |
  |                - 서버 인증서        |
  |                                     |
  |              4. ServerKeyExchange   |
  |                (필요시)              |
  |                                     |
  |              5. ServerHelloDone     |
  |<------------------------------------|
  |                                     |
  | 6. ClientKeyExchange                |
  |   - Pre-Master Secret (암호화)      |
  |                                     |
  | 7. ChangeCipherSpec                 |
  |   (이후 암호화 통신 시작)            |
  |                                     |
  | 8. Finished (암호화됨)              |
  |------------------------------------>|
  |                                     |
  |         9. ChangeCipherSpec         |
  |         10. Finished (암호화됨)     |
  |<------------------------------------|
  |                                     |
  | [암호화된 Application Data 전송]    |
  |<----------------------------------->|
```

**Cipher Suite 예시**
```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

분석:
- TLS: 프로토콜
- ECDHE: 키 교환 (Elliptic Curve Diffie-Hellman Ephemeral)
- RSA: 인증 (서버 인증서)
- AES_256_GCM: 대칭키 암호화 (데이터)
- SHA384: 해시 함수 (무결성)
```

**세션키 생성**
```
1. Client Random (ClientHello)
2. Server Random (ServerHello)
3. Pre-Master Secret (Client → Server, RSA 암호화)

Master Secret = PRF(Pre-Master Secret, "master secret", Client Random + Server Random)

Session Keys = PRF(Master Secret, ...)
  - Client Write Key (Client → Server 암호화)
  - Server Write Key (Server → Client 암호화)
  - Client MAC Key (Client → Server 무결성)
  - Server MAC Key (Server → Client 무결성)
```

### 5.3 TLS 1.3 개선사항

**1-RTT Handshake**
```
Client                      Server
  |                           |
  | ClientHello + KeyShare    |
  |-------------------------->|
  |                           |
  | ServerHello + KeyShare    |
  | Certificate               |
  | Finished                  |
  |<--------------------------|
  |                           |
  | Finished                  |
  |-------------------------->|
  |                           |
  | [Application Data]        |
  |<------------------------->|

→ 1 RTT만에 암호화 시작 (TLS 1.2는 2 RTT)
```

**제거된 기능**
- RSA 키 교환 제거 (Forward Secrecy 보장)
- 취약한 Cipher Suite 제거 (RC4, 3DES, MD5, SHA-1)
- 정적 DH 제거

**필수 기능**
- AEAD (AES-GCM, ChaCha20-Poly1305)
- Perfect Forward Secrecy (ECDHE만 사용)

### 5.4 HTTPS 확인

```bash
# TLS 버전 확인
openssl s_client -connect example.com:443 -tls1_2
openssl s_client -connect example.com:443 -tls1_3

# Cipher Suite 확인
nmap --script ssl-enum-ciphers -p 443 example.com

# 인증서 체인 확인
openssl s_client -connect example.com:443 -showcerts
```

**브라우저에서**
- 주소창 자물쇠 클릭
- "연결이 안전함" → 인증서 보기
- 발급자, 유효기간, 공개키, 서명 확인

---

## 6. 인증과 인가

### 6.1 Authentication (인증)

**정의**
- "너는 누구인가?"
- 사용자 신원 확인

**3가지 요소**
```
1. Something You Know (지식 기반)
   - 비밀번호
   - PIN
   - 보안 질문

2. Something You Have (소유 기반)
   - OTP (One-Time Password)
   - 스마트카드
   - USB 토큰
   - 휴대폰 (SMS)

3. Something You Are (생체 기반)
   - 지문
   - 홍채
   - 얼굴 인식
   - 음성 인식
```

**Multi-Factor Authentication (MFA)**
```
2개 이상 요소 조합:

2FA 예시:
1. 비밀번호 (지식)
2. OTP (소유)

→ 비밀번호 탈취되어도 OTP 없으면 로그인 불가
```

**인증 프로토콜**
```
HTTP Basic Auth:
  Authorization: Basic base64(username:password)
  → 평문 (Base64는 인코딩)
  → HTTPS 필수

HTTP Digest Auth:
  Challenge-Response
  비밀번호 해시 전송

OAuth 2.0:
  제3자 인증 (Google, Facebook 로그인)

SAML:
  기업용 SSO (Single Sign-On)

Kerberos:
  티켓 기반 인증
```

### 6.2 Authorization (인가)

**정의**
- "무엇을 할 수 있는가?"
- 권한 부여

**모델**

**RBAC (Role-Based Access Control)**
```
사용자 → 역할 → 권한

예:
- Alice → Admin → Read/Write/Delete
- Bob → User → Read/Write
- Charlie → Guest → Read
```

**ABAC (Attribute-Based Access Control)**
```
속성 기반:
- 부서, 직급, 위치, 시간 등

예:
"부서=영업 AND 직급=팀장 AND 시간=근무시간"
→ 영업 데이터 접근 허용
```

**ACL (Access Control List)**
```
파일별 권한:
file.txt:
  - Alice: Read, Write
  - Bob: Read
  - Group_Admins: Full Control
```

---

## 7. 실습 과제

### 과제 1: 해시 실습
```bash
# 1. 문자열 해시 비교
echo -n "password" | sha256sum
echo -n "Password" | sha256sum
# 결과 비교 (완전히 다름)

# 2. 파일 무결성 검증
sha256sum /etc/passwd > passwd.hash
# 파일 수정
sha256sum -c passwd.hash
# 실패 확인

# 3. 비밀번호 해시 + Salt 시뮬레이션
SALT=$(openssl rand -hex 16)
echo -n "mypassword$SALT" | sha256sum
# 매번 다른 SALT → 다른 해시
```

### 과제 2: 대칭키 암호화
```bash
# 1. 파일 암호화
openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.enc
# 비밀번호: test123

# 2. 복호화 (올바른 비밀번호)
openssl enc -aes-256-cbc -d -in encrypted.enc -out decrypted.txt
# 비밀번호: test123

# 3. 복호화 (잘못된 비밀번호)
openssl enc -aes-256-cbc -d -in encrypted.enc -out failed.txt
# 비밀번호: wrong
# 실패 확인
```

### 과제 3: 비대칭키 암호화
```bash
# 1. RSA 키 쌍 생성
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem

# 2. 공개키로 암호화
echo "Secret Message" > message.txt
openssl rsautl -encrypt -pubin -inkey public.pem -in message.txt -out message.enc

# 3. 개인키로 복호화
openssl rsautl -decrypt -inkey private.pem -in message.enc

# 4. 다른 키로 복호화 시도 (실패 확인)
openssl genrsa -out wrong_private.pem 2048
openssl rsautl -decrypt -inkey wrong_private.pem -in message.enc
```

### 과제 4: HTTPS 인증서 확인
```bash
# 1. 인증서 다운로드
openssl s_client -connect google.com:443 -showcerts > google_cert.pem

# 2. 인증서 내용 확인
openssl x509 -in google_cert.pem -text -noout

# 확인 사항:
# - Issuer (발급자)
# - Subject (주체, CN=*.google.com)
# - Validity (유효기간)
# - Public Key (공개키)
# - Signature Algorithm

# 3. 유효기간 확인
openssl x509 -in google_cert.pem -noout -dates
```

---

## 8. 연결 포인트

### Phase 1.1: Network Architecture
→ **TLS/SSL**: Application Layer (L7) 보안

### Phase 2.2: Spoofing
→ **ARP Spoofing**: 인증 없는 프로토콜의 취약점
→ **HTTPS**: MITM 방어

### Phase 2.3: Session Hijacking
→ **암호화**: Session ID 탈취 방지
→ **HTTPS**: Cookie Secure 플래그

### Phase 3.1: Firewall
→ **암호화 트래픽**: Deep Inspection 어려움

### Phase 3.2: IDS/IPS
→ **SSL/TLS Decryption**: 암호화 트래픽 검사

### Phase 4.1: Packet Analysis
→ **Wireshark**: TLS Handshake 분석
→ **암호화**: 페이로드 읽을 수 없음

---

## 9. 핵심 요약

**CIA Triad**
- Confidentiality (기밀성): 암호화
- Integrity (무결성): 해시, 서명
- Availability (가용성): 이중화, 백업

**암호화**
- 대칭키: 빠름, 같은 키 (AES)
- 비대칭키: 느림, 키 쌍 (RSA, ECC)
- 하이브리드: 실전 사용 (TLS)

**해시**
- 일방향, 고정 길이
- 무결성 검증
- SHA-256 권장

**TLS**
- Handshake: 인증서 교환, 키 생성
- 세션키: 대칭키 암호화
- TLS 1.3 권장

**인증 vs 인가**
- Authentication: 신원 확인 (누구?)
- Authorization: 권한 부여 (무엇?)

---

**다음 학습**: Phase 2 공격 기법으로 진입

**Phase 1 완료!** 네트워크 기초 → 주소 체계 → 정보보안 기초
