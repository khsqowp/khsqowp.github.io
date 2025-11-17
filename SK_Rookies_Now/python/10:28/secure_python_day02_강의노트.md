
# 📝 파이썬 강의 노트 (2일차): 객체와 변수, 그리고 자료구조 심화

오늘 2일차 파이썬 강의에서는 어제에 이어 파이썬의 핵심 자료구조를 더 깊이 있게 다루었다. 특히 파이썬이 모든 것을 **객체(Object)**로 다룬다는 사실과, 이로 인해 파생되는 **참조(Reference)**, **가변성(Mutability)**, 그리고 **복사(Copy)**의 개념이 매우 중요하다고 강사님께서 강조하셨다. 단순 코딩을 넘어, 메모리 동작 방식을 이해하고 보안적으로 안전한 코드를 작성하는 법에 대한 인사이트를 얻을 수 있는 시간이었다.

### 🎯 오늘의 학습 목표

- 파이썬의 **객체 지향** 개념과 `클래스`, `인스턴스`, `메서드`의 의미 이해하기
- 변수의 **참조 타입** 특성과 `얕은 복사(Shallow Copy)` vs `깊은 복사(Deep Copy)`의 차이점 학습
- **가변(Mutable)** 객체와 **불변(Immutable)** 객체의 동작 방식 및 보안적 중요성 파악하기
- `리스트(List)`와 `딕셔너리(Dictionary)`의 심화 활용법 및 `List Comprehension` 익히기

---

### 🏛️ 1. 파이썬의 모든 것은 '객체'다

#### 1-1. 왜 '객체'를 이해해야 하는가?

다른 프로그래밍 언어(C, Java 등)는 정수, 문자와 같은 데이터를 직접 담는 **기본 타입(Primitive Type)**과, 데이터가 저장된 메모리 주소를 담는 **참조 타입(Reference Type)**을 구분한다. 하지만 파이썬은 이 모든 것을 **참조 타입**, 즉 **객체**로 다룬다. 이 특징 때문에 변수를 다룰 때 우리가 예상치 못한 동작이 발생할 수 있으며, 특히 보안 관점에서 데이터가 의도치 않게 변경되거나 노출될 위험이 있어 정확한 이해가 필수적이다.

#### 1-2. 클래스, 객체, 인스턴스

> **💡 중요!:** 객체 지향 프로그래밍(OOP)은 우리가 사는 현실 세계를 모델링하는 방식이다.

- **객체(Object)**: 현실 세계에 존재하는 모든 것(유형, 무형)을 의미한다. 예를 들어, '나'라는 사람, '자동차', '수강 신청' 등이 모두 객체다.
- **클래스(Class)**: 현실의 객체를 프로그램 속에서 표현하기 위한 **'설계도' 또는 '템플릿'**이다. 객체의 특징(속성)과 행동(기능)을 정의한다.
  - **속성(Attribute)**: 객체의 명사적 특징. `변수`로 표현된다. (예: 사람의 `이름`, `나이`, `직업`)
  - **메서드(Method)**: 객체의 동사적 특징. `함수`로 표현된다. (예: 사람이 `걷는다()`, `말한다()`)
- **인스턴스(Instance)**: 클래스라는 설계도를 바탕으로 메모리에 **실제로 생성된 객체**를 의미한다. `붕어빵 틀(클래스)`로 찍어낸 `붕어빵(인스턴스)`에 비유할 수 있다.

파이썬에서 `a = 10`이라고 코드를 작성하면, `int`라는 클래스(설계도)를 바탕으로 `10`이라는 값을 가진 인스턴스가 메모리에 생성되고, 변수 `a`는 그 인스턴스의 **메모리 주소**를 가리키게(참조하게) 된다.

#### 1-3. 함수(Function) vs 메서드(Method)

- **함수**: `print()`, `len()`처럼 단독으로 호출할 수 있다. 파이썬에 기본 내장된 기능이다.
- **메서드**: 특정 인스턴스에 속한 기능으로, `인스턴스.메서드()` 형태로만 호출할 수 있다. (예: `my_list.append()`).

```python
# url은 str 클래스의 '인스턴스'이다.
url = 'http://www.naver.com'

# type()은 단독으로 쓰이는 내장 '함수'이다.
print('type - ', type(url))

# find()는 str 인스턴스에 속한 '메서드'이다.
# url.find(...) 형태로만 사용할 수 있다.
print('find - ', url.find('com'))
```

> **📌 노트:** 특정 인스턴스가 어떤 메서드를 가지고 있는지 확인하고 싶을 땐 `dir(인스턴스)` 함수를 사용하면 리스트 형태로 모든 속성과 메서드를 볼 수 있다.

---

### 🔡 2. 문자열(String) 타입 응용

문자열은 `str` 클래스의 인스턴스이므로, 다양한 내장 메서드를 활용해 손쉽게 데이터를 가공할 수 있다.

#### 2-1. 문자열 자르기 및 검색

```python
url = 'http://www.naver.com'

# 슬라이싱을 이용한 고전적인 방법
print('.com 추출 (슬라이싱): ', url[-4:])

# find() 메서드로 특정 문자열의 시작 인덱스를 찾고, 이를 슬라이싱에 활용
# 'com'의 시작 인덱스를 찾아 그 위치부터 끝까지 자른다.
com_index = url.find('com')
print('.com 추출 (find + 슬라이싱): ', url[com_index:])
```

#### 2-2. 공백 제거 및 대소문자 변경

```python
# 좌우에 불필요한 공백이 있는 문자열
company_name_padded = '     SK      '
print(f"원본: '{company_name_padded}', 길이: {len(company_name_padded)}")

# strip(): 좌우 모든 공백을 제거
stripped_name = company_name_padded.strip()
print(f"strip() 후: '{stripped_name}', 길이: {len(stripped_name)}")

# lstrip(): 왼쪽 공백만 제거
# rstrip(): 오른쪽 공백만 제거

# 대소문자 변경
company_name = 'samsung'

# capitalize(): 문자열의 '첫 글자'만 대문자로 변경
print(f"capitalize(): {company_name.capitalize()}")

# upper(): 모든 글자를 대문자로 변경
print(f"upper(): {company_name.upper()}")
```

#### 2-3. 특정 문자열로 끝나는지 확인하기

##### 퀴즈: 파일 확장자가 엑셀 파일(`.xlsx`)인지 확인하고 싶다면?

`endswith()` 메서드를 사용하면 특정 문자열로 끝나는지 여부를 `True`/`False`로 쉽게 확인할 수 있다.

```python
file_name1 = 'report.xlsx'
file_name2 = 'document.docx'

print(f"'{file_name1}'은(는) xlsx 파일인가? {file_name1.endswith('.xlsx')}")
print(f"'{file_name2}'은(는) xlsx 파일인가? {file_name2.endswith('.xlsx')}")
```

> #### 🔐 보안 노트: 파일 확장자 검증
> `endswith()`는 파일 확장자를 검증할 때 매우 유용하다. 예를 들어, 사용자가 업로드한 파일이 허용된 이미지 파일(`.jpg`, `.png`)인지 확인할 때 사용할 수 있다. 이를 통해 악성 스크립트 파일(`.php`, `.jsp`) 등의 업로드를 차단하는 1차적인 방어선으로 활용할 수 있다.

---

### 🧬 3. 얕은 복사(Shallow Copy) vs 깊은 복사(Deep Copy)

#### 3-1. 왜 복사를 이해해야 하는가?

파이썬의 모든 변수는 객체의 **주소값**을 저장하는 참조 변수이기 때문에, 변수를 복사할 때 얘기치 않은 문제가 발생할 수 있다. 원본을 바꾸지 않으려 했는데 복사본을 수정했더니 원본까지 바뀌는 현상이 대표적이다.

- **`id()` 함수**: 객체의 고유한 메모리 주소값을 반환한다. 두 변수의 `id()` 값이 같다면, 두 변수는 정확히 동일한 객체를 가리키고 있는 것이다.

```python
lst_a = [1, 2, 3]
lst_b = [1, 2, 3]

# 값은 같지만, 서로 다른 객체이므로 메모리 주소가 다르다.
print(f"lst_a와 lst_b의 주소는 같은가? {lst_a is lst_b}") # False
print(f"id(lst_a): {id(lst_a)}, id(lst_b): {id(lst_b)}") 
```

#### 3-2. 얕은 복사 (Shallow Copy)

- **정의**: 변수를 단순히 할당(`b = a`)하거나 `copy()` 모듈을 사용하면 얕은 복사가 일어난다.
- **동작**: 객체 자체는 새로 만들지만, 그 **내부의 요소들은 원본 객체가 가리키는 주소를 그대로 복사**한다.
- **문제점**: 복사된 객체 내부의 요소가 **가변(Mutable) 객체**일 경우(예: 리스트), 복사본의 요소를 수정하면 원본의 요소도 함께 변경된다.

```python
from copy import copy

# 중첩된 리스트 (내부 리스트는 가변 객체)
original = [[1, 2], [3, 4]]
shallow_copy = copy(original)

print(f"복사 전 original: {original}")

# 복사본의 내부 리스트 요소를 수정
shallow_copy[0][0] = 99

# 원본까지 함께 변경되어 버린다!
print(f"복사본 수정 후 original: {original}")
print(f"복사본 수정 후 shallow_copy: {shallow_copy}")
```

#### 3-3. 깊은 복사 (Deep Copy)

- **정의**: `deepcopy()` 모듈을 사용한다.
- **동작**: 객체 내부에 있는 모든 요소를 **재귀적으로 복사**하여, 완전히 독립된 새로운 객체를 만든다.
- **장점**: 원본과 복사본이 서로에게 전혀 영향을 주지 않는다.

```python
from copy import deepcopy

original = [[1, 2], [3, 4]]
deep_copy = deepcopy(original)

print(f"복사 전 original: {original}")

# 복사본의 내부 요소를 수정
deep_copy[0][0] = 99

# 원본은 전혀 영향을 받지 않는다.
print(f"복사본 수정 후 original: {original}")
print(f"복사본 수정 후 deep_copy: {deep_copy}")
```

> #### 🔐 보안 노트: 민감 데이터는 반드시 깊은 복사를 사용하라!
>
> 강사님께서는 보안 관점에서 얕은 복사의 위험성을 특히 강조하셨다.
> - **위협**: 사용자의 세션 정보, 인증 토큰, 권한 목록과 같은 민감한 데이터를 다룰 때 얕은 복사를 사용하면, 한 곳에서의 수정이 다른 곳에 예기치 않은 영향을 미쳐 **데이터 오염**이나 **권한 상승**과 같은 심각한 보안 문제로 이어질 수 있다.
> - **대응**: 민감 데이터를 복사하여 임시로 사용하거나 로그로 남겨야 할 경우, 반드시 `deepcopy`를 사용하여 원본 데이터와의 연결을 완전히 끊고 독립적인 복사본을 만들어야 한다.

---

### 🧱 4. 가변(Mutable) vs 불변(Immutable) 객체

복사 시 동작이 달라지는 근본적인 이유는 바로 객체의 **가변성** 때문이다.

- **불변(Immutable) 객체**: 값을 변경할 수 없는 객체. 변경을 시도하면 새로운 객체가 생성되고 변수는 그 새 객체를 가리킨다.
  - 종류: `int`, `float`, `str`, `tuple`, `bool`
- **가변(Mutable) 객체**: 값을 제자리에서(in-place) 변경할 수 있는 객체.
  - 종류: `list`, `dict`, `set`

##### 개념 증명 코드

```python
from copy import copy

# 1. 내부 요소가 '불변' 객체(str)인 경우
user_data_immutable = {'id': 1, 'token': 'secret1234'}
cache_immutable = copy(user_data_immutable) # 얕은 복사

# cache의 token 값을 변경 -> str은 불변이므로 '새로운' 문자열 객체가 생성됨
cache_immutable['token'] = 'new_secret'

# 원본은 영향을 받지 않는다.
print(f"[불변] 원본: {user_data_immutable['token']}")
print(f"[불변] 사본: {cache_immutable['token']}")

print('---')

# 2. 내부 요소가 '가변' 객체(list)인 경우
user_data_mutable = {'id': 1, 'roles': ['admin', 'user']}
cache_mutable = copy(user_data_mutable) # 얕은 복사

# cache의 roles 리스트에 값을 추가 -> list는 가변이므로 '기존' 객체가 수정됨
cache_mutable['roles'].append('guest')

# 얕은 복사였기 때문에 원본도 함께 변경된다!
print(f"[가변] 원본: {user_data_mutable['roles']}")
print(f"[가변] 사본: {cache_mutable['roles']}")
```

---

### 🗂️ 5. 자료구조 심화

#### 5-1. 열거형과 `range()`

- **열거형(Iterable)**: `for`문을 통해 요소를 하나씩 꺼낼 수 있는 객체. (`list`, `tuple`, `str`, `dict`, `set` 등)
- **`range()`**: 연속된 숫자 시퀀스를 생성하는 열거형 객체.
  - `range(end)`: 0부터 `end-1`까지
  - `range(start, end)`: `start`부터 `end-1`까지
  - `range(start, end, step)`: `start`부터 `step` 간격으로 `end-1`까지

```python
# 1부터 10까지 2씩 증가하는 숫자 순회
for i in range(1, 11, 2):
    print(i, end=' ') # 1 3 5 7 9
```

#### 5-2. 리스트 컴프리헨션 (List Comprehension)

> **📌 노트:** 강사님께서는 리스트 컴프리헨션이 코드를 간결하게 만들 뿐만 아니라, 일반 `for` 루프보다 성능 면에서도 이점이 있다고 강조하셨다.

- **기본 문법**: `[표현식 for 항목 in 열거형]`
- **조건부 문법**: `[표현식 for 항목 in 열거형 if 조건식]`

```python
# 1부터 100까지의 숫자 중 3의 배수만 담은 리스트 만들기

# 일반 for문 방식
multiples_of_3 = []
for i in range(1, 101):
    if i % 3 == 0:
        multiples_of_3.append(i)

# 리스트 컴프리헨션 방식 (훨씬 간결하다)
hund_lst = [i for i in range(1, 101) if i % 3 == 0]

print(hund_lst)
```

#### 5-3. 딕셔너리(`dict`) 심화

- **키(Key) 유무 확인**: `'my_key' in my_dict`
- **값(Value) 접근**: `my_dict['my_key']` (키가 없으면 `KeyError` 발생) 또는 `my_dict.get('my_key')` (키가 없으면 `None` 반환, 더 안전함)
- **순회 방법**:
  - `for key in my_dict.keys()`: 키 순회
  - `for value in my_dict.values()`: 값 순회
  - `for key, value in my_dict.items()`: 키와 값을 튜플로 묶어 순회 (가장 많이 사용됨)

##### 퀴즈: 단어 빈도수 계산기 (재도전)

어제 풀었던 단어 빈도수 계산 문제를 `for`문과 `if`문을 사용해 정석적으로 풀어보았다.

```python
word_lst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk']
word_dict = {}

for word in word_lst:
    if word in word_dict: # 이미 딕셔너리에 단어가 있으면
        word_dict[word] += 1 # 카운트 1 증가
    else: # 처음 나오는 단어이면
        word_dict[word] = 1 # 1로 초기화

print(word_dict)
```

> #### 🔐 보안 노트: 안전한 딕셔너리 업데이트 함수 만들기
>
> 아래 함수는 사용자의 역할을 변경하는 함수다. 하지만 입력값(`new_role`)에 대한 검증이 없어, 아무 역할이나 주입할 수 있는 **정보 변조(Data Tampering)** 취약점이 있다.
>
> ```python
> # 취약한 함수
> def update_role_unsafe(user_data, new_role):
>     user_data["role"] = new_role # 입력값을 검증 없이 바로 할당
> ```
>
> 이를 개선하기 위해, 허용된 역할 목록(**화이트리스트**)을 만들어 입력값을 검증하고, 원본 데이터를 보호하기 위해 **깊은 복사**를 사용하는 것이 안전하다.
>
> ```python
> from copy import deepcopy
>
> user = {
>     "id": 100,
>     "name": "admin",
>     "role": "superuser"
> }
>
> # 허용된 역할만 담은 화이트리스트 (set 자료형 사용)
> allowed_roles = {"user", "guest", "manager"}
>
> def update_role_safe(data, new_role):
>     # 원본 데이터를 보호하기 위해 깊은 복사본 생성
>     copy_user = deepcopy(data)
>     
>     # 입력된 역할이 화이트리스트에 있는지 검증
>     if new_role in allowed_roles:
>         copy_user["role"] = new_role
>         print(f"역할이 '{new_role}'(으)로 안전하게 변경되었습니다.")
>         return copy_user
>     else:
>         print(f"'{new_role}'은(는) 허용되지 않는 역할입니다.")
>         return data # 변경 실패 시 원본 데이터 반환
>
> # 안전한 함수 호출
> changed_user = update_role_safe(user, "guest")
> print(f"원본 데이터: {user}")
> print(f"변경 후 데이터: {changed_user}")
> 
> # 허용되지 않은 역할로 변경 시도
> failed_user = update_role_safe(user, "hacker")
> print(f"원본 데이터: {user}")
> print(f"변경 시도 후 데이터: {failed_user}")
> ```


