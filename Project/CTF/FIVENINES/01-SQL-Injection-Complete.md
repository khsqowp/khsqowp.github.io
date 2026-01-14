# SQL Injection 완전 정복

> 9개의 실전 문제로 배우는 SQL Injection 공격 기법

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

1. SQL_200 (Beginner) - 60분
2. SQL_SLASH (Intermediate) - 45분
3. SQL_MD5 (Intermediate) - 60분
4. SQL_CUT (Intermediate) - 45분
5. SQL_COLUMNS (Intermediate) - 30분
6. SQL_INSERT_I (Advanced) - 75분
7. SQL_INSERT_II (Advanced) - 60분
8. SQL_IF (Advanced) - 45분
9. SQL_TIME (Advanced) - 90분

### 학습 목표

이 카테고리를 완료하면:

- ✅ Time-based Blind SQLi와 Binary Search 알고리즘 구현
- ✅ 다양한 필터링 우회 기법 습득 (공백, 따옴표, 키워드)
- ✅ INSERT 문에서의 서브쿼리 주입 기법
- ✅ Boolean-based Blind SQLi 자동화 스크립트 작성
- ✅ WAF 우회 및 인코딩 기법 이해

### script 연동

**관련 Phase**: [Phase 2 - SQL Injection](/script/phase2-vulnerability-basics/02-sql-injection.md)

---

## 문제 목록

### 🟢 Beginner

#### [Hacking Log] SQL 200: 보이지 않는 데이터와의 잔혹한 스무고개

**난이도**: 🟢 Beginner
**예상 시간**: ⏱️ 60분
**주요 기술**: `#Time-based` `#Binary-Search` `#WAF-Bypass` `#Blind-SQLi`
**관련 스크립트**: [solve_sql200.py](../Scripts/solve_sql200.py)

## 1. 프롤로그: 침묵하는 서버
"스무고개"라는 제목은 로맨틱해 보이지만, 해커에게는 지옥 같은 노가다의 시작을 의미한다. **Blind SQL Injection**. 서버는 친절하게 데이터를 보여주지 않는다. 오직 "예" 혹은 "아니오"라는 단세포적인 반응만으로 거대한 데이터베이스의 지도를 그려내야 한다.

## 2. 1단계: 첫 번째 가설 - "눈으로 확인할 수 있을 것이다" (실패)
가장 먼저 사용자가 입력할 수 있는 `no` 파라미터를 분석했다. `index.phps`를 보니 `$no`가 쿼리에 직접 박힌다.

*   **실행**: 브라우저를 열고 `?no=1`을 입력해 본다. 결과가 나온다. `?no=1 AND 1=2`를 입력한다. 결과가 사라져야 정상이다.
*   **좌절**: 하지만 서버는 비웃기라도 하듯 **완벽하게 동일한 페이지**를 보여주었다.
*   **디버깅**: `curl`을 이용해 응답 바이트 수를 체크했다.
    ```bash
    $ curl -s "URL?no=1" | wc -c
    1643
    $ curl -s "URL?no=1 AND 1=2" | wc -c
    1643
    ```
    정확히 똑같다. Boolean-based 공격은 이 시점에서 폐기했다. 서버는 쿼리 결과가 있든 없든 빈 껍데기 템플릿만 반환하고 있었다.

## 3. 2단계: 두 번째 가설 - "시간은 거짓말을 하지 않는다" (실패)
눈에 보이지 않는다면 물리적인 현상을 이용해야 한다. 서버의 CPU를 잠시 멈추게 하는 `sleep()` 함수가 다음 타겟이다.

*   **실행**: `?no=1 AND sleep(3)`
*   **충격**: 결과는 `Access Denied`.
*   **분석**: 서버 전면에 강력한 WAF(웹 방화벽)가 버티고 있었다. 단순한 `curl` 요청이나 비정상적인 SQL 함수 호출을 실시간으로 감시하고 차단하는 것이었다. "아, 이 문제는 호락호락하지 않구나."라는 생각이 들었다.

## 4. 3단계: WAF와의 심리전 - "나는 정당한 유저다"
WAF는 보통 세션이 없는 익명의 공격자를 우선적으로 차단한다.
*   **해결**: 브라우저로 정식 접속하여 발급받은 `PHPSESSID` 쿠키를 가져왔다. 그리고 `User-Agent`를 실제 크롬 브라우저와 동일하게 설정했다.
*   **재검증**: `curl -H "Cookie: PHPSESSID=..." "URL?no=1 AND sleep(3)"`
*   **돌파구**: 3초... 정확히 3초 뒤에 응답이 왔다! 심장이 뛰기 시작했다. 이제 서버의 침묵을 깨뜨릴 도구를 확보했다.

## 5. 4단계: 노가다를 예술로 - 이진 탐색(Binary Search) 구현
단순히 `ascii(1, 2, 3...)`을 대입하는 방식으로는 플래그 하나를 얻는 데 며칠이 걸릴지도 모른다. 나는 이진 탐색 알고리즘을 파이썬으로 구현했다.

### 스크립트 작성 중 겪은 삽질들:
1.  **인덱스 오류**: PHP/MySQL의 `substr()`은 인덱스가 1부터 시작한다는 것을 깜빡하고 0부터 시작하게 짰다가 첫 글자가 자꾸 `?`로 나오는 현상을 겪었다.
2.  **네트워크 지연**: 가끔 인터넷이 느려지면 `sleep`이 실행되지 않았는데도 `True`로 인식되는 'False Positive' 에러가 발생했다. 이를 해결하기 위해 `sleep` 시간을 3초로 늘리고, 판정 임계값을 2.5초로 정밀하게 조정했다.

## 6. 데이터베이스 탐사 기록
1.  **데이터베이스 이름**: `database()` 함수를 한 글자씩 깎아내어 `sql_200`임을 확인했다.
2.  **테이블 목록**: `information_schema.tables`는 해커의 보물지도다. 여기서 `board`라는 미끼 테이블과 `flag`라는 진짜 목적지를 찾아냈다.
3.  **컬럼 이름**: `flag` 테이블 안에 설마 컬럼 이름도 `flag`일까? 확인해 보니 역시나 맞았다.

## 7. 최종 성공: Flag의 형체
이진 탐색 스크립트가 뿜어내는 ASCII 코드들을 문자로 변환하자, 마침내 그토록 고대하던 플래그가 모습을 드러냈다.

**FLAG**: `Th1s-15-fl@g`

## 8. 에필로그
단순한 인젝션 문제였지만, WAF의 방해와 보이지 않는 데이터라는 장벽은 나를 끊임없이 시험했다. 결국 해킹은 기술의 싸움이기도 하지만, 끝까지 포기하지 않고 가설을 수정해 나가는 인내심의 싸움이라는 것을 다시 한번 깨달았다.

---

### 🟡 Intermediate

#### [Hacking Blog] SQL SLASH: 개발자의 방심, 그 틈새를 비집고 들어가다

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 45분
**주요 기술**: `#Slash-Filter` `#Escaping` `#Parenthesis-Bypass` `#URL-Encoding`

## 1. 서론: 왜 제목이 SLASH인가?
"SQL SLASH". 제목부터 무언가 이스케이프(`\`)와 관련된 냄새가 났다. 아마도 `addslashes`나 `mysql_real_escape_string` 같은 함수가 우리를 괴롭힐 것이라 예상하며 소스 코드를 열었다.

## 2. 소스 분석: 보안의 '불균형'을 목격하다
공개된 `index.phps`는 충격적이었다.
```php
$pw = addslashes($pw);          // 비밀번호는 철저하게 따옴표를 막았다.
$id = str_replace(" ", "", $id); // 아이디는... 공백만 지우고 있다?
```
해커의 눈에는 이게 보안으로 보이지 않는다. 오히려 **"여기로 들어오세요"**라고 손짓하는 초대장 같았다. `$id` 파라미터는 따옴표(`'`)를 전혀 막지 않고 있었다. 공백만 쓰지 않으면 된다는 뜻이다.

## 3. 1차 도전: 호기로운 정면 돌파 (실패)
공백 필터링? 그까짓 거 `id=admin' OR 1=1#`으로 끝내주마... 라고 생각했다.

*   **실행**: `?id=admin' OR 1=1#&pw=guest`
*   **실패**: 결과는 에러. `str_replace`가 내 모든 공백을 지워버려 쿼리가 `user='admin'OR1=1#'`이 되어버렸다. SQL은 `OR1=1`이 하나의 문자인지 명령어인지 구분하지 못한다.

## 4. 2차 도전: 클래식한 공백 우회술 (모두 실패)
공백을 대신할 수 있는 고전적인 기술들을 총동원했다.

1.  **멀티라인 주석 (`/**/`)**: `id=admin'/**/OR/**/1=1#`
    - **결과**: `str_replace`가 주석 기호마저 공백으로 처리했는지, 아니면 WAF가 차단했는지 실패.
2.  **탭 문자 (`%09`)**: `id=admin'%09OR%091=1#`
    - **결과**: 서버 설정에 따라 `%09`를 공백으로 인식하고 지워버렸다. 실패.
3.  **개행 문자 (`%0a`)**: `id=admin'%0aOR%0a1=1#`
    - **결과**: 역시나 실패.

## 5. 3차 도전: "괄호는 공백이 필요 없다"
문득 SQL 기본 문법이 떠올랐다. `WHERE (user='admin')`은 되는데, `OR` 연산자도 괄호를 가질 수 있지 않을까?

*   **가설**: `OR(user='admin')`은 공백 없이도 `OR` 뒤에 조건이 온다는 것을 SQL 엔진에 알려줄 수 있다.
*   **검증**: `?id='or(user='admin')#`
*   **해석**: `... AND user=''OR(user='admin')#'`
*   **결과**: 여전히 실패. 왜지? 아, 주석 처리 기호인 `#`이 문제였다. URL에서 `#`은 프래그먼트로 인식되어 서버에 아예 전달되지 않는다.

## 6. 돌파구: URL 인코딩의 정수
*   **해결**: `#`을 **`%23`**으로 인코딩하여 전송했다.
*   **최종 Payload**: `?pw=guest&id='or(user='admin')%23`
*   **분석**:
    1. `'` : 앞의 `user='` 구문을 닫아버림.
    2. `or` : 앞의 조건(`pw` 불일치)을 무시함.
    3. `(user='admin')` : 강제로 `admin` 유저를 선택함. 공백이 없어도 완벽히 동작.
    4. `%23` : 뒤에 남은 쓰레기 쿼리(`'`)를 주석으로 무력화.

## 7. 최종 성공: Admin의 고백
서버가 마침내 플래그를 뱉어냈다.

**FLAG**: `92bb81b2fd434533d1b2f3a03520f7ae`

## 8. 마무리: 교훈
보안 함수 하나(`addslashes`)를 썼다고 해서 안심하는 개발자의 방심이 얼마나 무서운지 보여주는 문제였다. 또한, 공백이 막혔을 때 괄호`()`를 이용해 구문을 분리하는 테크닉은 인젝션의 기본 중의 기본임을 다시 한번 가슴에 새겼다.

---

#### [Hacker's Log] SQL MD5: 암호화 함수가 스스로 무덤을 파는 법 (Raw MD5 Injection)

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 60분
**주요 기술**: `#Raw-MD5` `#Binary-Data` `#Type-Juggling` `#Magic-String`

## 1. 개요: 암호화는 무적일까?
우리는 데이터를 보호하기 위해 해시(Hash)를 쓴다. 하지만 해시 함수의 '반환 형식' 하나 때문에 서버 전체가 뚫릴 수 있다면 믿겠는가? 이번 "SQL MD5" 문제가 바로 그 충격적인 사례다.

## 2. 코드 분석: 위험천만한 'true' 한 글자
```php
$pw = md5($pw, true);
$query = "SELECT id FROM user WHERE id = '$id' AND pw = '$pw'";
```
`md5()` 함수의 두 번째 인자가 `true`다. 이게 왜 문제일까?
- 보통 `md5("abc")`는 `900150983cd24fb0d6963f7d28e17f72` 같은 예쁜 16진수 문자열을 준다.
- 하지만 `true`를 주면 **16바이트의 끔찍한 이진(Binary) 데이터**가 나온다.
이 이진 데이터 속에는 온갖 특수문자가 섞여 있을 것이고, 그중에는 SQL 제어 문자인 `'` (따옴표)나 `or` 같은 단어가 우연히 포함될 수 있다.

## 3. 시행착오 과정: 나만의 마법을 찾아서

### 가설 1: 무차별 대입 (Brute Force) - (처참한 실패)
*   **시도**: 내 PC에서 0부터 10억까지 숫자를 대입하며 `hashlib.md5(s.encode()).digest()`를 돌려보았다.
*   **목표**: 결과물 안에 `'OR'1` (따옴표 + OR + 따옴표 + 참인 숫자) 패턴이 나오길 기대했다.
*   **결과**: 3시간 동안 CPU가 비명을 질렀지만, 조건에 딱 맞는 결과가 나오지 않았다. 해시의 바다에서 특정 문자열을 낚아채는 건 생각보다 훨씬 어려운 일이었다.

### 가설 2: 전설의 'ffifdypec' (실패)
*   **시도**: 해킹계에서 가장 유명한 Raw MD5 우회 문자열인 `ffifdypec`를 입력했다.
*   **분석**: 이 값은 해시 시 `'OR'6...` 패턴을 만든다. 이론적으로는 통과되어야 하지만, 이번 서버에서는 `Access Denied`가 떴다. 아마 서버의 DB 설정이 대소문자를 엄격히 구분하거나, `OR` 뒤의 숫자가 특정 범위 안에 있어야만 하는 특이한 설정인 것 같았다.

## 4. 돌파구: 더 정교한 매직 스트링의 발견
포기하지 않고 구글링과 보안 포럼을 뒤진 끝에, 현대적인 PHP/MySQL 환경에서 가장 성공률이 높다는 **매직 스트링**을 발견했다.
**`129581926211651571912466741651878684928`**

*   **왜 이 값인가?**: 이 거대한 숫자를 MD5 해싱하면 원시 바이트 중간에 정확히 **`'or'8`** 이라는 패턴이 박힌다.
*   **SQL 해석**:
    `WHERE id='admin' AND pw='[쓰레기데이터]'or'8[나머지쓰레기]'`
    - MySQL은 불리언 문맥에서 문자열 `'8...'`을 만나면, 맨 앞의 숫자인 **`8`**로 자동 형변환한다.
    - 0이 아닌 숫자는 무조건 **True(참)**다.
    - 결국 비밀번호가 무엇이든 `OR True` 구문에 의해 전체 조건이 참이 되어버린다!

## 5. 최종 성공: 관리자의 고백
`id`에 `admin`을, `pw`에 저 마법의 긴 숫자를 넣고 제출했다.

**FLAG**: `817e4d034f86e5abe8138a468d29a102`

## 6. 마무리: 우리가 배운 것
암호화 함수를 사용한다고 해서 모든 보안 문제가 해결되는 것은 아니다. 해시의 결과값이 쿼리문에 직접 결합(Concatenate)되는 구조 자체가 근본적인 문제다. 이를 방어하려면 반드시 **Prepared Statement**를 사용하여 데이터를 명령어와 분리하거나, 최소한 해시 결과를 **16진수 문자열**로 변환하여 안전한 문자로만 비교해야 한다.

---

#### [Hacking Tutorial] SQL CUT: 잘려나간 따옴표와 백슬래시의 반격

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 45분
**주요 기술**: `#Length-Limit` `#Backslash-Escape` `#Addslashes-Bypass` `#Logic-Order`

## 1. 개요: 보안의 두 바퀴가 충돌할 때
이번 문제는 "길이 제한"이라는 아주 흔한 보안 장치를 다룬다. 서버는 해커의 공격을 막기 위해 입력값을 10글자로 자른다. 하지만 이 단순한 로직이 `addslashes()`라는 이스케이프 함수와 만나는 순간, 상상도 못 한 거대한 취약점이 탄생한다.

## 2. 코드 정밀 해부: 재앙의 서막
제공된 의사 코드(`index.phps`)에서 가장 위험한 부분은 여기다.
```php
$id = addslashes($id);          // 1단계: 따옴표를 \'로 바꿈
if(strlen($id) > 10) $id = substr($id, 0, 10); // 2단계: 10자로 자름
$query = "select id, pw from user where id='$id' and pw='$pw'";
```
*   **문제점**: 필터링을 **먼저** 하고, 길이를 **나중에** 잰다. 이것이 모든 문제의 원흉이다.

## 3. 시행착오: 실패를 통한 가설 검증

### 시도 1: 10자 이내의 일반 인젝션 (실패)
- **입력**: `id=admin'#&pw=1` (8자)
- **결과**: `addslashes`에 의해 `admin\'#`이 되고, 쿼리는 `id='admin\'#'`이 된다. 따옴표가 안전하게 무력화되어 인젝션이 실패한다.

### 시도 2: 10자 초과 입력 (무의미)
- **입력**: `id=1234567890123`
- **결과**: `1234567890`으로 잘릴 뿐, 쿼리 구조를 바꿀 수 있는 특수문자가 전혀 없다.

## 4. 결정적 아이디어: 백슬래시를 유인하라
나의 목표는 **"백슬래시 하나만 문자열 끝에 남기는 것"**이다. 그러면 그 백슬래시가 쿼리문의 고정된 따옴표를 잡아먹어 버릴 것이기 때문이다.

*   **가설**: "9글자의 문자 + 마지막에 따옴표 하나를 넣으면 어떻게 될까?"
*   **시뮬레이션**:
    1.  **입력**: `123456789'` (정확히 10자)
    2.  **addslashes 실행**: `'`가 `\'`로 변하며 문자열은 **`123456789\'`** (총 11자)가 된다.
    3.  **substr 실행**: 앞에서부터 10자만 남기고 자른다.
        - `[1][2][3][4][5][6][7][8][9][\\]` ['] <-- 이 녀석이 잘려나간다!
    4.  **최종 변수 `$id`**: **`123456789\`** (백슬래시로 끝나는 기괴한 10자 문자열 완성)

## 5. 최종 공격 (The Exploit)
이제 이 조작된 아이디를 쿼리에 넣어보자.
*   **실행 쿼리**: `where id='123456789\' and pw='[PW]'`
*   **해커의 시점**:
    - `id` 값의 시작을 알리는 `'`가 열렸다.
    - 내 입력값 `123456789\`가 들어왔다.
    - 쿼리문에 고정되어 있던 닫는 따옴표 `'`가 내 백슬래시(`\`)에 의해 **이스케이프(`\'`)** 처리되어 버렸다!
    - 이제 SQL 엔진은 `id` 필드의 값이 `123456789' and pw=` 라는 거대한 텍스트라고 착각한다.
*   **결과**: 이제 `pw` 입력칸은 더 이상 데이터가 아니라 **실제 SQL 명령어를 마음껏 적을 수 있는 해커의 놀이터**가 되었다.

## 6. 성공 결과
- **Payload**: `?id=123456789'&pw=OR 1=1%23`
- **서버 반응**: `Hi Admin! FLAG is e9343ba7223bf50c53b61a7a31785a36`

**FLAG**: `e9343ba7223bf50c53b61a7a31785a36`

## 7. 결론: 순서의 미학
보안 로직은 단순히 존재한다고 해서 안전한 것이 아니다. "필터링 후 길이 제한"이라는 사소한 순서 실수가 어떻게 전체 시스템을 붕괴시키는지 보여준 교과서적인 문제였다. 개발자라면 반드시 "최종적으로 완성된 문자열"의 안전성을 검사해야 한다는 사실을 잊지 말아야 한다.

---

#### [Hacking Note] SQL COLUMNS: 막다른 길에서 가상의 통로를 만드는 기술

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 30분
**주요 기술**: `#Column-Injection` `#SQL-Alias` `#AS-Keyword` `#Constant-Value`

## 1. 서론: 지독하게 좁은 입구
이번 문제는 내가 조작할 수 있는 범위가 너무나 좁았다. 보통 SQL 인젝션은 `WHERE` 절을 장악하여 조건 전체를 뒤흔드는데, 이 문제는 오직 `SELECT` 뒤에 오는 **컬럼명(Column Name)** 자리만 허용했다. "길이 없다면 만들면 그만"이라는 힌트가 비장하게 느껴졌다.

## 2. 코드 분석: 성공의 유일한 조건
`index.phps`에서 확인한 로직은 매우 단순하면서도 까다로웠다.
```php
$columns = $_GET['columns'];
// 필터링: union, #, -, from, select 금지
if (preg_match("/union|#|-|from|select/i", $columns)) exit("Access Denied");

$query = "select $columns from mem";
$result = $conn->query($query);
$row = $result->fetch_assoc();

if ($row['id'] === "admin") {
    echo "FLAG is $flag";
}
```
*   **분석**: 쿼리 결과셋의 첫 번째 행에서 `id`라는 키의 값이 **정확히 "admin"**이어야 한다.
*   **난관**: 기본 링크인 `?columns=id`를 누르면 실제 DB의 첫 데이터인 `guest`가 나온다. 나는 DB 속의 실제 데이터를 'admin'으로 바꿀 수 없다.

## 3. 시행착오: 무너진 가설의 기록들

### 시도 1: 서브쿼리로 데이터 낚아채기 (실패)
*   **가설**: `columns` 자리에 `(SELECT 'admin')`을 넣으면 `id` 값이 'admin'으로 치환될 것이다.
*   **실패**: `select`라는 단어가 들어가는 순간 `Access Denied`가 떴다. 서버는 내 입에서 `select`나 `from`이 나오는 것을 원천 봉쇄하고 있었다.

### 시도 2: UNION을 이용한 행 추가 (실패)
*   **가설**: `id UNION SELECT 'admin'` 형식을 만들면 두 번째 행에 admin이 생길 것이다.
*   **실패**: `union` 키워드 역시 필터링 대상이었다.

### 시도 3: 다중 컬럼 출력 (무의미)
*   **가설**: `id,phone,name` 처럼 모든 컬럼을 다 불러오면 어딘가에 플래그가 있을 것이다.
*   **결과**: 데이터만 잔뜩 나올 뿐, 정작 `id` 값은 여전히 `guest`였다. 조건문인 `$row['id'] === "admin"`을 절대 통과할 수 없었다.

## 4. 결정적 돌파구: "존재하지 않는 것을 존재하게 하라"
필터링 목록을 다시 한번 정밀하게 살폈다.
`union`, `select`, `from`, `#`, `-`...
그런데 SQL의 핵심 기능 중 하나인 **`AS` (Alias, 별칭)**가 목록에 없었다! 그리고 싱글 쿼터(`'`)도 막혀있지 않았다.

*   **아이디어**: "실제 테이블의 컬럼을 부르는 대신, **내가 원하는 값을 담은 가상의 컬럼**을 그 자리에 끼워 넣자!"
*   **기술적 설계**: `SELECT 'admin' AS id FROM mem`
*   **동작 원리**:
    1. SQL은 테이블에 데이터가 있든 없든 `'admin'`이라는 상수 값을 출력할 수 있다.
    2. 여기에 `AS id`를 붙이면, 결과셋의 컬럼 이름이 강제로 `id`가 된다.
    3. 서버 코드는 `$row['id']`를 확인하게 되고, 그 안에는 내가 주입한 `'admin'`이 들어있게 된다.

## 5. 최종 성공 (The Exploit)
*   **Payload**: `'admin' as id`
*   **최종 쿼리**: `select 'admin' as id from mem`
*   **분석**: `mem` 테이블에 몇 개의 행이 있든 상관없이, 모든 행의 `id` 값은 `admin`으로 출력된다. 첫 번째 행을 가져오는 `fetch_assoc()`는 내가 만든 '가짜 admin'을 진짜로 믿고 플래그를 보여주었다.

**FLAG**: `4521aa07dd731d4281ae1617bccb7881`

## 6. 결론: 결과 중심의 사고
해킹은 때때로 정공법이 아닌 '사기'에 가깝다. DB를 뒤져서 정보를 찾아내는 게 아니라, 서버가 원하는 정답지를 내가 직접 인쇄해서 넘겨주는 방식이다. SQL의 별칭(Alias) 기능이 단순한 가독성 도구가 아니라, 데이터 위조의 핵심 무기가 될 수 있음을 배운 흥미로운 문제였다.

---

### 🔴 Advanced

#### [Hacking Tutorial] SQL INSERT I: 한 번의 가입으로 정보를 가로채는 서브쿼리 주입

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 75분
**주요 기술**: `#INSERT-Injection` `#Subquery` `#Information-Schema` `#Data-Exfiltration`
**관련 스크립트**: [solve_final_fixed.py](../Scripts/solve_final_fixed.py)

## 1. 개요: 저장되는 데이터의 반란
SQL 인젝션이라고 하면 흔히 `SELECT` 문의 `WHERE` 절을 조작하여 남의 정보를 훔쳐보는 것을 떠올린다. 하지만 이번 문제는 내가 나의 데이터를 저장하는 `INSERT` 문에서 시작한다. 내가 저장한 데이터가 서버를 돌아다니며 다른 중요한 정보를 낚아채 오게 만드는 것이 이번 미션의 핵심이다.

## 2. 코드 정밀 분석: 무방비한 비밀번호
제공된 `index.phps`는 아주 흥미로운 구조였다.
```php
$id = addslashes($id); // 아이디는 방어가 철저하다.
// ...
if($cmd == "register") {
    $query = "INSERT INTO mem(id,pw,ip) VALUES('$id','$pw','$ip')";
    $conn->query($query);
}
if($cmd == "login") {
    // 로그인 성공 시 내 아이디와 저장된 IP를 보여준다!
    echo("hi! $row[id]<br>ip : $row[ip]");
}
```
*   **분석**: `$pw` 파라미터는 `addslashes` 필터링을 거치지 않는다! 그리고 로그인을 하면 가입할 때 기록된 내 **IP 주소**를 다시 화면에 보여준다.
*   **전략**: "가입할 때 내 IP 대신 서버의 비밀번호(플래그)가 들어가게 조작한다면, 나중에 로그인을 하는 순간 서버가 내 눈앞에 플래그를 친절하게 출력해 줄 것이다."

## 3. 시행착오: 실패로부터 배우다

### 시도 1: UNION SELECT 연계 시도 (실패)
*   **아이디어**: `pw=1') UNION SELECT ...` 를 주입하여 데이터를 한 번에 가져오려 했다.
*   **실패**: MySQL에서 `INSERT` 문은 `UNION`과 결합할 수 없다. 쿼리 자체가 성립되지 않아 가입 자체가 안 됐다.

### 시도 2: 멀티플 인서트 (무의미)
*   **아이디어**: `pw=1'), ('admin', 'fake_pw', 'fake_ip` 를 주입하여 관리자 계정을 덮어쓰려 했다.
*   **실패**: 중복 아이디 체크 로직에 걸리거나, 서버의 데이터 삭제 로직 때문에 무의미했다.

## 4. 해결의 실마리: 서브쿼리 (Subquery)의 활용
MySQL은 `VALUES` 절 안에서 서브쿼리를 실행하는 것을 허용한다.
*   **최종 전략**: `ip` 컬럼 자리에 내가 직접 IP를 적는 대신, `(SELECT flag FROM ...)` 같은 쿼리를 넣는다.
*   **Payload 설계**:
    - `pw`에 `1', (서브쿼리)) #`를 입력한다.
    - 그러면 전체 쿼리는 `INSERT INTO mem(id,pw,ip) VALUES('myid', '1', (서브쿼리)) #', 'real_ip')`가 된다.
    - 뒷부분의 진짜 IP는 주석으로 날아간다.

## 5. 단계별 데이터 탈취 (Information Exfiltration)

### 1단계: 타겟 테이블 식별
*   `pw=1', (SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema=database())) #`
*   가입 후 로그인했더니, IP 칸에 **`mem, password_table`**이라는 이름이 떴다. 타겟은 `password_table`이다.

### 2단계: 타겟 컬럼 식별
*   `pw=1', (SELECT group_concat(column_name) FROM information_schema.columns WHERE table_name='password_table')) #`
*   로그인 후 IP 칸에 **`flag`**라는 컬럼명이 나타났다.

## 6. 최종 공격 및 성공
*   **회원가입**: `id=exfil_user&pw=1', (SELECT flag FROM password_table LIMIT 0,1)) #&cmd=register`
*   **로그인**: `id=exfil_user&pw=1`
*   **결과**: 화면에 `hi! exfil_user <br> ip : 1ns2rtsql1` 이라는 문구가 나타났다.

**FLAG**: `1ns2rtsql1`

## 7. 결론: 유출 경로의 창조
해킹에서 데이터를 가져오는 것만큼 중요한 것은 "그 데이터를 어떻게 나에게 보여주게 만들 것인가"이다. 이 문제에서는 '로그인 성공 화면'이 훌륭한 데이터 유출 통로(Exfiltration Channel)가 되었다. `INSERT` 시점에 폭탄을 설치하고 로그인 시점에 터뜨리는 이 공격 방식은 매우 강력하고 창의적인 방법임을 다시금 깨달았다.

---

#### [Write-up] SQL INSERT II: 20자의 성벽과 조각난 단어들

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 60분
**주요 기술**: `#String-Concatenation` `#SQL-Literal` `#Blacklist-Bypass` `#Comment-Techniques`

## 1. 개요: 극단적인 제약 환경
`SQL INSERT I`에서 맛본 인서트 인젝션의 연장선이지만, 난이도는 비약적으로 상승했다. 이번에는 무려 세 가지의 강력한 족쇄가 나를 기다리고 있었다.
1.  **길이 제한**: 입력값이 단 **20자**를 넘어서는 안 된다.
2.  **강력한 블랙리스트**: `admin`, `select`, `union`은 물론, 우회에 쓰일만한 `hex`, `char`, `reverse`, `concat` 등 대부분의 함수가 차단되었다.
3.  **주석 차단**: 흔히 쓰는 `#`과 `/*`가 필터링에 걸려 있었다.

## 2. 소스 코드 분석: 타겟은 lv 컬럼
제공된 `index.phps`에서 핵심 쿼리는 다음과 같았다.
```php
$query = "INSERT INTO mem VALUES('$id', $phone, 'guest')";
```
-   **취약점**: `$phone` 파라미터는 따옴표 없이 쿼리에 들어간다.
-   **목표**: 세 번째 컬럼인 `'guest'` 자리에 `'admin'`을 밀어 넣어야 한다.
-   **로그인 조건**: 쿼리 결과의 `lv` 값이 `admin`이어야만 플래그가 출력된다.

## 3. 시행착오와 가설의 붕괴

### 가설 1: 함수를 이용한 admin 생성 (실패)
가장 먼저 떠오른 건 `admin`이라는 글자를 직접 쓰지 않고 만드는 것이었다.
-   `reverse('nimda')` -> `Access Denied`. (`reverse` 함수가 블랙리스트에 있음)
-   `concat('a','dmin')` -> `Access Denied`. (`concat` 함수 역시 블랙리스트)
-   `unhex('61...')` -> `Access Denied`. (`hex` 키워드 차단에 걸림)

### 가설 2: 주석 우회 (실패와 성공의 교차)
뒤에 붙은 `,'guest')`를 떼어내기 위해 주석이 필수였다.
-   `1, 'admin') #` -> `#` 차단.
-   `1, 'admin') /*` -> `/*` 차단.
-   `1, 'admin') -- ` -> **성공!** 유일하게 하이픈 방식의 주석(`-- `)은 허용되었다.

### 가설 3: 20자의 장벽
설령 `admin`을 넣는 데 성공해도 전체 길이가 문제였다.
-   `1, 'admin')-- ` (13자) -> 단어 필터링에 걸림.
-   `1, replace('x','a','xdmin'))-- ` -> 20자가 훌쩍 넘어버림.

## 4. 결정적 돌파구: "공백은 결합이다"
MySQL의 아주 오래되고 독특한 특징 하나가 떠올랐다. **문자열 리터럴 사이에 공백이 있으면 하나의 문자열로 합쳐버린다**는 사실이다.
-   **원리**: `'a' 'b'` 는 SQL 엔진에서 `'ab'`와 완벽히 동일하게 취급된다.
-   **적용**: `'adm' 'in'` 이라고 적으면 `admin`이라는 단어를 직접 쓰지 않고도 `admin`을 만들어낼 수 있다!

## 5. 최종 공격 (The Masterpiece)
*   **Payload 구성**: `1,'adm' 'in')-- `
*   **길이**: 정확히 15자. (20자 미만 통과)
*   **필터링**: `admin`이라는 연속된 단어가 없으며, 금지된 함수도 전혀 쓰지 않았다.
*   **최종 쿼리**: `INSERT INTO mem VALUES('myid', 1, 'adm' 'in')-- , 'guest')`
    - 서버는 `lv` 컬럼에 `admin`이라는 값을 아주 정직하게 저장했다.

## 6. 결과 확인
생성된 계정으로 로그인을 시도했다.
-   **ID**: `myid` / **Phone**: `1`
-   **서버 반응**:
    ```text
    ID : myid
    Grade : admin
    FLAG is ffce2a1439efac0c0d7b5ca2c950cacf
    ```

**FLAG**: `ffce2a1439efac0c0d7b5ca2c950cacf`

## 7. 결론: 기본으로 돌아가라
모든 화려한 기법과 함수들이 막혔을 때, 나를 구원해 준 것은 SQL 표준의 아주 기초적인 문법이었다. 방어자가 아무리 많은 함수를 블랙리스트에 넣어도, 언어 자체가 가진 근본적인 특징까지 모두 막는 것은 불가능하다는 것을 보여준 아주 짜릿한 문제였다.

---

#### [Write-up] SQL IF: 보이는 것 너머의 Secret을 찾아라 (Boolean-based Blind SQLi)

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 45분
**주요 기술**: `#Boolean-Blind` `#IF-Function` `#Binary-Search` `#Hidden-Data`
**관련 스크립트**: [solve_sql_if.py](../Scripts/solve_sql_if.py)

## 1. 개요: 힌트 속에 숨겨진 힌트
이번 문제는 "SQL IF"라는 제목답게 `IF()` 함수를 이용한 인젝션을 유도한다. 웹 페이지에는 `id=1, 2, 3` 링크가 있으며, 특히 `id=3` 페이지는 다음과 같은 노골적인 정보를 흘리고 있었다.
- **Secret length**: 6
- **Columns**: id, title, description

## 2. 취약점 분석: 참과 거짓의 대화
가장 먼저 `id` 파라미터가 SQL 구문을 실행하는지 확인했다.
*   **참 테스트**: `?id=if(1=1,1,2)` -> `id=1`의 내용("IF 함수") 출력.
*   **거짓 테스트**: `?id=if(1=2,1,2)` -> `id=2`의 내용("사용예제") 출력.
*   **결론**: 서버는 `IF` 문의 조건에 따라 서로 다른 페이지를 보여준다. 전형적인 **Boolean-based Blind SQL Injection** 상황이다.

## 3. 시행착오와 탐색의 기록

### 난관 1: 데이터베이스의 정체 (실패와 분석)
비밀번호가 6글자라는 것은 알았지만, 어디에 있는지 찾아야 했다.
- **시도**: `information_schema`를 뒤져 `sql_if` 데이터베이스 내의 테이블을 모두 뽑았다.
- **결과**: `explanations`라는 테이블 하나뿐이었다. 컬럼 역시 힌트에서 준 `id, title, description` 외엔 없었다.

### 난관 2: 껍데기 뿐인 데이터? (가설 수정)
`id=3` 페이지에 이미 "Secret length: 6" 같은 힌트가 출력되고 있었기에, 처음에는 이 텍스트 자체가 데이터인 줄 알았다. 하지만 그건 6글자가 아니었다.
- **가설**: "화면에 보이는 것은 미끼일 뿐, 실제 DB 테이블 안에는 다른 값이 저장되어 있을 것이다."

## 4. 데이터 덤프: 진실을 인양하다
파이썬 스크립트를 짜서 `explanations` 테이블의 모든 컬럼 값을 한 글자씩 추출하기 시작했다. 이진 탐색을 통해 고속으로 데이터를 뽑아낸 결과, 놀라운 사실을 발견했다.

*   **Row id=3 데이터**:
    - **Title**: `Let's Try`
    - **Description**: **`s9l_1f`** (정확히 6글자!)

화면에는 "Secret length: 6..." 이라는 텍스트가 보였지만, 서버가 쿼리를 날려 가져오는 실제 데이터는 `s9l_1f`였던 것이다. 개발자가 `if($id == 3) echo "Hint...";` 같은 코드를 짜서 눈을 속이려 했지만, 인젝션 쿼리는 정직하게 DB의 속살을 보여주었다.

## 5. 최종 성공 (Exploit Execution)
추출해낸 Secret 값 `s9l_1f`를 하단 비밀번호 입력창에 넣고 제출했다.

**서버 반응**: `FLAG is 7eb36d2bb74b1b5e0d45661cc82160bb`

**FLAG**: `7eb36d2bb74b1b5e0d45661cc82160bb`

## 6. 결론: 해커는 눈이 아닌 로직을 믿는다
웹 화면에 출력되는 정보와 데이터베이스에 실제 저장된 정보가 다를 수 있음을 보여준 문제였다. 방어자가 화면에 가짜 정보를 뿌려두더라도, Blind SQL Injection을 통해 서버의 논리적 흐름(참/거짓)을 따라가면 결국 진실에 도달할 수 있다는 교훈을 얻었다.

---

#### [Hacker's Diary] SQL TIME: 응답 시간 속에 숨겨진 비밀

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 90분
**주요 기술**: `#Time-based` `#INSERT-Injection` `#SLEEP-Function` `#Automation`
**관련 스크립트**: [solve_sql_time_final.py](../Scripts/solve_sql_time_final.py)

## 1. 개요
관리자 대시보드의 연락처 입력 폼(Contact Form)에서 발생하는 SQL Injection 취약점을 이용하여 `admin_table`의 비밀번호를 알아내고 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 취약점 발견
제공된 소스 코드에서 `INSERT` 쿼리 부분을 확인했다.
```php
$query = "INSERT INTO contact (name, phone, contact) VALUES ('$name', $phone, '$contact')";
```
* `$name`과 `$contact`는 싱글 쿼터(`'`)로 감싸져 있지만, `$phone`은 감싸져 있지 않다.
* `addslashes`와 `htmlspecialchars`가 적용되어 있어 쿼터를 이용한 탈출은 어렵지만, `$phone`이 숫자형으로 처리되는 위치이므로 연산자(`AND`, `OR`)나 서브쿼리를 직접 삽입할 수 있다.

### 공격 가설
1.  **Time-based Blind SQL Injection**: 응답 결과를 직접 볼 수 없는 `INSERT` 문이므로, `SLEEP()` 함수를 이용하여 조건의 참/거짓을 응답 시간의 차이로 판별할 수 있다.
2.  **페이로드 구조**: `phone` 파라미터에 `1 AND (SELECT SLEEP(2))`와 같은 형태를 주입하여 쿼리를 지연시킨다.

## 3. 공격 실행 및 검증

### 1단계: 접근 제어 우회

제공받은 `PHPSESSID=0qc2jfrqdncj9tkf0g8hrl3042` 쿠키를 헤더에 포함하여 전송한 결과, `Access Denied`를 우회하고 페이지 소스를 읽어오는 데 성공했다.

### 3단계: 자동화 스크립트 작성 및 실행

`addslashes` 필터링을 우회하기 위해 싱글 쿼터를 사용하지 않는 `ASCII()` 및 `SUBSTR()` 방식을 채택했다. 또한 `AND` 연산자보다 확실한 지연을 위해 `phone` 필드에 직접 `SLEEP()` 시간을 주입하는 페이로드를 사용했다.

*   **최종 페이로드**: `SLEEP(IF(ASCII(SUBSTR((SELECT pw FROM admin_table LIMIT 1),{i},1))={ascii_val}, 1.2, 0))`

*   **추출 결과**:
    *   비밀번호 길이: 11
    *   비밀번호: `admin_nimda`

## 4. 결과: 관리자 권한 획득

추출한 비밀번호 `admin_nimda`로 로그인 폼을 통해 인증에 성공하고 플래그를 획득했다.

**최종 FLAG**: `53b890000076fb35405124b5b9f6ca98`

## 5. 마무리: 보안 대책

1.  **Prepared Statements 사용**: `INSERT` 문에서도 모든 파라미터를 쿼리에 직접 삽입하지 말고 Prepared Statement를 사용하여 SQL Injection을 원천 차단해야 한다. (소스 코드의 `admin_pw` 검증 부분은 이미 잘 구현되어 있으나 `contact` 저장 부분이 미흡했다.)

2.  **데이터 타입 검증**: `$phone` 변수가 숫자여야 한다면 `is_numeric()` 등을 통해 엄격히 검증해야 한다.

3.  **에러 및 시간 지연 방지**: 데이터베이스 쿼리 실행 시간에 제한을 두거나, 비정상적인 지연이 발생할 경우 모니터링하는 시스템을 구축한다.

---

## 핵심 개념 정리

### 1. Blind SQL Injection이란?

서버가 SQL 쿼리 결과를 직접 반환하지 않지만, 다른 방법으로 정보를 유출시키는 기법입니다.

#### Boolean-based Blind
```sql
' AND 1=1  -- True: 정상 응답
' AND 1=2  -- False: 다른 응답
```

응답의 차이(페이지 내용, HTTP 상태 코드, 응답 길이 등)를 통해 조건의 참/거짓을 판별합니다.

#### Time-based Blind
```sql
' AND SLEEP(3)  -- 3초 지연
' AND IF(1=1, SLEEP(3), 0)  -- 조건부 지연
```

응답 시간의 차이를 통해 조건의 참/거짓을 판별합니다.

### 2. Binary Search 알고리즘

**순차 탐색**: 최악의 경우 95번 (ASCII 32~126)
**Binary Search**: 최악의 경우 7번

```python
low, high = 32, 126
while low <= high:
    mid = (low + high) // 2
    payload = f"ASCII(SUBSTR(password, {pos}, 1)) > {mid}"

    if check(payload):  # True이면
        low = mid + 1
    else:
        high = mid - 1

char = chr(low)
```

**효율성**: O(log n) vs O(n)
**실전 예시**: 20자 비밀번호 추출 시 순차 탐색 1,900번 vs 이진 탐색 140번

### 3. 주요 SQL 함수

| 함수 | 설명 | 예시 |
|------|------|------|
| `SUBSTRING(str, pos, len)` | 부분 문자열 추출 | `SUBSTRING('admin', 1, 1)` = 'a' |
| `SUBSTR(str, pos, len)` | SUBSTRING의 별칭 | `SUBSTR('admin', 1, 1)` = 'a' |
| `ASCII(char)` | ASCII 코드 반환 | `ASCII('a')` = 97 |
| `LENGTH(str)` | 문자열 길이 | `LENGTH('admin')` = 5 |
| `SLEEP(seconds)` | 시간 지연 | `SLEEP(3)` |
| `IF(condition, true, false)` | 조건 분기 | `IF(1=1, 'yes', 'no')` = 'yes' |
| `GROUP_CONCAT(col)` | 여러 행을 하나로 결합 | `GROUP_CONCAT(table_name)` |

### 4. Information Schema 활용

#### 데이터베이스 목록
```sql
SELECT schema_name FROM information_schema.schemata
```

#### 테이블 목록
```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = database()
```

#### 컬럼 목록
```sql
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'users'
```

### 5. 필터링 우회 기법

#### 공백 우회
- 괄호: `OR(1=1)`
- 탭: `%09`
- 개행: `%0a`, `%0d`
- 주석: `/**/`

#### 따옴표 우회
- Hex 인코딩: `0x61646d696e` (admin)
- CHAR 함수: `CHAR(97,100,109,105,110)`
- 숫자 컬럼: 따옴표 불필요

#### 키워드 우회
- 대소문자: `SeLeCt`, `UnIoN`
- 인라인 주석: `SEL/**/ECT`
- Double 키워드: `SELSELECTECT`
- 문자열 결합: `'adm' 'in'` → `admin`

### 6. INSERT 문 인젝션

일반적인 SELECT 인젝션과 달리 결과를 직접 볼 수 없는 경우가 많습니다.

#### 서브쿼리 활용
```sql
INSERT INTO users (name, age, email)
VALUES ('test', 25, (SELECT flag FROM secrets))
```

#### 데이터 유출 채널 확보
1. 가입 시 서브쿼리로 플래그 삽입
2. 로그인 시 화면에 표시되는 필드 활용

---

## 방어 기법

### 1. Prepared Statements (필수)

**취약한 코드**:
```php
$query = "SELECT * FROM users WHERE id = $_GET[id]";
$result = $conn->query($query);
```

**안전한 코드**:
```php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$_GET['id']]);
$result = $stmt->fetchAll();
```

### 2. 입력값 검증

```php
// 타입 체크
if (!is_numeric($_GET['id'])) {
    die("Invalid input");
}

// 화이트리스트
$allowed = ['admin', 'user', 'guest'];
if (!in_array($_GET['role'], $allowed)) {
    die("Invalid role");
}

// 길이 제한 (정규식)
if (!preg_match('/^[a-zA-Z0-9]{3,20}$/', $_GET['username'])) {
    die("Invalid username format");
}
```

### 3. 최소 권한 원칙

```sql
-- 웹 애플리케이션 전용 계정 생성
CREATE USER 'webapp'@'localhost' IDENTIFIED BY 'password';

-- SELECT, INSERT, UPDATE만 허용
GRANT SELECT, INSERT, UPDATE ON database.* TO 'webapp'@'localhost';

-- DROP, CREATE 등 위험한 권한은 부여하지 않음
-- REVOKE ALL PRIVILEGES ON database.* FROM 'webapp'@'localhost';
```

### 4. 에러 메시지 숨김

```php
// 프로덕션 환경
ini_set('display_errors', 0);
error_reporting(0);

// 개발 환경에서만 에러 표시
if (ENVIRONMENT === 'development') {
    ini_set('display_errors', 1);
    error_reporting(E_ALL);
}
```

```python
# Python/Flask
app.config['DEBUG'] = False
app.config['TESTING'] = False
```

### 5. WAF (Web Application Firewall) 도입

- **ModSecurity**: 오픈소스 WAF
  ```apache
  SecRule ARGS "@rx (union|select|insert|update|delete)" \
      "id:1,phase:2,deny,status:403,msg:'SQL Injection Attempt'"
  ```

- **Cloudflare**: 클라우드 기반 보호
- **AWS WAF**: AWS 환경용

### 6. 시간 지연 모니터링

```php
// 쿼리 실행 시간 제한
$start = microtime(true);
$result = $conn->query($query);
$duration = microtime(true) - $start;

if ($duration > 2.0) {  // 2초 이상 걸리면
    log_security_event("Suspicious query detected", [
        'duration' => $duration,
        'query' => $query,
        'ip' => $_SERVER['REMOTE_ADDR']
    ]);
}
```

### 7. ORM 사용 (권장)

```python
# Django ORM (안전)
User.objects.filter(username=username, password=password)

# SQLAlchemy (안전)
session.query(User).filter_by(username=username, password=password).first()

# Raw SQL (위험)
cursor.execute(f"SELECT * FROM users WHERE username='{username}'")  # 절대 금지!
```

---

## 참고 자료

- **OWASP**: [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- **PortSwigger**: [SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- **script 가이드**: [Phase 2 - SQL Injection](/script/phase2-vulnerability-basics/02-sql-injection.md)
- **HackTricks**: [SQL Injection](https://book.hacktricks.xyz/pentesting-web/sql-injection)
- **PayloadsAllTheThings**: [SQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)

---

**문제 수**: 9개
**난이도 분포**: Beginner 1개 | Intermediate 4개 | Advanced 4개
**총 학습 시간**: 약 8-10시간
**마지막 업데이트**: 2026-01-14
