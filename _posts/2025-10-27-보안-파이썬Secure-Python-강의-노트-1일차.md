
---
title: "📝 보안 파이썬(Secure Python) 강의 노트 - Day 01 (2025년 10월 27일)"
date: 2025-10-27
excerpt: "보안 전문가를 위한 파이썬 기초: 변수, 데이터 타입, 로그 관리"
categories:
  - Python
tags:
  - Python
  - SK_Rookies
---

- Python
  - Python
  - SK_Rookies

# 📝 보안 파이썬(Secure Python) 강의 노트 - Day 01 (2025년 10월 27일)


## 📋 목차

1. [학습 개요 및 목표](#학습-개요-및-목표)
2. [파이썬 기본 개념](#파이썬-기본-개념)
3. [변수와 데이터 타입](#변수와-데이터-타입)
4. [Sequence 타입 상세](#sequence-타입-상세)
5. [Mapping 타입 (Dictionary)](#mapping-타입-dictionary)
6. [집합 타입 (Tuple, Set)](#집합-타입-tuple-set)
7. [출력 형식과 포매팅](#출력-형식과-포매팅)
8. [보안 관점의 로그 관리](#보안-관점의-로그-관리)
9. [실전 예제 코드 분석](#실전-예제-코드-분석)
10. [종합 정리 및 핵심 요약](#종합-정리-및-핵심-요약)


## 🎯 학습 개요 및 목표

### 강의 배경

오늘 강의는 **보안 전문가를 위한 파이썬 프로그래밍**의 첫 시간으로 진행되었습니다. 단순히 파이썬 문법을 배우는 것이 아니라, **보안 관점에서 파이썬을 어떻게 활용할 것인가**에 초점을 맞추었습니다.

강사님께서 강조하신 중요한 포인트는 다음과 같습니다:

- **"긴 레이스를 하시는 것이기 때문에 기록보다 머리의 기억력이 더 많이 남습니다."**
- 배운 내용을 반드시 노션이나 브이로그 등에 정리하면서 복습할 것
- 이미 파이썬을 아는 분들도 **"보안적으로는 어떻게 바라봐야 하지?"**라는 관점으로 접근할 것

### 학습 목표

1. **파이썬 기본 문법 이해**: 변수, 데이터 타입, 연산자 등 기초 개념 습득
2. **보안 관점의 사고방식**: 일반적인 프로그래밍이 아닌 보안 전문가로서의 코드 작성법
3. **로그 분석 및 관리**: 정형화된 로그 형식의 중요성과 파싱 기법
4. **실전 예제 학습**: SQL Injection 등 실제 보안 위협에 대한 코드 작성

💡 **중요!**: 이 강의는 SK 쉴더스와 협력하여 진행되는 **보안 전문 인력 양성 과정**입니다. 졸업 후 바로 취업을 목표로 하는 실무 중심 교육입니다.


## 🔧 파이썬 기본 개념

### 변수(Variable)란?

변수는 **데이터를 담는 그릇**입니다. 프로그래밍에서 변수는 메모리 공간에 값을 저장하고, 나중에 그 값을 참조하거나 변경할 수 있게 해줍니다.

#### 변수 명명 규칙

변수를 선언할 때 반드시 지켜야 할 규칙들이 있습니다:

1. **숫자로 시작할 수 없음**: `1user`는 불가능, `user1`은 가능
2. **특수문자 제한**: `_`(언더스코어)와 `$`만 허용됨
3. **예약어 사용 금지**: Python의 키워드는 변수명으로 사용할 수 없음

```python
import keyword

keywordList = keyword.kwlist
print(keywordList)
```

#### 💻 코드 실행 상세 분석

**1단계**: `keyword` 모듈을 가져옵니다. 이 모듈은 Python의 모든 예약어 목록을 제공합니다.

**2단계**: `keyword.kwlist`를 호출하여 예약어 리스트를 `keywordList` 변수에 저장합니다.

**3단계**: `print()` 함수로 예약어 목록을 출력합니다.

**최종 결과**: 다음과 같은 예약어 목록이 출력됩니다:
```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

🔐 **보안 노트**: 예약어를 변수명으로 사용하면 코드의 의도하지 않은 동작이 발생할 수 있습니다. 특히 `str`, `int`, `dict` 등 내장 타입을 변수명으로 사용하면 나중에 해당 타입을 사용할 때 에러가 발생합니다. 강의에서 강사님이 실수로 `str` 변수를 만들어 커널을 재시작해야 했던 사례를 통해 이를 직접 확인했습니다.

### 다양한 식별자 선언 방식

Python에서는 여러 가지 변수 명명 규칙이 존재합니다:

#### 1. **Camel Case** (카멜 케이스)
- 형식: `numberOfCollegeGraduates`
- 첫 단어는 소문자, 이후 단어의 첫 글자는 대문자
- 주로 **변수와 함수**에 사용

#### 2. **Pascal Case** (파스칼 케이스)
- 형식: `NumberOfCollegeGraduates`
- 모든 단어의 첫 글자를 대문자로
- 주로 **클래스**에 사용

#### 3. **Snake Case** (스네이크 케이스)
- 형식: `number_of_college_graduates`
- 단어를 언더스코어로 연결
- Python에서는 비추천이지만, 일부 개발자들이 사용

```python
# 실제 코드 예제
month = 10
year = 2025

# 변수 타입 확인
print(year, month)
print('year type - ', type(year))
```

#### 💻 코드 실행 상세 분석

**1단계**: `month` 변수에 정수 `10`을 할당합니다.

**2단계**: `year` 변수에 정수 `2025`를 할당합니다.

**3단계**: `print(year, month)`로 두 변수를 출력합니다. 콤마로 구분하면 자동으로 공백이 삽입됩니다.

**4단계**: `type()` 함수로 변수의 타입을 확인합니다.

**최종 결과**:
```
2025 10
year type -  <class 'int'>
```

📌 **노트**: `type()` 함수는 보안 코드를 작성할 때 **입력값 검증**에 매우 중요합니다. 예상한 타입과 다른 데이터가 들어오면 취약점이 될 수 있기 때문입니다.


## 📦 변수와 데이터 타입

### Python Built-In Types

Python에는 다음과 같은 기본 내장 타입들이 있습니다:

1. **Numeric** (숫자형): `int`, `float`
2. **Sequence** (시퀀스): `list`, `tuple`
3. **Text Sequence** (문자열): `str`
4. **Set** (집합): `set`
5. **Mapping** (매핑): `dict`
6. **Boolean** (불리언): `bool`

### Numeric 타입 상세

#### 정수(int)와 실수(float)

```python
# 정수 타입
age = 25
count = 100

# 실수 타입
score = 95.1234
pi = 3.14159

# 타입 확인
print(type(score))  # <class 'float'>
```

#### 💻 코드 실행 상세 분석

**1단계**: `score` 변수에 실수 값 `95.1234`를 할당합니다.

**2단계**: Python 인터프리터는 소수점이 있는 숫자를 자동으로 `float` 타입으로 인식합니다.

**3단계**: `type(score)`를 호출하면 변수의 타입 객체를 반환합니다.

**4단계**: `print()`로 타입 정보를 출력합니다.

**최종 결과**: `<class 'float'>`이 출력됩니다.

🔐 **보안 노트**: 실수형 데이터를 다룰 때는 **부동소수점 연산의 부정확성**을 항상 고려해야 합니다. 예를 들어, `0.1 + 0.2 == 0.3`은 `False`입니다. 금융 데이터나 정밀한 계산이 필요한 보안 시스템에서는 `decimal` 모듈을 사용해야 합니다.

### 문자열(String) 타입

```python
name = "김한수"
print(name, type(name))

# sep 파라미터를 사용한 출력
print('010', '1234', '5678', sep="-")
print('kknd03255', 'gmail.com', sep='@')
```

#### 💻 코드 실행 상세 분석

**1단계**: `name` 변수에 문자열 "김한수"를 할당합니다. 큰따옴표나 작은따옴표 모두 사용 가능합니다.

**2단계**: `print()` 함수의 `sep` 파라미터를 사용하여 출력 시 구분자를 지정합니다.

**3단계**: 첫 번째 `print()`는 세 개의 문자열을 `-`로 연결하여 출력합니다.

**4단계**: 두 번째 `print()`는 두 개의 문자열을 `@`로 연결하여 이메일 형식으로 출력합니다.

**최종 결과**:
```
김한수 <class 'str'>
010-1234-5678
kknd03255@gmail.com
```

💡 **중요!**: `sep` 파라미터는 보안 로그를 정형화할 때 매우 유용합니다. CSV 형식의 로그나 특정 구분자를 사용하는 로그 파일을 생성할 때 활용할 수 있습니다.


## 📚 Sequence 타입 상세

### List (리스트) - []

List는 **순서가 있는 열거형** 데이터 타입입니다. Python의 Array와 유사하지만, 더 유연하고 강력합니다.

#### List의 주요 특징

1. **인덱싱(Indexing)** 가능
2. **슬라이싱(Slicing)** 가능
3. **연결(Concatenation)** 가능
4. **반복(Iteration)** 가능
5. **가변성(Mutable)**: 요소를 추가, 삭제, 수정할 수 있음

```python
keywordList = keyword.kwlist

# 인덱싱
print('indexing - ', keywordList[0])  # 'False'

# 슬라이싱
print('slicing = ', keywordList[0:5])  # ['False', 'None', 'True', 'and', 'as']
```

#### 💻 코드 실행 상세 분석

**1단계**: `keywordList[0]`는 리스트의 첫 번째 요소에 접근합니다. Python은 0부터 인덱스가 시작합니다.

**2단계**: 인덱싱 연산은 리스트에서 해당 위치의 단일 요소를 반환합니다.

**3단계**: `keywordList[0:5]`는 슬라이싱 연산으로, 인덱스 0부터 4까지(5는 포함되지 않음)의 요소들을 새로운 리스트로 반환합니다.

**4단계**: 슬라이싱은 원본 리스트를 변경하지 않고 새로운 리스트 객체를 생성합니다.

**최종 결과**:
```
indexing -  False
slicing =  ['False', 'None', 'True', 'and', 'as']
```

#### 고급 슬라이싱 기법

```python
tupleTemp2 = "a","b","c","d","e"
print('slicing - ', tupleTemp2[0::2])  # 2칸씩 건너뛰기
```

#### 💻 코드 실행 상세 분석

**1단계**: 슬라이싱 문법 `[start:stop:step]`에서 `[0::2]`는 시작점 0, 끝점 생략(전체), 스텝 2를 의미합니다.

**2단계**: 인덱스 0에서 시작하여 2칸씩 건너뛰며 요소를 추출합니다.

**3단계**: 0번째, 2번째, 4번째 요소가 선택됩니다.

**최종 결과**: `('a', 'c', 'e')`

📌 **노트**: 이 기법은 **홀수 번째 또는 짝수 번째 데이터만 추출**할 때 유용합니다. 보안 로그 분석에서 특정 패턴의 데이터를 필터링할 때 활용할 수 있습니다.

#### 문자열에서의 슬라이싱 활용

```python
strEx = '홀짝홀짝홀짝홀짝홀짝홀짝홀짝홀짝홀짝홀짝'
print(strEx[::2])   # 홀수번째 문자만 출력
print(strEx[1::2])  # 짝수번째 문자만 출력
```

#### 💻 코드 실행 상세 분석

**1단계**: `strEx[::2]`는 인덱스 0부터 시작하여 2칸씩 건너뛰며 문자를 추출합니다.

**2단계**: 인덱스 0, 2, 4, 6, ... 의 문자들이 선택되어 "홀홀홀홀홀홀홀홀홀홀"이 출력됩니다.

**3단계**: `strEx[1::2]`는 인덱스 1부터 시작하여 2칸씩 건너뛰므로 인덱스 1, 3, 5, 7, ... 의 문자들이 선택됩니다.

**4단계**: "짝짝짝짝짝짝짝짝짝짝"이 출력됩니다.

**최종 결과**:
```
홀홀홀홀홀홀홀홀홀홀
짝짝짝짝짝짝짝짝짝짝
```

🔐 **보안 노트**: 이러한 슬라이싱 기법은 **데이터 마스킹**에 활용할 수 있습니다. 예를 들어, 주민등록번호나 신용카드 번호의 특정 자리만 표시하고 나머지는 숨길 때 유용합니다.

### Text Sequence - 문자열의 시퀀스 특성

문자열도 Sequence 타입이기 때문에 인덱싱과 슬라이싱이 가능합니다:

```python
strTemp = 'Talk is cheap. Show me the code.'
print(strTemp)

# 인덱싱
print('indexing - ', strTemp[0])  # 'T'

# 문자열 분리
listTemp = strTemp.split(' ')
print('indexing - ', listTemp[-1])  # 'code.'
```

#### 💻 코드 실행 상세 분석

**1단계**: 문자열 변수 `strTemp`에 전체 문장을 저장합니다.

**2단계**: `strTemp[0]`으로 첫 번째 문자 'T'에 접근합니다.

**3단계**: `split(' ')` 메서드는 공백을 기준으로 문자열을 분리하여 리스트를 반환합니다.

**4단계**: `listTemp[-1]`은 리스트의 마지막 요소에 접근합니다. 음수 인덱스는 뒤에서부터 세는 것을 의미합니다.

**최종 결과**:
```
Talk is cheap. Show me the code.
indexing -  T
indexing -  code.
```

💡 **중요!**: 문자열의 `split()` 메서드는 로그 파싱에서 가장 많이 사용되는 기능 중 하나입니다. 로그 파일의 각 줄을 특정 구분자로 분리하여 분석할 수 있습니다.


## 🗂️ Mapping 타입 (Dictionary)

### Dictionary (딕셔너리) - {}

Dictionary는 **Key-Value 쌍**으로 데이터를 저장하는 타입입니다. 웹 개발에서는 JSON 형식과 동일한 구조입니다.

#### Dictionary의 주요 특징

1. **Key와 Value의 쌍**으로 구성
2. **인덱싱 불가**: 숫자 인덱스로 접근할 수 없음
3. **Key로 접근**: Key를 통해서만 Value에 접근 가능
4. **콜론(:)**으로 Key와 Value 구분
5. **가변성(Mutable)**: 요소를 추가, 삭제, 수정할 수 있음

```python
log = {
    'SQL Injection': {
        "정의": "사용자 입력을 적절히 검증하지 않고 데이터베이스 쿼리에 직접 포함하는것",
        "용어": [
            "입력검증", "파라미터화", "블라인드", "에러기반"
        ],
        "취약 코드 예시": "query = select * from table",
        "공격 예시": "user = admin or 1=1",
        "탐지": [
            "웹 취약점 스캐너 사용", "비정상적인 쿼리", "오류 모니터링"
        ]
    }
}

print(log)
print('type - ', type(log))
print(log["SQL Injection"]["용어"], type(log["SQL Injection"]["용어"]))
```

#### 💻 코드 실행 상세 분석

**1단계**: 중첩된 Dictionary 구조를 생성합니다. 외부 Key는 'SQL Injection'이고, 그 Value는 또 다른 Dictionary입니다.

**2단계**: 내부 Dictionary는 여러 Key-Value 쌍을 가지며, 일부 Value는 리스트입니다.

**3단계**: `log["SQL Injection"]["용어"]`는 **중첩 접근**을 의미합니다. 먼저 "SQL Injection" Key로 접근한 후, 그 안의 "용어" Key로 접근합니다.

**4단계**: 최종적으로 "용어" Key의 Value인 리스트를 반환합니다.

**최종 결과**:
```
{'SQL Injection': {'정의': '사용자 입력을 적절히 검증하지 않고 데이터베이스 쿼리에 직접 포함하는것', '용어': ['입력검증', '파라미터화', '블라인드', '에러기반'], '취약 코드 예시': 'query = select * from table', '공격 예시': 'user = admin or 1=1', '탐지': ['웹 취약점 스캐너 사용', '비정상적인 쿼리', '오류 모니터링']&#125;&#125;
type -  <class 'dict'>
['입력검증', '파라미터화', '블라인드', '에러기반'] <class 'list'>
```

🔐 **보안 노트**: Dictionary는 **보안 설정 파일**이나 **취약점 데이터베이스**를 구성할 때 매우 유용합니다. 위 예제처럼 각 공격 유형별로 정의, 용어, 탐지 방법 등을 체계적으로 정리할 수 있습니다.

💡 **중요!**: 강사님께서 강조하신 부분 - "파이썬에서 가장 많이 쓰이는 변수 타입은 딕셔너리입니다. 하지만 실제로 가장 많이 사용되는 형태는 **딕셔너리를 담는 리스트**입니다." 즉, `[{}, {}, {}]` 형태의 데이터 구조가 대용량 데이터 분석에서 가장 일반적입니다.


## 🎲 집합 타입 (Tuple, Set)

### Tuple (튜플) - ()

Tuple은 **불변성(Immutable)**을 가진 순서형 데이터 타입입니다.

#### Tuple의 주요 특징

1. **불변성**: 한 번 생성되면 요소를 변경할 수 없음
2. **인덱싱과 슬라이싱** 가능
3. **소괄호 생략 가능**: `a, b, c = 1, 2, 3` (Packing)
4. **단일 요소 Tuple**: `(1,)` - 콤마 필수!

```python
# 잘못된 예
tupleTemp = (1)
print('type - ', type(tupleTemp))  # <class 'int'>

# 올바른 예
tupleTemp = (1,)
tupleTemp2 = "a","b","c"  # 소괄호 생략 가능 (packing)
print(tupleTemp)
print(tupleTemp2)
print('type - ', type(tupleTemp2))
```

#### 💻 코드 실행 상세 분석

**1단계**: `tupleTemp = (1)`은 단순히 정수 1을 소괄호로 감싼 것으로, Python은 이를 정수로 인식합니다.

**2단계**: Tuple로 인식되려면 반드시 콤마가 있어야 합니다. `(1,)`가 올바른 단일 요소 Tuple입니다.

**3단계**: `"a","b","c"`는 소괄호 없이 콤마만으로 Tuple을 생성하는 **packing** 문법입니다.

**4단계**: `type()` 함수로 각 변수의 타입을 확인합니다.

**최종 결과**:
```
type -  <class 'int'>
(1,)
('a', 'b', 'c')
type -  <class 'tuple'>
```

#### Unpacking (언패킹)

```python
tupleTemp2 = "a","b","c"
a, b, c = tupleTemp2
print('unpacking - ', a, b, c)
```

#### 💻 코드 실행 상세 분석

**1단계**: Tuple `tupleTemp2`에 세 개의 문자열 요소가 있습니다.

**2단계**: `a, b, c = tupleTemp2`는 **unpacking** 연산으로, Tuple의 각 요소를 개별 변수에 할당합니다.

**3단계**: `a`에는 "a", `b`에는 "b", `c`에는 "c"가 할당됩니다.

**최종 결과**: `unpacking -  a b c`

💡 **중요!**: Unpacking은 **함수의 다중 반환값**을 받을 때 자주 사용됩니다. 예를 들어, `x, y = get_coordinates()` 같은 형태입니다.

#### Tuple의 불변성 증명

```python
tupleTemp2 = "a","b","c"
# 시도: tupleTemp2[0] = "z"
# 결과: TypeError: 'tuple' object does not support item assignment
```

#### 💻 코드 실행 상세 분석

**1단계**: Tuple의 첫 번째 요소를 변경하려고 시도합니다.

**2단계**: Python 인터프리터는 Tuple이 불변 타입임을 확인합니다.

**3단계**: `TypeError` 예외를 발생시켜 수정을 차단합니다.

**최종 결과**: 오류 메시지 - `TypeError: 'tuple' object does not support item assignment`

🔐 **보안 노트**: Tuple의 불변성은 **보안 설정이나 암호화 키를 저장**할 때 유용합니다. 실수로 또는 악의적으로 데이터가 변경되는 것을 방지할 수 있습니다. 예를 들어, 암호화 알고리즘의 초기 벡터(IV)나 솔트(Salt) 값을 Tuple로 저장하면 안전합니다.

### Set (집합) - {}

Set은 **순서가 없고 중복을 허용하지 않는** 데이터 타입입니다.

#### Set의 주요 특징

1. **중복 불가**: 같은 값을 여러 번 추가해도 하나만 저장됨
2. **순서 없음**: 인덱싱 불가
3. **수학적 집합 연산** 가능: 합집합, 교집합, 차집합 등
4. **가변성(Mutable)**: 요소 추가/삭제 가능

```python
userRoles = {"admin", "user", "guest"}
print(userRoles)
print('type - ', type(userRoles))

userRoles.add("user")  # 중복 추가 시도
print(userRoles)  # 변화 없음
```

#### 💻 코드 실행 상세 분석

**1단계**: `{"admin", "user", "guest"}` Set을 생성합니다.

**2단계**: `add()` 메서드로 "user"를 추가하려 합니다.

**3단계**: Set은 중복을 허용하지 않으므로, 이미 존재하는 "user"는 추가되지 않습니다.

**4단계**: Set의 크기와 내용은 변하지 않습니다.

**최종 결과**: 여전히 3개의 요소만 존재

#### Set 메서드

```python
empSet = set()  # 빈 Set 생성

empSet.add("user")
empSet.add("guest")
empSet.add("admin")
print('data - ', empSet)

empSet.discard('guest')  # 요소 제거 (없어도 에러 X)
print('data - ', empSet)

empSet.remove('admin')  # 요소 제거 (없으면 에러 O)
print('data - ', empSet)
```

#### 💻 코드 실행 상세 분석

**1단계**: `set()` 함수로 빈 Set을 생성합니다. `{}`는 빈 Dictionary로 인식되므로 주의!

**2단계**: `add()` 메서드로 세 개의 요소를 추가합니다.

**3단계**: `discard('guest')`는 'guest'를 제거합니다. 존재하지 않는 요소를 삭제해도 에러가 발생하지 않습니다.

**4단계**: `remove('admin')`는 'admin'을 제거합니다. 존재하지 않는 요소를 삭제하면 `KeyError`가 발생합니다.

**최종 결과**:
```
data -  {'admin', 'user', 'guest'}
data -  {'admin', 'user'}
data -  {'user'}
```

📌 **노트**: `discard()`와 `remove()`의 차이점을 이해하는 것이 중요합니다. 보안 코드에서는 예외 처리가 필요한 경우 `remove()`를, 안전하게 처리하려면 `discard()`를 사용합니다.

#### Set의 집합 연산

```python
adminRoles = {"read", "write", "delete", "update"}
userRoles = {"read", "comment"}

print('합집합 - ', adminRoles | userRoles)
print('교집합 - ', adminRoles & userRoles)
print('차집합 - ', adminRoles - userRoles)
print('대칭 차집합 - ', adminRoles ^ userRoles)
```

#### 💻 코드 실행 상세 분석

**1단계**: 두 개의 Set을 생성합니다. 하나는 관리자 권한, 하나는 일반 사용자 권한입니다.

**2단계**: `|` 연산자는 **합집합**을 계산합니다. 두 Set의 모든 요소를 포함하되 중복은 제거합니다.

**3단계**: `&` 연산자는 **교집합**을 계산합니다. 두 Set에 공통으로 존재하는 요소만 반환합니다.

**4단계**: `-` 연산자는 **차집합**을 계산합니다. 첫 번째 Set에서 두 번째 Set의 요소를 제거합니다.

**5단계**: `^` 연산자는 **대칭 차집합**을 계산합니다. 한쪽에만 존재하는 요소들을 반환합니다.

**최종 결과**:
```
합집합 -  {'read', 'write', 'delete', 'update', 'comment'}
교집합 -  {'read'}
차집합 -  {'write', 'delete', 'update'}
대칭 차집합 -  {'write', 'delete', 'update', 'comment'}
```

🔐 **보안 노트**: Set의 집합 연산은 **권한 관리 시스템**에서 매우 유용합니다. 예를 들어:
- **합집합**: 여러 역할의 권한을 통합
- **교집합**: 공통 권한 확인
- **차집합**: 추가로 필요한 권한 계산
- **대칭 차집합**: 서로 다른 권한만 추출

#### Set을 활용한 중복 로그인 방지

강의에서 실제 보안 활용 사례로 제시된 코드입니다:

```python
userTokens = set()

def login(token):
    if token in userTokens:
        raise ValueError(f"[보안경고] 이미 로그인중 : {token}")
    userTokens.add(token)
    print(f"{token} 로그인 성공")

userTokens.add('jslim')
userTokens.add('sk')
userTokens.add('jslim')  # 중복 허용 X
```

#### 💻 코드 실행 상세 분석

**1단계**: 빈 Set `userTokens`를 생성하여 로그인 토큰을 저장합니다.

**2단계**: `login()` 함수는 토큰이 이미 Set에 있는지 `in` 연산자로 확인합니다.

**3단계**: 토큰이 이미 존재하면 `ValueError` 예외를 발생시켜 중복 로그인을 차단합니다.

**4단계**: 토큰이 없으면 `add()` 메서드로 Set에 추가하고 성공 메시지를 출력합니다.

**5단계**: 세 번째 `add('jslim')`은 중복이므로 Set에 추가되지 않습니다.

**최종 결과**: Set에는 'jslim'과 'sk' 두 개의 토큰만 저장됩니다.

💡 **중요!**: 강사님께서 강조하신 부분 - "리스트에서 `in` 연산자를 사용하면 전체를 스캔해야 하므로 리소스를 많이 먹습니다. Set은 해시 테이블 기반이므로 O(1) 시간 복잡도로 빠르게 검색할 수 있습니다. 따라서 중복 로그인 방지는 반드시 Set으로 처리해야 합니다."

🔐 **보안 노트**: 이 패턴은 **세션 관리**, **API 토큰 관리**, **IP 주소 블랙리스트** 등 다양한 보안 시나리오에 적용할 수 있습니다. Set의 빠른 검색 속도는 실시간 보안 시스템에서 필수적입니다.


## 🖨️ 출력 형식과 포매팅

### print() 함수의 기본 사용법

```python
userInfo = {
    'name': "jslim",
    'age': '20'
}

print('name ', userInfo['name'])
print('age ', userInfo['age'])

role = "admin"
print('문자열 연결(+) ', "Hello " + role + "!!")
```

#### 💻 코드 실행 상세 분석

**1단계**: Dictionary에서 Key로 Value에 접근하여 출력합니다.

**2단계**: `+` 연산자로 문자열을 연결하여 출력합니다.

**3단계**: `print()` 함수는 자동으로 줄바꿈을 수행합니다.

**최종 결과**:
```
name  jslim
age  20
문자열 연결(+)  Hello admin!!
```

### f-string (포맷 스트링)

**f-string**은 Python 3.6 버전부터 도입된 강력한 문자열 포매팅 방법입니다.

💡 **중요!**: 강사님께서 강조하신 버전 이슈 - "f-string은 Python 3.6 이상에서만 동작합니다. 개인 노트북에서 작업할 때는 반드시 Python 버전을 확인하세요!"

#### f-string의 기본 문법

```python
name = "sk"
score = 95.1234

print(f"name : {name}")
print(f"score : {score}", type(score))
print(f"name : {name}, score : {score:.2f}")
```

#### 💻 코드 실행 상세 분석

**1단계**: `f` 접두사를 사용하여 f-string임을 표시합니다.

**2단계**: 중괄호 `{}` 안에 변수를 직접 삽입할 수 있습니다.

**3단계**: `{score:.2f}`는 실수를 소수점 두 자리까지만 표시하는 포맷 지정자입니다.

**4단계**: 표현식이 평가되어 문자열에 삽입됩니다.

**최종 결과**:
```
name : sk
score : 95.1234 <class 'float'>
name : sk, score : 95.12
```

📌 **노트**: f-string 내부에는 변수뿐만 아니라 **표현식**도 사용할 수 있습니다. 예: `f"{len(name)} characters"`, `f"{score * 2}"` 등

🔐 **보안 노트**: f-string은 **SQL Injection** 등의 공격에는 안전하지만, **로그 인젝션** 공격에는 취약할 수 있습니다. 사용자 입력을 f-string에 직접 삽입할 때는 **입력 검증**을 먼저 수행해야 합니다.

### str.format() 메서드

`format()` 메서드는 f-string 이전에 널리 사용되던 방법입니다.

```python
lang = 'python'
version = 3.13

print("language : {}, version : {}".format(lang, version))
print("language : {0}, version : {1}".format(lang, version))
print("language : {a}, version : {b}".format(a=lang, b=version))
```

#### 💻 코드 실행 상세 분석

**1단계**: 문자열에 `{}` 플레이스홀더를 삽입합니다.

**2단계**: `format()` 메서드의 인자가 순서대로 플레이스홀더에 대입됩니다.

**3단계**: 두 번째 예제는 **위치 인덱스**를 명시적으로 지정합니다.

**4단계**: 세 번째 예제는 **키워드 인자**를 사용하여 더 명확하게 표현합니다.

**최종 결과**:
```
language : python, version : 3.13
language : python, version : 3.13
language : python, version : 3.13
```

💡 **중요!**: 강사님께서 강조하신 부분 - "format() 메서드는 **문자를 실행하는 게 아니라 치환하는 것**이기 때문에 보안상 더 안전할 수 있습니다."

### 서식 지정 연산자 (% 연산자)

C 스타일의 포맷팅 방법입니다.

```python
print('language : %s, version : %.2fcm' % (lang, version))
```

#### 💻 코드 실행 상세 분석

**1단계**: `%s`는 문자열(string)을 의미하는 포맷 지정자입니다.

**2단계**: `%.2f`는 소수점 두 자리까지 표시하는 실수(float) 포맷 지정자입니다.

**3단계**: `%` 연산자 뒤에 튜플 형태로 값을 전달합니다.

**4단계**: 각 포맷 지정자 위치에 해당하는 값이 순서대로 대입됩니다.

**최종 결과**: `language : python, version : 3.13cm`

#### 주요 포맷 지정자

- `%s`: 문자열(string)
- `%d`: 정수(decimal/integer)
- `%f`: 실수(float)
- `%.2f`: 소수점 두 자리 실수

🔐 **보안 노트**: 강사님께서 **매우 중요하게 강조하신 부분** - "서식 지정 연산자는 **보안 취약점**이 될 수 있습니다. 외부에서 입력되는 문자열을 직접적으로 % 포맷에 넣으면 포맷 스트링 공격(Format String Attack)의 대상이 될 수 있습니다. 따라서 보안 코드에서는 가급적 사용하지 않는 것이 좋습니다."

실제로 다음과 같은 공격이 가능합니다:
```python
# 위험한 코드
user_input = "%s%s%s%s%s"
print("User: %s" % user_input)  # 스택 내용 노출 가능
```

### 이스케이프 시퀀스 (Escape Sequence)

```python
data = "Hello\nPython"
print(data)
print(str(data))
print(repr(data))
```

#### 💻 코드 실행 상세 분석

**1단계**: `\n`은 이스케이프 시퀀스로 줄바꿈(new line)을 의미합니다.

**2단계**: `str(data)`는 일반적인 문자열 표현으로, 이스케이프 시퀀스를 해석하여 출력합니다.

**3단계**: `repr(data)`는 **표현(representation)** 형태로, 이스케이프 시퀀스를 문자 그대로 출력합니다.

**최종 결과**:
```
Hello
Python
Hello
Python
'Hello\nPython'
```

🔐 **보안 노트**: 강사님께서 매우 중요하게 강조하신 부분 - "`repr()` 함수는 **보안 디버깅과 로깅**에 매우 유용합니다. 누군가가 데이터를 조작했을 때, 특수 문자가 포함되어 있으면 `repr()`로 그대로 확인할 수 있습니다. 일반 `print()`는 이스케이프 시퀀스를 파싱해버리지만, `repr()`는 문자 그대로 출력하므로 악의적인 입력을 탐지하는 데 활용도가 높습니다."

예를 들어:
```python
# 악의적인 입력
malicious_input = "admin\x00hacker"
print(malicious_input)  # "admin"만 출력될 수 있음
print(repr(malicious_input))  # 'admin\x00hacker' - 전체 확인 가능
```

### 형 변환 함수

```python
strTemp = '100'
print(strTemp, 'type - ', type(int(strTemp)))
```

#### 💻 코드 실행 상세 분석

**1단계**: 문자열 `'100'`이 저장된 변수가 있습니다.

**2단계**: `int(strTemp)`는 문자열을 정수로 변환하는 형 변환 함수입니다.

**3단계**: `type()` 함수로 변환된 결과의 타입을 확인합니다.

**최종 결과**: `100 type -  <class 'int'>`

📌 **노트**: 주요 형 변환 함수들:
- `int()`: 정수로 변환
- `float()`: 실수로 변환
- `str()`: 문자열로 변환
- `list()`: 리스트로 변환
- `tuple()`: 튜플로 변환
- `set()`: 집합으로 변환
- `dict()`: 딕셔너리로 변환

🔐 **보안 노트**: 형 변환은 **입력 검증**의 핵심입니다. 예를 들어, 사용자로부터 숫자를 입력받을 때:
```python
try:
    age = int(user_input)
    if age < 0 or age > 150:
        raise ValueError("Invalid age")
except ValueError:
    print("보안 경고: 올바른 숫자를 입력하세요")
```

### 다중 라인 출력

```python
msg = f"""
[User login Report]
===================
ID   : sk
Time : 2025-10-27
STATUS : success
"""
print(msg)
```

#### 💻 코드 실행 상세 분석

**1단계**: 삼중 따옴표(`"""` 또는 `'''`)를 사용하여 여러 줄의 문자열을 작성합니다.

**2단계**: f-string과 결합하여 변수 삽입도 가능합니다.

**3단계**: 줄바꿈과 들여쓰기가 그대로 유지됩니다.

**최종 결과**:
```
[User login Report]
===================
ID   : sk
Time : 2025-10-27
STATUS : success
```

💡 **중요!**: 이는 **템플릿 기반 보고서**나 **로그 출력**에 매우 유용합니다. 정형화된 포맷으로 로그를 생성하면 나중에 파싱하기가 훨씬 쉬워집니다.

🔐 **보안 노트**: 강사님께서 강조하신 부분 - "이런 템플릿에 크리티컬한 데이터(비밀번호, 개인정보 등)가 들어가면 반드시 **마스킹 처리**를 해야 합니다. ID는 보여주되, 비밀번호는 일부만 표시하거나 완전히 숨겨야 합니다."

예시:
```python
def mask_password(password):
    if len(password) <= 2:
        return "*" * len(password)
    return password[0] + "*" * (len(password) - 2) + password[-1]

password = "mySecret123"
print(f"Password: {mask_password(password)}")  # m*********3
```

### 숫자 포맷

```python
num = 1234567.8912

# 천 단위 구분
print(f"{num:,}")

# 정렬
print(f"{num:>20.2f}")  # 오른쪽 정렬
print(f"{num:<20.2f}")  # 왼쪽 정렬
print(f"{num:020.2f}")  # 0으로 채우기
```

#### 💻 코드 실행 상세 분석

**1단계**: `{num:,}`는 천 단위마다 콤마를 삽입하는 포맷입니다.

**2단계**: `{num:>20.2f}`는 전체 폭 20자, 소수점 두 자리, 오른쪽 정렬을 의미합니다.

**3단계**: `<`는 왼쪽 정렬, `>`는 오른쪽 정렬을 나타냅니다.

**4단계**: `020`은 빈 공간을 0으로 채우라는 의미입니다.

**최종 결과**:
```
1,234,567.8912
          1234567.89
1234567.89          
00000000001234567.89
```

💡 **중요!**: 강사님께서 강조하신 부분 - "숫자 포맷이 중요한 이유는 **정형화된 출력**이 데이터 분석과 침해 탐지에 도움이 되기 때문입니다. 로그 파일에서 일정한 포맷을 유지하면 파싱과 패턴 인식이 훨씬 쉬워집니다."


## 🛡️ 보안 관점의 로그 관리

### 로그 템플릿의 중요성

강사님께서 반복적으로 강조하신 핵심 개념:

> "보안 관점에서 로그를 적용할 때는 반드시 **정형화된 템플릿**이 필요합니다. 수집된 데이터를 파싱하려면 일관된 형식이 있어야 하고, 이를 통해 로그 변조 여부도 쉽게 탐지할 수 있습니다."

### 보안 로그 예제

```python
loginUser = {
    'type': 'guest',
    'ip': '192.168.0.10',
    'event': 'LOGIN_SUCCESS'
}

logMsg = f"[ALTER] User={loginUser['type']}, IP={loginUser['ip']}, event={loginUser['event']}"
print(logMsg)
```

#### 💻 코드 실행 상세 분석

**1단계**: Dictionary에 로그인 정보를 저장합니다. 이는 **구조화된 데이터**입니다.

**2단계**: f-string을 사용하여 정형화된 로그 메시지를 생성합니다.

**3단계**: `[ALTER]` 태그로 로그의 심각도를 표시하고, Key=Value 형식으로 정보를 나열합니다.

**4단계**: 이러한 일관된 포맷은 **정규 표현식**이나 **문자열 파싱**으로 쉽게 분석할 수 있습니다.

**최종 결과**: `[ALTER] User=guest, IP=192.168.0.10, event=LOGIN_SUCCESS`

🔐 **보안 노트**: 이러한 로그 포맷의 장점:
1. **파싱 용이성**: 정규식 `\[(\w+)\] User=(\w+), IP=([\d.]+), event=(\w+)` 로 쉽게 추출
2. **탐지 규칙 생성**: 특정 패턴의 이벤트를 자동으로 탐지 가능
3. **변조 탐지**: 포맷에 맞지 않는 로그는 즉시 식별 가능
4. **자동화**: SIEM 시스템에 쉽게 통합 가능

### 리스트에 로그 누적하기

```python
logLst = []
print('type - ', type(logLst))

logLst.append(loginUser)
logLst.append(loginUser)
print(logLst)

# 각 로그 출력
logMsg = f"[ALTER] User={logLst[0]['type']}, IP={logLst[0]['ip']}, event={logLst[0]['event']}"
print(logMsg)
logMsg = f"[ALTER] User={logLst[1]['type']}, IP={logLst[1]['ip']}, event={logLst[1]['event']}"
print(logMsg)
```

#### 💻 코드 실행 상세 분석

**1단계**: 빈 리스트를 생성하여 로그를 저장할 준비를 합니다.

**2단계**: `append()` 메서드로 Dictionary 객체를 리스트에 추가합니다.

**3단계**: 리스트는 여러 개의 로그 이벤트를 시간 순서대로 저장할 수 있습니다.

**4단계**: 인덱스로 각 로그에 접근하여 포맷팅된 메시지를 생성합니다.

**최종 결과**:
```
type -  <class 'list'>
[{'type': 'guest', 'ip': '192.168.0.10', 'event': 'LOGIN_SUCCESS'}, {'type': 'guest', 'ip': '192.168.0.10', 'event': 'LOGIN_SUCCESS'}]
[ALTER] User=guest, IP=192.168.0.10, event=LOGIN_SUCCESS
[ALTER] User=guest, IP=192.168.0.10, event=LOGIN_SUCCESS
```

💡 **중요!**: 강사님께서 강조하신 데이터 구조 - "실제 대용량 로그 분석에서는 **리스트 안에 딕셔너리**가 들어가는 형태가 가장 일반적입니다. `[{}, {}, {}]` 형태죠. JSON으로 변환하기도 쉽고, 데이터 프레임으로 변환하여 pandas로 분석하기도 편리합니다."

### Boolean 타입과 보안

```python
isLoggedIn = True
hasPermission = False

print('casting - ', int(isLoggedIn), type(isLoggedIn))
print('casting - ', int(hasPermission))

# Truthy와 Falsy
print('castring - ', bool(1))    # True
print('castring - ', bool(0))    # False
print('castring - ', bool('a'))  # True
print('castring - ', bool([]))   # False
print('castring - ', bool([1,2,3]))  # True
```

#### 💻 코드 실행 상세 분석

**1단계**: Boolean 값 `True`와 `False`를 변수에 할당합니다.

**2단계**: `int()` 함수로 Boolean을 정수로 변환하면 `True`는 1, `False`는 0이 됩니다.

**3단계**: `bool()` 함수로 다양한 값을 Boolean으로 변환합니다.

**4단계**: Python의 **Truthy/Falsy** 개념:
   - Falsy: `0`, `''`, `[]`, `{}`, `None`, `False`
   - Truthy: 그 외 모든 값

**최종 결과**:
```
casting -  1 <class 'bool'>
casting -  0
castring -  True
castring -  False
castring -  True
castring -  False
castring -  True
```

🔐 **보안 노트**: Boolean 값은 **권한 체크**와 **상태 관리**에 핵심적입니다:
```python
def check_access(user):
    isAuthenticated = user.get('authenticated', False)
    hasAdminRole = 'admin' in user.get('roles', [])
    
    if not isAuthenticated:
        raise PermissionError("인증되지 않은 사용자")
    
    if not hasAdminRole:
        raise PermissionError("관리자 권한 필요")
    
    return True
```


## 🚀 실전 예제 코드 분석

### Day 02 예제: 보안 이벤트 로그 분석 시스템

이제 `day02_예제코드.py`를 상세히 분석하겠습니다. 이 코드는 **List, Dict, 제어문, 함수, JSON**을 종합적으로 활용한 실전 보안 코드입니다.

#### 예제 데이터 구조

```python
raw_security_logs = [
    {
        "event_id": "evt-20251028-001",
        "timestamp": "2025-10-28T14:00:15Z",
        "source_ip": "203.0.113.78",
        "event_type": "failed_login",
        "severity": "medium",
        "metadata": {
            "username": "admin",
            "attempt_count": 5
        }
    },
    {
        "event_id": "evt-20251028-002",
        "timestamp": "2025-10-28T14:05:22Z",
        "source_ip": "198.51.100.22",
        "event_type": "sql_injection_attempt",
        "severity": "high",
        "metadata": {
            "request_path": "/login",
            "payload": "' or 1=1--"
        }
    },
    {
        "event_id": "evt-20251028-003",
        "timestamp": "2025-10-28T14:06:01Z",
        "source_ip": "203.0.113.78",
        "event_type": "firewall_block",
        "severity": "low",
        "metadata": {
            "rule_id": "FW-RULE-099"
        }
    }
]
```

#### 💻 데이터 구조 분석

**특징 1**: 리스트 안에 여러 Dictionary가 있는 전형적인 **로그 데이터 구조**입니다.

**특징 2**: 각 Dictionary는 일관된 스키마를 가지고 있어 **파싱이 용이**합니다.

**특징 3**: `metadata` 필드는 **중첩된 Dictionary**로, 이벤트별로 다른 정보를 담을 수 있습니다.

**특징 4**: 실제 보안 시스템에서 수집되는 로그의 구조를 그대로 재현했습니다.

### 기본 로그 분석 함수

```python
def analyze_raw_logs(logs):
    """
    List와 Dict로 구성된 로그를 받아, 제어문을 활용해 기본적인 분석을 수행하는 함수
    """
    print("--- 1. 기본 로그 분석 시작 ---")
    
    high_severity_alerts = []
    ip_activity = {}

    # for 반복문: 리스트에 있는 모든 로그(dict)를 하나씩 순회
    for log in logs:
        ip = log["source_ip"]
        
        # if-elif-else 제어문: 로그의 'severity' 값에 따라 다른 동작 수행
        if log["severity"] == "high":
            print(f"[위험] 심각도 '높음' 이벤트 탐지! IP: {ip}")
            high_severity_alerts.append(log)
        elif log["severity"] == "medium":
            print(f"[주의] 심각도 '중간' 이벤트 탐지. IP: {ip}")
        else:
            print(f"[정보] 심각도 '낮음' 이벤트 탐지. IP: {ip}")

        # IP별 활동 횟수 집계
        if ip in ip_activity:
            ip_activity[ip] += 1
        else:
            ip_activity[ip] = 1
            
    print("\n--- 분석 결과 ---")
    print(f"심각도 '높음' 이벤트 수: {len(high_severity_alerts)}건")
    print(f"IP별 활동 빈도: {ip_activity}")
    print("--- 1. 기본 로그 분석 종료 ---\n")
    
    return high_severity_alerts
```

#### 💻 코드 실행 상세 분석

**1단계 (함수 정의)**: `def` 키워드로 함수를 정의합니다. `logs` 파라미터로 로그 리스트를 받습니다.

**2단계 (변수 초기화)**:
- `high_severity_alerts = []`: 고위험 이벤트를 저장할 빈 리스트
- `ip_activity = {}`: IP별 활동 횟수를 저장할 빈 Dictionary

**3단계 (for 반복문)**: `for log in logs:`는 리스트의 각 Dictionary를 순회합니다.
- 첫 번째 반복: `log`는 첫 번째 이벤트 Dictionary
- 두 번째 반복: `log`는 두 번째 이벤트 Dictionary
- 세 번째 반복: `log`는 세 번째 이벤트 Dictionary

**4단계 (IP 추출)**: `ip = log["source_ip"]`로 현재 로그의 출처 IP를 가져옵니다.

**5단계 (if-elif-else 제어문)**:
- `if log["severity"] == "high"`: 심각도가 "high"인 경우
  - 경고 메시지 출력
  - `high_severity_alerts` 리스트에 로그 추가
- `elif log["severity"] == "medium"`: 심각도가 "medium"인 경우
  - 주의 메시지 출력
- `else`: 그 외의 경우 (low)
  - 정보 메시지 출력

**6단계 (IP 활동 집계)**:
- `if ip in ip_activity`: IP가 이미 Dictionary에 있는지 확인
  - 있으면: 카운트 증가 (`ip_activity[ip] += 1`)
  - 없으면: 새로 추가 (`ip_activity[ip] = 1`)

**7단계 (결과 출력)**: 분석 결과를 정형화된 포맷으로 출력합니다.

**8단계 (반환)**: `high_severity_alerts` 리스트를 반환하여 후속 처리에 사용할 수 있게 합니다.

**최종 결과**:
```
--- 1. 기본 로그 분석 시작 ---
[주의] 심각도 '중간' 이벤트 탐지. IP: 203.0.113.78
[위험] 심각도 '높음' 이벤트 탐지! IP: 198.51.100.22
[정보] 심각도 '낮음' 이벤트 탐지. IP: 203.0.113.78

--- 분석 결과 ---
심각도 '높음' 이벤트 수: 1건
IP별 활동 빈도: {'203.0.113.78': 2, '198.51.100.22': 1}
--- 1. 기본 로그 분석 종료 ---
```

🔐 **보안 노트**: 이 함수는 **실시간 로그 모니터링 시스템**의 핵심 로직입니다. 실제 SIEM(Security Information and Event Management) 시스템에서 이와 유사한 방식으로 로그를 분석하고 위협을 탐지합니다.

### AI 분석 시뮬레이션 함수

```python
import json

def get_ai_analysis_from_logs(high_severity_logs):
    """
    분석이 필요한 로그를 받아 AI에게 JSON으로 보내고,
    규격화된 JSON 응답을 돌려받는 과정을 시뮬레이션하는 함수
    """
    print("--- 2. AI 분석 시뮬레이션 시작 ---")

    # AI에게 보낼 요청 데이터 생성 (Python dict)
    request_data = {
        "model_version": "threat-detector-v1.2",
        "logs_to_analyze": high_severity_logs
    }

    # json.dumps(): Python dict를 JSON 형식의 문자열로 변환
    request_json = json.dumps(request_data, indent=4)
    print("[클라이언트 -> AI 서버] AI 분석 요청 JSON 데이터:")
    print(request_json)
    print("-" * 20)

    # AI 응답 시뮬레이션
    simulated_ai_response_dict = {
        "request_id": "req-a1b2c3d4",
        "analysis_summary": {
            "overall_risk_score": 8.5,
            "threat_pattern_identified": "Coordinated Attack (SQLi from 198.51.100.22)",
            "confidence": 0.92
        },
        "detailed_results": [
            {
                "event_id": "evt-20251028-002",
                "source_ip": "198.51.100.22",
                "threat_type": "SQL Injection",
                "recommended_actions": [
                    "Block IP: 198.51.100.22 at firewall",
                    "Patch web application vulnerability (WAF-Rule-SQLi-001)",
                    "Force user password reset for related accounts"
                ]
            }
        ]
    }
    
    print("[AI 서버 -> 클라이언트] AI 분석 완료 JSON 응답:")
    print(json.dumps(simulated_ai_response_dict, indent=4, ensure_ascii=False))
    print("--- 2. AI 분석 시뮬레이션 종료 ---\n")
    
    return simulated_ai_response_dict
```

#### 💻 코드 실행 상세 분석

**1단계 (JSON 요청 생성)**:
- `request_data` Dictionary 생성: AI 모델 버전과 분석할 로그를 포함
- `json.dumps()`: Python Dictionary를 JSON 문자열로 직렬화(serialization)
- `indent=4`: JSON을 읽기 쉽게 4칸 들여쓰기로 포맷팅

**2단계 (AI 응답 시뮬레이션)**:
- 실제 AI API 호출 대신, 응답 데이터를 직접 생성
- `analysis_summary`: 전체 위험도, 패턴, 신뢰도 포함
- `detailed_results`: 구체적인 위협 정보와 대응 방안

**3단계 (JSON 출력)**:
- `ensure_ascii=False`: 한글 등 유니코드 문자를 그대로 출력
- 클라이언트-서버 간 데이터 교환 흐름을 시뮬레이션

**4단계 (반환)**: AI 분석 결과 Dictionary를 반환

**최종 결과**:
```
--- 2. AI 분석 시뮬레이션 시작 ---
[클라이언트 -> AI 서버] AI 분석 요청 JSON 데이터:
{
    "model_version": "threat-detector-v1.2",
    "logs_to_analyze": [
        {
            "event_id": "evt-20251028-002",
            "timestamp": "2025-10-28T14:05:22Z",
            ...
        }
    ]
}
--------------------
[AI 서버 -> 클라이언트] AI 분석 완료 JSON 응답:
{
    "request_id": "req-a1b2c3d4",
    "analysis_summary": {
        "overall_risk_score": 8.5,
        "threat_pattern_identified": "Coordinated Attack (SQLi from 198.51.100.22)",
        "confidence": 0.92
    },
    ...
}
--- 2. AI 분석 시뮬레이션 종료 ---
```

💡 **중요!**: 이 패턴은 **Gen AI와의 통합**을 시뮬레이션합니다. 실제로 OpenAI API, Claude API 등과 통신할 때 이와 동일한 방식으로 JSON을 주고받습니다.

🔐 **보안 노트**: JSON 직렬화/역직렬화 시 주의사항:
1. **입력 검증**: 외부에서 받은 JSON은 반드시 검증 후 파싱
2. **에러 처리**: `json.loads()`는 잘못된 JSON에 대해 예외 발생
3. **인코딩**: 한글 등 특수 문자는 `ensure_ascii=False` 옵션 필요

### AI 분석 결과 처리 함수

```python
def process_ai_verdict(ai_result):
    """
    AI의 분석 결과(dict)를 받아 후속 조치를 처리하는 함수
    """
    print("--- 3. AI 분석 결과 기반 후속 조치 시작 ---")
    
    summary = ai_result["analysis_summary"]
    
    # if 제어문: AI가 판단한 위험도 점수에 따라 대응 수준 결정
    if summary["overall_risk_score"] > 7.0:
        print(f"!! 긴급 대응 필요 !! 전체 위험도: {summary['overall_risk_score']}")
        print(f"탐지된 위협 패턴: {summary['threat_pattern_identified']}")
        
        # for 반복문: AI가 추천한 조치 사항들을 하나씩 출력
        for result in ai_result["detailed_results"]:
            print(f"\n이벤트(ID: {result['event_id']})에 대한 조치 권고:")
            for action in result["recommended_actions"]:
                print(f"  - [조치 실행] {action}")
    else:
        print("탐지된 특이사항 없음. 모니터링 유지.")
        
    print("--- 3. AI 분석 결과 기반 후속 조치 종료 ---")
```

#### 💻 코드 실행 상세 분석

**1단계 (요약 정보 추출)**: `summary = ai_result["analysis_summary"]`로 전체 분석 요약에 접근합니다.

**2단계 (위험도 평가)**:
- `if summary["overall_risk_score"] > 7.0`: 위험도가 7.0을 초과하면 긴급 대응
- 위험도 점수와 탐지된 위협 패턴을 출력

**3단계 (중첩 반복문)**:
- 외부 for문: `detailed_results` 리스트의 각 결과를 순회
- 내부 for문: 각 결과의 `recommended_actions` 리스트를 순회
- 모든 권장 조치를 순서대로 출력

**4단계 (else 분기)**: 위험도가 낮으면 단순 모니터링만 유지

**최종 결과**:
```
--- 3. AI 분석 결과 기반 후속 조치 시작 ---
!! 긴급 대응 필요 !! 전체 위험도: 8.5
탐지된 위협 패턴: Coordinated Attack (SQLi from 198.51.100.22)

이벤트(ID: evt-20251028-002)에 대한 조치 권고:
  - [조치 실행] Block IP: 198.51.100.22 at firewall
  - [조치 실행] Patch web application vulnerability (WAF-Rule-SQLi-001)
  - [조치 실행] Force user password reset for related accounts
--- 3. AI 분석 결과 기반 후속 조치 종료 ---
```

🔐 **보안 노트**: 이 함수는 **자동화된 사고 대응(Automated Incident Response)**의 핵심입니다. 실제 SOC(Security Operations Center)에서는:
1. AI가 위협을 분석하고 권장 조치를 제시
2. 시스템이 자동으로 방화벽 규칙 추가, IP 차단 등 실행
3. 심각한 경우 담당자에게 알림 전송
4. 모든 조치를 로그로 기록

### 메인 실행 로직

```python
if __name__ == "__main__":
    # 1단계: 기본 분석 수행 및 심각도 '높음' 이벤트 추출
    critical_logs = analyze_raw_logs(raw_security_logs)
    
    # 2단계: '높음' 이벤트만 AI에게 보내 분석 요청
    if critical_logs:
        ai_analysis_result = get_ai_analysis_from_logs(critical_logs)
        
        # 3단계: AI의 분석 결과를 바탕으로 후속 조치 수행
        process_ai_verdict(ai_analysis_result)
    else:
        print("AI 분석으로 넘길 심각한 이벤트가 없습니다.")
```

#### 💻 코드 실행 상세 분석

**1단계 (모듈 실행 확인)**: `if __name__ == "__main__":`는 이 파일이 직접 실행될 때만 아래 코드를 실행합니다.

**2단계 (기본 분석)**: `analyze_raw_logs()` 함수를 호출하여 모든 로그를 분석하고, 고위험 로그만 반환받습니다.

**3단계 (조건부 AI 분석)**:
- `if critical_logs:`: 고위험 로그가 있는 경우에만 AI 분석 수행
- 리소스를 절약하고 중요한 이벤트에만 집중

**4단계 (후속 조치)**: AI 분석 결과를 받아 자동 대응 수행

**5단계 (예외 처리)**: 고위험 이벤트가 없으면 AI 분석을 건너뜁니다.

💡 **중요!**: 이 구조는 **파이프라인(Pipeline)** 방식의 데이터 처리를 보여줍니다:
```
원시 로그 → 기본 분석 → 필터링 → AI 분석 → 자동 대응
```

실제 보안 시스템에서 수백만 개의 로그를 처리할 때 이러한 단계별 필터링은 필수적입니다.


## 📚 종합 정리 및 핵심 요약

### 오늘 배운 핵심 개념

#### 1. 변수와 데이터 타입
- **변수**: 데이터를 담는 그릇, 명명 규칙 준수 필수
- **Numeric**: `int`, `float` - 숫자 연산
- **Sequence**: `list` - 가변, 순서 있음
- **Text**: `str` - 불변, 인덱싱/슬라이싱 가능
- **Mapping**: `dict` - Key-Value, 가장 중요!
- **Set**: 중복 불가, 빠른 검색
- **Tuple**: 불변, 안전한 데이터 저장
- **Boolean**: 조건 판단, Truthy/Falsy

#### 2. 출력과 포매팅
- **기본 print()**: 콤마로 구분, `sep` 파라미터
- **f-string**: 가장 현대적, Python 3.6+
- **format()**: 안전한 치환 방식
- **% 연산자**: C 스타일, 보안 주의 필요
- **repr()**: 디버깅/로깅용, 특수 문자 그대로 표시
- **다중 라인**: 템플릿 기반 보고서
- **숫자 포맷**: 천 단위, 정렬, 소수점

#### 3. 보안 관점의 핵심
- **정형화된 로그**: 파싱 용이, 변조 탐지
- **Set 활용**: 중복 로그인 방지, 빠른 검색
- **마스킹**: 민감 정보 보호
- **입력 검증**: 형 변환과 예외 처리
- **데이터 구조**: `[{}, {}, {}]` - 리스트 안 딕셔너리

### 보안 관점에서 바라본 Python

강사님께서 반복적으로 강조하신 핵심 메시지:

> "파이썬을 이미 아는 분들도, 단순히 문법을 아는 것이 아니라 **'보안적으로는 어떻게 바라봐야 하지?'**라는 관점으로 접근해야 합니다. 이 수업은 일반 프로그래밍 수업이 아닙니다."

#### 보안 전문가로서 고려해야 할 사항들:

1. **입력 검증**
   - 모든 외부 입력은 신뢰할 수 없음
   - 타입 체크와 범위 검증 필수
   - 예외 처리로 안전하게 처리

2. **로그 관리**
   - 정형화된 포맷으로 일관성 유지
   - 민감 정보는 마스킹 처리
   - `repr()`로 숨겨진 문자 확인
   - 변조 탐지를 위한 체크섬

3. **데이터 구조 선택**
   - Set: 중복 방지, 빠른 검색 (O(1))
   - Tuple: 불변 데이터 보호
   - Dict: 구조화된 로그와 설정

4. **코드 안전성**
   - % 연산자: 포맷 스트링 공격 주의
   - 예약어 회피: 내장 타입을 변수명으로 사용 금지
   - 예외 처리: 모든 외부 상호작용에 try-except

### 실전 적용 가이드

#### 보안 로그 시스템 구축

```python
# 1. 로그 템플릿 정의
LOG_TEMPLATE = "[{timestamp}] [{level}] User={user}, IP={ip}, Action={action}, Result={result}"

# 2. 로그 생성 함수
def create_security_log(user, ip, action, result, level="INFO"):
    import datetime
    timestamp = datetime.datetime.now().isoformat()
    return LOG_TEMPLATE.format(
        timestamp=timestamp,
        level=level,
        user=mask_username(user),  # 마스킹
        ip=ip,
        action=action,
        result=result
    )

# 3. 마스킹 함수
def mask_username(username):
    if len(username) <= 2:
        return "*" * len(username)
    return username[0] + "*" * (len(username) - 2) + username[-1]

# 4. 로그 분석 함수
def analyze_failed_logins(logs):
    failed_attempts = {}
    for log in logs:
        if log['result'] == 'FAILED':
            ip = log['ip']
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
    
    # 5회 이상 실패 시 경고
    for ip, count in failed_attempts.items():
        if count >= 5:
            print(f"[경고] IP {ip}에서 {count}회 로그인 실패")
```

#### 권한 관리 시스템

```python
# Set을 활용한 효율적인 권한 체크
ADMIN_PERMISSIONS = {"read", "write", "delete", "admin"}
USER_PERMISSIONS = {"read", "write"}
GUEST_PERMISSIONS = {"read"}

def check_permission(user_role, required_permission):
    role_permissions = {
        'admin': ADMIN_PERMISSIONS,
        'user': USER_PERMISSIONS,
        'guest': GUEST_PERMISSIONS
    }
    
    permissions = role_permissions.get(user_role, set())
    return required_permission in permissions  # O(1) 시간복잡도

# 사용 예
if check_permission('user', 'delete'):
    print("삭제 권한 있음")
else:
    print("권한 부족")
```

### 다음 학습을 위한 준비

오늘 배운 내용을 바탕으로 다음에 학습할 내용들:

1. **제어문**: `if`, `for`, `while` - 로그 분석 자동화
2. **함수**: `def`, 매개변수, 반환값 - 코드 재사용
3. **예외 처리**: `try-except` - 안전한 에러 핸들링
4. **파일 입출력**: 로그 파일 읽기/쓰기
5. **정규 표현식**: 패턴 매칭으로 로그 파싱
6. **모듈과 패키지**: 코드 구조화

### 강사님의 당부 말씀

> "긴 레이스를 하시는 것이기 때문에 기록보다 머리의 기억력이 더 오래 남습니다. 반드시 배운 내용을 노션이나 브이로그에 정리하세요. 자기 자신의 머리만 믿고 머릿속으로만 기억하려 하면 안 됩니다."

### 복습 체크리스트

오늘 배운 내용을 제대로 이해했는지 확인해보세요:

- [ ] Python의 기본 데이터 타입 6가지를 설명할 수 있다
- [ ] List와 Tuple의 차이점을 알고 있다
- [ ] Dictionary의 중첩 접근 방법을 이해한다
- [ ] Set의 집합 연산 4가지를 활용할 수 있다
- [ ] f-string, format(), % 연산자의 차이를 안다
- [ ] repr() 함수의 보안적 의미를 이해한다
- [ ] 정형화된 로그의 중요성을 설명할 수 있다
- [ ] List 안에 Dict가 있는 구조를 다룰 수 있다
- [ ] Boolean의 Truthy/Falsy 개념을 안다
- [ ] 보안 관점에서 코드를 바라볼 수 있다

### 실습 과제

스스로 다음 코드를 작성해보세요:

1. **로그 필터링 시스템**
   - 여러 개의 로그 Dictionary를 List에 저장
   - 특정 조건(예: 심각도, IP, 시간대)으로 필터링
   - 결과를 정형화된 포맷으로 출력

2. **사용자 권한 검증**
   - Set을 활용한 권한 시스템 구현
   - 역할별 권한 정의
   - 권한 체크 함수 작성

3. **데이터 마스킹 유틸리티**
   - 이메일 주소 마스킹 (a***@example.com)
   - 전화번호 마스킹 (010-****-5678)
   - 주민등록번호 마스킹 (123456-*******)


## 🎓 마무리

오늘 강의에서 배운 내용은 단순한 Python 문법이 아닙니다. **보안 전문가로서 Python을 어떻게 활용할 것인가**에 대한 관점과 실전 기술을 익혔습니다.

특히 강조되었던 부분들:
- 정형화된 로그의 중요성
- Set을 활용한 효율적인 데이터 관리
- repr()를 통한 디버깅
- 입력 검증과 마스킹
- 리스트 안 딕셔너리 구조의 활용

이 모든 것들이 **실제 보안 시스템 구축**에 직접 적용되는 핵심 기술들입니다.

강사님의 마지막 당부:
> "여러분은 지금 긴 레이스를 시작했습니다. 오늘 배운 내용을 반드시 복습하고, 자신만의 방식으로 정리하세요. 그리고 항상 '보안 관점'에서 생각하는 습관을 들이세요."

**다음 강의에서 만나요!** 🚀


*본 강의 노트는 2025년 10월 27일 보안 파이썬 Day 01 강의를 바탕으로 작성되었습니다.*
*강의 내용, 코드 예제, 보안 노트를 모두 포함한 종합 학습 자료입니다.*


## 📎 부록: 주요 코드 스니펫 모음

### 예약어 확인
```python
import keyword
print(keyword.kwlist)
```

### 데이터 타입 체크
```python
print(type(variable_name))
```

### List 슬라이싱
```python
my_list[start:stop:step]
my_list[::2]  # 짝수 인덱스만
my_list[1::2] # 홀수 인덱스만
```

### Dictionary 접근
```python
my_dict["key"]
my_dict.get("key", default_value)
```

### Set 연산
```python
set1 | set2  # 합집합
set1 & set2  # 교집합
set1 - set2  # 차집합
set1 ^ set2  # 대칭 차집합
```

### 포매팅
```python
# f-string
f"Name: {name}, Score: {score:.2f}"

# format()
"Name: {}, Score: {}".format(name, score)

# % 연산자
"Name: %s, Score: %.2f" % (name, score)
```

### 로그 생성
```python
log_msg = f"[{level}] User={user}, IP={ip}, Event={event}"
```

이상으로 2025년 10월 27일 보안 파이썬 Day 01 강의 노트를 마칩니다! 📝