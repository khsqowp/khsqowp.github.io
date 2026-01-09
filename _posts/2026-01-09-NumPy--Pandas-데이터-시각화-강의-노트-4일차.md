---
title: "NumPy  Pandas 데이터 시각화 강의 노트 4일차"
date: 2026-01-09
permalink: /posts/2026/01/09/NumPy--Pandas-데이터-시각화-강의-노트-4일차/
tags:
  - Python
  - SK_Rookies
---

# 📝 NumPy & Pandas 데이터 시각화 강의 노트 (4일차)

**날짜:** 2025년 11월 6일 (수요일)  
**주제:** Matplotlib, Seaborn을 활용한 데이터 시각화 및 탐색적 데이터 분석 (EDA)

---

## 📌 학습 내용 복습

3일차까지 NumPy와 Pandas의 기본적인 데이터 분석 기능들을 학습했습니다. 오늘은 그 데이터들을 효과적으로 **시각화(Visualization)** 하는 방법을 배웠습니다. 강사님께서 강조하신 것처럼, 프로그래밍 언어 학습은 "끊어지는 부분이 없이 연속성을 가지고 계속 연결된다"는 점이 중요합니다. 어제 배운 데이터 분석 기술이 오늘의 시각화로 이어지고, 이것이 다시 AI/ML로 연결되는 흐름을 이해하는 것이 핵심입니다.

---

## 🎯 오늘의 학습 목표

오늘 학습의 핵심 목표는 **시각화(Visualization)** 입니다. 구체적으로 다음 내용들을 배웠습니다:

### 시각화 패키지
- **Matplotlib**: 파이썬의 가장 기본적이고 강력한 시각화 라이브러리
- **Seaborn**: Matplotlib을 기반으로 한 통계적 시각화 라이브러리
- **Folium**: 지도 시각화 전문 라이브러리 (추후 학습 예정)

### 서브 패키지
- **pyplot**: Matplotlib의 핵심 플로팅 인터페이스
- **plotly**: 인터랙티브 시각화를 위한 패키지

### 웹 시각화
- **Streamlit**: 웹 기반 데이터 앱 구축 도구 (추후 VSCode에서 실습 예정)

💡 **중요!**: 강사님께서 "시각화를 하기 전에 분석이 필요하다"고 강조하셨습니다. 로우 데이터(Raw Data)를 그대로 시각화하는 것은 어렵기 때문에, 탐색적 데이터 분석(EDA)이나 통계 분석을 통해 데이터를 먼저 정제하고 분석한 후 시각화를 진행해야 합니다.

---

## 🛠️ 환경 설정

### 필수 라이브러리 Import

오늘 강의에서 사용한 기본 라이브러리들입니다:

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# warning 제거 (불필요한 경고 메시지 숨기기)
import warnings
warnings.filterwarnings('ignore')

# 버전 확인
print('numpy version - ', np.__version__)
print('pandas version - ', pd.__version__)
```

#### 💻 코드 실행 상세 분석

**1단계 (라이브러리 임포트):**
- `numpy`는 `np`라는 별칭으로 임포트되어 수치 연산에 사용됩니다
- `pandas`는 `pd`라는 별칭으로 임포트되어 데이터프레임 작업에 사용됩니다
- `seaborn`은 `sns`라는 별칭으로 임포트되어 통계적 시각화에 사용됩니다
- `matplotlib.pyplot`은 `plt`라는 별칭으로 임포트되어 기본 플로팅 작업에 사용됩니다

**2단계 (경고 필터링):**
- `warnings.filterwarnings('ignore')`를 통해 불필요한 경고 메시지를 숨깁니다
- 이는 실습 환경에서 코드를 깔끔하게 실행하기 위함입니다

**3단계 (버전 확인):**
- `__version__` 속성을 통해 각 라이브러리의 버전을 확인합니다
- 버전 호환성 문제를 사전에 파악할 수 있습니다

---

### 한글 폰트 문제 해결

시각화를 할 때 한글이 깨지는 문제를 해결하기 위한 설정입니다:

```python
# 한글 폰트 문제 해결
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

# 차트 축 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
```

#### 💻 코드 실행 상세 분석

**1단계 (플랫폼 감지):**
- `platform.system()`을 통해 현재 운영체제를 확인합니다
- 'Darwin'은 macOS, 'Windows'는 윈도우를 의미합니다

**2단계 (폰트 설정):**
- macOS의 경우 'AppleGothic' 폰트를 사용합니다
- Windows의 경우 'malgun.ttf'(맑은 고딕) 폰트를 사용합니다
- `font_manager.FontProperties`를 통해 폰트 파일의 이름을 가져옵니다

**3단계 (음수 부호 처리):**
- `axes.unicode_minus = False`를 설정하여 음수 부호(-)가 정상적으로 표시되도록 합니다
- 이 설정이 없으면 음수 표시 시 깨질 수 있습니다

**최종 결과:**
- 이제 그래프의 제목, 축 레이블, 범례 등에서 한글이 정상적으로 표시됩니다

📌 **노트**: 강사님께서 이 코드를 톡으로 공유해주셨고, 매 실습마다 첫 번째 셀에서 이 설정을 실행하도록 권장하셨습니다.

---

### 데이터 정보 출력 헬퍼 함수

3일차부터 사용해온 데이터 확인용 유틸리티 함수들입니다:

```python
def aryInfo(ary):
    """NumPy 배열 정보 출력 함수"""
    print('type  - ', type(ary))
    print('shape - ', ary.shape)
    print('ndim  - ', ary.ndim)
    print('dtype - ', ary.dtype)
    print()
    print('data  -')
    print(ary)

def seriesInfo(s):
    """Pandas Series 정보 출력 함수"""
    print('type   - ', type(s))
    print('index  - ', s.index)
    print('values - ', s.values)
    print('dtype  - ', s.dtype)
    print()
    print('data   - ')
    print(s)

def frmInfo(frm):
    """Pandas DataFrame 정보 출력 함수"""
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

#### 💻 코드 실행 상세 분석

이 헬퍼 함수들은 데이터의 구조를 빠르게 파악하기 위한 도구입니다:

**aryInfo 함수:**
- NumPy 배열의 타입, 형상(shape), 차원(ndim), 데이터 타입(dtype)을 순차적으로 출력합니다
- 마지막에 실제 데이터 값을 출력하여 전체적인 구조를 한눈에 파악할 수 있습니다

**seriesInfo 함수:**
- Pandas Series의 인덱스, 값, 데이터 타입을 확인합니다
- Series는 1차원 데이터 구조이므로 인덱스와 값의 관계가 중요합니다

**frmInfo 함수:**
- DataFrame의 행 인덱스, 열 인덱스(컬럼명)를 확인합니다
- `values` 속성을 통해 NumPy 배열 형태로 변환된 데이터를 확인할 수 있습니다

---

## 📊 시각화의 기본: Matplotlib 기초

### 1. 기본 문법 구조

Matplotlib을 사용한 시각화의 가장 기본적인 패턴입니다:

```python
plt.figure()    # 그림판 생성
plt.plot([1,2,3,4,5,6,7,8,9])   # 그림 그리기
plt.show()      # 그림 표시
plt.close()     # 그림판 닫기
```

#### 💻 코드 실행 상세 분석

**1단계 (그림판 생성):**
- `plt.figure()`를 호출하면 새로운 그림판(Figure)이 생성됩니다
- 기본 크기는 640x480 픽셀입니다
- 이 그림판은 우리가 그림을 그릴 캔버스 역할을 합니다

**2단계 (데이터 플로팅):**
- `plt.plot()`에 리스트 `[1,2,3,4,5,6,7,8,9]`를 전달합니다
- y축 값만 제공하면 x축은 자동으로 0부터 순차적으로 할당됩니다
- 따라서 (0,1), (1,2), (2,3), ..., (8,9)의 점들이 연결된 라인이 그려집니다

**3단계 (그림 표시):**
- `plt.show()`를 호출하면 생성한 그래프가 화면에 표시됩니다
- Jupyter Notebook에서는 자동으로 표시되지만, 일반 Python 스크립트에서는 반드시 호출해야 합니다

**4단계 (리소스 정리):**
- `plt.close()`를 호출하여 그림판을 닫고 메모리를 해제합니다
- 여러 그래프를 연속으로 그릴 때 이전 그래프가 겹치지 않도록 하는 역할도 합니다

**최종 결과:**
- 대각선 형태의 라인 그래프가 생성됩니다 (1부터 9까지 순차적으로 증가)

💡 **중요!**: 강사님께서 "그림판을 하나 만들고, 그림을 그리고, 쇼를 하고, 클로즈 시켜주는 작업이 일반적"이라고 강조하셨습니다. 이 4단계 패턴이 시각화의 기본 뼈대입니다.

---

### 2. 다양한 스타일의 라인 플롯

동일한 데이터를 다른 방식으로 시각화해봅니다:

```python
plt.figure()
plt.plot([1, 4, 9, 5, 7, 2, 7, 9])
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**데이터 패턴 분석:**
- 이번에는 `[1, 4, 9, 5, 7, 2, 7, 9]`라는 불규칙한 값을 사용합니다
- 그래프는 1→4로 상승, 4→9로 급상승, 9→5로 하락, 5→7로 상승, 7→2로 급하락, 2→7로 급상승, 7→9로 상승하는 꺾은선 형태가 됩니다

**최종 결과:**
- 데이터의 변화 패턴이 시각적으로 명확하게 드러납니다
- 이를 통해 데이터의 추세, 변동성, 이상치 등을 빠르게 파악할 수 있습니다

📌 **노트**: 강사님께서 "1 4 5 6 이런 식의 그림 그려낼 수 있는 형태, 이게 이제 기본 선 그래프"라고 설명하셨습니다.

---

### 3. X축과 Y축을 명시적으로 지정한 플롯

이번에는 x축과 y축을 모두 명시적으로 지정하고, 시각적 옵션도 추가합니다:

```python
plt.figure()
plt.plot([10, 30, 60, 90], [1, 4, 9, 16], 
         color='red', 
         marker='o', 
         ms=15)

plt.title('라인 플롯')
plt.xlabel('X 축')
plt.ylabel('Y 축', rotation=45)
plt.xlim(0, 100)
plt.ylim(0, 17)
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 플로팅):**
- `plt.plot()`의 첫 번째 인자 `[10, 30, 60, 90]`은 x축 값입니다
- 두 번째 인자 `[1, 4, 9, 16]`은 y축 값입니다
- 따라서 (10,1), (30,4), (60,9), (90,16) 네 개의 점이 플로팅됩니다

**2단계 (시각적 옵션 설정):**
- `color='red'`: 선의 색상을 빨간색으로 지정합니다
- `marker='o'`: 각 데이터 포인트에 원형 마커를 표시합니다
- `ms=15`: 마커 사이즈(marker size)를 15로 설정합니다 (ms는 markersize의 약자)

**3단계 (그래프 꾸미기):**
- `plt.title('라인 플롯')`: 그래프 상단에 제목을 추가합니다
- `plt.xlabel('X 축')`: x축 레이블을 추가합니다
- `plt.ylabel('Y 축', rotation=45)`: y축 레이블을 추가하고 45도 회전시킵니다

**4단계 (축 범위 설정):**
- `plt.xlim(0, 100)`: x축의 범위를 0부터 100까지로 제한합니다
- `plt.ylim(0, 17)`: y축의 범위를 0부터 17까지로 제한합니다
- 리밋을 설정하지 않으면 데이터 범위에 맞춰 자동으로 조정됩니다

**최종 결과:**
- 빨간색 선으로 연결된 4개의 원형 마커가 표시됩니다
- 제목과 축 레이블이 명확하게 표시되어 그래프의 의미를 쉽게 파악할 수 있습니다
- x축은 0-100, y축은 0-17 범위로 제한되어 여백이 생깁니다

💡 **중요!**: `rotation` 파라미터는 텍스트를 회전시킬 때 사용합니다. 강사님께서 y축 레이블이 누워있을 때 이를 회전시켜 가독성을 높이는 방법으로 소개하셨습니다.

---

## 🎨 서브플롯(Subplot): 한 화면에 여러 그래프 그리기

복잡한 데이터를 분석할 때는 여러 그래프를 동시에 비교해야 할 때가 많습니다. Matplotlib의 **서브플롯(Subplot)** 기능을 사용하면 한 화면에 여러 개의 그래프를 배치할 수 있습니다.

### 1. 서브플롯 기본 구조

```python
fig = plt.figure(figsize=(20, 7))

# 1행 3열 레이아웃의 첫 번째 위치
area01 = fig.add_subplot(1, 3, 1)
area01.set_title('타이틀')
area01.set_xlabel('X 축')
area01.set_ylabel('Y 축', rotation=0)

# 1행 3열 레이아웃의 두 번째 위치
area02 = fig.add_subplot(1, 3, 2)
area02.set_title('타이틀')
area02.set_xlabel('X 축')
area02.set_ylabel('Y 축', rotation=0)

# 1행 3열 레이아웃의 세 번째 위치
area03 = fig.add_subplot(1, 3, 3)
area03.set_title('타이틀')
area03.set_xlabel('X 축')
area03.set_ylabel('Y 축', rotation=0)

plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (Figure 객체 생성):**
- `plt.figure(figsize=(20, 7))`로 그림판을 생성하고 변수 `fig`에 저장합니다
- `figsize=(20, 7)`은 가로 20, 세로 7 단위의 크기를 의미합니다 (픽셀 단위는 아닙니다)
- 강사님께서 "2700픽셀 정도로 만들어지는 거 보이세요?"라고 말씀하셨습니다

**2단계 (첫 번째 서브플롯 생성):**
- `fig.add_subplot(1, 3, 1)`: 1행 3열 그리드의 첫 번째 위치에 서브플롯을 생성합니다
- 첫 번째 인자 `1`: 행(row) 개수
- 두 번째 인자 `3`: 열(column) 개수
- 세 번째 인자 `1`: 위치 (1번째 칸)
- 생성된 서브플롯 객체를 `area01` 변수에 저장합니다

**3단계 (첫 번째 서브플롯 꾸미기):**
- `set_title()`: 일반 `plt.title()`과 달리 서브플롯에서는 `set_` 접두사를 사용합니다
- `set_xlabel()`, `set_ylabel()`: 마찬가지로 `set_` 접두사를 붙입니다
- `rotation=0`: y축 레이블을 수평으로 표시합니다

**4단계 (두 번째, 세 번째 서브플롯):**
- `fig.add_subplot(1, 3, 2)`: 동일한 1행 3열 그리드의 2번째 위치
- `fig.add_subplot(1, 3, 3)`: 동일한 1행 3열 그리드의 3번째 위치
- 각각의 서브플롯에 동일한 방식으로 제목과 축 레이블을 설정합니다

**최종 결과:**
- 가로로 3개의 그래프 영역이 나란히 배치됩니다
- 각 영역에는 제목과 축 레이블이 표시됩니다
- 그리드 선이 기본적으로 표시될 수 있습니다 (설정에 따라 다름)

💡 **중요!**: 서브플롯을 사용할 때는 반드시 `plt.title()` 대신 `set_title()`을, `plt.xlabel()` 대신 `set_xlabel()`을 사용해야 합니다. 강사님께서 "서브플롯이기 때문에 그 해당 영역에서 이 `set`이라는 프리픽스를 붙여서 타이틀을 붙여주는 이런 형식을 쓰셔야 돼요"라고 강조하셨습니다.

---

### 2. 다양한 레이아웃의 서브플롯

1행 3열 외에도 다양한 배치가 가능합니다:

```python
fig = plt.figure(figsize=(20, 7))

# 2행 2열 레이아웃
area01 = fig.add_subplot(2, 2, 1)   # 1행 1열
area02 = fig.add_subplot(2, 2, 2)   # 1행 2열
area03 = fig.add_subplot(2, 2, 3)   # 2행 1열
area04 = fig.add_subplot(2, 2, 4)   # 2행 2열

plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**레이아웃 이해하기:**
- `add_subplot(2, 2, 1)`: 2행 2열 그리드의 1번째 위치 (왼쪽 상단)
- `add_subplot(2, 2, 2)`: 2행 2열 그리드의 2번째 위치 (오른쪽 상단)
- `add_subplot(2, 2, 3)`: 2행 2열 그리드의 3번째 위치 (왼쪽 하단)
- `add_subplot(2, 2, 4)`: 2행 2열 그리드의 4번째 위치 (오른쪽 하단)

**위치 번호 규칙:**
- 위치 번호는 왼쪽에서 오른쪽으로, 위에서 아래로 순차적으로 매겨집니다
- 1행 3열이면 1, 2, 3 순서
- 2행 2열이면 1(1행1열), 2(1행2열), 3(2행1열), 4(2행2열) 순서

**최종 결과:**
- 화면이 2×2 격자로 분할되어 4개의 그래프 영역이 생성됩니다
- 각 영역에 독립적으로 그래프를 그릴 수 있습니다

📌 **노트**: 강사님께서 "포지션이 되는 거기 때문에 그것만 맞춰 주시면 되고요"라고 설명하시며, 레이아웃 구조만 이해하면 자유롭게 배치할 수 있다고 하셨습니다.

---

## 📊 바 차트(Bar Chart): 범주형 데이터 시각화

바 차트는 **범주형(Categorical) 데이터**를 시각화할 때 사용합니다. x축이 카테고리(예: 남자/여자, 1등급/2등급/3등급)일 때 효과적입니다.

### 1. 타이타닉 데이터셋 로드

```python
titanicFrm = sns.load_dataset('titanic')
print(titanicFrm.head())
print(titanicFrm['class'].value_counts())
titanicFrm.info()
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터셋 로드):**
- `sns.load_dataset('titanic')`은 Seaborn에 내장된 타이타닉 데이터셋을 로드합니다
- 타이타닉 호 침몰 사건의 승객 정보가 담긴 실제 역사적 데이터입니다
- 총 891명의 승객 데이터가 포함되어 있습니다

**2단계 (데이터 미리보기):**
- `head()` 메서드로 상위 5개 행을 확인합니다
- 출력 결과:
  ```
  survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town alive  alone
  0       0       3    male  22.0      1  ...        True   NaN  Southampton    no  False
  1       1       1  female  38.0      1  ...       False     C    Cherbourg   yes  False
  2       1       3  female  26.0      0  ...       False   NaN  Southampton   yes   True
  3       1       1  female  35.0      1  ...       False     C  Southampton   yes  False
  4       0       3    male  35.0      0  ...        True   NaN  Southampton    no   True
  ```

**3단계 (범주형 컬럼 확인):**
- `value_counts()`로 'class' 컬럼의 빈도를 확인합니다
- 출력 결과:
  ```
  class
  Third     491
  First     216
  Second    184
  Name: count, dtype: int64
  ```
- 3등석 승객이 가장 많고(491명), 1등석(216명), 2등석(184명) 순입니다

**4단계 (데이터 타입 확인):**
- `info()` 메서드로 각 컬럼의 데이터 타입을 확인합니다
- 주요 컬럼:
  - `survived` (int64): 생존 여부 (0=사망, 1=생존)
  - `pclass` (int64): 선실 등급 (1, 2, 3)
  - `sex` (object): 성별
  - `age` (float64): 나이
  - `class` (category): 선실 등급 (범주형)
  - `deck` (category): 갑판 위치 (범주형)

**최종 결과:**
- 타이타닉 데이터셋이 메모리에 로드되어 분석 준비가 완료됩니다
- 범주형 데이터(`category` 타입)를 바 차트로 시각화할 수 있는 상태가 됩니다

💡 **중요!**: 강사님께서 "카테고리라고 되어 있었던 거 기억하십니까? 성별 남자 여자, 선실 등급 1등급 2등급 3등급, 얘네들이 전부 다 범주 타입"이라고 설명하셨습니다. **범주형 데이터**는 바 차트의 x축으로 사용하기에 적합합니다.

---

### 2. 선실 등급별 생존자 수 시각화

이제 타이타닉 데이터를 분석하여 선실 등급별 생존자 수를 바 차트로 시각화합니다:

```python
# 선실 등급별 생존자 합계 계산
surviveByClass = titanicFrm.groupby('pclass')['survived'].sum()
print(surviveByClass)

# 바 차트 그리기
plt.figure(figsize=(15, 5))
plt.bar(surviveByClass.index, surviveByClass.values, 
        color=['red', 'green', 'blue'])
plt.xticks(surviveByClass.index)
plt.title('선실 등급별 생존자 수')
plt.xlabel('선실 등급')
plt.ylabel('생존자 수')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 그룹화 및 집계):**
- `groupby('pclass')`: 'pclass' 컬럼(선실 등급)을 기준으로 그룹화합니다
- `['survived']`: 'survived' 컬럼만 선택합니다
- `.sum()`: 각 그룹의 생존자 수를 합산합니다
- 결과 (Series):
  ```
  pclass
  1    136
  2     87
  3    119
  Name: survived, dtype: int64
  ```
- 1등석에서 136명, 2등석에서 87명, 3등석에서 119명이 생존했습니다

**2단계 (Figure 생성):**
- `figsize=(15, 5)`: 가로로 긴 그래프를 생성합니다
- 바 차트는 범주가 많을수록 가로 공간이 필요하므로 충분한 너비를 확보합니다

**3단계 (바 차트 플로팅):**
- `plt.bar()`: 바 차트를 그리는 함수입니다
- 첫 번째 인자 `surviveByClass.index`: x축 값 (1, 2, 3 - 선실 등급)
- 두 번째 인자 `surviveByClass.values`: y축 값 (136, 87, 119 - 생존자 수)
- `color=['red', 'green', 'blue']`: 각 막대에 다른 색상을 지정합니다

**4단계 (x축 눈금 설정):**
- `plt.xticks(surviveByClass.index)`: x축 눈금을 명시적으로 설정합니다
- 이렇게 하면 1, 2, 3이 정확하게 표시됩니다

**5단계 (그래프 꾸미기):**
- `plt.title()`: "선실 등급별 생존자 수"라는 제목을 추가합니다
- `plt.xlabel()`: x축에 "선실 등급" 레이블을 추가합니다
- `plt.ylabel()`: y축에 "생존자 수" 레이블을 추가합니다

**최종 결과:**
- 3개의 컬러풀한 막대가 표시됩니다
- 1등석(빨간색)의 막대가 가장 높고, 2등석(초록색)이 가장 낮습니다
- 이를 통해 "1등석 승객의 생존율이 가장 높았다"는 인사이트를 시각적으로 파악할 수 있습니다

📌 **노트**: 강사님께서 "이런 그림을 만들기 위해서는 통계 분석이 중요하다"고 강조하셨습니다. 시각화 전에 `groupby()`와 `sum()` 같은 집계 함수로 데이터를 분석하는 과정이 선행되어야 합니다.

---

## 🔐 보안 관점의 데이터 시각화: 로그 데이터 분석

이제 보안(Security) 관점에서 데이터를 생성하고 분석해봅니다. 로그인 로그 데이터를 만들어서 비정상적인 패턴을 탐지하는 실습입니다.

### 1. 더미 로그 데이터 생성

```python
# 로그인 로그 데이터 생성
timeStamp = pd.date_range('2025-11-06', periods=100, freq='H')
user = np.random.choice(['admin', 'superAdmin', 'root', 'guest', 'analyst'], size=100)
ip = np.random.choice(['192.168.0.1', '192.168.0.3', '192.168.0.5', 
                       '192.168.0.7', '192.168.0.9'], size=100)
status = np.random.choice(['SUCCESS', 'FAIL'], size=100, p=[0.6, 0.4])
delay_ms = np.random.randint(20, 80, 100)

frm = pd.DataFrame({
    'timestamp': timeStamp,
    'user': user,
    'ip': ip,
    'status': status,
    'delay_ms': delay_ms
})

print(frm.head())
```

#### 💻 코드 실행 상세 분석

**1단계 (타임스탬프 생성):**
- `pd.date_range('2025-11-06', periods=100, freq='H')`: 시작일부터 100개의 시간 데이터를 생성합니다
- `freq='H'`: 시간(Hour) 단위로 증가합니다
- 결과: 2025-11-06 00:00부터 1시간씩 증가하여 100개의 타임스탬프가 생성됩니다

**2단계 (사용자 데이터 생성):**
- `np.random.choice()`: 주어진 리스트에서 무작위로 선택합니다 (복원 추출)
- `['admin', 'superAdmin', 'root', 'guest', 'analyst']`: 5가지 사용자 유형
- `size=100`: 100개의 값을 생성합니다
- 각 사용자가 무작위로 선택되어 현실적인 로그 데이터를 시뮬레이션합니다

**3단계 (IP 주소 생성):**
- 5개의 IP 주소 중 무작위로 100개를 선택합니다
- 실제 환경에서는 각 사용자가 여러 IP에서 접속할 수 있음을 반영합니다

**4단계 (로그인 상태 생성):**
- `['SUCCESS', 'FAIL']`: 성공 또는 실패 두 가지 상태
- `p=[0.6, 0.4]`: 성공 확률 60%, 실패 확률 40%로 설정합니다
- 현실적으로 성공이 더 많지만, 실패도 일정 비율 발생하도록 합니다

**5단계 (지연 시간 생성):**
- `np.random.randint(20, 80, 100)`: 20ms부터 80ms 사이의 무작위 정수를 100개 생성합니다
- 로그인 처리 시간을 밀리초 단위로 시뮬레이션합니다

**6단계 (DataFrame 생성):**
- 딕셔너리 형태로 데이터를 전달하여 DataFrame을 생성합니다
- 각 키가 컬럼명이 되고, 값들이 해당 컬럼의 데이터가 됩니다

**최종 결과:**
- 100행 5열의 로그인 로그 DataFrame이 생성됩니다
- 각 행은 하나의 로그인 시도를 나타냅니다
- 출력 예시:
  ```
              timestamp        user            ip    status  delay_ms
  0 2025-11-06 00:00:00       guest  192.168.0.5   SUCCESS        45
  1 2025-11-06 01:00:00       admin  192.168.0.1      FAIL        73
  2 2025-11-06 02:00:00        root  192.168.0.9   SUCCESS        28
  3 2025-11-06 03:00:00     analyst  192.168.0.3      FAIL        61
  4 2025-11-06 04:00:00  superAdmin  192.168.0.7   SUCCESS        52
  ```

💡 **중요!**: 강사님께서 "전처리를 잘 해야한다. 한글과 영어를 섞는 행동 금지"라고 강조하셨습니다. 실제 프로젝트에서는 컬럼명을 일관성 있게 영어로 작성해야 합니다.

📌 **노트**: 공공 데이터셋을 구하는 경로로 강사님께서 "공공 데이터포털, Kaggle Competition, data.go.kr" 등을 소개하셨습니다.

---

### 2. 로그인 상태별 횟수 시각화

```python
# 로그인 시도 상태별 횟수 계산
loginStatusCount = frm['status'].value_counts()

# 바 차트로 시각화
plt.figure(figsize=(15, 5))
plt.bar(loginStatusCount.index, loginStatusCount.values, 
        color=['green', 'red'])
plt.title('로그인 시도 상태별 횟수')
plt.xlabel('상태')
plt.ylabel('횟수', rotation=0)
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (빈도수 계산):**
- `frm['status'].value_counts()`: 'status' 컬럼의 각 값이 몇 번 나타나는지 계산합니다
- 결과 (Series):
  ```
  status
  SUCCESS    60
  FAIL       40
  Name: count, dtype: int64
  ```
- 성공 60회, 실패 40회로 집계됩니다 (확률 p=[0.6, 0.4]를 반영)

**2단계 (바 차트 플로팅):**
- x축: `loginStatusCount.index` (SUCCESS, FAIL)
- y축: `loginStatusCount.values` (60, 40)
- `color=['green', 'red']`: 성공은 초록색, 실패는 빨간색으로 직관적으로 표현합니다

**최종 결과:**
- 성공(초록색 막대)이 실패(빨간색 막대)보다 높게 표시됩니다
- 전체 로그인 시도 중 성공과 실패의 비율을 한눈에 파악할 수 있습니다

---

### 3. 사용자별 평균 지연 시간 시각화

```python
# 사용자별 평균 지연 시간 계산
userAvgDelay = frm.groupby('user')['delay_ms'].mean()

# 바 차트로 시각화
plt.figure(figsize=(15, 5))
plt.bar(userAvgDelay.index, userAvgDelay.values, color='skyblue')
plt.title('사용자별 평균 로그인 지연 시간')
plt.xlabel('사용자')
plt.ylabel('평균 지연 시간 (ms)', rotation=0)
plt.xticks(rotation=45)
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (그룹화 및 평균 계산):**
- `groupby('user')`: 사용자별로 그룹화합니다
- `['delay_ms'].mean()`: 각 사용자의 평균 지연 시간을 계산합니다
- 결과 예시:
  ```
  user
  admin         48.2
  analyst       52.7
  guest         49.1
  root          51.3
  superAdmin    46.8
  Name: delay_ms, dtype: float64
  ```

**2단계 (바 차트 플로팅):**
- `color='skyblue'`: 모든 막대를 하늘색으로 통일합니다
- `plt.xticks(rotation=45)`: x축 레이블을 45도 회전하여 가독성을 높입니다
- 사용자 이름이 길 경우 회전하지 않으면 겹쳐 보일 수 있습니다

**최종 결과:**
- 각 사용자의 평균 로그인 지연 시간이 막대로 표시됩니다
- 비정상적으로 지연 시간이 긴 사용자가 있는지 시각적으로 확인할 수 있습니다
- 보안 관점에서 특정 사용자의 이상 행동을 탐지하는 데 활용할 수 있습니다

---

## 📊 히스토그램(Histogram): 데이터 분포 시각화

히스토그램은 **연속형 데이터의 분포**를 확인할 때 사용합니다. 데이터가 어느 구간에 얼마나 집중되어 있는지 파악할 수 있습니다.

### 1. 기본 히스토그램

```python
plt.figure(figsize=(15, 5))
plt.hist(frm['delay_ms'], bins=10, color='coral', edgecolor='black')
plt.title('로그인 지연 시간 분포')
plt.xlabel('지연 시간 (ms)')
plt.ylabel('빈도수')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (히스토그램 플로팅):**
- `plt.hist()`: 히스토그램을 그리는 함수입니다
- 첫 번째 인자 `frm['delay_ms']`: 지연 시간 데이터 (연속형 수치 데이터)
- `bins=10`: 데이터를 10개의 구간(bin)으로 나눕니다
- `color='coral'`: 막대를 산호색으로 채웁니다
- `edgecolor='black'`: 막대의 테두리를 검은색으로 표시하여 구분을 명확히 합니다

**2단계 (구간 분할 이해):**
- 지연 시간이 20ms부터 80ms까지 분포하므로, 각 구간은 약 6ms 단위로 나뉩니다
- 예: [20-26), [26-32), [32-38), ..., [74-80]
- 각 구간에 속하는 데이터 개수가 막대의 높이로 표시됩니다

**3단계 (분포 해석):**
- 막대가 고르게 분포하면 데이터가 균등하게 분산되어 있음을 의미합니다
- 특정 구간에 막대가 높으면 그 구간에 데이터가 집중되어 있음을 의미합니다
- 정규 분포, 편향 분포 등 데이터의 통계적 특성을 시각적으로 파악할 수 있습니다

**최종 결과:**
- 로그인 지연 시간이 어느 범위에 주로 분포하는지 한눈에 확인할 수 있습니다
- 이상치(outlier)가 있는지, 데이터가 정규 분포를 따르는지 등을 판단할 수 있습니다

💡 **중요!**: 히스토그램은 바 차트와 비슷해 보이지만, 바 차트는 **범주형 데이터**를, 히스토그램은 **연속형 데이터**를 다룬다는 차이가 있습니다.

---

## 📦 박스플롯(Boxplot): 분포와 이상치 파악

박스플롯은 데이터의 **사분위수(quartile)**와 **이상치(outlier)**를 시각화하는 강력한 도구입니다.

### 1. 기본 박스플롯

```python
plt.figure(figsize=(15, 5))
plt.boxplot([frm[frm['status'] == 'SUCCESS']['delay_ms'],
             frm[frm['status'] == 'FAIL']['delay_ms']],
            labels=['SUCCESS', 'FAIL'])
plt.title('로그인 상태별 지연 시간 분포')
plt.ylabel('지연 시간 (ms)')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 필터링):**
- `frm[frm['status'] == 'SUCCESS']['delay_ms']`: 성공한 로그인의 지연 시간만 추출합니다
- `frm[frm['status'] == 'FAIL']['delay_ms']`: 실패한 로그인의 지연 시간만 추출합니다
- 두 개의 Series가 리스트로 묶여 `plt.boxplot()`에 전달됩니다

**2단계 (박스플롯 플로팅):**
- `labels=['SUCCESS', 'FAIL']`: 각 박스에 레이블을 지정합니다
- 박스플롯의 구성 요소:
  - **박스(Box)**: 25% 백분위수(Q1)부터 75% 백분위수(Q3)까지의 범위 (IQR - Interquartile Range)
  - **중앙선(Median Line)**: 50% 백분위수 (중앙값)
  - **수염(Whiskers)**: Q1 - 1.5×IQR ~ Q3 + 1.5×IQR 범위
  - **이상치(Outliers)**: 수염 밖의 점들로 표시됩니다

**3단계 (분포 비교):**
- 두 개의 박스플롯이 나란히 표시되어 성공/실패 간 지연 시간 분포를 비교할 수 있습니다
- 박스의 위치, 크기, 중앙선의 높이를 통해 차이를 파악합니다

**최종 결과:**
- 성공한 로그인과 실패한 로그인의 지연 시간 분포를 비교할 수 있습니다
- 예를 들어, 실패한 로그인의 지연 시간이 더 길다면 네트워크 문제나 공격 시도를 의심할 수 있습니다
- 이상치가 있다면 특정 로그인 시도가 비정상적임을 시각적으로 파악할 수 있습니다

📌 **노트**: 박스플롯은 통계학에서 매우 중요한 시각화 도구로, 데이터의 중심 경향성, 분산, 대칭성, 이상치를 한 번에 파악할 수 있습니다.

---

## 🔍 산점도(Scatter Plot): 변수 간 관계 분석

산점도는 **두 변수 간의 관계**를 시각화할 때 사용합니다. 상관관계, 군집, 이상치 패턴 등을 파악할 수 있습니다.

### 1. 기본 산점도

```python
plt.figure(figsize=(15, 5))
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 4, 9, 5, 6, 7, 2, 7, 9]
plt.scatter(x, y, color='blue', marker='o', s=100, alpha=0.7)
plt.title('기본 산점도')
plt.xlabel('X 축')
plt.ylabel('Y 축')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (산점도 플로팅):**
- `plt.scatter()`: 산점도를 그리는 함수입니다
- 첫 번째 인자 `x`: x축 좌표 값들
- 두 번째 인자 `y`: y축 좌표 값들
- 각 (x, y) 쌍이 하나의 점으로 표시됩니다

**2단계 (시각적 옵션):**
- `color='blue'`: 점들의 색상을 파란색으로 지정합니다
- `marker='o'`: 점의 모양을 원형(circle)으로 지정합니다
- `s=100`: 점의 크기를 100으로 설정합니다 (기본값은 20)
- `alpha=0.7`: 투명도를 0.7로 설정합니다 (0=완전 투명, 1=완전 불투명)
- 투명도를 사용하면 점들이 겹칠 때 밀도를 시각적으로 파악할 수 있습니다

**3단계 (패턴 분석):**
- 점들이 일직선을 이루면 **선형 관계**가 있습니다
- 점들이 곡선을 이루면 **비선형 관계**가 있습니다
- 점들이 무작위로 흩어져 있으면 **상관관계가 없습니다**

**최종 결과:**
- 9개의 파란색 원형 점이 표시됩니다
- 이 예제에서는 특정한 패턴이 명확하지 않아 약한 상관관계를 보입니다

💡 **중요!**: 강사님께서 산점도에 대해 "점들이 어떠한 패턴을 갖느냐. 선형일수도, 곡선일수도, 군집일수도 있다. 어떻게 패턴을 이루는지 보면서 변수간의 관계를 파악하기 위한 시각화"라고 설명하셨습니다.

---

### 2. 사용자별 로그인 패턴 산점도

이제 실제 보안 데이터를 분석하여 비정상적인 사용자 행동 패턴을 탐지해봅니다:

```python
# 사용자별 통계 계산
userGroup = frm.groupby('user')
meanDelay = userGroup['delay_ms'].mean()
failRatio = userGroup.apply(lambda x: (x['status'] == 'FAIL').sum() / len(x))

# 산점도 그리기
plt.figure(figsize=(15, 5))
plt.scatter(meanDelay, failRatio, color='blue', marker='o', s=100, alpha=0.7)
plt.title('사용자별 로그인 패턴 분석 산점도')
plt.xlabel('평균 로그인 지연 시간 (ms)')
plt.ylabel('실패율', rotation=0)

# 각 점에 사용자 이름 표시
for user in meanDelay.index:
    plt.text(meanDelay[user], failRatio[user], user, 
             fontsize=9, ha='right')

plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (평균 지연 시간 계산):**
- `userGroup = frm.groupby('user')`: 사용자별로 그룹화합니다
- `meanDelay = userGroup['delay_ms'].mean()`: 각 사용자의 평균 지연 시간을 계산합니다
- 결과는 user를 인덱스로 하는 Series입니다

**2단계 (실패율 계산):**
- `lambda x: (x['status'] == 'FAIL').sum() / len(x)`: 람다 함수로 실패율을 계산합니다
- `(x['status'] == 'FAIL').sum()`: 해당 사용자의 실패 횟수
- `len(x)`: 해당 사용자의 전체 시도 횟수
- 실패율 = 실패 횟수 / 전체 시도 횟수 (0~1 사이의 값)

**3단계 (산점도 플로팅):**
- x축: 평균 지연 시간 (ms)
- y축: 실패율 (0~1)
- 각 점은 하나의 사용자를 나타냅니다

**4단계 (텍스트 레이블 추가):**
- `plt.text()`: 각 점 옆에 사용자 이름을 표시합니다
- `ha='right'`: 수평 정렬을 오른쪽으로 설정하여 점과 겹치지 않도록 합니다
- `fontsize=9`: 폰트 크기를 9로 설정합니다

**5단계 (인사이트 도출):**
- 오른쪽 위에 위치한 점: 지연 시간도 길고 실패율도 높음 → **가장 의심스러운 사용자**
- 왼쪽 아래에 위치한 점: 지연 시간도 짧고 실패율도 낮음 → 정상적인 사용자
- 이상치로 보이는 사용자는 추가 조사가 필요합니다

**최종 결과:**
- 비정상적인 로그인 패턴을 보이는 사용자를 시각적으로 탐지할 수 있습니다
- 예를 들어, 'admin' 사용자가 오른쪽 위에 위치한다면 무차별 대입 공격(Brute Force Attack)을 의심할 수 있습니다

📌 **노트**: 강사님께서 "찾고싶은 인사이트는 비정상적인 사용자의 행동 패턴을 탐지하고 싶다"고 강조하셨습니다. 이것이 보안 데이터 분석의 핵심 목적입니다.

---

### 3. Seaborn을 이용한 고급 산점도

Seaborn을 사용하면 더 풍부한 정보를 담은 산점도를 그릴 수 있습니다:

```python
# 사용자별 통계 데이터프레임 생성
avg = frm.groupby('user')['delay_ms'].mean()
failRatio = frm.groupby('user').apply(lambda x: (x['status'] == 'FAIL').mean())
attempts = frm['user'].value_counts()

userStatus = pd.DataFrame({
    'avg': avg,
    'failRatio': failRatio,
    'attempts': attempts
})

# Seaborn 산점도
plt.figure(figsize=(15, 5))
sns.scatterplot(x='avg', y='failRatio', 
                data=userStatus,
                size='attempts',
                hue='user',
                sizes=(50, 500))
plt.title('사용자별 로그인 패턴 분석 (시도 횟수 포함)')
plt.xlabel('평균 지연 시간 (ms)')
plt.ylabel('실패율')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (통계 데이터프레임 생성):**
- `avg`: 사용자별 평균 지연 시간
- `failRatio`: 사용자별 실패율 (`.mean()`은 0과 1의 평균이므로 실패율과 동일)
- `attempts`: 사용자별 시도 횟수 (`.value_counts()` 사용)
- 세 개의 Series를 딕셔너리로 묶어 DataFrame을 생성합니다

**2단계 (Seaborn 산점도):**
- `sns.scatterplot()`: Seaborn의 고급 산점도 함수입니다
- `x='avg'`, `y='failRatio'`: x축과 y축에 사용할 컬럼을 지정합니다
- `data=userStatus`: 데이터를 담고 있는 DataFrame을 전달합니다

**3단계 (다차원 정보 표현):**
- `size='attempts'`: 점의 크기로 시도 횟수를 나타냅니다
- 점이 클수록 해당 사용자의 로그인 시도가 많았음을 의미합니다
- `hue='user'`: 색상으로 사용자를 구분합니다
- 각 사용자가 다른 색상으로 표시됩니다
- `sizes=(50, 500)`: 점의 최소 크기와 최대 크기를 지정합니다

**4단계 (범례 자동 생성):**
- Seaborn은 자동으로 범례를 생성합니다
- 색상별 사용자 이름과 크기별 시도 횟수 범위가 표시됩니다

**최종 결과:**
- 하나의 산점도에 4차원 정보가 표현됩니다:
  1. x축: 평균 지연 시간
  2. y축: 실패율
  3. 점 크기: 시도 횟수
  4. 점 색상: 사용자 구분
- 복잡한 패턴을 한눈에 파악할 수 있어 매우 효과적입니다

💡 **중요!**: Matplotlib보다 Seaborn이 더 간결한 코드로 더 많은 정보를 표현할 수 있습니다. 특히 `hue`, `size`, `style` 등의 파라미터를 활용하면 다차원 데이터를 효과적으로 시각화할 수 있습니다.

---

## 🌡️ 히트맵(Heatmap): 상관관계 시각화

히트맵은 **변수 간의 상관관계**를 색상으로 표현하는 시각화 도구입니다. 특히 머신러닝에서 피처(feature) 선택 시 매우 유용합니다.

### 1. 상관계수(Correlation Coefficient) 이해

상관계수는 두 변수 간의 선형 관계의 강도와 방향을 -1부터 1까지의 값으로 나타냅니다:

- **+1에 가까울수록**: 강한 양의 상관관계 (한 변수가 증가하면 다른 변수도 증가)
- **-1에 가까울수록**: 강한 음의 상관관계 (한 변수가 증가하면 다른 변수는 감소)
- **0에 가까울수록**: 상관관계가 거의 없음

```python
# Iris 데이터셋 로드
irisFrm = sns.load_dataset('iris')
print(irisFrm.head())

# 상관계수 행렬 계산
corr = irisFrm.corr(numeric_only=True)
print(corr)
```

#### 💻 코드 실행 상세 분석

**1단계 (Iris 데이터셋 로드):**
- Iris 데이터셋은 붓꽃의 품종 분류를 위한 데이터입니다
- 4개의 수치형 피처: sepal_length, sepal_width, petal_length, petal_width
- 1개의 범주형 타겟: species (setosa, versicolor, virginica)

**2단계 (상관계수 행렬 계산):**
- `corr(numeric_only=True)`: 수치형 컬럼들 간의 상관계수를 계산합니다
- 결과는 4x4 행렬(DataFrame) 형태입니다
- 출력 결과:
  ```
                sepal_length  sepal_width  petal_length  petal_width
  sepal_length      1.000000    -0.117570      0.871754     0.817941
  sepal_width      -0.117570     1.000000     -0.428440    -0.366126
  petal_length      0.871754    -0.428440      1.000000     0.962865
  petal_width       0.817941    -0.366126      0.962865     1.000000
  ```

**3단계 (상관계수 해석):**
- **대각선 (1.000000)**: 자기 자신과의 상관계수는 항상 1입니다
- **sepal_length ↔ petal_length (0.871754)**: 강한 양의 상관관계
  - 꽃받침 길이가 길수록 꽃잎 길이도 긴 경향이 있습니다
- **petal_length ↔ petal_width (0.962865)**: 매우 강한 양의 상관관계
  - 꽃잎 길이와 너비는 거의 함께 증가합니다
- **sepal_width ↔ petal_length (-0.428440)**: 중간 정도의 음의 상관관계
  - 꽃받침 너비가 넓을수록 꽃잎 길이가 짧은 경향이 있습니다

**최종 결과:**
- 어떤 피처들이 서로 관련이 있는지 수치적으로 파악할 수 있습니다
- 머신러닝에서 이 정보를 바탕으로 피처 선택이나 차원 축소를 수행할 수 있습니다

📌 **노트**: 강사님께서 "상관관계가 높은 두 변수를 x, y로 해서 회귀분석을 하는 거죠. 리그레션(Regression). 회귀를 한다는 건 예측을 하겠다는 거예요"라고 설명하셨습니다.

---

### 2. 히트맵으로 상관관계 시각화

```python
plt.figure(figsize=(15, 5))
sns.heatmap(corr, fmt='.2f', annot=True, linewidth=0.5)
plt.title('Iris 데이터셋 피처 간 상관관계')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (히트맵 플로팅):**
- `sns.heatmap()`: Seaborn의 히트맵 함수입니다
- 첫 번째 인자 `corr`: 상관계수 행렬을 전달합니다

**2단계 (포매팅 옵션):**
- `fmt='.2f'`: 소수점 둘째 자리까지 표시합니다
- `annot=True`: 각 셀에 상관계수 값을 텍스트로 표시합니다
- `linewidth=0.5`: 셀 사이에 0.5 너비의 선을 그려 구분을 명확히 합니다

**3단계 (색상 매핑):**
- 기본 색상 팔레트가 적용됩니다
- 일반적으로 파란색(낮은 값) → 빨간색(높은 값) 그라데이션이 사용됩니다
- 대각선이 가장 진한 색으로 표시됩니다 (상관계수 1)

**4단계 (해석):**
- 진한 색상의 셀: 강한 상관관계
- 옅은 색상의 셀: 약한 상관관계
- 대각선을 제외하고 가장 진한 셀이 petal_length와 petal_width입니다 (0.96)
- 이는 이 두 변수가 거의 함께 움직인다는 것을 의미합니다

**최종 결과:**
- 4x4 격자 형태의 히트맵이 생성됩니다
- 각 셀의 색상과 숫자를 통해 변수 간 관계를 직관적으로 파악할 수 있습니다
- 복잡한 상관관계 행렬을 시각적으로 표현하여 이해하기 쉽습니다

💡 **중요!**: 히트맵의 색상 팔레트는 `cmap` 파라미터로 변경할 수 있습니다. 예: `cmap='YlGnBu'`, `cmap='coolwarm'` 등

---

### 3. 커스터마이징된 히트맵

```python
plt.figure(figsize=(15, 5))
sns.heatmap(corr, 
            fmt='.2f', 
            annot=True, 
            linewidth=0.5, 
            cmap='YlGnBu')
plt.title('Iris 데이터셋 피처 간 상관관계 (커스텀 컬러)')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**추가 옵션 설명:**
- `cmap='YlGnBu'`: Yellow-Green-Blue 색상 팔레트를 사용합니다
- 낮은 값은 노란색, 중간 값은 초록색, 높은 값은 파란색으로 표현됩니다
- 다른 컬러맵 예시:
  - `'coolwarm'`: 파란색(낮음) → 빨간색(높음)
  - `'viridis'`: 보라색 → 노란색
  - `'RdYlGn'`: 빨강 → 노랑 → 초록

**최종 결과:**
- 색상 팔레트가 변경되어 다른 느낌의 히트맵이 생성됩니다
- 색상 선택은 데이터의 특성과 발표 목적에 따라 결정합니다

---

## 🔄 피벗 테이블(Pivot Table)과 히트맵

실제 데이터는 수치형 피처들만 있는 경우가 드뭅니다. 범주형 변수와 수치형 변수가 섞여 있을 때는 **피벗 테이블(Pivot Table)**을 만들어 히트맵을 그려야 합니다.

### 1. 피벗 테이블 생성

```python
# 사용자 ~ 상태별 평균 지연시간 피벗 테이블
pivot = frm.pivot_table(index='user', 
                        columns='status', 
                        values='delay_ms', 
                        aggfunc='mean')
print(pivot)
```

#### 💻 코드 실행 상세 분석

**1단계 (피벗 테이블 생성):**
- `frm.pivot_table()`: DataFrame의 피벗 테이블 생성 함수입니다
- `index='user'`: 행(row) 인덱스로 사용할 컬럼을 지정합니다
- `columns='status'`: 열(column)로 사용할 컬럼을 지정합니다
- `values='delay_ms'`: 값으로 채울 데이터를 지정합니다
- `aggfunc='mean'`: 집계 함수로 평균을 사용합니다

**2단계 (피벗 테이블 구조 이해):**
- 출력 결과 예시:
  ```
  status           FAIL    SUCCESS
  user                            
  admin       37.000000  45.437500
  analyst     34.500000  50.625000
  guest       54.833333  55.888889
  root        44.000000  46.666667
  superAdmin  52.444444  49.125000
  ```
- 행: 5명의 사용자 (admin, analyst, guest, root, superAdmin)
- 열: 2가지 상태 (FAIL, SUCCESS)
- 값: 각 (사용자, 상태) 조합의 평균 지연 시간

**3단계 (데이터 재구조화):**
- 원래 frm은 100행 5열의 로그 형식 데이터였습니다
- 피벗 테이블은 5행 2열의 요약 형식 데이터로 변환되었습니다
- 이제 히트맵으로 시각화할 수 있는 형태가 되었습니다

**최종 결과:**
- 사용자별로 성공/실패 시 평균 지연 시간을 한눈에 비교할 수 있습니다
- 예: guest 사용자는 성공(55.89ms)과 실패(54.83ms) 시 지연 시간이 비슷합니다
- 예: analyst 사용자는 성공(50.63ms) 시 지연 시간이 실패(34.50ms)보다 높습니다

💡 **중요!**: 강사님께서 "피벗 테이블을 만들어야 히트맵을 만들 수 있어요. iris 데이터는 어차피 수치형으로 되어져 있는 피처들이 서로 간에 있기 때문에 가능했던 거고, 얘(frm)는 안 돼요"라고 설명하셨습니다.

---

### 2. 피벗 테이블을 히트맵으로 시각화

```python
plt.figure(figsize=(15, 5))
sns.heatmap(pivot, fmt='.2f', annot=True, linewidth=0.5, cmap='YlGnBu')
plt.title('사용자 ~ 상태별 평균 지연시간 히트맵')
plt.xlabel('로그인 상태')
plt.ylabel('사용자')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (히트맵 플로팅):**
- 피벗 테이블을 그대로 `sns.heatmap()`에 전달합니다
- 행 인덱스(user)가 y축이 됩니다
- 열 인덱스(status)가 x축이 됩니다

**2단계 (색상 해석):**
- `cmap='YlGnBu'` 사용 시:
  - 노란색: 낮은 지연 시간 (빠른 응답)
  - 초록색: 중간 지연 시간
  - 파란색: 높은 지연 시간 (느린 응답)

**3단계 (인사이트 도출):**
- 특정 사용자의 FAIL 셀이 진한 색이면:
  - 실패 시 지연 시간이 매우 높음
  - 비정상적인 반복 로그인 시도를 의심할 수 있음
- 특정 사용자의 SUCCESS와 FAIL 색상 차이가 크면:
  - 정상 로그인과 비정상 시도의 패턴이 다름
  - 보안 알람을 설정할 기준이 될 수 있음

**최종 결과:**
- 5행 2열의 히트맵이 생성됩니다
- 각 셀에는 평균 지연 시간(소수점 2자리)이 표시됩니다
- 색상과 숫자를 통해 비정상적인 패턴을 빠르게 파악할 수 있습니다

📌 **노트**: 강사님께서 "admin이 실패 확률이 되게 높은데요. admin이 비정상적인 반복 로그인을 했다는 걸로 저희가 판단할 수 있게 되는 거죠"라고 실무 관점에서 설명하셨습니다.

---

## 🚗 실습 프로젝트: 자동차 연비 데이터 분석

강사님께서 노션에 공유해주신 `mpg_visualization.xlsx` 파일을 사용한 실습 예제들입니다. 총 6개의 퀴즈 문제를 통해 오늘 배운 내용을 종합적으로 연습합니다.

### 실습 데이터셋 로드

```python
filePath = './SK_Rookies/data/mpg_visualization.xlsx'
mpgFrm = pd.read_excel(filePath, index_col=0)
mpgFrm.info()
print(mpgFrm.head())
```

#### 💻 코드 실행 상세 분석

**1단계 (엑셀 파일 읽기):**
- `pd.read_excel()`: 엑셀 파일(.xlsx)을 읽어 DataFrame으로 변환합니다
- `index_col=0`: 첫 번째 컬럼을 인덱스로 사용합니다
- CSV 파일은 `pd.read_csv()`를 사용하지만, 엑셀 파일은 `read_excel()`을 사용합니다

**2단계 (데이터 구조 확인):**
- `info()`: 234개 행, 11개 컬럼
- 주요 컬럼:
  - `manufacturer` (object): 제조사 (audi, toyota, chevrolet 등)
  - `model` (object): 모델명
  - `displ` (float64): 배기량 (리터)
  - `year` (int64): 연식
  - `cyl` (int64): 실린더 수
  - `trans` (object): 변속기 유형
  - `drv` (object): 구동방식 (4=4륜, f=전륜, r=후륜)
  - `cty` (int64): 도시 연비 (MPG - Miles Per Gallon)
  - `hwy` (int64): 고속도로 연비 (MPG)
  - `fl` (object): 연료 유형
  - `class` (object): 차량 클래스 (compact, suv 등)

**최종 결과:**
- 자동차 연비 데이터셋이 로드되어 분석 준비가 완료됩니다

💡 **중요!**: 강사님께서 "확장자가 엑셀 파일인 거 보이십니까? 그래서 읽어드릴 때 read_csv가 아니라 read_excel로 읽어드리고 있는 거 보이세요?"라고 강조하셨습니다.

---

### Q1) 배기량에 따른 고속도로 연비 비교

**문제:** 배기량 4 이하인 자동차와 5 이상인 자동차 중 고속도로 평균연비가 높은지를 확인한다면?

```python
# 배기량 기준으로 그룹화하여 평균 계산
dispLComp = mpgFrm.groupby(mpgFrm['displ'] <= 4)['hwy'].mean()
dispLComp.index = ['5 이상', '4 이하']

# 바 차트로 시각화
plt.figure(figsize=(15, 5))
plt.bar(dispLComp.index.astype(str), dispLComp.values, color=['green', 'blue'])
plt.title('배기량에 따른 고속도로 연비 비교')
plt.xlabel('배기량 (리터)')
plt.ylabel('평균 고속도로 연비 (MPG)')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (조건부 그룹화):**
- `mpgFrm['displ'] <= 4`: 배기량이 4 이하인지 판단하는 불리언 Series
- True 그룹과 False 그룹으로 나뉩니다
- `['hwy'].mean()`: 각 그룹의 고속도로 연비 평균을 계산합니다

**2단계 (인덱스 변경):**
- 기본 인덱스는 True, False입니다
- 더 직관적인 '4 이하', '5 이상'으로 변경합니다
- 순서는 [False, True] → ['5 이상', '4 이하']입니다

**3단계 (결과 해석):**
- 일반적으로 배기량이 작을수록 연비가 좋습니다
- '4 이하' 그룹의 막대가 더 높게 나타날 것입니다

**최종 결과:**
- 배기량과 연비의 반비례 관계를 시각적으로 확인할 수 있습니다

---

### Q2) 제조사별 도시 연비 비교

**문제:** audi, toyota 두 회사의 모든 차종에 대한 도시연비 평균을 비교한다면?

```python
# 특정 제조사만 필터링하여 평균 계산
brandComp = mpgFrm[mpgFrm['manufacturer'].isin(['audi', 'toyota'])].groupby('manufacturer')['cty'].mean()

# 바 차트로 시각화
plt.figure(figsize=(15, 5))
plt.bar(brandComp.index, brandComp.values, color='purple')
plt.xticks(rotation=45)
plt.title('제조사별 도시 연비 비교')
plt.xlabel('제조사')
plt.ylabel('평균 도시 연비 (MPG)')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터 필터링):**
- `mpgFrm['manufacturer'].isin(['audi', 'toyota'])`: 제조사가 audi 또는 toyota인 행만 선택합니다
- `isin()` 메서드는 여러 값 중 하나와 일치하는지 확인할 때 유용합니다

**2단계 (그룹화 및 평균):**
- `groupby('manufacturer')`: 제조사별로 그룹화합니다
- `['cty'].mean()`: 각 제조사의 도시 연비 평균을 계산합니다

**3단계 (시각화):**
- 모든 막대에 동일한 색상(보라색)을 사용합니다
- `plt.xticks(rotation=45)`: x축 레이블을 45도 회전하여 가독성을 높입니다

**최종 결과:**
- audi와 toyota의 도시 연비 평균을 직접 비교할 수 있습니다
- 어느 제조사의 차량이 도시 환경에서 더 효율적인지 파악할 수 있습니다

---

### Q3) 여러 제조사의 고속도로 연비 비교

**문제:** chevrolet, ford, honda 제조사의 모든 차종에 대한 고속도로 연비 평균을 시각화한다면?

```python
# 3개 제조사 필터링 및 평균 계산
cfhComp = mpgFrm[mpgFrm['manufacturer'].isin(['chevrolet', 'ford', 'honda'])].groupby('manufacturer')['hwy'].mean()

# 바 차트로 시각화
plt.figure(figsize=(15, 5))
plt.bar(cfhComp.index.astype(str), cfhComp.values, color=['red', 'green', 'blue'])
plt.title('제조사별 고속도로 연비 비교')
plt.xlabel('제조사')
plt.ylabel('평균 고속도로 연비 (MPG)')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (다중 제조사 필터링):**
- `isin(['chevrolet', 'ford', 'honda'])`: 3개 제조사만 선택합니다
- 리스트에 원하는 만큼의 값을 추가할 수 있습니다

**2단계 (색상 매핑):**
- `color=['red', 'green', 'blue']`: 각 제조사에 다른 색상을 할당합니다
- 리스트의 순서는 인덱스의 알파벳 순서와 일치합니다 (chevrolet, ford, honda)

**최종 결과:**
- 3개 제조사의 고속도로 연비를 색상으로 구분하여 비교할 수 있습니다
- 어느 제조사가 고속도로 주행에 최적화되어 있는지 판단할 수 있습니다

---

### Q4) 구동방식별 고속도로 연비 평균

**문제:** 구동방식별 고속도로연비평균을 막대 그래프로 시각화한다면?

```python
# 구동방식별 평균 계산
# drv: 4=4륜구동, f=전륜구동, r=후륜구동
transHwyComp = mpgFrm.groupby('drv')['hwy'].mean()

# 바 차트로 시각화
plt.figure(figsize=(15, 5))
plt.bar(transHwyComp.index.astype(str), transHwyComp.values, 
        color=['orange', 'purple', 'cyan'])
plt.xticks(rotation=45)
plt.title('구동방식별 고속도로 연비 평균')
plt.xlabel('구동방식 (4=4륜, f=전륜, r=후륜)')
plt.ylabel('평균 고속도로 연비 (MPG)')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (구동방식 이해):**
- '4': 4륜구동 (4WD - Four Wheel Drive)
- 'f': 전륜구동 (FWD - Front Wheel Drive)
- 'r': 후륜구동 (RWD - Rear Wheel Drive)

**2단계 (그룹화 및 평균):**
- `groupby('drv')`: 구동방식별로 그룹화합니다
- `['hwy'].mean()`: 각 구동방식의 고속도로 연비 평균을 계산합니다

**3단계 (결과 해석):**
- 일반적으로 전륜구동(f)이 가장 연비가 좋습니다
- 4륜구동(4)은 무게가 무거워 연비가 낮은 경향이 있습니다
- 후륜구동(r)은 중간 정도의 연비를 보입니다

**최종 결과:**
- 구동방식과 연비의 관계를 시각적으로 파악할 수 있습니다
- 연비를 중시하는 소비자에게 구동방식 선택의 참고 자료가 됩니다

---

### Q5) 구동방식별 도시 및 고속도로 연비 비교 (Multi Bar)

**문제:** 구동방식별 고속도로, 도시연비 평균을 서브셋을 만들고 시각화한다면?

```python
# 구동방식별 도시 및 고속도로 연비 평균 계산
drvCtyHwyComp = mpgFrm.groupby('drv')[['cty', 'hwy']].mean()

# Multi Bar 차트로 시각화
plt.figure(figsize=(15, 5))
plt.bar(drvCtyHwyComp.index.astype(str), drvCtyHwyComp['cty'], 
        width=0.4, label='도시연비', align='center', color='skyblue')
plt.bar(drvCtyHwyComp.index.astype(str), drvCtyHwyComp['hwy'], 
        width=0.4, label='고속도로연비', align='edge', color='salmon')
plt.xticks(rotation=45)
plt.title('구동방식별 도시 및 고속도로 연비 평균')
plt.xlabel('구동방식')
plt.ylabel('평균 연비 (MPG)')
plt.legend()
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (다중 컬럼 평균):**
- `groupby('drv')[['cty', 'hwy']].mean()`: 두 컬럼의 평균을 동시에 계산합니다
- 결과는 3행 2열의 DataFrame입니다

**2단계 (첫 번째 막대 그리기):**
- `plt.bar()`: 도시연비 막대를 먼저 그립니다
- `width=0.4`: 막대 너비를 0.4로 설정합니다 (기본값 0.8)
- `align='center'`: x축 위치를 막대의 중앙에 맞춥니다
- `color='skyblue'`: 하늘색으로 채웁니다
- `label='도시연비'`: 범례에 표시될 레이블을 지정합니다

**3단계 (두 번째 막대 그리기):**
- 동일한 x축 위치에 두 번째 막대를 그립니다
- `align='edge'`: x축 위치를 막대의 가장자리에 맞춥니다
- 이렇게 하면 두 막대가 나란히 배치됩니다
- `color='salmon'`: 연어색으로 채워 첫 번째 막대와 구분합니다

**4단계 (범례 추가):**
- `plt.legend()`: 범례를 표시합니다
- 각 막대의 `label` 값이 범례에 표시됩니다

**최종 결과:**
- 각 구동방식마다 두 개의 막대가 나란히 표시됩니다
- 도시연비(하늘색)와 고속도로연비(연어색)를 직접 비교할 수 있습니다
- 일반적으로 고속도로 연비가 도시 연비보다 높게 나타납니다

💡 **중요!**: Multi Bar 차트는 두 가지 이상의 값을 동시에 비교할 때 매우 유용합니다. `align` 파라미터를 조절하여 막대를 나란히 배치합니다.

---

### Q6) 클래스별 빈도수 시각화

**문제:** 해당 클래스별 빈도수를 시각화한다면?

```python
# 클래스별 빈도수 계산
classCount = mpgFrm['class'].value_counts()

# 바 차트로 시각화
plt.figure(figsize=(15, 5))
plt.bar(classCount.index, classCount.values, color='lightgreen')
plt.xticks(rotation=45)
plt.title('자동차 클래스별 빈도수')
plt.xlabel('차량 클래스')
plt.ylabel('차량 수')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석

**1단계 (빈도수 계산):**
- `value_counts()`: 각 클래스가 몇 번 나타나는지 계산합니다
- 자동으로 빈도가 높은 순서로 정렬됩니다
- 결과 예시:
  ```
  class
  suv            62
  compact        47
  midsize        41
  subcompact     35
  pickup         33
  minivan        11
  2seater         5
  Name: count, dtype: int64
  ```

**2단계 (시각화):**
- 모든 막대를 연두색(lightgreen)으로 통일합니다
- x축 레이블을 45도 회전하여 클래스 이름이 겹치지 않도록 합니다

**3단계 (결과 해석):**
- suv가 가장 많고(62대), 2seater가 가장 적습니다(5대)
- 데이터셋의 클래스 불균형을 확인할 수 있습니다
- 머신러닝 모델을 학습시킬 때 이 불균형을 고려해야 합니다

**최종 결과:**
- 데이터셋의 구성을 한눈에 파악할 수 있습니다
- 어떤 클래스의 데이터가 부족한지 확인하여 추가 데이터 수집 계획을 세울 수 있습니다

---

## 🧠 머신러닝과 데이터 시각화의 연결

강사님께서 강의 중 머신러닝의 기초 개념을 설명해주셨습니다. 시각화는 단순히 그래프를 그리는 것이 아니라, 머신러닝 모델을 설계하고 평가하는 데 필수적인 도구입니다.

### 1. 머신러닝의 3가지 학습 방법

#### 지도학습 (Supervised Learning)
- **정의**: 정답(Target)이 있는 상태에서 학습합니다
- **구성**: 독립변수(Feature) + 종속변수(Target)
- **예시**: 
  - 집값 예측: 면적, 위치, 방 개수(Feature) → 가격(Target)
  - 스팸 메일 분류: 이메일 내용(Feature) → 스팸/정상(Target)
  - 이미지 분류: 픽셀 값(Feature) → 고양이/개(Target)

**지도학습의 2가지 유형:**

1. **분류 (Classification)**
   - 타겟이 범주형 데이터입니다
   - 예: 스팸/정상, 합격/불합격, A등급/B등급/C등급
   - 성능 평가: 정확도(Accuracy), 정밀도(Precision), 재현율(Recall), F1-Score

2. **회귀 (Regression)**
   - 타겟이 연속형 숫자 데이터입니다
   - 예: 집값, 주식 가격, 온도
   - 성능 평가: MSE(Mean Squared Error), RMSE, MAE, R²

#### 비지도학습 (Unsupervised Learning)
- **정의**: 정답이 없는 상태에서 데이터의 패턴을 찾습니다
- **목적**: 데이터 자체의 구조나 숨겨진 패턴을 발견합니다
- **예시**:
  - 군집화(Clustering): 고객을 유사한 그룹으로 분류
  - 차원 축소: 고차원 데이터를 2D/3D로 축소하여 시각화
  - 이상치 탐지: 정상 범위를 벗어난 데이터 찾기

#### 강화학습 (Reinforcement Learning)
- **정의**: 에이전트가 환경과 상호작용하며 보상을 최대화하는 방향으로 학습합니다
- **특징**: 스스로 행동을 선택하고, 그 행동의 결과에 대한 보상을 받습니다
- **예시**:
  - 게임 플레이: AlphaGo, 게임 AI
  - 로봇 제어: 자율주행 자동차, 드론

💡 **중요!**: 강사님께서 "지도학습이 두 가지로 나뉘어지는 거예요. 하나는 Classification(분류), 두 번째는 Regression(회귀)"라고 설명하셨습니다.

---

### 2. 상관관계와 회귀분석

**상관계수 (Correlation Coefficient)**
- 두 변수 간의 선형 관계를 -1부터 1까지의 값으로 표현합니다
- **양의 상관관계 (+1에 가까움)**: 한 변수가 증가하면 다른 변수도 증가합니다
  - 예: 키와 몸무게, 공부 시간과 시험 점수
- **음의 상관관계 (-1에 가까움)**: 한 변수가 증가하면 다른 변수는 감소합니다
  - 예: 운동 시간과 체지방률, 속도와 연비
- **상관관계 없음 (0에 가까움)**: 두 변수 간 뚜렷한 관계가 없습니다

**회귀분석 (Regression Analysis)**
- 상관관계가 높은 변수들을 이용해 예측 모델을 만듭니다
- 과거 데이터를 학습하여 미래 값을 예측합니다
- 예시:
  - "키가 170cm라면 몸무게는 약 65kg일 것이다"
  - "배기량이 3.0L이라면 연비는 약 20MPG일 것이다"

**오차와 모델 평가**
- 회귀선(Regression Line)을 그렸을 때, 실제 데이터 점들이 선 주변에 분포합니다
- 각 점에서 회귀선까지의 거리가 **오차(Error)**입니다
- 이 오차를 제곱하여 평균을 구한 것이 **MSE (Mean Squared Error)**입니다
- MSE가 낮을수록 좋은 모델입니다

💡 **중요!**: 강사님께서 "상관관계를 예측을 해서 이 두 변수 간에 회귀분석을 하는 거죠. 회귀를 한다는 건 예측을 하겠다는 거예요"라고 강조하셨습니다.

---

## 📚 오늘 배운 핵심 개념 총정리

### 시각화 워크플로우

1. **데이터 로드 및 전처리**
   - CSV, Excel 파일 읽기
   - 결측치, 이상치 처리
   - 데이터 타입 확인 및 변환

2. **탐색적 데이터 분석 (EDA)**
   - `head()`, `info()`, `describe()` 등으로 데이터 파악
   - `groupby()`, `pivot_table()` 등으로 데이터 집계
   - 상관계수 분석 (`corr()`)

3. **시각화 선택**
   - 바 차트: 범주형 데이터 비교
   - 히스토그램: 연속형 데이터 분포
   - 박스플롯: 분포와 이상치
   - 산점도: 변수 간 관계
   - 히트맵: 상관관계 행렬

4. **인사이트 도출**
   - 그래프에서 패턴, 이상치, 트렌드 찾기
   - 비즈니스/보안 관점에서 의미 해석
   - 추가 분석이나 액션 아이템 도출

---

### Matplotlib vs Seaborn 비교

| 항목 | Matplotlib | Seaborn |
|------|------------|---------|
| **난이도** | 낮은 수준의 세밀한 제어 가능 | 고수준의 간결한 인터페이스 |
| **코드 길이** | 상대적으로 길고 복잡 | 짧고 간결 |
| **기본 스타일** | 기본 스타일이 단순함 | 통계적으로 세련된 기본 스타일 |
| **색상 팔레트** | 수동으로 지정 필요 | 자동으로 조화로운 색상 선택 |
| **통계 기능** | 제한적 | 상관관계, 분포 등 통계 기능 내장 |
| **사용 시기** | 세밀한 커스터마이징 필요 시 | 빠른 탐색과 분석이 필요할 때 |

📌 **노트**: 실무에서는 Seaborn으로 빠르게 탐색하고, Matplotlib으로 최종 발표용 그래프를 정교하게 다듬는 경우가 많습니다.

---

### 시각화 타입별 사용 시나리오

**바 차트 (Bar Chart)**
- **언제**: 범주형 데이터의 빈도나 평균을 비교할 때
- **예시**: 제품별 판매량, 지역별 인구, 등급별 점수

**히스토그램 (Histogram)**
- **언제**: 연속형 데이터의 분포를 확인할 때
- **예시**: 나이 분포, 소득 분포, 응답 시간 분포

**박스플롯 (Boxplot)**
- **언제**: 데이터의 중앙값, 사분위수, 이상치를 파악할 때
- **예시**: 부서별 급여 분포 비교, 실험군/대조군 비교

**산점도 (Scatter Plot)**
- **언제**: 두 변수 간의 관계를 탐색할 때
- **예시**: 키와 몸무게, 광고비와 매출

**히트맵 (Heatmap)**
- **언제**: 변수 간 상관관계나 2차원 행렬 데이터를 시각화할 때
- **예시**: 피처 간 상관계수, 사용자-상품 평점 행렬

---

## 🔐 보안 관점의 데이터 분석 인사이트

오늘 강의에서 강사님께서 특히 강조하신 **보안 관점의 데이터 분석**은 다음과 같은 시나리오에 활용됩니다:

### 비정상 로그인 탐지

1. **평균 지연 시간 분석**
   - 정상 사용자: 평균 40-60ms
   - 공격자 (무차별 대입): 평균 200-500ms (네트워크 지연)
   - → 지연 시간이 비정상적으로 높은 사용자 탐지

2. **실패율 분석**
   - 정상 사용자: 실패율 0-10%
   - 공격자: 실패율 50% 이상 (잘못된 비밀번호 시도)
   - → 실패율이 높은 사용자 탐지

3. **시도 횟수 분석**
   - 정상 사용자: 하루 1-5회
   - 공격자: 하루 수백~수천 회
   - → 시도 횟수가 비정상적으로 많은 사용자 탐지

4. **시간대 분석**
   - 정상 사용자: 업무 시간(9-18시)에 집중
   - 공격자: 새벽 시간대에 집중 (자동화 스크립트)
   - → 비정상 시간대에 활동하는 사용자 탐지

### 히트맵을 통한 패턴 분석

```python
# 사용자 ~ 상태별 평균 지연시간 피벗 테이블
pivot = frm.pivot_table(index='user', columns='status', 
                        values='delay_ms', aggfunc='mean')

# 히트맵 시각화
plt.figure(figsize=(15, 5))
sns.heatmap(pivot, fmt='.2f', annot=True, linewidth=0.5, cmap='YlGnBu')
plt.title('사용자 ~ 상태별 평균 지연시간 히트맵 (보안 분석)')
plt.show()
```

**히트맵에서 발견할 수 있는 이상 패턴:**
- FAIL 셀이 진한 색 → 실패 시 지연 시간이 높음 (의심)
- SUCCESS와 FAIL의 색상 차이가 큼 → 정상/비정상 패턴이 명확히 다름
- 특정 사용자의 모든 셀이 진한 색 → 전반적으로 문제가 있는 계정

💡 **중요!**: 강사님께서 "비정상적인 반복 로그인을 했다는 걸로 저희가 판단할 수가 있게 되는 거죠"라고 설명하시며, 실무에서 이러한 시각화가 보안 담당자의 의사결정을 돕는다고 강조하셨습니다.

---

## 🎓 학습 마무리 및 다음 스케줄

### 오늘의 학습 성과

오늘 우리는 다음 내용들을 학습했습니다:
1. ✅ Matplotlib의 기본 문법과 서브플롯
2. ✅ 바 차트를 이용한 범주형 데이터 시각화
3. ✅ 히스토그램과 박스플롯을 통한 분포 분석
4. ✅ 산점도를 이용한 변수 간 관계 파악
5. ✅ 히트맵과 피벗 테이블을 활용한 상관관계 분석
6. ✅ 보안 관점의 로그 데이터 분석 및 이상 탐지
7. ✅ 실습 프로젝트: 자동차 연비 데이터 분석 (6문제)

### 숙제 및 복습 과제

강사님께서 노션에 공유해주신 `mpg_visualization.xlsx` 파일의 6문제를 다시 한 번 풀어보세요:

1. Q1) 배기량에 따른 고속도로 연비 비교
2. Q2) audi, toyota 제조사 도시 연비 비교
3. Q3) chevrolet, ford, honda 고속도로 연비 시각화
4. Q4) 구동방식별 고속도로 연비 막대 그래프
5. Q5) 구동방식별 도시/고속도로 연비 Multi Bar
6. Q6) 클래스별 빈도수 시각화

💡 **팁**: 강사님께서 "이거 가지고 오늘 배우셨던 내용도 전체 전반적인 것들을 시각화하는 쪽에서 진행해 주시면 되지 않을까 싶습니다"라고 말씀하셨으므로, 단순히 코드를 따라 치는 것이 아니라 **왜 이렇게 분석하는지**, **어떤 인사이트를 얻을 수 있는지**를 생각하며 실습하세요.

### 내일 학습 예고

**학습 주제: LLM(Large Language Model) 기초**

강사님께서 "오늘은 이렇게 제가 뭐 말씀으로 드렸던 거 장표 보면서 좀 설명드리는 시간 한번 가져보는데, 초점은 뭐가 되어야 되냐면 우리는 이제 LLM을 쓰는 거니까 그 딥러닝에 CNN이 아닌 RNN에 대해서 좀 배우셔야 돼요"라고 예고하셨습니다.

**내일 다룰 내용:**
- 딥러닝(Deep Learning) 기초 개념
- CNN (Convolutional Neural Network) vs RNN (Recurrent Neural Network)
- RNN의 구조와 작동 원리
- LLM의 기초 이론
- Folium (지도 시각화) - 시간이 되면
- Streamlit (웹 시각화) - VSCode에서 실습

### 다음 주 일정

**11월 14일 (금요일) - 1차 사업평가**
- 시험 시간: 오후 5시
- 시험 형식: 60문제
- 시험 시간: 30분 (지난번 40분보다 짧음)
- 강사님 당부: "사업평가는 실제 시험 점수에 들어가니까 공부 열심히 해서 나쁘지 않은 성적 거두시기 바랍니다"

**다음 주 금요일부터 - 팀 프로젝트 시작**
- 팀 공개 및 주제 발표
- 팀별 아이스브레이킹, 기획 준비
- 기획, 데이터 준비, 방향성 설계
- 4일 정도의 짧은 기간이므로 효율적인 협업 필요

### 개발 환경 준비사항

**필수 설치:**
1. ✅ GitHub Desktop (또는 Git)
2. ✅ VSCode (Visual Studio Code)
3. ⏳ Streamlit (추후 설치 예정)

강사님께서 "깃허브 깔아놓으시는 걸 좀 부탁을 드렸었고, VSCode 인스톨 부탁 드렸는데요, 스토리 깔려 있다는 전제하에서 스트림릿은 제가 한번 보여드려 볼 수 있도록 할게요"라고 말씀하셨으므로, GitHub와 VSCode는 반드시 설치해 두세요.

---

## 📝 강사님 말씀 중 기억할 점

### 학습 태도에 대한 조언

"오늘도 저희 행복해지기 위해서 한번 열심히 웃어 보면서 하루를 시작해 볼 수 있도록 하겠습니다"

- 긍정적인 마인드로 학습에 임하는 것이 중요합니다
- "행복해서 웃는게 아니라 행복해지려고 웃는다"는 자세

### 프로그래밍 학습의 연속성

"프로그램 언어라고 하는 거는 끊어지는 부분이 없어요. 지속성을 가지고 계속 연결이 돼요"

- 어제 배운 내용이 오늘로 이어지고, 내일로 이어집니다
- 일을 몰라도 이를 하는데 전혀 문제가 되지 않는 일반 업무와 달리, 프로그래밍은 연속선상에 있습니다
- 복습과 반복 학습이 매우 중요합니다

### 자신감과 성장

"어제 이제 어려웠지만 오늘 하다 보면 자연스럽게 또 '아 그거 그렇지' 이렇게 할 수 있어, 이런 느낌으로 발전하시면 되니까"

- 처음에는 어렵고 낯설어도, 반복하면 익숙해집니다
- 어제보다 나은 오늘이 되도록 노력하세요
- 작은 성장을 축하하고 인정하세요

### 실습의 중요성

"피할 수 없다면 즐겨볼 수 있도록 하겠습니다"

- 실습이 어려워도 회피하지 말고 즐기는 마음으로 임하세요
- 직접 코드를 작성하고 에러를 해결하는 과정이 실력 향상의 지름길입니다

---

## 🔗 참고 자료 및 추가 학습 리소스

### 공식 문서
- [Matplotlib 공식 문서](https://matplotlib.org/stable/contents.html)
- [Seaborn 공식 문서](https://seaborn.pydata.org/)
- [Pandas 공식 문서](https://pandas.pydata.org/docs/)
- [NumPy 공식 문서](https://numpy.org/doc/)

### 데이터셋 출처
- **공공 데이터포털**: https://www.data.go.kr/
- **Kaggle Competitions**: https://www.kaggle.com/
- **Seaborn 내장 데이터셋**: `sns.get_dataset_names()` 로 확인

### 추가 학습 자료
- Matplotlib Gallery: 다양한 시각화 예제 확인
- Seaborn Tutorial: 통계적 시각화 학습
- Pandas Visualization: DataFrame 직접 시각화 방법

---

## 💬 질문과 토론

### 자주 묻는 질문 (FAQ)

**Q1: Matplotlib과 Seaborn 중 어떤 것을 먼저 배워야 하나요?**
- A: Matplotlib을 먼저 배우는 것을 권장합니다. Seaborn은 Matplotlib을 기반으로 하므로, Matplotlib의 기본 문법을 이해하면 Seaborn을 더 효과적으로 활용할 수 있습니다.

**Q2: 한글 폰트 설정을 매번 해야 하나요?**
- A: 네, 새로운 노트북이나 스크립트를 시작할 때마다 설정해야 합니다. 하지만 별도의 설정 파일에 저장하여 자동으로 로드할 수도 있습니다.

**Q3: 상관계수가 높다고 항상 인과관계가 있나요?**
- A: 아닙니다! 상관관계와 인과관계는 다릅니다. "아이스크림 판매량과 익사 사고"가 높은 상관관계를 보일 수 있지만, 이는 "여름"이라는 숨은 변수 때문입니다. 인과관계를 입증하려면 추가적인 실험과 분석이 필요합니다.

**Q4: 히트맵의 색상이 마음에 들지 않는데 변경할 수 있나요?**
- A: 네, `cmap` 파라미터로 변경할 수 있습니다. 인기 있는 컬러맵: 'viridis', 'coolwarm', 'YlGnBu', 'RdYlGn' 등

**Q5: 그래프를 파일로 저장하려면 어떻게 하나요?**
- A: `plt.savefig('filename.png')` 또는 `plt.savefig('filename.pdf')`를 `plt.show()` 전에 호출하면 됩니다.

---

## 🎯 핵심 요약 (TL;DR)

오늘 배운 가장 중요한 5가지:

1. **시각화의 4단계 패턴**: `plt.figure()` → 그래프 그리기 → `plt.show()` → `plt.close()`

2. **범주형 데이터 = 바 차트**, **연속형 데이터 = 히스토그램**

3. **서브플롯으로 한 화면에 여러 그래프**: `fig.add_subplot(행, 열, 위치)`

4. **상관관계 분석**: `df.corr()` + `sns.heatmap()` = 변수 간 관계 시각화

5. **피벗 테이블**: 범주형 변수를 포함한 데이터를 히트맵으로 만들 때 필수

---

**마지막 당부:**
강사님께서 "너무 우려하지 마시고 자신감 가지시라고 드려본 거기 때문에, 혹시 이거 하다가 갑자기 또 자신감이 자존감이 낮아지는 걸까요? 그러시면 안됩니다"라고 말씀하셨습니다. 

실습 문제가 어렵더라도 좌절하지 마세요. 오늘 배운 내용을 천천히 복습하고, 코드를 하나씩 따라 쳐보면서 이해하세요. 모든 전문가도 처음에는 초보자였습니다!

**오늘도 고생 많으셨습니다. 내일 더 건강한 모습으로 만나요! 🎉**

---

**작성일**: 2025년 11월 6일  
**작성자**: 학습 노트  
**버전**: 1.0  
**총 줄 수**: 1200+ 줄