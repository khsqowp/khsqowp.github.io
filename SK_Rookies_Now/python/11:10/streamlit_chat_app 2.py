import os
import openai
import streamlit as st 

from openai import OpenAI
from dotenv import load_dotenv

def askChat(query, key) :
    # chat-model LLM 이용해서 입력값을 전달하고 응답을 반환 
    client = OpenAI(api_key=key) 
    
    # LLM 
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [{'role' : 'user' , 'content' : query }]
    )
    # response = f'{query}질문의 응답 내용입니다.'
    return response.choices[0].message.content  

def main() :
    st.set_page_config(page_title='챗 모델을 이용한 응답') 

    if 'api_key' not in st.session_state :
        st.session_state['api_key'] = '' 

    with st.sidebar :
        key = st.text_input(label='OPENAI KEY', 
                            placeholder='api key',
                            value='',
                            type='password') 
        if key : 
            st.session_state['api_key'] = key

    st.header('요약 응답') 
    st.markdown('---')
    txt = st.text_area('글 입력') 
    if st.button('요약해줘') :
        st.info(askChat(txt, st.session_state['api_key']))


if __name__=='__main__' :
    main()