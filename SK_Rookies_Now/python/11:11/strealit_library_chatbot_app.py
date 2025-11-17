# import os
# from dotenv import load_dotenv

# # .env 파일에서 API 키를 로드합니다.
# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

# # 구버전 라이브러리에 맞는 import 경로
# from langchain.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.chains import RetrievalQA
# from langchain.chat_models import ChatOpenAI
# from langchain.text_splitter import CharacterTextSplitter

# # 외부 DB 개념으로 사용할 문서(doc)를 만듭니다.
# doc = [
#     '리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.',
#     '튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다.',
#     '딕셔너리는 키(key)와 값(value)의 쌍으로 데이터를 저장합니다.'
# ]

# # 문서를 청크(chunk) 단위로 분할합니다.
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# texts = text_splitter.create_documents(doc)

# # OpenAI 임베딩 모델을 초기화합니다.
# # 구버전에서는 openai_api_key 파라미터를 사용합니다.
# embeddings = OpenAIEmbeddings(openai_api_key=api_key, model='text-embedding-3-small')

# # 분할된 텍스트와 임베딩 모델을 사용하여 FAISS 벡터 데이터베이스를 생성합니다.
# db = FAISS.from_documents(texts, embeddings)

# # 질문-답변(QA) 체인을 생성합니다.
# qa_chain = RetrievalQA.from_chain_type(
#     llm=ChatOpenAI(openai_api_key=api_key, model_name="gpt-4o-mini"),
#     chain_type="stuff",
#     retriever=db.as_retriever()
# )

# # 챗봇에게 질문을 던지고 답변을 받습니다.
# query = "리스트가 뭐야?"
# # .run() 메소드는 간단히 질문(string)을 받아 답변(string)을 반환합니다.
# response = qa_chain.run(query)

# print(f"질문: {query}")
# print(f"답변: {response}")


'''
도서관 사서 챗봇 만들기
- 사용자가 묻고
- 챗봇(인공지능 모델)은 먼저 DB(RAG)부터 관련 내용을 찾아본 후
- 그 정보를 참고해서 똑똑해진 다음
- 사용자에게 응답
'''
import os
from dotenv import load_dotenv

# .env 파일에서 API 키를 로드합니다.
load_dotenv()

# 최신 버전에 맞는 import 경로 사용
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores      import FAISS
from langchain.text_splitter     import CharacterTextSplitter
from langchain.chat_models       import ChatOpenAI
from langchain.chains            import RetrievalQA

# 외부 DB 개념으로 사용할 문서(doc)를 만듭니다.
doc = [
    '리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.',
    '튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다.',
    '딕셔너리는 키(key)와 값(value)의 쌍으로 데이터를 저장합니다.'
]

# 문서를 청크(chunk) 단위로 분할합니다.
text_splitter = CharacterTextSplitter(chunk_size=1000)
texts = text_splitter.create_documents(doc)

# OpenAI 임베딩 모델을 초기화합니다.
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')

# 분할된 텍스트와 임베딩 모델을 사용하여 FAISS 벡터 데이터베이스를 생성합니다.
# 이것이 RAG의 핵심인 '검색(Retrieval)'을 위한 데이터베이스입니다.
db = FAISS.from_documents(texts, embedding=embeddings)
print(db)

# 질문-답변(QA) 체인을 생성합니다.
# 1. llm: 답변 생성에 사용할 언어 모델 (ChatOpenAI)
# 2. chain_type: "stuff"는 검색된 모든 문서를 프롬프트에 넣는 가장 간단한 방식입니다.
# 3. retriever: 위에서 생성한 벡터 데이터베이스를 기반으로 관련 문서를 찾는 검색기입니다.
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4o-mini"),
    chain_type="stuff",
    retriever=db.as_retriever()
)

# 챗봇에게 질문을 던지고 답변을 받습니다.
query = "리스트가 뭐야?"
response = qa_chain.invoke({"query": query})

print(f"질문: {query}")
print(f"답변: {response['result']}")

# 검색
retriever = db.as_retriever(search_kwargs={'k':1})
print('retriever - ', retriever)

# chain
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4o-mini"),
    # stuff, map_reduce, refine etc...
    chain_type="stuff",
    retriever=retriever
)

# 질의
'''
간단한 사실 확인
예제코드 요청
비교-선택 도움

RAG가 강한 부분 = 문서 기반의 질의응답
'''
query = '파이썬 리스트와 튜플의 차이점을 설명해줘.'
answer = qa.run(query)
print('Q - ', query)
print('사서가 참고한 내용 - ', )
print('answer - ', answer)
