# 📝 Python 웹 시각화와 Streamlit 마스터 클래스 강의 노트 (5일차)

금요일 아침, 한 주를 마무리하는 설렘과 함께 5일차 강의를 시작했습니다. 오늘은 어제까지 배웠던 정적인 시각화의 한계를 넘어, 웹 환경에서 사용자와 상호작용하는 동적 시각화를 구축하는 매우 흥미로운 주제들을 다루었습니다. 특히, Python만으로 멋진 웹 대시보드를 만들 수 있는 **Streamlit**의 강력함을 체감할 수 있었고, 다가올 미니 프로젝트와 LLM/LangChain 학습에 대한 기대감을 높이는 시간이었습니다.

---

## 1. 어제 학습 내용 복습: 자동차 연비(MPG) 데이터 분석 퀴즈 풀이

본격적인 진도를 나가기 전에, 어제 마지막 시간에 내주셨던 자동차 연비(MPG) 데이터셋 분석 퀴즈를 함께 풀어보는 시간을 가졌습니다. 이 과정은 데이터 분석의 전형적인 흐름인 **[데이터 로드] -> [데이터 탐색 및 이해] -> [조건에 따른 데이터 필터링/그룹화] -> [집계] -> [시각화]**를 복습하는 좋은 기회였습니다.

### 1.1. 데이터 로드 및 탐색

먼저, 분석할 `mpg_visualization.xlsx` 파일을 `pandas`를 이용해 로드합니다.

> **💡 중요!:** `pd.read_excel()` 함수에서 `index_col=0` 옵션을 사용하는 것이 핵심입니다. 이 옵션은 엑셀 파일의 첫 번째 열(0번째)을 DataFrame의 인덱스로 사용하도록 지정합니다. 이 옵션이 없으면, 엑셀의 인덱스 열이 \'Unnamed: 0\'라는 불필요한 컬럼으로 로드될 수 있습니다.

```python
import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일 로드 (첫 번째 열을 인덱스로 지정)
mpgFrm = pd.read_excel(\'./SK_Rookies/data/mpg_visualization.xlsx\', index_col=0)

# 데이터의 기본 정보 확인
print("--- 데이터 정보 (info) ---")
mpgFrm.info()

# 데이터의 상위 5개 행 확인
print("\\n--- 데이터 샘플 (head) ---")
print(mpgFrm.head())

# 주요 컬럼의 고유값 확인
print("\\n--- 실린더(cyl) 고유값 ---")
print(mpgFrm[\'cyl\'].unique())
print("\\n--- 구동방식(drv) 고유값 ---")
print(mpgFrm[\'drv\'].unique())
```

#### 💻 코드 실행 상세 분석
1.  **1단계 (라이브러리 임포트):** 데이터 분석을 위해 `pandas`를 `pd`라는 별칭으로, 시각화를 위해 `matplotlib.pyplot`을 `plt`라는 별칭으로 임포트합니다.
2.  **2단계 (파일 로드):** `pd.read_excel()` 함수가 호출되어 지정된 경로의 엑셀 파일을 읽어옵니다. `index_col=0` 인자 덕분에 첫 번째 열이 DataFrame의 인덱스로 설정됩니다. 이 결과가 `mpgFrm` 변수에 DataFrame 객체로 할당됩니다.
3.  **3단계 (정보 출력):**
    *   `mpgFrm.info()` 메서드가 호출되어 DataFrame의 전체적인 요약 정보(총 행 개수, 컬럼별 non-null 개수 및 데이터 타입 등)를 출력합니다. 이를 통해 결측치가 없는 깔끔한 데이터임을 확인했습니다.
    *   `mpgFrm.head()` 메서드가 호출되어 데이터의 실제 모습을 파악하기 위해 상위 5개 행을 출력합니다.
    *   `mpgFrm[\'cyl\'].unique()` 와 같이 특정 컬럼을 선택하고 `.unique()` 메서드를 호출하여 해당 컬럼에 어떤 고유한 값들이 있는지(범주형 데이터의 종류) 확인합니다.

### 1.2. 퀴즈 풀이 및 시각화

#### **Q1) 배기량(displ) 4 이하인 자동차와 5 이상인 자동차 중 어느 쪽의 고속도로 평균연비(hwy)가 더 높은지 비교 시각화하세요.**

> **📌 노트:** 이 문제는 `boolean 인덱싱`을 활용하여 조건에 맞는 데이터를 필터링하는 능력을 확인하는 것이 핵심입니다. `mpgFrm[\'displ\'] <= 4`와 같은 조건식은 각 행이 조건을 만족하는지에 따라 `True` 또는 `False` 값을 갖는 `Series`를 반환하며, 이를 이용해 원하는 행만 선택할 수 있습니다.

```python
# 배기량 4 이하 차량의 고속도로 평균 연비 계산
hwy_low_displ = mpgFrm[mpgFrm[\'displ\'] <= 4][\'hwy\'].mean()

# 배기량 5 이상 차량의 고속도로 평균 연비 계산
hwy_high_displ = mpgFrm[mpgFrm[\'displ\'] >= 5][\'hwy\'].mean()

# 시각화를 위한 데이터 준비
labels = [\'4 이하\', \'5 이상\']
values = [hwy_low_displ, hwy_high_displ]

# 막대 그래프 시각화
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=[\'skyblue\', \'salmon\'])
plt.title(\'배기량에 따른 고속도로 연비 비교\')
plt.ylabel(\'평균 고속도로 연비(hwy)\')
plt.show()
plt.close()
```

#### 💻 코드 실행 상세 분석
1.  **1단계 (데이터 필터링 및 집계):**
    *   `mpgFrm[\'displ\'] <= 4` 조건으로 배기량이 4 이하인 행들만 선택합니다.
    *   선택된 행들에서 `[\'hwy\']` 컬럼(고속도로 연비)만 추출합니다.
    *   `.mean()` 메서드를 호출하여 평균값을 계산하고, `hwy_low_displ` 변수에 할당합니다.
    *   배기량 5 이상에 대해서도 동일한 과정을 반복하여 `hwy_high_displ`에 할당합니다.
2.  **2단계 (시각화 데이터 생성):** `plt.bar()` 함수에 전달하기 위해 x축 레이블(`labels`)과 y축 값(`values`)을 리스트로 만듭니다.
3.  **3단계 (차트 생성 및 표시):**
    *   `plt.figure()`로 그림판을 준비하고, `plt.bar()` 함수에 `labels`와 `values`를 전달하여 막대 그래프를 그립니다.
    *   `plt.title()`, `plt.ylabel()`로 차트에 정보를 추가합니다.
    *   `plt.show()`를 통해 완성된 차트를 화면에 출력합니다.

**최종 결과:** 배기량이 4 이하인 차량들의 평균 고속도로 연비가 5 이상인 차량들보다 훨씬 높다는 것을 시각적으로 명확하게 확인할 수 있었습니다.

---

## 2. 오늘의 학습 목표: 정적(Static) 시각화를 넘어서

> **🤔 왜(Why) 새로운 시각화 도구가 필요할까요?**\
> 어제까지 사용한 `Matplotlib`은 매우 강력하고 기본적인 시각화 라이브러리이지만, 생성된 차트가 정적인 이미지라는 한계가 있습니다. 사용자가 차트의 특정 부분에 마우스를 올려 상세 정보를 보거나, 특정 영역을 확대/축소하는 등의 **상호작용(Interaction)**이 불가능합니다. 미니 프로젝트나 실제 웹 서비스에서는 사용자와 상호작용하며 데이터를 탐색할 수 있는 동적인 시각화가 훨씬 더 유용합니다.

오늘 배울 라이브러리들은 바로 이러한 필요성을 충족시켜 줍니다.

-   **`Folium`**: 지도 위에 데이터를 시각화하는 데 특화된 라이브러리입니다.
-   **`Plotly`**: `Matplotlib`보다 더 세련되고, 마우스 호버, 줌, 드래그 등 다양한 인터랙션을 기본적으로 지원하는 웹 친화적인 시각화 라이브러리입니다.
-   **`Streamlit`**: **Python 코드만으로** 복잡한 프론트엔드 지식(HTML, CSS, JS) 없이도 빠르고 쉽게 데이터 기반의 웹 애플리케이션(대시보드)을 만들 수 있게 해주는 혁신적인 프레임워크입니다.

---

## 3. `Folium`을 이용한 인터랙티브 지도 시각화

`Folium`은 파이썬으로 Leaflet.js 지도를 다룰 수 있게 해주는 라이브러리로, 위도/경도 데이터만 있으면 손쉽게 인터랙티브한 지도를 만들 수 있습니다.

### 3.1. `Folium` 설치

`Folium`은 아나콘다 기본 환경에 포함되어 있지 않으므로, 별도의 설치가 필요합니다. 아나콘다 프롬프트(Anaconda Prompt)를 열어 아래 명령어로 설치를 진행했습니다.

> **📌 노트:** `conda-forge`는 아나콘다의 기본 채널 외에 다양한 패키지를 제공하는 커뮤니티 기반 채널입니다. 많은 과학/데이터 분석 패키지들이 `conda-forge`를 통해 배포됩니다.

```bash
# Anaconda Prompt에서 실행
conda install -c conda-forge folium
```

### 3.2. 기본 지도 생성 및 마커 추가

`folium.Map` 객체를 생성하는 것이 지도 시각화의 첫걸음입니다. `location` 파라미터에 `[위도, 경도]`를 리스트 형태로 전달하여 지도의 초기 중심점을 설정합니다.

```python
import folium

# 1. 지도 객체 생성 (동국대학교 위치를 중심으로)
# location=[위도, 경도], zoom_start는 초기 확대 레벨
map = folium.Map(location=[37.5574771, 127.0020518], zoom_start=15)

# 2. 마커 추가
# folium.Marker()로 특정 위치에 마커를 생성합니다.
# popup은 마커를 클릭했을 때 나타나는 텍스트입니다.
# .add_to(map) 메서드를 이용해 생성된 마커를 지도 객체에 추가합니다.
folium.Marker([37.5574771, 127.0020518], popup=\'동국대학교\').add_to(map)

# 3. 원형 마커(CircleMarker) 추가
folium.CircleMarker(
    location=[37.5574771, 127.0020518],
    radius=50, # 원의 반지름
    color=\'#ff0000\', # 원의 테두리 색상
    fill_color=\'#ff0000\', # 원의 채우기 색상
    popup=\'학술관\'
).add_to(map)


# Jupyter Notebook 환경에서는 변수 이름만 마지막에 입력하면 지도가 출력됩니다.
map
```

#### 💻 코드 실행 상세 분석
1.  **1단계 (지도 생성):** `folium.Map()` 함수가 호출되어, `location`으로 지정된 위도/경도를 중심으로 하는 Leaflet 지도 객체를 생성하고 `map` 변수에 할당합니다.
2.  **2단계 (마커 추가):**
    *   `folium.Marker()`가 호출되어 지정된 위치에 기본 마커 객체를 생성합니다.
    *   생성된 마커 객체의 `.add_to(map)` 메서드가 호출되어, 1단계에서 만든 `map` 객체 위에 마커가 추가됩니다.
3.  **3단계 (원형 마커 추가):** `folium.CircleMarker()`가 호출되어 다양한 스타일 옵션(반지름, 색상 등)을 가진 원형 마커 객체를 생성하고, 마찬가지로 `.add_to(map)`을 통해 지도에 추가됩니다.
4.  **최종 결과:** `map` 변수를 실행하면, 두 종류의 마커가 추가된 인터랙티브한 지도가 Jupyter Notebook 셀에 렌더링됩니다. 사용자는 이 지도를 확대/축소하거나 드래그할 수 있습니다.

### 3.3. [실습] DataFrame 데이터를 이용한 다중 마커 표시

데이터프레임에 있는 여러 장소의 위도/경도 정보를 읽어와 지도에 모두 표시하는 실습을 진행했습니다.

**[Quiz]** `서울지역_대학교_위치.xlsx` 파일을 읽어, 모든 대학교의 위치를 지도 위에 마커로 표시해보세요.

```python
import folium
import pandas as pd

# 1. 데이터 로드
seoulUniFrm = pd.read_excel(\'./SK_Rookies/data/서울지역_대학교_위치.xlsx\', index_col=0)

# 2. 기본 지도 생성 (서울 중심)
map = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 3. 반복문을 이용한 다중 마커 추가
# for 반복문으로 DataFrame의 인덱스(대학교 이름)를 하나씩 순회합니다.
for name in seoulUniFrm.index:
    # .loc[행, 열]을 사용하여 해당 대학교의 위도와 경도를 가져옵니다.
    lat = seoulUniFrm.loc[name, \'위도\']
    lng = seoulUniFrm.loc[name, \'경도\']
    
    # 가져온 정보로 마커를 생성하고 지도에 추가합니다.
    folium.Marker([lat, lng], popup=name).add_to(map)

# 4. 결과 지도 출력
map
```

#### 💻 코드 실행 상세 분석
1.  **1단계 (데이터 로드 및 지도 생성):** 이전과 동일하게 `pandas`로 엑셀 파일을 읽고, `folium`으로 기본 지도를 생성합니다.
2.  **2단계 (반복문 실행):** `for name in seoulUniFrm.index:` 구문이 실행되어, `seoulUniFrm` DataFrame의 인덱스(대학교 이름 문자열)를 처음부터 끝까지 하나씩 `name` 변수에 할당하며 루프를 돕니다.
3.  **3단계 (데이터 추출 및 마커 생성):**
    *   루프의 각 반복마다, `seoulUniFrm.loc[name, \'위도\']` 코드가 실행됩니다. `name` 변수에 현재 할당된 대학교 이름(예: \'KAIST 서울캠퍼스\')을 행 인덱서로, \'위도\'를 열 인덱서로 사용하여 해당 셀의 위도 값을 찾아 `lat` 변수에 저장합니다. 경도 값도 동일한 방식으로 `lng` 변수에 저장됩니다.
    *   `folium.Marker([lat, lng], popup=name).add_to(map)` 코드가 실행되어, 방금 추출한 위도/경도 위치에 현재 대학교 이름(`name`)을 팝업으로 갖는 마커를 생성하고 지도에 추가합니다.
4.  **최종 결과:** 루프가 모든 대학교에 대해 반복을 마치면, `map` 객체에는 모든 대학교의 위치에 마커가 추가된 상태가 됩니다. 이 `map` 변수를 실행하면 모든 마커가 표시된 최종 지도가 출력됩니다.

---

## 4. `Plotly`를 이용한 고급 인터랙티브 시각화

`Plotly`는 `Matplotlib`이나 `Seaborn`보다 더 미려하고, 풍부한 인터랙션을 제공하는 모던한 시각화 라이브러리입니다. 특히 `Plotly Express` 모듈을 사용하면 매우 간결한 코드로 복잡한 그래프를 그릴 수 있습니다.

### 4.1. `Plotly` 설치

```bash
# Anaconda Prompt에서 실행
pip install plotly
```

### 4.2. `Plotly Express` 기본 사용법

`Plotly Express`는 보통 `px`라는 별칭으로 임포트하여 사용합니다. 대부분의 함수는 첫 번째 인자로 `DataFrame`을 받고, `x`, `y`, `color`, `title` 등의 파라미터에 컬럼 이름을 문자열로 지정하는 직관적인 방식을 사용합니다.

```python
import plotly.express as px

# 가상 데이터 생성
frm = pd.DataFrame({
    \'Country\' : [\'한국\', \'미국\', \'일본\', \'호주\'],
    \'Gdp\' : [1000, 2000, 3000, 4000],
    \'Population\' : [100,200,300,400]
})

# Plotly Express로 막대 그래프 생성
fig_bar = px.bar(frm, 
                 x=\'Country\', 
                 y=\'Gdp\', 
                 title=\'국가별 GDP\', 
                 color=\'Country\') # color 파라미터에 범주형 컬럼을 지정하면 자동으로 색상을 구분해줍니다.

# Plotly Express로 산점도 생성
fig_scatter = px.scatter(frm, 
                         x=\'Population\', 
                         y=\'Gdp\', 
                         hover_name=\'Country\', # 마우스를 올렸을 때 표시될 이름 지정
                         title=\'GDP vs Population\')

# .show() 메서드를 호출하여 그래프를 별도의 브라우저 탭이나 창에 표시합니다.
fig_bar.show()
fig_scatter.show()
```

#### 💻 코드 실행 상세 분석
1.  **1단계 (객체 생성):** `px.bar()` 함수가 호출됩니다. 이 함수는 `frm` 데이터프레임을 입력받아, `x`축에는 \'Country\' 컬럼 값을, `y`축에는 \'Gdp\' 컬럼 값을 매핑하여 막대 그래프 객체를 생성합니다. 이 객체가 `fig_bar` 변수에 할당됩니다.
2.  **2단계 (객체 표시):** `fig_bar.show()` 메서드가 호출됩니다. 이 메서드는 `fig_bar` 객체가 가진 시각화 정보를 바탕으로 HTML/JavaScript 코드를 생성하고, 웹 브라우저를 통해 인터랙티브한 차트를 렌더링합니다.
3.  **3단계 (산점도 생성 및 표시):** `px.scatter()` 함수와 `.show()` 메서드에 대해서도 위와 동일한 과정이 반복됩니다.
4.  **최종 결과:** 두 개의 인터랙티브 차트가 각각 화면에 표시됩니다. 사용자는 마우스를 막대나 점 위에 올려 상세 수치를 확인하거나, 특정 영역을 드래그하여 확대하는 등의 상호작용을 할 수 있습니다.

---

## 5. `Streamlit`으로 나만의 웹 대시보드 만들기

대망의 `Streamlit` 시간입니다. `Streamlit`은 데이터 과학자와 분석가들이 Python 스크립트만으로 빠르고 쉽게 데이터 기반의 웹 애플리케이션을 만들 수 있도록 도와주는 혁신적인 프레임워크입니다.

### 5.1. `Streamlit` 및 `Pydeck` 설치

`Streamlit`과 함께 지도 시각화를 위해 `Pydeck` 라이브러리도 설치합니다.

```bash
# Anaconda Prompt에서 실행
pip install streamlit
pip install pydeck
```

### 5.2. 개발 환경 구축 (VSCode & Conda 연동)

> **💡 중요!:** `Streamlit` 앱은 일반 Python 스크립트(`.py` 파일)이므로, Jupyter Notebook보다는 VSCode와 같은 코드 에디터에서 작업하는 것이 훨씬 효율적입니다. 강사님께서는 아나콘다 환경을 VSCode와 연동하여, 우리가 이미 설치한 라이브러리들을 그대로 사용하는 방법을 상세히 안내해주셨습니다.

1.  **프로젝트 폴더 생성:** 원하는 위치에 `streamlit_pjt`와 같은 프로젝트 폴더를 생성합니다.
2.  **VSCode에서 폴더 열기:** VSCode를 실행하고 `파일 > 폴더 열기` 메뉴를 통해 방금 만든 프로젝트 폴더를 엽니다.
3.  **Python 확장(Extension) 설치:** VSCode 좌측의 확장 탭에서 \'Python\'을 검색하여 Microsoft에서 제공하는 공식 확장 프로그램을 설치합니다.
4.  **인터프리터 선택:**
    *   `Ctrl + Shift + P`를 눌러 명령어 팔레트(Command Palette)를 엽니다.
    *   `Python: Select Interpreter`를 입력하고 선택합니다.
    *   나타나는 목록에서 `conda: base` 와 같이 아나콘다 기본 환경을 선택합니다.
    *   **이 과정을 통해 VSCode는 우리가 아나콘다 프롬프트에서 `pip`이나 `conda`로 설치한 모든 라이브러리(`pandas`, `streamlit` 등)를 인식하고 사용할 수 있게 됩니다.**
5.  **터미널 설정:**
    *   VSCode 상단 메뉴에서 `터미널 > 새 터미널`을 엽니다.
    *   기본 터미널이 PowerShell일 경우, 터미널 창 우측의 `+` 버튼 옆 드롭다운 메뉴에서 `Git Bash`를 선택하여 변경해줍니다. (Git Bash가 `conda` 환경을 더 잘 인식합니다.)
    *   터미널에 `(base)`와 같이 현재 conda 환경이 표시되는지 확인합니다. 만약 표시되지 않으면 `conda activate base` 명령어를 입력합니다.

### 5.3. Streamlit 첫걸음 (`app.py` 상세 분석)

이제 프로젝트 폴더에 `app.py` 파일을 생성하고, `Streamlit`의 다양한 기능들을 코드로 작성하며 배워보겠습니다.

> **📌 노트:** `Streamlit` 앱을 실행하는 명령어는 `python app.py`가 아니라 `streamlit run app.py` 입니다. 이 명령어를 터미널에 입력하면 웹 서버가 실행되고, 자동으로 웹 브라우저에 결과 페이지가 열립니다. 코드를 수정한 후 저장하면, 브라우저 화면에 나타나는 `Rerun` 버튼을 눌러 즉시 변경사항을 반영할 수 있습니다.

#### **`st.title`, `st.header`, `st.write`**: 텍스트 출력의 기본

```python
# app.py
import streamlit as st

# st.title() : 가장 큰 제목을 출력합니다. (페이지의 메인 제목)
st.title(\'streamlit 시각화 Demo\')

# st.header() : 중간 크기의 소제목을 출력합니다. (섹션 제목)
st.header("데이터 출력")

# st.write() : 일반 텍스트, 변수 내용 등 다양한 것을 출력할 수 있는 만능 함수입니다.
st.write("프레임 데이터 출력을 도와주는 함수 : dataframe()")
```

#### **`st.dataframe`, `st.table`**: 데이터프레임 표시

`pandas` 데이터프레임을 웹 페이지에 표 형태로 보여주는 함수입니다.

```python
# app.py
import pandas as pd
import numpy as np
import streamlit as st

# 가상 데이터프레임 생성
frm = pd.DataFrame({
    "timestamp" : pd.date_range(\'2025-11-06\', periods=10, freq=\'H\'),
    "user"      : np.random.choice([\'admin\', \'guest\'], 10),
    "delay_ms"  : np.random.randint(20, 800, 10)
})

# st.dataframe() : 스크롤이 가능한 인터랙티브한 표를 만듭니다.
st.dataframe(frm)

st.write("정적 프레임 데이터 출력을 도와주는 : table()")
# st.table() : 표 전체를 한 번에 보여주는 정적인 표를 만듭니다.
st.table(frm.head())
```

#### **`st.json`**: JSON 데이터 표시

딕셔너리나 JSON 형식의 데이터를 보기 좋게 출력합니다.

```python
# app.py
st.write("json 형식 : json()")
st.json({\'status\' : \'fail\', \'cnt\' : len(frm)})
```

#### **`st.line_chart`, `st.bar_chart`**: 기본 차트

`Streamlit`은 간단한 리스트나 데이터프레임을 전달하는 것만으로도 기본적인 차트를 빠르게 그려주는 내장 함수들을 제공합니다.

```python
# app.py
st.header("Streamlit 기본 Chart")
st.line_chart([1,2,3,8,5,9,4])
st.area_chart([1,2,3,8,5,9,4])
st.bar_chart([1,2,3,8,5,9,4])
```

#### **`st.plotly_chart`**: Plotly 차트 연동

> **💡 중요!:** `Streamlit`의 진정한 강력함은 `Plotly`와 같은 외부 시각화 라이브러리와의 연동에서 나옵니다. `Plotly`로 생성한 인터랙티브한 `figure` 객체를 `st.plotly_chart()` 함수에 그대로 전달하면, 웹 페이지에 완벽하게 통합할 수 있습니다.

```python
# app.py
import plotly.express as px
import streamlit as st

# 가상 데이터
frm_gdp = pd.DataFrame({
    \'Country\' : [\'한국\', \'미국\', \'일본\', \'호주\'],
    \'Gdp\' : [1000, 2000, 3000, 4000]
})

# Plotly로 막대 그래프 figure 생성
fig = px.bar(frm_gdp, x=\'Country\', y=\'Gdp\', title=\'국가별 GDP\', color=\'Country\')

# 생성된 figure를 Streamlit 웹 페이지에 렌더링
st.plotly_chart(fig)
```

#### **`st.video`**: 미디어 파일 임베딩

웹 페이지에 비디오나 오디오 파일을 쉽게 추가할 수 있습니다.

```python
# app.py
st.header("Image, Audio, Video")
st.video(\'https://www.w3schools.com/html/mov_bbb.mp4\')
```

#### **`st.slider`**: 사용자 입력 위젯

`Streamlit`은 슬라이더, 버튼, 텍스트 입력, 체크박스 등 다양한 사용자 입력 위젯을 제공하여 인터랙티브한 앱을 만들 수 있게 합니다.

```python
# app.py
st.header("사용자의 입력")

# st.slider(레이블, 최소값, 최대값, 기본값)
# 슬라이더를 움직이면 그 값이 data 변수에 실시간으로 저장됩니다.
data = st.slider(\'데이터 범위를 선택하세요 : \', 1, 100, 10)

# f-string을 이용해 사용자의 선택을 화면에 보여줍니다.
st.write(f\'당신이 선택한 값은 : {data} 입니다.\')
```

### 5.4. 실전! 동적 대시보드 구축 (`dashboard.py` 상세 분석)

`dashboard.py` 파일은 지금까지 배운 `Streamlit` 기능들을 총망라하여, 사용자가 직접 CSV 파일을 업로드하고, 사이드바의 필터를 통해 데이터를 동적으로 분석하여 시각화하는 멋진 대시보드 예제입니다.

```python
# dashboard.py
import pandas as pd
import streamlit as st
import plotly.express as px

st.title(\'실시간 공격 로그 분석 대시보드\')

# 1. 파일 업로드 기능
# st.file_uploader를 이용해 사용자로부터 파일을 받을 수 있습니다.
# type=[\'csv\']는 csv 파일만 업로드하도록 제한합니다.
file = st.file_uploader(\'분석할 CSV 로그 파일을 업로드하세요: \', type=[\'csv\'])

# 2. 파일이 업로드 되었을 때만 아래 로직 실행
if file is not None:
    # 업로드된 파일을 pandas DataFrame으로 읽어옵니다.
    rawData = pd.read_csv(file)
    st.success(f\'{file.name} 파일이 성공적으로 업로드되었습니다!\')

    # 3. 사이드바에 필터 위젯 배치
    st.sidebar.header(\'데이터 필터 설정\')
    
    # st.sidebar.multiselect를 이용해 여러 항목을 선택할 수 있는 필터를 생성합니다.
    countryFilter = st.sidebar.multiselect(\'국가 선택 : \',
                                           rawData[\'country\'].unique())
    attackFilter = st.sidebar.multiselect(\'공격 타입 선택 : \',
                                          rawData[\'attack_type\'].unique())

    # 4. 원본 데이터 표시
    st.write("--- 원본 데이터 샘플 ---")
    st.dataframe(rawData.head())
    
    # 5. 필터링 로직
    # 사용자가 선택한 국가와 공격 타입에 해당하는 데이터만 필터링합니다.
    filterData = rawData[(rawData[\'country\'].isin(countryFilter)) & (rawData[\'attack_type\'].isin(attackFilter))]

    st.write("--- 필터링된 데이터 결과 ---")
    st.dataframe(filterData)

    # 6. 필터링된 데이터를 기반으로 동적 시각화
    st.subheader(\'시간대별 공격 발생 추이\')
    fig01 = px.line(filterData, x=\'time\', color=\'attack_type\')
    st.plotly_chart(fig01)

    st.subheader(\'국가별 공격 비율\')
    fig02 = px.pie(filterData, names=\'country\', title=\'국가별 공격 비율\')
    st.plotly_chart(fig02)

    st.subheader(\'공격 유형별 성공/실패 현황\')
    fig03 = px.bar(filterData, x=\'attack_type\', color=\'status\', title="공격 유형별 상태")
    st.plotly_chart(fig03)
```

#### 💻 코드 실행 상세 분석
1.  **1단계 (파일 업로드 대기):** `st.file_uploader()`가 실행되어 웹 페이지에 파일 업로드 위젯을 생성합니다. `file` 변수는 초기에는 `None` 상태입니다.
2.  **2단계 (파일 업로드 확인):** 사용자가 파일을 업로드하면, `Streamlit`은 스크립트를 자동으로 다시 실행합니다. 이때 `file` 변수는 더 이상 `None`이 아니므로 `if file is not None:` 코드 블록 안으로 진입합니다.
3.  **3단계 (데이터 로드 및 필터 생성):**
    *   `pd.read_csv(file)`이 실행되어 업로드된 파일 내용을 `rawData` 데이터프레임으로 읽어옵니다.
    *   `st.sidebar.multiselect()`가 두 번 호출되어, `rawData`에 있는 고유한 국가명과 공격 유형을 선택지로 하는 멀티-선택 필터를 사이드바에 생성합니다. `countryFilter`와 `attackFilter` 변수에는 사용자가 선택한 값들의 리스트가 저장됩니다.
4.  **4단계 (동적 필터링):**
    *   `rawData[\'country\'].isin(countryFilter)` 코드는 `rawData`의 \'country\' 컬럼 값이 사용자가 선택한 국가 리스트(`countryFilter`)에 포함되는지 여부를 `True`/`False`로 반환합니다.
    *   `&` 연산자를 통해 국가 조건과 공격 유형 조건을 모두 만족하는 행들만 최종적으로 `filterData`에 할당됩니다.
5.  **5단계 (동적 시각화):**
    *   `px.line(filterData, ...)` 와 같이, **필터링된 결과인 `filterData`**를 입력으로 하여 3개의 `Plotly` 차트(`fig01`, `fig02`, `fig03`)가 생성됩니다.
    *   `st.plotly_chart()` 함수들이 이 `figure` 객체들을 받아 웹 페이지에 렌더링합니다.
6.  **최종 결과:** 사용자가 사이드바에서 필터를 변경할 때마다 스크립트가 다시 실행되고, 4-5단계가 반복되면서 필터링된 결과와 그에 따른 차트가 실시간으로 업데이트되는 동적인 대시보드가 완성됩니다.

---

## 6. 🔐 보안 관점 심화: 파일 업로드 기능의 잠재적 위협

`dashboard.py`에서 사용된 `st.file_uploader` 기능은 매우 편리하지만, 외부로부터 파일을 받는 모든 기능은 잠재적인 보안 위협을 내포하고 있습니다.

> #### 🔐 보안 노트: 파일 업로드 취약점
>
> 1.  **악성 파일 업로드:** 공격자가 `.csv` 확장자를 가졌지만 실제로는 악성 스크립트나 바이러스를 포함한 파일을 업로드할 수 있습니다. 만약 서버 측에서 이 파일을 부주의하게 처리(예: 실행)한다면 심각한 보안 사고로 이어질 수 있습니다.
> 2.  **자원 고갈(Resource Exhaustion) 공격:** 공격자가 수십 GB에 달하는 거대한 CSV 파일을 업로드하여 서버의 메모리나 디스크 공간을 가득 채워, 다른 사용자들이 서비스를 이용할 수 없게 만드는 서비스 거부(DoS) 공격을 시도할 수 있습니다.
> 3.  **경로 조작(Path Traversal):** 공격자가 `../../etc/passwd`와 같은 파일 이름을 사용하여 업로드 경로를 조작, 시스템의 민감한 파일을 덮어쓰려고 시도할 수 있습니다.
>
> **대응 방안:**
> -   **엄격한 파일 타입 검증:** `type=[\'csv\']` 옵션은 1차적인 방어선이지만, 파일의 실제 내용(Magic Number)까지 검사하여 정말 CSV 파일이 맞는지 확인하는 것이 더 안전합니다.
> -   **파일 크기 제한:** 웹 서버(예: Nginx) 설정이나 `Streamlit` 설정(`server.maxUploadSize`)을 통해 업로드 가능한 파일의 최대 크기를 합리적인 수준으로 제한해야 합니다.
> -   **안전한 파일 이름 처리:** 업로드된 파일의 이름에서 `..`, `/` 등 위험한 문자열을 제거하고, 임의의 문자열로 파일명을 재생성하여 저장하는 것이 안전합니다.
> -   **분리된 환경에서 실행:** `Docker`와 같은 컨테이너 기술을 사용하여 `Streamlit` 애플리케이션을 시스템의 다른 부분과 격리된 환경에서 실행하는 것이 좋습니다.

---

## 7. 🚀 다음 주 학습 및 미니 프로젝트 안내

강의 말미에 강사님께서는 다음 주에 진행될 **LLM/LangChain 학습**과 **미니 프로젝트**에 대한 중요한 안내를 해주셨습니다.

-   **LLM/LangChain 환경 구축:**
    -   다음 주 LLM 관련 실습은 현재 사용 중인 `conda`의 `base` 환경과 호환되지 않는 특정 버전의 라이브러리(`python`, `openai`, `langchain` 등)를 요구합니다.
    -   따라서, `conda`의 가상환경 생성 기능을 이용해 LLM 실습만을 위한 **완전히 새로운 가상환경**을 구축할 예정입니다. 이를 통해 기존 환경과의 충돌을 피하고 안정적인 실습 환경을 확보할 것입니다.
-   **미니 프로젝트 안내:**
    -   오늘 중으로 미니 프로젝트를 위한 팀 구성이 공지될 예정입니다.
    -   프로젝트의 대주제는 **"데이터 분석 및 시각화를 통한 인사이트 도출"** 입니다.
    -   단순히 기술을 사용하는 것을 넘어, 데이터를 통해 의미 있는 결론을 이끌어내는 것이 핵심 목표입니다.
    -   강사님께서 제시해주신 예시 주제들은 다음과 같습니다.
        -   시대/연령대에 따른 화장품 소비 트렌드 분석
        -   파일 확장자 변경 공격 등 악성 파일의 통계적 특성 분석 및 시각화
        -   웹 로그(Web Log) 데이터를 분석하여 SQL Injection 등 공격 시도 패턴 탐지 및 시각화
    -   오늘부터 팀원들과 아이스 브레이킹 시간을 갖고, 어떤 주제로 프로젝트를 진행할지 자유롭게 브레인스토밍을 시작하는 것을 권장하셨습니다.
