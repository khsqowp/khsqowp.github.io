# #함수 정리 oop method
# # 코드 재사용
# # 가독성 향상
# # 유지보수 용이
# # 디버깅 용이
# # 모듈화 (import utils)

# # def 함수명([매개변수, 매개변수 ...])
# #   실행할 코드
# #   return 결과값(내장변수타입) # 반환이 필요없다면 생략가능


# #키워드 함수, 람다 함수
# # 함수를 인자로 함수와 파라미터
# # map, filter와 람다식이 많이 사용됨
# # LEGB
# # 파이썬 기반의 어플리케이션에서는 클로저나 데코레이터 같은 문법을 많이 활용 -> 외면하기보다는 이해하는 시간 필요
# # 변수의 스코프는 global변수, 지역변수, 블록이 또다른 블록을 포함하면 지역변수가 아닌 외부함수 변수
# # 변수 찾는 순서 -> 지역변수, 외부함수 변수, 전역변수, 빌트인 변수

# print('실행시간 성능 로그 - ')
# from time import time, sleep
# def timer(func) : #클로져를 가장한 데코레이터 / 함수를 전달받는다.
#     def wrapper(*args, **kwargs) : # 실제 실행되는 함수 / 사용하던 사용하지않던 이렇게 받을 수 있다.
#         start = time()
#         result = func(*args, **kwargs)
#         elapsed = time() -start

#         if elapsed > 2 :
#             print(f'경고 : {func.__name__}, 실행시간 : {elapsed:.2f}초 초과되어서 알림')    #이거는 단순한 화면 출력, 이거를 로그로 저장 -> 이를 활용하여 분석
#         return result
#                                                                                     #수학 Numpy, 분석 Pandas + 시각화
#     return wrapper


# def timerFunc() :
#     sleep(3)
#     return '성능확인'

# inner = timer(timerFunc)
# print(inner())


# @timer  #<- 데코레이터 장식자 (function)
# def timeFunc() :
#     sleep(3)
#     return '성능확인'

# inner = timeFunc()
# print(inner)




# # ---
# # 학습목표
# # 예외처리
# # 파일 입출력

# # 예외처리
# # 파이썬 xxxxError (~에러라는 서픽스로 끝나는게 있다. (에러지만 예외처리))
# # raise xxxxError에 대해서도 알아야 함 -> 일부러 예외를 발생시킴
# # 예외랑 에러는 구분할 수 있어야 한다.
# # 에러 -> 휴먼 에러 syntax 에러, 문법 에러
# # 예외 -> 에러보다는 마일드한 에러. 사소한 에러 -> 이러한 상황으로 셧다운 되면 억울하다(?)
# # 예외도 에러는 맞다.
# # 예외처리를 통해서 시스템을 플랫시키거나 셧다운 시키지 않고 예외 상황을 알리고 대처할 수 있도록 하는 방법
# # 시스템의 비정상적인 종료를 막고 정상적인 흐름으로 시스템을 종료시키기 위한 방법
# # try :
# #   예외 발생 코드
# # except :
# #   try 블록에서 발생된 예외를 처리하는 영역
# # else :
# #   예외가 발생하지 않았을 때 수항하는 영역
# # finally :
# #   예외 발생 여부와 상관없이 항상 수행하는 영역


# lst = [1,2,3]

# for idx in range(len(lst) + 1) :
#     print(lst[idx])
# print('정상종료')
# # (base) user@Macintosh-2 Python % /Users/user/.pyenv/versions/3.9.12/bin/python /Users/user/Desktop/CODE/Python/SK_Rookies/secure_python_day05.py
# # 1
# # 2
# # 3
# # Traceback (most recent call last):
# #   File "/Users/user/Desktop/CODE/Python/SK_Rookies/secure_python_day05.py", line 81, in <module>
# #     print(lst[idx])
# # IndexError: list index out of range       -> Error로 끝나는 오류가 발생. -> 이런 상황으로 시스템을 플랫 시키지 말자.
# # (base) user@Macintosh-2 Python %

# lst = [1,2,3]
# try:
#     for idx in range(len(lst)+1) :
#         print(lst[idx])
# except IndexError as e:  # as e 는 별칭 / 예외처리 여러개를 해야되면 except를 여러개 작성하면 됨

#     print(f'{e} 예외발생')
# except Exception as e:  #exception을 쓰면 통합적인 느낌
#     print(f'{e} 예외발생 Exception')
# else :
#     print('예외가 발생하지 않았을 때 수행하는 블록')
# finally:
#     print('예외 발생 여부와 상관없이 수행하는 블록')
# print('>>>>> 정상종료')


# def getUserInfo() :
#     ''' 사용자의 정보를 입력받고, 형식 오류나 유효성을 처리하는 기능'''
#     try:
#         name = input('이름을 입력하세요 : ').strip()#strip: 좌우 공백 제거        # 이름인데 숫자를 입력할수도 있음. 유효성 체크 안됨 => regexp를 활용하여 검증 가능하지만 우선 진행X
#         if not name.isalpha() : # isalpha() -> 문자인지 아닌지 판단. is로 시작하는 경우 대부분 T/F로 정해짐
#             raise ValueError('이름은 문자만 포함해야 합니다.') #<- 일부러 예외를 터트림

#         age = input('나이를 입력하세요 : ').strip()    #숫자가 아닌 문자열을 입력
#         if not age.isdigit() :
#             raise ValueError('나이는 숫자만 포함해야 합니다.')
#         age = int(age)  # 값이 문제없으므로 이때 캐스팅
#         if age < 0 or age > 120 :
#             raise ValueError('1 ~ 120 안으로 입력하세요.')
# # 실제 코드를 개발할때에는 다양한 예외를 생각하여 대비해야한다.

#         email = input('이메일을 입력하세요 : ').strip()
#         if '@' not in email or '.' not in email :
#             raise ValueError('이메일주소는 @와 .이 모두 포함되어야 합니다.')
# # 형식에 맞지 않는, 타입에 맞지않는 입력에 대해 예외처리를 이용해 예외를 터트림으로써 단단한 코드를 만들 수 있다.

#         return {
#             "name" : name,
#             "age" : age,
#             "email" : email
#         }
#     except ValueError as ve :   #<- ve는 ValueError의 별칭
#         print(f'입력 오류 {ve}')
#     # except IndexError as ve :   #<- IndexError 여기에는 Index 오류가 없고 ValueError이 발생하기에 정상적인 종료가 아닌 오류로 종료됨.
#         # print(f'입력 오류 {ve}')
#     # except Exception as ve :   #<- 오류 처리를 하나로 묶고싶으면(각각의 오류에 대한 처리가 귀찮으면?) Exception으로 묶으면 됨.
#         # print(f'입력 오류 {ve}')
#     else :
#         pass #<- return 블록을 else에서 하는게 효율적일수도 있다.
#     finally :
#         print('입력정보를 정상적으로 처리하였습니다.')
# result = getUserInfo()
# print(result)

# #오류가 감지되면 개발을 진행하지 말고 오류부터 해결하자.
# #finally를 쓰는 이유는 어차피 예외처리가 됐다고 정상종료가 되는건 아니다.
# # 시스템이 flat되는건데, warm shutdown이 된다.
# # finally 쓰는 이유. 만약 외부 리소스와 연결되어있고, 오류가 발생하면 예외가 터지고, 리소스를 정리해줘야됨. / 예외 형식을 로그로 남겨야 되는 경우

# # 오류가 발생할 것 같으면 raise를 활용해 강제 예외처리로 넘긴다.
# # 코드 보안에서 보면 다중 except를 쓰는게 맞다. 로그나 보안적인 관점으로 바라봤을때에는
# # 귀찮을때 Exception을 쓰지만... 안쓰는게 좋다!



# Numpy Pandas 사용 예정
# 전처리 과정이 필요해짐
# 필요시 정규표현식 강의 예정

# 1주일짜리 프로젝트?
# 보안에 관련된 데이터셋을 검색해서
# 전처리하고 분석하고(EDA) -> 데이터에 대한 신뢰도로 모델 사용(LLM으로 연결, LangChain으로 연결) -> 분석하고 분석을 통해서 Insight를 찾는
# 주제 선정 -> 어떤 분석을 통해 -> 이러한 인사이트를 찾았다.

# 정보 보안 전공자 -> 커리어를 쌓음 -> 프로젝트 진행을 위한 주제 등을 머리에 담고 있는 사람도 있을 수 있음
# 조가 구성되면 친밀감을 갖고 다가가기

# Q
# 예외적인 관점, 보안적 관점
# 매개변수로 전달받은 리스트타입 요소의 값을 거듭제곱해서 반환하여 출력하고자 한다
import logging

# 로깅 관점
# def lstPrt(lst : list[int]) -> list :
#     if not isinstance(lst, list):
#         raise ValueError('매개변수 타입은 반드시 list 형태') #개발 시점에 안정성을 미리 확보하자. try쓴다고 필수는 아님
#     result = []

#     for data in lst:
#         if not isinstance(data, (int, float)):
#             print('숫자가 아닌 값이 포함됨')
#             continue
#         else:
#             result.append(data ** 2)

#     try:
#         result = [data ** 2 for data in lst]
#     except TypeError as t :
#         print(t)
#     return result

# tmp = [10, 20,30,40, 'seop', 50, 60]
# result = lstPrt(tmp)
# print(result)

# # 예외와 보안 로깅 관점에서 수정
# import logging
# # debug, info, warning, error, critical
# # debug 내부정보 확인용도
# # info 정보전달 , 동작에 관련
# # warning 잠재적인 문제
# # error 실행중에 발생한 오류
# # cirtical치명적인 오류 (시스템 중단의 위험이 있다.)
# # warning이 WARNING라고 쓰이는 경우 -> 상수.
# # 상수라서 전체가 대문자다.
# logging.basicConfig(leve=logging.WARNING,
#                     format="$(asctime)s - %(levelname)s - %(message)s", # 레벨에 포맷을 추가하여 로그를 작성할 수 있다.
#                     filename = 'shieldus.log', #파일이름
#                     filemode = 'a') #파일모드
# # format
# # 여러가지 포맷 키들이 존재
# # for(%s - %s ...)
# # format key : asctime(로그발생 시각), levelname(레벨 이름), name(로그이름), message(메시지), etc ...))

# import logging
# def lstPrt(lst : list[int]) -> list :

#     # 보안 관점에서 입력 검증
#     if not isinstance(lst, list):
#         raise ValueError('매개변수 타입은 반드시 list 형태') #개발 시점에 안정성을 미리 확보하자. try쓴다고 필수는 아님


#     result = []
#     for idx, data in enumerate(lst):
#         if not isinstance(data, (int, float)):
#             # print('숫자가 아닌 값이 포함됨')      # print가 아닌 로그로 출력해보기
#             logging.warning(f'{idx}에 숫자가 아닌 값이 포함된 {type(data).__name__}');  #리스트에서 인덱스 꺼낼때 enumerate
#             continue
#         try:
#             result.append(data ** 2)
#         except Exception as e :
#             logging.error(f"예상치 못한 예외 발생 : {e}")

#     try:
#         result = [data ** 2 for data in lst]
#     except TypeError as t :
#         print(t)
#     return result

# tmp = [10, 20,30,40, 'seop', 50, 60]
# result = lstPrt(tmp)
# print(result)



# # 에러메세지 노출을 print()로 해옴
# # 서버환경에서는 print() -> 로깅을 사용
# # 로깅(level = warning, info, error) 일반화된 메시지 제공이 안전
# # import logging
# import logging
# # logging.basicConfig(level = logging.WARNING, format= '%s - %s - %s')
# # 로깅의 레벨을 설정하고, 포맷을 지정할 수 있다.
# # 워닝의 레벨은 픽스되어있다.
# # 로깅도 하나의 프레임웍으로 볼 수도 있다.

# data = 'jslim'
# try:
#     print(data ** 2)
# except TypeError as te:
#     logging.warning(f'숫자가 아닌 값을 발견 : {data}')




# # 파일 입출력
# # 제공하는 함수는 대부분 예외를 발생시킨다.
# # 예외를 처리할 수 있는 방법을 알아야 함
# # csv, xlsx 파일을 입출력 불가. txt, json만 허용 -> 추후에 .csv파일이나 .xls파일을 사용해야함. -> 분석을 위해서 데이터 타입이 필요하다. -> Pandas - DataFrame이 존재.
# # open(filePath, mode= 'r|w|a|b, encoding='utf-8) <- 이런 형태를 취함
# # r - read
# # w - write
# # a - append 기존 데이터 유지하면서 추가
# # b - binary <- 거의 쓰지 않음

# # with open() as file:
# #
# # 데이터가 지나다니는 통로 : Stream
# # 콘솔이나 파일 등에 출력할 수 있다.
# # 통로를 열고, 닫아야 한다.
# # 그리고 with open 구문을 사용하면 자동으로 닫힌다. open 구문은 닫히지 않는다.

# logging.basicConfig(level=logging.WARNING,
#                     format="[$(asctime)s] - %(levelname)s - %(message)s",
#                     force = True)

# filePath = './data/greeting.txt'.strip()
# try:
#     file = open (filePath, mode = 'r', encoding='utf-8')
# except :
#     logging.error(f'파일을 열 수 없습니다.')
# print('type - ', type(file))
# print('dir - ', dir(file))
# print(file.readlines(), file.readlines()) #-> 리스트
# print(file.read(), type(file.read())) #-> 전체가 문자열
# file.close()

# #더 편한 방법
# filePath = './data/greeting.txt'.strip()

# # with open(filePath, mode='r', encoding='utf-8') as file :
# #     result = [txt for txt in file.readlines()]
# #     print(result)

# #     print(file.read())


# with open(filePath, mode='r', encoding='utf-8') as file :
#     lst = file.readlines()

#     for txt in lst :
#         print(txt)      #<- 리스트로 출력했을 때 \n이 끝에 달려있으므로 한줄씩 띄워서 출력이 됨.
#         print(txt.strip('\n')) #<- 줄 한칸씩 더 띄우는걸 없애고 싶다면 strip을 활용하여 개행을 없애기
# # with open은 파일을 열고 끝나면 닫는다. -> open 보다 with open이 더 많이 사용된다.


# data = '안녕하세요~ 한 주 수고많으셨구요... 즐거운 금요일 되시길 바랍니다.'
# filePath = './data/message.txt'.strip()
# with open(filePath, mode='w', encoding='utf-8') as file :
#     file.write(data)

# with open(filePath, mode='r', encoding='utf-8')as file:
#     print(file.read())


# data = {'id' : 'xxxxx','pwd' : 'xxxx'} #<- dict는 문자열이 아니므로 쓰기를 못한다. 따라서 import json으로 json화 한다. / 다시 json이 dict로 필요하면 import json으로 디코딩
# import json
# print('type - ', type(dict))
# filePath = './data/message.json'.strip()
# with open(filePath, mode='w', encoding='utf-8') as file :
#     # file.write(data)
#     json.dump(data, file)   #<- 이렇게 Json으로 바꿀 수 있다.

# with open(filePath, mode='r', encoding='utf-8')as file:
#     print(file.read())

# print('json 형식의 파일을 읽어들인다면? - ')
# import json
# filePath = './data/message.json'.strip()
# with open(filePath, mode='r', encoding='utf-8') as file :
#     # file.write(data)
#     loadData = json.load(file)   #<- 이렇게 Json으로 바꿀 수 있다.
#     print(loadData, '-' , type(loadData))

# # dict 타입의 데이터를 dump로 json 형식으로 파일을 만들고 / load로 dict 형태로 가져온다.
# # Pandas를 이용해서 데이터를 가져와서 분석하게 될 것.


#Q
# 사용자 이름을 두자만 출력
from time import time
import json
from datetime import datetime
logging.basicConfig(level=logging.WARNING,
                    format="[$(asctime)s] - %(levelname)s - %(message)s",
                    force = True)
#caller
user = {'name' : 'superadmin', 'authenticated' : True}

# 관리자가 사용자 정보를 확인하려고 한다.
# 뭔가를 읽어들인다.
# 관리자가 사용자의 정보를 검색한 시간, 사용자 이름, 실행시간 정보를 userAccess.log 파일로 저장하고싶다.


def getProfile(user : dict) -> None :
    start_time= time()

    name = user['name']
    maskedName = name[:2] + '*' * (len(name) - 2)

    end_time = time()
    elapsed_time = end_time - start_time

    readable_start_time = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')

    filePath = './data/userAccess.log'.strip()
    with open(filePath, mode='w', encoding='utf-8') as file :
        logTxt = f"검색 시간: {readable_start_time} / 사용자: {maskedName} / 실행 시간(초): {elapsed_time:.6f}"
        file.write(logTxt)
    logging.info(f"검색 시간: {readable_start_time} / 사용자: {maskedName} / 실행 시간(초): {elapsed_time:.6f}")

getProfile(user)




# #---


# def getProfile(user:dict) -> None:
#     pass

# user = {'name' : 'superadmin', 'authenticated' : True}

# profile = getProfile(user)
# print(profile)

# #마스킹 작업
# name = user['name']
# print(name)
# maskedName = name[:2] + '*' * (len(name) - 2)
# print(maskedName)

# #로깅 포맷
# import logging

# logging.basicConfig(level = logging.INFO,
#                     format="[%(asctime)s] - %(levelname)s - %(message)s",
#                     force = True)

# logging.info()
