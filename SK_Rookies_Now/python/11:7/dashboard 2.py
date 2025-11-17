import streamlit as st
import numpy     as np
import pandas    as pd
import plotly.express as px 

st.title('관리자 대시보드') 

# 파일 업로드
file = st.file_uploader('csv 파일 업로드  : ', type=['csv'])

if file is not None : 
    rawData = pd.read_csv(file)
    st.success(f'{file.name} 업로드 성공') 

    # side bar
    st.sidebar.header('필터 설정')
    countryFilter = st.sidebar.multiselect('국가선택 : ',
                                           rawData['country'].unique())
    attackFilter  = st.sidebar.multiselect('공격타입 : ',
                                           rawData['attack_type'].unique())
    
    
    st.write("프레임 데이터출력을 도와주는 : dataframe() ")
    st.dataframe(rawData.head())

    # 시각화를 위한 필터 데이터 
    filterData = rawData[ (rawData['country'].isin(countryFilter)) & (rawData['attack_type'].isin(attackFilter)) ]

    st.subheader('시간별 공격 발생 추이 - line ') 
    fig01 = px.line(filterData, x='time', color='attack_type')
    st.plotly_chart(fig01) 

    st.subheader('국가별 공격 비율 - pie ') 
    fig02 = px.pie(filterData, names='country') 
    st.plotly_chart(fig02) 

    st.subheader('침해공격유형별 상태 - bar ') 
    fig03 = px.bar(filterData, 
                   x='attack_type' , 
                   color='status',
                   title="공격유형별 상태") 
    st.plotly_chart(fig03) 
 
    
    

