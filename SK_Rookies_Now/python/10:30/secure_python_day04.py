# 학습 목표(function) -> 객체지향(OOP)적인 언어로 보면 메서드
# 함수에 대해서 알아보자.
# 보안적 관점에서 함수 구현을 해보는 시간
# 1개의 파이썬 파일 = 모듈
# 모듈에서 제공되는 파이썬 코드를 쓰는 느낌
# 대체적으로 재사용적인 느낌은 아님
# 기존에 만든 코드를 다른곳에서 반복해서 사용하려고 할 때 효율적이지 못함. 복붙하거나, 다시 하거나 등등(복잡한 코드가 아님에도 불구하고)
# 기능 구현은 수정이라는것이 매번 발생함, 짠 코드에 대한 디버그도 해야되고..
# 하나의 모듈이 클래스가 될 수 도 있다.
# 모듈에 fuction을 갖고 있을수도 있고, Class를 갖고 있을 수 도 있다.
# 지금까지 인터프리터 방식인 파이썬으로 대화형으로 작성 -> 이제는 var, method 등을 만들게 됨
# 현업에서는 모듈에 클래스를 만듬 클래스{ var, method }
# 이런 모듈들이 패키지로 묶여질 수 있다.
# 패키지가 하위 패키지를 가질 수 있다.
# 이제 function에 대해 살펴보기
# - 코드 재사용성
# - 가독성 향상
# - 수정 사항 발생 시 로직에 대한 외부 변경 사항을 최소화 -> 유지보수 측면에서 용이, 디버깅도 용이
# - 여러 함수를 묶어 모듈로 관리 가능 (import utils) 와 같이.
# def라는 이름을 통해 함수 정의 ([매개변수,매개변수,매개변수]) -> 필요에 따라 매개변수 여러개 선언 가능
# def 함수명 ([매개변수]):
# 실행할 코드
# return 결과값(내장변수타입) // 반환이 필요없다면 생략 가능

# def greet(name='guest') 이렇게 초기값을 줘버리면 caller가 값을 입력하지 않았ㅇ르 때 guest 반환 (default parameter)
def greet(name) : # <- working 함수
    '''사용자에게 인사하는 함수'''
    print(f'hi ~ , {name}') #<- return이 없으므로 반환 타입은 아니다.

greet('jslim') #<- caller 함수

def greet(name) : # <- working 함수
    '''사용자에게 인사하는 함수'''
    return f'hi~, {name}'

result = greet('jslim') #<- caller 함수
print(result)


def userAdd(a,b) :
    return a ** b

result = userAdd(2, 3)          # <- 위치인자 positional argument
print('type - ', type(result))
print('result - ', result)

result = userAdd(b = 2, a = 3)          # <- 키워드 인자 keyword argument
print('type - ', type(result))
print('result - ', result)


# def 네이밍 컨벤션은 동사적인 형태로 하면 좋다. (명사도 좋은가?)



# 람다 함수(lambda function) -> Anonymous Function
# lambda 매개변수 : 실행문 (return 키워드 없이 결과값을 바로 반환)
add = lambda x, y : x + y
print('type - ', type(add))
print(add)
# 람다는 함수의 인자로 함수를 전달하는것도 가능하다.
result = add(3,5)
print('result - ', result)
# 람다는 람다 자체로는 의미가 없다.
# 람다를 많이 쓰는 경우 -> map, filter 이런 기능을 쓸 때 자주 사용한다.
lst = [1,2,3,4,5,6,7,8]

# 기본적
result = [ data ** 2 for data in lst]
print(result)

# 람다
double = lambda data : data ** 2
# double(lst)  <- int 타입이 들어가야 되는데 list 타입이 들어감. 따라서 map이라는 함수가 있다.
# 람다는 간단한 함수를 만들어서 적용하는것.
# map -> 열거형 타입.(반복 가능한 요소에 대해서 특정 함수를 적용하고 그 결과를 map 객체로 반환)
# map이라는 함수는 인자를 2개 받는데 function, iterable 두개를 받는다.
# map(function, iterable)
lst2 = map(double, lst)
print(list(lst2))
lst2 = map(lambda data : data ** 2, lst)
print(lst2)

# filter 함수 -> map과 거의 비슷하다.
# filter(function, iterable)

double = list(filter(lambda data : data % 2 == 0, lst))
print(list(double))


wordLst = ['pineApple', 'apple', 'watermelon', 'banana', 'cherry']
result = sorted(wordLst, key= lambda x : len(x))
print(result)

# 클로져때 람다 사용 가능
# 리스트가 있다고 가정
# 반환 예시) ['www.skshieldus.com' 'www.samsung.com', ...]
def makeUrl(lst : list) -> list : # <- 타입을 지정함으로써 가독성 증가, lst : list <- 리스트로 받겠다. (lst : list) -> : (이거는 리스트로 받고 리스트로 반환하겠다.)
    return list(map(lambda x : 'www.' + x + '.com', lst)) # 보안의 취약점이 있을 수 있음. 악성 스크립트라던가 쿼리문 입력에 대한 검증이 없음. -> 입력 데이터에 대한 검증 없이 웹 페이지에 출력하게 된다면 XSS 취약점 발생.

from urllib.parse import quote #<- 공백이나 특수문자를 안전하게 인코딩
# def safeMakeUrl(lst : list) -> list :
#     return list(map(lambda x:'www.' + quote(x)+'.com',lst))
def safeMakeUrl(lst : list) -> list:
    if not isinstance(lst,list) :
        raise TypeError("입력은 리스트 타입으로 전달 부탁드립니다.")
    if not all(isinstance(name, str) for name in lst ) :
        raise ValueError("문자의 타입은 문자열")
    return list(map(lambda x : 'www.' + quote(x) + '.com', lst))

companyLst = ['sk shieldus', 'samsung', 'lg cns', 'sk cnc', '<script>alert(1)</script>']
urls = safeMakeUrl(companyLst)
print(urls)


# def myColor(name, color, TFCheck) : -> 파스칼 케이스보다는 카멜케이스, TFCheck보다는 is{} 방식 사용 권장
#     TFCheckAns = "좋아" if TFCheck == True else "싫어"
#     ans = name + '님은 ' + color +'색을 ' + TFCheckAns + '합니다.'
#     return ans

def myColor(name, color, isFlag : bool) :
    print(f"{name}닙은 {color}색을 {'좋아' if isFlag == True else '싫어'}하십니다.")

result = myColor('섭섮님', 'red', False)
print(result)
result = myColor('섭섭님', 'blue', True)
print(result)


#클로져, 데코레이터, 가변인자 등등.. 수업예정

# 함수화 : 어떤 기능을 모듈화 시키는 것
# 내부적으로 보안에 관련된 부분들을 고민해보는것.
# 이슈 : 변수에 대한 scope에 대한 이해.
# 함수의 규칙 : LEGB
# local에서 찾고 없으면 enclosing.
# enclosing에도 없으면 global
# global에도 없으면 built-in

globalVar = 10 #모듈이 선언되어있고, globalVar 는 변수 = 전역변수
print(globalVar) #전역변수이므로 전역에서 호출 가능

def outer() :   # function 만들기. function은 또 다른 function을 중첩할 수 있다.
    enclosingVar = 20   # 외부 함수 변수
    def inner() :
        localVar = 30   # 지역 변수
        print('global - ', globalVar)
        print('enclosingVar - ', enclosingVar)
        print('localVar - ', localVar)
    inner()
    # print(localVar) 이거는 오류 발생.localVar is not Defined -> 즉 블록을 벗어나서 변수에 접근을 못한다.
outer()
print('globalVar - ',globalVar)
# print(enclosingVar) -> outer() 함수 안에 있기에 외부에서 단독 호출 불가. 접근 문제 발생.


x = 10
def test():
    x = 20
test()
print(test())
print(x)


cnt = 0

def increment() :
    global cnt
    cnt += 1
    # cnt += 1        #cnt는 지역변수이기 때문에 접근이 안된다.

increment()
increment()
increment()

print(cnt)



def outer() :
    outerVar = 10   # 로컬 변수라기보다는 인클로징 변수다.
    def inner() :
        nonlocal outerVar
        # outerVar += 1 이렇게 부르면 안된다.
        outerVar += 1
        print('inner outerVar : ', outerVar)
    inner()
    print('outer outerVar : ', outerVar)
outer()

# 함수 안에 함수 안에 함수도 nonlocal 사용하면 됨.
# 대부분 함수 안에 함수를 넣을 때에는 1,2차원 내로 구성됨
# 보안관점에서 전역변수를 거의 쓰지 않는다. : 외부에서 공개되지 않기 위해서.
# 민감한 데이터(api키나 개인정보)를 전역변수로 쓰는것은 위험하다. -> 이런 정보를 유지하기 위한 방법으로 클로져 문법이 나오고, 데코레이터를 활용하여 코드를 작성.

#클로져(Closure) -> 전에 있던 변수를 기억하는것..?
# 함수가 호출되는 시점에서만 데이터 기억 / 클로져는 함수가 종료 되어도 외부 변수를 기억하는 것
# 따라서 단일함수가 아닌 중첩 함수에서 발생
# 중첩함수 - 함수 내부에서 외부함수의 변수를 기억하는 것.
# 클로져를 통해서 알아야 할 것 -> 상태유지
# 상태유지 -> 전역변수를 쓰지 않고도 함수 내부에서 상태를 유지할 수 있기 때문에.

# 함수 장식자(데코레이터) : 클로저 기반이다. 그래서 클로저에 대해서 잘 알아야 한다.

def outer(name : str) :
    def inner() : #외부에서 접근할 수 없다. 은닉화 느낌
        return f'hi ~ , {name}'
    return inner #함수를 반환

msg = outer('jslim') # 함수를 호출한건 여기서 끝.

print(msg, 'type - ', type(msg))
print('result - ', msg())   #outer라는 함수가 종료되어도 기존에 호출된 파라미터값을 기억하고 있다. -> 클로져. -> 전역함수를 사용하지 않고도 상태유지 가능


# 보안관점에서 취약점. 아래 코드를 클로져로 바꿔본다.
cnt = 0 # <- 전역변수다

def increment() :
    global cnt
    cnt += 1
    # cnt += 1        #cnt는 지역변수이기 때문에 접근이 안된다.

increment()
increment()
increment()

print(cnt)

#전역변수를 사용하지 않고 상태를 유지하는 코드개선

def counter() :
    count = 0 #지역변수, 중첩되는 입장에서는 인클로징 변수
    def increase() :
        nonlocal count #counter의 count를 사용할 수 있게 선언
        count+=1
        return count
    return increase


cnt = counter() # function은 cnt <- increase()
print(cnt())
print(cnt())
print(cnt())
print(cnt())
print(cnt())

#지역을 쓰면 휘발성, 전역을 써야 데이터가 유지가됨. 그러나 취약점이 있다.
#클로져를 기반으로 취약점을 보호할 수 있게 된다.
# outer는 inner를 반환하는게 기본 문법
# outer를 써도 outer의 값을 그대로 유지한다.

#클로져 함수를 이해해야 데코레이터를 사용할 수 있다.
# decorator(한수 장식자)
# dcorator는 현업에서 자주 사용됨.
# 로깅작업할때, 권한 체크, 실행시간 측정 등에서 사용
# 함수를 감싸서 기능(공통의 로직)을 추가, 수정 등을 시켜주는 것

# 모든 함수에서 권한 체크가 필요할때 / 로깅 작업 해야할 때 / 실행시간을 측정해야될 때
# 반복될 수 밖에 없는 작업이다. -> 함수장식자라는 개념을 사용하게 되면 반복되는 작업들을 만들지 않고,(별도로 만들지 않고) cross cutting으로 치고 들어가서 진행. -> 코드 진행해만 집중할 수 있게 된다.
# 데코레이터는 공통의 기능이어야 한다. 특정 로직을 건드리는게 아니라

# 클로져 기반으로 데코레이터 구성 -> 데이터의 상태유지가 가능하다는 장점
# def decorator() :
#     def logic() :
#         pass
#     return logic()


# 로깅, 권한체크, 실행시간 측정 등을 함수로 미리 만들어둬야 한다.
def commonChecking() :
    print(">>>>>> permission check")
def commonLogging() :
    print('>>>>>>> log...')

#실제 로직 구현 함
# 파이썬은 함수 인자로 함수 인자를 전달하는게 가능하다.
def decorator(checkingFunc, logginFunc) :
    def logic() :
        checkingFunc()
        print('업무로직 수행')
        logginFunc()
    return logic

# 함수에서 함수를 가져오는 모습
innerLogic = decorator(commonChecking, commonLogging)
innerLogic()

# 함수가 실행되고 끝나면 값을 유지할 수 없다.
# 동일한 함수를 여러번 출력하면 항상 같은 값을 출력해야된다.
# 그러나 함수 내의 함수를 호출함으로써 상태값을 유지하게 된다.
# 이를 활용하여 함수에서 다른 함수 인자로 받아서 추가 후 진행하면 데코레이터가 된다.

def clo(num):
    x = 10
    def test():
        nonlocal x
        x += num
        return x
    return test
a = clo(1)
print(a())
print(a())
print(a())
print(a())


# print('실행시간 성능 로그 - ')
# from time import time
# def timer() :
#     def wrapper() :
#         pass

# def timerFunc() :
#     pass

# inner = timer(timerFunc)
# inner()
# 가변인자 함수 : 몇개의 매개변수가 전달될지 모르는것.
# 두가지의 가변인자 : *args, **args 두가지가 있다.
# *args : 튜플형태
# **args : 키워드 인자(dict 형태)

def variableLenArgs(*args: int) -> None : #<- 튜플형태의 인자가 전달되어야 함 + 들어오는 만큼 받을 수 있다.
    print('type - ', type(args))
    total = sum(args)
    return total

result = variableLenArgs(1,23,24,23,2,5,63)
print(result)
result = variableLenArgs(1,2,6,3,435,54,423,234,36,234,34)
print(result)
result = variableLenArgs(1,2,3,4,5,6,7,8) # 튜플 형태이다.
print(result)
#---
def variableLenArgsDict(**args) :
    print('type - ', type(args))
    for key, value in args.items() :
        print(key, value)
variableLenArgsDict(name='jslim',age=30, region='seoul')


def variableLenArgsMix(subject, *args, **kwargs) :
    print('title - ', subject)
    print('args - ', args)
    print('kwargs - ', kwargs)

variableLenArgsMix("사용자 정보", "임섭순", "섭섭해", "쉴더스", a=1, b=2)


#내일 : 예외처리, 파일 입출력, 클로져를 이용한 데코레이터 활용(퀴즈)
# endpoint : 마지막에 도착하는 호스트
# 프론트엔드와 백엔드의 상호작용을 위한 규칙 : API 명세서
# 프론트엔드에서 백엔드에 요청하는 URL -> 엔드포인트

# url 관련 인코드 = from urllib.parse import urlencode
from urllib.parse import urlencode
params = {"q":'secure', "page":2}
queryString = urlencode(params)
print(queryString)

#http://api.v1.example.com/search?q=secure&page=2
def makeApiRequest(endpoint, **params) :
    q_string = endpoint + '?' + urlencode({"q": 'secure', 'page': 2})
    return q_string
result = makeApiRequest('http://api.v1.example.com/search', q='secure', page=2)  # q='secure', page=2 이게 가변인자.
print(result)

# 보안 관점에서 코드 개선을 한다면
#http://api.v1.example.com/search?q=secure&page=2
from urllib.parse import urlencode
def makeApiRequest(endpoint, **params) :
    whiteLst = {'q', 'page','lang'}                                 # 키 검증
    safeParams = {k : v for k,v in params.items() if k in whiteLst} # 파라미터 검증
    q_string = endpoint + '?' + urlencode(safeParams)
    return q_string
result = makeApiRequest('http://api.v1.example.com/search', q='secure', page=2)  # q='secure', page=2 이게 가변인자.
print(result)
