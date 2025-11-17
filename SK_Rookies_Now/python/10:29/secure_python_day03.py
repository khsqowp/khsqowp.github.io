# set으로 리스트화 하는데, 순서를 보장하지 않다 보니 오류가 나지 않는가?
# 기존코드
wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk']
wordDict = {word: 0 for word in set(wordLst)}
for word in wordLst:
    wordDict[word] += 1
print(wordDict)

result = dict(zip(set(wordLst), [wordLst.count(data) for data in set(wordLst)]))
print(result)
# ---
# 개선코드
unique = sorted(set(wordLst))
freq = [wordLst.count(word) for word in unique]
result = dict(zip(unique, freq))

# 개선코드 V2
from collections import Counter
result = dict(Counter(wordLst))

# 개선코드 V3
result = {key: wordLst.count(key) for key in dict.fromkeys(wordLst)}
print(result)


# ----
# 학습 목표
# - 분기분, 반복분
# 함수
# 연산자 etc...

# 제어구문
# 어떤 특정한 데이터가 용량이 많다면(동일한 포맷의 대량의 데이터)
# 특정한 조건에 맞는 필터링 필요 -> 분기문과 반복문 활용
# else문은 필수가 아니다. elif도 동일
# if (논리값, 표현식) :
#     실행코드 <- if문이 true일 때
# else :
#     실행코드 <- if문이 false일 때

# if (논리값, 표현식) :
#     실행코드
# elIf :
#     실행코드
# else :
#     실행코드

# if (논리값, 표현식) :
#     if (논리값, 표현식) :
#         실행코드

if True :
    print('Good')
else :
    print('Bad')

# ㅑnput() : 콘솔을 통해서 사용자의 입력을 전달받는 함수
score = int(input('점수를 입력하세요 : ')) #input은 str로만 반환한다.
print('type - ', type(score))
#
if score >= 60 :
    print('Pass')
else :
    print('None Pass')

# 점수에 따른 학점을 제공한다면?
#if문을 많이 사용하거나, 중첩If문을 사용하는걸 지양한다고 하는데 그 이유는?
score = int(input('점수를 입력하세요 : ')) #input은 str로만 반환한다.
print('type - ', type(score))
#
if score >= 90 :
    if score>=95 :
        print('A+')
    else :
        print('A-')
elif score >= 80 :
    if score >= 85 :
        print('B+')
    else :
        print('B-')
elif score >= 70 :
    if score >= 75 :
        print('C+')
    else :
        print('C-')
else :
    print('F')

# If ~ in
areas = ['서울', '경기', '인천', '부산'] #List
region = input('지역을 입력하세요 : ')

if region in areas :
    print('응')
else :
    print(f' {region} 지역은 대상이 아닙니다')

dictTmp = {'melon' : 100, 'bravo' : 200, 'bibibig' : 300}
print('키의 존재 유무 판단')
target = 'banana'
if target in dictTmp :
    print(dictTmp[target])
else :
    print(f'{target}키는 대상이 아닙니다.')


# 주의해야 할 연산자 : %, ==, &(논리 곱, and), |(논리 합, or)
# 윤년 : 4의 배수이고 100의 배수가 아니거나, 400의 배수일 때
# 요구사항) input함수를 이용해서 년도를 입력받아 윤년인지 평년인지 판단

# 정수가 아닌 문자열을 넣으면 Exception이 터진다. 따라서 보안적인 관점에서 개선 필요.
# 음수를 넣어도 정상작동됨. 기대값은 양수이지만..
# 랩업 시간에 유효성 검사나 길이 제한 등 다양한 개선 작업 하기.
youn = int(input("연도를 입력하세요 : "))

print(f"{youn}은 {'윤년' if ((youn % 4 == 0 and youn % 100 != 0) or (youn % 400 == 0)) else '윤년이 아닙니다.'}")


# 연도 월을 입력받아서 월의 마지막 날을 출력

year = int(input("연도 : "))
month = int(input("월 : "))


if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"{year}년 {month}월은 31일")


elif month == 2:
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        print(f"{year}년 {month}월은 29일")
    else:
        print(f"{year}년 {month}월은 28일")

else:
    print(f"{year}년 {month}월은 30일")

#---
year = int(input('년도를 입력하세요 : '))
month = int(input('월를 입력하세요 : '))

dayLst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    dayLst[1] = 29
print(f"{year}년 {month}월의 마지막 날은 {dayLst[month -1]}일 입니다")

# 날짜 타입
# date, datetime
# import
# from ~ import ~ 두가지가 있음
# import는 모듈을 가져옴
# from ~ import ~ 특정 모듈로부터 함수를 가져온다 라고 이해하면 됨.
# from module import function
# from package.module import function, class <- 인공지능에서 많이 사용. 패키지 밑에 새로운 패키지를 만들고, 또 새로운 패키지를 만들어서 모듈을 두기 때문에. / 모듈안에 또 패키지를 넣을수도 있다.
# from package import module

# 딱히 정형화 되어 있다.

from datetime import date, datetime #datetime은 함수 / date, datetime는 객체
# date는 날짜, datetime은 날짜 + 시분초
today = date.today()
print('dir - ', dir(today))
print(today)
print(today.year, today.month, today.day,sep = "-")

today = datetime.today()
print('dir - ', dir(today))
print(today)
print(today.year, today.month, today.day,sep = "-")

print('날짜에 대한 연산을 도와주는 함수 - dateutil')
from dateutil.relativedelta import relativedelta
from datetime import timedelta

today = date.today()
print('today - ', today)
# 날짜 연산은 + 사용 불가
print('날짜 연산')
day = timedelta(days = 1)
print(day)
print(today + day)
# timedelta는 Days만 지원
# relativedelta는 days, months, years 모두 지원
day = relativedelta(days = 1)
month = relativedelta(months = 1)
year = relativedelta(years = 1)

print(year, month, day)

today = today + year
today = today + month
today = today + day
print(today)

# 문자(날짜) -> 날짜 로 변경할 수 있어야 한다.
strDate = '2025-10-29'
today = datetime.strptime(strDate, '%Y-%m-%d')
print(today, type(today))

# 날짜 -> 문자(날짜)로 변경하기
today = today.strftime('%Y-%m-%d')
print(today, type(today))


startDay = datetime.strptime('2025-10-01', '%Y-%m-%d')
endDay = datetime.strptime('2025-10-01', '%Y-%m-%d')

# 날짜 관련된건 pandas에서 많이 사용
# %Y-%m-%d는 날짜 표기 양식 (대소문자 구분하기, - 대신 / 사용하면 2025/10/29 로 표기됨)


# 반복구문 while
# 초기식
# while 조석 :
#    실행문
#    초기값에 증감

# lst = []

# currentDay = startDay
# while currentDay <= endDay :
#     lst. append(currentDay.strftime('%Y-%m-%d'))
# currentDay += timedelta (days = 1)
# print (lst)


# 3항 연산자
# If ~ else를 사용하는건 동일
# if결과 if 조건 else else결과

a = 10
b = 20

maxValue = a if a > b else b
print(maxValue)

age = 20
status = "성인" if age > 18 else "미성년지"
print(status)


import random
lst = []
for _ in range(1, 10) :
    nan = random.randint(1,100)
    lst.append(nan)

print(lst)
result = ["짝수" if data % 2 == 0 else "홀수" for data in lst]
print(result)


pNum = input("핸드폰 번호를 입력하세요 : ")
tong = pNum[0:3]
result = "SKT" if tong == '011' else ("kt" if tong == '016' else ('LG' if tong == '019' else "Not Found"))

print(result)



ctzInput = input("주민등록번호를 입력해주세요 : ")

cityInfo = ctzInput[-2:]
print(cityInfo)
seoulCheck = []
for idx in range(0,9):
    seoulCheck.append('0' + str(idx))
print(seoulCheck)

result = ["서울" if cityInfo in seoulCheck else "서울X"]
print(result)

result2 = ["서울" if ctzInput[-2:] in ["00","01","02","03","04","05","06","07","08"]else "서울X"]
print(result2)

result3 = ["서울" if "00" <= ctzInput[-2:0] <= "08" else "서울X"]
print(result3)

from dateutil.relativedelta import relativedelta
from datetime import timedelta

#연산 우선순위는 산술이 가장 높고, 그다음이 관계, 그다음이 논리



# 반복구문
# for ~ in 열거형(range, list, dict, tuple) :
# for ~ else
# while
#
# 반복구문 키워드
# break, continue

for data in range(10) :
    print(data)


msg = 'see u next time'
for char in msg :
    print(char, end='')

for idx in range(len(msg)):
    print(msg[idx], end="")

tupleTmp = (4,6,1,3)
for idx, data in enumerate(tupleTmp) :       #enumerate : 언패킹해서 인덱스와 데이터 수령 가능
    print('idx - ', idx, 'data - ', data)


wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk', 'sk']
result = {}
for data in wordLst :
    if data in result :
        result[data] += 1
    else :
        result[data] = 1
print(result)


from random import randint

print('guess game - ')
print('1 ~100 사이의 난수를 생성하고 숫자를 맞춰보는 게임')
ranNum = randint(1,100)
inputNum = 0
count = 1
while ranNum != inputNum and count < 10:
    inputNum = int(input(f"숫자를 맞춰주세요({count}번째 시도)"))
    if inputNum > ranNum :
        print("다운")
        count+=1
    elif inputNum < ranNum:
        print("업")
        count+=1
    else:
        print(f"{count}번만에 정답! ranNum은 {ranNum} 이었어요")

    if count == 10:
        print("10회 동안 못 맞췄어요..")
        break
print(f"정답{ranNum}" if ranNum == inputNum else f"실패! 정답은 {ranNum}")

print(ranNum)
for i in range(10) :
    inputNum = int(input(f"숫자를 맞춰주세요{count}번째 시도"))
    if inputNum > ranNum :
        print("다운")
        count+=1
    elif inputNum < ranNum:
        print("업")
        count+=1
    else:
        print(f"{count}번만에 정답! ranNum은 {ranNum} 이었어요")
    if count == 10:
        print("10회 동안 못 맞췄어요..")
        break



# 프로젝트 데이터 개념, 시각화 , 시각화 AI 이용방법
# ㄴ> 이를 위해서 파이썬 문법이 바탕이 됨.
# 인공지능, 애플리케이션 개발도 가능 -> 프론트도 필요해짐
# react, vue와 같은 프레임워크, 라이브러리 등을 쓰고
# Django나 Flask를 백엔드에 사용(파이썬)
# 파이썬은 백엔드 사이드의 언어
# 백엔드에 인공지능 모델들을 도킹할 수 있게 됨.
# for랑 while를 나누는 기준이 애맿자만
# while -> 주어진 횟수가 주어지지 않은 상황
# for -> 특정한 주어진 횟수가 제공될 때



from random import randint
# 정상적으로 for문을 빠져나가지 못했을 때. else
print('guess game - ')
print('1 ~100 사이의 난수를 생성하고 숫자를 맞춰보는 게임')
ranNum = randint(1,100)
inputNum = 0
count = 1
print(ranNum)
for i in range(10) :
    inputNum = int(input(f"숫자를 맞춰주세요{count}번째 시도"))
    if inputNum > ranNum :
        print("다운")
        count+=1
    elif inputNum < ranNum:
        print("업")
        count+=1
    else:
        print(f"{count}번만에 정답! ranNum은 {ranNum} 이었어요")
        break
else :
    print(f'정답 {ranNum}, 제공되는 기회를 전부 사용하였습니다.')

# else를 반복구문에서도 사용할 수 있다.
from random import randint

print('guess game - ')
print('1 ~100 사이의 난수를 생성하고 숫자를 맞춰보는 게임')
ranNum = randint(1,100)
inputNum = 0
count = 1
while ranNum != inputNum and count < 10:
    inputNum = int(input(f"숫자를 맞춰주세요({count}번째 시도)"))
    if inputNum > ranNum :
        print("다운")
        count+=1
    elif inputNum < ranNum:
        print("업")
        count+=1
    else:
        print(f"{count}번만에 정답! ranNum은 {ranNum} 이었어요")
else:
    print(f"정답{ranNum}" if ranNum == inputNum else f"실패! 정답은 {ranNum}")


# 4년에 한번씩 열리는 올림픽
# 2024 이후 향후 50년동안

cnt = 0;
for year in range(2024,2074, 4) :
    cnt += 1
    if cnt % 5 == 0 :
        print(year, end='\n')
    else:
        print(year, end='\t')


# dan = int(input("단을 입력해주세요 : "))
for row in range(1,11) :
    if row == 3:
        break
    for col in range(1,11):
        print(f"{row}*{col}={row*col}",end = '\t')
    print('\n')

