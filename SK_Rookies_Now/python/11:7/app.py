import pydeck as pdk # 지도 시각화
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.title('streamlit 시각화 Demo')  # 웹 브라우저에서 문서를 만들어주는 함수


frm = pd.DataFrame({
    "timestamp" : pd.date_range('2025-11-06', periods=100, freq='H'),
    "user"      : np.random.choice(['admin', 'superAdmin', 'root', 'guest', 'analyst'], 100),
    "ip"        : np.random.choice(['192.168.0.1', '192.168.0.3', '192.168.0.5', '192.168.0.7', '192.168.0.9'], 100),
    "status"    : np.random.choice(['success', 'fail'], 100, p=[0.6, 0.4]),
    "delay_ms"  : np.random.randint(20, 800, 100)
})


st.header("데이터 출력")
st.write("프레임 데이터 출력을 도와주는 함수 : dataframe()")
st.dataframe(frm.head())

st.write("정적 프레임 데이터 출력을 도와주는 : table()")
st.table(frm.head())

st.write("json 형식 : json()")
st.json({'status' : 'fail', 'cnt' : len(frm)})

st.header("Chart")
st.line_chart([1,2,3,4,5,6,7,8,9])
st.area_chart([1,2,3,4,5,6,7,8,9])
st.bar_chart([1,2,3,4,5,6,7,8,9])


frm = pd.DataFrame({
    'Country' : ['한국', '미국', '일본', '호주'],
    'Gdp' : [1000, 2000, 3000, 4000],
    'Population' :[100, 200, 300, 400]
})

fig = px.bar(frm, x='Country', y='Gdp', title='국가별 GDP', color='Country')
st.plotly_chart(fig)
fig02 = px.scatter(frm, x='Population', y='Gdp', hover_name='Country', title='GDP vs Population')
st.plotly_chart(fig02)

st.header("Image, Audio, Video")
st.video('https://www.w3schools.com/html/mov_bbb.mp4')

st.header("사용자의 입력")
data = st.slider('선택하세요 : ', 1, 100, 10)
st.write(f'당신의 선택은 : {data}')

st.markdown('''
마크다운 형식을 지원합니다.
''')
