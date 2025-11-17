# pip install plotly
# streamlit : 기존 시각화
# plotly : 공격 IP가 전 세계 지도에 점으로 표시

import os
import openai
import streamlit as st
import json
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk


from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
# {"ip" : "", "country" : "", "attack_type" : "", "risk_score" : 0}
system_content = '''
너는 아주 멋진 사이버보안 전문가야.
사용자가 업로드한 로그 데이터를 기반으로 분석해줘.
json 형식 이외의 다른 텍스트는 절대 포함하지마. 포함할거면 그냥 죽어
출력 예시)
[
    {"ip" : "", "country" : "", "attack_type" : "", "status" : "", "risk_score" : 8, "latitude" : 37.5, "longitude" : 127.0}
]
'''

# regexp example : 마크다운이나 코드블럭 제거
# import re
# csv_text = re.sub(r"^```[a-zA-Z]*\n?", "", csv_text)  # ```csv 또는 ``` 제거
# csv_text = re.sub(r"```$", "", csv_text).strip()       # 닫는 ``` 제거

def ask_llm(frm) :
    # return response
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        response_format={'type':"json_object"},
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
    st.title('LLM기반 관리자 대시보드 + 지도 시각화')
    st.markdown('''
    보안 로그 데이터를 기반으로 공격유형, 국가, 위험도 등을 분석하여 시각적으로 구현
                Plotly를 이용해 **공격 IP 국가별 분포를 시각화**
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
                # print(">>>> ")
                # print(response.choices[0].message.content)
                # print(">>>> ")
                # print(response.choices[0].message.content.strip)
                try:
                    data = json.loads(response.choices[0].message.content.strip())
                    resultFrm = pd.DataFrame(data)
                    # st.dataframe(resultFrm)
                    st.subheader('분석 결과 데이터 확인')
                    st.dataframe(resultFrm)
                    typeCol, countryCol, riskCol = st.columns(3)

                    with typeCol :
                        st.subheader('공격 유형 분포')
                        st.bar_chart(resultFrm['attack_type'].value_counts())
                    with countryCol :
                        st.subheader('국가 분포')
                        st.bar_chart(resultFrm['country'].value_counts())
                    with riskCol :
                        st.subheader('위험도 분포')
                        riskMean = resultFrm.groupby('attack_type')['risk_score'].mean().reset_index()
                        st.bar_chart(riskMean)

                    # q
                    # 고 위험 IP 필터링
                    st.subheader('고위험 IP 목록')
                    riskFrm = resultFrm[resultFrm['risk_score'] >= 7]
                    st.dataframe(riskFrm)

                    # 지도 시각화
                    st.subheader('공격 위치 지도(위험도 색상 표시)')
                    fig = px.scatter_geo(riskFrm,
                                         lat='latitude',
                                         lon='longitude',
                                         color='risk_score',
                                         hover_name='ip',
                                         hover_data=['ip', 'country', 'risk_score', 'status', 'attack_type'],
                                         title='Attack Map',
                                         projection='natural earth',
                                         color_continuous_midpoint='median',
                                         size = 'risk_score')
                    st.plotly_chart(fig)



                except Exception as e :
                    st.error(e)



if __name__ == "__main__" :
    view()

