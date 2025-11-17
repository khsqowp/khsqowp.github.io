import os
from dotenv import load_dotenv
import streamlit as st

# .env 파일에서 API 키를 로드합니다.

api_key = os.getenv("OPENAI_API_KEY")

# 최신 버전에 맞는 import 경로 사용
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores      import FAISS
from langchain.text_splitter     import CharacterTextSplitter
from langchain.chat_models       import ChatOpenAI
from langchain.chains            import RetrievalQA

doc = [
    '리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.',
    '튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다.',
    '딕셔너리는 키(key)와 값(value)의 쌍으로 데이터를 저장합니다.'
]

def ask_gpt() :
# # 문서를 청크(chunk) 단위로 분할합니다.
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.create_documents(doc)

# # OpenAI 임베딩 모델을 초기화합니다.
# # 구버전에서는 openai_api_key 파라미터를 사용합니다.
    embeddings = OpenAIEmbeddings(openai_api_key=api_key, model='text-embedding-3-small')
    db = FAISS.from_documents(texts, embeddings)

    retriever = db.as_retriever(search_kwargs={"k": 1})
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-4o-mini", temperature = 0.9),
        chain_type="stuff",
        retriever=retriever
    )
    return qa, retriever


def view():
    st.title('LangChain + RAG 도서관 사서봇')

    query = st.text_input('질문을 입력하세요 : ')
    if query :
        with st.spinner('외부 데이터베이스를 검색하고 있습니다...'):
            qa, retriever = ask_gpt()
            answer = qa.run(query)
            st.success(' A - ' + answer)

            st.success(' A - ' + answer)
            st.caption(' R - ' + retriever.get_relevant_documents(query)[0].page_content)




if __name__ == "__main__" :
    view()
