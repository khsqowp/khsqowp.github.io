# 시각화를 위해서는 분석이 필요하다.
# 데이터 조작( 잘 꺼내야 된다)
# 프레임은 기본 열 인덱스를 사용하고, 행 인덱스를 위해서는 슬라이싱
# loc[] 라벨값, iloc[] 정수값 : 인덱스

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

scores = {
    'kor' : [90, 85, 100, 88, 78],
    'eng' : [90, 85, 100, 88, 78],
    'mat' : [90, 85, 100, 80, 78]
}

frm = pd.DataFrame(scores,
                    index = ['강승우', '최호준', '임종섭', '이현우', '오신원'])
frmInfo(frm)

# numpy를 배운 이유 - 배열의 개념을 알기 위해
# pandas를 배운 이유 - 데이터 프레임의 개념을 알기 위해
# frm은 2차원 배열
# 데이터 분석과 numpy는 밀접한 관련이 있다.

# Q
# 모든 학생의 과목 평균 점수를 새로운 열로 추가. 열의 이름은 'mean'
mean = frm.mean(axis=1)
frm['mean'] = mean
frmInfo(frm)


# 최호준 학생의 영어점수를 90점으로 수정 + 평균점수도 다시 계산
frm.loc['최호준', 'eng'] = 90
# Loc를 활용해서 행 인덱싱을 할 수 있다.
frm.loc['최호준', 'mean'] = frm.loc['최호준', ['kor', 'eng', 'mat']].mean().astype(np.int32)
# 이미 있는 열을 재지정하게 되면 업데이트된다.
frmInfo(frm)

# 만약에 이현우 학생의 점수를 꺼낸다 (행에 대한 접근)
print( frm.loc['이현우'], type(frm.loc['이현우']) )
# 행에 대한 접근 = Series 객체
# 열에 대한 접근 = Series 객체
# kor     88.000000
# eng     88.000000
# mat     80.000000
# mean    85.333333
# Name: 이현우, dtype: float64 <class 'pandas.core.series.Series'>

print( frm.loc['이현우'], type(frm.loc[['이현우']]) )
# [[]] 이중 대괄호를 사용하면 DataFrame 객체로 반환된다.
# kor     88.000000
# eng     88.000000
# mat     80.000000
# mean    85.333333
# Name: 이현우, dtype: float64 <class 'pandas.core.frame.DataFrame'>

lim = frm.loc['임종섭']
print( lim, type(lim) )
# kor     100.0
# eng     100.0
# mat     100.0
# mean    100.0
# Name: 임종섭, dtype: float64 <class 'pandas.core.series.Series'>

# 데이터분석 수업할때 많이 사용된 데이터 = 타이타닉 데이터
# titanic dataset(seaborn)
titanicRawData = sns.load_dataset('titanic')
print('type - ' , type(titanicRawData))
# type -  <class 'pandas.core.frame.DataFrame'>
print(titanicRawData.head())
#    survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town alive  alone
# 0         0       3    male  22.0      1  ...        True   NaN  Southampton    no  False
# 1         1       1  female  38.0      1  ...       False     C    Cherbourg   yes  False
# 2         1       3  female  26.0      0  ...       False   NaN  Southampton   yes   True
# 3         1       1  female  35.0      1  ...       False     C  Southampton   yes  False
# 4         0       3    male  35.0      0  ...        True   NaN  Southampton    no   True

# [5 rows x 15 columns]


# 열 제목을 잘 살펴봐야한다.
# 분석과 인공지능에서 열 제목은 feature, 속성(attribute) 라고 부른다.
# 별도의 feature들을 subset으로 추출해서 분석하기도 하고 시각화도 진행한다.
titanicRawData.info()
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

# Q
# 선실 등급(pclass)의 인원수를 확인하고싶다면?
print(titanicRawData['pclass'].unique())
# [3 1 2]
print(titanicRawData['pclass'].value_counts())
# series 타입으로 출력된다.
# 3    491
# 1    216
# 2    184
# Name: pclass, dtype: int64

# 값들만 보고싶다면?
print(titanicRawData['pclass'].value_counts().values)
# [491 216 184]

# 해당 데이터프레임에 컬럼명을 확인하고싶다면?
print(titanicRawData.columns)
# Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
#        'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town', 'alive',
#        'alone'], dtype='object')
print('type - ', type(titanicRawData.columns))
# type -  <class 'pandas.core.indexes.base.Index'>

# Q
# 기존 나이에 10살을 더해서 age_by_10 열을 추가하고싶다면?
# 나이에 결측값 존재 숙지하기
titanicRawData['age_by_10'] = (titanicRawData['age'].values + 10).astype('int')
print(titanicRawData[['age', 'age_by_10']].head())
#     age  age_by_10
# 0  22.0         32
# 1  38.0         48
# 2  26.0         36
# 3  35.0         45
# 4  35.0         45

# age_by_10 열을 삭제하고 싶다면?
# drop( , axis = 1, inplace = True) -> 열 삭제 / inplace = True : 원본에 반영
titanicRawData.drop(['age_by_10'], axis=1, inplace=True)

# Q
# 요금(Fare)에 대한 통계(최대, 최소, 평균, 합계) 확인이 필요하다면
print('fare max - ', np.max(titanicRawData['fare']))
print('fare min - ', np.min(titanicRawData['fare']))
print('fare mean - ', np.mean(titanicRawData['fare']))
print('fare sum - ', np.sum(titanicRawData['fare']))
# fare max -  512.3292
# fare min -  0.0
# fare mean -  32.204207968574636
# fare sum -  28693.9493

# 원본 데이터는 변경하는게 아니라 서브셋으로 만드는거다.

# Q
# 선실 등급(pclass)이 3등급인 데이터만의 subset 만들기
subset = titanicRawData[titanicRawData['pclass'] == 3]
print(subset.head())
#    survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town alive  alone
# 0         0       3    male  22.0      1  ...        True   NaN  Southampton    no  False
# 2         1       3  female  26.0      0  ...       False   NaN  Southampton   yes   True
# 4         0       3    male  35.0      0  ...        True   NaN  Southampton    no   True
# 5         0       3    male   NaN      0  ...        True   NaN   Queenstown    no   True
# 7         0       3    male   2.0      3  ...       False   NaN  Southampton    no  False

# 위 서브셋에서 성별과(sex), 생존여부(survived) 컬럼만 새로운 서브셋으로
subset2 = subset[['sex', 'survived']]
print(subset2.head())
#       sex  survived
# 0    male         0
# 2  female         1
# 4    male         0
# 5    male         0
# 7    male         0

# index가 0,2,4,5,7 인 행들만 추출됨. -> 1,2,3,4,5 순서대로 하기 위해서는?
subset = subset.reset_index()
print(subset)
#      index  survived  pclass     sex   age  ...  adult_male  deck  embark_town alive  alone
# 0        0         0       3    male  22.0  ...        True   NaN  Southampton    no  False
# 1        2         1       3  female  26.0  ...       False   NaN  Southampton   yes   True
# 2        4         0       3    male  35.0  ...        True   NaN  Southampton    no   True
# 3        5         0       3    male   NaN  ...        True   NaN   Queenstown    no   True
# 4        7         0       3    male   2.0  ...       False   NaN  Southampton    no  False
# ..     ...       ...     ...     ...   ...  ...         ...   ...          ...   ...    ...
# 486    882         0       3  female  22.0  ...       False   NaN  Southampton    no   True
# 487    884         0       3    male  25.0  ...        True   NaN  Southampton    no   True
# 488    885         0       3  female  39.0  ...       False   NaN   Queenstown    no  False
# 489    888         0       3  female   NaN  ...       False   NaN  Southampton    no  False
# 490    890         0       3    male  32.0  ...        True   NaN   Queenstown    no   True

# [491 rows x 16 columns]

# reset_index()를 했는데, 프레임을 다시 확인해보니 기존 Index가 새로운 feature로 추가되어있다.
# 따라서 drop을 사용
subset.drop('index', axis=1, inplace=True)
print(subset)
#      survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town alive  alone
# 0           0       3    male  22.0      1  ...        True   NaN  Southampton    no  False
# 1           1       3  female  26.0      0  ...       False   NaN  Southampton   yes   True
# 2           0       3    male  35.0      0  ...        True   NaN  Southampton    no   True
# 3           0       3    male   NaN      0  ...        True   NaN   Queenstown    no   True
# 4           0       3    male   2.0      3  ...       False   NaN  Southampton    no  False
# ..        ...     ...     ...   ...    ...  ...         ...   ...          ...   ...    ...
# 486         0       3  female  22.0      0  ...       False   NaN  Southampton    no   True
# 487         0       3    male  25.0      0  ...        True   NaN  Southampton    no   True
# 488         0       3  female  39.0      0  ...       False   NaN   Queenstown    no  False
# 489         0       3  female   NaN      1  ...       False   NaN  Southampton    no  False
# 490         0       3    male  32.0      0  ...        True   NaN   Queenstown    no   True

# [491 rows x 15 columns]


# set_index : 특정 컬럼을 인덱스로 변경하는 함수
# 데이터 분석 후 시각화를 진행할 때 데이터셋이 만들어져 있는데
# 프레임은 인덱스가 있다. -> x축의 라벨 역할인데 0,1,2가 있으면 이상하다. -> 특정 컬럼을 인덱스로(라벨로) 변경
subset.reset_index(inplace=True)
print(subset.head())
# 사라진 인덱스가 다시 돌아옴
#    index  survived  pclass     sex   age  ...  adult_male  deck  embark_town alive  alone
# 0      0         0       3    male  22.0  ...        True   NaN  Southampton    no  False
# 1      1         1       3  female  26.0  ...       False   NaN  Southampton   yes   True
# 2      2         0       3    male  35.0  ...        True   NaN  Southampton    no   True
# 3      3         0       3    male   NaN  ...        True   NaN   Queenstown    no   True
# 4      4         0       3    male   2.0  ...       False   NaN  Southampton    no  False

# [5 rows x 16 columns]

subset.set_index('index', inplace=True)
print(subset.head())
# index 컬럼이 index로 변경됨
#        survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town alive  alone
# index                                         ...
# 0             0       3    male  22.0      1  ...        True   NaN  Southampton    no  False
# 1             1       3  female  26.0      0  ...       False   NaN  Southampton   yes   True
# 2             0       3    male  35.0      0  ...        True   NaN  Southampton    no   True
# 3             0       3    male   NaN      0  ...        True   NaN   Queenstown    no   True
# 4             0       3    male   2.0      3  ...       False   NaN  Southampton    no  False

# [5 rows x 15 columns]

# 다시 원본 데이터로 진행

# Q
# 조건을 붙여볼 예정
# 원본 데이터로부터 나이가 60이상에 선실 등급이 1등급 이면서 성별이 여자인 데이터만 추출하여 서브셋으로 만듦
subsetCond = titanicRawData[(titanicRawData['age'] >= 60) & (titanicRawData['pclass'] == 1) & (titanicRawData['sex'] == 'female')]
print(subsetCond)
#      survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town alive  alone
# 275         1       1  female  63.0      1  ...       False     D  Southampton   yes  False
# 366         1       1  female  60.0      1  ...       False     D    Cherbourg   yes  False
# 829         1       1  female  62.0      0  ...       False     B          NaN   yes   True

# [3 rows x 15 columns]
# and와 &차이 + or 와  | 차이
# and, or : 파이썬에서 사용하는 논리 연산자 (단일 값에 대해서만 사용)
# &, | : 판다스에서 사용하는 논리 연산자 (시리즈, 데이터프레임에 대해서 사용)
# 반드시 괄호로 묶어줘야 한다.
# 결측값은 연산에서 처리하지 않는다.


# sort : index 기준, 열(feature)의 값을 기준으로 총 두가지 방법이 있다.
# 데이터를 가지고 sort하는 경우도 있고, 아닌 경우도 있다.
# sort_index(axis = (축의 방향), ascending = True는 오름차순 False는 내림차순) : index를 기준으로 sort
# sort_values(by = (정렬할 열 이름), ascending = True는 오름차순 False는 내림차순) : 특정 열의 값을 기준으로 sort

# 원본 데이터로부터 승객의 나이를 기준으로 내림차순
subsetFrm = titanicRawData.sort_values(by='age', ascending=False)
print(subsetFrm.head())
#      survived  pclass   sex   age  sibsp  ...  adult_male  deck  embark_town alive alone
# 630         1       1  male  80.0      0  ...        True     A  Southampton   yes  True
# 851         0       3  male  74.0      0  ...        True   NaN  Southampton    no  True
# 493         0       1  male  71.0      0  ...        True   NaN    Cherbourg    no  True
# 96          0       1  male  71.0      0  ...        True     A    Cherbourg    no  True
# 116         0       3  male  70.5      0  ...        True   NaN   Queenstown    no  True

# [5 rows x 15 columns]

# 인덱스가 섞여있다.
subsetFrm = subsetFrm.reset_index()
subsetFrm.drop('index', axis=1, inplace=True)
print(subsetFrm.head())
#    survived  pclass   sex   age  sibsp  ...  adult_male  deck  embark_town alive alone
# 0         1       1  male  80.0      0  ...        True     A  Southampton   yes  True
# 1         0       3  male  74.0      0  ...        True   NaN  Southampton    no  True
# 2         0       1  male  71.0      0  ...        True   NaN    Cherbourg    no  True
# 3         0       1  male  71.0      0  ...        True     A    Cherbourg    no  True
# 4         0       3  male  70.5      0  ...        True   NaN   Queenstown    no  True

# [5 rows x 15 columns]

# 성별에 따른 승객수를 시각화하기 위해서 정렬을 한다면?
titanicRawData['sex'].value_counts().sort_values(ascending=True)
# sort_values에서 by를 안하는 이유 = value_counts()의 결과는 series이기 때문에


# ------ 사담 ------
# 챗본 ㄱag 랭체인 -> API 키는 발급 해줌
# 사전 사후평가 -> 오른거에 대해서는 면접때 보는거에 따라 다름. 전체 평점 낼때는 사후만 봄. 일단은 사후만 평가 들어감 -> 면접때 사전사후 모두 조회 가능하긴 함. (면접관의 비중 영향에 따라 다름)
# 사전 사후보다는 프로젝트가 더 중요
# 문제 해결 방법 + 소통 방법

# 개발 SI랑 보안 SI 는 다름
# ------ 사담 끝 ------


# sorting 후 과제 출제 가능성 있음

# index로 sorting

tmp = titanicRawData.sort_index(ascending=False)
print(tmp.head())   # index를 기준으로 sorting


# Pandas를 가지고 csv 파일을 입출력하기. + 데이터 조작

# 미니 프로젝트 진행할때는 알아서 Dataset을 찾아야 한다.
# pandas에서도 데이터 입출력 가능 (csv 뿐만 아니라 xlsx, json, html, scraping된 비정형 데이터 등등)
# read_xxxx 로 시작 -> 읽어오는 함수
# to_xxxx 로 시작 -> 데이터를 파일로 만드는 함수

namesFrm = pd.read_csv('./SK_Rookies/data/year2022_baby_name.csv',
                       sep = ',',
                       encoding='utf-8')
print('type - ', type(namesFrm))
# type -  <class 'pandas.core.frame.DataFrame'>
namesFrm.info()
# RangeIndex: 33838 entries, 0 to 33837
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   NAME    33838 non-null  object   결측값이 없다.
#  1   GENDER  33838 non-null  object
#  2   COUNT   33838 non-null  int64
# dtypes: int64(1), object(2)
# memory usage: 793.2+ KB

print(namesFrm.describe())
# 통계정보 요약 기능
#               COUNT
# count  33838.000000
# mean     108.085348
# std      693.442991
# min        5.000000
# 25%        7.000000
# 50%       11.000000
# 75%       29.000000
# max    22731.000000

# training dataset 과 test dataset으로 나누는 작업
# 보통 7:3 비율로 나눈다.
# 요소의 타입으로 문자열을 가질 수 없다.
# object를 수치형으로 바꿔야된다. (인공지능에서는)

# 파일을 읽어오면 분석하기 전에 info보고 타입보고 결측값 보고 확인하는 작업 : column이름 확인
print(namesFrm.columns)
# Index(['NAME', 'GENDER', 'COUNT'], dtype='object')

# Q
# Count 열을 기준으로 내림차순 정렬하여 subset을 만든다면?
# 인덱스를 확인하고 reset_index()로 초기화 후 불필요한 'Index' 열을 삭제

subsetCount = namesFrm.sort_values(by='COUNT', ascending=False)
subsetCount = subsetCount.reset_index()
subsetCount.drop('index', axis=1, inplace=True)
print(subsetCount)
#            NAME GENDER  COUNT
# 0      Isabella      F  22731
# 1         Jacob      M  21875
# 2        Sophia      F  20477
# 3         Ethan      M  17866
# 4          Emma      F  17179
# ...         ...    ...    ...
# 33833  Mccauley      F      5
# 33834     Mazal      F      5
# 33835    Mayzee      F      5
# 33836    Maythe      F      5
# 33837     Zzyzx      M      5

# [33838 rows x 3 columns]

# 이렇게도 가능하다.
subsetCount = namesFrm.sort_values(by='COUNT', ascending=False).reset_index(drop=True)



# csv 파일에 헤딩이 있을때도 있지만 없을때도 있다.
# 헤딩이 없을때는 1번째 행이 헤더로 인식왼다.
# namesFrm = pd.read_csv('./SK_Rookies/data/year2022_baby_name.csv',
#                        sep = ',',
#                        encoding='utf-8',
#                        header=None) <- 헤더가 없을때 사용


# Q
# 열 이름을 변경하고자 하다. (NAME -> name / GENDER -> gender / COUNT -> count)
# 성별이 남자인 데이터만 추출하여 출력
subsetGender1 = subsetCount.rename(columns=({'NAME' : 'name' , 'GENDER' : 'gender' , 'COUNT' : 'count'}))
subsetGender2 = subsetCount.rename(columns=lambda x: x.lower())
subsetGender3 = subsetCount.rename( columns = { col: col.lower() for col in subsetCount.columns }, inplace = True)
subsetGender4 = subsetCount.rename(columns = {col: col.lower() for col in subset.columns}, inplace = True)
print(subsetGender1[subsetGender1['gender'] == 'M'])


# subset.columns 는 Index 객체
# subset.columns.values 는 ndarray 객체


# 데이터 분석을 많이 하다보면 기술적 통계분석을 많이 하게 된다.
# 통계량 확인
# - groupby( 열 인덱스 | 인덱스 ) : 특정 열을 기준으로 그룹화 / 데이터를 그룹으로 분할하여 독립된 그룹에 대해서 별도의 데이터 처리
# - apply( 함수 ) : 그룹화된 데이터에 대해 사용자 정의 함수 적용 / apply(lambda x: x.max() - x.min()) 를 많이 사용한다.
# - split : 데이터를 그룹으로 분할
# - combine : 그룹화된 데이터에 대해 연산 수행
# - agg() : 그룹화된 데이터에 대해 집계함수 적용
#   - mean(), sum(), max(), min(), count() 등등


frm = pd.read_csv('./SK_Rookies/data/service_data_groupby_sample.csv', encoding='cp949')
print(frm.head())
#    id gender  height  age region
# 0   1     남자     175   22     서울
# 1   2     여자     160   23     서울
# 2   3     여자     161   21     서울
# 3   4     여자     170   33     서울
# 4   5     여자     155   35     경기

frm.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 12 entries, 0 to 11
# Data columns (total 5 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   id      12 non-null     int64
#  1   gender  12 non-null     object
#  2   height  12 non-null     int64
#  3   age     12 non-null     int64
#  4   region  12 non-null     object
# dtypes: int64(3), object(2)
# memory usage: 612.0+ bytes

# Q
# 지역별 나이 평균을 확인하고싶다면?
# frm.groupby('region') 의 데이터타입은 DataFrameGroupBy    객체
regionAgeMean = frm.groupby('region')['age'].mean()
print(regionAgeMean)
print(type(regionAgeMean))
# region
# 경기    32.00
# 서울    28.25
# 인천    39.00
# 충북    33.00
# Name: age, dtype: float64
# <class 'pandas.core.series.Series'>

gyeoungi = frm.groupby('region').get_group('경기')  # DataFrame 반환
print(gyeoungi)
#    id gender  height  age region
# 4   5     여자     155   35     경기
# 8   9     남자     188   29     경기

# Q
# 성별을 기준으로 그룹을 나누고
genderGroupBy = frm.groupby('gender')
print(type(genderGroupBy))
# <class 'pandas.core.groupby.generic.DataFrameGroupBy'>
print(genderGroupBy.groups)
# {'남자': [0, 5, 6, 8, 9, 11], '여자': [1, 2, 3, 4, 7, 10]}
print(frm.groupby('gender')[['height']].mean())
#             height
# gender                    # gender 인덱스 이름
# 남자      180.666667      # 여자 남자는 인덱스 값
# 여자      161.500000

tmp = frm.groupby('gender')[['height']].mean()
tmp.reset_index(inplace = True)
print(tmp)
#   gender      height
# 0     남자  180.666667
# 1     여자  161.500000

subset = frm.drop('region', axis=1)

print(subset.groupby('gender').agg(['mean', 'var', 'std']))
#          id                      height                             age
#        mean   var       std        mean        var       std       mean        var       std
# gender
# 남자      7.5  14.7  3.834058  180.666667  21.066667  4.589844  31.333333  60.266667  7.763161
# 여자      5.5  11.5  3.391165  161.500000  59.500000  7.713624  29.000000  64.400000  8.024961
# agg() 안에 여러개의 집계함수를 리스트로 전달할 수 있다.
# mean, var(분산), std(표준편차) 를 구함


print(frm.groupby('gender')['age'].agg(['max', 'min', 'mean', 'median']).reset_index())
#   gender  max  min       mean  median
# 0     남자   41   22  31.333333    31.0
# 1     여자   40   21  29.000000    28.0

# Q
# 성별에 따른 거주지의 최빈값(mode())을 구하고싶다면?
print(frm.groupby('gender')['region'].agg(lambda x : x.mode()))
print(frm.groupby('gender')['region'].apply(lambda x : x.mode()))
# 해석
# frm을 groupby를 하는데 gender를 기준으로 그룹화
# region 컬럼에 대해서 agg(집계함수)를 적용하는데
# lambda x : x.mode()[0] -> 람다 함수로 mode()를 구하는데 최빈값이 여러개일 수 있기 때문에 [0]번째 값을 가져온다
#   reset_index() -> 인덱스를 초기화하여 데이터프레임으로 반환
#   결과적으로 성별에 따른 거주지의 최빈값을 구할 수 있다.
# gender                        # agg 사용
# 남자    서울
# 여자    서울
# Name: region, dtype: object
# gender                        # apply 사용
# 남자      0    서울
# 여자      0    서울
# Name: region, dtype: object


tipsFrm = sns.load_dataset('tips')
print(tipsFrm.head())
#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4

print(tipsFrm.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 244 entries, 0 to 243
# Data columns (total 7 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   total_bill  244 non-null    float64
#  1   tip         244 non-null    float64
#  2   sex         244 non-null    category
#  3   smoker      244 non-null    category
#  4   day         244 non-null    category
#  5   time        244 non-null    category
#  6   size        244 non-null    int64
# dtypes: category(4), float64(2), int64(1)
# memory usage: 7.4 KB
# None

print(tipsFrm.columns)
# Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='object')

titanicFrm = sns.load_dataset('titanic')
print(titanicFrm.head())

# tipsFrm 전체 평균 팀은 얼마?
print('tip mean - ', np.mean(tipsFrm['tip']))
print(tipsFrm['tip'].mean())
# 둘 다 똑같이 출력된다.
# tip mean -  2.99827868852459
# 2.99827868852459

# group 비교하기 - 남성과 여성중 평균 팁이 더 높은 성별은?
print('tips gender compare - ', tipsFrm.groupby('sex')['tip'].mean())
# tips gender compare -  sex
# Male      3.089618
# Female    2.833448
# Name: tip, dtype: float64

# 흡연자와 비흡연자 중 평균 팁 비율이 높은 그룹은?
print('tips smoker compare  -', tipsFrm.assign(pct = tipsFrm['tip'] / tipsFrm['total_bill'] ).groupby('smoker')['pct'].mean())
# tips smoker compare  - smoker
# Yes    0.163196
# No     0.159328
# Name: pct, dtype: float64

# yes와 no 합이 1이 아닌 이유는?
# A : 소수점 표현 문제로 인해 정확하게 1이 되지 않음.

# cs 지식 : 소수점을 표현할때 잘 표현 못함 (유동 소수점, 부동 소수점)
# 컴퓨터는 2진수를 씀.
# 10진수 체계를 쓸 때 정확하게 표현이 안되는 경우가 있음.

# git actions git hooks
# CI/CD 자동화 도구
# 개발된 프로덕트를 운영하기 위해서는 배포를 해야함
# 개발자는 배포를 못함 -> 배포를 도와주는 사람 : 오퍼레이터

# 대부분 금융권은 서버리스 -> 클라우드 환경으로 운영

# 개발과 배포를 같이하는 문화가 DevOps

# infra structor as code  (IaC)
# 주기적으로 통합 주기적으로 배포 : CI/CD
#

# Q 요일과 시간대 분석 day, time
# 팁이 가장 많이 발생하는 요일을 확인하고싶다면?
print('many tips day - ', tipsFrm.groupby('day')['tip'].sum().sort_values(ascending=False).head(1))
# many tips day -  day
# Sat    260.4
# Name: tip, dtype: float64

# Q
# time 이라는 Feature가 있다.
print(tipsFrm['time'].unique())
# Categories (2, object): ['Lunch', 'Dinner']
# 점심시간과 저녁시간 중 팁 비율이 더 많이 발생하는 시간대는?
print('many many tips time - ', tipsFrm.assign(pct = tipsFrm['tip'] / tipsFrm['total_bill']).groupby('time')['pct'].mean().sort_values(ascending=False).head(1))
# many many tips time -  time
# Lunch    0.164128
# Name: pct, dtype: float64


# 원본은 건들지 않게.
# Q
# 서브셋을 만들고, 그 서브셋에 age, sex, class, fare, survived 추출
subsetTitanic = titanicFrm[['age','sex','class','fare','survived']]
# 다른 방법은?
subsetTitanic = titanicFrm.loc[:, ['age','sex','class','fare','survived']]
subsettitanic = titanicFrm.iloc[:, [3,2,8,6,0]]  # iloc는 숫자 인덱스만 가능
subsetTitanic = titanicFrm.filter(items=['age','sex','class','fare','survived'])

print(subsetTitanic.head())
# Name: pct, dtype: float64
#     age     sex  class     fare  survived
# 0  22.0    male  Third   7.2500         0
# 1  38.0  female  First  71.2833         1
# 2  26.0  female  Third   7.9250         1
# 3  35.0  female  First  53.1000         1
# 4  35.0    male  Third   8.0500         0
# Traceback (most recent call last):


# Q
# 선실 등급에 따른 그룹을 만들고 1등급 승객만 데이터 프레임 형식으로 만들어본다면?
firstClass = subsetTitanic[subsetTitanic['class'] == 'First']
firstClass = subsetTitanic.groupby('class').get_group('First')
print(firstClass.head(), type(firstClass))
#      age     sex  class     fare  survived
# 1   38.0  female  First  71.2833         1
# 3   35.0  female  First  53.1000         1
# 6   54.0    male  First  51.8625         0
# 11  58.0  female  First  26.5500         1
# 23  28.0    male  First  35.5000         1
# <class 'pandas.core.frame.DataFrame'>


# subset에서 subset['class'] == 'First' 으로 하면 T /F 로 생기는데 이거는 무슨타입? -> boolean indexing
# boolean indexing  subset으로 감싸면 타입이 DataFrame
# get_group 으로 하면 DataFrameGroupBy 객체에서 DataFrame 으로 바뀜



irisFrm = sns.load_dataset('iris')

print(irisFrm['species'].value_counts())
# species
# setosa        50
# versicolor    50
# virginica     50
# Name: count, dtype: int64

grp = irisFrm.groupby('species')
print(grp)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x107d68c80>
print(grp.groups)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x14016a630>
# {'setosa': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 'versicolor': [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 'virginica': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]}

for key, group in grp :
    print('key - ', key)
    print()
    print(group)
# key -  setosa

#     sepal_length  sepal_width  petal_length  petal_width species
# 0            5.1          3.5           1.4          0.2  setosa
# 1            4.9          3.0           1.4          0.2  setosa
# 2            4.7          3.2           1.3          0.2  setosa
# 3            4.6          3.1           1.5          0.2  setosa
# 4            5.0          3.6           1.4          0.2  setosa
# 5            5.4          3.9           1.7          0.4  setosa
# 6            4.6          3.4           1.4          0.3  setosa
# 7            5.0          3.4           1.5          0.2  setosa
# 8            4.4          2.9           1.4          0.2  setosa
# 9            4.9          3.1           1.5          0.1  setosa
# 10           5.4          3.7           1.5          0.2  setosa
# 11           4.8          3.4           1.6          0.2  setosa
# 12           4.8          3.0           1.4          0.1  setosa
# 13           4.3          3.0           1.1          0.1  setosa
# 14           5.8          4.0           1.2          0.2  setosa
# 15           5.7          4.4           1.5          0.4  setosa
# 16           5.4          3.9           1.3          0.4  setosa
# 17           5.1          3.5           1.4          0.3  setosa
# 18           5.7          3.8           1.7          0.3  setosa
# 19           5.1          3.8           1.5          0.3  setosa
# 20           5.4          3.4           1.7          0.2  setosa
# 21           5.1          3.7           1.5          0.4  setosa
# 22           4.6          3.6           1.0          0.2  setosa
# 23           5.1          3.3           1.7          0.5  setosa
# 24           4.8          3.4           1.9          0.2  setosa
# 25           5.0          3.0           1.6          0.2  setosa
# 26           5.0          3.4           1.6          0.4  setosa
# 27           5.2          3.5           1.5          0.2  setosa
# 28           5.2          3.4           1.4          0.2  setosa
# 29           4.7          3.2           1.6          0.2  setosa
# 30           4.8          3.1           1.6          0.2  setosa
# 31           5.4          3.4           1.5          0.4  setosa
# 32           5.2          4.1           1.5          0.1  setosa
# 33           5.5          4.2           1.4          0.2  setosa
# 34           4.9          3.1           1.5          0.2  setosa
# 35           5.0          3.2           1.2          0.2  setosa
# 36           5.5          3.5           1.3          0.2  setosa
# 37           4.9          3.6           1.4          0.1  setosa
# 38           4.4          3.0           1.3          0.2  setosa
# 39           5.1          3.4           1.5          0.2  setosa
# 40           5.0          3.5           1.3          0.3  setosa
# 41           4.5          2.3           1.3          0.3  setosa
# 42           4.4          3.2           1.3          0.2  setosa
# 43           5.0          3.5           1.6          0.6  setosa
# 44           5.1          3.8           1.9          0.4  setosa
# 45           4.8          3.0           1.4          0.3  setosa
# 46           5.1          3.8           1.6          0.2  setosa
# 47           4.6          3.2           1.4          0.2  setosa
# 48           5.3          3.7           1.5          0.2  setosa
# 49           5.0          3.3           1.4          0.2  setosa
# key -  versicolor

#     sepal_length  sepal_width  petal_length  petal_width     species
# 50           7.0          3.2           4.7          1.4  versicolor
# 51           6.4          3.2           4.5          1.5  versicolor
# 52           6.9          3.1           4.9          1.5  versicolor
# 53           5.5          2.3           4.0          1.3  versicolor
# 54           6.5          2.8           4.6          1.5  versicolor
# 55           5.7          2.8           4.5          1.3  versicolor
# 56           6.3          3.3           4.7          1.6  versicolor
# 57           4.9          2.4           3.3          1.0  versicolor
# 58           6.6          2.9           4.6          1.3  versicolor
# 59           5.2          2.7           3.9          1.4  versicolor
# 60           5.0          2.0           3.5          1.0  versicolor
# 61           5.9          3.0           4.2          1.5  versicolor
# 62           6.0          2.2           4.0          1.0  versicolor
# 63           6.1          2.9           4.7          1.4  versicolor
# 64           5.6          2.9           3.6          1.3  versicolor
# 65           6.7          3.1           4.4          1.4  versicolor
# 66           5.6          3.0           4.5          1.5  versicolor
# 67           5.8          2.7           4.1          1.0  versicolor
# 68           6.2          2.2           4.5          1.5  versicolor
# 69           5.6          2.5           3.9          1.1  versicolor
# 70           5.9          3.2           4.8          1.8  versicolor
# 71           6.1          2.8           4.0          1.3  versicolor
# 72           6.3          2.5           4.9          1.5  versicolor
# 73           6.1          2.8           4.7          1.2  versicolor
# 74           6.4          2.9           4.3          1.3  versicolor
# 75           6.6          3.0           4.4          1.4  versicolor
# 76           6.8          2.8           4.8          1.4  versicolor
# 77           6.7          3.0           5.0          1.7  versicolor
# 78           6.0          2.9           4.5          1.5  versicolor
# 79           5.7          2.6           3.5          1.0  versicolor
# 80           5.5          2.4           3.8          1.1  versicolor
# 81           5.5          2.4           3.7          1.0  versicolor
# 82           5.8          2.7           3.9          1.2  versicolor
# 83           6.0          2.7           5.1          1.6  versicolor
# 84           5.4          3.0           4.5          1.5  versicolor
# 85           6.0          3.4           4.5          1.6  versicolor
# 86           6.7          3.1           4.7          1.5  versicolor
# 87           6.3          2.3           4.4          1.3  versicolor
# 88           5.6          3.0           4.1          1.3  versicolor
# 89           5.5          2.5           4.0          1.3  versicolor
# 90           5.5          2.6           4.4          1.2  versicolor
# 91           6.1          3.0           4.6          1.4  versicolor
# 92           5.8          2.6           4.0          1.2  versicolor
# 93           5.0          2.3           3.3          1.0  versicolor
# 94           5.6          2.7           4.2          1.3  versicolor
# 95           5.7          3.0           4.2          1.2  versicolor
# 96           5.7          2.9           4.2          1.3  versicolor
# 97           6.2          2.9           4.3          1.3  versicolor
# 98           5.1          2.5           3.0          1.1  versicolor
# 99           5.7          2.8           4.1          1.3  versicolor
# key -  virginica

#      sepal_length  sepal_width  petal_length  petal_width    species
# 100           6.3          3.3           6.0          2.5  virginica
# 101           5.8          2.7           5.1          1.9  virginica
# 102           7.1          3.0           5.9          2.1  virginica
# 103           6.3          2.9           5.6          1.8  virginica
# 104           6.5          3.0           5.8          2.2  virginica
# 105           7.6          3.0           6.6          2.1  virginica
# 106           4.9          2.5           4.5          1.7  virginica
# 107           7.3          2.9           6.3          1.8  virginica
# 108           6.7          2.5           5.8          1.8  virginica
# 109           7.2          3.6           6.1          2.5  virginica
# 110           6.5          3.2           5.1          2.0  virginica
# 111           6.4          2.7           5.3          1.9  virginica
# 112           6.8          3.0           5.5          2.1  virginica
# 113           5.7          2.5           5.0          2.0  virginica
# 114           5.8          2.8           5.1          2.4  virginica
# 115           6.4          3.2           5.3          2.3  virginica
# 116           6.5          3.0           5.5          1.8  virginica
# 117           7.7          3.8           6.7          2.2  virginica
# 118           7.7          2.6           6.9          2.3  virginica
# 119           6.0          2.2           5.0          1.5  virginica
# 120           6.9          3.2           5.7          2.3  virginica
# 121           5.6          2.8           4.9          2.0  virginica
# 122           7.7          2.8           6.7          2.0  virginica
# 123           6.3          2.7           4.9          1.8  virginica
# 124           6.7          3.3           5.7          2.1  virginica
# 125           7.2          3.2           6.0          1.8  virginica
# 126           6.2          2.8           4.8          1.8  virginica
# 127           6.1          3.0           4.9          1.8  virginica
# 128           6.4          2.8           5.6          2.1  virginica
# 129           7.2          3.0           5.8          1.6  virginica
# 130           7.4          2.8           6.1          1.9  virginica
# 131           7.9          3.8           6.4          2.0  virginica
# 132           6.4          2.8           5.6          2.2  virginica
# 133           6.3          2.8           5.1          1.5  virginica
# 134           6.1          2.6           5.6          1.4  virginica
# 135           7.7          3.0           6.1          2.3  virginica
# 136           6.3          3.4           5.6          2.4  virginica
# 137           6.4          3.1           5.5          1.8  virginica
# 138           6.0          3.0           4.8          1.8  virginica
# 139           6.9          3.1           5.4          2.1  virginica
# 140           6.7          3.1           5.6          2.4  virginica
# 141           6.9          3.1           5.1          2.3  virginica
# 142           5.8          2.7           5.1          1.9  virginica
# 143           6.8          3.2           5.9          2.3  virginica
# 144           6.7          3.3           5.7          2.5  virginica
# 145           6.7          3.0           5.2          2.3  virginica
# 146           6.3          2.5           5.0          1.9  virginica
# 147           6.5          3.0           5.2          2.0  virginica
# 148           6.2          3.4           5.4          2.3  virginica
# 149           5.9          3.0           5.1          1.8  virginica

print('--- Top 5 petal_length ---')
print(irisFrm.sort_values(by='petal_length', ascending=False))
# --- Top 5 petal_length ---
#      sepal_length  sepal_width  petal_length  petal_width    species
# 118           7.7          2.6           6.9          2.3  virginica
# 122           7.7          2.8           6.7          2.0  virginica
# 117           7.7          3.8           6.7          2.2  virginica
# 105           7.6          3.0           6.6          2.1  virginica
# 131           7.9          3.8           6.4          2.0  virginica
# ..            ...          ...           ...          ...        ...
# 16            5.4          3.9           1.3          0.4     setosa
# 35            5.0          3.2           1.2          0.2     setosa
# 14            5.8          4.0           1.2          0.2     setosa
# 13            4.3          3.0           1.1          0.1     setosa
# 22            4.6          3.6           1.0          0.2     setosa

# [150 rows x 5 columns]

print(irisFrm.sort_values(by='petal_length', ascending=False).groupby('species').get_group('setosa'))
#     sepal_length  sepal_width  petal_length  petal_width species
# 24           4.8          3.4           1.9          0.2  setosa
# 44           5.1          3.8           1.9          0.4  setosa
# 5            5.4          3.9           1.7          0.4  setosa
# 18           5.7          3.8           1.7          0.3  setosa
# 23           5.1          3.3           1.7          0.5  setosa
# 20           5.4          3.4           1.7          0.2  setosa
# 46           5.1          3.8           1.6          0.2  setosa
# 43           5.0          3.5           1.6          0.6  setosa
# 25           5.0          3.0           1.6          0.2  setosa
# 26           5.0          3.4           1.6          0.4  setosa
# 11           4.8          3.4           1.6          0.2  setosa
# 29           4.7          3.2           1.6          0.2  setosa
# 30           4.8          3.1           1.6          0.2  setosa
# 21           5.1          3.7           1.5          0.4  setosa
# 3            4.6          3.1           1.5          0.2  setosa
# 19           5.1          3.8           1.5          0.3  setosa
# 27           5.2          3.5           1.5          0.2  setosa
# 31           5.4          3.4           1.5          0.4  setosa
# 32           5.2          4.1           1.5          0.1  setosa
# 15           5.7          4.4           1.5          0.4  setosa
# 34           4.9          3.1           1.5          0.2  setosa
# 10           5.4          3.7           1.5          0.2  setosa
# 9            4.9          3.1           1.5          0.1  setosa
# 39           5.1          3.4           1.5          0.2  setosa
# 7            5.0          3.4           1.5          0.2  setosa
# 48           5.3          3.7           1.5          0.2  setosa
# 12           4.8          3.0           1.4          0.1  setosa
# 17           5.1          3.5           1.4          0.3  setosa
# 4            5.0          3.6           1.4          0.2  setosa
# 8            4.4          2.9           1.4          0.2  setosa
# 6            4.6          3.4           1.4          0.3  setosa
# 0            5.1          3.5           1.4          0.2  setosa
# 1            4.9          3.0           1.4          0.2  setosa
# 33           5.5          4.2           1.4          0.2  setosa
# 49           5.0          3.3           1.4          0.2  setosa
# 47           4.6          3.2           1.4          0.2  setosa
# 45           4.8          3.0           1.4          0.3  setosa
# 37           4.9          3.6           1.4          0.1  setosa
# 28           5.2          3.4           1.4          0.2  setosa
# 41           4.5          2.3           1.3          0.3  setosa
# 2            4.7          3.2           1.3          0.2  setosa
# 42           4.4          3.2           1.3          0.2  setosa
# 38           4.4          3.0           1.3          0.2  setosa
# 40           5.0          3.5           1.3          0.3  setosa
# 36           5.5          3.5           1.3          0.2  setosa
# 16           5.4          3.9           1.3          0.4  setosa
# 35           5.0          3.2           1.2          0.2  setosa
# 14           5.8          4.0           1.2          0.2  setosa
# 13           4.3          3.0           1.1          0.1  setosa
# 22           4.6          3.6           1.0          0.2  setosa
# 인덱스가 섞인 이유는 ?
# sort_values 로 정렬을 먼저 했기 때문에 원래 인덱스가 유지된 상태에서 정렬이 된 것임.

# groupby를 알아야 하는 이유.



print('age 결측값 - ',titanicFrm['age'].isnull().sum())  # 결측치 개수 확인
# age 결측값 -  177

print(titanicFrm.groupby('sex')['age'].mean())
# sex
# female    27.915709
# male      30.726645
# Name: age, dtype: float64

tmp = titanicFrm.groupby('sex')['age'].apply(lambda x: x.fillna(x.mean()))
print(tmp, type(tmp))
# sex
# female  1      38.0
#         2      26.0
#         3      35.0
#         8      27.0
#         9      14.0
#                ...
# male    883    28.0
#         884    25.0
#         886    27.0
#         889    26.0
#         890    32.0
# Name: age, Length: 891, dtype: float64
# <class 'pandas.core.series.Series'>

# tmp를 활용하여 titanicFrm의 age 결측치를 채운다면?
titanicFrm['age'] = tmp.values
print('age 결측값 - ', titanicFrm['age'].isnull().sum())
# age 결측값 -  0

# 내일부터는 시각화 진행 예정.
