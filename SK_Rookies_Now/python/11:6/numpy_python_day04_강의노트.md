# 📝 Python 데이터 시각화 및 분석 심화 강의 노트 (4일차)

오늘 4일차 강의에서는 Python의 대표적인 시각화 라이브러리인 **Matplotlib**와 **Seaborn**의 사용법을 깊이 있게 학습했습니다. 단순한 차트 그리기를 넘어, 데이터 분석 결과를 효과적으로 시각화하고 그 안에서 인사이트를 도출하는 구체적인 방법론에 초점을 맞춘 매우 유익한 시간이었습니다. 특히, 데이터 분석이 인공지능(AI) 분야와 어떻게 연결되는지에 대한 강사님의 깊이 있는 설명은 기술의 본질을 이해하는 데 큰 도움이 되었습니다.

### 1. 학습 목표 및 강의 계획

- **학습 목표**
    - **Matplotlib**의 기본 구조(Figure, Axes)와 다양한 플롯 유형을 이해하고 자유자재로 활용할 수 있다.
    - **Seaborn**을 사용하여 더 아름답고 통계적으로 유의미한 고급 시각화를 구현할 수 있다.
    - 데이터 분석(전처리, 그룹화, 피벗)과 시각화를 연계하여 실제 문제 해결에 적용할 수 있다.
    - 데이터 분포의 중요성을 이해하고, 히스토그램과 박스 플롯을 통해 데이터의 특성을 진단할 수 있다.
- **강의 계획**
    - **Streamlit**을 활용한 웹 시각화 맛보기 (VSCode 환경에서 진행 예정)
    - **가상환경(venv)** 설정 및 `open ai`, `langchain` 라이브러리 설치
    - 프로젝트 진행 방식 안내 (팀 구성, 기획 단계 등)

---

## 2. 시각화 환경 설정

본격적인 학습에 앞서, 원활한 시각화와 분석을 위한 개발 환경을 설정하는 과정을 거쳤습니다.

### 2.1. 핵심 라이브러리 임포트

오늘 사용할 핵심 라이브러리들을 임포트합니다. `numpy`와 `pandas`는 데이터 처리를, `matplotlib`와 `seaborn`은 시각화를 담당합니다. 각 라이브러리의 버전을 확인하여 호환성 문제를 미연에 방지하는 습관을 들이는 것이 좋습니다.

```python
import numpy  as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# warning 메시지는 분석에 직접적인 영향을 주지 않으므로, 깔끔한 출력을 위해 숨깁니다.
import warnings
warnings.filterwarnings('ignore')

# version check
print('numpy  version - ' , np.__version__)
print('pandas version - ' , pd.__version__)
```

### 2.2. 한글 폰트 및 마이너스 부호 설정

> **💡 중요!:** Matplotlib의 기본 폰트는 한글을 지원하지 않습니다. 차트의 제목이나 축 레이블에 한글을 사용하면 아래와 같이 글자가 깨지는 현상(소위 '두부 현상')이 발생합니다. 따라서 운영체제(OS)에 맞는 한글 폰트를 명시적으로 설정해주는 작업이 **반드시** 필요합니다.

운영체제별로 적절한 폰트 경로와 이름을 지정하여 Matplotlib의 전역 설정(`rc`)을 변경합니다.

```python
# 한글 폰트 문제 해결
import platform
from matplotlib import font_manager, rc

# 마이너스 부호가 깨지는 현상을 방지하기 위한 설정
plt.rcParams['axes.unicode_minus'] = False

# OS에 따라 다른 폰트 적용
if platform.system() == 'Darwin': # macOS
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~ ')
```

---

## 3. Matplotlib 기본 문법 마스터하기

> **🤔 왜(Why) 시각화를 해야 할까요?** 로우 데이터(raw data)나 복잡한 통계 수치만으로는 데이터가 가진 패턴, 추세, 이상치 등을 직관적으로 파악하기 매우 어렵습니다. 시각화는 이러한 복잡한 데이터를 한눈에 이해할 수 있는 그래픽 형태로 변환하여, 분석의 깊이를 더하고 설득력 있는 근거를 제시하는 데이터 분석의 핵심적인 과정입니다.

Matplotlib 시각화의 가장 기본적인 3단계 프로세스는 다음과 같습니다.

1.  **그림판(Figure) 만들기**: `plt.figure()` 함수로 차트를 그릴 전체 도화지를 준비합니다.
2.  **그림(Plot) 그리기**: `plt.plot()` 등 다양한 함수로 원하는 차트를 그립니다. 이 단계에서 각종 옵션을 추가하여 차트를 꾸밀 수 있습니다.
3.  **보여주기(Show) 및 닫기(Close)**: `plt.show()`로 완성된 차트를 화면에 표시하고, `plt.close()`로 메모리 리소스를 정리합니다.

### 3.1. 라인 플롯 (Line Plot)

가장 기본적인 선 그래프는 데이터의 시간적 변화나 순서에 따른 추세를 보여주는 데 효과적입니다. `x`축과 `y`축 데이터를 리스트나 배열 형태로 전달하여 그릴 수 있습니다.

```python
# 1. 그림판(Figure) 객체 생성
plt.figure()

# 2. 그림 그리기 (X, Y 좌표 지정 및 다양한 스타일 옵션 추가)
plt.plot([10,30,60,90], # X축 데이터
         [1,4,9,16],   # Y축 데이터
         color = 'red',      # 선 색상
         marker = 'o',       # 각 데이터 포인트의 마커 모양
         ms=15)              # 마커 사이즈 (markersize)

# 차트에 제목과 축 레이블 등 다양한 정보 추가
plt.title('라인 플롯 - 기본')
plt.xlabel('X 축 - ')
plt.ylabel('Y 축 - ', rotation=45) # rotation 옵션으로 레이블 텍스트 회전

# 축의 범위(limit)를 직접 지정하여 원하는 부분만 확대해서 볼 수 있음
plt.xlim(0,100)
plt.ylim(0,17)

# 3. 완성된 차트를 화면에 보여주기
plt.show()
plt.close() # 리소스 해제
```

### 3.2. 서브 플롯 (Subplots)으로 여러 그래프 그리기

하나의 그림판(Figure) 안에 여러 개의 독립된 차트(Axes)를 그리고 싶을 때 서브 플롯을 사용합니다. `fig.add_subplot()`을 이용해 그림판을 원하는 행과 열로 분할하고, 각 영역(Axes 객체)을 지정하여 개별적인 차트를 그릴 수 있습니다.

> **💡 중요!:** 서브플롯의 각 영역(`area01`, `area02` 등)은 `Axes`라는 객체입니다. 이 객체에 제목이나 레이블을 설정할 때는 `plt.title()`과 같은 전역 함수가 아닌, 해당 `Axes` 객체가 가진 메서드인 `area01.set_title()`, `area01.set_xlabel()` 등을 사용해야 합니다. 이것이 Matplotlib의 **객체지향적(Object-Oriented) 방식**이며, 더 복잡하고 세밀한 제어에 유리합니다.

```python
# figsize로 그림판의 전체 크기(가로, 세로 인치)를 지정
fig = plt.figure(figsize = (20,7))

# 1행 3열 중 첫 번째 영역(Axes) 생성
area01 = fig.add_subplot(1,3,1)
area01.set_title('첫 번째 영역')
area01.set_xlabel('X 축')
area01.set_ylabel('Y 축', rotation=0)
# 여기에 area01.plot(...) 등으로 차트를 그릴 수 있습니다.

# 1행 3열 중 두 번째 영역 생성
area02 = fig.add_subplot(1,3,2)
area02.set_title('두 번째 영역')

# 1행 3열 중 세 번째 영역 생성
area03 = fig.add_subplot(1,3,3)
area03.set_title('세 번째 영역')

# 모든 서브플롯이 포함된 Figure를 화면에 표시
plt.show()
plt.close()
```

---

## 4. 주요 차트 유형 및 실전 분석 예제

이제부터는 실제 데이터를 가지고 다양한 종류의 차트를 그리며 데이터 분석과 시각화를 연계하는 방법을 학습합니다.

### 4.1. 막대 차트 (Bar Chart)

> **🤔 왜(Why)?** 막대 차트는 **범주형(Categorical) 데이터**의 수량, 빈도, 비율 등을 비교하여 순위를 보여줄 때 가장 효과적인 시각화 방법입니다. 예를 들어, 성별, 혈액형, 등급, 종류 등 명확히 구분되는 항목들을 비교하는 데 매우 적합합니다.

**타이타닉 데이터셋**을 이용해 `선실 등급(pclass)`별 `생존자 수`를 시각화하는 예제를 진행했습니다. 이 과정은 **[데이터 그룹화] -> [집계] -> [시각화]**의 전형적인 분석 흐름을 보여줍니다.

```python
# Seaborn 라이브러리에 내장된 타이타닉 데이터셋을 로드합니다.
titanicFrm = sns.load_dataset('titanic')

# 1. 데이터 분석: 'pclass'(선실등급)로 그룹화하여 'survived'(생존 여부)의 합계를 구합니다.
# .sum()을 통해 각 등급별 생존자 총 인원을 계산합니다.
surviveByClass = titanicFrm.groupby('pclass')['survived'].sum()

# 분석 결과 확인 (Series 형태)
# pclass
# 1    136
# 2     87
# 3    119
# Name: survived, dtype: int64
print(surviveByClass)

# 2. 시각화
plt.figure(figsize=(15,5))

# plt.bar() 함수를 사용하여 막대 차트를 그립니다.
# .index는 그룹화된 기준(1, 2, 3등급)이므로 x축이 되고,
# .values는 집계된 값(생존자 수)이므로 y축이 됩니다.
plt.bar(surviveByClass.index, surviveByClass.values, color = ['red','green','blue'])

plt.xticks(surviveByClass.index) # x축 눈금을 1, 2, 3으로 명확하게 표시
plt.title('선실 등급별 생존자 수')
plt.xlabel('선실 등급')
plt.ylabel('생존자 수')
plt.show()
plt.close()
```

### 4.2. [시나리오] 보안 로그 데이터 분석 및 시각화

지금부터는 직접 가상 데이터를 생성하여 좀 더 복합적인 분석과 시각화를 진행해보겠습니다. 이 시나리오는 데이터 생성부터 분석, 시각화까지 이어지는 전체 과정을 담고 있습니다.

#### 4.2.1. 가상 데이터(Dummy Data) 생성

> **📌 노트:** 실제 프로젝트에서는 데이터를 수집하고 정제하는 과정이 매우 중요하지만, 학습 단계에서는 분석 및 시각화 기술 자체에 집중하기 위해 `numpy`와 `pandas`를 이용해 가상 데이터를 생성하는 경우가 많습니다. 이는 아이디어를 빠르게 프로토타이핑하는 데 도움이 됩니다.

로그인 시도에 대한 로그 데이터를 가정하여, `timestamp`, `user`, `ip`, `status`, `delay_ms` 컬럼을 가진 데이터프레임을 생성했습니다.

```python
# 시간, 사용자, IP, 상태, 지연시간(ms) 컬럼을 가진 100개의 로그 데이터 생성
timeStamp = pd.date_range('2025-11-06', periods=100, freq='H')
user = np.random.choice(['admin','superAdmin', 'root', 'guest', 'analyst'], size=100)
ip = np.random.choice(['192.168.0.1','192.168.0.3', '192.168.0.5', '192.168.0.7', '192.168.0.9'], size=100)
# p=[0.6, 0.4] 옵션은 SUCCESS가 60%, FAIL이 40% 확률로 나오도록 가중치를 부여합니다.
status = np.random.choice(['SUCCESS','FAIL'], size=100, p=[0.6,0.4])
delay_ms = np.random.randint(20, 80, 100)

frm = pd.DataFrame({
    'timestamp' : timeStamp,
    'user'      : user,
    'ip'        : ip,
    'status'    : status,
    'delay_ms'  : delay_ms
})

frm.head() # 생성된 데이터 확인
```

#### 4.2.2. 로그인 상태별 시도 횟수 (막대 차트)

**[Quiz]** 위에서 생성한 `frm` 데이터프레임을 이용해, 로그인 시도 상태(`status`)별 횟수를 막대 차트로 시각화해보세요.

**[Solution]** `pandas`의 `value_counts()` 함수는 특정 컬럼의 값들이 각각 몇 번씩 나타나는지 계산해주는 매우 유용한 함수입니다. 이 함수의 결과는 바로 시각화에 사용될 수 있는 `Series` 객체입니다.

```python
# 'status' 컬럼의 값(SUCCESS, FAIL)별 개수를 계산
loginStatusCount = frm['status'].value_counts()

plt.figure(figsize=(15,5))
plt.bar(loginStatusCount.index, loginStatusCount.values, color = ['green','red'])
plt.title('로그인 시도 상태별 횟수')
plt.xlabel('상태')
plt.ylabel('횟수', rotation=0)
plt.xticks(loginStatusCount.index)
plt.show()
plt.close()
```

#### 4.2.3. 시간대별 평균 지연 시간 (선 그래프)

**[Quiz]** `frm` 데이터프레임에서 시간대별 평균 지연시간(`delay_ms`)을 선 그래프로 시각화해보세요.

**[Solution]** 이 문제의 핵심은 `timestamp` 타입의 컬럼에서 시간(`hour`) 정보만 추출하여 그룹화하는 것입니다. `pandas`의 `Series.dt` 접근자를 사용하면 datetime 객체의 년, 월, 일, 시간, 분, 초 등의 속성에 쉽게 접근할 수 있습니다.

```python
# 1. 분석: 'timestamp' 컬럼에서 .dt.hour로 시간 정보만 추출하여 그룹화하고, 'delay_ms'의 평균을 계산
delayPerHour = frm.groupby(frm['timestamp'].dt.hour)['delay_ms'].mean()

# 2. 시각화
plt.figure(figsize=(15,5))
plt.plot(delayPerHour.index, delayPerHour.values, color='blue', marker='o', ms=10)
plt.title('시간대별 평균 지연시간')
plt.xlabel('시간대 (0-23시)')
plt.ylabel('평균 지연시간(ms)', rotation=0)
plt.xticks(delayPerHour.index) # x축 눈금을 모든 시간대로 표시
plt.grid() # 가독성을 높이기 위해 그리드(격자) 추가
plt.show()
plt.close()
```

### 4.3. 다중 막대 그래프 & DataFrame 직접 플로팅

`iris` (붓꽃) 데이터셋을 통해 여러 그룹과 여러 수치형 변수를 동시에 비교하는 방법을 학습했습니다. 이 방법은 복잡한 데이터를 한 번에 비교 분석할 때 매우 유용합니다.

> **💡 중요!:** `pandas`의 `groupby()`로 집계된 데이터프레임은 그 자체로 훌륭한 시각화 입력 자료입니다. 데이터프레임 변수 뒤에 `.plot(kind='bar')`를 붙이는 것만으로도, Matplotlib을 직접 사용하는 것보다 훨씬 간편하게 복잡한 다중 막대 그래프를 그릴 수 있습니다. 내부적으로 Pandas가 Matplotlib을 호출하여 그려주는 방식입니다.

```python
irisFrm = sns.load_dataset('iris')

# 품종(species)별로 각 피처(sepal_length 등)의 평균을 계산
groupBySpecies = irisFrm.groupby('species').mean()

# 데이터프레임에서 직접 다중 막대 그래프 그리기
groupBySpecies.plot(kind='bar', figsize=(15,7))
plt.legend(loc='best') # 범례를 최적의 위치에 자동 배치
plt.xticks(rotation=0)    # x축 레이블을 회전시키지 않음
plt.title('Iris 품종별 피처 평균 비교')
plt.ylabel('평균 길이/너비')
plt.show()
plt.close()
```

> **📌 노트: 데이터 관점 바꾸기 - 전치(Transpose)**
> 데이터의 행과 열을 바꾸어 새로운 관점으로 분석하고 싶을 땐 **전치(Transpose)** 행렬을 활용할 수 있습니다. 데이터프레임 변수 뒤에 `.T`를 붙이면 행과 열이 즉시 뒤바뀝니다. 이를 통해 피처를 기준으로 품종별 값을 비교하는 새로운 관점의 그래프를 그릴 수 있습니다.

```python
# .T를 붙여 행과 열을 전환한 후 플로팅
groupBySpecies.T.plot(kind='bar', figsize=(15,7))
plt.title('피처별 Iris 품종 평균 비교')
plt.xticks(rotation=0)
plt.show()
plt.close()
```

### 4.4. 히스토그램 (Histogram)과 데이터 분포

> **🤔 왜(Why)?** 히스토그램은 **연속형 수치 데이터**의 **분포**를 시각화하는 데 특화된 도구입니다. 데이터가 어떤 값의 범위에 얼마나 집중되어 있는지, 전체적으로 어떤 모양(예: 종 모양의 정규분포)을 띄는지, 특정 방향으로 치우쳐 있는지 등을 한눈에 파악할 수 있게 해줍니다.

```python
# 로그인 지연 시간(delay_ms)의 분포를 히스토그램으로 확인
plt.figure(figsize=(15,5))

# bins는 데이터를 몇 개의 구간(막대)으로 나눌지 결정하는 중요한 파라미터입니다.
plt.hist(frm['delay_ms'], bins=20, color='green', edgecolor='black')

plt.title('로그인 지연 분포 히스토그램')
plt.xlabel('지연 시간 (ms)')
plt.ylabel('빈도수(Frequency)', rotation=0)
plt.show()
plt.close()
```

> #### **[심화 학습] AI와 데이터 분포의 중요성**
> 강의 중 강사님께서 데이터 분포의 중요성에 대해 길게 설명해주셨습니다. 인공지능 모델, 특히 딥러닝 모델을 학습시킬 때, 입력 데이터가 **정규분포**에 가까울수록 모델이 안정적으로 학습하고 좋은 성능을 내는 경우가 많습니다. 만약 데이터가 한쪽으로 심하게 치우쳐(skewed) 있다면, 모델이 그 편향된 데이터에만 과하게 학습되는 **과대적합(Overfitting)** 문제가 발생할 수 있습니다. 이는 마치 특정 유형의 문제만 풀어본 학생이 새로운 유형의 시험 문제를 풀지 못하는 것과 같습니다. 히스토그램은 이러한 데이터의 편향성을 시각적으로 진단하고, 추후 정규화(Normalization)나 표준화(Standardization) 같은 전처리 기법을 적용해야 할지 판단하는 중요한 첫걸음입니다.

### 4.5. 카운트 플롯 (Count Plot) - Seaborn 활용

`Seaborn`은 Matplotlib을 기반으로 더 아름답고 통계적인 그래프를 훨씬 쉽게 그릴 수 있게 해주는 라이브러리입니다. `countplot`은 Seaborn 스타일의 빈도 기반 막대 그래프입니다.

`countplot`의 가장 큰 장점 중 하나는 `hue` 파라미터입니다. 이를 사용하면, 하나의 기준(`x='user'`)에 대해 다른 범주(`hue='status'`)를 색상으로 자동 구분하여 표현할 수 있어 매우 편리하고 직관적입니다.

```python
plt.figure(figsize=(15,5))

# data=frm으로 데이터프레임을 통째로 넘겨주고, x축과 hue에 컬럼 이름만 지정합니다.
sns.countplot(data=frm, x='user', hue='status', palette='Set2')

plt.title('사용자별 로그인 성공/실패 횟수')
plt.show()
plt.close()
```

### 4.6. 박스 플롯 (Box Plot) - 이상치(Outlier) 탐지

> **🤔 왜(Why)?** 박스 플롯은 데이터의 분포를 요약해서 보여주는 동시에, 정상 범주에서 크게 벗어난 **이상치(Outlier)**를 탐지하고 시각화하는 데 매우 효과적인 도구입니다. 데이터의 품질을 검증하고 정제하는 과정에서 필수적으로 사용됩니다.

> **💡 중요!: 박스 플롯의 구성 요소와 원리**
> - **Q1 (1사분위수)**: 데이터를 오름차순으로 정렬했을 때 하위 25%에 해당하는 값.
> - **Q3 (3사분위수)**: 데이터를 오름차순으로 정렬했을 때 상위 25% (즉, 75%)에 해당하는 값.
> - **IQR (Interquartile Range)**: `Q3 - Q1`. 데이터의 중간 50%가 모여있는 범위로, 데이터의 퍼짐 정도를 나타냅니다.
> - **중앙값(Median, Q2)**: 박스 안의 선. 데이터의 중심 위치를 나타냅니다.
> - **수염(Whisker)**: 박스 바깥으로 뻗어나간 선. 일반적으로 `Q1 - 1.5 * IQR`과 `Q3 + 1.5 * IQR` 범위 내에 있는 최대/최소값을 나타냅니다.
> - **이상치(Outlier)**: 수염의 범위를 벗어나는 값들. 다이아몬드나 점 등의 마커로 명확하게 표시됩니다.

#### 🔐 보안 노트: 이상치 탐지의 보안적 의미
로그인 지연 시간 데이터에서 이상치를 탐지하는 것은 보안 관점에서 매우 중요한 의미를 가집니다. 예를 들어,
- **비정상적으로 긴 지연 시간(상한 이상치)**: 시스템에 과부하를 주려는 서비스 거부(DoS) 공격의 징후일 수 있습니다.
- **특정 계정에서 짧은 시간 동안 수많은 로그인 실패(이상치 패턴)**: 비밀번호를 알아내려는 무차별 대입 공격(Brute-force)이나 사전 대입 공격(Dictionary Attack)을 강력하게 의심해볼 수 있습니다.

이러한 이상치를 탐지하고 분석함으로써 잠재적인 보안 위협에 선제적으로 대응할 수 있습니다.

```python
# 정상 데이터와 이상치 데이터를 의도적으로 섞어 가상 데이터 생성
boxFrm = pd.DataFrame({
    'user'      : np.random.choice(['admin', 'root', 'guest'], 100),
    'delay_ms'  : np.concatenate([
                    np.random.normal(200, 50, 80),  # 정상 데이터 (평균 200, 표준편차 50)
                    np.random.normal(800, 20, 10),  # 상한 이상치 (평균 800)
                    np.random.normal(100, 20, 10)   # 하한 이상치 (평균 100)
                  ])
})

# 박스 플롯 시각화
plt.figure(figsize=(15,5))
sns.boxplot(data=boxFrm, x='user', y='delay_ms', palette='Set3')

# stripplot을 함께 그리면 실제 데이터 포인트의 분포를 같이 볼 수 있어 더 유용합니다.
# jitter=True는 점들이 겹치지 않도록 좌우로 약간 흩뿌려주는 옵션입니다.
sns.stripplot(data=boxFrm, x='user', y='delay_ms', color='red', size=5, jitter=True, alpha = 0.7)

plt.title('사용자별 로그인 지연 시간 분포와 이상치 탐지')
plt.xlabel('사용자')
plt.ylabel('지연 시간 (ms)')
plt.show()
plt.close()
```

### 4.7. 산점도 (Scatter Plot)와 변수 간 관계 분석

> **🤔 왜(Why)?** 산점도는 **두 연속형 변수 간의 관계**를 파악하는 데 사용됩니다. X축과 Y축에 각각의 변수를 놓고 데이터 포인트들을 점으로 찍어, 점들이 모여있는 패턴을 통해 두 변수 간에 양의 상관관계, 음의 상관관계가 있는지, 혹은 아무 관계가 없는지를 시각적으로 확인할 수 있습니다.

**[Quiz]** 사용자별 행동 패턴을 종합적으로 탐지하기 위해, ①평균 로그인 지연시간, ②로그인 실패율, ③총 시도 횟수를 **하나의 산점도**에 모두 표현해보세요.
- **x축**: 평균 로그인 지연 시간
- **y축**: 실패율
- **점 크기**: 총 시도 횟수
- **점 색상**: 사용자 구분

**[Solution]** 이 문제는 여러 분석 단계를 거쳐야 하는 복합적인 문제입니다. 각 사용자별로 필요한 지표들을 계산한 후, 이를 새로운 데이터프레임으로 만들어 `seaborn`의 `scatterplot`에 매핑하는 과정이 필요합니다.

```python
# 1. 사용자별 분석 데이터 계산
# 사용자별 평균 지연시간
avg_delay = scatterFrm.groupby('user')['delay_ms'].mean()
# 사용자별 실패율 (apply와 lambda 함수 활용)
fail_ratio = scatterFrm.groupby('user')['status'].apply(lambda x: (x == 'FAIL').mean())
# 사용자별 시도 횟수
attempts = scatterFrm['user'].value_counts()

# 2. 분석 결과를 새로운 데이터프레임으로 생성
userStatus = pd.DataFrame({
    'avg_delay' : avg_delay,
    'fail_ratio' : fail_ratio,
    'attempts' : attempts
})

# 3. 산점도 시각화 (Seaborn 활용)
plt.figure(figsize=(15, 7))
sns.scatterplot(x='avg_delay',          # x축
                y='fail_ratio',         # y축
                size='attempts',        # 점의 크기로 시도 횟수 표현
                sizes=(50, 500),        # 점 크기 범위 조절
                hue=userStatus.index,   # 점의 색상으로 사용자 구분
                data=userStatus)

plt.title('사용자별 로그인 행동 패턴 분석 (평균지연, 실패율, 시도횟수)')
plt.xlabel('평균 지연 시간 (ms)')
plt.ylabel('실패율')
plt.legend(title='User')
plt.grid(True)
plt.show()
plt.close()
```
이 그래프를 통해, 예를 들어 **시도 횟수(큰 점)가 많으면서 실패율(y축 값이 높음)도 높은 사용자**를 비정상적인 행동 패턴으로 의심하고 집중적으로 분석하는 등의 인사이트를 얻을 수 있습니다.

### 4.8. 히트맵 (Heatmap)과 상관관계/피벗 테이블 시각화

> **🤔 왜(Why)?** 히트맵은 행렬(Matrix) 형태의 데이터를 색상의 농도(진하고 옅음)로 표현하는 시각화 기법입니다. 주로 변수들 간의 **상관관계 행렬(Correlation Matrix)**이나, 데이터를 특정 기준으로 재구조화한 **피벗 테이블(Pivot Table)**의 결과를 시각화하는 데 매우 효과적입니다.

#### 4.8.1. 상관관계 행렬 시각화

```python
# iris 데이터의 수치형 컬럼 간 상관관계를 계산합니다.
corr = irisFrm.corr(numeric_only=True)

plt.figure(figsize=(10, 8))

# annot=True는 각 셀에 실제 상관계수 값을 표시해주는 옵션입니다.
# fmt='.2f'는 소수점 둘째 자리까지 표시하라는 의미입니다.
# cmap은 히트맵의 전체적인 색상 테마를 지정합니다.
sns.heatmap(corr, fmt='.2f', annot=True, linewidth=0.5, cmap='YlGnBu')

plt.title('Iris 데이터 피처 간 상관관계 히트맵')
plt.show()
plt.close()
```
이 히트맵을 통해 `petal_length`와 `petal_width`가 0.96이라는 매우 강한 양의 상관관계를 가짐을 한눈에 알 수 있습니다.

#### 4.8.2. 피벗 테이블(Pivot Table)과 히트맵

> **💡 중요!:** 히트맵은 행과 열이 명확한 2차원 데이터(행렬)에 적합합니다. 일반적인 로그 데이터처럼 1차원적으로 나열된 데이터는 바로 히트맵으로 그릴 수 없습니다. 이럴 때 `pandas`의 `pivot_table` 함수를 사용하면, 특정 컬럼들을 각각 `index`(행), `columns`(열)로 지정하고 원하는 값을 `values`로 채워 데이터를 2차원 행렬 형태로 재구조화할 수 있습니다. 이는 히트맵 시각화를 위한 필수적인 전처리 과정입니다.

**[Quiz]** `frm` 데이터를 이용해 `사용자(user)`와 `로그인 상태(status)`에 따른 `평균 지연 시간(delay_ms)`을 히트맵으로 시각화해보세요.

```python
# 1. 피벗 테이블 생성
# index='user', columns='status', values='delay_ms'로 피벗 테이블을 생성합니다.
# aggfunc='mean'은 각 셀의 값을 평균으로 채우라는 의미입니다.
pivot = frm.pivot_table(index='user', columns='status', values='delay_ms', aggfunc='mean')

# 2. 히트맵 시각화
plt.figure(figsize=(12, 8))
sns.heatmap(pivot, fmt='.2f', annot=True, linewidth=0.5, cmap='viridis')
plt.title('사용자 및 상태별 평균 지연 시간 히트맵')
plt.show()
plt.close()
```
이 히트맵을 통해 특정 사용자(예: `admin`)가 로그인 실패(`FAIL`) 시 평균 지연 시간이 다른 경우보다 유독 높은지(색이 밝은지) 등을 한눈에 비교하고 파악할 수 있습니다.

---

## 5. [실습 퀴즈] 자동차 연비(MPG) 데이터 분석 및 시각화

강의 막바지에는 `mpg_visualization.xlsx` 파일을 이용한 실습 퀴즈가 있었습니다. 배운 내용을 총동원하여 문제를 해결하는 과정입니다.

```python
# 데이터 로드
filePath = './mpg_visualization.xlsx'
mpgFrm = pd.read_excel(filePath, index_col = 0)
```

**Q1) 배기량(displ) 4 이하인 자동차와 5 이상인 자동차 중 어느 쪽의 고속도로 평균연비(hwy)가 더 높은지 비교 시각화하세요.**

```python
# 4 이하 그룹과 5 이상 그룹으로 나누어 평균 연비 계산
dispLComp = mpgFrm.groupby(mpgFrm['displ'] <= 4)['hwy'].mean()
dispLComp.index = ['5 이상', '4 이하'] # boolean 인덱스를 알아보기 쉽게 변경

plt.figure(figsize=(10,6))
plt.bar(dispLComp.index, dispLComp.values, color=['red','skyblue'])
plt.title('배기량에 따른 고속도로 연비 비교')
plt.ylabel('평균 고속도로 연비(hwy)')
plt.show()
plt.close()
```

**Q2) `audi`와 `toyota` 두 제조사의 도시연비(cty) 평균을 비교 시각화하세요.**

```python
# isin()을 사용하여 두 제조사 데이터만 필터링 후 그룹화
brandComp = mpgFrm[mpgFrm['manufacturer'].isin(['audi','toyota'])].groupby('manufacturer')['cty'].mean()

plt.figure(figsize=(10,6))
plt.bar(brandComp.index, brandComp.values, color='purple')
plt.title('audi vs toyota 도시 연비 비교')
plt.ylabel('평균 도시 연비(cty)')
plt.show()
plt.close()
```

**Q3) `chevrolet`, `ford`, `honda` 세 제조사의 고속도로 연비(hwy) 평균을 시각화하세요.**

```python
cfhComp = mpgFrm[mpgFrm['manufacturer'].isin(['chevrolet', 'ford', 'honda'])].groupby('manufacturer')['hwy'].mean()

plt.figure(figsize=(12,6))
plt.bar(cfhComp.index, cfhComp.values, color=['red','green','blue'])
plt.title('주요 3사 고속도로 연비 비교')
plt.ylabel('평균 고속도로 연비(hwy)')
plt.show()
plt.close()
```

**Q4) 구동방식(drv)별 고속도로 연비(hwy) 평균을 막대 그래프로 시각화하세요.**

```python
transHwyComp = mpgFrm.groupby('drv')['hwy'].mean()

plt.figure(figsize=(10,6))
plt.bar(transHwyComp.index, transHwyComp.values, color=['orange','purple','cyan'])
plt.title('구동방식별 고속도로 연비 평균')
plt.xlabel('구동방식 (f:전륜, r:후륜, 4:4륜)')
plt.ylabel('평균 고속도로 연비(hwy)')
plt.show()
plt.close()
```

**Q5) 구동방식(drv)별 고속도로(hwy) 및 도시연비(cty) 평균을 다중 막대 그래프로 시각화하세요.**

```python
drvCtyHwyComp = mpgFrm.groupby('drv')[['cty','hwy']].mean()

drvCtyHwyComp.plot(kind='bar', figsize=(15,7))
plt.title('구동방식별 도시 및 고속도로 연비 평균')
plt.ylabel('평균 연비')
plt.xticks(rotation=0)
plt.show()
plt.close()
```

**Q6) 자동차 종류(class)별 빈도수를 시각화하세요.**

```python
classCount = mpgFrm['class'].value_counts()

plt.figure(figsize=(15,7))
plt.bar(classCount.index, classCount.values, color='lightgreen')
plt.title('자동차 클래스별 빈도수')
plt.xticks(rotation=45)
plt.ylabel('차량 대수')
plt.show()
plt.close()
```

---

## 🧩 복합 및 심화 예제: AI 연동 시나리오

강의에서 배운 내용을 종합하여, 데이터 분석 결과를 AI 서비스와 연동하는 가상 시나리오를 구성해보았습니다.

### 1. 데이터 준비 및 분석 함수 정의

먼저, 비정상적인 행동 패턴(예: 실패율이 50% 이상이고 시도 횟수가 20회 이상인 사용자)을 보이는 사용자를 탐지하는 함수를 정의합니다.

```python
def detect_suspicious_users(df):
    """
    로그 데이터에서 의심스러운 사용자를 탐지하는 함수
    """
    # 사용자별 분석 데이터 계산
    avg_delay = df.groupby('user')['delay_ms'].mean()
    fail_ratio = df.groupby('user')['status'].apply(lambda x: (x == 'FAIL').mean())
    attempts = df['user'].value_counts()

    # 분석 결과를 데이터프레임으로 합치기
    user_status = pd.DataFrame({
        'avg_delay': avg_delay,
        'fail_ratio': fail_ratio,
        'attempts': attempts
    })

    # 의심스러운 사용자 필터링 (실패율 50% 이상, 시도 횟수 20회 이상)
    suspicious = user_status[(user_status['fail_ratio'] >= 0.5) & (user_status['attempts'] >= 20)]
    
    return suspicious

# 함수 실행
suspicious_users = detect_suspicious_users(frm)
print("--- 탐지된 의심스러운 사용자 ---")
print(suspicious_users)
```

### 2. AI 연동 시뮬레이션

탐지된 사용자 정보를 `JSON` 형식으로 변환하여 가상의 AI 분석 서비스에 요청을 보내고, 응답을 받아 후속 조치를 하는 과정을 시뮬레이션합니다.

```python
# 1. 분석된 데이터를 JSON으로 변환 (AI 서비스 요청 데이터)
# to_json() 메서드를 사용하면 데이터프레임을 쉽게 JSON으로 변환 가능
request_data_json = suspicious_users.reset_index().to_json(orient='records')

print("\n--- AI 서비스 요청 (JSON) ---")
print(request_data_json)


# 2. AI가 분석 후 정형화된 JSON으로 응답했다고 가정
ai_response_json = """
{
  "analysis_id": "a-1234-xyz",
  "timestamp": "2025-11-06T15:30:00Z",
  "summary": {
    "risk_level": "High",
    "detected_patterns": ["Brute-force attempt suspected"],
    "confidence_score": 0.85
  },
  "details": [
    {
      "user": "guest",
      "fail_ratio": 0.6,
      "attempts": 25,
      "recommended_action": "Temporarily block user account and associated IP."
    }
  ]
}
"""

# 3. AI의 JSON 응답을 파싱하여 후속 조치 실행
import json
parsed_response = json.loads(ai_response_json)

risk_level = parsed_response['summary']['risk_level']
action = parsed_response['details'][0]['recommended_action']

print("\n--- AI 분석 결과 및 후속 조치 ---")
print(f"위험 수준: {risk_level}")
print(f"권장 조치: {action}")

if risk_level == "High":
    print(">> 위험 수준 'High' 감지. 자동 차단 프로세스를 시작합니다.")
```
이처럼 데이터 분석 및 시각화는 단순히 현상을 파악하는 것을 넘어, 자동화된 시스템이나 AI와 연동하여 실질적인 액션으로 이어지는 중요한 첫 단계가 될 수 있음을 배웠습니다.