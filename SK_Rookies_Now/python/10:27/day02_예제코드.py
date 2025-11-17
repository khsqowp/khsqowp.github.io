
import json

# --- 예제 데이터: List와 Dict를 혼합한 보안 이벤트 로그 ---
# 실제 시스템에서는 데이터베이스나 로그 파일에서 이런 형태의 데이터를 가져옵니다.
raw_security_logs = [
    {
        "event_id": "evt-20251028-001",
        "timestamp": "2025-10-28T14:00:15Z",
        "source_ip": "203.0.113.78",
        "event_type": "failed_login",
        "severity": "medium",
        "metadata": {
            "username": "admin",
            "attempt_count": 5
        }
    },
    {
        "event_id": "evt-20251028-002",
        "timestamp": "2025-10-28T14:05:22Z",
        "source_ip": "198.51.100.22",
        "event_type": "sql_injection_attempt",
        "severity": "high",
        "metadata": {
            "request_path": "/login",
            "payload": "' or 1=1--"
        }
    },
    {
        "event_id": "evt-20251028-003",
        "timestamp": "2025-10-28T14:06:01Z",
        "source_ip": "203.0.113.78",
        "event_type": "firewall_block",
        "severity": "low",
        "metadata": {
            "rule_id": "FW-RULE-099"
        }
    }
]

# --- 1. 제어문(if, for)과 함수(def)를 활용한 기본 로그 분석 ---

def analyze_raw_logs(logs):
    """
    List와 Dict로 구성된 로그를 받아, 제어문을 활용해 기본적인 분석을 수행하는 함수
    """
    print("--- 1. 기본 로그 분석 시작 ---")
    
    high_severity_alerts = []
    ip_activity = {}

    # for 반복문: 리스트에 있는 모든 로그(dict)를 하나씩 순회
    for log in logs:
        ip = log["source_ip"]
        
        # if-elif-else 제어문: 로그의 'severity' 값에 따라 다른 동작 수행
        if log["severity"] == "high":
            print(f"[위험] 심각도 '높음' 이벤트 탐지! IP: {ip}")
            high_severity_alerts.append(log)
        elif log["severity"] == "medium":
            print(f"[주의] 심각도 '중간' 이벤트 탐지. IP: {ip}")
        else:
            print(f"[정보] 심각도 '낮음' 이벤트 탐지. IP: {ip}")

        # IP별 활동 횟수 집계
        if ip in ip_activity:
            ip_activity[ip] += 1
        else:
            ip_activity[ip] = 1
            
    print("\n--- 분석 결과 ---")
    print(f"심각도 '높음' 이벤트 수: {len(high_severity_alerts)}건")
    print(f"IP별 활동 빈도: {ip_activity}")
    print("--- 1. 기본 로그 분석 종료 ---\n")
    
    return high_severity_alerts


# --- 2. JSON을 활용한 AI 분석 시뮬레이션 ---

def get_ai_analysis_from_logs(high_severity_logs):
    """
    분석이 필요한 로그를 받아 AI에게 JSON으로 보내고,
    규격화된 JSON 응답을 돌려받는 과정을 시뮬레이션하는 함수
    """
    print("--- 2. AI 분석 시뮬레이션 시작 ---")

    # AI에게 보낼 요청 데이터 생성 (Python dict)
    request_data = {
        "model_version": "threat-detector-v1.2",
        "logs_to_analyze": high_severity_logs
    }

    # json.dumps(): Python dict를 JSON 형식의 문자열로 변환 (AI 서버로 전송하는 데이터)
    request_json = json.dumps(request_data, indent=4)
    print("[클라이언트 -> AI 서버] AI 분석 요청 JSON 데이터:")
    print(request_json)
    print("-" * 20)

    # --- AI 호출 시뮬레이션 ---
    # 실제로는 이 부분에서 네트워크를 통해 AI API를 호출합니다.
    # 여기서는 AI가 분석 후 돌려줬다고 가정한 '규격화된 JSON 응답'을 직접 생성합니다.
    
    simulated_ai_response_dict = {
        "request_id": "req-a1b2c3d4",
        "analysis_summary": {
            "overall_risk_score": 8.5,
            "threat_pattern_identified": "Coordinated Attack (SQLi from 198.51.100.22)",
            "confidence": 0.92
        },
        "detailed_results": [
            {
                "event_id": "evt-20251028-002",
                "source_ip": "198.51.100.22",
                "threat_type": "SQL Injection",
                "recommended_actions": [
                    "Block IP: 198.51.100.22 at firewall",
                    "Patch web application vulnerability (WAF-Rule-SQLi-001)",
                    "Force user password reset for related accounts"
                ]
            }
        ]
    }
    
    # json.loads(): AI 서버로부터 받은 JSON 문자열을 Python dict로 다시 변환
    # 여기서는 시뮬레이션이므로 dict를 바로 사용합니다.
    print("[AI 서버 -> 클라이언트] AI 분석 완료 JSON 응답:")
    print(json.dumps(simulated_ai_response_dict, indent=4, ensure_ascii=False))
    print("--- 2. AI 분석 시뮬레이션 종료 ---\n")
    
    return simulated_ai_response_dict

def process_ai_verdict(ai_result):
    """
    AI의 분석 결과(dict)를 받아 후속 조치를 처리하는 함수
    """
    print("--- 3. AI 분석 결과 기반 후속 조치 시작 ---")
    
    summary = ai_result["analysis_summary"]
    
    # if 제어문: AI가 판단한 위험도 점수에 따라 대응 수준 결정
    if summary["overall_risk_score"] > 7.0:
        print(f"!! 긴급 대응 필요 !! 전체 위험도: {summary['overall_risk_score']}")
        print(f"탐지된 위협 패턴: {summary['threat_pattern_identified']}")
        
        # for 반복문: AI가 추천한 조치 사항들을 하나씩 출력
        for result in ai_result["detailed_results"]:
            print(f"\n이벤트(ID: {result['event_id']})에 대한 조치 권고:")
            for action in result["recommended_actions"]:
                print(f"  - [조치 실행] {action}")
    else:
        print("탐지된 특이사항 없음. 모니터링 유지.")
        
    print("--- 3. AI 분석 결과 기반 후속 조치 종료 ---")


# --- 메인 실행 로직 ---
if __name__ == "__main__":
    # 1단계: 기본 분석 수행 및 심각도 '높음' 이벤트 추출
    critical_logs = analyze_raw_logs(raw_security_logs)
    
    # 2단계: '높음' 이벤트만 AI에게 보내 분석 요청 (시뮬레이션)
    if critical_logs: # 처리할 로그가 있을 경우에만 실행
        ai_analysis_result = get_ai_analysis_from_logs(critical_logs)
        
        # 3단계: AI의 분석 결과를 바탕으로 후속 조치 수행
        process_ai_verdict(ai_analysis_result)
    else:
        print("AI 분석으로 넘길 심각한 이벤트가 없습니다.")
