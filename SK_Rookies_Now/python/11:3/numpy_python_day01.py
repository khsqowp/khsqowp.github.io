# numpy_python_day01.py
# NumPy 강의 1일차 예제 코드

import numpy as np

# ==============================================================================
# 1. NumPy 배열 생성 및 기본 정보 확인
# ==============================================================================
print("### 1. NumPy 배열 생성 및 기본 정보 확인 ###")

# 파이썬 리스트
lst = [1, 2, 3, 4, 5]
print(f"파이썬 리스트: {lst}, 타입: {type(lst)}")

# 리스트를 NumPy 배열로 변환
arr = np.array(lst)
print(f"NumPy 배열: {arr}, 타입: {type(arr)}")

# 배열 정보 확인을 위한 함수
def array_info(array):
    """NumPy 배열의 주요 정보(데이터, shape, 차원, dtype)를 출력하는 함수"""
    if not isinstance(array, np.ndarray):
        print("입력값은 NumPy 배열이 아닙니다.")
        return
    print(f"데이터: {array}")
    print(f"Shape (형태): {array.shape}")
    print(f"Dimension (차원): {array.ndim}")
    print(f"Data Type (자료형): {array.dtype}")
    print("-" * 20)

print("\n--- 배열 정보 확인 ---")
array_info(arr)

# ==============================================================================
# 2. 벡터화 연산 (Vectorization)
# ==============================================================================
print("\n### 2. 벡터화 연산 (Vectorization) ###")

# 파이썬 리스트로 각 요소 제곱하기 (반복문 필요)
result_list = []
for element in lst:
    result_list.append(element ** 2)
print(f"리스트 연산 (반복문): {result_list}")

# 리스트에 벡터화 연산 시도 -> TypeError 발생
try:
    lst ** 2
except TypeError as e:
    print(f"리스트에 직접 연산 시도 시 에러: {e}")

# NumPy 배열로 각 요소 제곱하기 (벡터화 연산)
result_arr = arr ** 2
print(f"NumPy 배열 연산 (벡터화): {result_arr}")

# 배열 간의 연산
x_arr = np.array([1, 2, 3])
y_arr = np.array([4, 5, 6])
print(f"배열 덧셈: {x_arr} + {y_arr} = {x_arr + y_arr}")

# ==============================================================================
# 3. 불리언 마스킹 (Boolean Masking)
# ==============================================================================
print("\n### 3. 불리언 마스킹 (Boolean Masking) ###")

# 조건에 맞는 요소 찾기 -> 불리언 배열 반환
bool_mask = arr > 3
print(f"arr > 3 의 결과 (불리언 마스크): {bool_mask}")

# 불리언 마스크를 사용해 값 필터링
print(f"arr[arr > 3] 의 결과 (필터링된 값): {arr[bool_mask]}")

# 복합 조건
# 예: arr에서 2와 같거나 4보다 큰 요소 찾기
complex_mask = (arr == 2) | (arr > 4)
print(f"(arr == 2) | (arr > 4) 의 결과: {arr[complex_mask]}")


# ==============================================================================
# 4. 2차원 배열 (행렬)
# ==============================================================================
print("\n### 4. 2차원 배열 (행렬) ###")

# 리스트의 리스트로 2차원 배열 생성
list_of_list = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(list_of_list)

print("--- 2차원 배열 정보 ---")
array_info(arr_2d)

# 인덱싱: 1행 2열의 값 (6) 접근
print(f"arr_2d[1, 2]: {arr_2d[1, 2]}")
print(f"arr_2d[1][2]: {arr_2d[1][2]}")

# ==============================================================================
# 5. 배열 생성 함수 (arange, reshape)
# ==============================================================================
print("\n### 5. 배열 생성 함수 (arange, reshape) ###")

# 0부터 11까지의 값을 갖는 1차원 배열 생성
arr_range = np.arange(12)
print(f"np.arange(12): {arr_range}")

# 1차원 배열을 3행 4열의 2차원 배열로 변형
arr_reshaped = arr_range.reshape(3, 4)
print("--- reshape(3, 4) 후 ---")
array_info(arr_reshaped)

# -1을 사용하여 차원 자동 계산
# 1부터 20까지의 배열을 4행 ?열로 변경
arr_auto_reshape = np.arange(1, 21).reshape(4, -1)
print("--- reshape(4, -1) 후 ---")
array_info(arr_auto_reshape)


# ==============================================================================
# 6. 팬시 인덱싱 (Fancy Indexing)
# ==============================================================================
print("\n### 6. 팬시 인덱싱 (Fancy Indexing) ###")

# 1차원 배열에서 짝수만 출력하기
arr_fancy = np.arange(10)
print(f"원본 배열: {arr_fancy}")

# 방법 1: 불리언 인덱싱
even_mask = arr_fancy % 2 == 0
print(f"짝수만 출력 (불리언): {arr_fancy[even_mask]}")

# 방법 2: 정수 인덱싱 (짝수 인덱스만)
even_indices = [0, 2, 4, 6, 8]
print(f"짝수 인덱스 값 출력 (정수): {arr_fancy[even_indices]}")

# 2차원 배열에서 팬시 인덱싱
arr_2d_fancy = np.arange(1, 13).reshape(3, 4)
print("\n--- 2차원 배열 팬시 인덱싱 ---")
print("원본 2차원 배열:")
print(arr_2d_fancy)

# 모든 행에 대해 0번째, 3번째 열 가져오기
print("모든 행의 0, 3열:")
print(arr_2d_fancy[:, [0, 3]])

# 0번째, 2번째 행을 선택하고, 그 안에서 1번째, 3번째 열 선택
print("0, 2행 & 1, 3열:")
print(arr_2d_fancy[[0, 2]][:, [1, 3]])


# ==============================================================================
# 7. 통계 함수
# ==============================================================================
print("\n### 7. 통계 함수 ###")
stats_arr = np.arange(1, 17).reshape(4, 4)
print("원본 배열:")
print(stats_arr)

print(f"전체 합 (sum): {np.sum(stats_arr)}")
print(f"전체 평균 (mean): {np.mean(stats_arr)}")
print(f"전체 최댓값 (max): {np.max(stats_arr)}")

# axis 사용: 0=열 기준, 1=행 기준
print(f"열 기준 합 (axis=0): {np.sum(stats_arr, axis=0)}")
print(f"행 기준 합 (axis=1): {np.sum(stats_arr, axis=1)}")

# argmin, argmax: 최소/최대값의 '인덱스' 반환
print(f"전체에서 최솟값의 인덱스 (flatten 기준): {np.argmin(stats_arr)}")
print(f"전체에서 최댓값의 인덱스 (flatten 기준): {np.argmax(stats_arr)}")

# ==============================================================================
# 8. 배열 정렬 (sort, argsort)
# ==============================================================================
print("\n### 8. 배열 정렬 (sort, argsort) ###")

# 정렬을 위한 랜덤 배열 생성
np.random.seed(42) # 결과를 동일하게 보기 위해 시드 고정
sort_arr = np.random.randint(1, 100, 10)
print(f"원본 랜덤 배열: {sort_arr}")

# np.sort(): 원본을 바꾸지 않고 정렬된 '새로운' 배열 반환
sorted_copy = np.sort(sort_arr)
print(f"np.sort() 후 반환된 배열: {sorted_copy}")
print(f"np.sort() 후 원본 배열: {sort_arr} (변경 없음)")

# 내림차순 정렬
print(f"내림차순 정렬: {np.sort(sort_arr)[::-1]}")

# array.sort(): 원본 배열을 '직접' 정렬 (in-place)
sort_arr.sort()
print(f"array.sort() 후 원본 배열: {sort_arr} (변경됨)")

# argsort: 정렬 후의 인덱스를 반환
argsort_arr = np.array([40, 30, 50, 10])
sorted_indices = np.argsort(argsort_arr)
print(f"\nargsort 원본 배열: {argsort_arr}")
print(f"정렬된 인덱스 (argsort): {sorted_indices}")
print(f"argsort 인덱스를 사용한 정렬: {argsort_arr[sorted_indices]}")


# ==============================================================================
# 9. 🔐 보안 노트 예제
# ==============================================================================
print("\n### 9. 🔐 보안 노트 예제 ###")
import os

# 악의적인 pickle 데이터를 포함할 수 있는 npy 파일 시뮬레이션
# 실제 악성코드를 생성하지는 않음
class Malicious:
    def __reduce__(self):
        # 이 예제는 시스템 명령을 실행하지 않지만,
        # 실제 악성 pickle은 'os.system("echo 해킹됨")'과 같은 코드를 포함할 수 있음
        return (print, ("악성 코드가 실행될 수 있습니다!",))

malicious_data = np.array([Malicious()], dtype=object)

# 위험한 파일 저장 (allow_pickle=True)
try:
    np.save("malicious.npy", malicious_data)
except Exception as e:
    print(f"np.save 에러: {e}")


# 안전하지 않은 로드 (allow_pickle=True)
print("--- 안전하지 않은 로드 (allow_pickle=True) ---")
try:
    # 이 코드는 잠재적으로 위험함
    loaded_data = np.load("malicious.npy", allow_pickle=True)
    print("파일 로드 성공 (위험).")
except ValueError as e:
    print(f"np.load 에러: {e}")


# 안전한 로드 (allow_pickle=False)
print("\n--- 안전한 로드 (allow_pickle=False) ---")
try:
    loaded_data_safe = np.load("malicious.npy", allow_pickle=False)
except ValueError as e:
    print(f"np.load 에러 (안전): {e}")
finally:
    # 생성된 파일 정리
    if os.path.exists("malicious.npy"):
        os.remove("malicious.npy")


# ==============================================================================
# 10. 🧩 복합 및 심화 예제
# ==============================================================================
print("\n### 10. 🧩 복합 및 심화 예제 ###")
import json

# 1. 데이터 준비: 서버 로그 데이터 시뮬레이션 (NumPy 배열 사용)
# 각 행: [timestamp, status_code, response_time_ms, severity]
# severity: 0=INFO, 1=WARN, 2=ERROR, 3=CRITICAL
log_data = np.array([
    [1672531201, 200, 150, 0],
    [1672531202, 503, 2500, 3],
    [1672531203, 200, 200, 0],
    [1672531204, 404, 50, 1],
    [1672531205, 500, 1800, 2],
    [1672531206, 200, 120, 0],
    [1672531207, 503, 3000, 3],
])
print("--- 원본 로그 데이터 (NumPy 배열) ---")
print(log_data)

# 2. 데이터 분석 함수: 심각도 'CRITICAL'(3)인 로그 필터링 및 분석
def analyze_critical_logs(logs):
    # 불리언 마스킹으로 심각도가 3인 로그만 추출
    critical_mask = logs[:, 3] == 3
    critical_logs = logs[critical_mask]

    if critical_logs.shape[0] > 0:
        # 평균 응답 시간 계산
        avg_response_time = np.mean(critical_logs[:, 2])
        # 발생 횟수
        count = critical_logs.shape[0]
        
        analysis = {
            "level": "CRITICAL",
            "count": count,
            "avg_response_time_ms": round(avg_response_time, 2), # JSON 직렬화를 위해 list로 변환
            "timestamps": critical_logs[:, 0].tolist() 
        }
        return analysis
    else:
        return {"level": "CRITICAL", "count": 0}

critical_analysis = analyze_critical_logs(log_data)
print("\n--- 심각도 'CRITICAL' 분석 결과 ---")
print(critical_analysis)


# 3. AI 연동 시뮬레이션
# 3.1. 분석된 데이터를 JSON으로 변환하여 AI에 요청
ai_request_payload = json.dumps(critical_analysis, indent=2)
print("\n--- AI 요청 페이로드 (JSON) ---")
print(ai_request_payload)

# 3.2. AI가 분석 결과를 JSON으로 응답했다고 가정
ai_response_json = '''
{
  "incident_id": "INC-2023-11-04-001",
  "summary": "Multiple service unavailable (503) errors detected with high response times.",
  "risk_level": "High",
  "recommended_actions": [
    "1. Check health of upstream service 'auth-service'.",
    "2. Scale up 'web-api' deployment.",
    "3. Notify on-call engineer."
  ],
  "related_metrics": {
    "cpu_usage_peak": "95%",
    "memory_usage_peak": "88%"
  }
}
'''
print("\n--- AI 응답 (JSON) ---")
print(ai_response_json)

# 3.3. AI의 JSON 응답을 파싱하여 후속 처리
incident_report = json.loads(ai_response_json)
print("\n--- 파싱된 AI 응답에서 후속 조치 실행 ---")
print(f"위험도: {incident_report['risk_level']}")
print("추천 조치:")
for action in incident_report['recommended_actions']:
    print(f"- {action}")