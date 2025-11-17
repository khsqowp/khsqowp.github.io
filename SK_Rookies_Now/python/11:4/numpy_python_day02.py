# numpy_python_day02.py
# Pandas 강의 2일차 예제 코드

import numpy as np
import pandas as pd
import warnings
from datetime import date, timedelta

# 경고 메시지 무시
warnings.filterwarnings('ignore')

# ==============================================================================
# 0. 정보 확인용 헬퍼 함수
# ==============================================================================
def array_info(ary):
    """NumPy 배열의 정보를 출력합니다."""
    print('type - ' , type(ary))
    print('shape - ' , ary.shape)
    print('ndim  - ' , ary.ndim)
    print('dtype - ' , ary.dtype)
    print('\ndata  -')
    print(ary)
    print("-" * 30)

def series_info(s):
    """Pandas Series의 정보를 출력합니다."""
    print('type   - ' , type(s)) 
    print('index  - ' , s.index)
    print('values - ' , s.values)
    print('dtype  - ' , s.dtype)
    print('\ndata   - ')
    print(s)
    print("-" * 30)

# ==============================================================================
# 1. NumPy 복습: CSV 파일 로드 및 분석
# ==============================================================================
print("### 1. NumPy 복습: CSV 파일 로드 및 분석 ###")

# data/기후통계분석.csv 파일이 필요합니다.
# 이 스크립트와 같은 디렉터리에 data 폴더를 만들고 그 안에 파일을 넣어주세요.
try:
    raw_data = np.loadtxt('./data/기후통계분석.csv',
                        dtype='U',
                        skiprows=1,
                        delimiter=',')
    print("--- CSV 데이터 로드 성공 ---")
    array_info(raw_data)

    # 최고 기온 데이터 추출 및 타입 변환
    temp_max = raw_data[:, -1].astype(float)

    # 최고 기온이 가장 높았던 날의 전체 정보 찾기
    highest_temp_idx = np.argmax(temp_max)
    highest_temp_info = raw_data[highest_temp_idx]
    print("\n--- 최고 기온이 가장 높았던 날의 정보 ---")
    print(highest_temp_info)

    # 평균 기온 데이터 추출 및 타입 변환
    temp_avg = raw_data[:, 2].astype(float)

    # 평균 기온이 가장 낮았던 날의 전체 정보 찾기
    lowest_avg_temp_idx = np.argmin(temp_avg)
    lowest_avg_temp_info = raw_data[lowest_avg_temp_idx]
    print("\n--- 평균 기온이 가장 낮았던 날의 정보 ---")
    print(lowest_avg_temp_info)

except FileNotFoundError:
    print("오류: './data/기후통계분석.csv' 파일을 찾을 수 없습니다.")
    print("스크립트와 동일한 위치에 'data' 폴더를 생성하고 그 안에 CSV 파일을 넣어주세요.")


# ==============================================================================
# 2. Pandas Series 생성
# ==============================================================================
print("\n### 2. Pandas Series 생성 ###")

# NumPy 배열로 Series 생성
lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
series_from_arr = pd.Series(arr)
print("--- 배열로 Series 생성 ---")
series_info(series_from_arr)

# 딕셔너리로 Series 생성 (키가 인덱스가 됨)
dict_data = {'idx01': 1, 'idx02': 2, 'idx03': 3}
series_from_dict = pd.Series(dict_data)
print("--- 딕셔너리로 Series 생성 ---")
series_info(series_from_dict)

# 데이터와 인덱스를 직접 지정하여 생성
user_data = ('임섭순', '2025-11-04', 'Male', True)
user_index = ['이름', '생년월일', '성별', '결혼여부']
user_series = pd.Series(data=user_data, index=user_index)
user_series.name = '사용자 정보'
user_series.index.name = '신상 정보'
print("--- 데이터/인덱스 지정 및 이름 부여 ---")
series_info(user_series)


# ==============================================================================
# 3. Series 인덱싱 및 슬라이싱
# ==============================================================================
print("\n### 3. Series 인덱싱 및 슬라이싱 ###")

# 인덱싱 (정수 위치, 레이블 이름 모두 가능)
print(f"정수 인덱싱 user_series[0]: {user_series[0]}")
print(f"레이블 인덱싱 user_series['이름']: {user_series['이름']}")

# 멀티 인덱싱 (팬시 인덱싱)
print("\n--- 멀티 인덱싱 ---")
print(user_series[[0, 2]])
print("-" * 20)
print(user_series[['이름', '성별']])

# 슬라이싱
print("\n--- 슬라이싱 ---")
print(user_series[0:2]) # 정수 위치 슬라이싱 (end 미포함)
print("-" * 20)
print(user_series['이름':'성별']) # 레이블 슬라이싱 (end 포함)


# ==============================================================================
# 4. Series와 결측값(NaN) 처리
# ==============================================================================
print("\n### 4. Series와 결측값(NaN) 처리 ###")

# 날짜 인덱스를 가진 Series 생성
today = date(2025, 11, 4)
date_index = pd.date_range(start=today, periods=10)
data_with_nan = pd.Series(data=[np.random.randint(1,100) for _ in range(10)],
                          index=date_index, dtype=float)

# 결측값 삽입
data_with_nan['2025-11-07'] = np.nan
data_with_nan['2025-11-12'] = np.nan
print("--- 결측값이 포함된 원본 Series ---")
print(data_with_nan)

# 결측값 확인 (isnull, notnull)
print("\n--- isnull() 결과 ---")
print(pd.isnull(data_with_nan))

# 불리언 마스킹으로 결측값만 선택
print("\n--- 결측값 데이터 ---")
print(data_with_nan[pd.isnull(data_with_nan)])

# 결측값 채우기 (fillna)
# 방법 1: 특정 값(0)으로 채우기
filled_zero = data_with_nan.fillna(0)
print("\n--- fillna(0)으로 결측값 채우기 ---")
print(filled_zero)

# 방법 2: 평균값으로 채우기
mean_val = np.mean(data_with_nan)
filled_mean = data_with_nan.fillna(mean_val)
print("\n--- 평균값으로 결측값 채우기 ---")
print(filled_mean)

# 결측값 제거 (dropna)
dropped_nan = data_with_nan.dropna()
print("\n--- dropna()로 결측값 제거 ---")
print(dropped_nan)


# ==============================================================================
# 5. DataFrame 소개
# ==============================================================================
print("\n### 5. DataFrame 소개 ###")

# 딕셔너리로 DataFrame 생성
df_data = {
    'feature01': [1, 2, 3],
    'feature02': [10, 20, 30],
    'feature03': [100, 200, 300]
}
df_from_dict = pd.DataFrame(df_data)
print("--- 딕셔너리로 DataFrame 생성 ---")
print(df_from_dict)

# 2차원 배열로 DataFrame 생성
df_from_arr = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                           columns=['A', 'B', 'C'],
                           index=['row_0', 'row_1', 'row_2'])
print("--- 2차원 배열로 DataFrame 생성 ---")
print(df_from_arr)

# 열 이름 변경 (rename)
df_from_arr.rename(columns={'A': 'col_A', 'B': 'col_B'}, inplace=True)
print("\n--- 열 이름 변경 후 ---")
print(df_from_arr)

# 열 추가 및 삭제
df_from_arr['col_D'] = [11, 12, 13]
print("\n--- 'col_D' 추가 후 ---")
print(df_from_arr)

del df_from_arr['col_D']
print("\n--- 'col_D' 삭제 후 ---")
print(df_from_arr)


# ==============================================================================
# 6. 🔐 보안 노트 예제
# ==============================================================================
print("\n### 6. 🔐 보안 노트 예제 ###")
# CSV Injection 시뮬레이션
# 사용자가 입력한 악의적인 문자열이 포함된 데이터 생성
malicious_input = '=SUM(1+1)*CMD|\'/C CALC\'!A1'
safe_input = 'Normal User'

# DataFrame 생성
injection_df = pd.DataFrame({
    'username': [safe_input, malicious_input],
    'value': [100, 200]
})

# CSV 파일로 저장
injection_df.to_csv('injection_example.csv', index=False)
print("--- 'injection_example.csv' 파일 생성 ---")
print("이 파일을 엑셀과 같은 스프레드시트 프로그램으로 열면")
print("악의적인 코드가 실행될 수 있다는 경고가 나타날 수 있습니다.")
print("절대 신뢰할 수 없는 CSV의 매크로나 외부 연결을 활성화하지 마세요.")

# 안전한 처리 방안: 저장 전 입력값 검증
def sanitize_for_csv(text):
    """CSV 주입 공격에 사용될 수 있는 특수문자를 제거하거나 이스케이프합니다."""
    if isinstance(text, str) and text.startswith(('=', '+', '-', '@')):
        return "'" + text  # 텍스트로 강제 인식
    return text

sanitized_df = pd.DataFrame({
    'username': [sanitize_for_csv(safe_input), sanitize_for_csv(malicious_input)],
    'value': [100, 200]
})
sanitized_df.to_csv('sanitized_example.csv', index=False)
print("\n--- 안전하게 처리된 'sanitized_example.csv' 파일 생성 ---")
# 파일 정리
import os
if os.path.exists('injection_example.csv'):
    os.remove('injection_example.csv')
if os.path.exists('sanitized_example.csv'):
    os.remove('sanitized_example.csv')


# ==============================================================================
# 7. 🧩 복합 및 심화 예제: 온라인 쇼핑 데이터 분석
# ==============================================================================
print("\n### 7. 🧩 복합 및 심화 예제 ###")
import urllib.request
import json

try:
    # 1. 데이터 준비: 웹 API로부터 JSON 데이터 로드
    endpoint = 'https://dummyjson.com/carts'
    with urllib.request.urlopen(endpoint) as response:
        result = json.loads(response.read())

    # 2. 데이터 전처리 및 DataFrame 생성
    # 중첩된 JSON 구조를 평탄화하여 DataFrame으로 변환
    rows = []
    for cart in result['carts']:
        for prod in cart['products']:
            rows.append({
                "userId": cart["userId"], 
                "total": cart["total"],
                "discountedTotal": cart["discountedTotal"],
                "product_title": prod["title"], 
                "product_price": prod["price"],
                "product_quantity": prod["quantity"]
            })
    shopping_df = pd.DataFrame(rows)
    print("--- 쇼핑 데이터 DataFrame (상위 5개) ---")
    print(shopping_df.head())

    # 3. 데이터 분석 (groupby)
    # 3.1. 사용자별 총 구매액(할인 후) 계산 및 상위 5명 추출
    user_spending = shopping_df.groupby("userId")["discountedTotal"].first().sort_values(ascending=False)
    print("\n--- 사용자별 총 구매액 (상위 5명) ---")
    print(user_spending.head())

    # 3.2. 가장 많이 팔린 상품 Top 5 (수량 기준)
    top_products = shopping_df.groupby("product_title")["product_quantity"].sum().sort_values(ascending=False)
    print("\n--- 가장 많이 팔린 상품 (상위 5개) ---")
    print(top_products.head())

    # 4. AI 연동 시뮬레이션
    # 분석 결과를 JSON으로 변환하여 AI에 요약 요청
    ai_request_data = {
        "top_spender_id": user_spending.index[0],
        "top_product_name": top_products.index[0],
        "top_product_quantity": int(top_products.iloc[0])
    }
    ai_request_payload = json.dumps(ai_request_data, indent=2)
    print("\n--- AI 요약 요청 페이로드 ---")
    print(ai_request_payload)

    # AI의 응답을 가정하고 파싱
    ai_response_summary = f"""
    {{
        "summary": "Key insights from recent sales data:",
        "top_customer_insight": "User #{ai_request_data['top_spender_id']} is the highest spender.",
        "top_product_insight": "The product '{ai_request_data['top_product_name']}' is the best-seller with {ai_request_data['top_product_quantity']} units sold."
    }}
    """
    summary_report = json.loads(ai_response_summary)
    print("\n--- AI 응답 요약 ---")
    print(summary_report['summary'])
    print(f"- {summary_report['top_customer_insight']}")
    print(f"- {summary_report['top_product_insight']}")

except Exception as e:
    print(f"\n심화 예제 실행 중 오류 발생: {e}")
    print("인터넷 연결을 확인하거나 API 엔드포인트가 유효한지 확인해주세요.")