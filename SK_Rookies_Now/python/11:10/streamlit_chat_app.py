import os
from dotenv import load_dotenv
import openai
from langchain_core.prompts import ChatPromptTemplate
import chromadb
import streamlit as st

from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA    # RAG에 특화된 체인
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA


def askChat(query, key) :
    # chat-model LLM 이용해서 입력값을 전달하고 응답을 반환
    # openai 구버전은 client 객체를 사용하지 않습니다.
    openai.api_key = key # API 키를 전역으로 설정

    # LLM 사용 구문
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role' : 'user', 'content' : query}]
    )

    # response = '{query}응답 내용'
    return response.choices[0].message.content


def main():
    st.set_page_config(page_title='챗 모델을 이용한 응답')

    if 'api_key' not in st.session_state :
        st.session_state['api_key'] = ''

    with st.sidebar :
        key = st.text_input('label = input',
                            placeholder = 'api key',
                            value = '',
                            type = 'password')
        if key :
            st.session_state['api_key'] = key

    st.header('요약 응답')
    txt = st.text_area('글 입력')
    if st.button('요약해줘') :
        st.info(askChat(txt, st.session_state['api_key']))

if __name__ == '__main__' :
    main()
