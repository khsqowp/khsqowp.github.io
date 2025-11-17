import os
import openai
import streamlit as st
##############################
from dotenv                      import load_dotenv
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

    # openai key load     
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY') 


    # RAG 숫자배열로 변환
    # chunk_size 는 chunk_overlap(겹치는 글자 수) 보다 커야함 
    text_splitter = CharacterTextSplitter(chunk_size=250)
    texts = text_splitter.create_documents(doc)
    
    # embedding & RAG
    embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
    db = FAISS.from_documents( texts , embedding = embeddings)

    # 검색
    # as_retriever() : 검색 인터페이스를 이용해서 LLM 연결하는 것 
    # Retriever 설정
    retriever = db.as_retriever(search_kwargs={'k' : 1}) # 반환 문서 수 : 1
    
    qa = RetrievalQA.from_chain_type(
        llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.9),
        # stuff, map_reduce, refine etc....
        chain_type='stuff',
        retriever = retriever
    )
    return qa , retriever

def view() :
    st.title('LangChain + RAG 도서관 사서봇')

    query = st.text_input('질문을 입력하세요 : ') 
    if query :
        with st.spinner('외부 데이터 베이스를 검색하고 있습니다....') :
            
            qa , retriever = ask_gpt()
            answer = qa.run(query) 

            st.success('A - '+answer) 
            st.caption('R - '+retriever.get_relevant_documents(query)[0].page_content )    

    
if __name__=='__main__' :
    view()