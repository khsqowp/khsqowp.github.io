--- 
title: "CTF-README"
date: 2026-01-14
excerpt: ""
categories:
  - Project
  - CTF
  - FIVENINES
tags:
  - FIVENINES
  - Project
  - CTF
---

# CTF 풀이 컬렉션 - 완전 가이드

> FIVENINES 39개 웹 보안 취약점 실전 분석 및 익스플로잇

## 📖 카테고리별 가이드

### 1️⃣ [SQL Injection 완전 정복](./01-SQL-Injection-Complete.md) (9개 문제)

**난이도**: 🟢 1개 | 🟡 4개 | 🔴 4개
**학습 시간**: 약 7.5시간
**주요 기법**: Time-based Blind, Union-based, Boolean-based, INSERT Injection

**포함 문제**:
- SQL_200 - Time-based Blind SQLi와 Binary Search
- SQL_SLASH - Addslashes 우회
- SQL_MD5 - Raw MD5 Injection
- SQL_CUT - 문자열 잘림 우회
- SQL_COLUMNS - 컬럼명 유추 및 AS 별칭
- SQL_INSERT_I - 서브쿼리 인젝션
- SQL_INSERT_II - 문자열 결합 우회
- SQL_IF - IF 조건문 활용
- SQL_TIME - 자동화 스크립트 구현

---

### 2️⃣ [Code Injection 완전 정복](./02-Code-Injection-Complete.md) (9개 문제)

**난이도**: 🟢 1개 | 🟡 4개 | 🔴 4개
**학습 시간**: 약 8시간
**주요 기법**: XSS, LFI, Command Injection, Obfuscation

**포함 문제**:
- Replace - Path Traversal과 str_replace 우회
- XSS - Snort IDS 우회 (Base64, SVG)
- LFI_I - Null Byte Injection
- LFI_II - Log Poisoning
- Regular_Expression - 정규식 패턴 최소화
- Command_Injection_I - 3글자 제한 우회
- Command_Injection_II - Newline Injection
- PHP_Obfuscation - Multi-layer Deobfuscation (gzdeflate)
- JavaScript_Obfuscation - Array Rotation Obfuscation

---

### 3️⃣ [Authentication & Authorization 완전 정복](./03-Authentication-Complete.md) (7개 문제)

**난이도**: 🟢 2개 | 🟡 3개 | 🔴 2개
**학습 시간**: 약 5.5시간
**주요 기법**: Cookie Manipulation, IDOR, PHP Object Injection

**포함 문제**:
- Basic_Auth - Apache 기본 인증과 비밀번호 크래킹
- Cookie - MD5/Base64 쿠키 조작
- ADMIN_Page - UNION SELECT 데이터 위조
- Insufficient_Auth - SHA-1 토큰 권한 상승
- Process_Validation - IDOR 취약점
- Serialize_I - PHP Object Injection
- Serialize_II - 파일 읽기 체이닝 공격

---

### 4️⃣ [File System 완전 정복](./04-File-System-Complete.md) (5개 문제)

**난이도**: 🟢 2개 | 🟡 2개 | 🔴 1개
**학습 시간**: 약 3시간
**주요 기법**: Path Traversal, Directory Listing, Steganography, .htaccess Injection

**포함 문제**:
- Read_Me - 디렉토리 리스팅 취약점
- Steganography - LSB 스테가노그래피
- Download_I - Path Traversal 기본
- Download_II - str_replace 중첩 우회
- Upload_II - .htaccess 업로드 공격

---

### 5️⃣ [Logic & Misc 완전 정복](./05-Logic-Misc-Complete.md) (9개 문제)

**난이도**: 🟢 4개 | 🟡 3개 | 🔴 2개
**학습 시간**: 약 6시간
**주요 기법**: Business Logic, Brute Force, PHP extract, SQL Quine

**포함 문제**:
- Shop - 가격 파라미터 변조
- Mart - Base64 인코딩 우회
- Guessing_I - JavaScript 분석
- Guessing_II - Vim 스왑 파일
- BOT - robots.txt 정보 유출
- Proxy - HTTP 헤더 분석
- Crack_Me - Brute Force (세션 관리)
- Hack_Me - SQL Quine
- Variable - PHP extract() 취약점

---

## 🎯 학습 로드맵

### 🌱 초보자 (3-6개월)

**1단계: 기본 개념 이해 (1-2개월)**
1. **파일 시스템** (Beginner) - 가장 직관적인 시작점
   - Read_Me → Steganography
2. **Logic & Misc** (Beginner) - 비즈니스 로직 이해
   - Shop → Mart → Guessing_I → Guessing_II

**2단계: 주요 공격 기법 (2-3개월)**
3. **Authentication** (Beginner)
   - Basic_Auth → Cookie
4. **SQL Injection** (Beginner + Intermediate 일부)
   - SQL_200 → SQL_SLASH → SQL_MD5
5. **Code Injection** (Beginner)
   - Replace

**3단계: 복습 및 자동화 입문 (1개월)**
- 학습한 문제들을 자동화 스크립트로 재구현
- script Phase 1-2 병행 학습

---

### 🚀 중급자 (6-12개월)

**목표**: 모든 Intermediate 문제 완료 + 자동화 능력

**4단계: 심화 공격 기법 (3-4개월)**
1. **SQL Injection** (Intermediate + Advanced 일부)
   - SQL_CUT → SQL_COLUMNS → SQL_INSERT_I
2. **Code Injection** (Intermediate)
   - XSS → LFI_I → LFI_II → Regular_Expression
3. **Authentication** (Intermediate)
   - ADMIN_Page → Insufficient_Auth → Process_Validation
4. **File System** (Intermediate)
   - Download_I → Download_II

**5단계: 자동화 및 최적화 (2-3개월)**
- script Phase 3 학습 (자동화)
- 모든 Intermediate 문제 자동화 구현
- Burp Suite / OWASP ZAP 활용

**6단계: Advanced 입문 (1-2개월)**
- SQL_INSERT_II, SQL_IF 도전
- Command_Injection_I, Command_Injection_II
- Upload_II

---

### 💎 고급자 (지속적)

**목표**: 모든 Advanced 문제 + 커스텀 도구 개발 + 실전 적용

**7단계: 최고난이도 도전 (2-3개월)**
1. **Obfuscation**
   - PHP_Obfuscation (Multi-layer)
   - JavaScript_Obfuscation (Array Rotation)
2. **Advanced SQL**
   - SQL_TIME (완전 자동화)
   - Hack_Me (SQL Quine)
3. **Advanced PHP**
   - Serialize_I & II (Object Injection + Chaining)
   - Variable (extract 복합 취약점)

**8단계: 커스텀 도구 개발**
- script Phase 4-5 완료
- 자신만의 스캐너/익스플로잇 프레임워크 개발

**9단계: 실전 적용**
- Bug Bounty 프로그램 참여
- CTF 대회 출전
- 오픈소스 프로젝트 보안 감사

---

## 📊 전체 통계

### 문제 분포

| 카테고리 | 전체 | 🟢 Beginner | 🟡 Intermediate | 🔴 Advanced |
|---------|------|-------------|----------------|-------------|
| **SQL Injection** | 9 | 1 | 4 | 4 |
| **Code Injection** | 9 | 1 | 4 | 4 |
| **Authentication** | 7 | 2 | 3 | 2 |
| **File System** | 5 | 2 | 2 | 1 |
| **Logic & Misc** | 9 | 4 | 3 | 2 |
| **전체** | **39** | **10 (26%)** | **16 (41%)** | **13 (33%)** |

### 학습 시간

- **전체 학습 시간**: 약 30시간
- **평균 문제당**: 약 45분
- **Beginner 평균**: 25분
- **Intermediate 평균**: 45분
- **Advanced 평균**: 75분

### 주요 기술 태그 TOP 10

1. `#SQL-Injection` (9개)
2. `#Parameter-Tampering` (8개)
3. `#Path-Traversal` (6개)
4. `#Authentication-Bypass` (5개)
5. `#PHP-Vulnerabilities` (5개)
6. `#Command-Injection` (4개)
7. `#XSS` (3개)
8. `#LFI` (3개)
9. `#Obfuscation` (2개)
10. `#Steganography` (1개)

---

## 🔗 script 연동

이 CTF 풀이들은 `/script/` 디렉토리의 학습 가이드와 밀접하게 연동됩니다.

### 학습 흐름

```
이론 (script) → 실전 (CTF) → 최적화 (script) → 응용 (CTF)
```

### Phase별 매핑

**Phase 1: 환경 설정 및 기초**
- Python 기초, HTTP 통신 기본
- 도구: requests, BeautifulSoup
- 연계 CTF: Shop, Mart, Guessing_I

**Phase 2: 취약점 기초**
- SQL Injection 기본 이론
- XSS, LFI 개념
- 연계 CTF: SQL_200, XSS, LFI_I, Cookie

**Phase 3: 자동화 및 최적화**
- Brute Force 스크립트
- Binary Search 알고리즘
- 연계 CTF: SQL_TIME, Crack_Me

**Phase 4: 고급 기법**
- WAF 우회, Obfuscation 해제
- Object Injection, SQL Quine
- 연계 CTF: PHP_Obfuscation, Serialize_I, Hack_Me

**Phase 5: 커스텀 도구 개발**
- 스캐너 제작, 익스플로잇 프레임워크
- 연계: 모든 Advanced 문제

---

## 💡 사용 팁

### 1. 순차 학습 vs 자유 탐색

**순차 학습 권장 대상**:
- 웹 보안 초보자
- 체계적인 학습을 선호하는 사람
- 진도율을 추적하고 싶은 사람

**자유 탐색 권장 대상**:
- 특정 분야에 관심이 있는 사람
- 실무에서 특정 기술이 필요한 사람
- 빠른 스킬업이 필요한 사람

### 2. 효과적인 학습 방법

#### 📖 읽기 전
- [ ] 문제 제목과 힌트만 보고 접근 방법 스스로 생각하기
- [ ] 관련 script 가이드 먼저 읽기
- [ ] 필요한 도구 준비 (Burp Suite, Python 등)

#### 🛠️ 읽는 중
- [ ] 코드를 직접 타이핑하며 이해하기
- [ ] 각 단계의 WHY를 스스로 질문하기
- [ ] 실패 케이스도 직접 재현해보기

#### ✅ 읽은 후
- [ ] 스크립트를 직접 작성해보기
- [ ] 다른 방법으로도 풀 수 있는지 고민하기
- [ ] 방어 기법 섹션 꼭 읽기
- [ ] 배운 내용을 블로그나 노트에 정리하기

### 3. 막힐 때 대처법

1. **30분 규칙**: 30분 이상 막히면 힌트 섹션 읽기
2. **1시간 규칙**: 1시간 이상 막히면 풀이 1단계만 읽고 다시 시도
3. **2시간 규칙**: 2시간 이상 막히면 전체 풀이를 읽되, 반드시 나중에 처음부터 다시 풀기

### 4. 스크립트 작성 권장

**모든 문제를 자동화 스크립트로 만들어보세요!**

```python
# 예시: SQL_200 자동화 스크립트 템플릿
import requests
import time

def binary_search_blind_sqli(url, session_id):
    """Time-based Blind SQLi with Binary Search"""
    # TODO: 구현하기
    pass

if __name__ == "__main__":
    url = "https://target.com/vuln"
    session_id = "your_session"
    flag = binary_search_blind_sqli(url, session_id)
    print(f"[+] FLAG: {flag}")
```

**스크립트 작성의 장점**:
- 개념을 정확히 이해했는지 검증
- 실무에서 바로 활용 가능
- 포트폴리오 자료로 활용
- 디버깅 과정에서 추가 학습

### 5. 도구 활용

**필수 도구**:
- **Burp Suite Community**: HTTP 프록시, 요청 변조
- **Python 3.x**: 자동화 스크립트 작성
- **curl**: 빠른 HTTP 요청 테스트
- **Browser DevTools**: JavaScript 분석, 네트워크 모니터링

**추천 도구**:
- **OWASP ZAP**: 자동 스캐닝
- **sqlmap**: SQL Injection 자동화
- **John the Ripper**: 비밀번호 크래킹
- **CyberChef**: 인코딩/디코딩

---

## 🏆 진행 상황 체크리스트

### SQL Injection (9/9)
- [ ] SQL_200
- [ ] SQL_SLASH
- [ ] SQL_MD5
- [ ] SQL_CUT
- [ ] SQL_COLUMNS
- [ ] SQL_INSERT_I
- [ ] SQL_INSERT_II
- [ ] SQL_IF
- [ ] SQL_TIME

### Code Injection (9/9)
- [ ] Replace
- [ ] XSS
- [ ] LFI_I
- [ ] LFI_II
- [ ] Regular_Expression
- [ ] Command_Injection_I
- [ ] Command_Injection_II
- [ ] PHP_Obfuscation
- [ ] JavaScript_Obfuscation

### Authentication & Authorization (7/7)
- [ ] Basic_Auth
- [ ] Cookie
- [ ] ADMIN_Page
- [ ] Insufficient_Auth
- [ ] Process_Validation
- [ ] Serialize_I
- [ ] Serialize_II

### File System (5/5)
- [ ] Read_Me
- [ ] Steganography
- [ ] Download_I
- [ ] Download_II
- [ ] Upload_II

### Logic & Misc (9/9)
- [ ] Shop
- [ ] Mart
- [ ] Guessing_I
- [ ] Guessing_II
- [ ] BOT
- [ ] Proxy
- [ ] Crack_Me
- [ ] Hack_Me
- [ ] Variable

**전체 진행률**: 0/39 (0%)

---

## 🎓 다음 단계

### CTF 완료 후 추천 활동

1. **Bug Bounty 시작**
   - HackerOne, Bugcrowd 가입
   - VDP 프로그램부터 시작
   - 실제 서비스에서 취약점 찾기

2. **CTF 대회 참가**
   - PicoCTF, OverTheWire
   - DEF CON CTF Qualifier
   - 국내 대회: CODEGATE, HITCON

3. **오픈소스 기여**
   - OWASP 프로젝트 참여
   - 보안 도구 개발
   - 취약점 보고서 작성

4. **심화 학습**
   - Binary Exploitation
   - Reverse Engineering
   - Cryptography
   - Web3/Blockchain Security

---

## 📚 추가 학습 자료

### 온라인 플랫폼
- **PortSwigger Web Security Academy** (무료, 강력 추천)
- **HackTheBox** (유료/무료)
- **TryHackMe** (유료/무료)
- **PentesterLab** (유료)

### 책 추천
- "The Web Application Hacker's Handbook" - Dafydd Stuttard
- "Real-World Bug Hunting" - Peter Yaworski
- "Black Hat Python" - Justin Seitz

### 커뮤니티
- **OWASP Korea Chapter**
- **Reddit r/netsec, r/bugbounty**
- **Discord CTF 서버들**

---

## 📞 피드백 및 기여

### 오류 발견 시
- Issues 생성하여 보고
- 정확한 파일명과 라인 번호 포함

### 개선 제안
- 더 나은 풀이 방법
- 추가 설명이 필요한 부분
- 새로운 문제 제안

---

**버전**: 1.0
**마지막 업데이트**: 2026-01-14
**문제 수**: 39개
**예상 학습 기간**: 초보자 3-6개월 | 중급자 2-4개월 | 고급자 1-2개월

**🚀 지금 바로 시작하세요!**

1. 자신의 레벨에 맞는 카테고리 선택
2. 첫 번째 Beginner 문제 도전
3. 막히면 힌트 확인, 1시간 후에도 안 되면 풀이 참고
4. 반드시 스크립트로 재구현
5. 다음 문제로!

**Happy Hacking! 🎯**
