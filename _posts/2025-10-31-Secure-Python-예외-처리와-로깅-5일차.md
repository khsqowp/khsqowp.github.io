---
title: "Secure Python: 예외 처리와 로깅 (5일차)"
date: 2025-10-31
categories:
  - 01_python
tags:
  - 01_python
  - SK_Rookies
---

# 📝 Secure Python 강의 노트 - Day 5 (2025년 10월 31일)

---

## 📚 학습 목표

오늘 강의에서는 Python의 **예외 처리(Exception Handling)**, **로깅(Logging)**, **파일 입출력(File I/O)**, 그리고 **데코레이터를 활용한 보안 강화** 기법을 배웠습니다. 이번 강의는 실무에서 매우 중요한 내용들로 구성되어 있으며, 특히 안전한 애플리케이션 개발을 위한 핵심 기술들을 다루었습니다.

### 주요 학습 내용
1. **예외 처리의 개념과 구조**
2. **사용자 입력 검증과 예외 발생**
3. **로깅 시스템의 이해와 활용**
4. **파일 입출력 (텍스트, JSON)**
5. **데코레이터를 활용한 보안 로깅**
6. **실전 프로젝트: 사용자 정보 마스킹 시스템**

---

## 📖 1. 예외 처리 (Exception Handling)

### 1.1 예외(Exception)와 에러(Error)의 차이

오늘 강의에서 강사님께서 예외와 에러의 차이에 대해 명확히 설명해주셨습니다.

- **에러(Error)**: 휴먼 에러, 문법 에러(Syntax Error) 등 프로그램이 실행조차 되지 않는 심각한 문제
- **예외(Exception)**: 에러보다는 마일드한 상황으로, 프로그램 실행 중 발생하는 의도하지 않은 상황

> 💡 **중요!**: 예외도 에러의 일종이지만, 예외 처리를 통해 시스템을 플랫(flat)시키거나 셧다운(shutdown)시키지 않고 정상적인 흐름으로 시스템을 종료시킬 수 있습니다. 이를 "웜 셧다운(warm shutdown)"이라고 합니다.

### 1.2 예외 처리의 필요성

강사님께서 강조하신 예외 처리의 핵심 목적:
- **시스템의 비정상적인 종료 방지**
- **예외 상황을 알리고 대처할 수 있도록 함**
- **정상적인 흐름으로 시스템 종료 유도**
- **외부 리소스 정리 (DB 연결, 파일 핸들 등)**
- **예외 형식을 로그로 남겨 추후 분석 가능**

### 1.3 예외 처리 구조

Python의 예외 처리는 `try-except-else-finally` 구조를 사용합니다.

```python
try:
    # 예외가 발생할 수 있는 코드
    예외발생 가능 코드
except:
    # try 블록에서 발생된 예외를 처리하는 영역
    예외 처리 로직
else:
    # 예외가 발생하지 않았을 때 수행하는 영역
    정상 실행 로직
finally:
    # 예외 발생 여부와 상관없이 항상 수행하는 영역
    정리 작업 (리소스 해제 등)
```

> 📌 **노트**: Python의 예외는 `xxxxError`라는 서픽스(suffix)로 끝나는 이름을 가지고 있습니다. 예를 들어 `IndexError`, `ValueError`, `TypeError` 등이 있습니다.

### 1.4 기본 예외 처리 예제

#### 예제 1: 예외 처리 전 (시스템 비정상 종료)

```python
lst = [1, 2, 3]

for idx in range(len(lst) + 1):
    print(lst[idx])
print('정상종료')
```

#### 💻 코드 실행 상세 분석

**1단계 (리스트 초기화)**: `lst` 변수에 `[1, 2, 3]`이 할당됩니다.

**2단계 (반복문 실행)**: `range(len(lst) + 1)`은 `range(4)`가 되어 0, 1, 2, 3의 인덱스로 반복합니다.

**3단계 (정상 출력)**: 인덱스 0, 1, 2까지는 정상적으로 `1`, `2`, `3`이 출력됩니다.

**4단계 (예외 발생)**: 인덱스 3에 접근하려고 할 때 리스트의 범위를 벗어나 `IndexError: list index out of range` 예외가 발생합니다.

**최종 결과**: 프로그램이 비정상 종료되어 `'정상종료'` 메시지가 출력되지 않습니다.

```
실행 결과:
1
2
3
Traceback (most recent call last):
  File "...", line 81, in <module>
    print(lst[idx])
IndexError: list index out of range
```

> 🔐 **보안 노트**: 이렇게 프로그램이 갑자기 종료되면 외부 리소스(데이터베이스 연결, 파일 핸들 등)가 제대로 정리되지 않아 리소스 누수(resource leak)가 발생할 수 있습니다. 또한 중요한 로그가 기록되지 않아 문제 추적이 어려워질 수 있습니다.

#### 예제 2: 예외 처리 후 (정상 종료)

```python
lst = [1, 2, 3]
try:
    for idx in range(len(lst) + 1):
        print(lst[idx])
except IndexError as e:
    print(f'{e} 예외 발생 함')
else:
    print('예외가 발생하지 않았을 때 수행하는 블럭')
finally:
    print('예외발생 여부와 상관없이 수행하는 블럭')
print('>>>> 정상종료')
```

#### 💻 코드 실행 상세 분석

**1단계 (try 블록 진입)**: 리스트를 순회하며 요소를 출력하기 시작합니다.

**2단계 (정상 실행)**: 인덱스 0, 1, 2는 정상적으로 처리되어 `1`, `2`, `3`이 출력됩니다.

**3단계 (예외 발생 및 처리)**: 인덱스 3에서 `IndexError`가 발생하지만, `except` 블록이 이를 잡아서 `'list index out of range 예외 발생 함'` 메시지를 출력합니다.

**4단계 (else 블록 생략)**: 예외가 발생했으므로 `else` 블록은 실행되지 않습니다.

**5단계 (finally 블록 실행)**: 예외 발생 여부와 관계없이 `finally` 블록이 실행되어 `'예외발생 여부와 상관없이 수행하는 블럭'`이 출력됩니다.

**최종 결과**: 프로그램이 정상적으로 종료되며 `'>>>> 정상종료'` 메시지가 출력됩니다.

```
실행 결과:
1
2
3
list index out of range 예외 발생 함
예외발생 여부와 상관없이 수행하는 블럭
>>>> 정상종료
```

> 💡 **중요!**: `except` 블록에서 `as e`를 사용하면 예외 객체를 변수에 담아서 예외의 상세 정보를 확인할 수 있습니다. 이는 디버깅과 로깅에 매우 유용합니다.

### 1.5 다중 예외 처리

여러 종류의 예외를 각각 다르게 처리해야 할 경우, 다중 `except` 블록을 사용할 수 있습니다.

```python
lst = [1, 2, 3]
try:
    for idx in range(len(lst) + 1):
        print(lst[idx])
except IndexError as e:
    print(f'{e} 예외발생')
except Exception as e:
    print(f'{e} 예외발생 Exception')
else:
    print('예외가 발생하지 않았을 때 수행하는 블록')
finally:
    print('예외 발생 여부와 상관없이 수행하는 블록')
print('>>>>> 정상종료')
```

> 📌 **노트**: 강사님께서 강조하신 것처럼, 보안 관점에서는 다중 `except`를 사용하는 것이 좋습니다. 각 예외 타입별로 적절한 로깅과 처리를 할 수 있기 때문입니다. `Exception`으로 모든 예외를 통합 처리하는 것은 편하지만, 보안과 로깅 관점에서는 권장되지 않습니다.

### 1.6 실전 예제: 사용자 정보 입력 검증

강의에서 다룬 실전 예제는 사용자로부터 이름, 나이, 이메일을 입력받아 검증하는 함수입니다.

```python
def getUserInfo():
    ''' 사용자의 정보를 입력받고, 형식 오류나 유효성을 처리하는 기능'''
    try:
        name = input('이름을 입력하세요 : ').strip()
        if not name.isalpha():
            raise ValueError('이름은 문자만 포함해야 합니다!!')
        
        age = input('나이를 입력하세요 : ').strip()
        if not age.isdigit():
            raise ValueError('나이는 숫자만 입력하세요!!')
        age = int(age)
        if age < 0 or age > 120:
            raise ValueError('1 ~ 120 사이의 숫자만 입력하세요!!')
            
        email = input('이메일 주소를 입력하세요 : ').strip()
        if '@' not in email or '.' not in email:
            raise ValueError('올바른 이메일 형식이 아닙니다!!')
        
    except Exception as ve:
        print(f'입력 오류 {ve}')
    else:
        return {
            "name": name,
            "age": age,
            "email": email
        }
    finally:
        print('입력정보를 정상적으로 처리 하였습니다!!')
```

#### 💻 코드 실행 상세 분석

**1단계 (이름 입력 및 검증)**:
- `input()` 함수로 사용자로부터 이름을 입력받습니다.
- `.strip()` 메서드로 좌우 공백을 제거합니다.
- `isalpha()` 메서드로 문자만 포함되어 있는지 확인합니다.
- 문자가 아닌 경우 `raise ValueError`로 예외를 명시적으로 발생시킵니다.

**2단계 (나이 입력 및 검증)**:
- 나이를 문자열로 입력받아 `isdigit()`으로 숫자인지 확인합니다.
- 숫자가 맞다면 `int(age)`로 정수로 캐스팅합니다.
- 나이가 0보다 작거나 120보다 크면 예외를 발생시킵니다.

**3단계 (이메일 입력 및 검증)**:
- 이메일 주소를 입력받아 `@`와 `.`이 모두 포함되어 있는지 확인합니다.
- 조건을 만족하지 않으면 예외를 발생시킵니다.

**4단계 (예외 처리)**:
- 모든 `ValueError`는 `except Exception as ve` 블록에서 잡힙니다.
- 예외 메시지를 사용자에게 보여줍니다.

**5단계 (정상 실행 시)**:
- `else` 블록에서 딕셔너리 형태로 사용자 정보를 반환합니다.

**6단계 (finally 블록)**:
- 예외 발생 여부와 관계없이 처리 완료 메시지를 출력합니다.

**최종 결과**: 입력이 유효하면 사용자 정보 딕셔너리를 반환하고, 유효하지 않으면 `None`을 반환합니다.

```python
result = getUserInfo()
print(result)
```

실행 예시:
```
이름을 입력하세요 : 123
입력 오류 이름은 문자만 포함해야 합니다!!
입력정보를 정상적으로 처리 하였습니다!!
None
```

> 🔐 **보안 노트**: 
> - `strip()` 메서드를 사용하여 좌우 공백을 제거하는 것은 **공백을 이용한 우회 공격**을 방지합니다.
> - `isalpha()`, `isdigit()` 같은 검증 메서드는 **타입 안정성(type safety)**을 확보합니다.
> - `raise ValueError`로 명시적으로 예외를 발생시키는 것은 **입력 검증(input validation)**의 핵심입니다.
> - 실제 프로덕션 환경에서는 정규표현식(Regular Expression)을 사용하여 더 정교한 검증을 수행해야 합니다.

### 1.7 raise를 활용한 예외 발생

강사님께서 강조하신 것처럼, `raise` 키워드를 사용하면 개발자가 의도적으로 예외를 발생시킬 수 있습니다.

```python
if not name.isalpha():
    raise ValueError('이름은 문자만 포함해야 합니다!!')
```

> 💡 **중요!**: `raise`를 사용하는 이유는 **개발 시점에 안정성을 미리 확보**하기 위함입니다. 잠재적인 문제를 사전에 차단하여 예외 처리 블록으로 넘김으로써 시스템의 안정성을 높일 수 있습니다.

### 1.8 예외 처리와 반환 값

강의에서 배운 중요한 포인트는 예외가 발생하면 함수가 `None`을 반환한다는 점입니다.

```python
result = getUserInfo()
print(result)  # 예외 발생 시 None 출력
```

> 📌 **노트**: `else` 블록에서 `return`을 수행하는 것이 효율적일 수 있습니다. 예외가 발생하지 않았을 때만 값을 반환하도록 명확히 구분할 수 있기 때문입니다.

### 1.9 finally 블록의 중요성

강사님께서 설명하신 `finally` 블록의 주요 용도:

1. **외부 리소스와의 연결 정리**: 데이터베이스 연결, 파일 핸들, 네트워크 소켓 등을 닫아야 할 때
2. **예외 형식을 로그로 남기기**: 시스템 분석을 위한 로그 기록
3. **웜 셧다운(warm shutdown)**: 시스템이 플랫되더라도 정리 작업을 수행

```python
finally:
    print('예외 발생 여부와 상관없이 수행하는 블록')
    # 데이터베이스 연결 종료
    # 파일 핸들 닫기
    # 로그 기록
```

---

## 🔍 2. 로깅 (Logging)

### 2.1 로깅의 필요성

강사님께서 강조하신 것처럼, 서버 환경에서는 `print()` 함수 대신 **로깅(logging)**을 사용하는 것이 안전합니다.

- **print()의 문제점**:
  - 콘솔에만 출력되어 영구적으로 기록되지 않음
  - 로그 레벨 구분 불가
  - 프로덕션 환경에서 디버깅 어려움
  - 보안 측면에서 민감한 정보 노출 위험

- **logging의 장점**:
  - 파일로 영구 저장 가능
  - 로그 레벨별 분류 가능
  - 일반화된 메시지 제공으로 보안 강화
  - 시간 정보 자동 기록
  - 포맷 커스터마이징 가능

> 💡 **중요!**: 강사님께서 말씀하신 것처럼, "에러 메시지 노출을 `print()`로 해왔지만, 서버 환경에서는 `print()` 대신 로깅을 사용하여 일반화된 메시지 제공이 안전합니다."

### 2.2 로깅 레벨 (Logging Levels)

Python의 `logging` 모듈은 5가지 로그 레벨을 제공합니다:

1. **DEBUG** (디버그): 내부 정보 확인용도, 상세한 진단 정보
2. **INFO** (정보): 정보 전달, 동작에 관련된 일반적인 정보
3. **WARNING** (경고): 잠재적인 문제, 주의가 필요한 상황
4. **ERROR** (에러): 실행 중에 발생한 오류
5. **CRITICAL** (치명적): 치명적인 오류, 시스템 중단의 위험이 있는 상황

> 📌 **노트**: 로그 레벨 이름이 대문자로 표시되는 이유는 이들이 **상수(constant)**이기 때문입니다. Python의 관례상 상수는 전체를 대문자로 작성합니다.

### 2.3 기본 로깅 설정

`logging` 모듈을 사용하기 위해서는 먼저 기본 설정을 해야 합니다.

```python
import logging

logging.basicConfig(level=logging.WARNING)
```

#### 💻 코드 실행 상세 분석

**1단계 (모듈 임포트)**: `import logging`으로 로깅 모듈을 불러옵니다.

**2단계 (기본 설정)**: `basicConfig()` 함수로 로깅의 기본 동작을 설정합니다.

**3단계 (레벨 설정)**: `level=logging.WARNING`으로 WARNING 레벨 이상의 로그만 출력하도록 설정합니다. 즉, DEBUG와 INFO는 출력되지 않습니다.

**최종 결과**: WARNING, ERROR, CRITICAL 레벨의 로그만 출력됩니다.

### 2.4 로깅 기본 사용 예제

```python
import logging

logging.basicConfig(level=logging.WARNING)

data = 'jslim'
try:
    print(data ** 2)
except TypeError as t:
    logging.warning(f'숫자가 아닌 값을 발견 : {data}')
```

#### 💻 코드 실행 상세 분석

**1단계 (변수 초기화)**: `data` 변수에 문자열 `'jslim'`이 할당됩니다.

**2단계 (try 블록)**: 문자열에 거듭제곱 연산(`** 2`)을 시도합니다.

**3단계 (예외 발생)**: 문자열은 거듭제곱 연산을 지원하지 않으므로 `TypeError`가 발생합니다.

**4단계 (예외 처리 및 로깅)**: `except` 블록에서 예외를 잡고, `logging.warning()`으로 경고 로그를 기록합니다.

**최종 결과**: 콘솔에 `WARNING:root:숫자가 아닌 값을 발견 : jslim` 메시지가 출력됩니다.

```
실행 결과:
WARNING:root:숫자가 아닌 값을 발견 : jslim
```

> 🔐 **보안 노트**: `print()`로 에러를 출력하는 대신 `logging.warning()`을 사용하면 로그 레벨별로 필터링할 수 있고, 파일로 저장하여 나중에 분석할 수 있습니다. 또한 일반화된 메시지를 제공하여 민감한 시스템 정보 노출을 방지할 수 있습니다.

### 2.5 로깅 포맷 커스터마이징

로깅 메시지의 형식을 커스터마이징할 수 있습니다.

```python
import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)
```

#### 주요 포맷 키워드

- `%(asctime)s`: 로그가 발생한 시각 (예: 2025-10-31 15:09:13,014)
- `%(levelname)s`: 로그 레벨 이름 (예: WARNING, ERROR)
- `%(name)s`: 로거 이름
- `%(message)s`: 로그 메시지 내용
- `%(filename)s`: 파일 이름
- `%(lineno)d`: 라인 번호
- `%(funcName)s`: 함수 이름

> 📌 **노트**: `force=True` 옵션은 이미 설정된 로깅 설정을 강제로 덮어쓰기 위해 사용합니다. Jupyter Notebook이나 대화형 환경에서 설정을 변경할 때 유용합니다.

### 2.6 파일로 로그 저장

로그를 파일로 저장하려면 `filename`과 `filemode` 옵션을 사용합니다.

```python
import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename='shieldus.log',
    filemode='a'  # 'a'는 append(추가), 'w'는 write(덮어쓰기)
)
```

#### 💻 코드 실행 상세 분석

**1단계 (파일 설정)**: `filename='shieldus.log'`로 로그를 저장할 파일 이름을 지정합니다.

**2단계 (파일 모드 설정)**: `filemode='a'`로 기존 로그에 추가하는 모드를 설정합니다. `'w'`를 사용하면 매번 파일이 새로 생성됩니다.

**3단계 (로그 기록)**: `logging.warning()`, `logging.error()` 등을 호출하면 콘솔이 아닌 파일에 로그가 기록됩니다.

**최종 결과**: `shieldus.log` 파일에 로그가 누적되어 저장됩니다.

> 💡 **중요!**: 프로덕션 환경에서는 로그를 파일로 저장하여 시스템 분석, 장애 추적, 보안 감사 등에 활용합니다. 로그 파일은 정기적으로 로테이션(rotation)하여 디스크 공간을 관리해야 합니다.

### 2.7 실전 예제: 리스트 거듭제곱 함수 (로깅 적용)

강의에서 다룬 실전 퀴즈는 예외 처리, 보안, 로깅을 모두 적용한 예제입니다.

```python
import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

def lstPrt(lst: list) -> list:
    '''매개변수로 전달받은 리스트 타입 요소의 값을 거듭제곱해서 반환'''
    
    # 보안 관점에서 입력 검증
    if not isinstance(lst, list):
        raise TypeError('매개변수 타입은 반드시 list 형태')
    
    result = []
    for idx, data in enumerate(lst):
        if not isinstance(data, (int, float)):
            logging.warning(
                f'인덱스 {idx} 번째에 숫자가 아닌 값 포함, 타입은: {type(data).__name__}'
            )
            continue
        try:
            result.append(data ** 2)
        except Exception as e:
            logging.error(f'예상치 못한 예외 발생: {e}')
    
    return result
```

#### 💻 코드 실행 상세 분석

**1단계 (타입 검증)**:
- `isinstance(lst, list)`로 매개변수가 리스트 타입인지 확인합니다.
- 리스트가 아니면 `TypeError`를 발생시켜 함수 실행을 중단합니다.

**2단계 (리스트 순회)**:
- `enumerate(lst)`를 사용하여 인덱스와 값을 동시에 얻습니다.
- 이는 로깅 시 어느 위치에서 문제가 발생했는지 명확히 알 수 있게 합니다.

**3단계 (요소 타입 검증)**:
- `isinstance(data, (int, float))`로 숫자 타입인지 확인합니다.
- 숫자가 아닌 경우 경고 로그를 기록하고 `continue`로 다음 요소로 넘어갑니다.
- `type(data).__name__`으로 실제 타입 이름을 로그에 포함시킵니다.

**4단계 (거듭제곱 연산)**:
- `try-except` 블록으로 예상치 못한 예외를 잡습니다.
- 정상적으로 실행되면 `data ** 2`의 결과를 `result` 리스트에 추가합니다.

**5단계 (예외 처리)**:
- 만약 거듭제곱 연산 중 예외가 발생하면 에러 로그를 기록합니다.

**최종 결과**: 숫자 요소만 거듭제곱하여 새로운 리스트를 반환합니다.

```python
tmp = [10, 20, 30, 40, 'seop', 50, 60]
result = lstPrt(tmp)
print(result)
```

실행 결과:
```
2025-10-31 15:09:13,014 - WARNING - 인덱스 4 번째에 숫자가 아닌 값 포함, 타입은: str
[100, 400, 900, 1600, 2500, 3600]
```

> 🔐 **보안 노트**:
> - **입력 검증(Input Validation)**: `isinstance()`로 타입을 검증하여 타입 안정성을 확보합니다.
> - **로깅(Logging)**: 문제가 발생한 위치와 타입 정보를 로그에 기록하여 추후 분석이 가능합니다.
> - **안전한 실패(Fail-Safe)**: 잘못된 요소를 만나도 프로그램이 중단되지 않고 다음 요소를 처리합니다.
> - **타입 힌팅(Type Hinting)**: 함수 시그니처에 `lst: list` 및 `-> list`를 명시하여 코드의 의도를 명확히 합니다.

### 2.8 로깅 프레임워크의 이해

강사님께서 말씀하신 것처럼, 로깅도 하나의 **프레임워크(framework)**로 볼 수 있습니다. 다양한 설정과 옵션을 통해 유연하게 로그를 관리할 수 있습니다.

```python
# 로깅 레벨은 고정되어 있음
# DEBUG < INFO < WARNING < ERROR < CRITICAL

# 현재 레벨이 WARNING이면:
# DEBUG, INFO는 출력 안 됨
# WARNING, ERROR, CRITICAL만 출력됨
```

---

## 📂 3. 파일 입출력 (File I/O)

### 3.1 파일 입출력의 기본 개념

강사님께서 설명하신 파일 입출력의 핵심 개념:

- **Stream(스트림)**: 데이터가 지나다니는 통로
- **콘솔(Console)** 또는 **파일(File)**에 출력 가능
- **통로를 열고(open), 닫아야(close) 함**
- **`with open` 구문을 사용하면 자동으로 닫힘**

> 💡 **중요!**: 일반적인 `open()` 구문은 명시적으로 `close()`를 호출해야 하지만, `with open` 구문은 블록을 벗어나면 자동으로 파일을 닫아줍니다. 따라서 **`with open`이 더 많이 사용됩니다**.

### 3.2 파일 모드 (File Modes)

Python의 `open()` 함수는 다양한 파일 모드를 지원합니다:

- **`'r'` (read)**: 읽기 전용 모드 (파일이 존재해야 함)
- **`'w'` (write)**: 쓰기 모드 (파일이 없으면 생성, 있으면 덮어쓰기)
- **`'a'` (append)**: 추가 모드 (기존 데이터 유지하면서 추가)
- **`'b'` (binary)**: 바이너리 모드 (거의 사용하지 않음)

```python
open(filePath, mode='r|w|a|b', encoding='utf-8')
```

> 📌 **노트**: 강사님께서 말씀하신 것처럼, Python의 파일 입출력 함수들은 대부분 **예외를 발생**시키므로 `try-except` 블록으로 감싸는 것이 좋습니다.

### 3.3 지원하는 파일 형식

현재 단계에서는 다음 파일 형식을 지원합니다:

- **텍스트 파일 (.txt)**
- **JSON 파일 (.json)**

> 📌 **노트**: CSV(.csv) 파일이나 Excel(.xls, .xlsx) 파일은 Pandas의 DataFrame을 사용해야 합니다. 이는 분석을 위한 데이터 타입이 필요하기 때문입니다. 다음 주에 Numpy와 Pandas를 배우면서 다룰 예정이라고 강사님께서 말씀하셨습니다.

### 3.4 텍스트 파일 읽기 (기본 방법)

```python
import logging

logging.basicConfig(
    level=logging.WARNING,
    format="[%(asctime)s] - %(levelname)s - %(message)s",
    force=True
)

filePath = './data/greeting.txt'.strip()
try:
    file = open(filePath, mode='r', encoding='utf-8')
except Exception:
    logging.error(f'파일을 열 수 없습니다.')

print('type - ', type(file))
print('dir - ', dir(file))
file.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (파일 경로 설정)**: `filePath` 변수에 파일 경로를 저장하고 `.strip()`으로 공백을 제거합니다.

**2단계 (파일 열기)**: `open()` 함수로 파일을 읽기 모드로 엽니다.
- `mode='r'`: 읽기 전용
- `encoding='utf-8'`: UTF-8 인코딩 사용 (한글 지원)

**3단계 (예외 처리)**: 파일이 없거나 접근 권한이 없으면 예외가 발생하므로 `try-except`로 감쌉니다.

**4단계 (파일 객체 확인)**:
- `type(file)`: 파일 객체의 타입 확인 (`<class 'TextIOWrapper'>`)
- `dir(file)`: 파일 객체가 가진 속성과 메서드 목록 확인

**5단계 (파일 닫기)**: `file.close()`로 파일을 명시적으로 닫습니다.

**최종 결과**: 파일 객체의 타입과 사용 가능한 메서드를 확인할 수 있습니다.

```
실행 결과:
type -  <class '_io.TextIOWrapper'>
dir -  ['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__exit__', ..., 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
```

### 3.5 텍스트 파일 읽기 (with 구문 사용)

`with` 구문을 사용하면 파일을 자동으로 닫아주므로 더 안전합니다.

#### 예제 1: read() 메서드

```python
filePath = './data/greeting.txt'.strip()
with open(filePath, mode='r', encoding='utf-8') as file:
    result = file.read()
    print(result, type(result))
```

#### 💻 코드 실행 상세 분석

**1단계 (with 블록 진입)**: `with open(...) as file:`로 파일을 열고 `file` 변수에 파일 객체를 할당합니다.

**2단계 (전체 읽기)**: `file.read()`는 파일의 전체 내용을 **하나의 문자열**로 반환합니다.

**3단계 (출력)**: 파일 내용과 타입을 출력합니다.

**4단계 (자동 닫기)**: `with` 블록을 벗어나면 파일이 자동으로 닫힙니다.

**최종 결과**: 파일의 전체 내용이 하나의 문자열로 출력됩니다.

```
실행 결과:
강사님과 함께하는 즐겁지 아니한 파이썬수업
그렇지만 열공하자
오늘은 즐거운 금요일
불금인데.......방콕이 답이다
 <class 'str'>
```

#### 예제 2: readlines() 메서드

```python
filePath = './data/greeting.txt'.strip()
with open(filePath, mode='r', encoding='utf-8') as file:
    lst = file.readlines()
    print(lst)
    for txt in lst:
        print(txt.strip('\n'))
```

#### 💻 코드 실행 상세 분석

**1단계 (readlines() 호출)**: `file.readlines()`는 파일의 각 줄을 **리스트의 요소**로 반환합니다.

**2단계 (리스트 출력)**: 각 요소의 끝에 개행 문자(`\n`)가 포함되어 있습니다.

**3단계 (반복문)**: `for` 문으로 리스트의 각 요소를 순회합니다.

**4단계 (개행 제거)**: `.strip('\n')`으로 개행 문자를 제거하여 깔끔하게 출력합니다.

**최종 결과**: 각 줄이 개행 없이 깔끔하게 출력됩니다.

```
실행 결과:
['강사님과 함께하는 즐겁지 아니한 파이썬수업\n', '그렇지만 열공하자\n', '오늘은 즐거운 금요일\n', '불금인데.......방콕이 답이다\n']
강사님과 함께하는 즐겁지 아니한 파이썬수업
그렇지만 열공하자
오늘은 즐거운 금요일
불금인데.......방콕이 답이다
```

> 💡 **중요!**: `read()`는 전체를 하나의 문자열로 반환하고, `readlines()`는 각 줄을 리스트의 요소로 반환합니다. 용도에 따라 적절한 메서드를 선택해야 합니다.

### 3.6 텍스트 파일 쓰기

```python
data = '안녕하세요~한 주 수고많으셨구요...즐거운 금요일 되시길 바랍니다.'
filePath = './data/message.txt'.strip()
with open(filePath, mode='w', encoding='utf-8') as file:
    file.write(data)
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 준비)**: 저장할 문자열을 `data` 변수에 할당합니다.

**2단계 (파일 열기)**: `mode='w'`로 쓰기 모드로 파일을 엽니다.
- 파일이 없으면 새로 생성
- 파일이 있으면 기존 내용을 모두 삭제하고 덮어쓰기

**3단계 (파일 쓰기)**: `file.write(data)`로 문자열을 파일에 씁니다.

**4단계 (자동 닫기 및 저장)**: `with` 블록을 벗어나면 파일이 자동으로 닫히며 내용이 저장됩니다.

**최종 결과**: `./data/message.txt` 파일에 문자열이 저장됩니다.

```python
# 파일 읽기로 확인
with open(filePath, mode='r', encoding='utf-8') as file:
    print(file.read())
```

```
실행 결과:
안녕하세요~한 주 수고많으셨구요...즐거운 금요일 되시길 바랍니다.
```

> 🔐 **보안 노트**:
> - 파일 쓰기는 **파일 시스템 접근 권한**을 필요로 합니다.
> - `mode='w'`는 기존 파일을 덮어쓰므로 **데이터 손실 위험**이 있습니다.
> - 민감한 데이터를 파일에 저장할 때는 **암호화**를 고려해야 합니다.
> - 파일 경로를 사용자 입력으로 받을 때는 **경로 조작(Path Traversal) 공격**을 방지해야 합니다.

### 3.7 JSON 파일 처리

강사님께서 강조하신 것처럼, 딕셔너리(dict) 타입은 문자열이 아니므로 파일에 직접 쓸 수 없습니다. 이때 **JSON 모듈**을 사용합니다.

#### 딕셔너리를 JSON 파일로 저장

```python
data = {'id': 'xxxxx', 'pwd': 'xxxx'}
print('type - ', type(data))

import json

filePath = './data/msg.json'.strip()
with open(filePath, mode='w', encoding='utf-8') as file:
    json.dump(data, file)
```

#### 💻 코드 실행 상세 분석

**1단계 (딕셔너리 생성)**: `data` 변수에 딕셔너리를 할당합니다.

**2단계 (타입 확인)**: `type(data)`는 `<class 'dict'>`를 반환합니다.

**3단계 (JSON 모듈 임포트)**: `import json`으로 JSON 처리 모듈을 불러옵니다.

**4단계 (파일 열기)**: 쓰기 모드로 JSON 파일을 엽니다.

**5단계 (JSON 변환 및 저장)**: `json.dump(data, file)`는 딕셔너리를 JSON 형식의 문자열로 변환하여 파일에 씁니다.
- `dump`: "덤프한다", "떠서 옮긴다"는 의미

**최종 결과**: `./data/msg.json` 파일에 JSON 형식으로 데이터가 저장됩니다.

```json
{"id": "xxxxx", "pwd": "xxxx"}
```

> 💡 **중요!**: 강사님께서 설명하신 것처럼, "파이썬에는 JSON이라는 변수 타입이 없습니다. 그러니까 내가 지금 입출력이라는 개념으로 하게 되면 우리가 입출력 할 수 있는 건 텍스트 파일 밖에 없단 말이에요. 이 텍스트 파일에 심을 수 있는 형식은 문자열이에요. 그래서 딕셔너리라는 변수의 타입을 문자열로 컨버팅 시켜주는 모듈이 JSON인 거죠."

#### JSON 파일을 딕셔너리로 읽기

```python
import json

filePath = './data/msg.json'.strip()
with open(filePath, mode='r', encoding='utf-8') as file:
    loadData = json.load(file)
    print(loadData, '-', type(loadData))
    print(loadData['id'])
```

#### 💻 코드 실행 상세 분석

**1단계 (파일 열기)**: 읽기 모드로 JSON 파일을 엽니다.

**2단계 (JSON 파싱)**: `json.load(file)`는 JSON 형식의 문자열을 읽어서 딕셔너리로 변환합니다.
- `load`: "로드한다", "불러온다"는 의미

**3단계 (타입 확인)**: `type(loadData)`는 `<class 'dict'>`를 반환하여 딕셔너리로 변환되었음을 확인합니다.

**4단계 (데이터 접근)**: 딕셔너리이므로 키(`'id'`)로 값에 접근할 수 있습니다.

**최종 결과**: JSON 파일이 딕셔너리로 변환되어 사용 가능합니다.

```
실행 결과:
{'id': 'xxxxx', 'pwd': 'xxxx'} - <class 'dict'>
xxxxx
```

### 3.8 JSON 처리 요약

강사님께서 정리해주신 JSON 처리 흐름:

```
딕셔너리 (dict) → json.dump() → JSON 파일 (.json)
JSON 파일 (.json) → json.load() → 딕셔너리 (dict)
```

- **`json.dump(data, file)`**: 딕셔너리를 JSON 형식으로 변환하여 파일에 쓰기
- **`json.load(file)`**: JSON 파일을 읽어서 딕셔너리로 변환

> 📌 **노트**: 앞으로 Pandas를 이용해서 CSV 파일이나 Excel 파일을 가져와서 분석하게 될 것이라고 강사님께서 말씀하셨습니다.

---

## 🎨 4. 데코레이터 복습 및 심화

### 4.1 데코레이터의 개념 복습

강의에서 이전에 배운 데코레이터 개념을 복습했습니다. 데코레이터는 함수를 장식(decorate)하여 기능을 추가하는 문법입니다.

```python
from time import time, sleep

def timer(func):
    '''클로저를 가장한 데코레이터 / 함수를 전달받는다'''
    def wrapper(*args, **kwargs):
        '''실제 실행되는 함수 / 사용하던 사용하지 않던 이렇게 받을 수 있다'''
        start = time()
        result = func(*args, **kwargs)
        elapsed = time() - start
        
        if elapsed > 2:
            print(f'경고: {func.__name__}, 실행시간: {elapsed:.2f}초 초과되어서 알림')
        return result
    return wrapper

@timer
def timeFunc():
    sleep(3)
    return '성능확인'

inner = timeFunc()
print(inner)
```

#### 💻 코드 실행 상세 분석

**1단계 (데코레이터 정의)**:
- `timer` 함수는 다른 함수를 매개변수로 받습니다.
- 내부에 `wrapper` 함수를 정의하여 실제 실행 로직을 구현합니다.

**2단계 (wrapper 함수)**:
- `*args, **kwargs`로 모든 종류의 인자를 받을 수 있습니다.
- 시작 시간을 `start`에 기록합니다.
- 원래 함수 `func`를 실행하고 결과를 받습니다.
- 종료 시간과의 차이로 실행 시간을 계산합니다.

**3단계 (성능 체크)**:
- 실행 시간이 2초를 초과하면 경고 메시지를 출력합니다.
- 원래 함수의 결과를 반환합니다.

**4단계 (@timer 적용)**:
- `@timer`로 `timeFunc` 함수를 데코레이트합니다.
- 이는 `timeFunc = timer(timeFunc)`와 동일합니다.

**5단계 (함수 실행)**:
- `timeFunc()`를 호출하면 실제로는 `wrapper` 함수가 실행됩니다.
- `sleep(3)`으로 3초 대기하므로 2초를 초과하여 경고가 출력됩니다.

**최종 결과**: 실행 시간 경고와 함께 함수의 반환값이 출력됩니다.

```
실행 결과:
경고: timeFunc, 실행시간: 3.00초 초과되어서 알림
성능확인
```

> 💡 **중요!**: 강사님께서 말씀하신 것처럼, "이거는 단순한 화면 출력이고, 이거를 로그로 저장하면 추후에 이를 활용하여 분석할 수 있습니다." 실무에서는 성능 로그를 파일로 저장하여 시스템 최적화에 활용합니다.

### 4.2 클로저와 데코레이터

강사님께서 설명하신 것처럼, 데코레이터는 **클로저를 가장한 패턴**입니다.

- **클로저(Closure)**: 외부 함수의 변수를 내부 함수에서 사용하는 패턴
- **데코레이터(Decorator)**: 함수를 인자로 받아서 기능을 추가한 새로운 함수를 반환하는 패턴

```python
def timer(func):          # 외부 함수
    def wrapper(...):     # 내부 함수 (클로저)
        # func를 사용
    return wrapper        # 내부 함수를 반환
```

> 📌 **노트**: Python 기반의 애플리케이션에서는 클로저나 데코레이터 같은 문법을 많이 활용합니다. 강사님께서 강조하신 것처럼 "외면하기보다는 이해하는 시간이 필요합니다."

---

## 🛡️ 5. 실전 프로젝트: 보안 로깅 시스템

### 5.1 프로젝트 개요

강의 후반부에 진행한 최종 미션은 다음 요구사항을 포함합니다:

**시나리오**: 관리자가 사용자 정보를 조회할 때, 보안을 위해 다음 정보를 로그 파일로 저장하고 싶습니다.

**요구사항**:
1. 사용자 이름을 마스킹 처리 (예: `superadmin` → `su********`)
2. 관리자가 사용자 정보를 검색한 시간 기록
3. 함수 실행 시간 측정
4. 로그 포맷 형태로 `userAccess.log` 파일에 저장
5. 데코레이터를 이용하여 보안적인 측면 강화
6. 필요시 예외 처리 추가

### 5.2 마스킹 처리 구현

첫 번째 미션은 사용자 이름의 마스킹 처리입니다.

```python
user = {'name': 'superadmin', 'authenticated': True}
name = user['name']
print(name)

maskedName = name[:2] + '*' * (len(name) - 2)
print(maskedName)
```

#### 💻 코드 실행 상세 분석

**1단계 (이름 추출)**: 딕셔너리에서 `'name'` 키로 사용자 이름을 가져옵니다.
- `name = 'superadmin'`

**2단계 (슬라이싱)**: `name[:2]`는 처음 두 글자(`'su'`)를 추출합니다.

**3단계 (별표 생성)**: `'*' * (len(name) - 2)`는 별표를 8번 반복합니다.
- `len(name)` = 10
- `len(name) - 2` = 8
- `'*' * 8` = `'********'`

**4단계 (문자열 연결)**: `'su' + '********'` = `'su********'`

**최종 결과**: 처음 두 글자만 보이고 나머지는 별표로 마스킹됩니다.

```
실행 결과:
superadmin
su********
```

> 💡 **중요!**: 강사님께서 설명하신 것처럼, "사용자의 계정은 길이가 다를 수 있단 말이에요. 그걸 감안한다면 `len(name) - 2`를 사용하여 동적으로 마스킹 길이를 조절할 수 있습니다."

### 5.3 로깅 포맷 설정

두 번째 미션은 로깅 포맷을 생성하는 것입니다.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - %(levelname)s - %(message)s",
    force=True
)

logging.info("테스트 로그 메시지")
```

#### 💻 코드 실행 상세 분석

**1단계 (로깅 설정)**: `basicConfig()`로 로깅의 기본 설정을 구성합니다.

**2단계 (레벨 설정)**: `level=logging.INFO`로 INFO 레벨 이상의 로그만 출력하도록 설정합니다.

**3단계 (포맷 설정)**: 각 로그 메시지는 `[시간] - 레벨 - 메시지` 형식으로 출력됩니다.

**4단계 (로그 출력)**: `logging.info()`로 INFO 레벨의 로그를 기록합니다.

**최종 결과**: 설정한 포맷에 따라 로그가 출력됩니다.

```
실행 결과:
[2025-10-31 15:30:45,123] - INFO - 테스트 로그 메시지
```

### 5.4 완전한 보안 로깅 시스템 구현

강의에서 완성한 최종 솔루션입니다.

```python
import logging
from time import time, sleep

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - %(levelname)s - %(message)s",
    force=True
)

def secureLog(func):
    '''보안 로깅 데코레이터'''
    def wrapper(user, *args, **kwargs):
        start = time()
        logFile = "userAccess.log"
        try:
            result = func(user, *args, **kwargs)
            return result
        except Exception as e:
            with open(logFile, "a", encoding="utf-8") as f:
                f.write(f"[ERROR] {func.__name__} 실행 중 오류 발생: {e}\n")
            raise
        finally:
            end = time()
            # 이름 마스킹
            name = user.get("name", "unknown")
            maskedName = name[:2] + '*' * (len(name) - 2)
            duration = end - start
            # 로그를 파일에 저장
            with open(logFile, "a", encoding="utf-8") as f:
                f.write(
                    f"[INFO] 사용자 {maskedName}, "
                    f"함수 '{func.__name__}' 실행시간: {duration:.4f}초\n"
                )
    return wrapper

@secureLog
def getProfile(user: dict) -> None:
    print(f'{user["name"]} 프로필을 관리자가 검색합니다.')
    sleep(5)
    return {"profile": "user data"}

# 실행
user = {'name': 'superadmin', 'authenticated': True}
profile = getProfile(user)
print(profile)
```

#### 💻 코드 실행 상세 분석

**1단계 (데코레이터 정의)**:
- `secureLog` 함수는 보안 로깅 기능을 추가하는 데코레이터입니다.
- `wrapper` 함수에서 실제 로깅 로직을 구현합니다.

**2단계 (시작 시간 기록)**:
- `start = time()`으로 함수 실행 시작 시간을 기록합니다.

**3단계 (try 블록)**:
- 원래 함수 `func(user, *args, **kwargs)`를 실행합니다.
- 정상적으로 실행되면 결과를 반환합니다.

**4단계 (except 블록)**:
- 예외가 발생하면 에러 로그를 파일에 기록합니다.
- `raise`로 예외를 다시 발생시켜 호출자에게 전달합니다.

**5단계 (finally 블록)**:
- 예외 발생 여부와 관계없이 실행됩니다.
- 종료 시간을 기록하고 실행 시간을 계산합니다.
- `user.get("name", "unknown")`으로 안전하게 이름을 가져옵니다.
- 이름을 마스킹 처리합니다.
- 로그를 `userAccess.log` 파일에 추가 모드(`'a'`)로 저장합니다.

**6단계 (getProfile 함수)**:
- `@secureLog` 데코레이터가 적용되어 보안 로깅이 자동으로 수행됩니다.
- 사용자 프로필 조회 시뮬레이션을 위해 5초 대기합니다.
- 프로필 정보를 딕셔너리로 반환합니다.

**7단계 (함수 호출)**:
- `getProfile(user)`를 호출하면 데코레이터의 `wrapper`가 실행됩니다.

**최종 결과**: 
- 콘솔에 프로필 검색 메시지와 결과가 출력됩니다.
- `userAccess.log` 파일에 마스킹된 사용자 이름과 실행 시간이 기록됩니다.

```
실행 결과 (콘솔):
superadmin 프로필을 관리자가 검색합니다.
{'profile': 'user data'}

실행 결과 (userAccess.log 파일):
[INFO] 사용자 su********, 함수 'getProfile' 실행시간: 5.0023초
```

> 🔐 **보안 노트**:
> - **마스킹(Masking)**: 민감한 사용자 정보를 로그에 직접 기록하지 않고 일부를 가려서 기록합니다. 이는 로그 파일이 유출되더라도 실제 사용자 이름을 알 수 없게 합니다.
> - **안전한 딕셔너리 접근**: `user.get("name", "unknown")`을 사용하면 키가 없어도 예외가 발생하지 않고 기본값을 반환합니다.
> - **파일 추가 모드**: `mode='a'`를 사용하여 기존 로그를 유지하면서 새 로그를 추가합니다.
> - **예외 재발생**: `raise`를 사용하여 예외를 기록한 후 다시 발생시켜 호출자가 예외를 처리할 수 있게 합니다.
> - **finally 블록 활용**: 예외 발생 여부와 관계없이 로그를 기록하여 모든 실행 이력을 추적합니다.

### 5.5 코드 구현 접근 방법

강사님께서 강조하신 점진적 구현 방법:

1. **단계별 구현**: 한 번에 모든 것을 구현하지 말고 단계별로 접근
2. **마스킹 먼저**: 문자열 마스킹 로직을 먼저 테스트
3. **로깅 포맷**: 로깅 포맷을 설정하고 테스트
4. **파일 저장**: 로그를 파일로 저장하는 기능 추가
5. **데코레이터 통합**: 최종적으로 데코레이터로 통합

> 💡 **중요!**: 강사님께서 말씀하신 것처럼, "저는 한 번에 할 수 없어요. 전 능력이 안 돼가지고 이걸 한 번에 이제 구현을 못할 것 같아요. 그래서 저는 어떻게 한번 해보고 싶냐면 여러분들께 조금 끊어서 끊어서 설명을 한번 드려볼까 합니다." 이런 접근 방식이 실제로 더 효과적입니다.

### 5.6 단순화된 버전

데코레이터 없이 단순화된 버전도 살펴보았습니다.

```python
from time import time
from datetime import datetime

def getProfile(user: dict) -> None:
    start_time = time()
    
    name = user['name']
    maskedName = name[:2] + '*' * (len(name) - 2)
    
    end_time = time()
    elapsed_time = end_time - start_time
    
    readable_start_time = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
    
    filePath = './data/userAccess.log'.strip()
    with open(filePath, mode='w', encoding='utf-8') as file:
        logTxt = (
            f"검색 시간: {readable_start_time} / "
            f"사용자: {maskedName} / "
            f"실행 시간(초): {elapsed_time:.6f}"
        )
        file.write(logTxt)
    logging.info(logTxt)

user = {'name': 'superadmin', 'authenticated': True}
getProfile(user)
```

#### 💻 코드 실행 상세 분석

**1단계 (시작 시간 기록)**: `time()`으로 Unix 타임스탬프를 기록합니다.

**2단계 (마스킹 처리)**: 사용자 이름을 마스킹합니다.

**3단계 (종료 시간 및 실행 시간 계산)**: 종료 시간과의 차이로 실행 시간을 구합니다.

**4단계 (시간 포맷 변환)**: `datetime.fromtimestamp()`로 Unix 타임스탬프를 읽기 쉬운 형식으로 변환합니다.
- `strftime('%Y-%m-%d %H:%M:%S')`로 `2025-10-31 15:30:45` 형식으로 포맷팅합니다.

**5단계 (로그 텍스트 생성)**: f-string으로 로그 메시지를 생성합니다.

**6단계 (파일 저장)**: `with open`으로 로그를 파일에 저장합니다.

**7단계 (콘솔 로깅)**: `logging.info()`로 콘솔에도 로그를 출력합니다.

**최종 결과**: 파일과 콘솔에 모두 로그가 기록됩니다.

```
실행 결과 (콘솔):
[2025-10-31 15:30:45,123] - INFO - 검색 시간: 2025-10-31 15:30:45 / 사용자: su******** / 실행 시간(초): 0.000123

실행 결과 (userAccess.log 파일):
검색 시간: 2025-10-31 15:30:45 / 사용자: su******** / 실행 시간(초): 0.000123
```

---

## 🧩 6. 복합 예제 및 심화 학습

### 6.1 문자열 연산의 이해

강의에서 흥미로운 문자열 연산을 배웠습니다.

```python
print('*' * 10)
```

#### 💻 코드 실행 상세 분석

**1단계 (문자열 곱셈)**: 문자열에 정수를 곱하면 문자열이 반복됩니다.

**최종 결과**: `'*'`이 10번 반복됩니다.

```
실행 결과:
**********
```

> 💡 **중요!**: 강사님께서 말씀하신 것처럼, "신기하죠? 어? 문자열에 대한 연산도 가능해? 이게 파이썬입니다." Python의 유연한 연산자 오버로딩(operator overloading) 기능입니다.

### 6.2 리스트 컴프리헨션 활용

파일 읽기에서 리스트 컴프리헨션을 활용할 수 있습니다.

```python
with open(filePath, mode='r', encoding='utf-8') as file:
    result = [txt for txt in file.readlines()]
    print(result)
```

#### 💻 코드 실행 상세 분석

**1단계 (파일 읽기)**: `file.readlines()`로 모든 줄을 리스트로 가져옵니다.

**2단계 (리스트 컴프리헨션)**: `[txt for txt in file.readlines()]`는 각 줄을 순회하며 새 리스트를 생성합니다.

**최종 결과**: 파일의 각 줄이 리스트의 요소가 됩니다.

```
실행 결과:
['강사님과 함께하는 즐겁지 아니한 파이썬수업\n', '그렇지만 열공하자\n', ...]
```

### 6.3 enumerate의 활용

`enumerate`는 인덱스와 값을 동시에 얻을 수 있는 유용한 함수입니다.

```python
lst = ['apple', 'banana', 'cherry']
for idx, data in enumerate(lst):
    print(f'인덱스 {idx}: {data}')
```

#### 💻 코드 실행 상세 분석

**1단계 (enumerate 호출)**: `enumerate(lst)`는 `(index, value)` 튜플을 생성합니다.

**2단계 (언패킹)**: `for idx, data`로 튜플을 인덱스와 값으로 분리합니다.

**최종 결과**: 각 요소의 인덱스와 값이 함께 출력됩니다.

```
실행 결과:
인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
```

> 📌 **노트**: 강의에서 로깅할 때 어느 위치에서 문제가 발생했는지 명확히 알기 위해 `enumerate`를 사용했습니다.

### 6.4 isinstance()를 활용한 타입 체크

보안 관점에서 타입 체크는 매우 중요합니다.

```python
data = 'hello'
print(isinstance(data, str))     # True
print(isinstance(data, int))     # False
print(isinstance(data, (int, float)))  # False

number = 42
print(isinstance(number, (int, float)))  # True
```

#### 💻 코드 실행 상세 분석

**1단계 (단일 타입 체크)**: `isinstance(data, str)`은 `data`가 문자열인지 확인합니다.

**2단계 (튜플을 이용한 다중 타입 체크)**: `isinstance(data, (int, float))`는 `data`가 정수 또는 실수인지 확인합니다.

**최종 결과**: 타입이 일치하면 `True`, 아니면 `False`를 반환합니다.

> 🔐 **보안 노트**: 강사님께서 강조하신 것처럼, "보안 관점에서 입력 검증"을 위해 `isinstance()`를 사용하는 것은 **타입 안정성(type safety)**을 확보하는 핵심 방법입니다.

---

## 📚 7. 향후 학습 방향

### 7.1 다음 주 학습 내용

강사님께서 안내하신 다음 주 학습 계획:

1. **NumPy (넘파이)**: 수학적 연산과 배열 처리
2. **Pandas (판다스)**: 데이터 분석과 DataFrame
3. **시각화 (Visualization)**: Matplotlib, Seaborn 등
4. **LLM (Large Language Model)**: 언어 모델 연동

> 💡 **중요!**: 강사님께서 말씀하신 것처럼, "다음 주 금요일쯤에는 LLM 쪽을 들어갈 수 있지 않을까라는 그런 생각을 좀 가져봅니다."

### 7.2 프로젝트 방향성

강사님께서 언급하신 향후 프로젝트:

**1주일짜리 프로젝트 개요**:
- 보안에 관련된 데이터셋 검색
- 데이터 전처리 및 분석(EDA)
- 데이터 신뢰도 기반 모델 사용
- LLM 또는 LangChain 연결
- 인사이트(Insight) 도출

**프로젝트 흐름**:
```
주제 선정 → 데이터 수집 → 전처리 → 분석 → 모델링 → 인사이트 도출
```

> 📌 **노트**: 강사님께서 강조하신 것처럼, "정보 보안 전공자는 커리어를 쌓으면서 프로젝트 진행을 위한 주제 등을 머리에 담고 있는 사람도 있을 수 있습니다. 조가 구성되면 친밀감을 갖고 다가가기 바랍니다."

### 7.3 필요 시 학습할 내용

- **정규표현식 (Regular Expression)**: 필요시 강의 예정
- **전처리 과정**: 데이터 분석을 위한 사전 작업
- **EDA (Exploratory Data Analysis)**: 탐색적 데이터 분석

---

## 💡 8. 핵심 개념 정리

### 8.1 예외 처리 핵심 요약

- **예외 처리 구조**: `try-except-else-finally`
- **예외 발생**: `raise` 키워드 사용
- **다중 예외 처리**: 보안 관점에서 권장
- **finally 블록**: 리소스 정리 및 로그 기록에 필수
- **안전한 종료**: 웜 셧다운(warm shutdown) 구현

### 8.2 로깅 핵심 요약

- **로그 레벨**: DEBUG < INFO < WARNING < ERROR < CRITICAL
- **로깅 설정**: `logging.basicConfig()`
- **포맷 커스터마이징**: `format` 파라미터 사용
- **파일 저장**: `filename`과 `filemode` 설정
- **보안 이점**: 일반화된 메시지로 시스템 정보 노출 방지

### 8.3 파일 입출력 핵심 요약

- **파일 모드**: `'r'` (읽기), `'w'` (쓰기), `'a'` (추가)
- **with 구문**: 자동 파일 닫기로 리소스 관리
- **read() vs readlines()**: 전체 문자열 vs 줄 단위 리스트
- **JSON 처리**: `json.dump()`로 저장, `json.load()`로 읽기
- **인코딩**: `encoding='utf-8'`로 한글 지원

### 8.4 데코레이터 핵심 요약

- **데코레이터 패턴**: 함수에 기능을 추가하는 고급 패턴
- **@구문**: 간편한 데코레이터 적용
- **클로저 활용**: 외부 함수의 변수를 내부 함수에서 사용
- **보안 강화**: 로깅, 인증, 권한 검사 등에 활용
- **성능 측정**: 실행 시간 측정에 유용

---

## 🎯 9. 실전 팁 및 모범 사례

### 9.1 코드 개발 접근 방법

강사님께서 강조하신 개발 접근 방법:

1. **단계별 구현**: 한 번에 모든 것을 구현하려 하지 말 것
2. **테스트 주도**: 각 단계마다 테스트하며 진행
3. **긍정적 사고**: "이렇게 안 되네? 어, 그럼 이렇게 해볼까?" 같은 발전적 생각
4. **오류 환영**: 오류가 감지되면 해결 기회로 여길 것
5. **점진적 개선**: 기능을 하나씩 추가하며 완성도를 높일 것

> 💡 **중요!**: "저는 항상 말씀드리지만 여러분들의 생각을 확장시키는 게 좋아요. 어떤 결과만을 환호하는 건 큰 의미가 없다라고 생각을 합니다. 그 진행하는 과정 하나하나씩 내가 곱씹어보는 그 과정에 있어서의 자양분이 여러분들에게 분명 될 거라는 생각을 합니다."

### 9.2 예외 처리 모범 사례

1. **명확한 예외 타입 사용**: `Exception`보다는 구체적인 예외 타입
2. **의미 있는 에러 메시지**: 문제 해결에 도움이 되는 정보 포함
3. **로깅 활용**: 예외 발생 시 로그에 상세 정보 기록
4. **예외 재발생**: 필요시 `raise`로 상위 호출자에게 전달
5. **리소스 정리**: `finally` 블록에서 반드시 정리 작업 수행

### 9.3 보안 코딩 가이드라인

1. **입력 검증**: 모든 사용자 입력은 검증 후 사용
2. **타입 체크**: `isinstance()`로 타입 안정성 확보
3. **민감 정보 마스킹**: 로그에 민감 정보 직접 기록 금지
4. **안전한 파일 작업**: 경로 조작 공격 방지
5. **일반화된 에러 메시지**: 시스템 내부 정보 노출 방지

### 9.4 로깅 모범 사례

1. **적절한 로그 레벨**: 상황에 맞는 레벨 사용
2. **구조화된 로그**: 일관된 포맷으로 파싱 용이하게
3. **파일 로테이션**: 로그 파일 크기 관리
4. **타임스탬프 포함**: 모든 로그에 시간 정보 기록
5. **추적 가능성**: 문제 발생 시 추적할 수 있는 충분한 정보 기록

---

## 🚀 10. 실습 과제 및 확장 아이디어

### 10.1 제안하는 실습 과제

강의 내용을 복습하기 위한 실습 과제:

**과제 1: 향상된 사용자 입력 검증 시스템**
- 정규표현식을 활용한 이메일 검증
- 전화번호 형식 검증
- 주민등록번호 형식 검증 (마스킹 포함)

**과제 2: 다양한 로그 레벨 활용**
- 각 로그 레벨에 적합한 상황 정의
- 로그 파일을 레벨별로 분리
- 로그 통계 및 분석 기능 추가

**과제 3: JSON 데이터베이스 구현**
- JSON 파일을 데이터베이스처럼 사용
- CRUD (Create, Read, Update, Delete) 기능 구현
- 트랜잭션 및 백업 기능 추가

**과제 4: 데코레이터 라이브러리**
- 권한 검사 데코레이터
- 캐싱 데코레이터
- 재시도(retry) 데코레이터
- API 호출 제한 데코레이터

### 10.2 확장 아이디어

**보안 감사 시스템**:
```python
@audit_trail
@authentication_required
@rate_limit(max_calls=100, period=60)
def sensitive_operation(user, data):
    # 민감한 작업 수행
    pass
```

**성능 모니터링 시스템**:
```python
@performance_monitor
@alert_on_slow(threshold=2.0)
def critical_function():
    # 중요한 작업 수행
    pass
```

**분산 로깅 시스템**:
```python
@distributed_log(service='api-gateway')
@trace_id_injection
def api_endpoint(request):
    # API 처리
    pass
```

---

## 📖 11. 학습 점검 및 복습 가이드

### 11.1 핵심 질문

다음 질문에 답할 수 있는지 확인해보세요:

1. 예외(Exception)와 에러(Error)의 차이는 무엇인가요?
2. `try-except-else-finally` 각 블록은 언제 실행되나요?
3. `raise` 키워드는 왜 사용하나요?
4. 로깅 레벨의 우선순위는 어떻게 되나요?
5. `print()`와 로깅의 차이는 무엇인가요?
6. `with open` 구문의 장점은 무엇인가요?
7. `json.dump()`와 `json.load()`의 역할은 무엇인가요?
8. 데코레이터는 어떤 상황에서 유용한가요?
9. 마스킹 처리는 왜 필요한가요?
10. `enumerate()`와 `isinstance()`는 언제 사용하나요?

### 11.2 코드 리뷰 체크리스트

자신의 코드를 다음 항목으로 점검해보세요:

**예외 처리**:
- [ ] 예외가 발생할 수 있는 코드는 `try-except`로 감쌌는가?
- [ ] 구체적인 예외 타입을 사용했는가?
- [ ] 의미 있는 에러 메시지를 제공하는가?
- [ ] `finally` 블록에서 리소스를 정리하는가?

**로깅**:
- [ ] 적절한 로그 레벨을 사용했는가?
- [ ] 로그 포맷이 일관성 있는가?
- [ ] 중요한 이벤트를 로그에 기록했는가?
- [ ] 민감한 정보를 마스킹했는가?

**파일 입출력**:
- [ ] `with` 구문을 사용했는가?
- [ ] 파일 모드를 올바르게 설정했는가?
- [ ] UTF-8 인코딩을 지정했는가?
- [ ] 예외 처리를 했는가?

**보안**:
- [ ] 입력 검증을 수행했는가?
- [ ] 타입 체크를 했는가?
- [ ] 민감한 정보를 보호했는가?
- [ ] 경로 조작 공격을 방지했는가?

### 11.3 복습 방법

**하루 복습**:
- 오늘 배운 코드를 처음부터 다시 작성해보기
- 각 개념을 자신의 말로 설명해보기

**주간 복습**:
- 이번 주 학습 내용을 하나의 프로젝트로 통합하기
- 학습 노트를 정리하고 이해 안 되는 부분 표시하기

**프로젝트 실습**:
- 실제 사용 가능한 작은 프로그램 만들기
- 강의 내용을 응용한 새로운 기능 추가하기

---

## 🎓 12. 강사님의 조언 및 격려

### 12.1 학습 태도

강사님께서 강조하신 중요한 조언들:

> "여러분들, 제가 항상 말씀드리지만 여러분들, 천만 배우셨던 내용을 지금 와서 한번 생각해 보세요. 어떠세요? 발전하신 거 맞죠? 그러지 않나요? 어제는 몰랐던 거 오늘 좀 더 이해되고 그렇다면 그게 하루하루가 더 지나다 보면 좀 더 이해가 될 수 있겠죠."

> "맵집을 키우고 여러분들의 생각을 확장시키는 게 좋아요. 저는 이런 교육을 하면서 항상 느끼는 게 어떤 결과만을 환호하는 건 큰 의미가 없다라고 생각을 합니다."

> "결과에 환호하지 마세요. 그 진행하는 과정 하나하나씩 내가 곱씹어보는 그 과정에 있어서의 자양분이 여러분들이 분명 될 거라는 생각을 합니다."

### 12.2 어려움 극복

강사님께서 공유하신 어려움 극복 방법:

> "이거 제가 토로 드릴게요. 너무 어려운 부분이기 때문에. 자, 그래서 오늘 제가 기분 좋게 여러분들 '수업 오늘 나는 퀴즈 풀고 집에 가서 쉬어야겠다' 라는 느낌을 드리고 싶긴 했지만 네, 그러지 못했습니다."

> "단순하게 하신 분 계실까요 혹시? 그래서 만약에 한다라면 아마 이런 식으로도 많이 하시지 않으셨을까 싶은데. 이렇게 단계별로 좀 진행하시길 좀 부탁을 드려봤던 거고."

### 12.3 지속적인 학습

강사님의 학습 철학:

> "저는 이제 MBTI가 ISFJ라고 제가 어제인가 말씀을 드렸잖아요. 그래서 외향적이지는 않아요. 뭐 제가 갖는 취미 중에 하나가 있는데요. 그니까 제가 말하는 정적이라는 건 뭔가 그런 모임 같은 걸 하기보다는 이제 혼자서 이게 하는 내 나름대로 어떤 그 레벨업을 하는 스킬을 쌓는 이런 걸 좀 좋아한다라는 의미로 이제 정적이다라고 말씀을 드려봤습니다."

### 12.4 함께 성장하기

팀워크와 협업의 중요성:

> "정보 보안 전공자는 커리어를 쌓으면서 프로젝트 진행을 위한 주제 등을 머리에 담고 있는 사람도 있을 수 있습니다. 조가 구성되면 친밀감을 갖고 다가가기 바랍니다."

---

## 🌟 13. 마무리 및 다음 강의 안내

### 13.1 오늘 배운 내용 요약

오늘 강의에서는 다음과 같은 내용을 학습했습니다:

1. **예외 처리의 기본과 실전 활용**
   - try-except-else-finally 구조
   - raise를 통한 예외 발생
   - 사용자 입력 검증 시스템

2. **로깅 시스템의 이해와 활용**
   - 로그 레벨과 포맷 설정
   - 파일 로깅
   - 보안 관점의 로깅

3. **파일 입출력의 기본**
   - 텍스트 파일 읽기/쓰기
   - JSON 파일 처리
   - with 구문의 활용

4. **데코레이터를 활용한 보안 강화**
   - 성능 측정 데코레이터
   - 보안 로깅 데코레이터
   - 실전 프로젝트 구현

5. **마스킹 처리와 보안 로깅 시스템**
   - 민감 정보 보호
   - 로그 파일 관리
   - 통합 보안 시스템 구축

### 13.2 다음 주 학습 준비

**학습 환경 준비**:
- NumPy, Pandas 라이브러리 설치 준비
- Jupyter Notebook 환경 점검
- 이번 주 학습 내용 복습

**예습 권장 사항**:
- NumPy의 기본 개념 (배열, 행렬)
- Pandas의 DataFrame 개념
- 데이터 분석의 기본 흐름

### 13.3 강사님의 마지막 인사

> "어떠셨습니까, 여러분? 일주일 동안 저와 함께 뭐, 항해를 시작해 봤는데 네, 파도가 너무 심하던가요? 어떠셨어요? 난파당했다고요?"

> "여튼 저도 한 주 동안 여러분과 함께 즐거웠고요. 여러분들도 행복한 주말 보내시고요. 사건 사고 없이 저는 다음 주 월요일에 건강한 모습으로 여러분 찾아뵐 수 있도록 하겠습니다."

> "네, 수고하셨습니다. 주말 잘 보내시고요. 저희의 그라운드를 다음 주에 뵐게요."

---

## 📝 14. 강의 노트 작성자 후기

### 14.1 학습 소감

오늘 강의는 실무에서 가장 중요한 내용들로 구성되어 있었습니다. 특히 예외 처리, 로깅, 파일 입출력은 어떤 프로그램을 만들더라도 반드시 필요한 기본기입니다. 강사님께서 단계별로 차근차근 설명해주신 덕분에 복잡한 개념들도 이해할 수 있었습니다.

### 14.2 중요 포인트

1. **예외 처리는 선택이 아닌 필수**: 안정적인 프로그램을 위해 반드시 필요
2. **로깅은 보안의 시작**: print() 대신 로깅을 습관화해야 함
3. **파일 입출력은 데이터 영속성의 기본**: 데이터를 저장하고 불러오는 기본 기술
4. **데코레이터는 강력한 도구**: 코드 재사용과 보안 강화에 탁월
5. **보안은 코딩의 일부**: 처음부터 보안을 고려한 코드 작성 습관 중요

### 14.3 실전 적용 계획

1. **개인 프로젝트에 예외 처리 추가**: 기존 코드에 예외 처리 적용
2. **로깅 시스템 구축**: 모든 프로그램에 로깅 기능 추가
3. **데코레이터 라이브러리 만들기**: 자주 사용하는 데코레이터 모음 제작
4. **보안 코딩 가이드라인 작성**: 팀 내 보안 코딩 규칙 정립
5. **실전 프로젝트 진행**: 배운 내용을 통합한 보안 시스템 구축

### 14.4 다짐

강사님께서 말씀하신 것처럼 "결과에 환호하지 말고, 과정을 곱씹는" 자세로 학습하겠습니다. 매일 조금씩 성장하는 개발자가 되기 위해 꾸준히 노력하겠습니다. 다음 주에 배울 NumPy와 Pandas도 기대가 됩니다!

---

## 🔗 15. 참고 자료 및 추가 학습 자료

### 15.1 공식 문서

- [Python 공식 문서 - 예외 처리](https://docs.python.org/ko/3/tutorial/errors.html)
- [Python 공식 문서 - logging 모듈](https://docs.python.org/ko/3/library/logging.html)
- [Python 공식 문서 - 파일 입출력](https://docs.python.org/ko/3/tutorial/inputoutput.html)
- [Python 공식 문서 - json 모듈](https://docs.python.org/ko/3/library/json.html)

### 15.2 추천 읽을거리

- **Clean Code (로버트 C. 마틴)**: 깔끔한 코드 작성법
- **Effective Python (브렛 슬래킨)**: Python 고급 기법
- **Python Cookbook (데이비드 비즐리)**: Python 실전 레시피
- **The Pragmatic Programmer (앤드류 헌트)**: 실용주의 프로그래머

### 15.3 온라인 리소스

- Real Python: 고품질 Python 튜토리얼
- Python Weekly: 주간 Python 뉴스레터
- PyCon 발표 자료: 다양한 Python 활용 사례
- GitHub: 오픈소스 Python 프로젝트

---

## 📌 16. 부록: 전체 코드 예제 모음

### 16.1 예외 처리 완전 예제

```python
def getUserInfo():
    '''사용자 정보 입력 및 검증'''
    try:
        name = input('이름을 입력하세요 : ').strip()
        if not name.isalpha():
            raise ValueError('이름은 문자만 포함해야 합니다!!')
        
        age = input('나이를 입력하세요 : ').strip()
        if not age.isdigit():
            raise ValueError('나이는 숫자만 입력하세요!!')
        age = int(age)
        if age < 0 or age > 120:
            raise ValueError('1 ~ 120 사이의 숫자만 입력하세요!!')
            
        email = input('이메일 주소를 입력하세요 : ').strip()
        if '@' not in email or '.' not in email:
            raise ValueError('올바른 이메일 형식이 아닙니다!!')
        
        return {
            "name": name,
            "age": age,
            "email": email
        }
    except ValueError as ve:
        print(f'입력 오류 {ve}')
        return None
    finally:
        print('입력정보를 정상적으로 처리 하였습니다!!')

# 실행
result = getUserInfo()
if result:
    print(f"등록 성공: {result}")
else:
    print("등록 실패")
```

### 16.2 로깅 완전 예제

```python
import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename='application.log',
    filemode='a'
)

def lstPrt(lst: list) -> list:
    '''리스트 거듭제곱 함수 (예외 처리 및 로깅)'''
    if not isinstance(lst, list):
        raise TypeError('매개변수 타입은 반드시 list 형태')
    
    result = []
    for idx, data in enumerate(lst):
        if not isinstance(data, (int, float)):
            logging.warning(
                f'인덱스 {idx} 번째에 숫자가 아닌 값 포함, '
                f'타입은: {type(data).__name__}'
            )
            continue
        try:
            result.append(data ** 2)
        except Exception as e:
            logging.error(f'예상치 못한 예외 발생: {e}')
    
    return result

# 실행
tmp = [10, 20, 30, 40, 'seop', 50, 60]
result = lstPrt(tmp)
print(result)
```

### 16.3 파일 입출력 완전 예제

```python
import json

# 텍스트 파일 쓰기
data_text = "안녕하세요~ 한 주 수고많으셨구요...즐거운 금요일 되시길 바랍니다."
with open('./data/message.txt', mode='w', encoding='utf-8') as file:
    file.write(data_text)

# 텍스트 파일 읽기
with open('./data/message.txt', mode='r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# JSON 파일 쓰기
data_dict = {'id': 'xxxxx', 'pwd': 'xxxx'}
with open('./data/msg.json', mode='w', encoding='utf-8') as file:
    json.dump(data_dict, file)

# JSON 파일 읽기
with open('./data/msg.json', mode='r', encoding='utf-8') as file:
    loadData = json.load(file)
    print(loadData, type(loadData))
    print(loadData['id'])
```

### 16.4 데코레이터 완전 예제

```python
import logging
from time import time, sleep

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - %(levelname)s - %(message)s",
    force=True
)

def secureLog(func):
    '''보안 로깅 데코레이터'''
    def wrapper(user, *args, **kwargs):
        start = time()
        logFile = "userAccess.log"
        try:
            result = func(user, *args, **kwargs)
            return result
        except Exception as e:
            with open(logFile, "a", encoding="utf-8") as f:
                f.write(f"[ERROR] {func.__name__} 실행 중 오류 발생: {e}\n")
            raise
        finally:
            end = time()
            name = user.get("name", "unknown")
            maskedName = name[:2] + '*' * (len(name) - 2)
            duration = end - start
            with open(logFile, "a", encoding="utf-8") as f:
                f.write(
                    f"[INFO] 사용자 {maskedName}, "
                    f"함수 '{func.__name__}' 실행시간: {duration:.4f}초\n"
                )
    return wrapper

@secureLog
def getProfile(user: dict) -> dict:
    '''사용자 프로필 조회'''
    print(f'{user["name"]} 프로필을 관리자가 검색합니다.')
    sleep(5)
    return {"profile": "user data"}

# 실행
user = {'name': 'superadmin', 'authenticated': True}
profile = getProfile(user)
print(profile)
```

---

## 🎉 강의 노트 완성!

이번 강의는 Python의 핵심 기능인 **예외 처리**, **로깅**, **파일 입출력**, **데코레이터**를 실무 관점에서 깊이 있게 다루었습니다. 특히 보안을 고려한 코드 작성 방법과 마스킹 처리를 통한 민감 정보 보호 기법은 실무에서 바로 활용할 수 있는 귀중한 지식입니다.

강사님께서 강조하신 것처럼 **"과정을 곱씹으며 하루하루 발전"**하는 자세로 학습을 이어가겠습니다. 다음 주에 배울 NumPy와 Pandas, 그리고 LLM 연동 수업도 기대가 됩니다!

**행복한 주말 보내시고, 다음 주에 또 만나요!** 🚀

---

**작성일**: 2025년 10월 31일  
**작성자**: Secure Python 수강생  
**강의**: Day 5 - 예외 처리, 로깅, 파일 입출력  
**다음 강의 예고**: NumPy, Pandas, 데이터 분석