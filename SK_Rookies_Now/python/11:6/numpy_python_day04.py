# 계획
# streamlit 은 vscode 활용 예정
# 아나콘다 로컬 설치 상태.
# virtual environment를 만들 수 있다.
# venv에다가 open ai langchain 버전을 전부 설치 예정 (아나콘다 기반에다가)
# 가상환경에 인터프리터를 vscode에서 등록해주면 별도의 설치 없이 py를 만들 수 있다.
# 프로젝트를 진행할 때 streamlit을 이용해서 파이썬에 Imput 함수들을 이용해서 데이터 입력받는 기능 구현하여 챗봇 가능
# vscode에서 .py 형태로 진행하는게 가장 이상적이지 않을까 생각함.
# 실제 기능구현을 모듈화 시켜서 만든다.
# 내일까지는 팀 공개 예정 + 주제도

# ----------------------------------
# 다음주부터는 팀별로 아이스브레이킹 기획 등 준비 추천
# 팀의 케미를 맞추기에는 기간상 힘듦 4일정도..
# 기획도 해야되고 데이터도 준비해야되고, 방향성도 설계해야되는데.
# 다음주 금요일부터 진행 예정 (기획 단계)


#--------------------------------
# 학습목표
# 시각화 패키지 Matplotlib, seaborn, folium
# 서브 패키지 pyplot, plotly
# 웹 시각화 streamlit

import numpy  as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# warning 제거
import warnings
warnings.filterwarnings('ignore')

# version check
print('numpy  version - ' , np.__version__)
print('pandas version - ' , pd.__version__)

# 데이터 정보 출력 함수
def aryInfo(ary) :
    print('type - ' , type(ary))
    print('shape - ' , ary.shape)
    print('ndim  - ' , ary.ndim)
    print('dtype - ' , ary.dtype)
    print()
    print('data  -')
    print(ary)

def seriesInfo(s) :
    print('type   - ' , type(s))
    print('index  - ' , s.index)
    print('values - ' , s.values)
    print('dtype  - ' , s.dtype)
    print()
    print('data   - ')
    print(s)

def frmInfo(frm) :
    print('type    - ' , type(frm))
    print('shape   - ' , frm.shape)
    print('ndim    - ' , frm.ndim)
    print('row idx - ' , frm.index , type(frm.index))
    print('col idx - ' , frm.columns , type(frm.columns))
    print('values  - ' , type(frm.values))
    print(frm.values)
    print('data - ')
    print(frm)
#--------------------------------


# %matplotlib inline

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


# 차트 축 <- 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


#--------------------------------


# plt.figure()    # plt 그림판 만들기
# # plt.plot([1,2,3,4,5,6,7,8,9])   # 그림판에 선 그리기
# # plt.plot([1,4,9,5,6,7,2,7,9]) # 그림판에 선 그리기

# plt.plot([10,30,60,90],[1,4,9,16], color = 'red', marker = 'o', ms=15)  # 그림판에 선 그리기

# plt.title('라인 플롯 - ')
# plt.xlabel('X 축 - ')
# plt.ylabel('Y 축 - ', rotation=45)

# plt.xlim(0,100)   # x 축 범위 지정
# plt.ylim(0,17)     # y 축 범위 지정
# plt.show()      # 그림판에 그린 내용을 보여주기
# plt.close()     # 그림판 닫기

#--------------------------------


# 서브플롯을 이용해서 한 화면에 여러 그래프 그리기
# fig = plt.figure(figsize = (20,7))
# area01 = fig.add_subplot(1,3,1)   # 1행 3열 중 첫번째
# area01.set_title('타이틀')
# area01.set_xlabel('X 축 - ')
# area01.set_ylabel('Y 축 - ', rotation=0)

# area02 = fig.add_subplot(1,3,2)   # 1행 3열 중 두번째
# area02.set_title('타이틀')
# area02.set_xlabel('X 축 - ')
# area02.set_ylabel('Y 축 - ', rotation=0)

# area03 = fig.add_subplot(1,3,3)   # 1행 3열 중 세번째
# area03.set_title('타이틀')
# area03.set_xlabel('X 축 - ')
# area03.set_ylabel('Y 축 - ', rotation=0)

# plt.show()
# plt.close()

#--------------------------------


# bar chart : x축이 범주형(카테고리) 데이터인 경우)
# 타입이 카테고리(남자, 여자 / 선실 등급 1,2,3 / A,B,C,D)인 경우
titanicFrm = sns.load_dataset('titanic')
print(titanicFrm.head())
print(titanicFrm['class'].value_counts())
#    survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town alive  alone
# 0         0       3    male  22.0      1  ...        True   NaN  Southampton    no  False
# 1         1       1  female  38.0      1  ...       False     C    Cherbourg   yes  False
# 2         1       3  female  26.0      0  ...       False   NaN  Southampton   yes   True
# 3         1       1  female  35.0      1  ...       False     C  Southampton   yes  False
# 4         0       3    male  35.0      0  ...        True   NaN  Southampton    no   True

# [5 rows x 15 columns]
# class
# Third     491
# First     216
# Second    184
# Name: count, dtype: int64
titanicFrm.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 15 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   survived     891 non-null    int64
#  1   pclass       891 non-null    int64
#  2   sex          891 non-null    object
#  3   age          714 non-null    float64
#  4   sibsp        891 non-null    int64
#  5   parch        891 non-null    int64
#  6   fare         891 non-null    float64
#  7   embarked     889 non-null    object
#  8   class        891 non-null    category
#  9   who          891 non-null    object
#  10  adult_male   891 non-null    bool
#  11  deck         203 non-null    category
#  12  embark_town  889 non-null    object
#  13  alive        891 non-null    object
#  14  alone        891 non-null    bool
# dtypes: bool(2), category(2), float64(2), int64(4), object(5)
# memory usage: 80.7+ KB

#--------------------------------


# Q
# 선실 등급별 생존자 합을 시각화 한다면?
surviveByClass = titanicFrm.groupby('pclass')['survived'].sum() # .values도 되고 .index도 된다.
# .index를 x축으로 쓰고 .values를 y축으로 쓰면 된다.
print(surviveByClass)
# class
# First     136
# Second     87
# Third     119
# Name: survived, dtype: int64

# plt.figure(figsize=(15,5))
# plt.bar(surviveByClass.index, surviveByClass.values, color = ['red','green','blue'])
# # 이런 그림을 만들기 위해서는 통계 분석이 중요하다.
# plt.xticks(surviveByClass.index)
# plt.title('선실 등급별 생존자 수')
# plt.xlabel('선실 등급')
# plt.ylabel('생존자 수')
# plt.show()
# plt.close()

#--------------------------------


# 간단한 시각화를 위해서 더미 데이터셋을 만들어보자.
# 누군가가 로그인 시도 했을 때 로그인 성공 및 실패 로그 데이터.
# 로그인 로그 데이터(timestamp, user, ip, status, delay_ms) <- 전처리를 잘 해야한다. 한글과 영어를 섞는 행동 금지
# 공공 데이터 셋 구하는 경로 : 공공 데이터포털, competition kaggle, data.go.kr

pd.date_range('2025-11-06', periods=100, freq='H')
timeStamp = pd.date_range('2025-11-06', periods=100, freq='H')       # 시간이나 일자, 월, 연, 분, 초 등 각각 대소문자를 구분하는 기준은 ? : Pandas 공식문서 참조
user = np.random.choice(['admin','superAdmin', 'root', 'guest', 'analyst'], size=100)  # 복원 추출
ip = np.random.choice(['192.168.0.1','192.168.0.3', '192.168.0.5', '192.168.0.7', '192.168.0.9'], size=100)  # 복원 추출
status = np.random.choice(['SUCCESS','FAIL'], size=100, p=[0.6,0.4])  # p는 확률
delay_ms = np.random.randint(20, 80, 100)
frm = pd.DataFrame({
    'timestamp' : timeStamp,
    'user'      : user,
    'ip'        : ip,
    'status'    : status,
    'delay_ms'  : delay_ms
})
print(frm.head())

#--------------------------------


# Q
# 로그인 시도 상태별 횟수를 bar plot 이용하여 시각화 하세요.
# loginStatusCount = frm['status'].value_counts()
# frm.groupby('status')['status'].count()  # 이렇게 해도 된다.
# # series로 받게 되고, index와 values로 x축과 y축을 지정하면 된다.
# plt.figure(figsize=(15,5))
# plt.bar(loginStatusCount.index, loginStatusCount.values, color = ['green','red'])
# plt.title('로그인 시도 상태별 횟수')
# plt.xlabel('상태')
# plt.ylabel('횟수', rotation=0)
# plt.xticks(loginStatusCount.index)
# plt.show()
# plt.close()

#--------------------------------

# Q
# 시간대별 평균 지연시간을 line plot 시각화
# X축에 뭐가 들어가고 y 축에 뭐가 들어가는지 잘 생각해보자.
# delayPerHour = frm.groupby(frm['timestamp'].dt.hour)['delay_ms'].mean()
# plt.figure(figsize=(15,5))
# plt.plot(delayPerHour.index, delayPerHour.values, color='blue', marker='o', ms=10)
# plt.title('시간대별 평균 지연시간')
# plt.xlabel('시간대')
# plt.ylabel('지연시간', rotation=0)
# plt.xticks(delayPerHour.index)
# plt.grid()
# plt.show()
# plt.close()

# 하나의 figure에 여러 plot 그리기도 가능하다.

#--------------------------------

irisFrm = sns.load_dataset('iris')
print(irisFrm.head())
#             timestamp        user           ip   status  delay_ms
# 0 2025-11-06 00:00:00       guest  192.168.0.3  SUCCESS        68
# 1 2025-11-06 01:00:00  superAdmin  192.168.0.1     FAIL        72
# 2 2025-11-06 02:00:00       guest  192.168.0.3  SUCCESS        25
# 3 2025-11-06 03:00:00       admin  192.168.0.5  SUCCESS        22
# 4 2025-11-06 04:00:00     analyst  192.168.0.3     FAIL        25
irisFrm.info()
# Data columns (total 5 columns):
#  #   Column        Non-Null Count  Dtype
# ---  ------        --------------  -----
#  0   sepal_length  150 non-null    float64
#  1   sepal_width   150 non-null    float64
#  2   petal_length  150 non-null    float64
#  3   petal_width   150 non-null    float64
#  4   species       150 non-null    object
# dtypes: float64(4), object(1)
# memory usage: 6.0+ KB


# species를 기준으로 시각화가 가능하다.
# sepapl = 꽃 받침
# petal = 꽃잎

#--------------------------------

# Q
# 품종을 기준으로 그룹화를 진행
groupBySpecies = irisFrm.groupby('species').groups
print(groupBySpecies)
# {'setosa': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 'versicolor': [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 'virginica': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]}
groupBySpecies = irisFrm.groupby('species').mean()
print(groupBySpecies)
#             sepal_length  sepal_width  petal_length  petal_width
# species
# setosa             5.006        3.428         1.462        0.246
# versicolor         5.936        2.770         4.260        1.326
# virginica          6.588        2.974         5.552        2.026
# species를 x축
# sepal_length를 y축
# 종별 4개의 막대그래프도 가능. 왜? feature가 4개이기 때문에.

# plt.figure()
# groupBySpecies.plot(kind='bar')
# plt.legend(loc='best')
# plt.xticks(rotation=0)
# plt.show()
# plt.close()

# 만약 legend를 x축으로 하고싶다면? -> transpose() 이용
# plt.figure()
# groupBySpecies.T.plot(kind='bar')
# plt.legend(loc='best')
# plt.xticks(rotation=0)
# plt.show()
# plt.close()


#--------------------------------

# 히스토그램 histogram : 정규분포, 치우침
# 인공지능 학습의 경우 정규분포가 가장 이상적
# 꼬리가 길다? -> 치우침(skewness), 편향되어있다. : 과대적합(overfitting) 문제 발생 가능성
# 연속형 데이터(숫자형)의 분포를 시각화, / 일정한 구간(bin)의 간격
# 해당 구간에 포함되는 데이터의 개수를 세어서 막대 형태로 표현
# 구간에 속하는 데이터 = 빈도수(frequency)
# ex) 시험 점수 분포, 키 분포, 몸무게 분포 등

# LLM과 NLP 분야에서 단어 빈도수 분석에도 활용
# 학습이라는걸 진행하게 된다.
# 처음에는 깡동 -> 최소 10만건 이상의 데이터를 가지고 학습을 진행해야 한다.
# 학습된 모델에 텍스트를 전달 -> 단어의 빈도수 분석 -> 단어의 중요도 파악 -> 문서의 주제 파악 -> 요약, 번역, 감성 분석 등
# 데이터 분석 실습은 우리가 직접 튜닝을 진행 : 미분과 적분을 이용해서
# 모델에 재학습을 한다 : 파인 튜닝
# 파인 튜닝은 비용이 많이 듬 -> 모델의 신뢰성을 높히기 위해 RAG 기법 활용
# RAG = Retrieval Augmented Generation 검색 증강 생성
# 외부 지식 데이터베이스에서 관련 정보를 검색 -> 검색된 정보를 바탕으로 응답 생성
# 이렇게 하면 모델이 더 정확하고 신뢰성 있는 답변을 제공할 수 있다.
# RAG 기법을 활용하면 모델의 크기를 줄이고, 학습 비용을 절감하면서도 성능을 향상시킬 수 있다.
# RAG란 외부에 있는 데이터베이스 에서 정보를 검색해서 그 정보를 바탕으로 답변을 생성하는 기법이다.
# 따라서 LLM 모델과 RAG를 합치면 : langchain

# 벡터DB : 데이터를 숫자로 표현(벡터화)하여 저장하고 검색하는 데이터베이스
# 벡터 DB에 하나의 문장이 들어가면 -> 수백 차원의 숫자(벡터)로 변환 -> 이 벡터를 DB에 저장
# 사용자가 질문을 하면 -> 질문을 벡터로 변환 -> 벡터 DB에서 가장 유사한 벡터(문장) 검색 -> 검색된 문장을 바탕으로 답변 생성

# RAG는 기본적으로 임베딩 벡터 -> 이런 벡터 DB에서 검색을 해서 답변을 생성하는 기법이다.

# 랭체인이 업데이트 되면서 의존성이 싹 바뀜. -> 따라서 자료 조사할 때 최신 자료를 참고해야 한다.

# 분석할 데이터를 LLM에 보내고, LLM에서 나온 데이터는 json, csv 형태이고

# 랭체인을 찍먹만 해서는 안된다. 내가 원하는 프로젝트를 하기 위해서는 튜닝이 필요하다.
# object detection : 영상이나 이미지에서 특정 객체를 인식하는 기술
# 특정 부분에 트레이닝 된 모델을 찾으려 하면 없다.
# 다시 직접 데이터를 모아서 파인튜닝 해줘야 한다.
# 그래야 효과가 있는 결과가 나온다.

# 모델의 중요성 -> 편향되지 않은 데이터 -> 파인 튜닝 -> RAG 기법 활용


#--------------------------------

# 다시 히스토그램
# Q
# 로그인 지연 분포 확인하기
# plt.figure(figsize=(15,5))
# plt.hist(frm['delay_ms'], bins=20, color='green', edgecolor='black')    #bins는 구간의 개수, edgecolor는 막대 테두리 색상
# plt.title('로그인 지연 분포 히스토그램')
# plt.xlabel('지연 시간 (ms)')
# plt.ylabel('Frequency', rotation=0)

# plt.show()
# plt.close()

# 수치형을 보이면 양적 자료 / box plot을 쓰기도 함
# box plot : 이상치를 시각화 하는데 효과적
# 이상치 : 정상 범주에서 벗어난 값
# 이상치는 데이터 분석에 방해가 될 수 있기 때문에 사전에 제거하거나 보정

# 타이타닉 데이터는 양적 자료보다는 질적 자료가 맞다.

# countplot : 범주형 데이터의 빈도수를 시각화 하는데 효과적
# Countplot도 bar plot과 비슷하다.
# 사용자별 로그인 시도 패턴을 countplot을 화용하여 시각화
# countplot은 matplotlib이 아니라 seaborn 패키지에 포함되어 있다.


#--------------------------------

# plt.figure(figsize=(15,5))

# # sns.countplot(data=frm, x='user')   # 로그인에 성공했을수도 있고, 실패했을수도 있다.
# sns.countplot(data=frm, x='user', hue='status', palette='Set2')
# # 데이터 프레임을 가지고 함수를 적용할 수 있다.
# # seaborn은 데이터라는 키워드를 통해서 데이터를 입력받게 되어있다.
# plt.show()
# plt.close()



# box plot은 정리가 선행하기.
# box plot : 이상치 (outlier)를 탐지하는 시각화 도구.
# 이상치 : 정상 범주에서 벗어난 값
# 데이터의 중심(mean은 아니다.)은 4분위수에서 50%지점. (중앙값인 Median), 퍼짐(사분위수), 이상치(outlier)를 한눈에 보여주는 것.
# Q1 이라는 용어를 사용. Q1은 1사분위수, Q3는 3사분위수
# IQR = Q3 - Q1 / IQR : Inner Quartile Range
# lower bound, upper bound = Q1 - 1.5 * IQR , Q3 + 1.5 * IQR
# 이 범위를 벗어나는 값을 이상치로 간주
# whisker : 상자에서 뻗어나온 선 IQR 1.5배 이내의 가장 극단적인 값
# 판정 기준 : 값 < lower bound : 하한 이상치
# 값 > upper bound : 상한 이상치


#--------------------------------

user = np.random.choice(['admin', 'root', 'guest'], size=100)  # 복원 추출
boxFrm = pd.DataFrame({            # 사용자와 비정상 데이터를 만들 예정
    'user'      : user,
# 정규분포의 더미 데이터를 만들어주는 함수
# numpy에서 제공하는 통계 함수중 np.random.normal() 이라는 함수가 있다.
    'delay_ms'  : np.concatenate([
    np.random.normal(200, 50, 80),  # 평균 200, 표준편차 50인 정규분포에서 80개 추출
    np.random.normal(800, 20, 10),
    np.random.normal(100, 20, 10)
])
})
print(boxFrm.head())

boxFrm.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99
# Data columns (total 2 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   user      100 non-null    object
#  1   delay_ms  100 non-null    float64
# dtypes: float64(1), object(1)
# memory usage: 1.7+ KB

print(boxFrm['delay_ms'].describe())
# count    100.000000
# mean     257.626609
# std      194.625160
# min       67.013616
# 25%      155.153459
# 50%      214.439285
# 75%      258.571394
# max      841.123098
# Name: delay_ms, dtype: float64

# 이상치는 결측값 처리 or 제거를 해야 한다.

# IQR
Q1 = boxFrm['delay_ms'].quantile(0.25)
print('Q1 = ', Q1)
Q3 = boxFrm['delay_ms'].quantile(0.75)
print('Q3 = ', Q3)
IQR = Q3 - Q1
print('IQR = ', IQR)

lowerBound = Q1 - 1.5 * IQR
print('lowerBound = ', lowerBound)
upperBound = Q3 + 1.5 * IQR
print('upperBound = ', upperBound)

# Q1 =  158.11084214170978
# Q3 =  234.8733514890295
# IQR =  76.7625093473197
# lowerBound =  42.96707812073022
# upperBound =  350.01711551000903

# box plot 그리는건 쉽지만, 이해하는게 중요하다.
# 데이터 분석해서 이해하는것 까지 진행
# 탐지 시작
print(' 이상치 탐지 - ')
# 이상치 = outlier
outliers = boxFrm[(boxFrm['delay_ms'] < lowerBound) | (boxFrm['delay_ms'] > upperBound)]
print(outliers)
#  이상치 탐지 -
#      user    delay_ms
# 80   root  806.574612
# 81  guest  778.151267
# 82   root  834.430018
# 83  admin  799.059207
# 84  admin  789.461161
# 85   root  830.644272
# 86   root  786.314571
# 87  admin  832.981541
# 88  admin  794.214144
# 89  admin  790.259609

# 이제 수염처럼 box plot으로 그리기
# plt.figure(figsize=(15,5))
# sns.boxplot(data=boxFrm, x='user', y='delay_ms', palette='Set3')    #데이터는 데이터프레임이나 시리즈로 받아온다. / x는 feature, y는 수치형 데이터
# sns.stripplot(data=boxFrm, x='user', y='delay_ms', color='red', size=5, jitter=True, alpha = 0.7)  # 이상치를 점으로 표시 / jitter는 점들을 좌우로 약간 흩뜨려서 겹치지 않게 함
# plt.title('사용자별 로그인 지연 시간 분포와 이상치 탐지')
# plt.xlabel('사용자')
# plt.ylabel('지연 시간 (ms)', rotation=0)
# plt.show()
# plt.close()


# 산점도(scatter plot) : 두개의 연속형 변수 간의 관계를 시각화
# x : 독립변수(feature), y : 종속변수(target)    / 카테고리형은 안된다.
# 독립변수, 종속변수
# AI가 있다. AI 가 학습을 안하면 깡통
# 알고리즘을 주입해서 학습을 시킨다.
# 1. 지도학습 : 정답이 있는 상태에서 학습을 시킨다. 정답(target), 학습할 데이터를 준다. = feature
#   타겟을 주면서 학습을 시킨다. / 독립변수와 종속변수를 명확히 구분
#    ex) 집값 예측, 스팸 메일 분류, 이미지 분류 등
# 2. 비지도학습 : 정답이 없는 상태에서 학습을 시킨다. 데이터의 패턴이나 구조를 찾아내는 것
#   타겟이 없다. 데이터 자체에서 패턴을 찾아내는 것. / 클러스터링 : 군집화
#    ex) 군집화, 차원 축소, 이상치 탐지 등
# 3. 강화학습 : 에이전트가 환경과 상호작용하면서 보상을 최대화하는 방향으로 학습
#   스스로 행동을 선택하고, 그 행동에 대한 보상을 받으면서 학습
#    ex) 게임 플레이, 로봇 제어 등

# 점들이 어떠한 패턴을 갖느냐. 선형일수도, 곡선일수도, 군집일수도 있다. 어떻게 패턴을 이루는지 보면서 변수간의 관계를 파악하기 위한 시각화.

# 변수 간의 상관관계 파악
# 양적 자료(수치형 데이터) 간의 관계를 시각화
# ex) 키와 몸무게의 관계, 공부 시간과 시험 점수의 관계
# 산점도는 x축과 y축에 각각 변수를 배치하여 점으로 표현
# 점들이 어떤 패턴을 이루는지 관찰하여 변수 간의 관계를 분석
# 양의 상관관계 : 한 변수가 증가할 때 다른 변수도 증가
# 음의 상관관계 : 한 변수가 증가할 때 다른 변수는 감소
# 상관관계가 없는 경우 : 두 변수 간에 뚜렷한 패턴이 없음

# plt.figure(figsize=(15,5))
# x = [1,2,3,4,5,6,7,8,9]
# y = [1,4,9,5,6,7,2,7,9]
# plt.scatter(x, y, color='blue', marker='o', s=100, alpha=0.7)  # s는 점의 크기, alpha는 투명도
# plt.show()
# plt.close()


# Q
# 사용자별 로그인 시도 패턴을 산점도로 시각화 하고싶다.
# 각 점은 사용자
# x : 평균 로그인 지연 시간
# y : 실패율(fail Ratio)
# 찾고싶은 인사이트 : 비정상적인 사용자의 행동 패턴을 탐지하고 싶다.
# 데이터셋은 frm 사용 예정
scatterFrm = pd.date_range('2025-11-06', periods=100, freq='H')
timeStamp = pd.date_range('2025-11-06', periods=100, freq='H')       # 시간이나 일자, 월, 연, 분, 초 등 각각 대소문자를 구분하는 기준은 ? : Pandas 공식문서 참조
user = np.random.choice(['admin','superAdmin', 'root', 'guest', 'analyst'], size=100)  # 복원 추출
ip = np.random.choice(['192.168.0.1','192.168.0.3', '192.168.0.5', '192.168.0.7', '192.168.0.9'], size=100)  # 복원 추출
status = np.random.choice(['SUCCESS','FAIL'], size=100, p=[0.6,0.4])  # p는 확률
delay_ms = np.random.randint(20, 80, 100)
scatterFrm = pd.DataFrame({
    'timestamp' : timeStamp,
    'user'      : user,
    'ip'        : ip,
    'status'    : status,
    'delay_ms'  : delay_ms
})
# 사용자별 로그인 시도 패턴을 산점도로 시각화 하고싶다.
# 각 점은 사용자
# x : 평균 로그인 지연 시간
# y : 실패율(fail Ratio)
# 찾고싶은 인사이트 : 비정상적인 사용자의 행동 패턴을 탐지하고 싶다.
# userGroup = scatterFrm.groupby('user')
# meanDelay = userGroup['delay_ms'].mean()
# failRatio = userGroup.apply(lambda x: (x['status'] == 'FAIL').sum() / len(x) )
# plt.figure(figsize=(15,5))
# plt.scatter(meanDelay.index, failRatio.values, color='blue', marker='o', s=100, alpha=0.7)
# plt.title('사용자별 로그인 패턴 분석 산점도')
# plt.xlabel('평균 로그인 지연 시간 (ms)')
# plt.ylabel('실패율', rotation=0)
# plt.show()
# plt.close()



# avg = scatterFrm.groupby('user')['delay_ms'].mean()
# failRatio = scatterFrm.groupby('user').apply(lambda x: (x['status'] == 'FAIL').mean() )
# attemps = scatterFrm['user'].value_counts()

# userStatus = pd.DataFrame({
#     'avg' : avg,
#     'failRatio' : failRatio,
#     'attemps' : attemps
# })
# plt.figure(figsize=(15,5))
# sns.scatterplot(x='avg', y='failRatio',
#                 data = userStatus,
#                 size= 'attemps',
#                 hue = 'user')
# plt.show()
# plt.close()


# 히트맵 : 변수 간의 상관관계를 색상으로 표현
# 상관계수(correlation coefficient)를 이용하여 변수 간의 관계를 수치화
# 상관계수 행렬 (correlation matrix)을 히트맵으로 시각화
# 상관계수 값은 -1에서 1 사이의 값을 가지며,
# 1에 가까울수록 강한 양의 상관관계, -1에 가까울수록 강한 음의 상관관계
# corr = irisFrm.corr(numeric_only=True)
# print(corr)
# #               sepal_length  sepal_width  petal_length  petal_width    #feature들 간의 상관관계
# # sepal_length      1.000000    -0.117570      0.871754     0.817941    # 양의 상관관계 : 한 변수가 증가할 때 다른 변수도 증가
# # sepal_width      -0.117570     1.000000     -0.428440    -0.366126    # 음의 상관관계 : 한 변수가 증가할 때 다른 변수는 감소
# # petal_length      0.871754    -0.428440      1.000000     0.962865    # 이런 상관관계로 회귀분석 진행 regression analysis
# # petal_width       0.817941    -0.366126      0.962865     1.000000    # 상관관계가 없는 경우 : 두 변수 간에 뚜렷한 패턴이 없음
# plt.figure(figsize=(15,5))
# sns.heatmap(corr, fmt='.2f', annot=True, linewidth=0.5)
# plt.show()
# plt.close()







# Frm 데이터를 이용해서 히트맵 시각화
# Q
# 사용자 ~ 상태별 평균 지연시간 히트맵 시각화
pd.date_range('2025-11-06', periods=100, freq='H')
timeStamp = pd.date_range('2025-11-06', periods=100, freq='H')       # 시간이나 일자, 월, 연, 분, 초 등 각각 대소문자를 구분하는 기준은 ? : Pandas 공식문서 참조
user = np.random.choice(['admin','superAdmin', 'root', 'guest', 'analyst'], size=100)  # 복원 추출
ip = np.random.choice(['192.168.0.1','192.168.0.3', '192.168.0.5', '192.168.0.7', '192.168.0.9'], size=100)  # 복원 추출
status = np.random.choice(['SUCCESS','FAIL'], size=100, p=[0.6,0.4])  # p는 확률
delay_ms = np.random.randint(20, 80, 100)
frm = pd.DataFrame({
    'timestamp' : timeStamp,
    'user'      : user,
    'ip'        : ip,
    'status'    : status,
    'delay_ms'  : delay_ms
})

# corr = frm.corr(numeric_only=True)
# pivot = frm.pivot_table(index='user', columns='status', values='delay_ms', aggfunc='mean')
# print(pivot)
# # status           FAIL    SUCCESS
# # user
# # admin       37.000000  45.437500
# # analyst     34.500000  50.625000
# # guest       54.833333  55.888889
# # root        44.000000  46.666667
# # superAdmin  52.444444  49.125000

# pivot = frm.pivot_table(index='user', columns='status', values='delay_ms', aggfunc='mean')
# plt.figure(figsize=(15,5))
# sns.heatmap(pivot, fmt='.2f', annot=True, linewidth=0.5, cmap='YlGnBu')
# plt.show()
# plt.close()

#print('Q1) 배기량(dispL)에 파른 고속연비를 확인하고 한다')
#print('배기량 4 이하인 자동차와 5이상인 자동차 중 고속도로 평균연비가 높은지를 확인한다면')
#print('Q2) 자동차 제조사에 따른 도시 연비를 비교할려고 한다') #print('audi, toyota 두 회사의 모든 차종에 대한 도시연비 평균을 비교-')
#print('Q3) chevrolet, ford, honda 제조사의 모든 차종에 대한 고속도로 연비 평균을 시각화')
#print('Q4) 구동방식별 고속도로연비평균을 막대 그래프로 시각화-')
#print('Q5) 구동방식별 고속도로, 도시연비 평균을 서브셋을 만들고') #print('시각화- multi bar ')
#print('Q6) 해당 클래스별 빈도수를 시각화-')
filePath = './SK_Rookies/data/mpg_visualization.xlsx'
mpgFrm = pd.read_excel(filePath, index_col = 0)
mpgFrm.info()
print(mpgFrm.head())
# <class 'pandas.core.frame.DataFrame'>
# Index: 234 entries, 1 to 234
# Data columns (total 11 columns):
#  #   Column        Non-Null Count  Dtype
# ---  ------        --------------  -----
#  0   manufacturer  234 non-null    object
#  1   model         234 non-null    object
#  2   displ         234 non-null    float64
#  3   year          234 non-null    int64
#  4   cyl           234 non-null    int64
#  5   trans         234 non-null    object
#  6   drv           234 non-null    object
#  7   cty           234 non-null    int64
#  8   hwy           234 non-null    int64
#  9   fl            234 non-null    object
#  10  class         234 non-null    object
# dtypes: float64(1), int64(4), object(6)
# memory usage: 21.9+ KB
#   manufacturer model  displ  year  cyl       trans drv  cty  hwy fl    class
# 1         audi    a4    1.8  1999    4    auto(l5)   f   18   29  p  compact
# 2         audi    a4    1.8  1999    4  manual(m5)   f   21   29  p  compact
# 3         audi    a4    2.0  2008    4  manual(m6)   f   20   31  p  compact
# 4         audi    a4    2.0  2008    4    auto(av)   f   21   30  p  compact
# 5         audi    a4    2.8  1999    6    auto(l5)   f   16   26  p  compact

# Q1) 배기량(displ)에 따른 고속연비를 확인하고 한다
# plt.figure(figsize=(15,5))
# dispLComp = mpgFrm.groupby(mpgFrm['displ'] <= 4)['hwy'].mean()
# dispLComp.index = ['4 이하', '5 이상']
# plt.bar(dispLComp.index.astype(str), dispLComp.values, color=['green','blue'])
# plt.title('배기량에 따른 고속도로 연비 비교')
# plt.show()
# plt.close()

# Q2) 자동차 제조사에 따른 도시 연비를 비교할려고 한다
# audi, toyota 두 회사의 모든 차종에 대한 도시연비 평균을 비교
# brandComp = mpgFrm[mpgFrm['manufacturer'].isin(['audi','toyota'])].groupby('manufacturer')['cty'].mean()
# plt.figure(figsize=(15,5))
# plt.bar(brandComp.index, brandComp.values, color='purple')
# plt.xticks(rotation=45)
# plt.title('제조사별 도시 연비 비교')
# plt.show()
# plt.close()


# Q3) chevrolet, ford, honda 제조사의 모든 차종에 대한 고속도로 연비 평균을 시각화
# cfhComp = mpgFrm[mpgFrm['manufacturer'].isin(['chevrolet', 'ford', 'honda'])].groupby('manufacturer')['hwy'].mean()
# plt.figure(figsize=(15,5))
# plt.bar(cfhComp.index.astype(str), cfhComp.values, color=['red','green','blue'])
# plt.title('제조사별 고속도로 연비 비교')
# plt.show()
# plt.close()

# Q4) 구동방식별 고속도로연비평균을 막대 그래프로 시각화
# 구동방식 = drv
# 4 = 4륜구동 F = 전륜구동 R = 후륜구동
# transHwyComp = mpgFrm.groupby('drv')['hwy'].mean()
# plt.figure(figsize=(15,5))
# plt.bar(transHwyComp.index.astype(str), transHwyComp.values, color=['orange','purple','cyan'])
# plt.xticks(rotation=45)
# plt.title('구동방식별 고속도로 연비 평균')
# plt.show()
# plt.close()

# Q5) 구동방식별 고속도로, 도시연비 평균을 서브셋을 만들고 시각화- multi bar
# 시각화 = multi bar
# drvCtyHwyComp = mpgFrm.groupby('drv')[['cty','hwy']].mean()
# plt.figure(figsize=(15,5))
# plt.bar(drvCtyHwyComp.index.astype(str), drvCtyHwyComp['cty'], width=0.4, label='도시연비', align='center', color='skyblue')
# plt.bar(drvCtyHwyComp.index.astype(str), drvCtyHwyComp['hwy'], width=0.4, label='고속도로연비', align='edge', color='salmon')
# plt.xticks(rotation=45)
# plt.title('구동방식별 도시 및 고속도로 연비 평균')
# plt.legend()
# plt.show()
# plt.close()

# Q6) 해당 클래스별 빈도수를 시각화
# classCount = mpgFrm['class'].value_counts()
# plt.figure(figsize=(15,5))
# plt.bar(classCount.index, classCount.values, color='lightgreen')
# plt.xticks(rotation=45)
# plt.title('자동차 클래스별 빈도수')
# plt.show()
# plt.close()
