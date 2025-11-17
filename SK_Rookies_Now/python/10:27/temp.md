공격에 대한 원리, 방어에 대한 원리로 → 코드를 작성

해커가 코드를 가지고 공격 → SQL injection, xss, csrf → 프로그램 코드와 입력값 조작 → 보안 전문가가 된다면 방어할 수 있도록 코드가 어떻게 동작하는지 이해하는게 더 중요

취약점 및 자동화

반복적인 수작업을 → 도구로 제작.

보안은 수없이 많은 데이터를 다룸

- 로그
- 포트 스캔
- 취약점 탐지

→ 사람이 수작업으로 할 수 없다. → 프로그램 코드를 작성할 수 있어야 됨 → 취약점 분석 및 스크립트 작성을 하게 된다. → 이중에 파이썬을 활용

파이썬

- 보안쪽도 있지만
- 데이터 분석이나 인공지능 쪽 보안
- 클라우드 쪽 보안, 시스템 보안 등등 다양함
- 최종적으로 보안 사고에 대한 대응(로그 분석, 포렌식 데이터 추출 → 스크립트 작성)
- 문법적으로 언어 정리

프로그램언어

- 컴파일 기반 언어 : 고급 언어로 소스코드를 만듬 (ex : [src.py](http://src.py))
    - 사람 언어는 기계가 이해 불가 → 따라서 컴퓨터가 이해할 수 있는 언어로 번역 → 바이너리 코드, 바이트 코드로 변경 (컴파일) → 프로그램 실행
    - 컴파일이라는 과정이 인터프리터
    - 대표 : 자바
- 인터프리터 방식 : 컴파일 과정이 생략, 라인단위로 해석
    - 대표 : 자바 스크립트, 파이썬
    - 변수의 데이터 타입을 정의하지 않는다. → 이러한 점으로 인해 데이터 이슈가 발생 가능 → 변수의 타입을 체크하기.
    - 누군가에게 전달받은 데이터로 작업하기 때문에, 데이터 타입을 확인하지 않고 작업하는건 휴먼에러의 발생 확률을 높이게 됨.
    - 묵시적인 변수의 타입을 갖고 있음.
- 컴파일과 인터프리트 방식 차이 :
- 변수 : 데이터를 담는 그릇
    - 데이터 타입의 존재 유무에 따라 컴파일 기반, 인터프리터 방식이 될 수 있음.
    - 변수 선언 방식 사용할 수 있는 네이밍 컨벤션
        - Camel Case : numberOfColleageGraduates → 변수와 함수
        - Snake Case : NumberOfColleageGraduates → 클래스를 만들 때 자주 사용하는 방식
        - Pascal Case : number_of_colleage_graduates → 가급적이면 비추천
    - 카멜케이스 위주로 만들자.
    - 숫자로 시작하면 안됨
    - 특수문자는 _ $ 정도만 허용됨.
- 예약어는 변수로 사용할 수 없음.
- “”” “”” , : 독 스트링 형태
- # : 주석
    
- `['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']`

변수(Variable)

Python Built-In Types

- Numeric : int, float
- Sequence : list, tuple
- Text Sequence : sequence에 text sequence 추가도 가능
- Set :
- Mapping : dict
- Bool :

변수에 값이 할당되는 시점에 데이터 타입이 지정됨. 그전에는 데이터 타입 X

파이썬도 객체지향 방식 → OOP 적용.

현업에서 문서화시 : 표준으로 만들때에는 펑션 기반이 아닌, 클래스 기반으로 만들어서 확장 시킴

함수(fucntion) vs 메서드(method)

- 함수는 단독 실행이 가능
- 메서드는 객체에 종속적이다. 단독 실행이 불가능하다.

변수 타입 확인을 위한 함수 - type()

Sequence - list type

[ ] = 순서가 있는 열거형(Array가 아님, 배열이 아님)

파이썬에서 dict는 {}

- dict 작성 후 화면 출력시 {} 기호로 나옴 → dictionary다.

web - javascript 에서도 {}를 사용함.

- {} : Object 객체라고 함. / 주로 json으로 표현하는 경우가 많음.
- json은 하나의 표현식 / 노테이션(?)
- rest api service
- open api

browser → backend → DB

FE(프론트엔드 | BE(백엔드)

- json 형식으로 데이터를 주고받게 됨.
- 레거시로 하나의 서버와 통신이 되지만 다른 서버 open api에는 접속불가
- SPA는 가능, 데이터 통신 표준 포맷은 json 형태를 취하고 있다.

새로운 개발보다는 기존의 서비스를 개선하는 방향으로 갈 수 도 있다.

lambda → 화살표 혹은 익명함수

어디 보안을 담당할지 모르지만 전체적인 워크플로우는 알아야 함.

사내 표준 문서를 만들 때에는 function 기반이 아닌 class 기반으로 만듬.

- int, list, dict 모두 클래스 기반
- class 라고 하지만 class list, class dict 이런 방식
- function은 object

list → 열거(숫자를 나열)

dict → 사전(키와 값 나열)

tuple → set

- 집합 (set, tuple)
- 기본적으로 () 기호를 사용
- 단순 숫자만 삽입하면 int로 출력. “,” 기호를 필수로 사용
- 튜플도 Indexing, slicing 가능.
- 불변성을 갖는다.(immutable)

Text Sequence

- 인덱싱, 슬라이싱 가능

파이썬 파일들의 모듈이 있고, 그 모듈들이 모이면 패키지

클래스들이 있고 그 안에 var, function 이 존재한다.

function과 메서드를 구분할 수 있어야 한다.

set

- dict와 동일하게 {} 사용 (값이 없을 경우 {} 만 입력 시 dict로 인식
- 순서가 보장되지 않는다.
- 중복을 보장하지 않는다.
- 변수와 메서드를 받을 수 있다.
- 슬라이싱 인덱싱 불가
- 변경 가능하다
- print( dir (empSet))
    - 매직 메서드
    - `['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',`
    - 매직 함수
    - `'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']`
- 집합 연산도 가능하다. (합집합, 교집합, 차집합)
- set 연산자 ( | , & , - , ^ )
- 보안 관점에서 set()을 사용한다면?
    - 중복 로그인 감지(토큰 또는 세션을 관리)
        - 사용자 ID 집합들을 만들어두고
        - 사용자 로그인 시 같은 아이디가 로그인중이라면 예외처리
    - 허용 IP 관리하기

연산자(Operator) : in

언어마다 자체의 특이한 연산자들이 있다.

출력 형식

- 출력 형식과 포맷은 다양하다.
- print() → 중간중간 코드의 실행 흐름 확인
    - print할 때 민감정보는 출력 금지. 마스킹처리 하기.
    - 문자열도 + 기호로 이어 출력하기 가능
        - +로 연결해서 출력하는것도 보안적으로 위험 가능성 높음
- f - string()
    - 3.6 버전부터 출시했으므로 구형 버전시 충돌 가능성 있음. (버전 확인 필수)
    - {} 안에 변수나 표현식을 넣을 수 있음
- str.fromat()
    - format을 활용하여 ()안에 출력문의 변수의 개수와 동일하게 입력
    - 변수를 다른 이름으로 변경해서 삽입 가능
- 서식 지정 연산자
    - C 스타일 포맷 : %s, %d, %f, %.2f → 보안적인 지점에서는 취약점이 될 수 있음.
- 줄바꿈(개행) : \n
- 형변환 함수 : {변환할 타입}({변수명})
- 다중라인 출력 “”” “”” ,
    - 리포트 메시지 출력할때 사용 가능.
    - 한번에 여러줄의 여러 문장을 전송하거나 쿼리문 끊어 작성할 때, 로그 출력 등등
    - 중요한 정보는 마스킹처리 하기.
- 숫자 포맷
    - 1000단위로 구분할때 print(f”{num:,}”)
    - print(f"{num:20.2f}") → 전체 20자리에서 우측 정렬
    - print(f"{num:>20.2f}")->우측 print(f"{num:<20.2f}")-> 좌측 print(f"{num:020.2f}")-> 빈자리 0으로 채우기
- 분석은 json이 아닌 List형태를 취함
    - List안에 여러개의 Dictionary
    - gen ai를 활용하여 데이터를 가져오게 되면 Json의 출력형식을 지정해줘야 원하는 형식에 맞게 데이터 전달 가능 → 이를 활용하여 출력형식을 만들 수 있다.
    - 따라서 List와 Dict 연습을 잘 해야함
- 보안 관점에서의 로그
    - 이벤트로 수집된 데이터의 파싱을 용이하게 하기 위해서
    - 탐지를 위한 규칙을 생성
    - 변조된 데이터 식별을 쉽게 하기 위해서
    - loginUser = { 'type' : 'guest', 'ip' : '192.168.0.10', 'event' : 'LOGIN_ACCESS' }
- 리스트에 로그를 쉽게 넣기 위해서는 반복문 사용
- logMsg를 활용하여 출력 형식을 만듬 f”[ALTER] User = {}, IP = {}, event = {}” print(logMsg)
- ㄴ> {} 안에 변수나 표현식을 바인딩 하기.

Numpy, Pandas 학습 후

더미데이터를 활용하여 시각화

그 데이터를 활용하여 GenAI에게 전달

인공지능의 프롬프트를 활용하여 정확하게 지시를 전달

전달 후 받을 수 있는 형식을 규격화된 JSON으로 받아야 함.

→ 이거를 로그 형식으로 뿌림

Iter, add, append, extend,insert, pop, remove, revberse, sort emdemd

리스트는 대괄호

튜플은 소괄호

셋, dict는 중괄호

튜플은 패킹과 언패킹

- 소괄호 없이 변수를 선언할 수 있었다.

현장에서는 [] {} 두가지를 가장 많이 사용

{}를 쓴다는건 json으로 주로 응용

numeric은 int, float 주로 사용

형변환을 할 줄 알아야 한다. 함수를 활용하여 형변환(int, list, str 등등)

Boolean

- 참(True), 거짓(False)
- 조건문, 비교, 논리 연산자에서 사용
- semi boolean 이라는 개념이 있음.
- 0,1로도 bool()로 감싸면 boolean으로 활용 가능
- (’’) 빈 공간은 False / (’a’) 무언가 채워져 있으면 True