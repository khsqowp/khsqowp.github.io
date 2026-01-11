---"
title: "📝 NumPy & Pandas Day 3 강의 노트 (11월 5일)"
date: 2025-11-05
excerpt: "실전 데이터셋(Titanic, Iris)을 활용한 데이터 조작, 인덱싱(loc/iloc), 결측치 처리 및 GroupBy 연산을 통한 데이터 분석 심화 과정을 다룹니다."
categories:
  - Python
tags:
  - Python
  - SK_Rookies
"---

# 📝 NumPy & Pandas Day 3 강의 노트 (11월 5일)

---

## 📚 학습 내용 개요

오늘 강의에서는 **데이터 프레임 조작**에 대해 심도 깊게 배웠습니다. 어제까지는 데이터 프레임을 만들고 이해하는 시간이었다면, 오늘은 본격적으로 데이터 프레임을 조작하고 분석하는 다양한 함수들을 학습했습니다. 특히 실제 데이터셋(Titanic, Iris)을 활용하여 실무에서 자주 사용되는 데이터 조작 기법들을 익혔습니다.

### 🎯 학습 목표

1. **데이터 조작 기법 습득**: DataFrame을 효과적으로 다루는 방법 학습
2. **인덱싱과 슬라이싱**: `loc[]`, `iloc[]` 인덱서를 활용한 데이터 접근 방법
3. **실전 데이터셋 활용**: Titanic, Iris 데이터셋을 통한 실습
4. **GroupBy 연산**: 그룹별 집계와 분석 기법
5. **결측값 처리**: 실무에서 필수적인 데이터 전처리 기법

---

## 🔄 이전 강의 복습

### Series와 DataFrame의 기본 개념

강사님께서 오늘 수업을 시작하기 전에 어제 배웠던 내용을 복습하는 시간을 가졌습니다. 복습 내용은 다음과 같습니다:

#### Series 구조

**Series는 무엇으로 이루어져 있을까요?**

- **인덱스(Index)**: 각 데이터를 식별하는 라벨
- **값(Value)**: 실제 데이터가 저장된 배열

> 💡 **중요!**: Series는 DataFrame을 이루는 구성 요소 중 하나입니다. DataFrame에서 **열(Column)**의 역할을 담당합니다.

#### DataFrame 구조

**DataFrame은 어떻게 구성될까요?**

- **행 인덱스(Row Index)**: 각 행을 식별하는 라벨
- **열 인덱스(Column Index)**: 각 열을 식별하는 라벨
- **2차원 배열 데이터**: NumPy 배열 형태로 저장된 실제 데이터

> 💡 **핵심 개념**: DataFrame은 여러 개의 Series가 모여서 만들어진 2차원 데이터 구조입니다. DataFrame을 이해할 때는 "행의 집합"이 아니라 **"열의 집합"**으로 바라봐야 합니다.

#### 인덱싱 원칙

강사님께서 강조하신 중요한 원칙:

1. **DataFrame의 기본 인덱싱**: 열(Column) 인덱싱
2. **행 인덱싱을 위한 방법**: 슬라이싱 또는 `loc[]`, `iloc[]` 인덱서 사용

#### 전처리(Preprocessing) 개념

어제 노출되었던 중요한 용어:

- **전처리(Preprocessing)**: 데이터를 분석하기 전에 정제하는 과정
- **가장 기본적인 전처리**: **널(Null) 값 처리**
  
> 📌 **노트**: 널 값이 포함된 데이터는 학습용 데이터로 활용할 수 없기 때문에, 전처리를 통해 반드시 처리해야 합니다.

---

## 🛠️ 개발 환경 설정 안내

### VS Code와 Git 설치

강사님께서 오늘 수업 시작 전에 개발 환경 설정에 대해 안내해주셨습니다.

#### VS Code 설치 이유

지금까지는 Jupyter Notebook 환경에서 작업했지만, 앞으로는 **Python 파일(.py)**을 사용해야 하는 경우가 있습니다. 특히 **시각화 툴인 Streamlit**을 사용하려면 VS Code 환경이 필요합니다.

**설치 방법**:
- VS Code 공식 사이트에서 다운로드
- 설치 과정은 특별한 설정 없이 기본 옵션으로 진행 (클릭만 하면 됨)

#### Git 설치

VS Code에서 터미널을 PowerShell로 열어서 사용할 수도 있지만, 조금 불편합니다. Git을 로컬에 설치하면 더 편리하게 작업할 수 있습니다.

**설치 방법**:
- Git 공식 사이트에서 다운로드
- VS Code와 마찬가지로 기본 옵션으로 설치 진행

### Streamlit 시각화 툴

강사님께서 아침에 테스트하신 **Streamlit**은 데이터를 웹 브라우저 상에서 시각화할 수 있는 강력한 도구입니다.

**Streamlit의 특징**:
- Python 파일(.py)로 작성
- 브라우저에서 실시간으로 결과 확인
- Matplotlib, Seaborn 등의 시각화 라이브러리와 연동
- Plotly를 사용하면 더욱 고급스러운 시각화 가능 (그라데이션 등)

> 📌 **노트**: 시각화를 하기 위해서는 먼저 **분석**이 필요합니다. 단순히 데이터 프레임을 시각화하는 것이 아니라, 의미 있는 인사이트를 찾아내는 과정이 선행되어야 합니다.

---

## 💻 환경 설정 및 기본 셋업

### 필수 라이브러리 Import

오늘 강의를 위해 준비한 기본 셋업 코드입니다. 강사님께서 처음에 이 코드를 공유해주셨습니다.

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# warning 제거
import warnings
warnings.filterwarnings('ignore')

# version check
print('numpy  version - ', np.__version__)
print('pandas version - ', pd.__version__)
```

#### 💻 코드 실행 상세 분석

**1단계 (라이브러리 Import)**:
- `numpy as np`: 배열 연산과 수학 함수를 위한 라이브러리
- `pandas as pd`: 데이터 프레임 조작을 위한 라이브러리
- `seaborn as sns`: 통계 데이터 시각화 라이브러리
- `matplotlib.pyplot as plt`: 기본 시각화 라이브러리
- `json`: JSON 데이터 처리를 위한 라이브러리

**2단계 (Warning 제거)**:
- `warnings` 모듈을 import하고 `filterwarnings('ignore')`를 호출합니다.
- 이렇게 하면 실행 중 발생하는 경고 메시지들을 숨길 수 있어 출력이 깔끔해집니다.

**3단계 (버전 확인)**:
- `np.__version__`: NumPy 버전 출력 (예: 2.1.3)
- `pd.__version__`: Pandas 버전 출력 (예: 2.2.3)
- 버전 확인을 통해 사용 중인 라이브러리가 최신인지 확인할 수 있습니다.

**최종 결과**:
```
numpy  version -  2.1.3
pandas version -  2.2.3
```

### 유틸리티 함수 정의

데이터 정보를 출력하는 세 가지 유틸리티 함수를 정의했습니다.

#### 1. aryInfo 함수 - NumPy 배열 정보 출력

```python
def aryInfo(ary):
    print('type - ', type(ary))
    print('shape - ', ary.shape)
    print('ndim  - ', ary.ndim)
    print('dtype - ', ary.dtype)
    print()
    print('data  -')
    print(ary)
```

#### 💻 함수 설명

**함수의 목적**: NumPy 배열의 상세 정보를 한눈에 파악할 수 있도록 출력

**출력 정보**:
- `type`: 객체의 타입 (numpy.ndarray)
- `shape`: 배열의 형태 (행, 열)
- `ndim`: 배열의 차원 수
- `dtype`: 배열 요소의 데이터 타입
- `data`: 실제 배열 데이터

#### 2. seriesInfo 함수 - Pandas Series 정보 출력

```python
def seriesInfo(s):
    print('type   - ', type(s))
    print('index  - ', s.index)
    print('values - ', s.values)
    print('dtype  - ', s.dtype)
    print()
    print('data   - ')
    print(s)
```

#### 💻 함수 설명

**함수의 목적**: Pandas Series의 상세 정보를 출력

**출력 정보**:
- `type`: 객체의 타입 (pandas.core.series.Series)
- `index`: Series의 인덱스 정보
- `values`: Series의 값들 (NumPy 배열 형태)
- `dtype`: Series 요소의 데이터 타입
- `data`: 실제 Series 데이터 (인덱스와 함께 표시)

#### 3. frmInfo 함수 - DataFrame 정보 출력

```python
def frmInfo(frm):
    print('type    - ', type(frm))
    print('shape   - ', frm.shape)
    print('ndim    - ', frm.ndim)
    print('row idx - ', frm.index, type(frm.index))
    print('col idx - ', frm.columns, type(frm.columns))
    print('values  - ', type(frm.values))
    print(frm.values)
    print('data - ')
    print(frm)
```

#### 💻 함수 설명

**함수의 목적**: DataFrame의 모든 구조적 정보를 상세하게 출력

**출력 정보**:
- `type`: 객체의 타입 (pandas.core.frame.DataFrame)
- `shape`: DataFrame의 형태 (행 개수, 열 개수)
- `ndim`: DataFrame의 차원 (항상 2)
- `row idx`: 행 인덱스와 그 타입
- `col idx`: 열 인덱스와 그 타입
- `values`: 값들의 타입과 실제 2차원 배열
- `data`: DataFrame을 표 형태로 출력

> 💡 **중요!**: 이 세 가지 함수는 강사님께서 데이터 구조를 설명하실 때 자주 사용하셨습니다. 데이터의 구조를 이해하는 데 매우 유용한 도구입니다.

---

## 📊 DataFrame 생성과 기본 조작

### 딕셔너리로 DataFrame 만들기

강사님께서 간단한 학생 성적 데이터를 예제로 사용하셨습니다.

```python
scores = {
    'kor': [90, 85, 100, 88, 78],
    'eng': [90, 85, 100, 88, 78],
    'mat': [90, 85, 100, 88, 78]
}

frm = pd.DataFrame(scores,
                   index=['강승우', '최호준', '임종섭', '이현우', '오신원'])
frmInfo(frm)
```

#### 💻 코드 실행 상세 분석

**1단계 (딕셔너리 생성)**:
- `scores` 딕셔너리를 생성합니다.
- 키(`kor`, `eng`, `mat`)는 DataFrame의 **열 이름**이 됩니다.
- 값(리스트)은 각 열의 **데이터**가 됩니다.

**2단계 (DataFrame 생성)**:
- `pd.DataFrame(scores)`: 딕셔너리를 DataFrame으로 변환합니다.
- `index` 파라미터: 행 인덱스를 지정합니다 (학생 이름).
- 딕셔너리의 키들이 자동으로 열 인덱스가 되므로 `columns` 파라미터는 생략 가능합니다.

**3단계 (DataFrame 구조 이해)**:
- 총 **5개의 행**(학생 수)이 생성됩니다.
- 총 **3개의 열**(과목 수)이 생성됩니다.
- 형태: **(5, 3)** - 5행 3열의 2차원 구조

**최종 결과**:
```
type    -  <class 'pandas.core.frame.DataFrame'>
shape   -  (5, 3)
ndim    -  2
row idx -  Index(['강승우', '최호준', '임종섭', '이현우', '오신원'], dtype='object')
col idx -  Index(['kor', 'eng', 'mat'], dtype='object')
values  -  <class 'numpy.ndarray'>
[[ 90  90  90]
 [ 85  85  85]
 [100 100 100]
 [ 88  88  88]
 [ 78  78  78]]
data - 
     kor  eng  mat
강승우   90   90   90
최호준   85   85   85
임종섭  100  100  100
이현우   88   88   88
오신원   78   78   78
```

> 📌 **노트**: 강사님께서 강조하신 중요한 점은, DataFrame을 볼 때 "행의 집합"이 아니라 **"열의 집합"**으로 바라봐야 한다는 것입니다. 딕셔너리의 각 키-값 쌍이 하나의 열(Series)을 만들고, 이러한 열들이 모여 DataFrame을 구성합니다.

### NumPy와 Pandas의 관계

강사님께서 NumPy를 배운 이유에 대해 다시 한 번 강조하셨습니다.

#### NumPy를 배운 이유

1. **배열의 개념 이해**: 1차원 배열(Vector), 2차원 배열(행렬)
2. **배열 연산의 필요성**: 벡터 연산, 행렬 연산
3. **Pandas와의 밀접한 관계**: DataFrame의 내부 데이터는 NumPy 배열

> 💡 **핵심 인사이트**: DataFrame을 이루는 데이터는 결국 **2차원 NumPy 배열**입니다. 따라서 데이터 분석을 한다는 것은 NumPy와 떼려야 뗄 수 없는 관계입니다.

---

## 🎯 퀴즈: 평균 점수 열 추가하기

강사님께서 첫 번째 퀴즈를 내주셨습니다.

### 문제

**모든 학생의 과목 평균 점수를 새로운 열로 추가하세요. 열의 이름은 'mean'입니다.**

### 축(Axis) 개념 복습

이 문제를 해결하기 위해서는 **축(axis)의 방향**에 대한 이해가 필요합니다.

- `axis=0`: **열 방향** (세로 방향)
- `axis=1`: **행 방향** (가로 방향)

학생의 과목 평균을 구한다는 것은 **각 학생마다(각 행마다)** 세 과목의 평균을 계산한다는 의미입니다. 따라서 `axis=1`을 사용해야 합니다.

### 해결 방법 1: values 속성과 NumPy 함수 사용

```python
# frm.values로 NumPy 배열 추출
print(frm.values)
```

**출력 결과**:
```
[[ 90  90  90]
 [ 85  85  85]
 [100 100 100]
 [ 88  88  88]
 [ 78  78  78]]
```

#### 💻 코드 실행 상세 분석

**1단계 (배열 추출)**:
- `frm.values`: DataFrame에서 순수 NumPy 배열만 추출합니다.
- 결과는 2차원 배열로, 인덱스 정보 없이 데이터만 포함됩니다.

**2단계 (NumPy 함수 사용)**:
```python
# axis 방향을 지정하지 않으면 전체 평균
print(np.mean(frm.values))  # 88.8

# axis=1로 행 방향 평균
print(np.mean(frm.values, axis=1))  # [90. 85. 100. 88. 78.]
```

#### 💻 코드 실행 상세 분석

**axis 파라미터 없이 실행**:
- 모든 요소를 평탄화(flatten)하여 하나의 평균값을 계산합니다.
- 결과: `88.8` (모든 점수의 전체 평균)

**axis=1로 실행**:
- 각 행별로 평균을 계산합니다.
- 결과: `[90. 85. 100. 88. 78.]` (각 학생의 평균 점수)

**axis=0으로 실행**:
- 각 열별로 평균을 계산합니다.
- 결과: 각 과목의 평균 점수

**3단계 (데이터 타입 변환)**:
```python
# 정수형으로 변환
mean = np.mean(frm.values, axis=1).astype(np.int32)
```

- `.astype(np.int32)`: 평균값을 32비트 정수로 변환합니다.
- NumPy의 `mean()` 함수는 기본적으로 float 타입을 반환하기 때문에, 필요시 정수로 변환할 수 있습니다.

### 해결 방법 2: DataFrame의 mean() 메서드 사용

```python
# DataFrame의 mean() 메서드 사용
mean = frm.mean(axis=1)
frm['mean'] = mean
frmInfo(frm)
```

#### 💻 코드 실행 상세 분석

**1단계 (평균 계산)**:
- `frm.mean(axis=1)`: DataFrame에 직접 `mean()` 메서드를 적용합니다.
- `axis=1`을 지정하여 각 행의 평균을 계산합니다.
- 결과는 Series 객체로 반환됩니다.

**2단계 (새 열 추가)**:
- `frm['mean'] = mean`: 계산된 평균값을 새로운 열로 추가합니다.
- 이미 존재하는 열 이름을 사용하면 **덮어쓰기(업데이트)**가 됩니다.

**최종 결과**:
```
     kor  eng  mat   mean
강승우   90   90   90   90.0
최호준   85   85   85   85.0
임종섭  100  100  100  100.0
이현우   88   88   88   88.0
오신원   78   78   78   78.0
```

> 💡 **중요!**: DataFrame에 새로운 열을 추가하는 것은 **열 인덱싱**을 사용하는 것입니다. `frm['mean'] = mean`은 'mean'이라는 이름의 열을 생성하고, 거기에 값을 할당하는 것입니다.

---

## 🔍 loc 인덱서를 활용한 데이터 접근

### 퀴즈: 특정 학생의 점수 수정하기

강사님께서 두 번째 퀴즈를 내주셨습니다.

**문제**: 최호준 학생의 영어 점수를 90점으로 수정하고, 평균 점수도 다시 계산하세요.

### 행 인덱싱의 두 가지 방법

DataFrame에서 특정 행의 특정 열에 접근하려면 어떻게 해야 할까요?

**방법 1: 열 먼저 접근 후 행 인덱싱**
```python
# 영어 열을 먼저 선택
eng_series = frm['eng']
# 최호준 학생의 영어 점수 접근
score = eng_series['최호준']  # 85
```

하지만 이 방법은 값을 수정할 때 주의가 필요합니다.

**방법 2: loc 인덱서 사용** (권장)
```python
frm.loc['최호준', 'eng'] = 90
```

### loc 인덱서란?

`loc[]`는 **라벨 기반 인덱싱**을 제공하는 Pandas의 인덱서입니다.

**사용 문법**:
```python
DataFrame.loc[행_라벨, 열_라벨]
```

- 행과 열의 **라벨(이름)**을 사용하여 데이터에 접근합니다.
- 슬라이싱도 가능합니다.
- 값 읽기와 쓰기 모두 가능합니다.

### 퀴즈 해결

```python
# 1. 최호준 학생의 영어 점수를 90점으로 수정
frm.loc['최호준', 'eng'] = 90

# 2. 평균 점수 다시 계산
frm.loc['최호준', 'mean'] = frm.loc['최호준', ['kor', 'eng', 'mat']].mean().astype(np.int32)

frmInfo(frm)
```

#### 💻 코드 실행 상세 분석

**1단계 (영어 점수 수정)**:
- `frm.loc['최호준', 'eng']`: '최호준' 행의 'eng' 열에 접근합니다.
- `= 90`: 해당 위치의 값을 90으로 변경합니다.

**2단계 (평균 재계산 - 복잡한 과정)**:
- `frm.loc['최호준', ['kor', 'eng', 'mat']]`: '최호준' 학생의 세 과목 점수를 Series로 가져옵니다.
  - 이때 대괄호가 이중으로 사용됨에 주목하세요: `[['kor', 'eng', 'mat']]`
  - 단일 대괄호 `['kor']`는 하나의 값을 반환하지만, 이중 대괄호 `[['kor']]`는 DataFrame 형태로 반환합니다.
- `.mean()`: 해당 Series의 평균을 계산합니다.
- `.astype(np.int32)`: 계산된 평균을 32비트 정수로 변환합니다.
- `frm.loc['최호준', 'mean'] = ...`: 계산된 평균을 'mean' 열에 저장합니다.

**최종 결과**:
```
     kor  eng  mat   mean
강승우   90   90   90   90.0
최호준   85   90   85   86.6666... → 86 (정수 변환 후)
임종섭  100  100  100  100.0
이현우   88   88   88   88.0
오신원   78   78   78   78.0
```

### loc 인덱서의 다양한 사용법

#### 1. 단일 행 접근

```python
# 이현우 학생의 모든 정보 가져오기
print(frm.loc['이현우'], type(frm.loc['이현우']))
```

**출력 결과**:
```
kor     88.000000
eng     88.000000
mat     80.000000
mean    85.333333
Name: 이현우, dtype: float64 <class 'pandas.core.series.Series'>
```

> 📌 **노트**: 단일 대괄호로 행에 접근하면 **Series 객체**가 반환됩니다.

#### 2. 행을 DataFrame으로 반환

```python
# 이중 대괄호 사용
print(frm.loc[['이현우']], type(frm.loc[['이현우']]))
```

**출력 결과**:
```
     kor  eng  mat   mean
이현우   88   88   80   85.333333
<class 'pandas.core.frame.DataFrame'>
```

> 💡 **중요!**: 이중 대괄호 `[[]]`를 사용하면 결과가 **DataFrame 객체**로 반환됩니다. 이는 여러 행을 선택할 때도 동일하게 적용됩니다.

#### 3. 임종섭 학생 데이터

```python
lim = frm.loc['임종섭']
print(lim, type(lim))
```

**출력 결과**:
```
kor     100.0
eng     100.0
mat     100.0
mean    100.0
Name: 임종섭, dtype: float64 <class 'pandas.core.series.Series'>
```

---

## 📊 실전 데이터셋 활용: Titanic Dataset

### Titanic 데이터셋 소개

강사님께서 말씀하시길, Titanic 데이터셋은 **데이터 분석 수업에서 가장 많이 사용되는 데이터**라고 하셨습니다.

#### 데이터셋 로드

```python
titanicRawData = sns.load_dataset('titanic')
print('type - ', type(titanicRawData))
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터셋 로드)**:
- `sns.load_dataset('titanic')`: Seaborn 라이브러리가 제공하는 샘플 데이터셋을 로드합니다.
- Titanic 호의 승객 정보가 담긴 DataFrame을 반환합니다.

**최종 결과**:
```
type -  <class 'pandas.core.frame.DataFrame'>
```

### 데이터 미리보기

```python
print(titanicRawData.head())
```

**출력 결과** (처음 5행):
```
   survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town alive  alone
0         0       3    male  22.0      1  ...        True   NaN  Southampton    no  False
1         1       1  female  38.0      1  ...       False     C    Cherbourg   yes  False
2         1       3  female  26.0      0  ...       False   NaN  Southampton   yes   True
3         1       1  female  35.0      1  ...       False     C  Southampton   yes  False
4         0       3    male  35.0      0  ...        True   NaN  Southampton    no   True

[5 rows x 15 columns]
```

> 📌 **노트**: `head()` 메서드는 DataFrame의 처음 5행을 보여줍니다. 파라미터로 숫자를 전달하면 해당 개수만큼의 행을 볼 수 있습니다. 예: `head(10)`

### Feature(피처)의 중요성

강사님께서 강조하신 중요한 개념:

> 💡 **핵심 개념**: 분석과 인공지능에서 **열 제목은 feature(피처) 또는 attribute(속성)**라고 부릅니다.

**Feature의 활용**:
- 별도의 피처들을 **subset(부분집합)**으로 추출하여 분석
- 선택한 피처들로 시각화 진행
- 모델 학습 시 필요한 피처만 선택

### 데이터 상세 정보 확인

```python
titanicRawData.info()
```

#### 💻 실행 결과

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
```

#### 정보 분석

**총 데이터 개수**: 891개 (승객 수)

**결측값(Null) 확인**:
- `age`: 714개 (177개 결측)
- `deck`: 203개 (688개 결측)
- `embarked`: 889개 (2개 결측)
- `embark_town`: 889개 (2개 결측)

> 💡 **중요!**: `info()` 메서드는 각 열의 Non-Null Count를 보여줍니다. 전체 데이터 개수(891)와 비교하여 결측값의 개수를 파악할 수 있습니다.

**데이터 타입**:
- `int64`: 정수형 (survived, pclass, sibsp, parch)
- `float64`: 실수형 (age, fare)
- `object`: 문자열 또는 혼합 타입 (sex, embarked, who, embark_town, alive)
- `category`: 범주형 데이터 (class, deck)
- `bool`: 불린 타입 (adult_male, alone)

---

## 🔎 데이터 탐색과 분석

### 퀴즈: 선실 등급별 인원수 확인

**문제**: 선실 등급(pclass)의 인원수를 확인하고 싶다면?

#### 1. 고유값 확인

```python
print(titanicRawData['pclass'].unique())
```

**출력 결과**:
```
[3 1 2]
```

#### 💻 코드 실행 상세 분석

**1단계 (열 선택)**:
- `titanicRawData['pclass']`: DataFrame에서 'pclass' 열을 Series로 추출합니다.

**2단계 (고유값 추출)**:
- `.unique()`: Series에 존재하는 모든 고유한(중복되지 않은) 값들을 NumPy 배열로 반환합니다.
- 순서는 데이터에 처음 나타나는 순서대로입니다.

**최종 결과**: 
- Titanic에는 1등급, 2등급, 3등급 세 가지 선실 등급이 존재합니다.

#### 2. 각 등급별 인원수 확인

```python
print(titanicRawData['pclass'].value_counts())
```

**출력 결과**:
```
3    491
1    216
2    184
Name: pclass, dtype: int64
```

#### 💻 코드 실행 상세 분석

**1단계 (열 선택)**:
- 앞선 예제와 동일하게 'pclass' 열을 선택합니다.

**2단계 (값 카운트)**:
- `.value_counts()`: 각 고유 값이 나타나는 횟수를 세어 Series로 반환합니다.
- 기본적으로 **내림차순**으로 정렬됩니다 (가장 많은 것부터).

**최종 결과**:
- 3등급: 491명 (가장 많음)
- 1등급: 216명
- 2등급: 184명 (가장 적음)

> 📌 **노트**: `value_counts()`는 범주형 데이터를 분석할 때 매우 유용한 함수입니다. 각 카테고리의 분포를 한눈에 파악할 수 있습니다.

#### 3. 값만 추출하기

```python
print(titanicRawData['pclass'].value_counts().values)
```

**출력 결과**:
```
[491 216 184]
```

#### 💻 코드 실행 상세 분석

**추가 단계 (값 추출)**:
- `.values`: Series에서 인덱스 정보를 제외하고 순수한 값들만 NumPy 배열로 추출합니다.
- 인덱스(등급 번호) 없이 개수만 필요할 때 사용합니다.

### 컬럼명 확인하기

```python
print(titanicRawData.columns)
print('type - ', type(titanicRawData.columns))
```

**출력 결과**:
```
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town', 'alive',
       'alone'], dtype='object')
type -  <class 'pandas.core.indexes.base.Index'>
```

#### 💻 코드 설명

- `.columns`: DataFrame의 모든 열 이름을 Index 객체로 반환합니다.
- Index 객체는 리스트처럼 사용할 수 있지만, 더 효율적이고 다양한 기능을 제공합니다.

---

## 🔧 데이터 조작 실습

### 퀴즈: 나이에 10살 더하기

**문제**: 기존 나이에 10살을 더해서 `age_by_10` 열을 추가하고 싶다면?

```python
titanicRawData['age_by_10'] = (titanicRawData['age'].values + 10).astype('int')
print(titanicRawData[['age', 'age_by_10']].head())
```

#### 💻 코드 실행 상세 분석

**1단계 (age 열의 값 추출)**:
- `titanicRawData['age']`: age 열을 Series로 선택합니다.
- `.values`: Series를 NumPy 배열로 변환합니다.

**2단계 (10 더하기)**:
- `+ 10`: NumPy의 브로드캐스팅 기능으로 배열의 모든 요소에 10을 더합니다.
- 결측값(NaN)에 10을 더하면 여전히 NaN입니다.

**3단계 (정수형 변환)**:
- `.astype('int')`: 결과를 정수형으로 변환합니다.
- 주의: NaN 값이 있으면 에러가 발생할 수 있습니다. 이 경우 NaN은 정수로 변환할 수 없기 때문입니다.

**4단계 (새 열 생성)**:
- `titanicRawData['age_by_10'] = ...`: 계산된 결과를 새로운 열로 추가합니다.

**최종 결과**:
```
    age  age_by_10
0  22.0         32
1  38.0         48
2  26.0         36
3  35.0         45
4  35.0         45
```

> 🔐 **보안 노트**: 나이 데이터에 산술 연산을 수행할 때는 결측값의 존재를 항상 고려해야 합니다. 결측값이 있는 상태에서 무리하게 정수 변환을 시도하면 프로그램이 중단될 수 있습니다. 실무에서는 먼저 결측값을 처리한 후 연산을 수행하는 것이 안전합니다.

### 열 삭제하기

```python
titanicRawData.drop('age_by_10', axis=1, inplace=True)
```

#### 💻 코드 실행 상세 분석

**파라미터 설명**:
- 첫 번째 인자 (`'age_by_10'`): 삭제할 열의 이름
- `axis=1`: 열을 삭제한다는 의미 (axis=0이면 행 삭제)
- `inplace=True`: 원본 DataFrame을 직접 수정 (False면 복사본 반환)

**실행 결과**:
- 'age_by_10' 열이 DataFrame에서 완전히 제거됩니다.
- `inplace=True`이므로 별도의 변수 할당 없이 원본이 변경됩니다.

> 💡 **중요!**: `inplace=True`를 사용하면 원본 데이터가 변경되므로 주의가 필요합니다. 데이터를 보존하고 싶다면 `inplace=False`(기본값)를 사용하고 결과를 새 변수에 저장하세요.

---

## 🌸 Iris Dataset 실습

### Iris 데이터셋 소개

Iris(붓꽃) 데이터셋은 기계학습에서 가장 유명한 데이터셋 중 하나입니다.

```python
irisFrm = sns.load_dataset('iris')
print('type - ', type(irisFrm))
print(irisFrm.head())
```

**출력 결과**:
```
type -  <class 'pandas.core.frame.DataFrame'>
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
```

#### 데이터셋 구조

**피처(Features)**:
- `sepal_length`: 꽃받침 길이
- `sepal_width`: 꽃받침 너비
- `petal_length`: 꽃잎 길이
- `petal_width`: 꽃잎 너비
- `species`: 붓꽃의 종류 (setosa, versicolor, virginica)

**데이터 개수**: 150개 (각 종마다 50개씩)

### 데이터 정보 확인

```python
irisFrm.info()
```

**출력 결과**:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
```

> 📌 **노트**: Iris 데이터셋은 모든 값이 Non-Null이므로 **결측값이 없는 깨끗한 데이터**입니다. 이것이 학습용으로 많이 사용되는 이유 중 하나입니다.

---

## 📋 GroupBy: 그룹별 집계의 핵심

### GroupBy의 필요성

강사님께서 GroupBy를 설명하시면서 강조하신 점:

> 💡 **핵심 개념**: GroupBy는 데이터를 특정 기준으로 그룹화하여 **각 그룹별로 집계나 연산을 수행**하는 강력한 기능입니다. 분석의 인사이트를 찾는 용도뿐만 아니라 **데이터 전처리**에서도 매우 많이 사용됩니다.

### 기본 GroupBy 예제

#### Iris 데이터를 species로 그룹화

```python
print(irisFrm.groupby('species').groups)
```

**출력 결과**:
```
{'setosa': [0, 1, 2, ..., 48, 49], 
 'versicolor': [50, 51, 52, ..., 98, 99], 
 'virginica': [100, 101, 102, ..., 148, 149]}
```

#### 💻 코드 실행 상세 분석

**1단계 (GroupBy 객체 생성)**:
- `irisFrm.groupby('species')`: 'species' 열의 값을 기준으로 그룹화합니다.
- 결과는 GroupBy 객체이며, 아직 실제 연산은 수행되지 않았습니다.

**2단계 (그룹 정보 확인)**:
- `.groups`: 각 그룹의 키(species 이름)와 해당 그룹에 속한 행의 인덱스를 딕셔너리로 반환합니다.

**최종 결과**:
- setosa 그룹: 인덱스 0~49번 행
- versicolor 그룹: 인덱스 50~99번 행
- virginica 그룹: 인덱스 100~149번 행

### GroupBy + 집계 함수

#### 종별 평균 계산

```python
print(irisFrm.groupby('species').mean())
```

**출력 결과**:
```
            sepal_length  sepal_width  petal_length  petal_width
species                                                          
setosa             5.006        3.428         1.462        0.246
versicolor         5.936        2.770         4.260        1.326
virginica          6.588        2.974         5.552        2.026
```

#### 💻 코드 실행 상세 분석

**1단계 (그룹화)**:
- `groupby('species')`: species별로 데이터를 그룹화합니다.

**2단계 (평균 계산)**:
- `.mean()`: 각 그룹의 **수치형 열들**에 대해 평균을 계산합니다.
- species 열은 문자열이므로 자동으로 제외됩니다.

**3단계 (결과 구조)**:
- 결과는 DataFrame으로 반환됩니다.
- species가 인덱스가 되고, 각 수치형 피처의 평균값이 열로 나타납니다.

**분석 결과 해석**:
- virginica 종이 평균적으로 가장 큰 꽃잎과 꽃받침을 가지고 있습니다.
- setosa 종이 평균적으로 가장 작은 꽃잎을 가지고 있습니다.

### 특정 피처만 선택하여 GroupBy

```python
print(irisFrm.groupby('species')['petal_length'].mean())
```

**출력 결과**:
```
species
setosa        1.462
versicolor    4.260
virginica     5.552
Name: petal_length, dtype: float64
```

#### 💻 코드 실행 상세 분석

**차원 축소 개념**:
- `groupby('species')`: DataFrame을 그룹화
- `['petal_length']`: 그룹화된 객체에서 특정 열만 선택
- `.mean()`: 해당 열의 평균 계산

**결과 타입**:
- Series 객체로 반환됩니다.
- 인덱스는 species, 값은 petal_length의 평균입니다.

### get_group(): 특정 그룹 추출

```python
print(irisFrm.groupby('species').get_group('setosa'))
```

**출력 결과**:
```
    sepal_length  sepal_width  petal_length  petal_width species
0            5.1          3.5           1.4          0.2  setosa
1            4.9          3.0           1.4          0.2  setosa
2            4.7          3.2           1.3          0.2  setosa
...
48           5.3          3.7           1.5          0.2  setosa
49           5.0          3.3           1.4          0.2  setosa

[50 rows x 5 columns]
```

#### 💻 코드 실행 상세 분석

**1단계 (그룹화)**:
- `groupby('species')`: species별로 그룹화합니다.

**2단계 (특정 그룹 추출)**:
- `.get_group('setosa')`: 'setosa' 그룹에 해당하는 모든 행을 DataFrame으로 반환합니다.

**활용**:
- 특정 카테고리의 데이터만 분석하고 싶을 때 유용합니다.
- 반환된 DataFrame에 추가적인 연산을 적용할 수 있습니다.

### 복합 GroupBy 예제

강사님께서 보여주신 복잡한 예제:

```python
# 1. petal_length로 정렬
# 2. species로 그룹화
# 3. setosa 그룹만 추출
result = irisFrm.sort_values(by='petal_length', ascending=False)\
                .groupby('species')\
                .get_group('setosa')
print(result)
```

**출력 결과**:
```
    sepal_length  sepal_width  petal_length  petal_width species
24           4.8          3.4           1.9          0.2  setosa
44           5.1          3.8           1.9          0.4  setosa
18           5.7          3.8           1.7          0.3  setosa
...
13           4.3          3.0           1.1          0.1  setosa
22           4.6          3.6           1.0          0.2  setosa
```

#### 💻 코드 실행 상세 분석

**1단계 (정렬)**:
- `sort_values(by='petal_length', ascending=False)`: petal_length를 기준으로 내림차순 정렬합니다.
- 이 시점에서 인덱스는 원래 순서를 유지하고 있습니다.

**2단계 (그룹화)**:
- `.groupby('species')`: 정렬된 데이터를 species별로 그룹화합니다.
- 정렬이 먼저 되었기 때문에, 각 그룹 내의 데이터도 정렬된 상태입니다.

**3단계 (그룹 추출)**:
- `.get_group('setosa')`: setosa 그룹만 추출합니다.
- petal_length가 긴 순서대로 정렬된 setosa 데이터를 얻게 됩니다.

**결과 분석**:
- 인덱스가 섞여 있는 이유: 원래 데이터의 인덱스를 유지하면서 정렬했기 때문입니다.
- 24번 인덱스의 setosa가 petal_length가 가장 긴 setosa입니다 (1.9).
- 22번 인덱스의 setosa가 petal_length가 가장 짧은 setosa입니다 (1.0).

> 💡 **중요!**: 메서드 체이닝(Method Chaining)을 사용하면 여러 연산을 순차적으로 적용할 수 있습니다. 가독성을 위해 백슬래시(`\`)로 줄을 나눌 수 있습니다.

---

## 🔧 결측값 처리: GroupBy 활용 사례

### 실전 문제 상황

강사님께서 실무적인 문제를 제시하셨습니다:

**상황**: Titanic 데이터의 'age' 열에 177개의 결측값이 있습니다.

**요구사항**: 이 결측값을 **성별에 따른 나이 평균**으로 채우고 싶습니다.
- 남성의 결측값 → 남성의 평균 나이로 채움
- 여성의 결측값 → 여성의 평균 나이로 채움

이것이 바로 **GroupBy를 데이터 전처리에 활용**하는 대표적인 사례입니다.

### 단계별 해결 과정

#### 1. 결측값 확인

```python
titanicFrm = sns.load_dataset('titanic')
print('age 결측값 - ', titanicFrm['age'].isnull().sum())
```

**출력 결과**:
```
age 결측값 -  177
```

#### 💻 코드 실행 상세 분석

**1단계 (결측값 판별)**:
- `titanicFrm['age']`: age 열을 Series로 선택합니다.
- `.isnull()`: 각 요소가 결측값(NaN)인지 판별하여 불린 Series를 반환합니다 (True/False).

**2단계 (결측값 개수 세기)**:
- `.sum()`: 불린 Series를 합산합니다 (True=1, False=0으로 계산됨).
- 결과적으로 True의 개수, 즉 결측값의 개수가 반환됩니다.

**최종 결과**:
- 총 891명의 승객 중 177명의 나이 정보가 누락되어 있습니다.

#### 2. 성별별 평균 나이 계산

```python
print(titanicFrm.groupby('sex')['age'].mean())
```

**출력 결과**:
```
sex
female    27.915709
male      30.726645
Name: age, dtype: float64
```

#### 💻 코드 실행 상세 분석

**1단계 (성별로 그룹화)**:
- `groupby('sex')`: 'sex' 열을 기준으로 데이터를 male과 female로 그룹화합니다.

**2단계 (age 열 선택)**:
- `['age']`: 그룹화된 객체에서 age 열만 선택합니다.
- 이는 차원 축소를 의미하며, 결과는 Series가 됩니다.

**3단계 (평균 계산)**:
- `.mean()`: 각 그룹의 age 평균을 계산합니다.
- 결측값(NaN)은 자동으로 제외하고 계산됩니다.

**분석 결과**:
- 여성 승객의 평균 나이: 약 27.9세
- 남성 승객의 평균 나이: 약 30.7세

#### 3. GroupBy + apply + lambda를 활용한 결측값 채우기

이 부분이 오늘 강의의 **가장 어렵고 중요한 부분**입니다.

```python
tmp = titanicFrm.groupby('sex')['age'].apply(lambda x: x.fillna(x.mean()))
print(tmp, type(tmp))
```

**출력 결과**:
```
sex
female  1      38.0
        2      26.0
        3      35.0
        8      27.0
        9      14.0
             ...
male    883    28.0
        884    25.0
        886    27.0
        889    26.0
        890    32.0
Name: age, Length: 891, dtype: float64
<class 'pandas.core.series.Series'>
```

#### 💻 코드 실행 상세 분석 (매우 중요!)

이 코드는 여러 단계로 나누어 이해해야 합니다.

**1단계 (그룹화와 열 선택)**:
- `titanicFrm.groupby('sex')['age']`: 
  - sex별로 그룹을 만들고, 각 그룹의 age 데이터만 선택합니다.
  - 이 시점에서 GroupBy 객체가 생성됩니다.

**2단계 (apply 함수의 역할 이해)**:
- `.apply(lambda x: ...)`: 
  - 각 그룹(female 그룹, male 그룹)에 대해 람다 함수를 적용합니다.
  - `x`는 **각 그룹의 age Series**를 의미합니다.
  
**3단계 (람다 함수 내부 로직)**:
- `x.fillna(x.mean())`:
  - `x.mean()`: 현재 그룹(female 또는 male)의 age 평균을 계산합니다.
  - `x.fillna(...)`: 해당 그룹의 결측값을 평균값으로 채웁니다.

**4단계 (그룹별 처리 흐름)**:

**Female 그룹 처리**:
```python
# x = female 그룹의 age Series (인덱스: [1, 2, 3, 8, 9, ...])
# x.mean() = 27.915709
# x.fillna(27.915709) 
# → female 그룹의 모든 NaN 값이 27.915709로 채워짐
```

**Male 그룹 처리**:
```python
# x = male 그룹의 age Series (인덱스: [0, 4, 5, 6, 7, ...])
# x.mean() = 30.726645
# x.fillna(30.726645)
# → male 그룹의 모든 NaN 값이 30.726645로 채워짐
```

**5단계 (결과 구조)**:
- 반환값은 **MultiIndex Series**입니다.
- 첫 번째 레벨: sex (female/male)
- 두 번째 레벨: 원래의 행 인덱스
- 값: 결측값이 채워진 나이

> 💡 **핵심 개념**: `apply` 함수는 각 그룹을 독립적으로 처리할 수 있게 해줍니다. 람다 함수의 `x`는 각 그룹의 데이터를 의미하며, 그룹 내에서 필요한 연산(평균 계산, 결측값 채우기 등)을 수행할 수 있습니다.

#### 4. 결측값이 채워진 데이터 적용

```python
titanicFrm['age'] = tmp.values
print('age 결측값 - ', titanicFrm['age'].isnull().sum())
```

**출력 결과**:
```
age 결측값 -  0
```

#### 💻 코드 실행 상세 분석

**1단계 (값 추출)**:
- `tmp.values`: Series에서 인덱스 정보를 제거하고 순수한 NumPy 배열만 추출합니다.
- MultiIndex가 제거되고 원래 순서대로 정렬된 값들이 반환됩니다.

**2단계 (age 열 업데이트)**:
- `titanicFrm['age'] = ...`: 기존 age 열을 결측값이 채워진 새로운 값으로 덮어씁니다.

**3단계 (검증)**:
- `.isnull().sum()`: 다시 결측값 개수를 확인합니다.
- 결과가 0이므로 모든 결측값이 성공적으로 채워졌습니다.

> 📌 **노트**: 강사님께서는 예전 버전에서는 이 코드가 더 간단하게 작동했다고 하셨습니다. 현재는 MultiIndex 때문에 `.values`를 사용해야 했습니다.

### GroupBy를 사용한 전처리의 장점

강사님께서 강조하신 점:

**전통적인 방법** (GroupBy 없이):
1. 성별별로 평균 나이를 계산
2. 전체 데이터를 순회하는 루프 작성
3. 각 행의 성별 확인
4. 조건문으로 남성이면 남성 평균, 여성이면 여성 평균으로 결측값 채우기

**GroupBy를 사용한 방법**:
```python
titanicFrm.groupby('sex')['age'].apply(lambda x: x.fillna(x.mean()))
```

단 한 줄로 해결!

> 💡 **중요!**: GroupBy를 이해하지 못하면 이런 간단한 코드를 작성하기 위해 상당히 복잡한 로직을 구현해야 합니다. 리스트 컴프리헨션, 삼항 연산자 등을 동원해도 코드가 복잡해질 수 있습니다.

---

## 🎨 시각화 예고

### 내일 학습 계획

강사님께서 오늘 강의를 마무리하시면서 내일 계획을 공유해주셨습니다:

**내일의 학습 내용**:
1. **시각화 문법 정리**: Matplotlib, Seaborn 기본 문법
2. **보안 데이터 시각화**: 실제 보안 로그 데이터(또는 더미 데이터)를 활용
3. **인사이트 찾기**: 데이터에서 의미 있는 패턴 발견
4. **Streamlit 실습**: 웹 기반 대시보드 만들기

> 📌 **노트**: 강사님께서는 "분석의 깊이"까지는 들어가지 않는다고 안심시켜 주셨습니다. 우리는 분석 전문가를 양성하는 과정이 아니기 때문에, 시각화에 필요한 수준의 데이터 조작만 배우게 됩니다.

### 오늘 배운 내용의 활용

시각화를 하려면 다음과 같은 과정이 필요합니다:

1. **데이터 불러오기**: CSV, JSON 등의 파일 읽기
2. **데이터 탐색**: `head()`, `info()`, `describe()` 등으로 구조 파악
3. **데이터 전처리**: 결측값 처리, 이상치 제거, 데이터 타입 변환
4. **데이터 조작**: GroupBy, 필터링, 정렬 등으로 필요한 형태로 가공
5. **시각화**: Matplotlib, Seaborn으로 그래프 생성
6. **웹 출력**: Streamlit으로 브라우저에 표시

오늘 배운 내용(1~4단계)은 시각화(5~6단계)의 기초가 됩니다.

---

## 🔐 보안 관점의 데이터 분석

### 보안 로그 데이터의 특징

시각화 예제로 보안 데이터를 사용하는 이유:

**보안 로그의 일반적인 구조**:
- 타임스탬프: 언제 발생했는가
- 소스 IP: 어디서 왔는가
- 목적지 IP: 어디로 가는가
- 심각도(Severity): 얼마나 위험한가 (low, medium, high, critical)
- 공격 유형: 어떤 종류의 공격인가 (SQL Injection, XSS, DDoS 등)

### 보안 데이터 분석 시나리오

**분석 목표 예시**:
1. 시간대별 공격 빈도 분석
2. 심각도별 공격 분포
3. 가장 많이 공격받은 IP 주소
4. 공격 유형별 통계

**필요한 데이터 조작**:
```python
# 1. 심각도별 그룹화
security_data.groupby('severity').size()

# 2. 시간대별 공격 빈도
security_data.groupby(security_data['timestamp'].dt.hour).size()

# 3. 상위 10개 공격자 IP
security_data['source_ip'].value_counts().head(10)

# 4. 심각도가 'high' 이상인 데이터만 필터링
critical_attacks = security_data[security_data['severity'].isin(['high', 'critical'])]
```

> 🔐 **보안 노트**: 실제 보안 로그를 분석할 때는 다음 사항을 고려해야 합니다:
> - **개인정보 보호**: IP 주소, 사용자 정보 등은 익명화 필요
> - **데이터 무결성**: 로그가 변조되지 않았는지 검증
> - **실시간 처리**: 대량의 로그를 빠르게 처리하는 효율성
> - **패턴 인식**: 정상 트래픽과 비정상 트래픽 구분

---

## 🧩 종합 실습 예제

### 복합 데이터 분석 시나리오

오늘 배운 내용을 모두 활용하는 종합 예제를 만들어보겠습니다.

```python
# 시나리오: Titanic 데이터로 생존율 분석

# 1. 데이터 로드 및 기본 정보 확인
titanic = sns.load_dataset('titanic')
print("전체 데이터 개수:", len(titanic))
print("\n결측값 현황:")
print(titanic.isnull().sum())

# 2. 성별, 선실 등급별 생존율 분석
survival_rate = titanic.groupby(['sex', 'pclass'])['survived'].mean()
print("\n성별, 선실 등급별 생존율:")
print(survival_rate)

# 3. 연령대별 생존율 (10세 단위로 그룹화)
titanic['age_group'] = (titanic['age'] // 10) * 10
age_survival = titanic.groupby('age_group')['survived'].mean()
print("\n연령대별 생존율:")
print(age_survival)

# 4. 결측값 처리 - 나이는 성별 평균으로, 승선지는 최빈값으로
titanic['age'] = titanic.groupby('sex')['age'].transform(lambda x: x.fillna(x.mean()))
titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)

# 5. 생존자 중 1등급 승객 추출
first_class_survivors = titanic[(titanic['pclass'] == 1) & (titanic['survived'] == 1)]
print("\n1등급 생존자 수:", len(first_class_survivors))

# 6. 가족 동반 여부에 따른 생존율
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1
titanic['has_family'] = titanic['family_size'] > 1
family_survival = titanic.groupby('has_family')['survived'].mean()
print("\n가족 동반 여부별 생존율:")
print(family_survival)
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 탐색)**:
- `len(titanic)`: 전체 데이터 개수 확인
- `isnull().sum()`: 각 열의 결측값 개수 확인
- 데이터의 전반적인 품질을 파악합니다.

**2단계 (다중 기준 그룹화)**:
- `groupby(['sex', 'pclass'])`: 두 개의 컬럼으로 그룹화
- 결과는 MultiIndex Series로 반환됩니다.
- 성별과 선실 등급의 조합별 생존율을 계산합니다.

**3단계 (파생 변수 생성)**:
- `titanic['age'] // 10`: 나이를 10으로 나눈 몫 (0-9세는 0, 10-19세는 10)
- `* 10`: 10을 곱해서 연령대를 만듦 (0, 10, 20, 30, ...)
- 새로운 열 'age_group'을 생성하여 연령대별 분석을 가능하게 합니다.

**4단계 (전처리 - 결측값 처리)**:
- `transform(lambda x: ...)`: groupby와 함께 사용하면 원래 DataFrame의 형태를 유지하면서 값을 변환
- `mode()[0]`: 최빈값(가장 자주 나타나는 값)의 첫 번째 요소
- 나이는 성별 평균으로, 승선지는 최빈값으로 채웁니다.

**5단계 (복합 조건 필터링)**:
- `&` 연산자로 여러 조건을 결합
- 1등급이면서 생존한 승객만 추출합니다.

**6단계 (새로운 인사이트 발견)**:
- `sibsp`: 함께 탑승한 형제자매/배우자 수
- `parch`: 함께 탑승한 부모/자녀 수
- `family_size`: 본인 포함 가족 구성원 수
- 혼자 탑승했는지, 가족과 함께 탑승했는지에 따른 생존율 차이를 분석합니다.

**예상 출력**:
```
전체 데이터 개수: 891

결측값 현황:
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
...

성별, 선실 등급별 생존율:
sex     pclass
female  1         0.968085
        2         0.921053
        3         0.500000
male    1         0.368852
        2         0.157407
        3         0.135447
Name: survived, dtype: float64

연령대별 생존율:
age_group
0.0     0.612903
10.0    0.401869
20.0    0.365079
30.0    0.445652
40.0    0.383721
50.0    0.404255
60.0    0.240000
70.0    0.200000
Name: survived, dtype: float64

1등급 생존자 수: 136

가족 동반 여부별 생존율:
has_family
False    0.303538
True     0.505650
Name: survived, dtype: float64
```

**분석 인사이트**:
1. 여성의 생존율이 남성보다 훨씬 높습니다 (특히 1, 2등급).
2. 선실 등급이 높을수록 생존율이 높습니다.
3. 가족과 함께 탑승한 승객의 생존율이 더 높습니다.
4. 연령대별로는 어린이(0-10세)와 30대의 생존율이 상대적으로 높습니다.

> 💡 **중요!**: 이러한 분석 결과는 시각화를 통해 더욱 명확하게 전달할 수 있습니다. 내일 배울 Matplotlib과 Seaborn을 사용하면 이 데이터를 막대 그래프, 히트맵, 박스플롯 등 다양한 형태로 표현할 수 있습니다.

---

## 📚 오늘 배운 주요 개념 정리

### DataFrame 조작의 핵심

1. **인덱싱 방법**:
   - 기본 인덱싱: `df['column']` (열 선택, Series 반환)
   - `loc[]`: 라벨 기반 인덱싱
   - `iloc[]`: 정수 기반 인덱싱

2. **축(Axis) 개념**:
   - `axis=0`: 열 방향 (세로, 행 단위 연산)
   - `axis=1`: 행 방향 (가로, 열 단위 연산)

3. **GroupBy 연산**:
   - 그룹화: `df.groupby('column')`
   - 집계 함수: `mean()`, `sum()`, `count()`, `size()` 등
   - 그룹 추출: `get_group('group_name')`
   - 함수 적용: `apply(lambda x: ...)`

4. **결측값 처리**:
   - 확인: `isnull()`, `notnull()`
   - 제거: `dropna()`
   - 채우기: `fillna(value)`
   - 그룹별 채우기: `groupby().apply(lambda x: x.fillna(...))`

### 데이터 분석 워크플로우

```
데이터 로드
    ↓
기본 정보 확인 (head, info, describe)
    ↓
결측값 확인 및 처리
    ↓
필요한 피처 선택
    ↓
데이터 변환 및 파생 변수 생성
    ↓
그룹화 및 집계
    ↓
필터링 및 정렬
    ↓
시각화 (다음 강의)
```

---

## 💡 학습 팁과 실무 조언

### 강사님의 조언

1. **NumPy의 중요성**:
   - Pandas의 모든 연산은 내부적으로 NumPy를 사용합니다.
   - NumPy의 브로드캐스팅, 축 개념을 이해하면 Pandas가 훨씬 쉬워집니다.

2. **GroupBy는 어렵습니다**:
   - 강사님도 "어렵다"고 인정하셨습니다.
   - 하지만 실무에서 매우 자주 사용됩니다.
   - 다양한 예제를 직접 실행해보면서 익숙해지는 것이 중요합니다.

3. **전처리의 중요성**:
   - 데이터 분석의 80%는 전처리입니다.
   - 깨끗한 데이터가 좋은 분석 결과를 만듭니다.
   - 결측값, 이상치, 데이터 타입 등을 항상 체크하세요.

4. **문서화와 주석**:
   - 복잡한 GroupBy 코드는 주석을 남기세요.
   - 3개월 후에 자신이 쓴 코드를 이해하지 못하는 경우가 많습니다.

### 추천 학습 자료

강사님께서는 노션에 NumPy와 Pandas 관련 요약 시트를 올려두셨다고 하셨습니다. 해당 자료를 참고하면 오늘 배운 내용을 간단하게 정리할 수 있습니다.

---

## 🔍 자주 하는 실수와 해결 방법

### 실수 1: axis 혼동

**잘못된 코드**:
```python
# 각 학생의 평균을 구하고 싶은데 axis=0을 사용
mean = frm.mean(axis=0)  # 각 과목의 평균이 나옴
```

**올바른 코드**:
```python
# 각 학생의 평균을 구하려면 axis=1
mean = frm.mean(axis=1)  # 각 학생의 평균이 나옴
```

**해결 방법**: 
- axis=0은 "열을 따라서" (세로로 내려가면서) 연산
- axis=1은 "행을 따라서" (가로로 가면서) 연산
- 헷갈리면 결과를 출력해보고 확인하세요.

### 실수 2: inplace 누락

**잘못된 코드**:
```python
# drop을 했는데 열이 안 사라짐
df.drop('column', axis=1)
print(df.columns)  # 여전히 'column'이 있음
```

**올바른 코드**:
```python
# inplace=True를 추가하거나
df.drop('column', axis=1, inplace=True)

# 또는 결과를 다시 할당
df = df.drop('column', axis=1)
```

### 실수 3: 결측값이 있는 상태에서 연산

**문제가 되는 코드**:
```python
# 결측값이 있는데 astype으로 정수 변환
df['age_int'] = df['age'].astype(int)  # Error 발생 가능
```

**올바른 코드**:
```python
# 먼저 결측값을 처리
df['age'].fillna(df['age'].mean(), inplace=True)
# 그 다음에 변환
df['age_int'] = df['age'].astype(int)
```

### 실수 4: 체이닝 시 복사본 문제

**문제가 될 수 있는 코드**:
```python
# 필터링 후 값 수정
df[df['age'] > 30]['age'] = 25  # SettingWithCopyWarning
```

**올바른 코드**:
```python
# loc를 사용하여 명확하게 지정
df.loc[df['age'] > 30, 'age'] = 25
```

> 🔐 **보안 노트**: 데이터를 조작할 때는 항상 원본 데이터의 백업을 유지하세요. 특히 `inplace=True`를 사용할 때는 실수로 중요한 데이터를 잃을 수 있습니다. 중요한 작업 전에는 `df.copy()`로 복사본을 만들어두는 것이 안전합니다.

---

## 📝 오늘의 실습 과제 (자율)

강사님께서 직접 과제를 내주시지는 않았지만, 오늘 배운 내용을 복습하기 위한 실습 문제를 만들어보았습니다:

### 과제 1: Iris 데이터 분석

```python
# 1. Iris 데이터를 로드하고 기본 정보를 확인하세요.
# 2. 각 species별 모든 피처의 평균, 최대값, 최소값을 계산하세요.
# 3. petal_length가 4.0 이상인 데이터만 추출하세요.
# 4. sepal_length를 기준으로 5개 구간으로 나누고, 각 구간별 species 분포를 확인하세요.
```

### 과제 2: Titanic 데이터 심화 분석

```python
# 1. 나이와 운임(fare)의 결측값을 적절한 방법으로 채우세요.
# 2. 각 승선지(embark_town)별 생존율을 계산하세요.
# 3. 30세 이상 남성 승객 중 3등급인 사람들의 생존율을 구하세요.
# 4. sibsp와 parch를 합쳐서 family_size를 만들고, 
#    가족 크기가 생존에 미친 영향을 분석하세요.
```

### 과제 3: 복합 데이터 조작

```python
# 학생 성적 데이터를 만들고 다음을 수행하세요:
# 1. 5명의 학생, 3개 과목의 성적 DataFrame 생성
# 2. 각 학생의 평균 점수를 새로운 열로 추가
# 3. 평균이 가장 높은 학생과 가장 낮은 학생의 정보 출력
# 4. 특정 과목의 점수를 상대평가(A, B, C등급)로 변환
# 5. 등급별 학생 수를 계산
```

---

## 🎓 마무리 및 다음 강의 예고

### 오늘 배운 내용의 의의

오늘은 **데이터 프레임을 자유자재로 조작**하는 방법을 배웠습니다. 특히:

1. **loc 인덱서**: 특정 행과 열의 데이터를 정확하게 접근
2. **축(axis) 개념**: 행 방향과 열 방향 연산의 차이 이해
3. **GroupBy**: 가장 강력한 데이터 집계 도구
4. **전처리**: 결측값을 그룹별로 지능적으로 처리

이러한 기술들은 **모든 데이터 분석 작업의 기초**가 됩니다.

### 내일 학습 내용

강사님께서 예고하신 내일의 학습 주제:

1. **Matplotlib 기본 문법**:
   - Figure와 Axes 개념
   - 다양한 그래프 종류 (선 그래프, 막대 그래프, 산점도 등)

2. **Seaborn 활용**:
   - 통계 시각화
   - 히트맵, 박스플롯, 바이올린 플롯

3. **Streamlit**:
   - Python 파일로 웹 앱 만들기
   - 브라우저에서 인터랙티브 대시보드 구현

4. **보안 데이터 시각화**:
   - 실제 보안 로그 데이터 (또는 더미) 분석
   - 시간대별, 유형별, 심각도별 공격 시각화

> 📌 **노트**: 강사님께서 다시 한 번 강조하셨습니다. "분석의 깊이까지는 들어가지 않습니다." 우리의 목표는 데이터를 시각화하고 기본적인 인사이트를 찾는 것이지, 전문 데이터 분석가가 되는 것이 아닙니다.

### 강사님의 격려

강의를 마무리하시면서 강사님께서 하신 말씀:

"GroupBy가 어렵죠? 당연히 어렵습니다. 저도 처음 배울 때 정말 어려웠어요. 하지만 실무에서 계속 사용하다 보면 익숙해집니다. 오늘 여러분들이 '아, 이런 게 있구나' 정도만 알아가셔도 충분합니다. 나중에 필요할 때 '아, 그때 배웠던 GroupBy를 쓰면 되겠다'고 생각하실 수 있으면 성공입니다."

---

## 📖 추가 학습 자료 및 참고 링크

### 공식 문서

- **Pandas 공식 문서**: https://pandas.pydata.org/docs/
- **NumPy 공식 문서**: https://numpy.org/doc/
- **Seaborn 공식 문서**: https://seaborn.pydata.org/

### 유용한 치트시트

강사님께서 노션에 올려주신 자료 외에도:
- Pandas 치트시트: 주요 함수와 메서드를 한눈에 정리
- NumPy 치트시트: 배열 연산과 인덱싱 방법 정리

### 연습 데이터셋

Seaborn이 제공하는 샘플 데이터셋 목록:
```python
import seaborn as sns
print(sns.get_dataset_names())
```

**추천 데이터셋**:
- `titanic`: 생존 예측 (분류)
- `iris`: 종 분류
- `tips`: 팁 예측 (회귀)
- `planets`: 행성 데이터
- `flights`: 시계열 데이터

---

## 🎯 핵심 요약

### 오늘의 핵심 5가지

1. **DataFrame = 열(Series)의 집합**: 행이 아닌 열의 관점으로 바라보기
2. **loc[행, 열]**: 라벨 기반 인덱싱으로 정확한 데이터 접근
3. **axis=0(열), axis=1(행)**: 축 방향을 정확히 이해하고 사용
4. **GroupBy**: 그룹별 집계와 전처리의 핵심 도구
5. **결측값 처리**: 그룹별 평균으로 지능적으로 채우기

### 반드시 기억할 코드 패턴

```python
# 1. DataFrame 생성
df = pd.DataFrame(data_dict, index=row_labels)

# 2. 정확한 데이터 접근
value = df.loc[row_label, col_label]

# 3. 새 열 추가
df['new_column'] = calculated_values

# 4. 그룹별 집계
df.groupby('category')['value'].mean()

# 5. 결측값 그룹별 채우기
df.groupby('group')['column'].apply(lambda x: x.fillna(x.mean()))
```

---

## 🙏 마치며

오늘 강의에서는 데이터 프레임을 본격적으로 다루는 방법을 배웠습니다. loc 인덱서, axis 개념, GroupBy 연산 등 처음에는 어려울 수 있지만, 데이터 분석의 핵심이 되는 내용들입니다.

특히 GroupBy를 활용한 결측값 처리는 실무에서 매우 자주 사용되는 패턴입니다. 성별별, 등급별, 카테고리별로 다른 방식으로 데이터를 처리해야 하는 상황이 빈번하기 때문입니다.

내일은 드디어 시각화를 배웁니다! 오늘 고생스럽게 준비한 데이터를 아름답고 의미 있는 그래프로 표현하는 방법을 배우게 됩니다. Matplotlib과 Seaborn을 활용하여 다양한 차트를 만들고, Streamlit으로 웹 대시보드까지 만들어볼 예정입니다.

강사님께서 하신 말씀처럼, "힘들다, 나 힘들다 일수록 더 웃어볼 수 있도록" 하면서 즐겁게 학습합시다! 😊

---

**강의 노트 작성 완료 시각**: 2025년 11월 5일
**작성자**: Day 3 강의 참석 학생
**다음 강의**: Day 4 - 데이터 시각화 (Matplotlib, Seaborn, Streamlit)

> 📌 **노트**: 이 강의 노트는 11월 5일 강의 내용을 바탕으로 작성되었습니다. 강사님께서 제공하신 코드 파일들(numpy_python_day03.py, security_numpy_pandas_day03.ipynb)의 모든 내용이 포함되어 있으며, STT 파일의 강의 내용도 충실히 반영되었습니다. 복습 시 참고하시고, 이해가 안 되는 부분은 직접 코드를 실행해보면서 익히시기 바랍니다.
