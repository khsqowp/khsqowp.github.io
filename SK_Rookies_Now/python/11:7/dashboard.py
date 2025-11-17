# llm쪽으로 input 던지고 langchain이랑 llm
# 나온 결과를 분석을 통해서 시각화 하고 인사이트를 얻기.
# 이를 웹페이지로.
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import pydeck as pdk  # 지도 시각화

st.title('관리자 대시보드')

# 파일 업로드
file = st.file_uploader('CSV 파일 업로드 : ', type=['csv']) # 진짜 파일 업로드 가능

if file is not None :
    rawData = pd.read_csv(file)
    st.success(f'{file.name} 업로드 성공!')

    # side bar
    st.sidebar.header('필터 설정')
    countryFilter = st.sidebar.multiselect('국가 선택 : ',
                                           rawData['country'].unique())
    attackFilter = st.sidebar.multiselect('공격 타입 : ',
                                          rawData['attack_type'].unique())

    st.write("프레임 데이터출력을 도와주는 : dataframe()")
    st.dataframe(rawData.head())
    # 시각화를 위한 필터 데이터
    filterData = rawData[(rawData['country'].isin(countryFilter)) & (rawData['attack_type'].isin(attackFilter))]
    st.subheader('시간대별 공격 발생 추이 - line ')
    fig01 = px.line(filterData, x='time', color = 'attack_type')
    st.plotly_chart(fig01)

    st.subheader('국가별 고격 비율 - pie ')
    fig02 = px.pie(filterData, names = 'country', title='국가별 공격 비율')
    st.plotly_chart(fig02)

    st.subheader('침해공격 유형별 상태 - bar ')
    fig03 = px.bar(filterData, x='attack_type', color = 'status', title="공격 유형별 상태")
    st.plotly_chart(fig03)

# 분석 혹은 실시간 모니터링 활용 가능 + 이상치 탐지도 가능?
# 지도 시각화도 가능

# 다음주에 할 수업은 아주아주아주 어려울 예정
# 접근하는 방법에 대해서만 이해







# 파인튜닝은 아님
# streamlit을 쓸거면 vscode

# 1차 인성평가 오전 10시 진행 예정
# 안되는 인원들은 다음주 목요일 13일 18:30에 진행 예정
#
# 1차 사후평가 : 다음주 금요일 11월 14일 17:10 ~ 17:40 진행 예정
#
# 미니 프로젝트
# 2주뒤 있을 미니 프로젝트 발표함
# 팀빌딩 확인하기
# 미니프로젝트1의 팀이다.
#
# 대주제 : 데이터 분석 및 시각화
# 데이터 분석과 시각화를 통해 인사이트 도출
# 대주제를 필두로느 ㄴ자유
# - 화장품 종류에 시대적 흐름
#     - 20, 30대에 따른 화장품 분석
# - 파이썬과 데이터분석, LLM을 최대한 활용하는 것.
# - 파일 확장자로 악성 파일 받을 때 확장자 변경 공격 : 통계 등을 조사해서 인사이트 얻기
# - 관제를 할때 splunk, idsips 관제 도구를 배울텐데, 웹공격(sql injection이 어떤 요청을 통해서 들어오고 공격이 터지게 한다던가, 웹 로그 데이터를 조사해서 공격자들이 어떤식으로 조사를 하는지 등등)
# - 보안 자동화 X / 데이터 분석 및 시각화를 통한 인사이트 도출
