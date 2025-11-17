from copy import copy, deepcopy

import random
#copy = 모듈 / copy, deepcopy = 함수
#---
# ###

# ### 학습 예상 진도

# 열거형, 제어구문, 반복문

# 프로그램 언어라고 하는건 → 데이터를 다룸

# 변수 : 데이터를 담는 그릇

# - 기본 타입 : 데이터를 담는다
# - 참조 타입 : 메모리 주소 값을 담는다

# 객체지향 - Object Oriented Program

# - 실세계에 존재하는 객체 (무형, 유형의 것들) → 재료
# - 이를 프로그램 영역에서 구현하고싶어함
# - 컴퓨터에 그대로 넣을 수 없음 → 실세계의 객체를 프로그램에 넣기 위한 변형 템플릿 : 클래스
# - 프로그램에서는 인스턴스라고 부름
# - 파이썬은 참조타입만 존재하고, 기본타입은 존재하지 않는다.
# - 명사적인 특징 → 변수로 정의
# - 동사적인 특징 → 메서드로 정의
# - dict, list, tuple 등등 → 클래스
# - 클래스에 정의된 변수나 메서드는 클래스의 소유가 아닌, 인스턴스의 소유가 된다.
# - .을 찍고 쓰는것들 → 단독이 아님 (인스턴스의 소유다)

# 변수에 값을 담는 시점부터 타입이 결정됨 → 따라서 타입에 대해서 잘 알아야 함

# 이전에 배운 변수의 타입들을 확장 예정

# ### 학습 목표

# - 변수타입 응용
# - 열거형
# - 반복구문, 분기
# - 함수

# 변수에 문자열을 할당하면 참조타입이 STR이 된다.

# 문자를 컨트롤하는 다양한 메서드들이 존재
url = 'http://www.naver.com'

print('type - ', type(url))

print('com - ', url[-3 : ])
print('instance method - ', dir(url))

print('find - ', url.find('com'))
# com 이라는 단어 찾기
print('com -  ', url[url.find('com') : ])

companyName = '     SK      '

print('type - ', type(companyName), 'len - ', len(companyName))
#공백 제거
print(companyName.strip(' '), len(companyName.strip(' ')))

companyName = 'samsung'
#첫 문자를 대문자로
print('첫번째 문자를 대분자로 ', companyName.capitalize())

# .xls로 끝나는지 확인하지
fileName = 'report.xls'
print('flag - ', fileName.endswith('.xls'))

# 함수유형 4가지
# - 매개변수 받고 반환X -> 의미없음
# - 매개변수 받고 반환
# - 매개변수는 없지만 반환
# - 매개변수도 안 받고, 리턴도 하지 않음 -> 의미없음

# 모아서 한번에 출력 -> 함수

# 사용자 정의 함수
# def를 사용
# 함수는 블록을 가져야 한다. 주로 () 사용 (다른 언어는 {} 주로 사용)
# worker function
def printCoin( ):
    print('코인')

# 호출 caller
printCoin()

def greet(name):
    return f"Hello~ {name}"


result = greet('jslim')
print(result, type(result))

lst = [1,2,3,4,5,6,7]
print('type - ', type(lst))


print(dir(lst))
print('max - ', max(lst))
print('min - ', min(lst))
print('min - ', sum(lst))
print('mean - ', sum(lst) / len(lst), type(int(sum(lst) / len(lst))))

# 참조타입은 주소값을 담는 것.
# 파이썬에서 사용하는 모든 데이터타입은 참조타입으로 변수에 값이 아닌 주소값을 담는다.

lstTmp01 = [1,2,3]    # 참조타입
lstTmp02 = [1,2,3]    # 참조타입

print('instance address - ', id(lstTmp01), id(lstTmp02))
print('is - 주소번지를 비교하는 연산자 ' , lstTmp01 is lstTmp02)

#주소값을 copy
#얕은 복사(shallow copy) vs 깊은 복사(deep copy)
#얕은 복사 -> 동일 객체 복사
#같은 객체를 바라보고 있기에 원본 수정 -> 얕은복사 항목도 변경됨
lstTmp03 = lstTmp01 #<- 얕은 복사라는 뜻

#기본 모듈이 아닌것들은 반드시 import, from ~ import 구문 활용해서 사용 승인을 얻어야 함
#하나의 파일을 만들면 하나의 모듈이 됨. -> 다른 모듈을 가져다 쓸 때 사용
# import 모듈 전체를 사용 / from ~ import 모듈에서 일부를 사용
#깊은 복사 -> 내부에서 리스트를 새롭게 만들기 때문에 원본 영향 X
#파이썬에서 카피할 때에는 전부 얕은 복사로 진행

print('is - 주소번지를 비교하는 연산자 ' , lstTmp01 is lstTmp03)

#리스트는 리스트 중첩 가능, 리스트가 dict 중첩이 대부분
original = [[1,2],[3,4]]

shallowCopy = copy(original)
deepCopy = deepcopy(original)

original [0][0] = 2

print('shallowCopy - ',shallowCopy)    # 새롭게 만들어서 요소의 값을 그대로 카피, 내부의 값 주소는 동일
print('deepCopy - ', deepCopy)         # 요소의 주소는 같지만 담는 컨테이너가 새롭게 만들어지는 것

#List는 가변 [0][0]을 2로 바꿨을 때 기존 메모리 값에 대한 것만 변경됨

#보안관점
# 얕은복사는 값이 공유됨 -> 예기치않게 공유되는 변수의 수정이 될 가능성 있음. -> 공유객체의 무분별한 참조
# 사용자의 세션정보나 토큰 정보를 copy해야될 경우 얕은복사는 금지 -> 깊은 복사를 해야 로그나 메모리에 오래 남길 수 있음.
# 민감한 데이터는 얕은복사를 해서는 안된다.

# 복사라는 개념은 파이썬에서는 얕은 복사
# 혹시라도 보안 관점에서 코딩을 할 때에는 불필요한 복사는 피해야 한다.
# 만약 혹시라도 민감한 데이터에 대해 복사하고 오래 유지해야 한다면 무조건 Deep Copy를 활용하기.
print('instance address - ', id(shallowCopy), id(original))
print('instance address - ', id(deepCopy), id(original))


#복사에 취약점
#불변성 - 기존에
userData = {'id' : 1, 'token' : 'secret1234'}
cache = copy(userData)

userData['token'] = 'secret4321' #dict에서 키가 token인 값을 변경 -> str이므로 불변 -> 따라서 새로운 값이 만들어짐 (얕은 복사가 안됨(?))

print(cache['token'])

#---
userData = {'id' : 1, 'roles' : ['admin', 'user']}
cache = copy(userData) #새로운 객체를 만듬. 주소는 다르지만 가리키는 방향은 같음

cache['roles'].append('guest')   #원본 변경이 아닌 Cache에서 변경

print(userData['roles'])        #Cache를 수정했는데 원본이 변경됨 -> 원본의 타입이 가변이었기 때문에. List는 불변, Dict는 가변..?

# 가변(Mutable) / 불변(Immutable)
# 불변 : Numeric, text, tuple, bool, str/ 값 변경시 새로운 객체가 생성
# 가변 : list, dict, set / 값 자체를 변경할 수 있는 타입
# list = [] -> buffer -> 기존 요소의 값이 변함 -> 가변
#


#열거형 : 숫자형 값을 생성하는 객체타입
# range(start, end-1, step)
# range(end-1)
# range(start, end-1)
# range는 가변함수 : 매개변수를 3개를 받을 수도 1개를 받을 수 도 있음. 2개도 가능함

rangeTmp = range(1, 11)
print(rangeTmp, 'type - ', type(rangeTmp)) #객체가 그대로 출력이 됨..

print('dir - ', dir(rangeTmp)) #iter이 있다 -> 반복해서 코드수행이 가능한 객체)

#반복 구문 -> for 변수 in 열거형 :
for data in rangeTmp :
    print(data, end = '\t')    # end = '\t' 는 줄바꿈이 아닌 탭으로 구분 -> 세로가 아닌 가로로 볼 수 있다.

lst = [10, 20, 30]

for i in lst :
    print(i)

for idx in range(len(lst)) :
    print('idx - ',idx, 'data - ', lst[idx])

#In, not in을 쓰면 있다, 없다가 되고 / for ~ in을 써서 반복 구문도 가능

rangeTmp = range(1, 11, 2)
print(rangeTmp, 'type - ', type(rangeTmp)) #객체가 그대로 출력이 됨..

print('dir - ', dir(rangeTmp)) #iter이 있다 -> 반복해서 코드수행이 가능한 객체)

for data in rangeTmp :
    print(data, end = '\t')    # end = '\t' 는 줄바꿈이 아닌 탭으로 구분 -> 세로가 아닌 가로로 볼 수 있다.

rangeTmp = range(11)
print(rangeTmp, 'type - ', type(rangeTmp)) #객체가 그대로 출력이 됨..

print('dir - ', dir(rangeTmp)) #iter이 있다 -> 반복해서 코드수행이 가능한 객체)

for data in rangeTmp :
    print(data, end = '\t')    # end = '\t' 는 줄바꿈이 아닌 탭으로 구분 -> 세로가 아닌 가로로 볼 수 있다.

#append() : 0부터 차곡차곡 넣어주는 메서드
lst = []

for idx in range(10):
    lst.append(random.randint(1,5))
print(lst)


print(' dir - ', dir(lst))
lst.sort() # 원본 자체에 대한 위치 변경 -> 따라서 가변. 기본은 오름차순
lst.sort(reverse = True)
print('sort - ', lst)

#sort는 정렬, .reverse()는 현재 리스트에서 역방향
# in-place : 원본에 반영되는 것들

# 프로그램의 흐름을 제어하는 구문( if ~ else ~  , if ~ in )
#데이터가 있는지 없는지 판단하고싶을 때
# if라는 구분은 True, False를 이용해서 조건처리
if 6 in lst:
    print('find  - ')
else :
    print('not found')

# list comprehension
# 문법은 동일
# [실행문 for 변수 In 열거형_객체]
# [실행문 for 변수 in 열거형_객체 If 조건식]

lst = [2,4,1,5,8,4]
for data in lst :
    print(data, end='\t')

for idx in range(len(lst)):
    print(lst[idx], end = '\t')

for idx in range(len(lst)):
    print(lst[idx]*lst[idx])

result = []
for idx in range(len(lst)) :
    result.append(lst[idx] ** 2)
print(result)

result = [ lst[idx]**2 for idx in range(len(lst))]
print(result)

# 연산자 : % (나머지 구하기)
result = []
for idx in range(len(lst)):
    if (lst[idx] ** 2 % 2) == 0:
        result.append(lst[idx]**2)
print(result)

#list comprehension을 쓰면 성능이 더 좋다.
result = [lst[idx] ** 2 for idx in range(len(lst)) if lst[idx]**2%2 == 0]
print(result)


hund = range(1,101)
hund_lst = []
for idx in hund :
    if idx % 3 == 0:
        hund_lst.append(idx)
print(hund_lst)

hund = range(1,101)
hund_lst = [idx for idx in hund if idx % 3 == 0]
print(hund_lst)

# dict
# 키와 밸류, 키의 중복 허용안함, {}, 불변객체, 숫자 인덱싱 불가, 열거형이 아니므로 순서 존재X, dict는 가변형이지만, Key값으로 불변(immutable)이 아닌 타입은 정의할 수 없다.(list, set, tuple ...)

#사용자에 대한 정보가 dict에 담겨 내려올 때 json -> 파이썬에서는 dict
#사용자의 정보 저장
user = {
    "id" : 100,
    "name" : "admin",
    "role" : "superuser"
}
print(user)

#키 유무 판단하고싶다면?
print("key 유무 판단 - ", "id" in user)
print("key 통한 데이터 접근 - ", user["id"])
print("key 통한 데이터 접근 - ", user.get("id"))
user["address"] = "seoul"
print('data - ', user)


#권한 변경 함수
def updateRole(data, newRole) :
    data["role"] = newRole

#Caller (누군가가 호출해야 동적된다.)
#guest라는 권한을 전달 -> 검증되지 않은 데이터가 수정되는 문제가 생김 -> 권한에 대한 오염, Injection, 정보 변조의 가능성이 있다.
# 함수 내부에서 dict를 그대로 원본 데이터에 직접적인 수정을 진행. -> 보안적인 측면에서 개선되어야 할 코드.
# caller에서 리스트로 만들어두고, 리스트에 존재하는 데이터로만 수정 가능하게 하기 : white list 라고 부른다.(검증된 데이터로만 수정 가능.)
updateRole(user, "guest")
print('data - ', user)

#개선 Ver.
user = {
    "id" : 100,
    "name" : "admin",
    "role" : "superuser"
}


#white list
allowedRoles = {"user", "guest", "manager"} #<- Set 형식 (가변, 중복제거, 인덱싱 슬라이싱 불가능, 순서없음)

def updateRole(data, newRole) :
    copyUser = deepcopy(data)   #<- deepcopy로 원본 건들지 않음
    if newRole in allowedRoles:
        copyUser["role"] = newRole
    else:
        pass

    return copyUser
changeUser = updateRole(user, "guest")

print('original - ', user)
print('copy     - ', changeUser)

#우리는 여기서 키만 찾으면 된다.
prodJson = {
    'melon' : {'price' : 100, 'qty' : 10},      #dict
    'bravo' : [200, 50],                        #리스트
    'bibigo' : [(),()]                          #튜플
}
print(prodJson)

#클래스에 대한 객체생성
dictTmp = dict(city = 'busan', expo = 2030)
print(dictTmp)

dictTmp = dict([
    ('city' , 'busan'),
    ('expo', 2030)
])
print(dictTmp)

# zip()을 현업에서 많이 사용(압축)
# 정제되지 않은 데이터를 필요한 데이터 타입으로 만드는것도 능력
#zip()을 사용하기 위해서는 객체의 개수가 같아야 한다.(데이터셋을 만들어야 한다)
# 서로 다은 데이터타입을 dict로 만들어야 되기도 한다.
keys = ('key01','key02','key03','key04')
datas = ('sk', 'samsung', 'lg', 'lgcns')

dictZip = dict(zip(keys, datas))
print(dictZip)
print('type - ', dir(dictZip))

for key in dictZip :
    print(key, dictZip[key])

for key in dictZip.keys() :         #키 반환
    print(key, dictZip[key])

for key in dictZip.values() :       #값 반환
    print(data)

for key, data in dictZip.items() :  #튜플 형식을 언패킹
    print(key,' - ', data)

wordLst = ['dog', 'dog', 'cat', 'cat', 'word', 'dog', 'cat', 'cs', 'cat', 'cs', 'sk']
wordDict = {word: 0 for word in set(wordLst)}
for word in wordLst:
    wordDict[word] += 1
print(wordDict)

result = dict(zip(set(wordLst), [wordLst.count(data) for data in set(wordLst)]))
print(result)
