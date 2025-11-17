
# pip install plotly
# streamlit : 기존시각화
# plotly : 공격 IP가 전 세계 지도에 점으로 표시 

import os
import openai
import json 

import streamlit as st
import pandas    as pd
import numpy     as np 
import plotly.express as px 


##############################
from   openai import OpenAI
from   dotenv import load_dotenv

# openai key load     
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY') 

system_content = '''
너는 아주 멋진 사이버보안 전문가야.
사용자가 업로드한 로그 데이터를 기반으로 리스크 위험도 분석해줘.

- ip : 공격IP
- country : 공격 발생 국가명(영문)
- status : 'Blocked' 또는 'Allowed'
- risk_score : 1 ~ 10 숫자
- latitude : 해당 국가의 대략적인 위도(중심값)
- longitude : 해당 국가의 대략적인 경도(중심값)
json 형식이외의 다른 텍스트는 절대 포함하지 마.!!
예시)
[
    {"ip" : "", "country" : "", "attack_type" : "", "status" : "" , "risk_score" :  8, "latitude" : 37.5, "longitude" : 127.0} 
]
'''

###################################################### 
def ask_llm(frm) :
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            # role : system, user, assistance
            # content : content
            {'role' : 'system'  , 'content' :  system_content},
            {'role' : 'user'  , 'content' : f'로그분석\n{frm.head(20).to_dict()}' }
        ],
        # 응답 문장의 길이제한
        max_tokens=1500,
        # 출력 다양성(무작위성) : 보수적, 창의적 : 0 ~ 1 낮을수록 보수적
        temperature=0.8
    )
    return response 
    


def view() :
    st.set_page_config(page_title='보안로그분석AI', layout='wide')
    st.title('LLM 기반 관리자 대시보드 + 지도 시각화')

    st.markdown('---')
    st.markdown('''
    보안 로그 데이터를 기반으로 공격유형, 국가, 위험도등을 분석하여 시각적으로 구현
    Plotly를 이용해 **공격 IP 국가별 분포를 시각화**
    ''')

    # csv 파일 업로드
    file = st.file_uploader('***_log.csv')
    if file :
        frm = pd.read_csv(file)
        st.dataframe(frm.head())

        if st.button('분석요청') :
            with st.spinner('분석중......') :
                response = ask_llm(frm)

                # response parsing
                # print()
                # print(">>>>>>>> content")
                # print(response.choices[0].message.content)
                # print()
                # print(">>>>>>>> strip")
                # print(response.choices[0].message.content.strip()) 
                try :

                    data = json.loads(response.choices[0].message.content.strip())
                    resultFrm = pd.DataFrame(data) 
                    st.success('분석 완료!!') 
                    st.subheader('분석 결과 데이터 확인')
                    st.dataframe(resultFrm)
                    typeCol, countryCol, riskCol = st.columns(3) 

                    with typeCol : 
                        st.subheader('공격유형 분포')
                        st.bar_chart(resultFrm['attack_type'].value_counts())
                    with countryCol :
                        st.subheader('나라별 공격비율 ')
                        st.bar_chart(resultFrm['country'].value_counts())
                    with riskCol :
                        st.subheader('위험도 평균')
                        riskMean = resultFrm.groupby('attack_type')['risk_score'].mean()
                        st.bar_chart(riskMean) 

                    # Q - 고위험 IP 필터링 
                    # risk_score 7 이상인 IP들만 필터링해서 데이터 프레임으로 출력 
                    st.subheader('고위험 IP 목록')
                    riskFrm = resultFrm[resultFrm['risk_score'] >= 7]
                    st.dataframe(riskFrm)

                    st.write(resultFrm.dtypes)

                    # 지도 시각화 
                    st.subheader('공격 위치 지도(위험도 색상표시)') 
                    fig = px.scatter_geo(
                        resultFrm,
                        lat='latitude',
                        lon='longitude',
                        color='risk_score',
                        hover_name='ip',
                        hover_data=['country','attack_type'],
                        title='Attack Map',
                        projection='natural earth',
                        color_continuous_scale='Reds',
                        size='risk_score'  
                    )
                    st.plotly_chart(fig, use_container_width=True) 
                    
                except Exception as e :  
                    st.error( e ) 



 
if __name__=='__main__' :
    view()