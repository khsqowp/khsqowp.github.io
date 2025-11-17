# 학습 목표
# 당연히 LLM, LangChain 복습
# 정규표현식
# 분석 결과 불필요한 정보 전처

# llm
import os , re, openai, json
from   openai import OpenAI
from   dotenv import load_dotenv

# langchain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models       import ChatOpenAI
from langchain.prompts           import ChatPromptTemplate
from langchain.vectorstores      import FAISS
from langchain.text_splitter     import CharacterTextSplitter
from langchain.chains            import RetrievalQA, LLMChain

# 정규표현식이란?
# 문자열 패턴을 만들어서 문자열로부터 검색, 추출, 변환을 도와주는 형식
# csv_text = re.sub(r"^```[a-zA-Z]*\n?", "", csv_text)  # ```csv 또는 ``` 제거
# csv_text = re.sub(r"```$", "", csv_text).strip()       # 닫는 ``` 제거

# 패턴을 만드는 방법
# 메타문자 : . ^ $ * + ? {} [] ()
# . : 임의의 한 문자
# ^ : 문자열의 시작
# $ : 문자열의 끝
# * : 앞 문자가 0회 이상 반복
# + : 앞 문자가 1회 이상 반복
# ? : 앞 문자가 0회 또는 1회 존재
# {} : 앞 문자의 반복 횟수 지정 {m,n} m회 이상 n회 이하
# [] : 문자 집합, [abc] a 또는 b 또는 c
# () : 그룹화, (abc)+ abc가 1회 이상 반복

# 패턴 : /d /D /w /W /s /S
# /d : 숫자 [0-9]와 매칭
# /D : 숫자가 아닌 문자와 매칭
# /w : 단어 문자 [a-zA-Z0-9_]와 매칭
# /W : 단어 문자가 아닌 문자와 매칭
# /s : 공백 문자 (스페이스, 탭, 개행 등)와 매칭
# /S : 공백 문자가 아닌 문자와 매칭

# 이메일, 전화번호 정규표현식
txt = "문의하신 고객의 전화번호는 010-1234-5678이고, 추가 문의사항이 있으면 help@example.com 으로 연락주세요."
patternEmail = r'\w+@\w+\.\w+'
patternPhone = r'\d{3}-\d{3,4}-\d{4}'

# re.search() -> 첫 매칭되는 것 반환(부분 매치)
# re.match() -> 문자열 처음부터 매칭되는지 확인 (문자열 시작에서 매치))
# re.fullmatch() -> 전체 문자열이 매칭되는지 확인 (전체 문자열이 패턴과 일치할 때)
# re.sub() -> 치환
# re.findall() -> 매칭되는 모든 것 반환(리스트)

email = re.search(patternEmail, txt)
print(email)
# <re.Match object; span=(10, 26), match='help@example.com'>
print(email.group())
# help@example.com

# 전화번호 추출 패턴
phone = re.findall(patternPhone, txt)
print(phone)
# <re.Match object; span=(11, 23), match='010-1234-5678'>
# print(phone.group())
# 010-1234-5678

# Q
# 숫자만 추출한다면
lst = re.findall(r'\d+',txt)
print(lst)
# ['010', '1234', '5678']

# 정규표현식을 알아야 하는 당위성

# AI 모델 반환 결과는 자유로운 영혼의 문자열
# 필요에 따라서 특정 조건에 만족하는 데이터를 추출해야 되는 경우, 변환해야 되는 경우 발생
# 이럴 경우 re를 이용해서 처리해야 함.

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def masking(key) :
    if len(key) <= 8 :
        return '*' * len(key)
    return key[:4] + "*" * (len(key) - 8) + key[-4:]

if api_key:
    masked_api_key = masking(api_key)
    print(f"Masked API Key: {masked_api_key}")
else:
    print("API key not found. Please check your .env file.")

chat = ChatOpenAI(model_name = "gpt-3.5-turbo", api_key=api_key, temperature=0.8)
# temperature(0 ~ 1)
# 값이 낮을수록 응답은 보수적(같은 입력이면 거의 같은 답변)
# 값이 높을수록 응답은 창의적(같은 입력이면 다양한 답변)

chat_uncreative = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=api_key, temperature=0)
chat_creative = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=api_key, temperature=1)

prompt = "인공지능을 간단히 설명해줘."
print('uncreative - ', chat_uncreative.predict(prompt))
print('creative - ', chat_creative.predict(prompt))
# uncreative -  인공지능은 인간의 학습능력, 추론능력, 지각능력, 언어능력 등을 컴퓨터 프로그램이나 기계에 구현한 기술을 말합니다. 이를 통해 기계가 인간과 유사한 지능적인 작업을 수행하거나 인간의 결정을 돕는 등 다양한 역할을 수행할 수 있습니다. 인공지능 기술은 머신러닝, 딥러닝, 자연어 처리, 컴퓨터 비전 등 다양한 분야에서 활용되고 있습니다.
# creative -  인공지능은 기계가 지능적인 작업을 수행할 수 있도록 하는 기술이며, 기계가 인간의 학습, 추리, 해결, 판단 등의 인지 능력을 모방하도록 고안된 분야입니다. 주로 머신 러닝과 딥 러닝 기술을 활용하여 데이터를 분석하고 패턴을 학습하여 문제를 해결하는 기술을 지칭합니다. 인공지능은 다양한 분야에서 활용되며, 음성인식, 이미지 인식, 자율주행차, 의료 진단, 금융 분석 등의 다양한 분야에서 발전이 이뤄지고 있습니다.


# langchain llm model
chat = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature = 0)

# langchain prompt template
question = '섭섭님과 사담이 필요하면 jslim9413@naer.com 또는 jslim9413@gmail.com 으로 문의 부탁드립니다.'
prompt = ChatPromptTemplate.from_template(
    """
    해당 텍스트에서 이메일을 추출해줘 : {text}
"""
)

# langchain except RAG
chain = LLMChain(llm = chat, prompt = prompt)


print(chain.run(text = question))
# jslim9413@naer.com, jslim9413@gmail.com

answer = chain.run(text='오늘 날씨 알려줘')
print(answer)
print('re -')
emails = re.findall(r'\w+@\w+\.\w+', answer)
print(emails)






'''
Quiz) 아래 제공되는 입력정보를 바탕으로 langchain 모델을 만들고 실행해 본다.
- 조건) 프롬프트는 : json 형식으로 정리해줘
- 조건) llm의 반환값을 확인하고 json 형식인지 확인하고 해당 결과를 정규표현식을 사용하여 데이터만 추출하고
- 조건) 구조화된 json 데이터를 만들기(json.dumps())
'''

reservation = """
이름  : 임섭순
연락처: 010-1234-5678
예약일: 2025-11-15
문의 이메일: jslim9413@naver.com
추가 이메일: jslim9413@gmail.com
"""

# 1. 프롬프트 작성
# 2. reservation 데이터와 프롬프트를 llm에 전달
# 3. llm 반환값 확인
# 4. json 형식이 아닐 경우 정규표현식으로 데이터만 추출
# 5. json.dumps()로 구조화된 json 데이터 만들기
prompt = '''
당신은 친절한 데이터 분석가입니다.
사용자가 업로드한 로그 데이터를 기반으로 분석해줘.
json 형식 이외의 다른 텍스트는 절대 포함하지마. 포함할거면 그냥 죽어
{reservation}
출력 예시)
[
    {{"name" : "", "phone" : "", "date" : "", "email1" : "", "email2" : ""}}
]
'''
chain = LLMChain(llm = chat, prompt = ChatPromptTemplate.from_template(prompt))
response = chain.run(reservation=reservation)
# re를 활용하여 json 형식 데이터만 추출, 불필요한 텍스트 제거
print('response - ', response)
pattern = r'\[.*\]'  # 대괄호로 감싸진 부분만 추출
match = re.search(pattern, response, re.DOTALL)  # re.DOTALL: 줄바꿈 포함 모든 문자 매칭
if match:
    response = match.group(0)
    print('>>> json 형식 데이터 추출 성공')
else:
    print('>>> json 형식 데이터 추출 실패')
json_data = json.dumps(response)
print('json_data - ', json_data)


chat = ChatOpenAI(model_name = "gpt-4o-mini", temperature = 0)
prompt = ChatPromptTemplate.from_template(
    """
    당신은 친절한 보안 로그 분석가입니다.
    사용자가 업로드한 로그 데이터를 기반으로 분석해줘.
    json 형식 이외의 다른 텍스트는 절대 포함하지마. 포함할거면 그냥 죽어
    {log_data}
    출력 예시)
    [
        {{"name" : "", "phone" : "", "date" : "", "email1" : "", "email2" : ""}}
    ]
    """
)

chain = LLMChain(llm = chat, prompt = prompt)

# answer = chain.run(log_data=reservation)
answer = chain.run(text=reservation)
pattern = r'json\s*(\{[\s\S]*?\})'  # 중괄호로 감싸진 부분만 추출
match = re.search(pattern, answer)
if match :
    result = match.group(1)
    print('result - ', result)
    # json.dumps() (dict -> json) , json.loads() (json -> dict)
    print('type - ', type(json.loads(result)))
answer = re.sub(r"^```[a-zA-Z]*\n?", "", answer)
result = re.sub(r"```$", "", answer).strip()
print(result)
