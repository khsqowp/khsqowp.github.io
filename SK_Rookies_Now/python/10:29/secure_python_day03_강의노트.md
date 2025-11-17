# 📝 파이썬 강의 노트 (3일차): 제어문, 반복문, 그리고 날짜 다루기

오늘 3일차 강의에서는 파이썬 프로그래밍의 핵심적인 로직을 구성하는 **제어문**과 **반복문**에 대해 깊이 있게 배웠다. 또한, 데이터 분석이나 로그 처리 시 필수적인 **날짜와 시간 다루는 법**까지 학습했다. 강사님께서 실제 현업에서 마주할 수 있는 문제와 보안적 관점까지 짚어주셔서 더욱 유익한 시간이었다.

### 📚 1. 어제 학습 내용 복습: 단어 빈도수 계산 코드 개선

오늘 강의는 어제 마지막에 다루었던 **단어 빈도수 계산** 문제를 복습하며 시작했다. `set`을 사용해 중복을 제거하는 아이디어는 좋았지만, `set`은 **순서를 보장하지 않는다**는 특징 때문에 잠재적인 버그가 발생할 수 있다는 점을 강사님께서 지적해주셨다.

> **💡 중요!**
> `set`은 순서가 없기 때문에, 두 개의 `set`을 각각 만들어 `zip`으로 묶을 경우, 각 `set`의 순서가 달라져 데이터가 잘못 매핑될 위험이 있습니다. 예를 들어, `zip(set1, set2)`를 할 때 `set1`의 첫 번째 요소와 `set2`의 첫 번째 요소가 원래 같은 쌍이라는 보장이 없습니다.

이를 해결하기 위한 몇 가지 개선된 코드를 배웠다.

#### 1-1. `sorted()` 함수로 순서 보장하기

가장 직관적인 해결책은 `set`으로 중복을 제거한 뒤, `sorted()` 함수를 사용해 **알파벳 순으로 정렬**하는 것이다. 이렇게 하면 언제나 동일한 순서가 보장되므로, 키와 값의 순서가 꼬일 일이 없다.

```python
wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk', 'sk']

# 1. set으로 중복을 제거하고 sorted로 정렬하여 순서를 보장한다.
unique_words = sorted(set(wordLst))

# 2. 정렬된 리스트를 기준으로 빈도수를 계산한다.
freq = [wordLst.count(word) for word in unique_words]

# 3. 순서가 보장된 두 리스트를 zip으로 묶어 딕셔너리를 생성한다.
result = dict(zip(unique_words, freq))

print(result)
# 출력: {'cat': 4, 'cs': 2, 'dog': 3, 'sk': 2, 'word': 1}
```

#### 1-2. `collections.Counter` 활용하기

파이썬의 기본 라이브러리인 `collections` 모듈의 `Counter` 클래스를 사용하면 단어 빈도수를 훨씬 간결하게 계산할 수 있다.

> **📌 노트:** `Counter`는 리스트와 같은 반복 가능한(iterable) 객체를 인자로 받아, 각 요소의 개수를 세어 딕셔너리처럼 생긴 `Counter` 객체로 반환해줍니다. 현업에서도 매우 유용하게 쓰인다고 강사님께서 강조하셨다.

```python
from collections import Counter

wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk', 'sk']

# Counter 객체에 리스트를 전달하기만 하면 자동으로 빈도수를 계산해준다.
result = dict(Counter(wordLst))

print(result)
# 출력: {'dog': 3, 'cat': 4, 'word': 1, 'cs': 2, 'sk': 2}
```

#### 1-3. `dict.fromkeys()` 활용하기

딕셔너리의 `fromkeys()` 메소드를 사용하는 방법도 있다. 이 방법은 리스트의 중복을 제거하여 키로 사용하고, 각 키에 대한 값을 리스트 컴프리헨션으로 계산하여 채워 넣는다.

```python
wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk', 'sk']

# 1. dict.fromkeys(wordLst)는 {'dog': None, 'cat': None, ...} 와 같이 중복이 제거된 딕셔너리를 생성한다.
# 2. 이 딕셔너리의 키들을 순회하며 원래 리스트에서 각 키(단어)의 개수를 센다.
result = {key: wordLst.count(key) for key in dict.fromkeys(wordLst)}

print(result)
# 출력: {'dog': 3, 'cat': 4, 'word': 1, 'cs': 2, 'sk': 2}
```

---

### 🎯 2. 오늘의 학습 목표

- **분기문 (`if`)**: 조건에 따라 코드의 실행 흐름을 나누는 방법
- **반복문 (`for`, `while`)**: 특정 코드를 여러 번 실행하는 방법
- **연산자**: 다양한 계산과 비교를 수행하는 기호
- **함수**: 코드의 재사용성을 높이는 방법 (내일 더 자세히 다룰 예정)
- **날짜/시간 다루기**: `datetime` 모듈 사용법

---

### 🔀 3. 제어 구문 (Control Flow)

#### 3-1. 왜 제어 구문이 필요한가?

프로그래밍은 단순히 코드를 위에서 아래로 순차적으로 실행하는 것만으로 끝나지 않는다.
- **상황에 따른 다른 처리**: 예를 들어, 로그 분석 시 'ERROR' 로그와 'INFO' 로그는 다르게 처리해야 한다.
- **반복적인 작업 자동화**: 수천, 수만 건의 데이터를 처리할 때, 각 데이터를 동일한 방식으로 처리해야 한다.

이처럼 **프로그램의 실행 흐름을 제어**하기 위해 **분기문(`if`)**과 **반복문(`for`, `while`)**이 반드시 필요하다.

#### 3-2. 분기문 `if`

`if`문은 주어진 **조건(Condition)**이 참(`True`)인지 거짓(`False`)인지에 따라 코드 블록을 선택적으로 실행한다.

- **기본 구조**:
  - `if`: 조건이 참일 때 실행
  - `elif`: 이전 `if` 또는 `elif` 조건이 거짓일 때, 새로운 조건을 검사
  - `else`: 위의 모든 조건이 거짓일 때 실행

- **조건식**:
  - `True` 또는 `False` 같은 **불리언(Boolean)** 값
  - 비교 연산자(`>`, `<`, `==`, `!=`)나 논리 연산자(`and`, `or`)를 포함한 **표현식**
  - **Truthy & Falsy**: 파이썬에서는 `True`/`False`가 아니더라도 조건식으로 평가될 수 있다.
    - **Falsy**: `False`, 숫자 `0`, 빈 문자열 `""`, 빈 리스트 `[]`, 빈 딕셔너리 `{}` 등
    - **Truthy**: Falsy가 아닌 모든 값

- **블록과 들여쓰기**:
  - 파이썬은 다른 언어의 `{}` (중괄호) 대신 **콜론(`:`)**과 **들여쓰기(Indentation)**로 코드 블록을 구분한다.
  - 들여쓰기는 보통 공백 4칸을 사용하며, 코드의 가독성과 구조에 매우 중요하다.

##### `input()` 함수와 사용자 입력 처리

`input()` 함수는 사용자로부터 콘솔을 통해 직접 값을 입력받을 수 있게 해준다.

```python
# input() 함수는 모든 입력을 문자열(str)로 받는다.
score_str = input('점수를 입력하세요 : ')

# 따라서 숫자 계산을 위해서는 반드시 숫자형(int, float)으로 형변환(casting)이 필요하다.
score = int(score_str)

print('입력받은 점수의 타입: ', type(score))

if score >= 60 :
    print('Pass')
else :
    print('None Pass')
```

> #### 🔐 보안 노트: `input()` 사용 시 주의점
>
> `input()`으로 받은 값을 `int()`로 변환할 때, 만약 사용자가 숫자가 아닌 문자(예: "abc")를 입력하면 `ValueError`가 발생하여 프로그램이 비정상적으로 종료될 수 있다.
>
> - **취약점**: 악의적인 사용자가 의도적으로 잘못된 타입의 입력을 주어 시스템을 중단시키는 **서비스 거부(Denial of Service)** 공격의 빌미가 될 수 있다.
> - **대응**: 사용자 입력을 항상 **신뢰하지 않고 검증(Validation)**하는 습관이 중요하다. `try-except` 구문을 사용해 예외 처리를 하거나, 입력값이 숫자로만 구성되었는지(`isdigit()`) 미리 확인하는 로직이 필요하다.

##### 중첩 `if`문과 다중 조건 처리

`if`문 안에 또 다른 `if`문을 사용하여 더 복잡한 조건을 처리할 수 있다.

```python
# 점수에 따라 학점을 부여하는 예제 (A+, A-, B+, B- 등)
score = int(input('점수를 입력하세요 : '))

if score >= 90 :
    if score >= 95 :
        print('A+')
    else :
        print('A-')
elif score >= 80 :
    if score >= 85 :
        print('B+')
    else :
        print('B-')
elif score >= 70 :
    if score >= 75 :
        print('C+')
    else :
        print('C-')
else :
    print('F')
```

> **📌 노트:** 강사님께서는 `if`문 중첩이 너무 깊어지면 코드를 이해하기 어려워지고(가독성 저하), 나중에 수정하기도 힘들어지므로(유지보수성 저하) 가급적 지양하는 것이 좋다고 하셨다. 복잡한 조건은 함수로 분리하거나 다른 방식으로 구조화하는 것을 고민해봐야 한다.

##### `if ... in` 구문

특정 값이 리스트, 튜플, 딕셔너리 등 **열거형(iterable) 자료** 안에 포함되어 있는지 확인할 때 매우 유용하다.

```python
# 리스트(List)에서 값 확인하기
areas = ['서울', '경기', '인천', '부산']
region = input('지역을 입력하세요 : ')

if region in areas :
    print(f'"{region}" 지역은 서비스 대상입니다.')
else :
    print(f'"{region}" 지역은 대상이 아닙니다.')

# 딕셔너리(Dictionary)에서 키(key) 확인하기
# 'in' 연산자는 딕셔너리에 사용할 경우 기본적으로 '키'의 존재 여부를 확인한다.
dictTmp = {'melon' : 100, 'bravo' : 200, 'bibibig' : 300}
target = 'banana'

if target in dictTmp :
    print(f'{target}의 가격은 {dictTmp[target]}원 입니다.')
else :
    print(f'"{target}"는 메뉴에 없습니다.')
```

---

### 🧮 4. 연산자 (Operators)

- **산술 연산자**: `+`, `-`, `*`, `/`, `%`(나머지), `**`(거듭제곱)
- **비교 연산자**: `==`(같다), `!=`(다르다), `>`, `<`, `>=`, `<=`
- **논리 연산자**: `and`(논리 곱), `or`(논리 합)

> **💡 중요! `or` vs `|`**
>
> - `or`: **논리 연산자**. `a or b`에서 `a`가 Truthy이면 `a`를, 아니면 `b`를 반환한다.
> - `|`: **비트 연산자**. 숫자를 2진수로 바꾼 뒤, 각 비트를 OR 연산한다.
>
> 두 연산자는 완전히 다르게 동작하므로, 논리적인 조건을 연결할 때는 반드시 `and`, `or` 키워드를 사용해야 한다.

##### 퀴즈: 윤년 계산기 만들기

- **요구사항**: 연도를 입력받아 윤년인지 평년인지 판단하기
- **윤년 조건**: 4의 배수**이면서** 100의 배수가 아니**거나**, 400의 배수일 때

```python
year = int(input("연도를 입력하세요 : "))

# 조건식을 괄호로 묶어 우선순위를 명확히 해주는 것이 가독성에 좋다.
is_leap_year = ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

if is_leap_year:
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 평년입니다.")

# 3항 연산자를 사용하면 더 간결하게 표현할 수 있다.
# print(f"{year}은(는) {'윤년' if is_leap_year else '평년'}입니다.")
```

> #### 🔐 보안 노트: 윤년 계산기의 입력값 검증
>
> 위 코드 역시 사용자가 숫자가 아닌 값을 입력하면 `ValueError`가 발생한다. 또한, **음수 연도**나 비정상적으로 큰 숫자를 입력하는 경우에 대한 처리가 없다. 실제 서비스라면 이런 **엣지 케이스(Edge Case)**에 대한 유효성 검사를 반드시 추가해야 한다.

---

### 📅 5. 날짜 및 시간 다루기 (`datetime`)

로그 분석, 데이터 처리 등에서 날짜와 시간 정보는 매우 중요하다. 파이썬에서는 `datetime` 기본 모듈을 통해 날짜와 시간을 쉽게 다룰 수 있다.

#### 5-1. `import`의 이해

- `import 모듈`: 모듈 전체를 가져온다. 모듈 안의 함수를 사용하려면 `모듈이름.함수이름()` 형태로 접근해야 한다.
- `from 모듈 import 함수/클래스`: 모듈에서 특정 함수나 클래스만 가져온다. `함수이름()` 형태로 바로 사용할 수 있다.
- **패키지(Package)**: 여러 모듈을 디렉토리 구조로 묶어놓은 것. `from 패키지.모듈 import 함수` 형태로 복잡한 구조도 가져올 수 있다.

#### 5-2. `date`와 `datetime` 객체

- `from datetime import date, datetime`
- `date`: **날짜**(연, 월, 일) 정보만 다룬다.
- `datetime`: **날짜와 시간**(연, 월, 일, 시, 분, 초) 정보를 모두 다룬다.

```python
from datetime import date, datetime

# 오늘 날짜 가져오기
today_date = date.today()
print(f"date 객체: {today_date}")
print(f"연: {today_date.year}, 월: {today_date.month}, 일: {today_date.day}")

# 현재 날짜와 시간 가져오기
today_datetime = datetime.today()
print(f"datetime 객체: {today_datetime}")
print(f"시: {today_datetime.hour}, 분: {today_datetime.minute}, 초: {today_datetime.second}")
```

#### 5-3. 날짜 연산: `timedelta`와 `relativedelta`

날짜에 단순히 숫자를 더하거나 뺄 수는 없다. 날짜/시간 간의 **차이**를 표현하는 별도의 객체를 사용해야 한다.

- `timedelta`: **일(days), 초(seconds), 마이크로초(microseconds)** 등 비교적 짧은 시간 간격을 더하거나 뺄 때 사용한다.
- `relativedelta`: `dateutil` 라이브러리에 포함되어 있으며, **년(years), 월(months)** 단위의 복잡한 연산이 가능하다. (`pip install python-dateutil` 필요)

```python
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

today = date.today()
print(f"오늘: {today}")

# 1일 더하기 (timedelta 사용)
day_delta = timedelta(days=1)
print(f"내일: {today + day_delta}")

# 1년 1개월 1일 더하기 (relativedelta 사용)
year_delta = relativedelta(years=1)
month_delta = relativedelta(months=1)

future_day = today + year_delta + month_delta + day_delta
print(f"1년 1개월 1일 뒤: {future_day}")
```

#### 5-4. 문자열 ↔ 날짜 변환

실제 데이터는 `'2025-10-29'`와 같은 **문자열 형태**인 경우가 많다. 이를 연산 가능한 **날짜 객체로** 바꾸거나, 그 반대로 변환하는 작업은 매우 중요하다.

- `strptime()`: **Str**ing **P**arse **Time**. 문자열을 날짜 객체로 변환.
- `strftime()`: **Str**ing **F**ormat **Time**. 날짜 객체를 문자열로 변환.

> **💡 중요!**
> 날짜 형식 코드(`%Y`, `%m`, `%d` 등)는 변환하려는 문자열의 형식과 **정확히 일치**해야 한다. 예를 들어, 문자열이 `'2025/10/29'` 라면 형식 코드는 `'%Y/%m/%d'`가 되어야 한다.

```python
from datetime import datetime

# 문자열 -> 날짜 객체 (strptime)
str_date = '2025-10-29'
date_obj = datetime.strptime(str_date, '%Y-%m-%d')
print(f"문자열 '{str_date}' -> 날짜 객체: {date_obj}, 타입: {type(date_obj)}")

# 날짜 객체 -> 문자열 (strftime)
str_from_obj = date_obj.strftime('%Y년 %m월 %d일')
print(f"날짜 객체 {date_obj} -> 문자열: '{str_from_obj}', 타입: {type(str_from_obj)}")
```

---

### 🔄 6. 반복문 (Loops)

#### 6-1. `while` 반복문

`while`문은 **특정 조건이 참인 동안** 코드 블록을 계속해서 반복한다. 주로 반복 횟수가 정해져 있지 않을 때 사용된다.

- **구조**:
  1.  **초기식**: 반복을 시작하기 전, 조건에 사용될 변수를 초기화한다.
  2.  **조건식**: 이 조건이 `True`인 동안 루프가 계속된다.
  3.  **증감식**: 루프의 마지막 부분에서 초기식 변수의 값을 변경하여, 언젠가 루프가 종료될 수 있도록 한다. (무한 루프 방지)

##### 예제: 특정 기간의 날짜 리스트 생성하기

```python
from datetime import datetime, timedelta

start_day_str = '2025-10-01'
end_day_str = '2025-10-10'

start_day = datetime.strptime(start_day_str, '%Y-%m-%d')
end_day = datetime.strptime(end_day_str, '%Y-%m-%d')

date_list = []
current_day = start_day  # 1. 초기식

while current_day <= end_day:  # 2. 조건식
    # 실행문
    date_list.append(current_day.strftime('%Y-%m-%d'))
    
    # 3. 증감식
    current_day += timedelta(days=1)

print(date_list)
```

#### 6-2. `for` 반복문

`for`문은 리스트, 튜플, 문자열 등 **순서가 있는 자료구조(iterable)**의 모든 요소를 하나씩 순회할 때 사용된다.

- **`for ... in range()`**: 정해진 횟수만큼 반복할 때 가장 많이 사용된다.
- **`enumerate()`**: 리스트를 순회할 때 **인덱스**와 **값**을 동시에 얻고 싶을 때 사용한다.
- **`break`**: 반복문을 즉시 **중단**하고 빠져나온다.
- **`continue`**: 현재 반복 차례를 **건너뛰고** 다음 반복으로 넘어간다.

##### 예제: 구구단 출력하기 (중첩 for문, `break`, `continue`)

```python
# 2단부터 9단까지 출력
for dan in range(2, 10):
    
    # continue 예제: 5단은 건너뛰기
    if dan == 5:
        continue
        
    # break 예제: 8단부터는 출력하지 않기
    if dan == 8:
        break
        
    print(f"--- {dan}단 ---")
    for i in range(1, 10):
        print(f"{dan} * {i} = {dan * i}")
    print() # 단이 끝날 때마다 한 줄 띄우기
```

#### 6-3. `for-else`와 `while-else`

파이썬의 독특한 문법으로, 반복문이 `break`에 의해 중단되지 않고 **정상적으로 끝까지 실행되었을 때** `else` 블록의 코드가 실행된다.

> **📌 노트:** 이 기능은 "반복문을 모두 돌았지만 원하는 것을 찾지 못했을 때" 특정 작업을 수행하는 데 매우 유용하다.

##### 예제: 숫자 추측 게임 (`for-else` 활용)

```python
import random

answer = random.randint(1, 100)
print("1부터 100 사이의 숫자를 맞춰보세요! 기회는 10번입니다.")

for i in range(1, 11):
    try:
        guess = int(input(f"({i}번째 시도) 숫자를 입력하세요: "))
    except ValueError:
        print("숫자만 입력해주세요.")
        continue

    if guess > answer:
        print("다운(Down)!")
    elif guess < answer:
        print("업(Up)!")
    else:
        print(f"정답입니다! {i}번 만에 맞추셨네요.")
        break  # 정답을 맞췄으므로 break로 반복 중단
else:
    # for문이 10번 모두 실행되고도 break를 만나지 못했을 때 실행됨
    print(f"실패! 모든 기회를 사용했습니다. 정답은 {answer}였습니다.")
```

---

### 🧩 7. 종합 실습: 로그 데이터 분석 및 AI 연동 시뮬레이션

오늘 배운 `list`, `dict`, `if`, `for`, `def` 등을 모두 활용하여 실용적인 데이터 처리 시나리오를 구현해보자.

> **시나리오**: 시스템에서 발생한 로그 데이터 뭉치가 있다. 이 중에서 심각도(`level`)가 'high'인 로그만 필터링하여 원인을 분석하고, AI 서비스에 분석을 요청하여 대응 방안을 받는 과정을 시뮬레이션한다.

```python
import json

def analyze_and_report_logs(logs):
    """
    로그 데이터에서 심각도가 'high'인 로그를 분석하고,
    AI 서비스에 리포트를 요청하는 과정을 시뮬레이션하는 함수
    """
    print("### 1. 'high' 레벨 로그 필터링 시작 ###")
    high_risk_logs = []
    for log in logs:
        # 'level' 키가 존재하고, 그 값이 'high'인 경우에만 리스트에 추가
        if 'level' in log and log['level'] == 'high':
            high_risk_logs.append(log)
            print(f"- 발견: {log['message']} (IP: {log['ip']})")

    if not high_risk_logs:
        print("-> 심각한 위험 로그가 발견되지 않았습니다.")
        return

    print(f"
### 2. AI 분석을 위한 데이터 준비 ({len(high_risk_logs)}건) ###")
    # AI 서비스에 보내기 위해 필터링된 로그를 JSON 형식의 문자열로 변환
    report_data = {
        "service_name": "user-auth-api",
        "risk_logs": high_risk_logs
    }
    
    # json.dumps를 사용하여 파이썬 딕셔너리를 JSON 문자열로 변환
    # indent=2 옵션은 가독성을 위해 JSON을 예쁘게 출력해준다.
    json_request_body = json.dumps(report_data, indent=2, ensure_ascii=False)
    print("-> AI 요청 데이터(JSON):")
    print(json_request_body)

    print("
### 3. AI 서비스 응답 시뮬레이션 ###")
    # 실제로는 HTTP 요청을 보내지만, 여기서는 AI가 분석 결과를 반환했다고 가정한다.
    mock_ai_response_str = """
    {
      "analysis_id": "analysis-12345",
      "summary": "동일 IP(115.95.200.10)에서 1초 내 10회 이상의 로그인 실패 발생. Brute-force 공격으로 의심됨.",
      "recommendation": {
        "action": "BLOCK_IP",
        "details": {
          "ip_address": "115.95.200.10",
          "reason": "Suspicious brute-force attack pattern detected.",
          "block_duration_minutes": 60
        }
      },
      "confidence_score": 0.95
    }
    """
    print("-> AI 응답 데이터(JSON):")
    print(mock_ai_response_str)

    print("
### 4. AI 응답 파싱 및 후속 조치 실행 ###")
    # json.loads를 사용하여 JSON 문자열을 다시 파이썬 딕셔너리로 변환
    ai_response = json.loads(mock_ai_response_str)

    # 딕셔너리의 키를 통해 필요한 정보에 접근
    action = ai_response.get("recommendation", {}).get("action")
    details = ai_response.get("recommendation", {}).get("details", {})

    if action == "BLOCK_IP":
        ip_to_block = details.get("ip_address")
        duration = details.get("block_duration_minutes")
        print(f"-> 실행 조치: IP {ip_to_block}를 {duration}분 동안 차단합니다.")
    else:
        print("-> 특이 조치 없음.")


# --- 시뮬레이션 실행 ---
# 1. 샘플 로그 데이터 (리스트 안에 딕셔너리가 중첩된 구조)
sample_logs = [
    {'timestamp': '2025-10-29T10:00:01Z', 'level': 'info', 'message': 'User logged in', 'ip': '203.245.1.12'},
    {'timestamp': '2025-10-29T10:01:15Z', 'level': 'high', 'message': 'Login failed: invalid password', 'ip': '115.95.200.10'},
    {'timestamp': '2025-10-29T10:01:15Z', 'level': 'high', 'message': 'Login failed: invalid password', 'ip': '115.95.200.10'},
    {'timestamp': '2025-10-29T10:01:16Z', 'level': 'warn', 'message': 'API rate limit exceeded', 'ip': '211.110.8.100'},
    {'timestamp': '2025-10-29T10:01:16Z', 'level': 'high', 'message': 'Login failed: invalid password', 'ip': '115.95.200.10'},
    {'timestamp': '2025-10-29T10:02:30Z', 'level': 'info', 'message': 'User updated profile', 'ip': '203.245.1.12'},
]

# 2. 정의된 함수 실행
analyze_and_report_logs(sample_logs)
```
