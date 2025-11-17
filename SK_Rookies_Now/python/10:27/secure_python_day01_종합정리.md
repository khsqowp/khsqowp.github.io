### 서론: 강의 목표 및 개요

본 강의는 단순한 파이썬 문법 학습을 넘어, **사이버 보안이라는 명확한 목표**를 가지고 프로그래밍에 접근하는 것을 목표로 합니다. 첫 시간은 아이스 브레이킹을 통해 동료들과의 유대감을 형성하고, 이후 본격적으로 보안 전문가에게 프로그래밍이 왜 필수적인 역량인지 그 이유를 심도 있게 탐구합니다. 강의 전반에 걸쳐 파이썬의 가장 기본적인 구성 요소인 **변수와 데이터 타입**을 상세히 학습하며, 각 문법 요소가 실제 **보안 업무(로그 분석, 자동화 도구 제작, 취약점 분석 등)**에서 어떻게 활용될 수 있는지에 대한 구체적인 관점을 제시합니다. 본 문서는 강의의 모든 내용을 코드 예제와 함께 상세히 기록하여, 단순한 요약을 넘어 실질적인 학습 자료가 되도록 구성되었습니다.

---

### Part 1. 보안 전문가에게 프로그래밍이란? (심화)

프로그래밍은 현대 사이버 보안의 핵심 역량입니다. 단순히 개발자의 업무라고 치부할 수 없으며, 보안 전문가는 코드를 통해 공격을 이해하고 방어를 구축하며, 반복적인 업무를 자동화합니다.

- **공격과 방어의 근간**: 대부분의 웹 해킹(예: **SQL 인젝션**, **XSS**, **CSRF**)은 결국 프로그램의 로직 허점과 입력값 조작을 통해 발생합니다. 공격자가 작성한 악성 스크립트나 조작된 데이터가 애플리케이션에 어떻게 영향을 미치는지 이해하려면, 해당 애플리케이션이 어떤 코드로 작성되었고 어떻게 동작하는지 알아야 합니다. 즉, **코드를 읽고 이해하는 능력**은 곧 위협을 분석하고 방어 전략을 수립하는 능력과 직결됩니다.

- **보안 업무의 효율성과 자동화**: 보안 업무는 방대한 양의 데이터를 다루는 반복적인 작업이 많습니다. 예를 들어, 수십만 라인의 **로그 파일을 분석**하여 특정 패턴을 찾거나, 수많은 서버의 **취약점을 주기적으로 스캔**하고, 특정 공격 패턴이 탐지되었을 때 **자동으로 IP를 차단**하는 등의 업무는 사람의 수작업만으로는 불가능에 가깝습니다. 파이썬과 같은 스크립트 언어는 이러한 반복 작업을 자동화하는 강력한 도구를 제작하는 데 사용되며, 이를 통해 보안 전문가는 더 고차원적인 위협 분석 및 대응에 집중할 수 있습니다.

- **다양한 보안 영역으로의 확장**: 파이썬은 웹 보안뿐만 아니라 **데이터 분석, 인공지능(AI), 클라우드, 시스템 포렌식** 등 다양한 분야에서 활용됩니다. 예를 들어, 머신러닝을 이용해 정상적인 로그 패턴을 학습하고, 이를 벗어나는 **이상 행위를 탐지**하는 시스템을 구축할 수 있습니다. 또한, 클라우드 환경의 보안 설정을 코드로 관리하고 검증하는 등(Infrastructure as Code), 파이썬의 활용 범위는 매우 넓습니다.

---

### Part 2. 파이썬 언어의 근본적 특징

#### 1. 컴파일 언어 vs 인터프리터 언어

- **컴파일 언어 (Java, C/C++)**: 소스코드 전체를 기계가 이해할 수 있는 파일(실행 파일)로 **미리 번역**해두는 방식입니다. 번역 과정(컴파일)이 번거롭지만, 번역된 파일은 매우 빠르게 실행됩니다. 정적 타입 언어가 대부분으로, 코드 작성 시 변수의 타입을 명확히 지정해야 합니다.

- **인터프리터 언어 (Python, JavaScript)**: 별도의 번역 과정 없이, 실행 시 코드를 **한 줄씩 실시간으로 해석**하며 동작합니다. 개발 및 수정이 편리하고 빠르지만, 실행 속도는 컴파일 언어에 비해 느립니다. 파이썬은 대표적인 인터프리터 언어이자 **동적 타입 언어**로, 변수에 값이 할당될 때 타입이 결정됩니다.

    > **보안 관점에서의 시사점**: 인터프리터 언어의 유연성은 빠른 도구 개발에 장점이지만, 개발자의 실수로 인해 데이터 타입 관련 버그가 발생하기 쉽습니다. 예를 들어, 숫자여야 할 값에 문자열이 들어가 연산 오류가 발생하는 등의 문제입니다. 따라서 파이썬 프로그래밍 시에는 항상 변수에 어떤 타입의 데이터가 담겨있는지 명확히 인지하고, 필요하다면 **타입 체크 로직을 추가**하는 습관이 매우 중요합니다.

#### 2. 변수(Variable)와 명명 규칙(Naming Convention)

변수는 데이터를 저장하기 위한 메모리 공간에 붙이는 이름입니다. 파이썬에서는 변수 선언 시 타입을 지정하지 않습니다.

- **명명 규칙 예제**
    - **`camelCase`**: 변수와 함수명에 주로 사용됩니다. `myVariableName = 10`
    - **`PascalCase`**: 클래스명에 사용됩니다. `class MySampleClass:`
    - **`snake_case`**: 파이썬 커뮤니티에서 변수 및 함수명으로 가장 널리 권장되는 방식입니다. `my_variable_name = 20`

- **예약어 확인**: 파이썬이 내부적으로 사용하는 키워드(예약어)는 변수명으로 사용할 수 없습니다. 사용 가능한 키워드는 아래 코드로 확인할 수 있습니다.

```python
import keyword

# 파이썬의 모든 예약어를 리스트로 출력
keywordList = keyword.kwlist
print(keywordList)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', ...]
```

---

### Part 3. 파이썬 핵심 데이터 타입과 예제 코드

#### 1. 기본 변수 바인딩 및 타입 확인

파이썬은 변수에 값이 할당될 때 타입이 결정됩니다. `type()` 함수를 통해 변수의 현재 데이터 타입을 확인할 수 있습니다.

```python
# 기본 변수 바인딩
year = "2025"
month = 10

# 함수 호출을 통한 출력
print(year, month)

# 변수 타입 확인을 위한 함수 - type()
print('year type - ', type(year)) # <class 'str'>

name = "김한수"
print(name, type(name)) # 김한수 <class 'str'>
```

#### 2. 숫자형 (Numeric)과 문자열 (String)

- **`int` (정수), `float` (실수)**
```python
year = 2025
score = 95.5
print(type(year))   # <class 'int'>
print(type(score))  # <class 'float'>
```

- **`str` (문자열)**: **불변성(Immutable)**을 가지며, **시퀀스** 데이터로 인덱싱/슬라이싱이 가능합니다.
```python
# 문자열 생성
name = "secure_python"

# 인덱싱 (Indexing): 특정 위치의 문자 접근
print(f"첫 번째 글자: {name[0]}") # 's'
print(f"마지막 글자: {name[-1]}") # 'n'

# 슬라이싱 (Slicing): 특정 범위의 부분 문자열 추출
print(f"0~5번째 글자: {name[0:6]}") # 'secure'
print(f"뒤에서 6글자: {name[-6:]}") # 'python'

# 불변성 확인 (값 변경 시도 시 에러 발생)
try:
    name[0] = 'S' # 첫 글자를 대문자로 바꾸려고 시도
except TypeError as e:
    print(f"문자열 변경 시도 시 에러: {e}")
# 출력: 문자열 변경 시도 시 에러: 'str' object does not support item assignment
```

- **Text Sequence 활용 예제**
```python
strTemp = 'Talk is cheap. Show me the code.'
print(strTemp, type(strTemp))

# 문자열도 시퀀스이므로 인덱싱 가능
print('indexing - ', strTemp[0]) # 'T'

# .split() 메서드로 공백 기준 분리 시 리스트(list)가 됨
listTemp = strTemp.split(' ')
print(listTemp) # ['Talk', 'is', 'cheap.', 'Show', 'me', 'the', 'code.']
print(type(listTemp)) # <class 'list'>

# 리스트가 되었으므로 인덱싱으로 마지막 단어 접근 가능
print('indexing - ', listTemp[-1]) # 'code.'

# 리스트 슬라이싱 (2칸씩 건너뛰기)
print(listTemp[0 : : 2]) # ['Talk', 'cheap.', 'me', 'code.']
```

- **문자열 슬라이싱 심화 예제**
```python
strEx = '홀짝홀짝홀짝홀짝홀짝홀짝홀짝홀짝홀짝홀짝'

# 홀수 번째 문자만 출력 (0번 인덱스부터 2칸씩)
print(strEx[::2])  # '홀홀홀홀홀홀홀홀홀홀'

# 짝수 번째 문자만 출력 (1번 인덱스부터 2칸씩)
print(strEx[1::2]) # '짝짝짝짝짝짝짝짝짝짝'
```

#### 3. 리스트 (List)

순서가 있고, 값을 추가/수정/삭제할 수 있는 **가변형(Mutable)** 시퀀스 데이터입니다.

```python
# 다양한 타입을 담을 수 있는 리스트 생성
my_list = ["apple", 100, True, ["nested", "list"]]

# 요소 접근 및 변경
print(f"첫 번째 요소: {my_list[0]}")
my_list[0] = "banana" # 값 변경 가능
print(f"변경된 첫 번째 요소: {my_list[0]}")

# 메서드를 이용한 요소 추가 및 삭제
my_list.append("new_item") # 맨 뒤에 요소 추가
print(f"추가 후: {my_list}")
my_list.pop() # 맨 뒤 요소 삭제
print(f"삭제 후: {my_list}")

# 예약어 리스트를 활용한 슬라이싱
print('slicing = ', keywordList[0:5]) # ['False', 'None', 'True', 'and', 'as']
```

#### 4. 튜플 (Tuple)

리스트와 유사하지만, 한 번 생성되면 값을 변경할 수 없는 **불변형(Immutable)** 시퀀스 데이터입니다.

```python
# 요소가 하나인 튜플 생성 시 주의점
tupleTemp = (1) 
print('type - ', type(tupleTemp)) # <class 'int'>, 튜플이 아님

tupleTemp = (1,) # 요소가 하나일 때는 반드시 쉼표(,)를 붙여야 함
print('type - ', type(tupleTemp)) # <class 'tuple'>

# 패킹(Packing): 소괄호 생략 가능
tupleTemp2 = "a","b","c"
print(tupleTemp2, type(tupleTemp2)) # ('a', 'b', 'c') <class 'tuple'>

# 언패킹(Unpacking): 튜플의 요소를 여러 변수에 나누어 담기
a, b, c = tupleTemp2
print('unpacking - ', a, b, c) # a b c

# 튜플도 시퀀스이므로 인덱싱, 슬라이싱 가능
print('indexing - ', tupleTemp2[0]) # 'a'
print('slicing - ', tupleTemp2[0:2]) # ('a', 'b')

tupleTemp3 = "a","b","c","d","e"
print('slicing - ', tupleTemp3[0 : : 2]) # ('a', 'c', 'e')

# 불변성 확인 (값 변경 시도 시 에러 발생)
try:
    tupleTemp2[0] = 'z'
except TypeError as e:
    print(f"튜플 변경 시도 시 에러: {e}")
# 출력: 튜플 변경 시도 시 에러: 'tuple' object does not support item assignment
```
> **보안 활용**: 튜플의 불변성은 프로그램 실행 중 절대 변경되어서는 안 되는 중요한 데이터를 안전하게 보관하는 데 최적입니다. (예: IP 화이트리스트, 시스템 설정값, 고정된 권한 목록 등)

#### 5. 딕셔너리 (Dictionary)

**Key-Value** 쌍으로 데이터를 저장하는 **매핑(Mapping)** 타입입니다. 순서가 없으며(최신 파이썬 버전에서는 입력 순서가 유지되기도 함), Key를 통해 값에 접근합니다. 웹 통신 데이터 형식인 **JSON**과 매우 유사하여 데이터 처리에 핵심적입니다.

```python
# 중첩된 딕셔너리와 리스트를 포함하는 복잡한 딕셔너리 예제
log = {
    'SQL Injection' : {
        "정의" : "사용자 입력을 적절히 검증하지 않고 데이터베이스 쿼리에 직접 포함하는것",
        "용어" : [
            "입력검증", "파라미터화", "블라인드", "에러기반"
        ],
        "취약 코드 예시" :"query = select * from table",
        "공격 예시" : "user = admin or 1=1",
        "탐지" : [
            "웹 취약점 스캐너 사용", "비정상적인 쿼리", "오류 모니터링"
        ]
    }
}

print(log, type(log))

# Key를 통한 값 접근 (인덱싱 불가)
print(log["SQL Injection"]["용어"], type(log["SQL Injection"]["용어"]))
# ['입력검증', '파라미터화', '블라인드', '에러기반'] <class 'list'>
```

#### 6. 셋 (Set)

**중복을 허용하지 않고**, **순서가 없는** 데이터의 집합입니다. 수학의 집합 연산이 가능합니다.

```python
# 셋 생성 (중복된 'admin'은 자동으로 제거됨)
userRoles = {"admin", "user", "guest", "admin"}
print(userRoles, type(userRoles)) # {'guest', 'user', 'admin'} <class 'set'>

# 요소 추가 (.add)
userRoles.add("user") # 이미 있는 요소라 변화 없음
print(userRoles)

# 비어있는 셋 생성 ({}는 비어있는 딕셔너리이므로 set() 함수 사용)
empSet = set()
print(dir(empSet)) # 셋 객체가 가진 메서드 목록 확인
print('type - ', type(empSet)) # <class 'set'>

# 요소 추가/삭제 메서드
empSet.add("user")
empSet.add("guest")
empSet.add("admin")
print('data - ', empSet)
empSet.discard('guest') # 요소가 없어도 에러 발생 안 함
print('data - ', empSet)
empSet.remove('admin')  # 요소가 없으면 에러 발생
print('data - ', empSet)

# 집합 연산
adminRoles = {"read", "write", "delete", "update"}
userroles = {"read", "comment"}
print('합집합 - ', adminRoles | userroles)
print('교집합 - ', adminRoles & userroles)
print('차집합 - ', adminRoles - userroles)
print('대칭 차집합 - ', adminRoles ^ userroles)
```

#### 7. 불리언 (Boolean)

`True`(참) 또는 `False`(거짓) 값을 나타냅니다. 조건문 등에서 논리적 판단의 기준으로 사용됩니다.

```python
isLoggedIn = True
print(isLoggedIn) # True

hasPermission = False
print(hasPermission) # False

# 숫자와 불리언의 관계 (True=1, False=0)
print(int(hasPermission)) # 0
```

---

### Part 4. 연산자(Operators)와 함수/메서드

- **`in` 연산자**: 특정 요소가 리스트, 튜플, 셋, 딕셔너리(키) 등에 포함되어 있는지 확인합니다.
```python
fruits = ['apple', 'banana', 'durian', 'orange']

print('orange' in fruits)  # True

# 리스트에서 in 연산자는 내부적으로 전체를 스캔할 수 있어 성능 저하의 원인이 될 수 있음
# 반면, set에서 in 연산은 해시 기반으로 매우 빠름
if 'apple' in fruits:
    print('apple 있음')
else:
    print('apple 없음')
```

- **보안 관점에서의 `set` 활용 (중복 로그인 방지 예제)**
```python
userTokens = set()

def login(token):
    if token in userTokens:
        raise ValueError(f"[보안경고] 이미 로그인중 : {token}")
    userTokens.add(token)
    print(f"{token} 로그인 성공")

login('jslim')
login('sk')

try:
    login('jslim') # 이미 로그인된 토큰으로 다시 로그인 시도
except ValueError as e:
    print(e)
```

- **함수(Function) vs 메서드(Method)**: `print()`, `len()`, `type()`처럼 독립적으로 호출되면 **함수**입니다. 반면, `my_string.split()`이나 `my_list.append()`처럼 특정 데이터(객체)에 점(`.`)을 찍어 호출되면 **메서드**입니다. 메서드는 그 객체에 종속된 기능입니다.

- **클래스(Class)와 객체(Object/Instance)**: 파이썬의 모든 데이터 타입(`int`, `str`, `list` 등)은 사실 **클래스**라는 '설계도'로 만들어져 있습니다. 우리가 `name = "python"`이라고 코드를 작성하는 순간, `str` 클래스 설계도를 바탕으로 `name`이라는 **객체(또는 인스턴스)**가 메모리에 생성되는 것입니다. `type(name)`의 결과가 `<class 'str'>`로 나오는 이유가 바로 이것입니다.

- **`dir()` 함수**: 해당 객체가 어떤 메서드와 속성(변수)들을 가지고 있는지 목록을 보여줍니다. 객체의 기능을 탐색할 때 유용합니다.
```python
my_string = "hello"
# 문자열 객체가 사용할 수 있는 모든 메서드와 속성 출력
print(dir(my_string))
# [... 'capitalize', 'center', 'count', 'endswith', 'find', 'format', 'split', ...]
```

---

### Part 5. 다양한 출력 형식과 포매팅 예제

정형화된 출력은 가독성뿐만 아니라 로그 분석 및 데이터 파싱 효율에도 큰 영향을 미칩니다.

- **기본 `print`와 `sep` 옵션**
```python
print('010' , '1234' , '5678', sep="-") # 010-1234-5678
print('kknd03255' , 'gamail.com', sep='@') # kknd03255@gamail.com
```

- **f-string (Python 3.6+ 권장)**: 가장 직관적이고 강력합니다.
```python
user = "admin"
score = 95.12345

# 기본 사용
print(f"로그인 사용자: {user}")

# 숫자 포매팅 (소수점 2자리)
print(f"점수: {score:.2f}") # 출력: 점수: 95.12

# 숫자 포맷 (천 단위 쉼표)
num = 1234567.8912
print(f"{num:,}") # 1,234,567.8912

# 정렬 및 패딩 (총 20자리 확보)
print(f"오른쪽 정렬: {num:>20.2f}")
print(f"왼쪽 정렬: {num:<20.2f}")
print(f"빈자리 0으로 채우기: {num:020.2f}")
```

- **`str.format()` 메서드**: f-string 이전 버전에서 널리 사용되었습니다.
```python
lang = 'python'
version = 3.13

# 위치 기반
print("언어: {}, 버전: {}".format(lang, version))
# 인덱스 기반
print("버전: {1}, 언어: {0}".format(lang, version))
# 이름 기반
print("언어: {a}, 버전: {b}".format(a=lang, b=version))
```

- **C-style 서식 지정 (`%`)**: 오래된 방식이며, 보안상 취약할 수 있어 사용을 권장하지 않습니다.
```python
print('language : %s, version : %.2fcm' % (lang, version))
```

- **`repr()` 함수와 이스케이프 시퀀스**: `repr()`은 `\n`과 같은 이스케이프 시퀀스를 해석하지 않고 문자열을 그대로 표현하여 디버깅에 유용합니다.
```python
data = "Hello \n Python"
print(data) # 줄바꿈이 적용되어 출력
# Hello 
#  Python

print(repr(data)) # '\n'이 문자 그대로 출력됨
# 'Hello \n Python'
```

- **형 변환 (Type Casting)**: 데이터 타입을 의도적으로 바꿀 때 사용합니다.
```python
strTemp = '100'
num_int = int(strTemp)
print(strTemp, 'type - ', type(num_int)) # 100 type -  <class 'int'>
```

- **다중 라인 문자열**: 템플릿이나 긴 쿼리문을 작성할 때 유용합니다.
```python
query = f"""select *
        from table
        where id = admin or 1=1 """
print(query)
```

---

### Part 6. 보안 관점의 로그 분석을 위한 최종 예제

강의에서 배운 `dict`와 `list`를 복합적으로 사용하여, 실제 보안 로그를 생성하고 분석하는 간단한 시나리오입니다.

```python
# 1. 개별 로그 이벤트를 딕셔너리로 정의
loginUser = {
    'type' : 'guest',
    'ip' : '192.168.0.10',
    'event' : 'LOGIN_ACCESS'
}

# 2. 여러 로그 이벤트를 리스트에 저장
logLst = []
logLst.append(loginUser)
# 동일한 로그를 한번 더 추가 (실제로는 다른 로그들이 쌓임)
logLst.append(loginUser) 

print(logLst)
# [{'type': 'guest', 'ip': '192.168.0.10', 'event': 'LOGIN_ACCESS'}, {'type': 'guest', 'ip': '192.168.0.10', 'event': 'LOGIN_ACCESS'}]

# 3. 저장된 로그를 정형화된 포맷으로 출력하여 분석
logMsg1 = f"[ALERT] User={logLst[0]['type']}, IP={logLst[0]['ip']}, event = {logLst[0]['event']}"
print(logMsg1)
# [ALERT] User=guest, IP=192.168.0.10, event = LOGIN_ACCESS

logMsg2 = f"[ALERT] User={logLst[1]['type']}, IP={logLst[1]['ip']}, event = {logLst[1]['event']}"
print(logMsg2)
# [ALERT] User=guest, IP=192.168.0.10, event = LOGIN_ACCESS
```
- **분석 관점**: 이처럼 로그를 `[{}, {}, ...]` (리스트 안의 딕셔너리들) 형태로 구조화하면, 반복문을 통해 각 로그 이벤트에 쉽게 접근할 수 있습니다. 또한, `log['ip']`와 같이 명확한 키를 사용하여 원하는 데이터만 정확히 추출하고, 이를 바탕으로 특정 IP의 활동을 추적하거나 특정 이벤트만 필터링하는 등 복잡한 분석 로직을 손쉽게 구현할 수 있습니다.
