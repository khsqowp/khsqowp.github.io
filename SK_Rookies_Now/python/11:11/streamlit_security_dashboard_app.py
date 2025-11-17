import os
import openai
import streamlit as st
import json
import pandas as pd
import numpy as np

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

system_content = '''
너는 아주 멋진 사이버보안 전문가야.
사용자가 업로드한 로그 데이터를 기반으로 분석해줘.
json 형식 이외의 다른 텍스트는 절대 포함하지마. 포함할거면 그냥 죽어
출력 예시)
[
    {'ip' : '', 'country' : '', 'attack_type' : '', 'risk_score' : 0}
]
'''

def ask_llm(frm) :
    # return response
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
        # role: system, user, assistance
        # content : content
        {'role' : 'system', 'content': system_content },
        {'role' : 'user', 'content': f'로그분석\n{frm.to_dict()}' }
    ],
    max_tokens=4096,
    temperature=0.8
    )
    return response

def view() :
    st.set_page_config(page_title='보안 로그 분석 AI', layout = 'wide')
    st.title('LLM기반 관리자 대시보드')
    st.markdown('''
    - 보안로그 데이터를 기반으로 공격유형, 국가, 위험도 등을 분석하여 시각적으로 구현
    - LangChain과 RAG 기법을 활용하여 보안 관련 질문에 답변합니다.
    ''')

    # csv 파일 업로드
    file = st.file_uploader("보안 로그 파일을 업로드하세요")
    if file :
        frm = pd.read_csv(file)
        st.dataframe(frm.head())

        if st.button('분석 요청'):
            with st.spinner('분석중....'):
                response = ask_llm(frm)

                # response parsing
                # print(response.choices[0].message.content)
                # print(">>>> ")
                # print(response.choices[0].message.content.strip)
                data = json.loads(response.choices[0].message.content.strip())
                resultFrm = pd.DataFrame(data)
                # st.dataframe(resultFrm)
                st.subheader('분석 결과 데이터 확인')
                st.dataframe(resultFrm)


if __name__ == "__main__" :
    view()

