
--- 
title: "📝 Secure Python Day 04 강의 노트 (4일차)"
date: 2025-01-01
excerpt: "오늘 강의에서는 파이썬의 함수(Function)에 대해 깊이 있게 학습했습니다. 단순히 함수를 사용하는 것을 넘어서, 보안 관점에서 안전한 함수 구현 방법과 실무에서 활용되는 고급 기법들을 배우는 시간이었습니다."
categories:
  - Python
tags:
  - Python
  - SK_Rookies
---

# 📝 Secure Python Day 04 강의 노트 (4일차)

## 📚 학습 개요

오늘 강의에서는 파이썬의 **함수(Function)**에 대해 깊이 있게 학습했습니다. 단순히 함수를 사용하는 것을 넘어서, **보안 관점에서 안전한 함수 구현 방법**과 **실무에서 활용되는 고급 기법**들을 배우는 시간이었습니다.

특히 강사님께서 강조하신 것은, 지금까지 우리가 작성한 코드는 **재사용성이 떨어지고 유지보수가 어렵다**는 점이었습니다. 이러한 문제를 해결하기 위해 함수를 활용하고, 더 나아가 **클로저(Closure)**와 **데코레이터(Decorator)**를 통해 코드의 품질을 높이는 방법을 학습했습니다.

---

## 🎯 학습 목표

오늘의 핵심 학습 목표는 다음과 같습니다:

1. **함수(Function)**의 기본 개념과 필요성 이해
2. **함수의 4가지 유형**과 적절한 활용 방법 습득
3. **람다 함수(Lambda Function)**와 `map`, `filter` 함수 활용
4. **변수 스코프(LEGB 규칙)** 이해 및 적용
5. **클로저(Closure)**를 통한 안전한 상태 관리
6. **데코레이터(Decorator)**의 개념과 활용
7. **가변인자(*args, **kwargs)** 활용법
8. **보안 관점에서 함수 작성**하는 방법 습득

---

## 📖 목차

### 1. 모듈, 패키지, 함수의 관계
### 2. 함수(Function)란 무엇인가?
### 3. 함수의 기본 구조와 4가지 유형
### 4. 매개변수의 종류 (위치 인자 vs 키워드 인자)
### 5. 람다 함수(Lambda Function)
### 6. 변수 스코프와 LEGB 규칙
### 7. 클로저(Closure) - 상태 유지의 비밀
### 8. 데코레이터(Decorator) - 함수 장식자
### 9. 가변인자 함수 (*args, **kwargs)
### 10. 실전 예제: API 엔드포인트 생성
### 11. 보안 관점에서의 코드 개선

---

## 1. 모듈, 패키지, 함수의 관계

### 1.1 파이썬의 구조적 이해

강사님께서는 수업을 시작하면서 **파이썬 코드의 구조**에 대해 설명해주셨습니다.

#### 1.1.1 모듈(Module)이란?

- **1개의 파이썬 파일(.py) = 1개의 모듈**입니다.
- 모듈은 관련된 함수와 클래스를 담고 있는 코드 파일입니다.
- 예를 들어, `utils.py` 파일을 만들면 이것이 하나의 모듈이 됩니다.

```python
# utils.py 파일 (모듈)
def calculate_sum(a, b):
    return a + b

def calculate_product(a, b):
    return a * b
```

#### 1.1.2 모듈의 구성 요소

모듈은 다음과 같은 요소들을 포함할 수 있습니다:

1. **함수(Function)**: 특정 기능을 수행하는 코드 블록
2. **클래스(Class)**: 변수(속성)와 메서드(함수)를 포함하는 객체 지향 구조

```python
# module_example.py

# 함수를 포함하는 모듈
def greet(name):
    return f"Hello, {name}!"

# 클래스를 포함하는 모듈
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self.result
```

#### 1.1.3 패키지(Package)란?

- **패키지는 여러 모듈을 묶은 것**입니다.
- 패키지는 계층적 구조를 가질 수 있습니다 (하위 패키지 포함 가능).
- 실무에서는 관련된 모듈들을 패키지로 구성하여 관리합니다.

```
my_package/
│
├── __init__.py
├── module1.py
├── module2.py
└── sub_package/
    ├── __init__.py
    └── module3.py
```

#### 💡 중요!: 실무에서의 모듈 구성

강사님께서 강조하신 점은, **현업에서는 모듈에 함수만 넣기보다는 클래스를 넣는 경우가 일반적**이라는 것입니다. API 명세를 만들 때 클래스 기반으로 설계하는 것이 표준적인 방식입니다.

---

### 1.2 지금까지의 코드 작성 방식과 문제점

#### 1.2.1 이전까지의 작업 방식

지금까지 우리는 다음과 같은 방식으로 코드를 작성했습니다:

- **인터프리터 방식**으로 대화형 프로그래밍
- **절차적(Procedural)** 방식으로 코드를 순차적으로 작성
- 기존 모듈의 함수를 **가져다 쓰는** 입장 (예: `print()`, `len()` 등)

#### 1.2.2 발생한 문제점들

강사님께서 지적하신 문제점들:

1. **재사용성 부족**: 같은 기능을 여러 곳에서 사용할 때 복사-붙여넣기 해야 함
2. **유지보수 어려움**: 기능을 수정할 때 모든 곳을 찾아서 수정해야 함
3. **코드 가독성 저하**: 복잡한 로직이 반복되면 코드를 이해하기 어려움
4. **디버깅 곤란**: 문제가 발생했을 때 어디서 문제인지 찾기 어려움
5. **협업 어려움**: 다른 개발자가 코드를 이해하고 사용하기 어려움

```python
# 문제가 있는 코드 예시 - 재사용성 없음
user_data = [1, 2, 3, 4, 5]
total = 0
for num in user_data:
    total += num
print(f"Total: {total}")

# 같은 로직을 또 다른 곳에서 사용해야 한다면?
sales_data = [100, 200, 300]
total = 0
for num in sales_data:
    total += num
print(f"Sales Total: {total}")

# 이런 식으로 계속 복사-붙여넣기를 해야 함 (비효율적!)
```

#### 1.2.3 해결책: 함수(Function)

이러한 문제들을 해결하기 위해 **함수**라는 개념을 사용합니다.

---

## 2. 함수(Function)란 무엇인가?

### 2.1 함수의 정의

**함수(Function)**는 특정 작업을 수행하는 코드 블록에 이름을 붙인 것입니다. 객체 지향 프로그래밍(OOP) 관점에서는 **메서드(Method)**라고도 부릅니다.

### 2.2 함수를 사용하는 이유

강사님께서 설명하신 함수의 5가지 주요 장점:

#### 2.2.1 코드 재사용성 (Code Reusability)

- 한 번 작성한 코드를 여러 곳에서 반복해서 사용 가능
- 같은 기능이 필요할 때마다 함수를 호출하기만 하면 됨

```python
# 함수를 사용한 재사용 가능한 코드
def calculate_sum(data_list):
    """리스트의 합계를 계산하는 함수"""
    return sum(data_list)

# 여러 곳에서 재사용
user_total = calculate_sum([1, 2, 3, 4, 5])
sales_total = calculate_sum([100, 200, 300])
product_total = calculate_sum([50, 75, 125])
```

#### 2.2.2 가독성 향상 (Improved Readability)

- 함수 이름만 보고도 어떤 작업을 하는지 알 수 있음
- 복잡한 로직을 의미 있는 이름의 함수로 분리하면 코드가 명확해짐

```python
# 가독성이 낮은 코드
data = [1, 2, 3, 4, 5]
result = sum([x ** 2 for x in data if x % 2 == 0])

# 가독성이 높은 코드
def calculate_even_squares_sum(numbers):
    """짝수의 제곱의 합을 계산"""
    even_numbers = [x for x in numbers if x % 2 == 0]
    squares = [x ** 2 for x in even_numbers]
    return sum(squares)

data = [1, 2, 3, 4, 5]
result = calculate_even_squares_sum(data)
```

#### 2.2.3 유지보수 용이 (Easy Maintenance)

- 수정 사항이 발생하면 함수 내부만 수정하면 됨
- **외부 변경 사항을 최소화**할 수 있음
- 함수를 사용하는 다른 코드는 수정할 필요가 없음

```python
# 기존 함수
def calculate_discount(price):
    return price * 0.9  # 10% 할인

# 할인율이 변경되어도 함수만 수정하면 됨
def calculate_discount(price):
    return price * 0.8  # 20% 할인으로 변경

# 이 함수를 사용하는 모든 코드는 자동으로 새로운 할인율 적용
```

#### 💡 중요!: 유지보수성의 핵심

강사님께서 특히 강조하신 점은 **"로직 변경에 대한 외부 변경 사항을 최소화"**할 수 있다는 것입니다. 이것이 함수를 사용하는 가장 큰 이유 중 하나입니다.

#### 2.2.4 디버깅 용이 (Easy Debugging)

- 문제가 발생했을 때 어느 함수에서 문제가 생겼는지 파악하기 쉬움
- 각 함수를 독립적으로 테스트할 수 있음
- 함수 단위로 문제를 격리(isolation)할 수 있음

```python
def read_data(filename):
    """파일에서 데이터를 읽는 함수"""
    with open(filename, 'r') as file:
        return file.read()

def process_data(raw_data):
    """데이터를 처리하는 함수"""
    return raw_data.strip().split('\n')

def save_results(results, output_file):
    """결과를 저장하는 함수"""
    with open(output_file, 'w') as file:
        file.write('\n'.join(results))

# 문제가 발생하면 어느 함수에서 발생했는지 쉽게 파악 가능
```

#### 2.2.5 모듈화 (Modularization)

- 여러 함수를 묶어서 모듈로 관리 가능
- `import utils`와 같이 필요한 함수들을 쉽게 가져올 수 있음
- 팀 작업 시 각자 담당 모듈을 개발할 수 있음

```python
# utils.py 모듈
def validate_email(email):
    """이메일 유효성 검증"""
    return '@' in email and '.' in email

def format_phone(phone):
    """전화번호 포맷팅"""
    return phone.replace('-', '')

# main.py에서 사용
import utils

email = "user@example.com"
if utils.validate_email(email):
    print("Valid email")
```

---

## 3. 함수의 기본 구조와 4가지 유형

### 3.1 함수의 기본 구조

파이썬에서 함수는 `def` 키워드를 사용하여 정의합니다.

```python
def 함수명([매개변수, 매개변수, ...]):
    """독스트링(Docstring): 함수 설명"""
    실행할 코드
    return 결과값  # 반환이 필요없다면 생략 가능
```

#### 3.1.1 함수 구조의 각 요소

1. **`def` 키워드**: 함수를 정의한다는 선언
2. **함수명**: 함수를 식별하는 이름 (명명 규칙 준수)
3. **매개변수(Parameter)**: 함수가 받을 입력값 (선택사항)
4. **콜론(:)**: 함수 블록의 시작을 나타냄
5. **독스트링(Docstring)**: 함수의 설명 (선택사항이지만 권장)
6. **함수 본문**: 실제 수행할 코드
7. **`return` 문**: 결과값 반환 (선택사항)

#### 💡 중요!: 함수 명명 규칙

강사님께서 강조하신 네이밍 컨벤션:
- 함수 이름은 **동사형**으로 작성하는 것이 좋습니다
- 예: `calculateSum()`, `getUserData()`, `validateInput()`
- 명사형도 가능하지만, 동사형이 더 명확합니다

### 3.2 함수의 4가지 유형

강사님께서 설명하신 함수는 크게 4가지 유형으로 분류할 수 있습니다.

#### 3.2.1 유형 1: 매개변수 X, 반환값 X

```python
def greet():
    """단순히 인사 메시지를 출력하는 함수"""
    print("Hello, Welcome!")

# 호출
greet()  # 출력: Hello, Welcome!
```

**사용 시나리오**:
- 단순한 출력만 필요한 경우
- 상태를 변경하는 경우 (예: 로그 기록)
- 반환값이 필요 없는 작업

#### 3.2.2 유형 2: 매개변수 O, 반환값 X

```python
def greet(name):
    """사용자 이름을 받아 인사하는 함수"""
    print(f"hi ~, {name}")

# 호출
greet('jslim')  # 출력: hi ~, jslim
greet('Alice')  # 출력: hi ~, Alice
```

**사용 시나리오**:
- 입력을 받아 처리는 하지만 반환은 필요 없는 경우
- 출력, 로깅, 파일 쓰기 등의 작업

#### 3.2.3 유형 3: 매개변수 X, 반환값 O

```python
def get_current_time():
    """현재 시간을 반환하는 함수"""
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

# 호출
current_time = get_current_time()
print(f"Current time: {current_time}")
```

**사용 시나리오**:
- 고정된 값이나 계산 결과를 반환
- 설정값을 가져오는 경우
- 랜덤 값을 생성하는 경우

#### 3.2.4 유형 4: 매개변수 O, 반환값 O (가장 일반적!)

```python
def greet(name):
    """사용자 이름을 받아 인사 메시지를 반환하는 함수"""
    return f'hi ~, {name}'

# 호출
result = greet('jslim')
print(result)  # 출력: hi ~, jslim
```

💡 **중요!**: 강사님께서 말씀하시길, **실무에서는 유형 4(매개변수와 반환값 모두 있는 형태)가 가장 많이 사용**된다고 하셨습니다.

### 3.3 실습 코드: 기본 함수 작성

#### 3.3.1 첫 번째 함수 만들기

```python
def greet(name='guest'):
    '''사용자에게 인사하는 함수'''
    return f'hi ~, {name}'

# 함수 호출
result = greet('jslim')
print(result)  # 출력: hi ~, jslim
```

#### 💻 코드 실행 상세 분석

1. **함수 정의 단계**: `def greet(name='guest'):`가 실행되면서 함수 객체가 메모리에 생성됩니다.
2. **기본값 설정**: 매개변수 `name`에 기본값 `'guest'`가 설정됩니다.
3. **함수 호출**: `greet('jslim')`이 실행되면서 인자 `'jslim'`이 매개변수 `name`에 전달됩니다.
4. **f-string 평가**: `f'hi ~, {name}'`이 평가되어 `'hi ~, jslim'`이라는 문자열이 생성됩니다.
5. **반환**: `return` 문이 실행되면서 생성된 문자열이 호출자에게 반환됩니다.
6. **변수 할당**: 반환된 값이 `result` 변수에 저장됩니다.
7. **출력**: `print(result)`가 실행되어 `hi ~, jslim`이 화면에 출력됩니다.

#### 📌 노트: 기본 매개변수(Default Parameter)

함수 정의 시 `name='guest'`와 같이 기본값을 설정하면, 호출 시 인자를 전달하지 않아도 기본값이 사용됩니다.

```python
# 인자를 전달하지 않으면 기본값 사용
print(greet())  # 출력: hi ~, guest

# 인자를 전달하면 전달된 값 사용
print(greet('Alice'))  # 출력: hi ~, Alice
```

#### 3.3.2 거듭제곱 계산 함수

```python
def userAdd(a, b):
    """a를 b제곱한 값을 반환하는 함수"""
    return a ** b
```

---

## 4. 매개변수의 종류 (위치 인자 vs 키워드 인자)

### 4.1 위치 인자 (Positional Argument)

**위치 인자**는 함수 호출 시 **매개변수의 순서대로** 값을 전달하는 방식입니다.

```python
def userAdd(a, b):
    return a ** b

# 위치 인자 방식
result = userAdd(2, 3)  # a=2, b=3
print('type - ', type(result))  # 출력: type -  <class 'int'>
print('result - ', result)      # 출력: result -  8
```

#### 💻 코드 실행 상세 분석

1. **함수 호출**: `userAdd(2, 3)`이 실행됩니다.
2. **인자 매핑**: 첫 번째 인자 `2`는 매개변수 `a`에, 두 번째 인자 `3`은 매개변수 `b`에 **순서대로** 할당됩니다.
3. **거듭제곱 계산**: `a ** b`, 즉 `2 ** 3`이 계산되어 `8`이 생성됩니다.
4. **반환**: `8`이 호출자에게 반환됩니다.
5. **타입 확인**: `type(result)`는 `<class 'int'>`를 반환합니다 (정수형).
6. **결과 출력**: `print`를 통해 타입과 결과값이 출력됩니다.

### 4.2 키워드 인자 (Keyword Argument)

**키워드 인자**는 함수 호출 시 **매개변수 이름을 명시**하여 값을 전달하는 방식입니다.

```python
# 키워드 인자 방식
result = userAdd(b=2, a=3)  # 순서가 바뀌어도 이름으로 구분
print('type - ', type(result))  # 출력: type -  <class 'int'>
print('result - ', result)      # 출력: result -  9
```

#### 💻 코드 실행 상세 분석

1. **함수 호출**: `userAdd(b=2, a=3)`이 실행됩니다.
2. **인자 매핑**: `b=2`이므로 매개변수 `b`에 `2`가, `a=3`이므로 매개변수 `a`에 `3`이 할당됩니다.
3. **순서 무관**: 키워드를 사용했으므로 **인자의 순서는 중요하지 않습니다**.
4. **거듭제곱 계산**: `a ** b`, 즉 `3 ** 2`가 계산되어 `9`가 생성됩니다.
5. **반환**: `9`가 호출자에게 반환됩니다.
6. **결과 출력**: 타입과 결과값이 출력됩니다.

### 4.3 위치 인자 vs 키워드 인자 비교

| 특성 | 위치 인자 | 키워드 인자 |
|-----|---------|----------|
| **순서** | 순서가 중요함 | 순서 무관 |
| **가독성** | 매개변수가 많으면 헷갈림 | 명확함 |
| **유연성** | 낮음 | 높음 |
| **사용 시나리오** | 매개변수가 적을 때 | 매개변수가 많거나 명확성이 필요할 때 |

#### 💡 중요!: 실무에서의 사용

- **위치 인자**: 매개변수가 1-2개로 적고, 의미가 명확할 때
- **키워드 인자**: 매개변수가 많거나, 기본값이 있는 선택적 매개변수를 사용할 때

```python
# 좋은 예: 위치 인자 (매개변수가 적고 명확)
result = calculate_sum(10, 20)

# 좋은 예: 키워드 인자 (매개변수가 많고 선택적)
user = create_user(
    name="Alice",
    age=25,
    email="alice@example.com",
    is_active=True,
    role="admin"
)
```

### 4.4 혼합 사용 시 주의사항

위치 인자와 키워드 인자를 함께 사용할 때는 **위치 인자가 먼저** 와야 합니다.

```python
# 올바른 사용
result = userAdd(2, b=3)  # OK: 위치 인자 먼저, 키워드 인자 나중

# 잘못된 사용
# result = userAdd(a=2, 3)  # 에러! 키워드 인자 다음에 위치 인자 불가
```

---

## 5. 람다 함수(Lambda Function)

### 5.1 람다 함수란?

**람다 함수**는 **익명 함수(Anonymous Function)**라고도 불리며, 간단한 함수를 한 줄로 정의할 수 있는 방법입니다.

#### 5.1.1 람다 함수의 기본 구조

```python
lambda 매개변수 : 실행문
```

- `lambda` 키워드 사용
- `return` 키워드 없이 결과값을 바로 반환
- 간단한 연산이나 변환에 주로 사용

#### 5.1.2 람다 함수 생성 예제

```python
# 일반 함수
def add(x, y):
    return x + y

# 람다 함수로 변환
add = lambda x, y : x + y

# 타입 확인
print('type - ', type(add))  # 출력: type -  <class 'function'>
print(add)  # 출력: <function <lambda> at 0x...>

# 사용
result = add(3, 5)
print('result - ', result)  # 출력: result -  8
```

#### 💻 코드 실행 상세 분석

1. **람다 함수 정의**: `lambda x, y : x + y`가 실행되면서 익명 함수 객체가 생성됩니다.
2. **변수 할당**: 생성된 람다 함수가 `add` 변수에 할당됩니다.
3. **타입 확인**: `type(add)`는 함수 타입(`<class 'function'>`)을 반환합니다.
4. **함수 호출**: `add(3, 5)`가 실행되면서 `x=3`, `y=5`가 전달됩니다.
5. **연산 수행**: `x + y`, 즉 `3 + 5 = 8`이 계산됩니다.
6. **자동 반환**: 람다 함수는 `return` 없이 자동으로 연산 결과를 반환합니다.
7. **결과 저장**: 반환된 `8`이 `result` 변수에 저장됩니다.

### 5.2 람다 함수의 특징과 제약

#### 5.2.1 람다 함수의 특징

- **간결성**: 한 줄로 함수를 정의
- **익명성**: 이름이 없는 함수 (변수에 할당하여 사용)
- **표현식**: 단일 표현식만 가능 (여러 줄 불가)
- **즉시 사용**: 다른 함수의 인자로 바로 전달 가능

#### 5.2.2 람다 함수의 제약

- 복잡한 로직은 구현 불가 (한 줄 표현식만 가능)
- `if-elif-else` 같은 복잡한 분기는 어려움
- 여러 문장(statement) 사용 불가
- 독스트링(Docstring) 작성 불가

#### 📌 노트: 람다 함수 사용 시기

강사님께서 말씀하시길, **"람다 자체로는 의미가 없다"**고 하셨습니다. 람다는 주로 `map`, `filter`, `sorted`와 같은 고차 함수(Higher-Order Function)와 함께 사용될 때 진정한 가치를 발휘합니다.

### 5.3 람다 + map 함수

#### 5.3.1 map 함수란?

**`map` 함수**는 iterable(반복 가능한 객체)의 모든 요소에 함수를 적용하고, 그 결과를 `map` 객체로 반환합니다.

```python
map(function, iterable)
```

#### 5.3.2 리스트 컴프리헨션 vs map + 람다

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8]

# 방법 1: 리스트 컴프리헨션
result = [data ** 2 for data in lst]
print(result)
# 출력: [1, 4, 9, 16, 25, 36, 49, 64]

# 방법 2: map + 람다
double = list(map(lambda data : data ** 2, lst))
print(double)
# 출력: [1, 4, 9, 16, 25, 36, 49, 64]
```

#### 💻 코드 실행 상세 분석 (map + 람다)

1. **리스트 준비**: `lst = [1, 2, 3, 4, 5, 6, 7, 8]`가 메모리에 생성됩니다.
2. **람다 함수 정의**: `lambda data : data ** 2`가 생성됩니다.
3. **map 함수 실행**: `map(lambda data : data ** 2, lst)`가 실행됩니다.
4. **요소별 적용**:
   - 첫 번째 요소 `1`에 람다 함수 적용 → `1 ** 2 = 1`
   - 두 번째 요소 `2`에 람다 함수 적용 → `2 ** 2 = 4`
   - 세 번째 요소 `3`에 람다 함수 적용 → `3 ** 2 = 9`
   - ... (모든 요소에 대해 반복)
5. **map 객체 생성**: 결과들이 담긴 `map` 객체가 생성됩니다.
6. **리스트 변환**: `list()`를 통해 map 객체를 리스트로 변환합니다.
7. **결과 출력**: `[1, 4, 9, 16, 25, 36, 49, 64]`가 출력됩니다.

### 5.4 람다 + filter 함수

#### 5.4.1 filter 함수란?

**`filter` 함수**는 iterable의 요소 중 조건을 만족하는 요소만 필터링하여 반환합니다.

```python
filter(function, iterable)
```

- `function`은 `True` 또는 `False`를 반환해야 함
- 조건이 `True`인 요소만 결과에 포함

#### 5.4.2 filter 사용 예제

```python
lst = [1, 2, 3, 4, 5, 6, 7, 8]

# 짝수만 필터링
even = list(filter(lambda data : data % 2 == 0, lst))
print(even)
# 출력: [2, 4, 6, 8]
```

#### 💻 코드 실행 상세 분석

1. **람다 함수 정의**: `lambda data : data % 2 == 0` (짝수 판별 함수)
2. **filter 함수 실행**: 각 요소에 대해 람다 함수 실행
3. **조건 검사**:
   - `1 % 2 == 0` → `False` (제외)
   - `2 % 2 == 0` → `True` (포함) ✅
   - `3 % 2 == 0` → `False` (제외)
   - `4 % 2 == 0` → `True` (포함) ✅
   - ... (모든 요소 검사)
4. **filter 객체 생성**: 조건을 만족하는 요소들만 담긴 객체
5. **리스트 변환**: `list()`를 통해 리스트로 변환
6. **결과 출력**: `[2, 4, 6, 8]`

### 5.5 람다 + sorted 함수

#### 5.5.1 sorted 함수의 key 매개변수

`sorted` 함수의 `key` 매개변수에 람다 함수를 전달하여 정렬 기준을 커스터마이징할 수 있습니다.

```python
wordLst = ['pineApple', 'apple', 'watermelon', 'banana', 'cherry']

# 단어 길이를 기준으로 정렬
result = sorted(wordLst, key=lambda x : len(x))
print(result)
# 출력: ['apple', 'cherry', 'banana', 'pineApple', 'watermelon']
```

#### 💻 코드 실행 상세 분석

1. **리스트 준비**: 5개의 단어가 담긴 리스트
2. **sorted 함수 호출**: `sorted(wordLst, key=lambda x : len(x))`
3. **정렬 키 계산**: 각 단어에 대해 `len()` 계산
   - 'pineApple' → 9
   - 'apple' → 5
   - 'watermelon' → 10
   - 'banana' → 6
   - 'cherry' → 6
4. **정렬 수행**: 계산된 길이를 기준으로 오름차순 정렬
5. **결과 반환**: 길이 순으로 정렬된 새로운 리스트 반환
6. **출력**: `['apple', 'cherry', 'banana', 'pineApple', 'watermelon']`

---

## 6. 변수 스코프와 LEGB 규칙

### 6.1 변수 스코프(Scope)란?

**변수 스코프**는 변수가 접근 가능한 범위를 의미합니다. 파이썬은 **LEGB 규칙**에 따라 변수를 검색합니다.

#### 6.1.1 LEGB 규칙

강사님께서 강조하신 **함수의 규칙: LEGB**

- **L (Local)**: 지역 변수 - 함수 내부에서 정의된 변수
- **E (Enclosing)**: 인클로징 변수 - 중첩 함수의 외부 함수에서 정의된 변수
- **G (Global)**: 전역 변수 - 모듈 레벨에서 정의된 변수
- **B (Built-in)**: 내장 변수 - 파이썬이 제공하는 내장 함수/변수

**검색 순서**: Local → Enclosing → Global → Built-in

#### 💡 중요!: 변수 검색 원리

파이썬은 변수를 참조할 때:
1. 먼저 **Local**에서 찾고
2. 없으면 **Enclosing**에서 찾고
3. 없으면 **Global**에서 찾고
4. 없으면 **Built-in**에서 찾습니다
5. 어디에도 없으면 `NameError` 발생

### 6.2 전역 변수와 지역 변수

#### 6.2.1 기본 예제

```python
globalVar = 10  # 전역 변수 (모듈 레벨)
print(globalVar)  # 출력: 10 (전역에서 접근 가능)

def outer():
    enclosingVar = 20  # 인클로징 변수 (외부 함수 변수)
    
    def inner():
        localVar = 30  # 지역 변수
        print('global - ', globalVar)       # 출력: global -  10
        print('enclosingVar - ', enclosingVar)  # 출력: enclosingVar -  20
        print('localVar - ', localVar)      # 출력: localVar -  30
    
    inner()
    # print(localVar)  # 에러 발생! localVar는 inner() 내부에서만 접근 가능

outer()
print('globalVar - ', globalVar)  # 출력: globalVar -  10
# print(enclosingVar)  # 에러 발생! outer() 함수 밖에서는 접근 불가
```

#### 💻 코드 실행 상세 분석

1. **전역 변수 생성**: `globalVar = 10`이 모듈 레벨에서 생성됩니다.
2. **전역 변수 출력**: `print(globalVar)`이 성공적으로 실행됩니다 (전역 변수는 어디서나 접근 가능).
3. **outer 함수 호출**: `outer()` 함수가 실행됩니다.
4. **인클로징 변수 생성**: `enclosingVar = 20`이 outer 함수 내부에 생성됩니다.
5. **inner 함수 정의**: `def inner()`가 실행되면서 함수 객체가 생성됩니다.
6. **inner 함수 호출**: `inner()`가 실행됩니다.
7. **지역 변수 생성**: `localVar = 30`이 inner 함수 내부에 생성됩니다.
8. **변수 출력 (LEGB 규칙 적용)**:
   - `globalVar` 출력: Local에 없음 → Enclosing에 없음 → **Global에서 찾음** ✅
   - `enclosingVar` 출력: Local에 없음 → **Enclosing에서 찾음** ✅
   - `localVar` 출력: **Local에서 찾음** ✅
9. **inner 함수 종료**: localVar는 메모리에서 제거됩니다.
10. **outer 함수 내 접근 시도**: `# print(localVar)`는 주석 처리되어 있지만, 실행하면 에러 발생 (localVar는 inner 함수 종료와 함께 소멸).
11. **outer 함수 종료**: enclosingVar는 메모리에서 제거됩니다.
12. **전역에서 접근**: `print('globalVar - ', globalVar)`는 성공 (전역 변수는 여전히 존재).
13. **전역에서 enclosingVar 접근 시도**: 주석 처리되어 있지만, 실행하면 에러 발생 (outer 함수 종료와 함께 소멸).

#### 6.2.2 변수 스코프의 경계

```python
x = 10  # 전역 변수

def test():
    x = 20  # 지역 변수 (전역 변수 x와는 다른 변수)
    print(x)  # 출력: 20 (지역 변수 x)

test()
print(x)  # 출력: 10 (전역 변수 x는 변하지 않음)
```

#### 💻 코드 실행 상세 분석

1. **전역 변수 x 생성**: `x = 10` (모듈 레벨)
2. **test 함수 호출**: `test()` 실행
3. **지역 변수 x 생성**: 함수 내부에서 `x = 20` 실행
   - **중요**: 이것은 전역 변수 `x`를 수정하는 것이 아니라, **새로운 지역 변수 `x`를 생성**하는 것입니다!
4. **지역 변수 출력**: `print(x)`는 지역 변수 `x`를 출력 → `20`
5. **함수 종료**: 지역 변수 `x`는 메모리에서 제거됩니다.
6. **전역 변수 출력**: `print(x)`는 전역 변수 `x`를 출력 → `10` (변경되지 않음)

### 6.3 global 키워드

함수 내부에서 전역 변수를 **수정**하려면 `global` 키워드를 사용해야 합니다.

```python
cnt = 0  # 전역 변수

def increment():
    global cnt  # 전역 변수 cnt를 사용하겠다고 선언
    cnt += 1

increment()
increment()
increment()

print(cnt)  # 출력: 3
```

#### 💻 코드 실행 상세 분석

1. **전역 변수 초기화**: `cnt = 0`
2. **첫 번째 호출**: `increment()` 실행
   - `global cnt` 선언으로 전역 변수 `cnt`를 사용
   - `cnt += 1` 실행 → `cnt`는 `0 + 1 = 1`
3. **두 번째 호출**: `increment()` 실행
   - `cnt += 1` 실행 → `cnt`는 `1 + 1 = 2`
4. **세 번째 호출**: `increment()` 실행
   - `cnt += 1` 실행 → `cnt`는 `2 + 1 = 3`
5. **결과 출력**: `print(cnt)` → `3`

#### 🔐 보안 노트: global 키워드의 위험성

강사님께서 강조하신 점: **"보안 관점에서 전역 변수를 거의 쓰지 않는다"**

**이유**:
1. **외부 노출 위험**: 전역 변수는 모든 함수에서 접근 가능하므로 의도치 않은 수정 위험
2. **민감 정보 관리 문제**: API 키, 개인정보 등을 전역 변수로 관리하면 보안 취약점 발생
3. **디버깅 어려움**: 어디서 변수가 수정되었는지 추적하기 어려움
4. **테스트 어려움**: 전역 상태에 의존하면 단위 테스트가 복잡해짐

**대안**: 클로저(Closure)와 데코레이터를 활용한 안전한 상태 관리 (다음 섹션에서 설명)

### 6.4 nonlocal 키워드

중첩 함수에서 **외부 함수의 변수를 수정**하려면 `nonlocal` 키워드를 사용합니다.

```python
def outer():
    outerVar = 10  # 외부 함수의 지역 변수 (inner 입장에서는 인클로징 변수)
    
    def inner():
        nonlocal outerVar  # 외부 함수의 outerVar를 사용하겠다고 선언
        outerVar += 1
        print('inner outerVar : ', outerVar)
    
    inner()
    print('outer outerVar : ', outerVar)

outer()
# 출력:
# inner outerVar :  11
# outer outerVar :  11
```

#### 💻 코드 실행 상세 분석

1. **outer 함수 호출**: `outer()` 실행
2. **outerVar 초기화**: `outerVar = 10` (outer 함수의 지역 변수)
3. **inner 함수 정의**: `def inner()` 실행
4. **inner 함수 호출**: `inner()` 실행
5. **nonlocal 선언**: `nonlocal outerVar`로 외부 함수의 변수 사용 선언
6. **값 수정**: `outerVar += 1` → `outerVar`는 `10 + 1 = 11`
7. **inner 출력**: `print('inner outerVar : ', outerVar)` → `11`
8. **inner 함수 종료**: inner 함수가 종료되지만, outerVar는 outer 함수의 변수이므로 유지됨
9. **outer 출력**: `print('outer outerVar : ', outerVar)` → `11` (inner에서 수정된 값)
10. **outer 함수 종료**: outerVar가 메모리에서 제거됨

#### 📌 노트: global vs nonlocal

| 키워드 | 대상 | 사용 시나리오 |
|-------|-----|-------------|
| `global` | 전역 변수 | 함수 내부에서 전역 변수 수정 |
| `nonlocal` | 인클로징 변수 | 중첩 함수에서 외부 함수의 변수 수정 |

---

## 7. 클로저(Closure) - 상태 유지의 비밀

### 7.1 클로저란 무엇인가?

**클로저(Closure)**는 함수가 자신이 정의된 환경(외부 함수의 변수)을 "기억"하는 기능입니다.

#### 7.1.1 클로저의 핵심 개념

- **일반 함수**: 호출이 끝나면 지역 변수는 소멸하고 상태를 기억하지 못함
- **클로저**: 함수가 종료되어도 **외부 함수의 변수를 기억**함
- **중첩 함수**: 함수 내부에 또 다른 함수가 정의되어야 클로저 생성 가능

#### 💡 중요!: 클로저의 목적

강사님께서 강조하신 클로저의 핵심: **"상태 유지 (State Preservation)"**

클로저를 사용하면:
- **전역 변수를 쓰지 않고도** 함수 내부에서 상태를 유지할 수 있음
- 보안적으로 더 안전한 코드 작성 가능
- 데이터 은닉(Data Hiding) 구현 가능

### 7.2 클로저의 기본 구조

#### 7.2.1 첫 번째 클로저 예제

```python
def outer(name : str):
    def inner():  # 외부에서 접근할 수 없음 (은닉화)
        return f'hi ~ , {name}'
    return inner  # 함수를 반환

# 함수 호출
msg = outer('jslim')  # outer 함수가 종료됨

print(msg, 'type - ', type(msg))
# 출력: <function outer.<locals>.inner at 0x...> type -  <class 'function'>

print('result - ', msg())
# 출력: result -  hi ~ , jslim
```

#### 💻 코드 실행 상세 분석

1. **outer 함수 호출**: `outer('jslim')` 실행
2. **매개변수 전달**: `name` 매개변수에 `'jslim'` 저장
3. **inner 함수 정의**: `def inner()` 실행되면서 inner 함수 객체 생성
   - **중요**: inner 함수는 외부 변수 `name`을 참조함
4. **함수 반환**: `return inner`로 **inner 함수 자체**(호출X)를 반환
5. **outer 함수 종료**: 일반적으로는 `name` 변수가 소멸해야 함
6. **클로저 생성**: 하지만! inner 함수가 `name`을 참조하므로, **`name`은 메모리에 유지됨** ✨
7. **msg 변수에 저장**: inner 함수 객체가 `msg`에 저장됨
8. **타입 확인**: `type(msg)`는 함수 타입을 반환
9. **클로저 호출**: `msg()`를 실행하면 inner 함수가 실행됨
10. **기억된 변수 사용**: inner 함수는 여전히 `name='jslim'`을 기억하고 있음!
11. **결과 반환**: `f'hi ~ , {name}'`가 평가되어 `'hi ~ , jslim'` 반환

#### 🌟 클로저의 핵심 포인트

**outer 함수가 종료되었는데도 `name` 변수를 기억하고 있다!** 이것이 바로 클로저의 핵심입니다.

### 7.3 클로저를 이용한 상태 유지

#### 7.3.1 문제가 있는 코드 (전역 변수 사용)

```python
# 보안 관점에서 취약한 코드
cnt = 0  # 전역 변수 (누구나 접근/수정 가능)

def increment():
    global cnt
    cnt += 1

increment()
increment()
increment()

print(cnt)  # 출력: 3
```

**문제점**:
- `cnt`가 전역 변수이므로 어디서든 접근 가능
- 실수로 다른 곳에서 `cnt`를 수정할 위험
- 보안상 취약 (민감한 데이터를 이런 식으로 관리하면 위험)

#### 7.3.2 개선된 코드 (클로저 사용)

```python
def counter():
    count = 0  # 지역 변수 (중첩 함수 입장에서는 인클로징 변수)
    
    def increase():
        nonlocal count  # count 변수를 사용하겠다고 선언
        count += 1
        return count
    
    return increase  # increase 함수를 반환

# 카운터 생성
cnt = counter()  # cnt는 increase 함수

# 카운터 사용
print(cnt())  # 출력: 1
print(cnt())  # 출력: 2
print(cnt())  # 출력: 3
print(cnt())  # 출력: 4
print(cnt())  # 출력: 5
```

#### 💻 코드 실행 상세 분석

1. **counter 함수 호출**: `counter()` 실행
2. **count 초기화**: `count = 0` (counter 함수의 지역 변수)
3. **increase 함수 정의**: `def increase()` 실행
   - increase 함수는 외부 변수 `count`를 참조
4. **함수 반환**: `return increase`로 increase 함수 반환
5. **클로저 생성**: increase 함수가 `count` 변수를 기억하는 클로저 생성
6. **cnt에 저장**: increase 함수가 `cnt` 변수에 저장됨

**각 호출마다**:
7. **첫 번째 cnt() 호출**:
   - `nonlocal count`로 클로저의 count 사용
   - `count += 1` → `count`는 `0 + 1 = 1`
   - `return count` → `1` 반환
   
8. **두 번째 cnt() 호출**:
   - 클로저가 기억하고 있는 `count`는 `1`
   - `count += 1` → `count`는 `1 + 1 = 2`
   - `return count` → `2` 반환

9. **세 번째 cnt() 호출**:
   - `count`는 `2`
   - `count += 1` → `count`는 `2 + 1 = 3`
   - `return count` → `3` 반환

**이후 호출도 동일하게 상태가 유지됨**

#### 🔐 보안 노트: 클로저의 장점

1. **데이터 은닉**: `count` 변수는 외부에서 직접 접근 불가
2. **상태 보호**: 의도하지 않은 수정 방지
3. **캡슐화**: 상태와 로직을 하나로 묶음
4. **전역 변수 대체**: 전역 변수 없이도 상태 유지 가능

```python
# 외부에서 count에 직접 접근 시도
# print(count)  # 에러 발생! count는 외부에서 접근 불가

# cnt를 통해서만 상태 변경 가능
print(cnt())  # 정상 작동
```

### 7.4 클로저를 활용한 실전 예제

#### 7.4.1 여러 개의 독립적인 카운터 생성

```python
def counter():
    count = 0
    def increase():
        nonlocal count
        count += 1
        return count
    return increase

# 독립적인 카운터 3개 생성
counter1 = counter()
counter2 = counter()
counter3 = counter()

# 각각 독립적으로 동작
print(counter1())  # 출력: 1
print(counter1())  # 출력: 2

print(counter2())  # 출력: 1 (counter1과 독립적)
print(counter2())  # 출력: 2

print(counter3())  # 출력: 1 (다른 카운터들과 독립적)

print(counter1())  # 출력: 3 (자신의 상태 유지)
```

#### 💻 코드 실행 상세 분석

1. **첫 번째 카운터 생성**: `counter1 = counter()`
   - 새로운 클로저 생성 (`count1` 변수 생성)
2. **두 번째 카운터 생성**: `counter2 = counter()`
   - 또 다른 독립적인 클로저 생성 (`count2` 변수 생성)
3. **세 번째 카운터 생성**: `counter3 = counter()`
   - 또 다른 독립적인 클로저 생성 (`count3` 변수 생성)

**각 카운터는 자신만의 `count` 변수를 가지고 있어 서로 영향을 주지 않음!**

#### 7.4.2 추가 연습 문제

```python
def clo(num):
    x = 10
    def test():
        nonlocal x
        x += num
        return x
    return test

a = clo(1)
print(a())  # 출력: 11
print(a())  # 출력: 12
print(a())  # 출력: 13
print(a())  # 출력: 14
```

#### 💻 코드 실행 상세 분석

1. **clo(1) 호출**:
   - `num = 1` 매개변수 저장
   - `x = 10` 초기화
   - test 함수가 `x`와 `num`을 기억하는 클로저 생성
   
2. **첫 번째 a() 호출**:
   - 기억하고 있는 `x = 10`, `num = 1`
   - `x += num` → `x = 10 + 1 = 11`
   - 반환: `11`

3. **두 번째 a() 호출**:
   - 이전 상태 기억: `x = 11`, `num = 1`
   - `x += num` → `x = 11 + 1 = 12`
   - 반환: `12`

**이후 호출도 동일한 패턴**

---

## 8. 데코레이터(Decorator) - 함수 장식자

### 8.1 데코레이터란?

**데코레이터(Decorator)**는 기존 함수를 수정하지 않고 **기능을 추가하거나 확장**하는 문법입니다. 클로저를 기반으로 동작합니다.

#### 8.1.1 데코레이터의 필요성

강사님께서 설명하신 실무 시나리오:

- **로깅(Logging)**: 모든 함수 호출을 기록해야 할 때
- **권한 체크(Authorization)**: 함수 실행 전 사용자 권한 확인
- **실행 시간 측정(Performance Monitoring)**: 함수의 실행 시간 측정
- **캐싱(Caching)**: 함수 결과를 캐시하여 성능 향상
- **예외 처리(Error Handling)**: 모든 함수에 일관된 예외 처리 추가

#### 💡 중요!: 데코레이터의 핵심 개념

강사님께서 강조하신 점: **"반복되는 작업을 별도로 만들지 않고, cross-cutting(횡단 관심사)으로 치고 들어가서 진행"**

즉, 데코레이터는:
- **공통 기능**이어야 함 (특정 로직을 건드리는 게 아님)
- **비즈니스 로직에 집중**할 수 있게 함 (부가 기능은 데코레이터가 처리)

### 8.2 데코레이터의 기본 구조 (클로저 기반)

#### 8.2.1 기본 데코레이터 예제

```python
# 공통 기능 함수들
def commonChecking():
    print(">>>>>> permission check")

def commonLogging():
    print('>>>>>>> log...')

# 데코레이터 함수
def decorator(checkingFunc, loggingFunc):
    def logic():
        checkingFunc()       # 권한 체크
        print('업무로직 수행')  # 실제 업무 로직
        loggingFunc()        # 로깅
    return logic

# 데코레이터 사용
innerLogic = decorator(commonChecking, commonLogging)
innerLogic()
```

**출력**:
```
>>>>>> permission check
업무로직 수행
>>>>>>> log...
```

#### 💻 코드 실행 상세 분석

1. **공통 기능 함수 정의**: `commonChecking`과 `commonLogging` 함수 생성
2. **decorator 함수 호출**: `decorator(commonChecking, commonLogging)` 실행
   - `checkingFunc = commonChecking` 저장
   - `loggingFunc = commonLogging` 저장
3. **logic 함수 정의**: 내부 함수 `logic` 생성
   - `checkingFunc`와 `loggingFunc`를 기억하는 클로저
4. **logic 함수 반환**: `return logic`으로 logic 함수 자체 반환
5. **innerLogic에 저장**: logic 함수가 `innerLogic` 변수에 저장
6. **innerLogic 호출**: `innerLogic()` 실행
7. **순차 실행**:
   - `checkingFunc()` 호출 → ">>>>>> permission check" 출력
   - `print('업무로직 수행')` 실행 → "업무로직 수행" 출력
   - `loggingFunc()` 호출 → ">>>>>>> log..." 출력

#### 📌 노트: 데코레이터 패턴의 이점

- **코드 중복 제거**: 권한 체크와 로깅을 매번 작성할 필요 없음
- **관심사 분리(Separation of Concerns)**: 비즈니스 로직과 부가 기능 분리
- **유지보수 용이**: 공통 기능 수정 시 한 곳만 수정하면 됨

### 8.3 데코레이터의 실전 활용

#### 8.3.1 실행 시간 측정 데코레이터 (개념)

```python
# 강의에서 언급된 실행 시간 측정 데코레이터 개념
from time import time

def timer(func):
    """함수의 실행 시간을 측정하는 데코레이터"""
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"실행 시간: {end_time - start_time}초")
        return result
    return wrapper

# 사용 예시 (개념)
# @timer
# def slow_function():
#     # 시간이 오래 걸리는 작업
#     pass
```

#### 💡 중요!: 내일 학습 예정

강사님께서 말씀하시길, **데코레이터의 상세한 활용법과 @ 문법은 내일(Day 5) 더 깊이 있게 다룬다**고 하셨습니다.

---

## 9. 가변인자 함수 (*args, **kwargs)

### 9.1 가변인자란?

**가변인자 함수**는 **몇 개의 매개변수가 전달될지 모르는 상황**에서 사용하는 함수입니다.

파이썬에는 두 가지 종류의 가변인자가 있습니다:
1. **`*args`**: 튜플(tuple) 형태로 받음
2. **`**kwargs`**: 딕셔너리(dict) 형태로 받음 (키워드 인자)

### 9.2 *args (튜플 형태의 가변인자)

#### 9.2.1 기본 사용법

```python
def variableLenArgs(*args: int) -> None:
    """가변 개수의 정수를 받아 합계를 계산하는 함수"""
    print('type - ', type(args))  # 튜플 타입 확인
    total = sum(args)
    return total

# 다양한 개수의 인자로 호출 가능
result = variableLenArgs(1, 2, 3)
print(result)  # 출력: 6

result = variableLenArgs(1, 2, 3, 4, 5)
print(result)  # 출력: 15

result = variableLenArgs(1, 2, 3, 4, 5, 6, 7, 8)
print(result)  # 출력: 36
```

#### 💻 코드 실행 상세 분석 (첫 번째 호출)

1. **함수 호출**: `variableLenArgs(1, 2, 3)` 실행
2. **인자 패킹**: 전달된 인자들이 **튜플로 패킹**됨
   - `args = (1, 2, 3)` 튜플 생성
3. **타입 확인**: `type(args)`는 `<class 'tuple'>` 반환
4. **합계 계산**: `sum(args)` → `sum((1, 2, 3))` → `6`
5. **결과 반환**: `6`이 반환됨
6. **결과 출력**: `print(result)` → `6`

**두 번째, 세 번째 호출도 동일한 방식으로 동작하지만 인자 개수만 다름**

#### 📌 노트: *args의 특징

- **튜플 타입**: args는 항상 튜플입니다
- **개수 제한 없음**: 0개부터 무한대까지 받을 수 있음
- **순서 유지**: 전달된 순서대로 튜플에 저장됨
- **언패킹 가능**: for 루프로 각 요소 접근 가능

### 9.3 **kwargs (딕셔너리 형태의 가변인자)

#### 9.3.1 기본 사용법

```python
def variableLenArgsDict(**args):
    """키워드 인자를 받아 출력하는 함수"""
    print('type - ', type(args))  # 딕셔너리 타입 확인
    for key, value in args.items():
        print(key, value)

# 키워드 인자로 호출
variableLenArgsDict(name='jslim', age=30, region='seoul')
```

**출력**:
```
type -  <class 'dict'>
name jslim
age 30
region seoul
```

#### 💻 코드 실행 상세 분석

1. **함수 호출**: `variableLenArgsDict(name='jslim', age=30, region='seoul')` 실행
2. **키워드 인자 패킹**: 키워드 인자들이 **딕셔너리로 패킹**됨
   - `args = {'name': 'jslim', 'age': 30, 'region': 'seoul'}`
3. **타입 확인**: `type(args)`는 `<class 'dict'>` 반환
4. **딕셔너리 순회**: `args.items()`로 키-값 쌍 추출
   - 첫 번째 반복: `key='name'`, `value='jslim'`
   - 두 번째 반복: `key='age'`, `value=30`
   - 세 번째 반복: `key='region'`, `value='seoul'`
5. **각 쌍 출력**: `print(key, value)`로 출력

#### 📌 노트: **kwargs의 특징

- **딕셔너리 타입**: kwargs는 항상 딕셔너리입니다
- **키-값 쌍**: 키워드 인자가 딕셔너리의 키-값 쌍으로 저장됨
- **순서 보장**: Python 3.7+에서는 삽입 순서 유지
- **키 접근**: `args['name']` 형태로 값 접근 가능

### 9.4 혼합 사용 (일반 매개변수 + *args + **kwargs)

#### 9.4.1 모든 종류의 매개변수 함께 사용

```python
def variableLenArgsMix(subject, *args, **kwargs):
    """일반 매개변수, 가변 위치 인자, 가변 키워드 인자를 모두 받는 함수"""
    print('subject  - ', subject)
    print('args     - ', args)
    print('kwargs   - ', kwargs)

# 호출
variableLenArgsMix("사용자 정보", "임섭순", "섭섭해", "쉴더스", a=1, b=2)
```

**출력**:
```
subject  -  사용자 정보
args     -  ('임섭순', '섭섭해', '쉴더스')
kwargs   -  {'a': 1, 'b': 2}
```

#### 💻 코드 실행 상세 분석

1. **함수 호출**: `variableLenArgsMix("사용자 정보", "임섭순", "섭섭해", "쉴더스", a=1, b=2)` 실행
2. **인자 분류**:
   - **일반 매개변수**: 첫 번째 인자 `"사용자 정보"`가 `subject`에 할당
   - **위치 인자**: 나머지 위치 인자들 `("임섭순", "섭섭해", "쉴더스")`가 `args` 튜플로 패킹
   - **키워드 인자**: `a=1, b=2`가 `kwargs` 딕셔너리로 패킹 `{'a': 1, 'b': 2}`
3. **각 값 출력**: 세 가지 유형의 매개변수가 각각 출력됨

#### 📌 노트: 매개변수 순서 규칙

함수를 정의할 때 매개변수 순서는 반드시 다음과 같아야 합니다:

```python
def function(일반_매개변수, *args, **kwargs):
    pass
```

**순서**:
1. 일반 매개변수 (필수 매개변수)
2. `*args` (가변 위치 인자)
3. `**kwargs` (가변 키워드 인자)

**잘못된 순서**:
```python
# def function(**kwargs, *args, 일반):  # 에러!
```

---

## 10. 실전 예제: API 엔드포인트 생성

### 10.1 엔드포인트(Endpoint)란?

강의 후반부에서 강사님께서 설명하신 실무 개념입니다.

#### 10.1.1 엔드포인트의 정의

**엔드포인트(Endpoint)**는:
- **마지막에 도착하는 호스트**를 의미
- 프론트엔드에서 백엔드로 데이터를 요청할 때 사용하는 **URL**
- API 명세서에 정의된 통신 규칙

#### 10.1.2 프론트엔드와 백엔드의 통신

```
[프론트엔드] -----(요청)-----> [백엔드]
     |                           |
     |  엔드포인트 URL              |
     |  + 파라미터                 |
     |                           |
     |<----(응답: JSON)---------- |
```

**API 명세서 예시**:
- **엔드포인트**: `https://api.v1.example.com/search`
- **메서드**: GET
- **파라미터**: 
  - `q`: 검색어 (필수)
  - `page`: 페이지 번호 (선택, 기본값: 1)
- **응답 형식**: JSON

### 10.2 기본 API 엔드포인트 생성

#### 10.2.1 요구사항

다음과 같은 API 요청을 생성하는 함수 작성:
```
https://api.v1.example.com/search?q=secure&page=2
```

#### 10.2.2 첫 번째 구현 (기본 버전)

```python
def makeApiRequest(endpoint, **params):
    """엔드포인트와 파라미터를 받아 API URL을 생성하는 함수"""
    # 딕셔너리를 수동으로 Query String으로 변환
    query_parts = []
    for key, value in params.items():
        query_parts.append(f"{key}={value}")
    
    query_string = '&'.join(query_parts)
    return endpoint + '?' + query_string

# 사용
result = makeApiRequest(
    'https://api.v1.example.com/search',
    q='secure',
    page=2
)
print(result)
# 출력: https://api.v1.example.com/search?q=secure&page=2
```

#### 💻 코드 실행 상세 분석

1. **함수 호출**: `makeApiRequest('https://api.v1.example.com/search', q='secure', page=2)` 실행
2. **인자 분류**:
   - `endpoint = 'https://api.v1.example.com/search'`
   - `params = {'q': 'secure', 'page': 2}`
3. **빈 리스트 생성**: `query_parts = []`
4. **딕셔너리 순회 및 변환**:
   - 첫 번째 반복: `key='q'`, `value='secure'`
     - `"q=secure"` 생성
     - `query_parts = ['q=secure']`
   - 두 번째 반복: `key='page'`, `value=2`
     - `"page=2"` 생성
     - `query_parts = ['q=secure', 'page=2']`
5. **Query String 생성**: `'&'.join(query_parts)` → `'q=secure&page=2'`
6. **URL 조합**: `endpoint + '?' + query_string`
   - `'https://api.v1.example.com/search' + '?' + 'q=secure&page=2'`
   - 결과: `'https://api.v1.example.com/search?q=secure&page=2'`
7. **반환**: 완성된 URL 반환

### 10.3 개선된 구현 (urlencode 사용)

#### 10.3.1 urllib.parse.urlencode 활용

파이썬 표준 라이브러리의 `urlencode` 함수를 사용하면 더 안전하고 간편합니다.

```python
from urllib.parse import urlencode

def makeApiRequest(endpoint, **params):
    """urlencode를 사용한 개선된 API URL 생성 함수"""
    query_string = urlencode(params)
    return endpoint + '?' + query_string

# 사용
result = makeApiRequest(
    'https://api.v1.example.com/search',
    q='secure',
    page=2
)
print(result)
# 출력: https://api.v1.example.com/search?q=secure&page=2
```

#### 💻 코드 실행 상세 분석

1. **함수 호출**: 이전과 동일
2. **urlencode 실행**: `urlencode(params)` 호출
   - `params = {'q': 'secure', 'page': 2}`
   - 자동으로 URL 인코딩 수행
   - 특수문자, 공백 등이 있으면 안전하게 인코딩
   - 결과: `'q=secure&page=2'`
3. **URL 조합**: `endpoint + '?' + query_string`
4. **반환**: 완성된 URL 반환

#### 📌 노트: urlencode의 장점

- **자동 인코딩**: 특수문자, 공백, 한글 등을 자동으로 URL 인코딩
- **안전성**: 표준 라이브러리이므로 검증된 코드
- **간결성**: 한 줄로 처리 가능

```python
# 예시: 특수문자가 포함된 경우
from urllib.parse import urlencode

params = {"q": "파이썬 보안", "filter": "top>100"}
print(urlencode(params))
# 출력: q=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EB%B3%B4%EC%95%88&filter=top%3E100
```

---

## 11. 보안 관점에서의 코드 개선

### 11.1 URL 생성 함수의 보안 문제점

#### 11.1.1 XSS(Cross-Site Scripting) 취약점

**XSS 공격 시나리오**:

```python
def makeUrl(lst : list) -> list:
    """회사 이름을 받아 URL을 생성하는 함수 (취약한 버전)"""
    return list(map(lambda x : 'www.' + x + '.com', lst))

# 공격 예시
companyLst = [
    'skshieldus',
    'samsung',
    'lgcns',
    '<script>alert(1)</script>'  # 악성 스크립트!
]
urls = makeUrl(companyLst)
print(urls)
# 출력: ['www.skshieldus.com', 'www.samsung.com', 'www.lgcns.com', 
#       'www.<script>alert(1)</script>.com']
```

**문제점**:
- 입력 데이터에 대한 검증 없이 URL 생성
- 악성 스크립트가 그대로 URL에 포함됨
- 웹 페이지에 출력 시 XSS 공격 발생 가능

#### 11.1.2 개선 방법 1: URL 인코딩

```python
from urllib.parse import quote

def safeMakeUrl(lst : list) -> list:
    """quote를 사용한 안전한 URL 생성 (1차 개선)"""
    return list(map(lambda x : 'www.' + quote(x) + '.com', lst))

# 사용
companyLst = ['sk shieldus', 'samsung', '<script>alert(1)</script>']
urls = safeMakeUrl(companyLst)
print(urls)
# 출력: ['www.sk%20shieldus.com', 'www.samsung.com', 
#       'www.%3Cscript%3Ealert%281%29%3C/script%3E.com']
```

#### 💻 코드 실행 상세 분석

1. **함수 호출**: `safeMakeUrl(companyLst)` 실행
2. **map + 람다 적용**: 각 요소에 대해 람다 함수 실행
3. **첫 번째 요소**: `'sk shieldus'`
   - `quote('sk shieldus')` → `'sk%20shieldus'` (공백이 `%20`으로 인코딩)
   - 결과: `'www.sk%20shieldus.com'`
4. **두 번째 요소**: `'samsung'`
   - `quote('samsung')` → `'samsung'` (특수문자 없음)
   - 결과: `'www.samsung.com'`
5. **세 번째 요소**: `'<script>alert(1)</script>'`
   - `quote('<script>alert(1)</script>')` → `'%3Cscript%3Ealert%281%29%3C/script%3E'`
   - **특수문자가 모두 안전하게 인코딩됨** ✅
   - 결과: `'www.%3Cscript%3Ealert%281%29%3C/script%3E.com'`
6. **리스트 반환**: 모든 URL이 안전하게 인코딩됨

#### 🔐 보안 노트: URL 인코딩의 효과

- **XSS 방지**: `<`, `>` 등의 HTML 태그 문자가 인코딩되어 스크립트 실행 불가
- **공백 처리**: 공백이 `%20`으로 변환되어 URL 형식 유지
- **특수문자 안전**: 모든 특수문자가 안전한 형식으로 변환

#### 11.1.3 개선 방법 2: 입력값 검증 + URL 인코딩

```python
from urllib.parse import quote

def safeMakeUrl(lst : list) -> list:
    """입력값 검증 + URL 인코딩 (최종 개선 버전)"""
    
    # 1. 타입 검증
    if not isinstance(lst, list):
        raise TypeError("입력은 리스트 타입으로 전달 부탁드립니다.")
    
    # 2. 요소 타입 검증
    if not all(isinstance(name, str) for name in lst):
        raise ValueError('요소의 타입은 문자열')
    
    # 3. 안전하게 URL 인코딩
    return list(map(lambda x : 'www.' + quote(x) + '.com', lst))

# 사용
companyLst = ['skshieldus', 'samsung', '<script>alert(1)</script>']
urls = safeMakeUrl(companyLst)
print(urls)
# 정상 작동 (검증 통과 + 안전한 인코딩)
```

#### 💻 코드 실행 상세 분석

1. **함수 호출**: `safeMakeUrl(companyLst)` 실행
2. **타입 검증**: `isinstance(lst, list)` 검사
   - `lst`가 리스트인지 확인
   - 리스트가 아니면 `TypeError` 발생
3. **요소 타입 검증**: `all(isinstance(name, str) for name in lst)` 검사
   - 모든 요소가 문자열인지 확인
   - 하나라도 문자열이 아니면 `ValueError` 발생
4. **검증 통과**: 모든 검증 통과 후 URL 생성 진행
5. **URL 인코딩**: 이전 예제와 동일하게 `quote()` 사용
6. **안전한 URL 반환**

#### 🔐 보안 노트: 다층 방어 (Defense in Depth)

**보안의 여러 계층**:
1. **입력 검증 (Input Validation)**: 잘못된 타입이나 데이터 형식 차단
2. **인코딩 (Encoding)**: 특수문자를 안전한 형식으로 변환
3. **화이트리스트 (Whitelist)**: 허용된 값만 처리 (다음 예제에서 설명)

### 11.2 API 파라미터 필터링 (화이트리스트)

#### 11.2.1 취약한 코드 예시

```python
from urllib.parse import urlencode

def makeApiRequest(endpoint, **params):
    """파라미터 필터링 없는 버전 (취약)"""
    query_string = urlencode(params)
    return endpoint + '?' + query_string

# 공격 시나리오: 의도하지 않은 파라미터 전달
result = makeApiRequest(
    'https://api.v1.example.com/search',
    q='secure',
    page=2,
    token='shieldus',  # 악의적인 토큰 파라미터!
    admin='true'       # 권한 상승 시도!
)
print(result)
# 출력: https://api.v1.example.com/search?q=secure&page=2&token=shieldus&admin=true
```

**문제점**:
- 허용되지 않은 파라미터(`token`, `admin`)가 URL에 포함됨
- 백엔드 API가 이런 파라미터를 처리하면 보안 문제 발생 가능
- 민감한 정보나 권한 관련 파라미터가 노출될 수 있음

#### 11.2.2 화이트리스트를 사용한 개선

```python
from urllib.parse import urlencode

def makeApiRequest(endpoint, **params):
    """화이트리스트 기반 파라미터 필터링 (안전한 버전)"""
    
    # 1. 허용된 파라미터 목록 (화이트리스트)
    whiteLst = {'q', 'page', 'lang'}
    
    # 2. 화이트리스트에 있는 파라미터만 필터링
    safeParams = {k : v for k, v in params.items() if k in whiteLst}
    
    # 3. 안전한 파라미터로 Query String 생성
    query_string = urlencode(safeParams)
    
    return endpoint + '?' + query_string

# 사용 (악의적인 파라미터 포함)
result = makeApiRequest(
    'https://api.v1.example.com/search',
    q='secure',
    page=2,
    token='shieldus',  # 필터링됨!
    admin='true'       # 필터링됨!
)
print(result)
# 출력: https://api.v1.example.com/search?q=secure&page=2
# token과 admin 파라미터가 제거됨!
```

#### 💻 코드 실행 상세 분석

1. **함수 호출**: `makeApiRequest(...)` 실행
2. **params 수신**: `params = {'q': 'secure', 'page': 2, 'token': 'shieldus', 'admin': 'true'}`
3. **화이트리스트 정의**: `whiteLst = {'q', 'page', 'lang'}`
4. **딕셔너리 컴프리헨션 실행**: `{k : v for k, v in params.items() if k in whiteLst}`
   - **첫 번째 항목**: `k='q'`, `v='secure'`
     - `'q' in whiteLst` → `True` ✅
     - 포함: `{'q': 'secure'}`
   - **두 번째 항목**: `k='page'`, `v=2`
     - `'page' in whiteLst` → `True` ✅
     - 포함: `{'q': 'secure', 'page': 2}`
   - **세 번째 항목**: `k='token'`, `v='shieldus'`
     - `'token' in whiteLst` → `False` ❌
     - **제외됨**
   - **네 번째 항목**: `k='admin'`, `v='true'`
     - `'admin' in whiteLst` → `False` ❌
     - **제외됨**
5. **안전한 파라미터**: `safeParams = {'q': 'secure', 'page': 2}`
6. **URL 생성**: 허용된 파라미터만으로 URL 생성
7. **결과 반환**: `https://api.v1.example.com/search?q=secure&page=2`

#### 🔐 보안 노트: 화이트리스트 방식의 장점

**화이트리스트(Whitelist) vs 블랙리스트(Blacklist)**:

| 방식 | 설명 | 장점 | 단점 |
|-----|------|-----|-----|
| **화이트리스트** | 허용된 것만 통과 | 안전 (기본적으로 모두 차단) | 허용 목록 관리 필요 |
| **블랙리스트** | 금지된 것만 차단 | 유연함 | 누락된 위협 발생 가능 |

강사님께서 강조하신 점: **"보안에서는 화이트리스트 방식을 선호"**

**이유**:
- **기본적으로 거부**: 명시적으로 허용한 것만 통과
- **새로운 공격에 안전**: 알려지지 않은 악성 파라미터도 자동 차단
- **예측 가능성**: 어떤 파라미터가 허용되는지 명확

### 11.3 보안 강화 체크리스트

#### 11.3.1 입력값 검증

```python
def secure_function(data):
    """보안이 강화된 함수 예제"""
    
    # 1. 타입 검증
    if not isinstance(data, expected_type):
        raise TypeError("잘못된 타입입니다.")
    
    # 2. 값 범위 검증
    if not (min_value <= data <= max_value):
        raise ValueError("값이 허용 범위를 벗어났습니다.")
    
    # 3. 패턴 검증 (정규표현식)
    import re
    if not re.match(pattern, data):
        raise ValueError("올바르지 않은 형식입니다.")
    
    # 4. 화이트리스트 검증
    if data not in allowed_values:
        raise ValueError("허용되지 않은 값입니다.")
    
    # ... 비즈니스 로직 수행
```

#### 11.3.2 보안 코딩 원칙

강사님께서 강조하신 보안 원칙들:

1. **절대 사용자 입력을 신뢰하지 말 것**
   - 모든 입력은 검증되어야 함
   - 클라이언트 사이드 검증만으로는 부족 (서버 사이드 검증 필수)

2. **최소 권한 원칙 (Principle of Least Privilege)**
   - 필요한 최소한의 권한만 부여
   - 전역 변수 대신 지역 변수 사용
   - 클로저를 활용한 데이터 은닉

3. **방어적 프로그래밍 (Defensive Programming)**
   - 예외 상황을 항상 고려
   - 에러 처리 철저히
   - 기본값을 안전한 값으로 설정

4. **다층 방어 (Defense in Depth)**
   - 여러 보안 계층 구현
   - 한 계층이 뚫려도 다른 계층에서 막을 수 있도록

5. **보안 라이브러리 활용**
   - 검증된 표준 라이브러리 사용 (예: `urllib.parse`)
   - 직접 구현보다는 라이브러리 활용

---

## 📚 오늘의 핵심 정리

### ✅ 반드시 기억해야 할 5가지

1. **함수는 코드 재사용성과 유지보수성을 위해 필수**
   - 반복되는 코드는 함수로 만들기
   - 함수 이름은 동사형으로 (예: `calculateSum`, `validateInput`)

2. **LEGB 규칙을 이해하고 변수 스코프 관리**
   - Local → Enclosing → Global → Built-in 순서로 변수 검색
   - 전역 변수는 보안상 위험 (가능한 사용 자제)

3. **클로저를 활용한 안전한 상태 관리**
   - 클로저 = 함수가 외부 변수를 기억하는 기능
   - 전역 변수 대신 클로저로 상태 유지
   - 데이터 은닉과 캡슐화 가능

4. **가변인자로 유연한 함수 작성**
   - `*args`: 튜플 형태 (위치 인자)
   - `**kwargs`: 딕셔너리 형태 (키워드 인자)
   - API 엔드포인트 생성 등에 활용

5. **보안 관점에서 함수 작성**
   - 입력값 검증 철저히 (타입, 범위, 패턴)
   - URL 인코딩으로 XSS 방지
   - 화이트리스트로 파라미터 필터링

### 🔍 실무 적용 팁

#### Tip 1: 함수 설계 시 고려사항

```python
def good_function_design(input_data, options=None):
    """
    좋은 함수 설계 예시
    
    Args:
        input_data: 필수 입력 데이터
        options: 선택적 옵션 (기본값: None)
    
    Returns:
        처리된 결과
    
    Raises:
        TypeError: 잘못된 타입일 경우
        ValueError: 잘못된 값일 경우
    """
    # 1. 입력 검증
    if not isinstance(input_data, expected_type):
        raise TypeError("...")
    
    # 2. 기본값 처리
    if options is None:
        options = default_options
    
    # 3. 비즈니스 로직
    result = process(input_data, options)
    
    # 4. 결과 반환
    return result
```

#### Tip 2: 람다는 간단한 경우에만

```python
# 좋은 예: 간단한 변환
doubled = list(map(lambda x: x * 2, numbers))

# 나쁜 예: 복잡한 로직은 일반 함수로
# result = list(map(lambda x: x * 2 if x > 0 else x / 2 if x < 0 else 0, numbers))

# 개선: 일반 함수 사용
def transform(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return x / 2
    else:
        return 0

result = list(map(transform, numbers))
```

#### Tip 3: 클로저는 간단한 상태 관리에만

```python
# 적절한 사용: 간단한 카운터
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# 부적절한 사용: 복잡한 상태 관리는 클래스 사용
class ComplexCounter:
    """복잡한 상태 관리는 클래스로"""
    def __init__(self):
        self.count = 0
        self.history = []
    
    def increment(self):
        self.count += 1
        self.history.append(self.count)
        return self.count
    
    def get_average(self):
        return sum(self.history) / len(self.history)
```

---

## 💭 강사님의 조언

### 내일 학습 예정 내용

강사님께서 내일(Day 5) 다룰 내용들:

1. **예외 처리 (Exception Handling)**
   - try-except-finally 구문
   - 사용자 정의 예외
   - 예외 처리 모범 사례

2. **파일 입출력 (File I/O)**
   - 파일 읽기/쓰기
   - with 문 활용
   - 파일 경로 처리

3. **데코레이터 심화**
   - @ 문법 사용법
   - 데코레이터 체이닝
   - 매개변수가 있는 데코레이터

4. **클로저와 데코레이터 활용 퀴즈**
   - 실전 문제 풀이
   - 보안 관련 데코레이터 작성

### 학습 방법 조언

강사님께서 강조하신 학습 전략:

> "첫날 말씀드렸던 것처럼 **모방, 모방**... 어떤 문법을 가져다 이렇게 계속적으로 동일하게 그려보는 시간. 그런 **하드코딩**을 통해서 여러분 거에 어떤 정립된 내용들을 만드셔야 되는 것 같아요."

#### 학습 단계

1. **이해 (Understanding)**: 개념 이해
2. **모방 (Imitation)**: 예제 코드 직접 타이핑
3. **반복 (Repetition)**: 여러 번 반복 연습
4. **응용 (Application)**: 비슷한 문제에 적용
5. **창조 (Creation)**: 자신만의 코드 작성

#### 실습 권장사항

- **직접 타이핑**: 복사-붙여넣기보다는 직접 타이핑하면서 익히기
- **에러 경험**: 일부러 에러를 발생시켜보고 해결해보기
- **변형 연습**: 예제를 조금씩 변형해보면서 이해도 높이기
- **주석 작성**: 각 줄의 의미를 주석으로 작성하면서 정리

---

## 🎓 추가 학습 자료

### 권장 연습 문제

#### 연습 문제 1: 안전한 계산기 함수

```python
"""
다음 요구사항을 만족하는 안전한 계산기 함수를 작성하세요:

1. 사칙연산(+, -, *, /) 지원
2. 입력값 검증 (숫자인지 확인)
3. 0으로 나누기 예외 처리
4. 지원하지 않는 연산자 처리
"""

def safe_calculator(a, b, operator):
    # 여기에 코드 작성
    pass

# 테스트
print(safe_calculator(10, 5, '+'))   # 15
print(safe_calculator(10, 5, '-'))   # 5
print(safe_calculator(10, 5, '*'))   # 50
print(safe_calculator(10, 5, '/'))   # 2.0
print(safe_calculator(10, 0, '/'))   # 에러 처리
```

#### 연습 문제 2: 클로저를 이용한 비밀번호 관리

```python
"""
클로저를 사용하여 비밀번호를 안전하게 관리하는 함수를 작성하세요:

1. set_password(): 비밀번호 설정
2. verify_password(): 비밀번호 확인
3. 실제 비밀번호는 외부에서 접근 불가능해야 함
"""

def create_password_manager():
    # 여기에 코드 작성
    pass

# 테스트
manager = create_password_manager()
manager.set_password("secure123")
print(manager.verify_password("secure123"))  # True
print(manager.verify_password("wrong"))      # False
```

#### 연습 문제 3: 화이트리스트 기반 사용자 검증

```python
"""
다음 요구사항을 만족하는 사용자 검증 함수를 작성하세요:

1. 허용된 사용자만 접근 가능
2. 화이트리스트에 없는 사용자는 거부
3. 로그 기록 기능 (데코레이터 활용)
"""

ALLOWED_USERS = {'admin', 'user1', 'user2'}

def validate_user(username):
    # 여기에 코드 작성
    pass

# 테스트
validate_user('admin')      # 접근 허용
validate_user('hacker')     # 접근 거부
```

### 참고 링크

- **Python 공식 문서**: https://docs.python.org/3/
- **urllib.parse 모듈**: https://docs.python.org/3/library/urllib.parse.html
- **PEP 8 스타일 가이드**: https://pep8.org/

---

## 📝 복습 체크리스트

학습한 내용을 제대로 이해했는지 확인해보세요:

### 기본 개념

- [ ] 모듈, 패키지, 함수의 관계를 설명할 수 있다
- [ ] 함수의 4가지 유형을 설명하고 각각의 사용 시나리오를 알고 있다
- [ ] 위치 인자와 키워드 인자의 차이를 설명할 수 있다
- [ ] 기본 매개변수(default parameter)를 사용할 수 있다

### 람다와 고차 함수

- [ ] 람다 함수의 구조와 제약사항을 이해한다
- [ ] map 함수와 람다를 함께 사용할 수 있다
- [ ] filter 함수로 조건에 맞는 요소를 필터링할 수 있다
- [ ] sorted 함수의 key 매개변수에 람다를 활용할 수 있다

### 변수 스코프

- [ ] LEGB 규칙을 설명할 수 있다
- [ ] global과 nonlocal 키워드의 차이를 이해한다
- [ ] 변수 스코프에 따른 접근 가능 범위를 파악할 수 있다

### 클로저

- [ ] 클로저의 개념과 동작 원리를 설명할 수 있다
- [ ] 클로저를 사용하여 상태를 유지할 수 있다
- [ ] 클로저가 전역 변수보다 안전한 이유를 설명할 수 있다

### 가변인자

- [ ] *args의 동작 방식을 이해한다 (튜플)
- [ ] **kwargs의 동작 방식을 이해한다 (딕셔너리)
- [ ] 일반 매개변수, *args, **kwargs를 함께 사용할 수 있다

### 보안

- [ ] URL 인코딩의 필요성과 방법을 이해한다
- [ ] 화이트리스트 방식의 장점을 설명할 수 있다
- [ ] 입력값 검증의 중요성을 이해하고 구현할 수 있다
- [ ] XSS 공격의 위험성과 방어 방법을 알고 있다

---

## 🙏 마무리

오늘 강의에서는 파이썬의 **함수**에 대해 깊이 있게 학습했습니다. 단순히 함수를 만들고 사용하는 것을 넘어서, **보안 관점에서 안전한 코드를 작성하는 방법**과 **클로저, 데코레이터와 같은 고급 기법**까지 다루었습니다.

특히 강사님께서 강조하신 것처럼, **전역 변수 대신 클로저를 활용한 상태 관리**와 **화이트리스트 기반의 입력값 검증**은 실무에서 매우 중요한 보안 패턴입니다.

### 오늘 배운 핵심

1. ✅ **함수의 필요성**: 재사용성, 가독성, 유지보수성 향상
2. ✅ **변수 스코프**: LEGB 규칙 이해
3. ✅ **클로저**: 전역 변수 없이 안전하게 상태 유지
4. ✅ **가변인자**: 유연한 함수 설계
5. ✅ **보안 코딩**: 입력 검증, URL 인코딩, 화이트리스트

내일은 **예외 처리, 파일 입출력, 데코레이터 심화**를 학습할 예정입니다. 오늘 배운 클로저 개념이 데코레이터를 이해하는 데 핵심이 되므로, 오늘 내용을 꼭 복습하고 넘어가시기 바랍니다!

**강사님 말씀**: "여러분과 함께하고 있는 이 시간이 저에게는 선물이죠." 🎂

수고하셨습니다! 내일 더 발전된 모습으로 만나요! 💪

---

**작성일**: 2025년 10월 30일  
**강의**: Secure Python Day 04  
**주제**: 함수(Function), 클로저(Closure), 가변인자, 보안 코딩  
**문서 버전**: 1.0
