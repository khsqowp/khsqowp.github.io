
# LLM : 대형 언어모델, 인공지능을 학습하기 위해서는 방대한 데이터가 필요, 문장을 이해하고 답변할 수 있는 인공지능 모델(알고리즘)
# RAG ( Retrieval Augmented Generation) : 사용자가 질문을 하면, 관련된 문서를 검색하여 그 내용을 바탕으로 답변을 생성하는 방식, LLM이 대답하기 전에 관련 문서를 찾아서 참고할 수 있도록 도와주는 비서
# LangChain : 다양한 데이터 소스와 LLM을 연결하여, 더 나은 결과를 도출할 수 있도록 돕는 프레임워크, LLM + RAG - AI 연결 조립 키트


# .env api key load (보안상 안전을 위해서 마스킹)

# 'gpt-4o-mini'는 채팅 모델이므로 ChatOpenAI를 사용합니다.
# API 키는 환경 변수에서 자동으로 읽어옵니다.

# .invoke() 메소드를 사용하여 응답을 생성하고, content 속성을 출력합니다.

        # role : system, user, assistant
        # content : content
    #응답 문장의 길이제한
# 딥러닝
# cnn rnn 시험 나옴
# cnn 이미지 판별하는것
# rnn 시계열 데이터, 자연어 처리
# 임베딩 매트릭스를 인공지능 모델에 넣고, 학습된 인공지능이 확률적으로 결정



import os
from dotenv import load_dotenv
import openai
from langchain_core.prompts import ChatPromptTemplate
import chromadb

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

# .env api key load (보안상 안전을 위해서 마스킹)
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

print('LLM - ')
# 'gpt-4o-mini'는 채팅 모델이므로 ChatOpenAI를 사용합니다.
# API 키는 환경 변수에서 자동으로 읽어옵니다.
client = ChatOpenAI(model_name='gpt-4o-mini')


prompt = input('검색하고자 하는 내용을 입력하세요 : ')
print('prompt - ', prompt)

# .invoke() 메소드를 사용하여 응답을 생성하고, content 속성을 출력합니다.
system_content = '''
당신은 친절한 파이썬 보안 도우미입니다.
    사용자의 요청에 대해 항상 보안 모범 사례를 우선으로 설명하고,
    민감 정보 노출을 방지하는 방법, 최소 권한 원칙, 패키지/채널 검증, 파일 권한 설정,
    취약점 완화 방법을 구체적 명령어와 체크리스트 형태로 제공하십시오.
    응답에 실제 비밀번호나 실사용 API 키를 절대 포함하지 마십시오.
    '''

user_content = f'''
1) 패키지 설치시 보안 지침
2) 모니터링 권장 설정 방법
3) 민감정보 관리 방법과 예시
4) 가상환경 구축 권장 방법
{prompt}
'''

# .invoke() 메소드를 사용하여 응답을 생성하고, content 속성을 출력합니다.
response = client.chat.completions.create(
    model = 'gpt-4o-mini',
    messages = [
        # role : system, user, assistant
        # content : content
        {'role' : 'system', 'content' : system_content},
        {'role' : 'user', 'content' : user_content}
    ],

    #응답 문장의 길이제한
    max_tokens = 1024,
    # 출력 다양성(무작위성) : 보수적, 창의적
    temperature = 0.7
)
print('response - ', response)
print('content - ', response.choices[0].message.content)

# python.exe streamlit_library_chatbot_app.py
# streamlit run streamlit_library_chatbot_app.py
