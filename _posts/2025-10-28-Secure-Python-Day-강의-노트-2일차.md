
--- 
title: "📝 Secure Python Day 02 강의 노트 (2일차)"
date: 2025-10-28
excerpt: "강사: 임정섭 강사님"
categories:
  - Python
tags:
  - Python
  - SK_Rookies
---

# 📝 Secure Python Day 02 강의 노트 (2일차)

**강의일자**: 2025년 10월 28일  
**주제**: 변수 타입 응용, 열거형, 제어/반복 구문, 함수, 보안 코딩  
**강사**: 임정섭 강사님

---

## 📚 학습 내용 복습

오늘은 2일차 수업으로, 어제 배웠던 파이썬의 기본 변수 타입들을 더욱 깊이 있게 활용하고 응용하는 시간을 가졌습니다. 어제 파이썬이 **함수 기반의 언어**이면서 동시에 **객체지향 언어**라는 점을 배웠는데, 오늘은 이를 바탕으로 실무에서 자주 사용되는 패턴들과 보안 관점에서의 코딩 방법을 학습했습니다.

강사님께서 아침에 비둘기 똥을 맞으셨다는 재미있는 에피소드로 수업을 시작하셨는데요, 비둘기 똥을 맞을 확률이 약 1.2%라고 하시면서 로또 한 장 사보시겠다는 농담으로 분위기를 밝게 만들어주셨습니다!

---

## 🎯 오늘의 학습 목표

1. **변수 타입 응용**: 문자열, 리스트, 딕셔너리 등의 고급 활용법
2. **열거형(Enumerable)**: `range` 객체와 반복 가능한 객체들
3. **제어 구문**: `if`, `elif`, `else`를 활용한 조건 분기
4. **반복문**: `for`문과 `in` 연산자 활용
5. **함수(Function)**: 사용자 정의 함수와 매개변수, 반환값
6. **보안 코딩**: 얕은 복사의 위험성과 입력값 검증

---

## 📖 Section 1: 파이썬의 타입 시스템 심화 이해

### 1.1 파이썬의 특별한 타입 시스템

강사님께서 오늘 수업 초반에 파이썬의 타입 시스템에 대해 매우 중요한 개념을 설명해주셨습니다.

#### 1.1.1 기본 타입 vs 참조 타입

일반적인 프로그래밍 언어에서 변수는 두 가지 타입으로 나뉩니다:

- **기본 타입(Primitive Type)**: 데이터 자체를 직접 담는 타입
- **참조 타입(Reference Type)**: 데이터가 저장된 메모리 주소값을 담는 타입

하지만 파이썬은 다릅니다!

> 💡 **중요!**: 파이썬은 기본 타입이 존재하지 않고, **모든 데이터 타입이 참조 타입**입니다. 즉, 모든 변수는 값이 아닌 **메모리 주소값**을 담고 있습니다.

#### 1.1.2 객체지향 프로그래밍(OOP)과 파이썬

파이썬은 **OOP(Object Oriented Programming)** 언어입니다.

**OOP의 핵심 개념:**
- **실세계의 객체(Object)**: 우리 눈에 보이는 모든 것 (사람, 모니터, 키보드 등)
- **프로그램 영역으로의 구현**: 이러한 실세계 객체를 프로그램에서 사용하고 싶음
- **클래스(Class)**: 실세계 객체를 프로그램 영역에서 사용할 수 있도록 변환하는 **템플릿**
- **인스턴스(Instance)**: 클래스를 통해 생성된 프로그램 영역의 객체

```
실세계 객체(Object) → 클래스(Class) 템플릿 → 프로그램 영역의 인스턴스(Instance)
```

**객체의 분석 방법:**

임정섭 강사님이라는 실세계 객체를 예로 들면:
- **명사적 특징**: 성별, 이름, 나이, 직업 → 클래스에서 **변수**로 정의
- **동사적 특징**: 강의하다, 숨쉬다, 담배피다, 걷다 → 클래스에서 **메서드**로 정의

> 📌 **노트**: 클래스에 정의된 변수나 메서드는 클래스의 소유가 아닌 **인스턴스의 소유**가 됩니다. 따라서 `.` 연산자를 통해 접근합니다.

#### 1.1.3 함수(Function) vs 메서드(Method)

- **함수(Function)**: 단독으로 실행 가능 (예: `print()`, `len()`, `max()`)
- **메서드(Method)**: 인스턴스에 종속되어 `.` 연산자로 호출 (예: `list.append()`, `str.upper()`)

---

## 📝 Section 2: 문자열(String) 타입 심화

### 2.1 문자열의 기본 이해

문자열 변수에 값을 할당하면, 변수의 타입은 자동으로 `str` 클래스의 인스턴스가 됩니다.

```python
url = 'http://www.naver.com'
print('type - ', type(url))  # <class 'str'>
```

#### 💻 코드 실행 상세 분석

**1단계 (변수 할당)**: `url` 변수에 문자열 리터럴 `'http://www.naver.com'`이 할당됩니다. 이 순간 `url` 변수는 `str` 타입의 인스턴스가 됩니다.

**2단계 (타입 확인)**: `type(url)` 함수를 호출하면 `<class 'str'>`이 반환됩니다. 이는 `url`이 `str` 클래스의 인스턴스임을 의미합니다.

**최종 결과**: 출력 결과는 `type -  <class 'str'>`입니다. 파이썬의 문자열은 클래스 기반의 참조 타입입니다.

### 2.2 문자열 슬라이싱(Slicing) 활용

문자열에서 특정 부분만 추출하고 싶을 때 슬라이싱을 사용합니다.

```python
url = 'http://www.naver.com'
print('com - ', url[-3:])  # 'com'
```

#### 💻 코드 실행 상세 분석

**1단계**: `url[-3:]`는 음수 인덱싱을 사용합니다. `-3`은 뒤에서 세 번째 문자부터를 의미합니다.

**2단계**: 콜론(`:`) 뒤에 아무것도 없으면 끝까지를 의미합니다.

**최종 결과**: 문자열의 마지막 3글자인 `'com'`이 추출됩니다.

### 2.3 문자열의 주요 메서드들

문자열 인스턴스는 다양한 메서드를 소유하고 있습니다. `dir()` 함수로 확인할 수 있습니다.

```python
print('instance method - ', dir(url))
```

이 명령어를 실행하면 매우 많은 메서드 목록이 출력됩니다:
- `capitalize()`, `find()`, `strip()`, `upper()`, `lower()`, `replace()`, `split()` 등

#### 2.3.1 `find()` 메서드 - 문자열 검색

특정 문자열의 위치(인덱스)를 찾아주는 메서드입니다.

```python
url = 'http://www.naver.com'
print('find - ', url.find('com'))  # 17
print('com - ', url[url.find('com'):])  # 'com'
```

#### 💻 코드 실행 상세 분석

**1단계**: `url.find('com')`은 `url` 문자열에서 `'com'`이라는 부분 문자열을 찾습니다.

**2단계**: `'com'`은 인덱스 17번 위치에서 시작됩니다. (`h`가 0번, `t`가 1번... 순서로 세어가면 17번)

**3단계**: `url[17:]`는 17번 인덱스부터 끝까지 슬라이싱합니다.

**최종 결과**: `'com'`이 출력됩니다. 이 방법은 동적으로 문자열의 특정 부분을 찾아 추출할 때 매우 유용합니다.

> 📌 **노트**: 이러한 패턴은 URL 파싱, 도메인 추출, 파일 확장자 확인 등 실무에서 자주 사용됩니다.

#### 2.3.2 `strip()` 메서드 - 공백 제거

문자열 양 끝의 공백을 제거하는 메서드입니다.

```python
companyName = '     SK      '
print('type - ', type(companyName), 'len - ', len(companyName))  # 길이: 13
print(companyName.strip(' '), len(companyName.strip(' ')))  # 'SK', 길이: 2
```

#### 💻 코드 실행 상세 분석

**1단계**: `companyName` 변수에는 앞뒤로 많은 공백이 포함된 문자열이 저장됩니다.

**2단계**: `len(companyName)`은 공백을 포함한 전체 길이를 반환합니다. (공백 5개 + 'SK' 2글자 + 공백 6개 = 13)

**3단계**: `companyName.strip(' ')`는 문자열 양 끝의 공백을 모두 제거합니다.

**4단계**: 제거 후 `len()`을 다시 호출하면 2가 반환됩니다. (순수하게 'SK'만 남음)

**최종 결과**: 공백이 제거된 `'SK'` 문자열과 길이 2가 출력됩니다.

> 🔐 **보안 노트**: 사용자 입력값을 받을 때 `strip()` 메서드는 필수적입니다. 악의적인 사용자가 의도적으로 공백을 삽입하여 입력값 검증을 우회하려는 시도를 방지할 수 있습니다. 예를 들어, ID 입력 시 `"admin    "`과 같이 공백을 포함시켜 입력하는 경우를 방어할 수 있습니다.

#### 2.3.3 `capitalize()` 메서드 - 첫 글자 대문자화

문자열의 첫 번째 글자만 대문자로 변환하는 메서드입니다.

```python
companyName = 'samsung'
print('첫번째 문자를 대문자로 ', companyName.capitalize())  # 'Samsung'
```

#### 💻 코드 실행 상세 분석

**1단계**: `companyName` 변수에 소문자로만 이루어진 `'samsung'`이 저장됩니다.

**2단계**: `capitalize()` 메서드가 호출되면 첫 글자 `'s'`를 대문자 `'S'`로 변환합니다.

**3단계**: 나머지 글자들은 소문자로 유지됩니다.

**최종 결과**: `'Samsung'`이 출력됩니다. 이 메서드는 이름이나 회사명을 표준화할 때 유용합니다.

#### 2.3.4 `endswith()` 메서드 - 문자열 끝 확인

문자열이 특정 문자열로 끝나는지 확인하는 메서드입니다.

```python
fileName = 'report.xls'
print('flag - ', fileName.endswith('.xls'))  # True
```

#### 💻 코드 실행 상세 분석

**1단계**: `fileName` 변수에 `'report.xls'` 문자열이 저장됩니다.

**2단계**: `endswith('.xls')` 메서드는 문자열이 `'.xls'`로 끝나는지 검사합니다.

**3단계**: 실제로 `'report.xls'`는 `'.xls'`로 끝나므로 조건이 참입니다.

**최종 결과**: `True`가 반환되고 출력됩니다.

> 🔐 **보안 노트**: 파일 업로드 기능을 구현할 때 `endswith()` 메서드는 매우 중요합니다. 허용된 확장자만 업로드하도록 검증하여 악성 파일 업로드를 방지할 수 있습니다. 예를 들어:
> ```python
> allowed_extensions = ['.jpg', '.png', '.pdf']
> if any(fileName.endswith(ext) for ext in allowed_extensions):
>     # 안전한 파일 - 업로드 허용
> else:
>     # 위험한 파일 - 업로드 거부
> ```
> 하지만 단순히 확장자만 확인하는 것은 불충분합니다. 파일의 실제 MIME 타입과 매직 넘버도 함께 검증해야 합니다.

---

## 🔧 Section 3: 함수(Function) 정의와 활용

### 3.1 함수의 필요성

프로그래밍에서 같은 코드를 반복해서 작성하는 것은 비효율적입니다. 강사님께서는 "모아서 한번에 출력하고 싶다"는 필요성에서 함수가 탄생했다고 설명하셨습니다.

### 3.2 함수의 4가지 유형

함수는 매개변수와 반환값의 유무에 따라 4가지로 분류됩니다:

1. **매개변수 받고 반환 X**: 입력은 받지만 결과를 돌려주지 않음 (의미가 적음)
2. **매개변수 받고 반환 O**: 입력을 받아 처리 후 결과를 돌려줌 (가장 일반적)
3. **매개변수 없지만 반환 O**: 입력 없이 결과만 돌려줌
4. **매개변수도 없고 반환도 X**: 입력도 없고 결과도 없음 (의미가 거의 없음)

### 3.3 사용자 정의 함수 작성

#### 3.3.1 기본 함수 정의

파이썬에서 함수는 `def` 키워드를 사용하여 정의합니다.

```python
# worker function (작업자 함수)
def printCoin():
    print('코인')

# caller (호출자)
printCoin()  # 출력: 코인
```

#### 💻 코드 실행 상세 분석

**1단계 (함수 정의)**: `def printCoin():`은 `printCoin`이라는 이름의 함수를 정의합니다. 괄호 `()`는 매개변수가 없음을 의미합니다.

**2단계 (함수 본문)**: 들여쓰기된 `print('코인')` 코드가 함수의 본문(body)입니다. 이 코드는 함수가 호출될 때 실행됩니다.

**3단계 (함수 호출)**: `printCoin()`을 실행하면 함수가 호출되고 본문의 코드가 실행됩니다.

**최종 결과**: `'코인'`이 출력됩니다.

> 📌 **노트**: 강사님께서 "worker function"과 "caller"라는 용어를 사용하셨는데, 이는 함수를 정의하는 부분과 실제로 호출하는 부분을 구분하기 위함입니다. 함수는 정의만으로는 실행되지 않고, 반드시 누군가가 호출해야 동작합니다.

#### 3.3.2 매개변수와 반환값이 있는 함수

```python
def greet(name):
    return f"Hello~ {name}"

result = greet('jslim')
print(result, type(result))  # Hello~ jslim <class 'str'>
```

#### 💻 코드 실행 상세 분석

**1단계 (함수 정의)**: `def greet(name):`에서 `name`은 매개변수(parameter)입니다. 함수가 호출될 때 값을 전달받습니다.

**2단계 (f-string 사용)**: `f"Hello~ {name}"`은 f-string 문법으로, `{name}` 부분에 매개변수의 값이 삽입됩니다.

**3단계 (return 문)**: `return` 키워드는 함수의 실행을 종료하고 값을 호출자에게 돌려줍니다.

**4단계 (함수 호출)**: `greet('jslim')`을 호출하면 `'jslim'`이 `name` 매개변수로 전달됩니다.

**5단계 (반환값 저장)**: 함수가 반환한 `"Hello~ jslim"` 문자열이 `result` 변수에 저장됩니다.

**최종 결과**: `Hello~ jslim <class 'str'>`이 출력됩니다. 반환된 값의 타입도 `str` 클래스입니다.

---

## 📊 Section 4: 리스트(List) 타입 심화

### 4.1 리스트의 기본 특성

리스트는 파이썬에서 가장 많이 사용되는 자료구조 중 하나입니다.

```python
lst = [1, 2, 3, 4, 5, 6, 7]
print('type - ', type(lst))  # <class 'list'>
```

### 4.2 리스트 관련 내장 함수들

리스트에 사용할 수 있는 유용한 내장 함수들이 많습니다.

```python
lst = [1, 2, 3, 4, 5, 6, 7]
print('max - ', max(lst))   # 7
print('min - ', min(lst))   # 1
print('sum - ', sum(lst))   # 28
print('mean - ', sum(lst) / len(lst), type(int(sum(lst) / len(lst))))  # 4.0, <class 'int'>
```

#### 💻 코드 실행 상세 분석

**1단계**: `max(lst)` 함수는 리스트에서 가장 큰 값을 찾아 반환합니다. → 7

**2단계**: `min(lst)` 함수는 리스트에서 가장 작은 값을 찾아 반환합니다. → 1

**3단계**: `sum(lst)` 함수는 리스트의 모든 요소를 합산합니다. → 1+2+3+4+5+6+7 = 28

**4단계**: 평균값 계산은 `sum(lst) / len(lst)`로 합계를 개수로 나눕니다. → 28 / 7 = 4.0

**5단계**: `int()` 함수로 실수를 정수로 변환합니다. → 4

**최종 결과**: 최댓값, 최솟값, 합계, 평균이 모두 정확하게 계산되어 출력됩니다.

> 📌 **노트**: 이러한 통계 함수들은 데이터 분석의 기초입니다. 실무에서 로그 데이터나 센서 데이터를 분석할 때 매우 자주 사용됩니다.

---

## 🔄 Section 5: 참조 타입과 복사의 이해

### 5.1 참조 타입의 특성

앞서 배웠듯이 파이썬의 모든 타입은 참조 타입입니다. 이는 변수가 값이 아닌 **메모리 주소**를 담는다는 의미입니다.

```python
lstTmp01 = [1, 2, 3]  # 참조타입
lstTmp02 = [1, 2, 3]  # 참조타입

print('instance address - ', id(lstTmp01), id(lstTmp02))
print('is - 주소번지를 비교하는 연산자 ', lstTmp01 is lstTmp02)  # False
```

#### 💻 코드 실행 상세 분석

**1단계**: `lstTmp01 = [1, 2, 3]`이 실행되면 메모리 어딘가에 `[1, 2, 3]` 리스트 객체가 생성되고, `lstTmp01`은 그 주소를 가리킵니다.

**2단계**: `lstTmp02 = [1, 2, 3]`이 실행되면 또 다른 메모리 공간에 새로운 `[1, 2, 3]` 리스트 객체가 생성됩니다.

**3단계**: `id()` 함수는 객체의 메모리 주소를 반환합니다. 두 주소는 서로 다릅니다.

**4단계**: `is` 연산자는 두 변수가 같은 객체를 가리키는지 (같은 주소인지) 확인합니다.

**최종 결과**: 두 리스트는 내용은 같지만 서로 다른 객체이므로 `is` 연산의 결과는 `False`입니다.

> 💡 **중요!**: `==` 연산자는 값의 동등성을, `is` 연산자는 객체의 동일성(같은 메모리 주소)을 비교합니다.

### 5.2 얕은 복사(Shallow Copy)

```python
lstTmp03 = lstTmp01  # 얕은 복사

print('is - 주소번지를 비교하는 연산자 ', lstTmp01 is lstTmp03)  # True
```

#### 💻 코드 실행 상세 분석

**1단계**: `lstTmp03 = lstTmp01`은 단순 대입 연산입니다.

**2단계**: 이 연산은 `lstTmp01`이 가리키는 메모리 주소를 `lstTmp03`에 **복사**합니다.

**3단계**: 결과적으로 `lstTmp01`과 `lstTmp03`은 **같은 객체**를 가리키게 됩니다.

**최종 결과**: `is` 연산의 결과는 `True`입니다. 두 변수는 완전히 동일한 객체를 참조합니다.

> 🔐 **보안 노트**: 얕은 복사는 매우 위험합니다! 한 변수를 수정하면 다른 변수도 영향을 받기 때문입니다. 특히 민감한 사용자 정보(세션, 토큰, 개인정보)를 다룰 때는 절대 얕은 복사를 사용해서는 안 됩니다.

### 5.3 깊은 복사(Deep Copy)

얕은 복사의 문제를 해결하기 위해 **깊은 복사**를 사용합니다.

```python
from copy import copy, deepcopy
import random

original = [[1, 2], [3, 4]]

shallowCopy = copy(original)
deepCopy = deepcopy(original)

original[0][0] = 2

print('shallowCopy - ', shallowCopy)  # [[2, 2], [3, 4]]
print('deepCopy - ', deepCopy)        # [[1, 2], [3, 4]]
```

#### 💻 코드 실행 상세 분석

**1단계 (import)**: `from copy import copy, deepcopy`로 복사 관련 함수들을 가져옵니다. 기본 모듈이 아닌 것들은 반드시 `import`해야 합니다.

**2단계 (원본 생성)**: `original = [[1, 2], [3, 4]]`는 2차원 리스트(리스트 안에 리스트)를 생성합니다.

**3단계 (얕은 복사)**: `copy(original)`은 새로운 리스트 컨테이너를 만들지만, 내부 요소들은 같은 객체를 참조합니다.

**4단계 (깊은 복사)**: `deepcopy(original)`은 완전히 새로운 객체를 만들며, 내부 요소들도 모두 새로 복사됩니다.

**5단계 (원본 수정)**: `original[0][0] = 2`로 첫 번째 리스트의 첫 번째 요소를 수정합니다.

**6단계 (얕은 복사 영향)**: `shallowCopy`는 내부 리스트를 공유하므로 함께 변경됩니다. → `[[2, 2], [3, 4]]`

**7단계 (깊은 복사 불변)**: `deepCopy`는 완전히 독립적이므로 영향을 받지 않습니다. → `[[1, 2], [3, 4]]`

**최종 결과**: 얕은 복사는 원본 변경에 영향을 받지만, 깊은 복사는 영향을 받지 않습니다.

> 💡 **중요!**: 
> - **얕은 복사(Shallow Copy)**: 새로운 컨테이너를 만들지만 요소의 주소는 동일
> - **깊은 복사(Deep Copy)**: 완전히 새로운 객체를 재귀적으로 복사

강사님께서 이 부분을 매우 강조하셨습니다:

> 🔐 **보안 노트**: 
> 1. **얕은 복사의 위험성**: 예기치 않게 공유되는 변수의 수정 가능성 → 공유 객체의 무분별한 참조
> 2. **민감한 데이터 처리**: 사용자 세션 정보나 토큰 정보를 복사할 때 얕은 복사는 **절대 금지**
> 3. **깊은 복사 필수**: 민감한 데이터를 복사하고 오래 유지해야 한다면 무조건 **Deep Copy 활용**
> 4. **불필요한 복사 피하기**: 보안 관점에서 코딩할 때 불필요한 복사는 최소화해야 함

### 5.4 복사의 취약점 - 실전 예제

#### 5.4.1 불변(Immutable) 타입의 경우

```python
userData = {'id': 1, 'token': 'secret1234'}
cache = copy(userData)

userData['token'] = 'secret4321'  # 값 변경

print(cache['token'])  # 'secret1234' (원본 변경되지 않음)
```

#### 💻 코드 실행 상세 분석

**1단계**: 딕셔너리 `userData`가 생성되고, `'token'` 키의 값으로 문자열 `'secret1234'`가 저장됩니다.

**2단계**: `copy(userData)`로 얕은 복사를 수행합니다. 딕셔너리 자체는 새로 만들어지지만, 값들은 같은 객체를 가리킵니다.

**3단계**: `userData['token'] = 'secret4321'`에서 **새로운 문자열 객체**가 생성됩니다. 왜냐하면 문자열(str)은 **불변(Immutable)** 타입이기 때문입니다.

**4단계**: `userData`의 `'token'` 키는 이제 새로운 문자열 `'secret4321'`을 가리킵니다.

**5단계**: 하지만 `cache`는 여전히 원래의 문자열 `'secret1234'`를 가리킵니다.

**최종 결과**: `cache['token']`은 `'secret1234'`를 출력합니다. 불변 타입은 얕은 복사에서도 안전합니다.

#### 5.4.2 가변(Mutable) 타입의 경우 - 위험!

```python
userData = {'id': 1, 'roles': ['admin', 'user']}
cache = copy(userData)  # 얕은 복사

cache['roles'].append('guest')  # cache를 수정

print(userData['roles'])  # ['admin', 'user', 'guest'] - 원본도 변경됨!
```

#### 💻 코드 실행 상세 분석

**1단계**: 딕셔너리 `userData`가 생성되고, `'roles'` 키의 값으로 리스트 `['admin', 'user']`가 저장됩니다.

**2단계**: `copy(userData)`로 얕은 복사를 수행합니다. 딕셔너리는 새로 만들어지지만, `'roles'` 리스트는 **같은 객체를 가리킵니다**.

**3단계**: `cache['roles'].append('guest')`를 실행하면, **공유되고 있는 리스트**에 `'guest'`가 추가됩니다.

**4단계**: 리스트(list)는 **가변(Mutable)** 타입이므로, 같은 메모리 위치의 값이 직접 수정됩니다.

**5단계**: `userData`의 `'roles'`와 `cache`의 `'roles'`는 같은 리스트를 가리키므로 둘 다 변경됩니다.

**최종 결과**: `userData['roles']`를 출력하면 `['admin', 'user', 'guest']`가 나옵니다. 원본이 의도치 않게 변경되었습니다!

> 💡 **중요!**: 
> - **불변(Immutable) 타입**: Numeric, text, tuple, bool, str → 값 변경 시 **새로운 객체 생성**
> - **가변(Mutable) 타입**: list, dict, set → 값 자체를 **직접 변경 가능**

> 🔐 **보안 노트**: 이러한 얕은 복사의 취약점은 실제 보안 사고로 이어질 수 있습니다. 예를 들어:
> - 사용자 A의 권한 정보를 복사하여 사용자 B에게 할당했는데, 얕은 복사로 인해 A의 권한을 수정하면 B의 권한도 함께 변경되는 경우
> - 세션 정보를 캐싱할 때 얕은 복사를 사용하면, 한 세션의 토큰이 변경될 때 다른 세션에도 영향을 줄 수 있음
> - 로그 데이터를 저장할 때 얕은 복사를 사용하면, 나중에 원본 데이터가 변경되어 로그의 무결성이 손상될 수 있음

---

## 🔢 Section 6: 열거형(Enumerable) - range 객체

### 6.1 range 객체의 이해

`range`는 숫자 시퀀스를 생성하는 **열거형 객체**입니다.

```python
rangeTmp = range(1, 11)
print(rangeTmp, 'type - ', type(rangeTmp))  # range(1, 11) <class 'range'>
```

#### 💻 코드 실행 상세 분석

**1단계**: `range(1, 11)`은 1부터 10까지의 숫자 시퀀스를 생성합니다. (11은 포함 안 됨!)

**2단계**: `range` 객체는 메모리 효율적입니다. 실제로 모든 숫자를 메모리에 저장하지 않고, 필요할 때 생성합니다.

**3단계**: `type(rangeTmp)`은 `<class 'range'>`를 반환합니다.

**최종 결과**: `range(1, 11)`이 출력되며, 이는 `range` 클래스의 인스턴스입니다.

### 6.2 range의 3가지 사용 형태

`range`는 가변 함수로, 매개변수를 1개, 2개, 3개 받을 수 있습니다:

1. `range(end)`: 0부터 end-1까지
2. `range(start, end)`: start부터 end-1까지
3. `range(start, end, step)`: start부터 end-1까지 step 간격으로

```python
# 형태 1: range(end)
rangeTmp = range(11)
for data in rangeTmp:
    print(data, end='\t')  # 0	1	2	3	4	5	6	7	8	9	10

# 형태 2: range(start, end)
rangeTmp = range(1, 11)
for data in rangeTmp:
    print(data, end='\t')  # 1	2	3	4	5	6	7	8	9	10

# 형태 3: range(start, end, step)
rangeTmp = range(1, 11, 2)
for data in rangeTmp:
    print(data, end='\t')  # 1	3	5	7	9
```

#### 💻 코드 실행 상세 분석

**형태 1 분석:**
- **1단계**: `range(11)`은 0부터 10까지 생성
- **2단계**: `for` 반복문이 각 숫자를 순회
- **최종 결과**: 0부터 10까지 출력

**형태 2 분석:**
- **1단계**: `range(1, 11)`은 1부터 10까지 생성
- **2단계**: `for` 반복문이 각 숫자를 순회
- **최종 결과**: 1부터 10까지 출력

**형태 3 분석:**
- **1단계**: `range(1, 11, 2)`는 1부터 시작해서 2씩 증가하며 10까지
- **2단계**: 실제로는 1, 3, 5, 7, 9만 생성됨 (10은 포함 안 됨)
- **최종 결과**: 홀수만 출력

> 📌 **노트**: `end='\t'`는 `print()` 함수의 출력 후 줄바꿈 대신 탭 문자를 출력하라는 의미입니다. 이를 통해 가로로 나열하여 출력할 수 있습니다.

### 6.3 반복 가능한 객체(Iterable)

`range` 객체가 반복문에서 사용될 수 있는 이유는 **iterable** 속성을 가지고 있기 때문입니다.

```python
print('dir - ', dir(rangeTmp))  # '__iter__'가 포함되어 있음
```

`__iter__` 메서드가 있으면 반복 가능한 객체입니다. `for ~ in` 반복문에 사용할 수 있습니다.

---

## 🔄 Section 7: 반복 구문(for문)

### 7.1 for문의 기본 구조

```python
for 변수 in 열거형객체:
    실행문
```

### 7.2 리스트를 이용한 반복

```python
lst = [10, 20, 30]

# 방법 1: 값을 직접 순회
for i in lst:
    print(i)  # 10, 20, 30

# 방법 2: 인덱스를 이용한 순회
for idx in range(len(lst)):
    print('idx - ', idx, 'data - ', lst[idx])
    # idx - 0 data - 10
    # idx - 1 data - 20
    # idx - 2 data - 30
```

#### 💻 코드 실행 상세 분석 (방법 2)

**1단계**: `len(lst)`는 3을 반환합니다. (리스트의 요소 개수)

**2단계**: `range(3)`은 0, 1, 2를 생성합니다.

**3단계**: 첫 번째 반복에서 `idx`는 0이 되고, `lst[0]`은 10입니다.

**4단계**: 두 번째 반복에서 `idx`는 1이 되고, `lst[1]`은 20입니다.

**5단계**: 세 번째 반복에서 `idx`는 2가 되고, `lst[2]`는 30입니다.

**최종 결과**: 인덱스와 값이 함께 출력됩니다.

> 📌 **노트**: 방법 1은 값만 필요할 때, 방법 2는 인덱스와 값이 모두 필요할 때 사용합니다.

### 7.3 리스트 생성 및 정렬

```python
import random

lst = []

for idx in range(10):
    lst.append(random.randint(1, 5))
print(lst)  # [3, 1, 5, 2, 4, 1, 5, 3, 2, 4] (예시)

lst.sort()  # 오름차순 정렬 (in-place)
print('sort - ', lst)  # [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

lst.sort(reverse=True)  # 내림차순 정렬
print('sort - ', lst)  # [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
```

#### 💻 코드 실행 상세 분석

**1단계**: 빈 리스트 `lst = []`를 생성합니다.

**2단계**: `range(10)`으로 0부터 9까지 10번 반복합니다.

**3단계**: 각 반복마다 `random.randint(1, 5)`로 1~5 사이의 랜덤 숫자를 생성합니다.

**4단계**: `lst.append()`로 생성된 숫자를 리스트에 추가합니다.

**5단계**: `lst.sort()`는 **in-place 정렬**입니다. 원본 리스트 자체를 정렬하며, 반환값은 없습니다.

**6단계**: `reverse=True` 매개변수를 주면 내림차순으로 정렬됩니다.

**최종 결과**: 정렬된 리스트가 출력됩니다.

> 💡 **중요!**: `sort()` 메서드는 **in-place** 방식입니다. 즉, 원본 리스트를 직접 수정하며 반환값이 없습니다. 반면 `sorted()` 함수는 새로운 정렬된 리스트를 반환하고 원본은 변경하지 않습니다.

---

## 🎯 Section 8: 조건문(if문)과 in 연산자

### 8.1 데이터 존재 여부 확인

```python
lst = [2, 4, 1, 5, 8, 4]

if 6 in lst:
    print('find  - ')
else:
    print('not found')  # 출력됨
```

#### 💻 코드 실행 상세 분석

**1단계**: `6 in lst` 표현식이 평가됩니다.

**2단계**: `in` 연산자는 리스트에 6이 있는지 확인합니다.

**3단계**: 리스트에 6이 없으므로 `False`가 반환됩니다.

**4단계**: `if` 조건이 거짓이므로 `else` 블록이 실행됩니다.

**최종 결과**: `'not found'`가 출력됩니다.

> 📌 **노트**: `in` 연산자는 매우 편리하지만, 대용량 리스트에서는 성능이 떨어질 수 있습니다. 빠른 검색이 필요하면 `set`이나 `dict`를 사용하는 것이 좋습니다.

---

## 📝 Section 9: 리스트 컴프리헨션(List Comprehension)

### 9.1 리스트 컴프리헨션이란?

리스트 컴프리헨션은 리스트를 간결하게 생성하는 파이썬의 강력한 문법입니다.

**기본 문법:**
```python
[실행문 for 변수 in 열거형객체]
[실행문 for 변수 in 열거형객체 if 조건식]
```

### 9.2 일반 반복문 vs 리스트 컴프리헨션

#### 9.2.1 제곱 값 구하기

**일반 반복문 방식:**
```python
lst = [2, 4, 1, 5, 8, 4]
result = []
for idx in range(len(lst)):
    result.append(lst[idx] ** 2)
print(result)  # [4, 16, 1, 25, 64, 16]
```

**리스트 컴프리헨션 방식:**
```python
lst = [2, 4, 1, 5, 8, 4]
result = [lst[idx] ** 2 for idx in range(len(lst))]
print(result)  # [4, 16, 1, 25, 64, 16]
```

#### 💻 코드 실행 상세 분석 (리스트 컴프리헨션)

**1단계**: `for idx in range(len(lst))`로 인덱스를 생성합니다 (0부터 5까지).

**2단계**: 각 인덱스에 대해 `lst[idx] ** 2`를 계산합니다.

**3단계**: 계산된 값들이 자동으로 새 리스트에 수집됩니다.

**최종 결과**: 제곱 값들로 이루어진 리스트 `[4, 16, 1, 25, 64, 16]`가 생성됩니다.

#### 9.2.2 조건을 포함한 리스트 컴프리헨션

짝수 제곱만 필터링하기:

**일반 반복문 방식:**
```python
lst = [2, 4, 1, 5, 8, 4]
result = []
for idx in range(len(lst)):
    if (lst[idx] ** 2 % 2) == 0:
        result.append(lst[idx] ** 2)
print(result)  # [4, 16, 64, 16]
```

**리스트 컴프리헨션 방식:**
```python
lst = [2, 4, 1, 5, 8, 4]
result = [lst[idx] ** 2 for idx in range(len(lst)) if lst[idx] ** 2 % 2 == 0]
print(result)  # [4, 16, 64, 16]
```

#### 💻 코드 실행 상세 분석

**1단계**: `for idx in range(len(lst))`로 인덱스를 생성합니다.

**2단계**: 각 인덱스에 대해 `lst[idx] ** 2`를 계산합니다.

**3단계**: `if lst[idx] ** 2 % 2 == 0` 조건을 확인합니다. (짝수인지 검사)

**4단계**: 조건이 참인 경우에만 결과 리스트에 포함됩니다.

**최종 결과**: 짝수 제곱 값들만 포함된 리스트 `[4, 16, 64, 16]`이 생성됩니다.

> 💡 **중요!**: 강사님께서 "리스트 컴프리헨션을 사용하면 성능이 더 좋다"고 강조하셨습니다. 리스트 컴프리헨션은 C 언어 레벨에서 최적화되어 있어 일반 반복문보다 빠릅니다.

### 9.3 실전 예제 - 3의 배수 찾기

```python
# 일반 반복문
hund = range(1, 101)
hund_lst = []
for idx in hund:
    if idx % 3 == 0:
        hund_lst.append(idx)
print(hund_lst)

# 리스트 컴프리헨션
hund = range(1, 101)
hund_lst = [idx for idx in hund if idx % 3 == 0]
print(hund_lst)
# [3, 6, 9, 12, ..., 99]
```

#### 💻 코드 실행 상세 분석

**1단계**: `range(1, 101)`로 1부터 100까지의 숫자 시퀀스를 생성합니다.

**2단계**: 각 숫자에 대해 `idx % 3 == 0` 조건을 확인합니다. (3의 배수인지)

**3단계**: 조건이 참인 숫자들만 리스트에 포함됩니다.

**최종 결과**: 1부터 100까지 중 3의 배수인 숫자들의 리스트가 생성됩니다.

---

## 📚 Section 10: 딕셔너리(Dictionary) 심화

### 10.1 딕셔너리의 특징 정리

- **키(Key)와 값(Value) 쌍**: `{key: value}` 형태
- **키의 중복 불허**: 같은 키는 하나만 존재
- **불변 객체**: 딕셔너리 자체는 가변이지만, 키로 사용되는 값은 불변(immutable) 타입이어야 함
- **숫자 인덱싱 불가**: 키로만 접근 가능
- **순서 없음**: Python 3.7+ 에서는 삽입 순서가 유지되지만, 순서에 의존해서는 안 됨

### 10.2 딕셔너리와 보안

#### 10.2.1 사용자 정보 저장 및 수정 - 취약한 코드

```python
user = {
    "id": 100,
    "name": "admin",
    "role": "superuser"
}
print(user)

# 권한 변경 함수
def updateRole(data, newRole):
    data["role"] = newRole

# caller (누군가가 호출)
updateRole(user, "guest")  # 검증되지 않은 값 전달!

print(user)  # {'id': 100, 'name': 'admin', 'role': 'guest'}
```

#### 💻 코드 실행 상세 분석

**1단계**: `user` 딕셔너리가 생성됩니다. 초기 권한은 `"superuser"`입니다.

**2단계**: `updateRole(user, "guest")` 함수가 호출됩니다.

**3단계**: 함수 내부에서 `data["role"] = newRole`이 실행됩니다.

**4단계**: `data`는 `user`와 같은 객체를 가리키므로 (참조 전달), **원본이 직접 수정됩니다**.

**5단계**: 아무런 검증 없이 권한이 `"guest"`로 변경됩니다.

**최종 결과**: 원본 `user` 딕셔너리의 `"role"`이 `"guest"`로 변경됩니다.

> 🔐 **보안 노트**: 이 코드는 매우 위험합니다!
> 1. **입력값 검증 없음**: `newRole`이 어떤 값이든 그대로 적용됨
> 2. **원본 직접 수정**: 딕셔너리를 함수에 전달하면 참조가 전달되어 원본이 변경됨
> 3. **권한 오염 가능**: 악의적인 사용자가 임의의 권한으로 변경 가능 (Privilege Escalation)
> 4. **정보 변조**: SQL Injection처럼 데이터 무결성이 손상될 수 있음

#### 10.2.2 사용자 정보 저장 및 수정 - 개선된 코드

```python
from copy import deepcopy

user = {
    "id": 100,
    "name": "admin",
    "role": "superuser"
}

# White List - 허용된 권한 목록
allowedRoles = {"user", "guest", "manager"}

# 개선된 권한 변경 함수
def updateRole(data, newRole):
    # 1. 불변 데이터 사용 (깊은 복사)
    copyUser = deepcopy(data)
    
    # 2. 입력값 검증
    if newRole in allowedRoles:
        copyUser["role"] = newRole
    else:
        pass  # 또는 예외 발생
    
    return copyUser

# caller
changeUser = updateRole(user, "guest")

print('original - ', user)       # {'id': 100, 'name': 'admin', 'role': 'superuser'}
print('copy     - ', changeUser)  # {'id': 100, 'name': 'admin', 'role': 'guest'}
```

#### 💻 코드 실행 상세 분석

**1단계**: `allowedRoles` 세트에 허용된 권한 목록을 정의합니다. (White List 방식)

**2단계**: `updateRole()` 함수가 호출되면 먼저 `deepcopy(data)`로 완전히 새로운 딕셔너리를 생성합니다.

**3단계**: `if newRole in allowedRoles` 조건으로 입력값을 검증합니다.

**4단계**: 검증을 통과한 경우에만 복사본의 권한을 변경합니다.

**5단계**: 변경된 복사본을 반환합니다. 원본은 전혀 손상되지 않습니다.

**최종 결과**: 원본 `user`는 그대로 유지되고, 새로운 딕셔너리 `changeUser`만 변경됩니다.

> 💡 **중요!**: 이 코드가 보안적으로 안전한 이유:
> 1. **White List 검증**: `allowedRoles`에 정의된 값만 허용
> 2. **불변 데이터 사용**: Deep Copy로 원본 보호
> 3. **명시적 반환**: 변경된 데이터를 새로운 변수로 받음
> 4. **권한 제한**: 정의되지 않은 권한으로의 변경 불가

강사님께서 이 부분을 매우 강조하셨습니다: "caller에서 리스트로 만들어두고, 리스트에 존재하는 데이터로만 수정 가능하게 하기. 이것을 **White List**라고 부른다."

### 10.3 딕셔너리 생성의 다양한 방법

#### 10.3.1 기본 리터럴 방식

```python
user = {
    "id": 100,
    "name": "admin",
    "role": "superuser"
}
```

#### 10.3.2 dict() 생성자 - 키워드 인자 방식

```python
dictTmp = dict(city='busan', expo=2030)
print(dictTmp)  # {'city': 'busan', 'expo': 2030}
```

#### 10.3.3 dict() 생성자 - 튜플 리스트 방식

```python
dictTmp = dict([
    ('city', 'busan'),
    ('expo', 2030)
])
print(dictTmp)  # {'city': 'busan', 'expo': 2030}
```

#### 10.3.4 zip()을 이용한 딕셔너리 생성

```python
keys = ('key01', 'key02', 'key03', 'key04')
datas = ('sk', 'samsung', 'lg', 'lgcns')

dictZip = dict(zip(keys, datas))
print(dictZip)  
# {'key01': 'sk', 'key02': 'samsung', 'key03': 'lg', 'key04': 'lgcns'}
```

#### 💻 코드 실행 상세 분석

**1단계**: `keys`와 `datas`라는 두 개의 튜플이 정의됩니다.

**2단계**: `zip(keys, datas)` 함수는 두 시퀀스를 **쌍으로 묶어줍니다**.
```
('key01', 'sk')
('key02', 'samsung')
('key03', 'lg')
('key04', 'lgcns')
```

**3단계**: `dict()` 생성자가 이 튜플 쌍들을 받아 딕셔너리로 변환합니다.

**최종 결과**: 키와 값이 매핑된 딕셔너리가 생성됩니다.

> 💡 **중요!**: `zip()` 함수는 현업에서 매우 자주 사용됩니다. 서로 다른 데이터 타입을 딕셔너리로 만들어야 할 때 매우 유용합니다. 강사님께서 "정제되지 않은 데이터를 필요한 데이터 타입으로 만드는 것도 능력"이라고 강조하셨습니다.

> 📌 **노트**: `zip()`을 사용하기 위해서는 두 시퀀스의 길이가 같아야 합니다. 길이가 다르면 짧은 쪽에 맞춰집니다.

### 10.4 딕셔너리 순회(Iteration)

#### 10.4.1 기본 순회 (키만)

```python
dictZip = {'key01': 'sk', 'key02': 'samsung', 'key03': 'lg', 'key04': 'lgcns'}

for key in dictZip:
    print(key, dictZip[key])
```

#### 💻 코드 실행 상세 분석

**1단계**: `for key in dictZip`는 딕셔너리의 키들을 순회합니다.

**2단계**: 기본적으로 딕셔너리를 반복하면 **키만** 반환됩니다.

**3단계**: 각 키를 사용해 `dictZip[key]`로 값에 접근합니다.

**최종 결과**: 키와 값이 함께 출력됩니다.

#### 10.4.2 keys() 메서드 사용

```python
for key in dictZip.keys():
    print(key, dictZip[key])
```

`keys()` 메서드는 명시적으로 키들을 반환합니다. 기본 순회와 동일한 결과입니다.

#### 10.4.3 values() 메서드 사용

```python
for data in dictZip.values():
    print(data)
```

`values()` 메서드는 값들만 반환합니다. 키는 필요 없고 값만 필요할 때 사용합니다.

#### 10.4.4 items() 메서드 사용 - 튜플 언패킹

```python
for key, data in dictZip.items():
    print(key, ' - ', data)
```

#### 💻 코드 실행 상세 분석

**1단계**: `dictZip.items()`는 `(key, value)` 형태의 튜플들을 반환합니다.

**2단계**: `for key, data in ...` 구문은 **튜플 언패킹**입니다.

**3단계**: 각 반복에서 튜플의 첫 번째 요소는 `key`에, 두 번째 요소는 `data`에 자동으로 할당됩니다.

**최종 결과**: 키와 값을 따로 변수에 담아 편리하게 사용할 수 있습니다.

> 💡 **중요!**: `items()` 메서드는 키와 값을 동시에 필요로 할 때 가장 권장되는 방식입니다. 튜플 언패킹을 통해 코드가 더 깔끔해집니다.

---

## 🧩 Section 11: 실전 프로젝트 - 단어 빈도수 구하기

강사님께서 돌발 퀴즈를 내주셨습니다. 이 퀴즈는 오늘 배운 내용을 모두 활용하는 종합 문제입니다.

### 11.1 문제 정의

주어진 단어 리스트에서 각 단어의 빈도수를 구하여 딕셔너리로 반환하기.

```python
wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk', 'sk']

# 원하는 출력 결과:
# {'dog': 3, 'cat': 4, 'word': 1, 'cs': 2, 'sk': 2}
```

### 11.2 해결 방법 1: count() 메서드와 zip() 활용

```python
wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk', 'sk']

result = dict(zip(set(wordLst), [wordLst.count(data) for data in set(wordLst)]))
print(result)
# {'dog': 3, 'sk': 2, 'cs': 2, 'cat': 4, 'word': 1}
```

#### 💻 코드 실행 상세 분석

**1단계**: `set(wordLst)`로 중복을 제거하여 유니크한 단어들만 추출합니다.
```python
{'dog', 'cat', 'word', 'cs', 'sk'}  # 순서는 보장되지 않음
```

**2단계**: 리스트 컴프리헨션 `[wordLst.count(data) for data in set(wordLst)]`로 각 단어의 빈도를 계산합니다.
```python
[3, 4, 1, 2, 2]  # 각 단어의 출현 횟수
```

**3단계**: `zip()`으로 단어와 빈도를 쌍으로 묶습니다.
```python
[('dog', 3), ('cat', 4), ('word', 1), ('cs', 2), ('sk', 2)]
```

**4단계**: `dict()`로 딕셔너리로 변환합니다.

**최종 결과**: 단어와 빈도수가 매핑된 딕셔너리가 생성됩니다.

> 💡 **중요!**: 이 방법은 매우 간결하지만, `set()`을 두 번 호출하고 `count()`를 여러 번 호출하므로 대용량 데이터에서는 비효율적일 수 있습니다.

### 11.3 해결 방법 2: 딕셔너리 직접 구성 (수업 중 다른 학생들의 방법)

```python
wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk', 'sk']

wordDict = {word: 0 for word in set(wordLst)}  # 초기화
for word in wordLst:
    wordDict[word] += 1
print(wordDict)
```

#### 💻 코드 실행 상세 분석

**1단계**: 딕셔너리 컴프리헨션으로 모든 유니크 단어를 키로 하고 값을 0으로 초기화합니다.
```python
{'dog': 0, 'cat': 0, 'word': 0, 'cs': 0, 'sk': 0}
```

**2단계**: 원본 리스트를 순회하면서 각 단어가 나올 때마다 해당 키의 값을 1씩 증가시킵니다.

**3단계**: 
- 'dog' 나올 때: `wordDict['dog'] += 1` → 1
- 'dog' 또 나올 때: `wordDict['dog'] += 1` → 2
- 'dog' 또 나올 때: `wordDict['dog'] += 1` → 3
- (cat, word, cs, sk도 동일하게 진행)

**최종 결과**: 정확한 빈도수를 가진 딕셔너리가 완성됩니다.

> 💡 **중요!**: 이 방법은 리스트를 한 번만 순회하므로 시간 복잡도가 O(n)으로 효율적입니다.

### 11.4 강사님의 독특한 해결 방법

강사님께서는 한 줄로 해결하는 방법을 보여주셨습니다:

```python
wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk', 'sk']

result = dict(zip(set(wordLst), [wordLst.count(data) for data in set(wordLst)]))
print(result)
```

강사님께서 "저 이길 수 있는 분 있나요? 한 줄 말고?" 하시며 농담을 하셨습니다. 😄

> 📌 **노트**: 강사님께서 다양한 풀이 방법을 보여주신 이유는 "코딩의 어떤 감수성 이런 것들을 좀 느껴보시는 시간이 되시라고" 하셨습니다. 정답은 하나가 아니며, 상황에 맞는 최적의 방법을 선택하는 것이 중요합니다.

---

## 🔍 Section 12: 집합(Set) 타입

### 12.1 Set의 특징

수업 중에 Set에 대해서도 간단히 다뤘습니다:

- **가변(Mutable)**: 요소 추가/삭제 가능
- **중복 제거**: 같은 값은 하나만 저장
- **인덱싱/슬라이싱 불가능**: 순서가 없음
- **순서 없음**: 요소의 저장 순서가 보장되지 않음

```python
allowedRoles = {"user", "guest", "manager"}  # Set 생성
```

### 12.2 중복 제거에 활용

```python
gender = ['남', '여', '여', '남', '남', '남', '여', '여']
unique_gender = list(set(gender))
print(unique_gender)  # ['남', '여'] 또는 ['여', '남']
```

#### 💻 코드 실행 상세 분석

**1단계**: 리스트 `gender`에는 중복된 값들이 포함되어 있습니다.

**2단계**: `set(gender)`는 리스트를 집합으로 변환하면서 자동으로 중복을 제거합니다.

**3단계**: `list()`로 다시 리스트로 변환합니다.

**최종 결과**: 중복이 제거된 유니크한 값들만 남습니다.

> 📌 **노트**: Set은 해시 테이블 기반이므로 `in` 연산이 O(1)로 매우 빠릅니다. 멤버십 테스트가 빈번한 경우 리스트 대신 Set을 사용하는 것이 좋습니다.

---

## 🎓 Section 13: 종합 예제 - 보안 이벤트 로그 분석 시스템

`day02_예제코드.py` 파일에는 오늘 배운 내용을 종합적으로 활용한 실전 예제가 포함되어 있습니다.

### 13.1 예제 개요

이 예제는 보안 이벤트 로그를 분석하고, AI에게 분석을 요청하며, 결과에 따라 조치를 취하는 전체 흐름을 시뮬레이션합니다.

### 13.2 샘플 데이터 구조

```python
import json

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

> 📌 **노트**: 이러한 형태의 데이터 구조는 실제 시스템에서 매우 흔합니다. 리스트 안에 딕셔너리가 중첩되어 있고, 딕셔너리 안에 또 다른 딕셔너리가 있는 구조입니다.

### 13.3 기본 로그 분석 함수

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

**1단계**: `high_severity_alerts`와 `ip_activity` 변수를 초기화합니다.

**2단계**: `for log in logs`로 각 로그 이벤트를 순회합니다.

**3단계**: 각 로그에서 `source_ip`를 추출합니다.

**4단계**: `if-elif-else` 구조로 심각도에 따라 분류합니다:
- `"high"`: 위험 메시지 출력 및 별도 리스트에 저장
- `"medium"`: 주의 메시지 출력
- 기타: 정보 메시지 출력

**5단계**: IP별 활동 횟수를 딕셔너리에 집계합니다:
- IP가 이미 있으면: 횟수 +1
- IP가 없으면: 새로 추가하고 1로 설정

**6단계**: 분석 결과를 출력하고 `high_severity_alerts`를 반환합니다.

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

### 13.4 AI 분석 시뮬레이션 함수

```python
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

    # AI 호출 시뮬레이션 (실제로는 네트워크 통신)
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
    
    # json.loads()는 여기서는 시뮬레이션이므로 사용하지 않음
    print("[AI 서버 -> 클라이언트] AI 분석 완료 JSON 응답:")
    print(json.dumps(simulated_ai_response_dict, indent=4, ensure_ascii=False))
    print("--- 2. AI 분석 시뮬레이션 종료 ---\n")
    
    return simulated_ai_response_dict
```

#### 💻 코드 실행 상세 분석

**1단계**: `request_data` 딕셔너리를 생성하여 AI에게 보낼 데이터를 준비합니다.

**2단계**: `json.dumps(request_data, indent=4)`로 Python 딕셔너리를 JSON 문자열로 변환합니다.
- `indent=4`: 보기 좋게 들여쓰기 적용

**3단계**: 실제 환경에서는 여기서 네트워크를 통해 AI API를 호출하지만, 이 예제에서는 시뮬레이션된 응답을 직접 생성합니다.

**4단계**: AI의 분석 결과를 나타내는 복잡한 구조의 딕셔너리를 생성합니다:
- `overall_risk_score`: 전체 위험도 점수
- `threat_pattern_identified`: 탐지된 위협 패턴
- `recommended_actions`: 권장 조치 사항 리스트

**5단계**: 응답을 JSON 형식으로 출력합니다.

**최종 결과**: AI의 분석 결과가 JSON 형식으로 반환됩니다.

> 📌 **노트**: `json.dumps()`와 `json.loads()`의 차이:
> - `json.dumps()`: Python 객체 → JSON 문자열 (직렬화, Serialization)
> - `json.loads()`: JSON 문자열 → Python 객체 (역직렬화, Deserialization)

### 13.5 AI 판정 결과 처리 함수

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

**1단계**: AI 결과에서 `analysis_summary`를 추출합니다.

**2단계**: `overall_risk_score`가 7.0을 초과하는지 확인합니다.

**3단계**: 위험도가 높은 경우:
- 긴급 메시지 출력
- 탐지된 위협 패턴 출력
- 상세 결과를 순회하며 권장 조치 출력

**4단계**: 위험도가 낮은 경우:
- 모니터링 유지 메시지만 출력

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

### 13.6 메인 실행 로직

```python
if __name__ == "__main__":
    # 1단계: 기본 분석 수행 및 심각도 '높음' 이벤트 추출
    critical_logs = analyze_raw_logs(raw_security_logs)
    
    # 2단계: '높음' 이벤트만 AI에게 보내 분석 요청 (시뮬레이션)
    if critical_logs:  # 처리할 로그가 있을 경우에만 실행
        ai_analysis_result = get_ai_analysis_from_logs(critical_logs)
        
        # 3단계: AI의 분석 결과를 바탕으로 후속 조치 수행
        process_ai_verdict(ai_analysis_result)
    else:
        print("AI 분석으로 넘길 심각한 이벤트가 없습니다.")
```

#### 💻 코드 실행 상세 분석

**1단계**: `analyze_raw_logs()` 함수를 호출하여 모든 로그를 분석하고, 심각도가 `"high"`인 이벤트만 추출합니다.

**2단계**: `if critical_logs:` 조건으로 심각한 이벤트가 있는지 확인합니다.
- 리스트가 비어있으면 `False`로 평가됩니다.
- 요소가 있으면 `True`로 평가됩니다.

**3단계**: 심각한 이벤트가 있으면 AI 분석을 요청합니다.

**4단계**: AI의 분석 결과를 바탕으로 후속 조치를 수행합니다.

**최종 결과**: 전체 보안 로그 분석 파이프라인이 순차적으로 실행됩니다.

> 🔐 **보안 노트**: 이 예제는 실제 보안 시스템의 축소판입니다. 실무에서는:
> 1. 로그 수집 → 2. 1차 필터링 → 3. 상세 분석 (AI/ML) → 4. 자동화된 대응
> 이러한 단계를 거칩니다. 이 예제에서 배운 딕셔너리, 리스트, 조건문, 반복문 등이 모두 활용됩니다.

---

## 💭 Section 14: 강사님의 조언 및 수업 마무리

### 14.1 다양한 수준의 학생들

강사님께서 수업 마지막에 하신 말씀:

> "모르겠어요. 제가 지금 저희 클래스에 다양한 분들이 섞여 있다 보니 제가 때로는 뭐 해보신 분들을 위해서 수업을 하는 경우도 있고요. 때로는 이제 처음 접하시는 분들을 위해서 좀 기본기를 좀 다지는 역할로서 수업을 하는 경우도 있어요 지금. 이런 식으로 좀 밸런스를 좀 잡아가고 있거든요."

### 14.2 복습과 실습의 중요성

> "처음 하시는 분들은 이제 문법적인 부분부터 정리를 하시면서 기존에 했던 코드들을 좀 복습하시고 곱씹어 보시면서 레버법 시간에 필요하신 경우 여러분들 이제 지리해 주시면 좋지 않을까."

### 14.3 코딩 감수성

강사님께서 다양한 코드 작성 방법을 보여주신 이유:

> "코딩의 어떤 감수성 이런 것들을 좀 느껴보시는 시간이 되시라고 저는 이렇게..."

### 14.4 내재화의 중요성

> "처음부터 여러분들 이게 코딩이라는 건 그거거든요. 내재화가 돼야 됩니다. 아직까지 여러분들 이런 코드들은 어려우실 수 있어요. 왜? 본인 걸로 만들지 못했기 때문에. 문법적인 걸 각인하거나 여러 케이스들을 보지 못했기 때문에."

---

## 📋 오늘 배운 핵심 개념 정리

### 1. 파이썬 타입 시스템
- 파이썬은 **모든 타입이 참조 타입** (기본 타입 없음)
- **객체지향(OOP)**: 실세계 객체 → 클래스 → 인스턴스
- **함수 vs 메서드**: 단독 실행 vs 인스턴스에 종속

### 2. 문자열 메서드
- `find()`: 문자열 검색
- `strip()`: 공백 제거
- `capitalize()`: 첫 글자 대문자화
- `endswith()`: 특정 문자열로 끝나는지 확인

### 3. 함수
- `def` 키워드로 정의
- 매개변수와 반환값의 4가지 조합
- Worker function과 Caller의 구분

### 4. 복사의 이해
- **얕은 복사(Shallow Copy)**: 주소만 복사, 원본에 영향
- **깊은 복사(Deep Copy)**: 완전히 새로운 객체 생성
- 민감한 데이터는 반드시 깊은 복사 사용

### 5. 가변 vs 불변
- **불변(Immutable)**: Numeric, str, tuple → 값 변경 시 새 객체 생성
- **가변(Mutable)**: list, dict, set → 값 직접 수정 가능

### 6. 열거형과 반복문
- `range(start, end, step)`: 숫자 시퀀스 생성
- `for ~ in`: 반복 구문
- `in` 연산자: 멤버십 테스트

### 7. 리스트 컴프리헨션
- 간결한 리스트 생성 문법
- 조건문 포함 가능
- 일반 반복문보다 성능 우수

### 8. 딕셔너리
- Key-Value 쌍
- `keys()`, `values()`, `items()` 메서드
- `zip()`을 이용한 딕셔너리 생성

### 9. 보안 코딩
- **White List 방식**: 허용된 값만 처리
- **입력값 검증**: 함수 내에서 반드시 검증
- **불변 데이터 사용**: 원본 보호를 위한 깊은 복사

---

## 🎯 실전 활용 팁

### 1. 데이터 타입 선택 가이드

**리스트 사용:**
- 순서가 중요할 때
- 중복을 허용해야 할 때
- 인덱싱이 필요할 때

**딕셔너리 사용:**
- Key-Value 매핑이 필요할 때
- 빠른 검색이 필요할 때 (O(1))
- JSON 데이터와 호환성이 필요할 때

**셋 사용:**
- 중복 제거가 필요할 때
- 빠른 멤버십 테스트가 필요할 때
- 집합 연산 (합집합, 교집합)이 필요할 때

### 2. 반복문 선택 가이드

**값만 필요:**
```python
for item in collection:
    process(item)
```

**인덱스와 값 모두 필요:**
```python
for idx in range(len(collection)):
    process(idx, collection[idx])
```

**인덱스와 값을 동시에 (권장):**
```python
for idx, item in enumerate(collection):
    process(idx, item)
```

### 3. 보안 코딩 체크리스트

✅ 사용자 입력은 반드시 검증
✅ White List 방식 사용
✅ 민감한 데이터는 깊은 복사
✅ 파일 확장자는 다중 검증 (endswith + MIME type)
✅ 원본 데이터 직접 수정 금지
✅ 함수는 새로운 객체 반환

---

## 📚 추가 학습 자료 및 복습 포인트

### 복습이 필요한 부분

1. **얕은 복사 vs 깊은 복사**: 실습을 통해 차이점 명확히 이해하기
2. **리스트 컴프리헨션**: 다양한 예제로 연습하기
3. **딕셔너리 순회**: `keys()`, `values()`, `items()`의 차이 명확히 하기
4. **zip()` 함수**: 다양한 활용 사례 연습하기

### 실습 과제 (자가 학습용)

1. 주어진 문자열 리스트에서 길이가 5 이상인 단어만 추출하여 대문자로 변환하기
2. 딕셔너리를 받아 값이 특정 조건을 만족하는 항목만 필터링하는 함수 작성하기
3. 중첩된 리스트에서 모든 숫자의 합을 구하는 함수 작성하기 (깊은 복사 활용)
4. 로그 파일 데이터를 파싱하여 통계 정보를 딕셔너리로 반환하는 프로그램 작성하기

---

## 🙏 수업 후기

오늘 2일차 수업에서는 1일차에 배운 기본 개념들을 실전에 활용하는 방법을 배웠습니다. 특히 얕은 복사와 깊은 복사의 차이, 보안 관점에서의 코딩 방법 등은 실무에서 매우 중요한 내용이었습니다.

강사님께서 다양한 수준의 학생들을 모두 배려하시면서 기본기와 심화 내용을 균형있게 다뤄주셨고, 특히 실전 예제(보안 로그 분석 시스템)를 통해 오늘 배운 모든 개념이 어떻게 통합되는지 명확히 보여주셨습니다.

"코딩의 감수성"이라는 표현이 인상 깊었는데, 정답은 하나가 아니며 상황에 맞는 최적의 방법을 선택하는 것이 중요하다는 것을 배웠습니다.

내일도 열심히 학습하여 더 많은 것을 배우고 내재화하도록 노력하겠습니다!

---

**다음 수업 예고**: 3일차에는 더 심화된 제어 구문과 함수, 그리고 모듈 시스템에 대해 배울 예정입니다.

**강사님 말씀**: "저는 내일 여러분들 웃는 얼굴로 찾아뵙겠습니다. 수고하셨습니다!" 😊
