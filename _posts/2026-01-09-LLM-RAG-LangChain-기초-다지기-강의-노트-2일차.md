---
title: "LLM RAG LangChain 기초 다지기 강의 노트 2일차"
date: 2026-01-09
categories:
  - Python
tags:
  - Python
  - SK_Rookies
---

# 📝 LLM, RAG, LangChain 기초 다지기 강의 노트 (2일차)

**강의 날짜**: 2025년 11월 11일  
**주제**: LLM, RAG, LangChain 개념 복습 및 실전 애플리케이션 구축  
**학습 목표**: 기존 내용을 다시 학습하면서 LLM, RAG, Langchain 기초를 탄탄히 다지고, 실제 보안 로그 분석 대시보드 구축하기

---

## 📚 학습 내용 복습

### 🔄 지난 강의 연결

지난 시간에 우리는 LLM과 RAG의 기본 개념을 학습했습니다. 오늘 강의는 그 개념들을 더욱 탄탄히 다지고, 실제 애플리케이션으로 구현하는 방법을 배웠습니다. 강사님께서는 "작은 것의 소중함"을 강조하시며, 하루에 한 시간씩이라도 이해하는 것에 감사함을 느끼며 꾸준히 학습하는 것이 중요하다고 말씀하셨습니다.

*💡 중요!: 개발과 코딩은 한 번에 완성되는 것이 아닙니다. 에러를 만나고 해결하는 과정 자체가 학습이며, 이를 통해 우리는 성장합니다. "긍정의 마인드"를 가지고 끊임없이 지속적인 관심과 노력을 기울이는 것이 핵심입니다.*

---

## 🎯 핵심 개념 정리

### 1. LLM (Large Language Model) - 대형 언어 모델

#### 💭 LLM이란 무엇인가?

오늘 강의에서 강사님께서는 LLM을 여러 관점에서 설명해 주셨습니다:

**기본 정의**:
- **문장을 이해하고 답변할 수 있는 인공지능 모델(알고리즘)**
- 방대한 데이터를 학습하여 인간과 대화할 수 있는 능력을 갖춘 모델
- 내부적으로는 알고리즘으로 구현된 "로봇"

**비유적 설명**:
- 똑똑한 친구처럼 질문에 답변해주는 존재
- 입력(input)을 받아 학습된 패턴에 따라 문장을 반환(output)하는 시스템
- 확률 계산을 통해 가장 적절한 응답을 생성하는 모델

*📌 노트: LLM은 단순히 암기된 내용을 반복하는 것이 아니라, 패턴을 학습하여 새로운 문맥에서도 적절한 응답을 생성할 수 있습니다. 이는 앵무새가 같은 말을 반복하는 것과는 근본적으로 다릅니다.*

#### 🔍 LLM의 동작 원리

LLM이 작동하기 위해서는 다음 요소들이 필요합니다:

1. **방대한 데이터**: 인공지능이 학습할 수 있는 대규모 데이터셋
2. **패턴 학습**: 데이터에서 패턴을 추출하고 학습하는 과정
3. **임베딩**: 텍스트를 숫자 배열(벡터)로 변환하는 과정
4. **확률적 결정**: 학습된 패턴을 바탕으로 다음 단어를 확률적으로 예측

*💡 중요!: AI 사회가 도래하기 위해서는 수십 년 전부터 데이터 수집과 전처리가 필요했습니다. 현재 데이터 관련 회사들이 큰 성공을 거두고 있는 이유도 바로 이러한 선견지명 때문입니다.*

#### 🤖 LLM의 한계와 보완

**LLM의 한계**:
- 파인튜닝(Fine-tuning)이 되지 않으면 최신 정보를 모를 수 있음
- 학습 데이터의 시점에 따라 정보가 오래될 수 있음 (할루시네이션 발생 가능)
- 특정 도메인에 대한 전문 지식이 부족할 수 있음

**보완 방법**:
- 지속적인 파인튜닝: 새로운 데이터를 계속 학습시켜 점점 똑똑하게 만들기
- RAG 활용: 외부 문서나 데이터베이스와 연결하여 정확한 정보 제공

---

### 2. RAG (Retrieval Augmented Generation) - 검색 증강 생성

#### 🏛️ RAG란 무엇인가?

**기본 정의**:
- LLM이 대답하기 전에 관련 문서를 찾아서 참고할 수 있도록 도와주는 비서
- 사용자 질문에 대한 관련 문서를 검색(Retrieval)하여 그 내용을 바탕으로 답변을 생성(Generation)하는 방식

**비유적 설명**:
- 도서관과 같은 역할
- LLM이 답변하기 전에 참고할 수 있는 외부 지식 저장소
- 똑똑한 친구(LLM)가 공부할 수 있는 도서관

*📌 노트: RAG는 반드시 외부 오픈 API를 통해서만 구현되는 것이 아닙니다. 회사 내부의 데이터베이스나 사내 CRM을 RAG로 활용할 수도 있습니다. 이를 통해 기업 특화 AI 서비스 구축이 가능합니다.*

#### 🔗 RAG의 활용 시나리오

**실무 활용 예시**:

1. **사내 문서 검색 시스템**:
   - 회사의 내부 규정, 매뉴얼, 기술 문서를 RAG로 연동
   - 직원들이 질문하면 관련 문서를 찾아 정확한 답변 제공

2. **고객 지원 챗봇**:
   - 제품 매뉴얼, FAQ, 과거 상담 이력을 RAG로 구성
   - 고객 질문에 대해 정확한 답변 제공

3. **법률/의료 자문 시스템**:
   - 판례, 의학 논문 등 전문 문서를 RAG로 활용
   - 전문가 수준의 조언 제공

#### 💾 RAG의 구성 요소

**외부 문서 데이터베이스**:
```python
doc = [
    '리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.',
    '튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다.',
    '딕셔너리는 키(key)와 값(value)의 쌍으로 데이터를 저장합니다.'
]
```

위 코드는 간단한 텍스트 문서를 리스트로 정의한 것입니다. 실제 환경에서는 이 데이터가 데이터베이스, 파일 시스템, 또는 웹 API에서 가져올 수 있습니다.

---

### 3. LangChain - AI 연결 조립 키트

#### 🔧 LangChain이란?

**기본 정의**:
- LLM + RAG를 연결하는 프레임워크
- 다양한 데이터 소스와 LLM을 연결하여 더 나은 결과를 도출하도록 돕는 도구
- AI 연결 조립 키트

**핵심 역할**:
- LLM과 RAG(도서관)를 연결해주는 다리 역할
- 검색, 데이터베이스, 외부 API 등을 체인처럼 연결하여 자동화 프로그램 생성

*💡 중요!: LangChain을 반드시 사용해야 하는 것은 아닙니다. LLM만으로도 대화형 챗봇을 충분히 만들 수 있습니다. 하지만 LangChain을 사용하면 문서 기반의 정확한 정보를 제공하는 시스템을 더 쉽게 구축할 수 있습니다.*

#### 🔄 LangChain의 동작 흐름

**전체 시나리오**:

1. **사용자 질문**: "파이썬에서 리스트와 튜플의 차이점을 알려줘"
2. **RAG 검색**: LangChain이 관련 문서를 데이터베이스에서 검색
3. **문서 참조**: 검색된 문서를 LLM에게 제공
4. **답변 생성**: LLM이 문서를 참고하여 정확한 답변 생성
5. **응답 반환**: 사용자에게 정확한 정보가 담긴 답변 전달

```
[사용자 질문] → [LangChain] → [RAG 검색] → [문서 발견] 
                                                    ↓
[사용자 응답] ← [LLM 답변] ← [문서 참조] ← [LLM에게 전달]
```

*📌 노트: 이러한 구조를 통해 LLM이 학습하지 못한 최신 정보나 특정 도메인 지식도 정확하게 답변할 수 있게 됩니다. 이것이 바로 "사실에 근거한 정보 전달"의 핵심입니다.*

---

## 🛠️ 환경 설정 및 준비

### 📦 가상환경 실행

오늘 강의에서는 주피터 노트북을 사용하여 실습을 진행했습니다. 가상환경을 활성화하는 방법은 다음과 같습니다:

**Windows 아나콘다 프롬프트에서 실행**:

```bash
# 1단계: 가상환경 목록 확인
conda env list

# 2단계: 가상환경 활성화
conda activate security_env

# 3단계: 주피터 노트북 실행
jupyter notebook
```

*💡 중요!: 명령어에 익숙해지는 것이 중요합니다. 매번 실행하면서 손에 익히도록 합니다. 가상환경을 사용하는 이유는 프로젝트별로 독립적인 패키지 환경을 유지하기 위함입니다.*

---

## 🔐 보안: API 키 관리 및 마스킹 처리

### ⚠️ 왜 API 키를 마스킹해야 하는가?

강의 중 강사님께서는 전날 실수로 API 키를 그대로 출력하여 영상에 노출된 사건을 언급하셨습니다. 보안 과정에서 이는 절대 해서는 안 되는 실수입니다.

**API 키 노출의 위험성**:
- 타인이 API 키를 도용하여 무단으로 서비스 사용 가능
- 예상치 못한 요금 청구 발생
- 서비스 계정 해킹 및 데이터 유출 위험
- 기업의 경우 법적 책임 문제 발생 가능

### 🔒 API 키 안전하게 관리하기

#### 1. 환경 변수 사용 (.env 파일)

**`.env` 파일 생성**:
```plaintext
OPENAI_API_KEY=sk-proj-abcd1234efgh5678...
```

**`.env` 파일 로드 및 사용**:
```python
import os
from dotenv import load_dotenv

# .env 파일에서 API 키를 로드
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
```

#### 💻 코드 실행 상세 분석

**1단계 (모듈 임포트)**: `os` 모듈과 `dotenv` 모듈을 임포트하여 환경 변수 관리 준비를 합니다.

**2단계 (환경 변수 로드)**: `load_dotenv()` 함수가 호출되면서 현재 디렉토리에 있는 `.env` 파일을 읽어 환경 변수로 등록합니다.

**3단계 (API 키 추출)**: `os.getenv('OPENAI_API_KEY')` 함수를 통해 환경 변수에서 API 키 값을 가져와 `api_key` 변수에 저장합니다.

**최종 결과**: API 키가 코드에 직접 노출되지 않고 안전하게 관리됩니다. `.env` 파일은 `.gitignore`에 추가하여 버전 관리 시스템에 포함되지 않도록 해야 합니다.

*🔐 보안 노트: `.env` 파일은 절대로 GitHub 등 공개 저장소에 업로드하지 마세요. `.gitignore` 파일에 `.env`를 추가하여 실수로 커밋되는 것을 방지해야 합니다.*

---

#### 2. API 키 마스킹 함수 구현

```python
def masking(key):
    """
    API 키를 마스킹 처리하는 함수
    앞 4자리와 뒤 4자리만 표시하고 나머지는 * 처리
    """
    # 키가 8자리 이하인 경우 전체를 *로 처리
    if len(key) <= 8:
        return '*' * len(key)
    
    # 앞 4자리 + 중간 * + 뒤 4자리
    return key[:4] + "*" * (len(key) - 8) + key[-4:]

# 사용 예시
if api_key:
    masked_api_key = masking(api_key)
    print(f"Masked API Key: {masked_api_key}")
else:
    print("API key not found. Please check your .env file.")
```

#### 💻 코드 실행 상세 분석

**1단계 (함수 정의)**: `masking` 함수가 정의됩니다. 이 함수는 문자열 형태의 키를 인자로 받습니다.

**2단계 (키 길이 검사)**: `if len(key) <= 8` 조건문에서 키의 길이가 8자 이하인지 확인합니다. 만약 8자 이하라면, 전체를 `*`로 처리하여 반환합니다. 이는 너무 짧은 키의 경우 일부만 마스킹하면 원본을 추측할 수 있기 때문입니다.

**3단계 (부분 마스킹 처리)**: 
- `key[:4]`: 문자열의 처음 4자리를 추출합니다.
- `"*" * (len(key) - 8)`: 키의 전체 길이에서 8을 뺀 만큼의 `*`를 생성합니다. (앞 4자리 + 뒤 4자리 = 8자리를 제외한 나머지)
- `key[-4:]`: 문자열의 마지막 4자리를 추출합니다.
- 이 세 부분을 합쳐서 반환합니다.

**4단계 (조건부 실행)**: `if api_key:` 조건문에서 API 키가 성공적으로 로드되었는지 확인합니다.

**5단계 (마스킹 적용)**: API 키가 존재하면 `masking()` 함수를 호출하여 마스킹된 키를 생성합니다.

**6단계 (결과 출력)**: 마스킹된 API 키를 출력합니다. API 키가 없다면 오류 메시지를 출력합니다.

**최종 결과**: 예를 들어 `sk-proj-1234567890abcdefghij`라는 키가 있다면, `sk-p**************ghij`와 같이 마스킹되어 출력됩니다.

*🔐 보안 노트: 마스킹은 출력 시 보안을 위한 것이며, 실제 API 호출 시에는 원본 키를 사용해야 합니다. 또한, 로그 파일에도 마스킹된 키만 기록되도록 주의해야 합니다.*

---

## 🤖 OpenAI API를 활용한 LLM 기본 사용

### 📡 OpenAI API 클라이언트 초기화

```python
import openai
from openai import OpenAI

# OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)
```

#### 💻 코드 실행 상세 분석

**1단계 (모듈 임포트)**: `openai` 라이브러리와 `OpenAI` 클래스를 임포트합니다.

**2단계 (클라이언트 초기화)**: `OpenAI()` 생성자에 API 키를 전달하여 클라이언트 객체를 생성합니다. 이 객체를 통해 OpenAI의 다양한 서비스에 접근할 수 있습니다.

**최종 결과**: `client` 객체를 통해 GPT 모델에 요청을 보낼 준비가 완료됩니다.

---

### 💬 기본 대화형 프롬프트 구현

#### 🎭 Role 기반 메시지 구조

OpenAI의 채팅 API는 세 가지 역할(role)로 메시지를 구분합니다:

1. **system**: AI의 행동과 성격을 정의하는 시스템 메시지
2. **user**: 사용자가 입력한 질문이나 요청
3. **assistant**: AI가 생성한 응답 (대화 이력 유지 시 사용)

```python
# 사용자 입력 받기
prompt = input('검색하고자 하는 내용을 입력하세요 : ')
print('prompt - ', prompt)

# 시스템 역할 정의 (AI의 성격과 행동 지침)
system_content = '''
당신은 친절한 파이썬 보안 도우미입니다.
사용자의 요청에 대해 항상 보안 모범 사례를 우선으로 설명하고,
민감 정보 노출을 방지하는 방법, 최소 권한 원칙, 패키지/채널 검증, 파일 권한 설정,
취약점 완화 방법을 구체적 명령어와 체크리스트 형태로 제공하십시오.
응답에 실제 비밀번호나 실사용 API 키를 절대 포함하지 마십시오.
'''

# 사용자 역할 메시지 (구체적인 질문)
user_content = f'''
1) 패키지 설치시 보안 지침
2) 모니터링 권장 설정 방법
3) 민감정보 관리 방법과 예시
4) 가상환경 구축 권장 방법
{prompt}
'''
```

#### 💻 코드 실행 상세 분석

**1단계 (사용자 입력)**: `input()` 함수로 사용자로부터 검색 내용을 입력받습니다. 예를 들어 "코드보안"이라고 입력했다면 `prompt` 변수에 저장됩니다.

**2단계 (시스템 메시지 정의)**: `system_content` 변수에 AI의 역할과 행동 지침을 정의합니다. 이 메시지는 AI가 어떤 페르소나로 답변할지를 결정합니다. 여기서는 "보안 도우미"로 설정되어, 모든 답변이 보안 관점에서 제공됩니다.

**3단계 (사용자 메시지 구성)**: `user_content` 변수에 구체적인 질문을 f-string으로 구성합니다. 사용자가 입력한 `prompt`를 포함하여 총 4가지 질문을 포함합니다.

**최종 결과**: 이제 시스템 메시지와 사용자 메시지가 준비되어 API 호출에 사용될 수 있습니다.

*📌 노트: 시스템 메시지는 AI의 "성격"을 정의합니다. 여기서 보안 중심의 답변을 요구했기 때문에, AI는 모든 답변에서 보안 모범 사례를 우선으로 설명하게 됩니다.*

---

### 🚀 API 호출 및 응답 받기

```python
# OpenAI API 호출
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        # role : system, user, assistant
        # content : content
        {'role': 'system', 'content': system_content},
        {'role': 'user', 'content': user_content}
    ],
    
    # 응답 문장의 길이 제한
    max_tokens=1024,
    
    # 출력 다양성(무작위성) : 0 ~ 1 (낮을수록 보수적)
    temperature=0.7
)

# 응답 출력
print('response - ', response)
print('content - ', response.choices[0].message.content)
```

#### 💻 코드 실행 상세 분석

**1단계 (API 요청 생성)**: `client.chat.completions.create()` 메서드가 호출됩니다. 이는 OpenAI의 채팅 완성 API에 요청을 보내는 함수입니다.

**2단계 (모델 선택)**: `model='gpt-4o-mini'` 파라미터로 사용할 AI 모델을 지정합니다. GPT-4o-mini는 속도와 비용 측면에서 유리한 경량 모델입니다.

**3단계 (메시지 배열 구성)**: `messages` 파라미터에 시스템 메시지와 사용자 메시지를 리스트 형태로 전달합니다. 각 메시지는 `role`과 `content` 키를 가진 딕셔너리입니다.

**4단계 (토큰 제한 설정)**: `max_tokens=1024` 파라미터로 응답의 최대 길이를 제한합니다. 1024 토큰은 대략 768~1024 단어 정도에 해당합니다.

**5단계 (temperature 설정)**: `temperature=0.7` 파라미터로 응답의 창의성을 조절합니다. 0에 가까울수록 보수적이고 일관된 답변, 1에 가까울수록 창의적이고 다양한 답변을 생성합니다.

**6단계 (API 호출 실행)**: 모든 파라미터가 설정되면 실제로 OpenAI 서버에 HTTP 요청을 보냅니다.

**7단계 (응답 수신)**: 서버로부터 응답을 받아 `response` 변수에 저장합니다. 이 응답은 복잡한 JSON 구조의 객체입니다.

**8단계 (응답 파싱)**: 
- `response.choices`: 여러 응답 후보 중 선택할 수 있는 리스트 (보통 1개)
- `response.choices[0]`: 첫 번째 응답 선택
- `.message.content`: 실제 응답 텍스트 추출

**최종 결과**: AI가 생성한 답변이 문자열 형태로 출력됩니다. 예를 들어 "코드보안"에 대한 질문이라면, 패키지 설치 보안 지침, 모니터링 설정 방법, 민감정보 관리 등에 대한 상세한 답변이 출력됩니다.

*💡 중요!: `max_tokens`를 너무 낮게 설정하면 답변이 중간에 잘릴 수 있습니다. 충분한 길이를 보장하려면 1024~2048 정도의 값을 사용하는 것이 좋습니다.*

---

### 🎛️ 주요 파라미터 설명

#### 1. model (모델 선택)

OpenAI는 다양한 모델을 제공합니다:

- **gpt-3.5-turbo**: 채팅용 최적화된 가성비 모델
- **gpt-4o**: 텍스트와 이미지/비전 지원을 도와주는 멀티모달 모델
- **gpt-4o-mini**: 속도/비용 측면에서 유리한 경량 모델 (오늘 강의에서 주로 사용)

*📌 노트: 실무에서는 비용과 성능을 고려하여 모델을 선택해야 합니다. 간단한 질의응답은 mini 모델로도 충분하지만, 복잡한 추론이 필요한 경우 gpt-4o를 사용하는 것이 좋습니다.*

#### 2. max_tokens (응답 길이 제한)

- 생성되는 응답의 최대 토큰 수를 제한
- 1 토큰 ≈ 0.75 단어 (영어 기준)
- 한국어의 경우 토큰 수가 더 많이 소요됨
- 비용 절감과 응답 속도 향상에 중요

#### 3. temperature (창의성 조절)

- 범위: 0.0 ~ 1.0
- **0.0 ~ 0.3**: 매우 보수적, 일관된 답변 (사실 확인, 코드 생성에 적합)
- **0.4 ~ 0.7**: 균형잡힌 답변 (일반적인 대화에 적합)
- **0.8 ~ 1.0**: 매우 창의적, 다양한 답변 (창작, 브레인스토밍에 적합)

*💡 중요!: 보안 관련 답변처럼 정확성이 중요한 경우 temperature를 0.3 이하로 설정하는 것이 좋습니다. 반면 창의적인 아이디어가 필요한 경우 0.8 이상으로 설정합니다.*

---

## 📚 RAG 구현: 도서관 사서 챗봇 만들기

### 🎯 프로젝트 목표

**시나리오**:
- 사용자가 파이썬에 관한 질문을 합니다.
- 챗봇(인공지능 모델)은 먼저 DB(RAG)에서 관련 내용을 찾아봅니다.
- 그 정보를 참고하여 똑똑해진 다음, 사용자에게 정확한 응답을 제공합니다.

*📌 노트: 이 시스템은 "도서관 사서"에 비유할 수 있습니다. 사서는 질문을 받으면 먼저 도서관에서 관련 책을 찾아보고, 그 내용을 바탕으로 답변을 제공합니다.*

---

### 📦 필요한 라이브러리 임포트

```python
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores      import FAISS
from langchain.text_splitter     import CharacterTextSplitter
from langchain.chat_models       import ChatOpenAI
from langchain.chains            import RetrievalQA
```

#### 💻 코드 실행 상세 분석

**각 모듈의 역할**:

1. **OpenAIEmbeddings**: 텍스트를 숫자 벡터로 변환하는 임베딩 모델
2. **FAISS**: Facebook AI Similarity Search - 벡터 검색을 위한 데이터베이스
3. **CharacterTextSplitter**: 긴 문서를 작은 청크(chunk)로 분할
4. **ChatOpenAI**: OpenAI의 채팅 모델을 LangChain에서 사용할 수 있게 해주는 래퍼
5. **RetrievalQA**: 검색 기반 질의응답 체인

**최종 결과**: RAG 시스템 구축에 필요한 모든 도구가 준비됩니다.

---

### 📝 외부 문서 데이터베이스 구축

#### 1. 문서 데이터 준비

```python
# 외부 DB 개념으로 사용할 문서(doc)를 만듭니다.
doc = [
    '리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.',
    '튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다.',
    '딕셔너리는 키(key)와 값(value)의 쌍으로 데이터를 저장합니다.'
]
```

#### 💻 코드 실행 상세 분석

**1단계 (리스트 생성)**: 파이썬의 리스트 자료형을 사용하여 3개의 문자열을 저장합니다. 각 문자열은 파이썬의 자료형에 대한 설명입니다.

**최종 결과**: 이 `doc` 리스트가 우리의 "지식 베이스" 역할을 합니다. 실제 환경에서는 이 데이터가 수천, 수만 개의 문서로 확장될 수 있습니다.

*📌 노트: 실무에서는 이 문서 데이터가 파일 시스템, 데이터베이스, 또는 웹 스크래핑을 통해 수집됩니다. 예를 들어, 회사의 매뉴얼 PDF, 기술 문서, 이메일 아카이브 등을 RAG 데이터로 활용할 수 있습니다.*

---

#### 2. 문서 청크 분할

```python
# 문서를 청크(chunk) 단위로 분할합니다.
# chunk_size는 chunk_overlap(겹치는 글자 수)보다 커야 합니다.
text_splitter = CharacterTextSplitter(chunk_size=250)
texts = text_splitter.create_documents(doc)
print(texts)
```

#### 💻 코드 실행 상세 분석

**1단계 (Splitter 객체 생성)**: `CharacterTextSplitter` 클래스의 인스턴스를 생성합니다. `chunk_size=250`은 각 청크의 최대 문자 수를 의미합니다.

**2단계 (문서 분할 실행)**: `create_documents(doc)` 메서드가 호출되면서 다음 과정이 진행됩니다:
- 리스트의 각 문자열을 확인합니다.
- 각 문자열의 길이가 250자를 초과하는지 확인합니다.
- 초과하면 여러 청크로 분할하고, 그렇지 않으면 하나의 청크로 유지합니다.
- 각 청크를 `Document` 객체로 래핑합니다.

**3단계 (결과 출력)**: `texts` 변수에는 `Document` 객체들의 리스트가 저장됩니다.

**출력 예시**:
```python
[
    Document(page_content='리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.'),
    Document(page_content='튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다.'),
    Document(page_content='딕셔너리는 키(key)와 값(value)의 쌍으로 데이터를 저장합니다.')
]
```

**최종 결과**: 각 문서가 `Document` 객체로 래핑되어 LangChain에서 처리하기 쉬운 형태로 변환됩니다.

*💡 중요!: chunk_size를 적절히 설정하는 것이 중요합니다. 너무 크면 검색 정확도가 떨어지고, 너무 작으면 문맥이 손실될 수 있습니다. 일반적으로 500~1000 정도가 적절합니다.*

---

#### 3. 임베딩 및 벡터 데이터베이스 생성

```python
# OpenAI 임베딩 모델을 초기화합니다.
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')

# 분할된 텍스트와 임베딩 모델을 사용하여 FAISS 벡터 데이터베이스를 생성합니다.
# 이것이 RAG의 핵심인 '검색(Retrieval)'을 위한 데이터베이스입니다.
db = FAISS.from_documents(texts, embedding=embeddings)
print(db)
```

#### 💻 코드 실행 상세 분석

**1단계 (임베딩 모델 초기화)**: `OpenAIEmbeddings` 클래스의 인스턴스를 생성합니다. 이 객체는 텍스트를 1536차원의 숫자 벡터로 변환하는 역할을 합니다.

**2단계 (벡터 생성)**: `FAISS.from_documents()` 메서드가 호출되면서 다음 과정이 진행됩니다:
- `texts` 리스트의 각 `Document` 객체를 순회합니다.
- 각 문서의 `page_content`를 임베딩 모델에 전달합니다.
- 임베딩 모델이 텍스트를 1536개의 부동소수점 숫자로 구성된 벡터로 변환합니다.
- 생성된 벡터들을 FAISS 인덱스에 저장합니다.

**3단계 (인덱스 생성)**: FAISS는 내부적으로 효율적인 검색을 위한 인덱스 구조를 생성합니다. 이를 통해 수백만 개의 벡터 중에서도 빠르게 유사한 벡터를 찾을 수 있습니다.

**출력 예시**:
```python
<langchain_community.vectorstores.faiss.FAISS object at 0x0000027F2DA29750>
```

**최종 결과**: `db` 객체는 이제 우리의 "지식 베이스"를 벡터 형태로 저장하고 있습니다. 질문이 들어오면 이 db에서 유사한 문서를 빠르게 검색할 수 있습니다.

*📌 노트: 임베딩 과정에서 "리스트"라는 단어와 "mutable"이라는 단어가 함께 나타나는 패턴, "튜플"과 "immutable"이 함께 나타나는 패턴 등이 벡터 공간에서 가까운 위치에 배치됩니다. 이를 통해 의미적으로 유사한 문서를 찾을 수 있습니다.*

---

#### 4. Retriever 설정

```python
# 검색 인터페이스를 설정합니다.
# as_retriever(): 검색 인터페이스를 이용해서 LLM과 연결하는 것
retriever = db.as_retriever(search_kwargs={'k': 1})  # 반환 문서 수: 1
print(retriever)
```

#### 💻 코드 실행 상세 분석

**1단계 (Retriever 생성)**: `db.as_retriever()` 메서드가 호출되면서 FAISS 데이터베이스를 검색 가능한 인터페이스로 변환합니다.

**2단계 (검색 파라미터 설정)**: `search_kwargs={'k': 1}` 파라미터는 검색 시 반환할 문서의 개수를 지정합니다. `k=1`은 가장 유사한 문서 1개만 반환하라는 의미입니다.

**출력 예시**:
```python
tags=['FAISS', 'OpenAIEmbeddings'] 
vectorstore=<langchain_community.vectorstores.faiss.FAISS object at 0x0000027F2DA29750> 
search_kwargs={'k': 1}
```

**최종 결과**: `retriever` 객체는 이제 질문을 받으면 가장 관련성 높은 문서 1개를 찾아주는 역할을 합니다.

*💡 중요!: `k` 값을 조절하여 반환할 문서 수를 변경할 수 있습니다. `k=3`이면 상위 3개의 관련 문서를 반환합니다. 너무 많은 문서를 반환하면 LLM이 처리할 토큰 수가 증가하므로, 비용과 성능을 고려하여 적절히 설정해야 합니다.*

---

### 🔗 RetrievalQA 체인 생성

```python
# 질문-답변(QA) 체인을 생성합니다.
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model='gpt-4o-mini', temperature=0.9),
    # stuff, map_reduce, refine etc...
    chain_type='stuff',
    retriever=retriever
)
print(qa)
```

#### 💻 코드 실행 상세 분석

**1단계 (LLM 설정)**: `ChatOpenAI(model='gpt-4o-mini', temperature=0.9)` 객체를 생성하여 답변 생성에 사용할 언어 모델을 지정합니다.

**2단계 (체인 타입 선택)**: `chain_type='stuff'` 파라미터는 검색된 문서를 LLM에 전달하는 방식을 지정합니다:
- **stuff**: 검색된 모든 문서를 하나의 프롬프트에 넣는 가장 간단한 방식
- **map_reduce**: 각 문서를 개별적으로 처리한 후 결과를 종합
- **refine**: 문서를 순차적으로 처리하며 답변을 개선

**3단계 (Retriever 연결)**: `retriever` 파라미터로 앞서 생성한 검색기를 연결합니다.

**4단계 (체인 생성)**: `RetrievalQA.from_chain_type()` 메서드가 전체 파이프라인을 구성합니다:
```
[사용자 질문] → [Retriever로 문서 검색] → [검색된 문서 + 질문을 LLM에 전달] 
              → [LLM이 답변 생성] → [사용자에게 반환]
```

**출력 예시**:
```python
combine_documents_chain=StuffDocumentsChain(
    llm_chain=LLMChain(
        prompt=ChatPromptTemplate(...),
        llm=ChatOpenAI(model_name='gpt-4o-mini', temperature=0.9, ...)
    ),
    document_variable_name='context'
) 
retriever=VectorStoreRetriever(...)
```

**최종 결과**: `qa` 객체는 이제 완전한 RAG 시스템입니다. 질문을 받으면 자동으로 문서를 검색하고, 그 내용을 바탕으로 답변을 생성합니다.

*📌 노트: "stuff" 방식은 간단하고 빠르지만, 문서가 많거나 길 경우 토큰 제한에 걸릴 수 있습니다. 이런 경우 "map_reduce"나 "refine" 방식을 사용하는 것이 좋습니다.*

---

### 💬 실제 질의 및 응답

```python
# 질의: 문서 기반 질의 (RAG가 강한 부분)
'''
간단한 사실 확인
예제코드 요청
비교-선택 도움

RAG가 강한 부분 = 문서 기반의 질의응답
'''

query = '파이썬 리스트와 튜플의 차이점을 설명해줘'
answer = qa.run(query)

print('Q - ', query)
print()
print('사서가 참고한 내용 - ', retriever.get_relevant_documents(query)[0].page_content)
print()
print('A - ', answer)
```

#### 💻 코드 실행 상세 분석

**1단계 (질문 입력)**: `query` 변수에 사용자의 질문을 저장합니다.

**2단계 (qa.run() 실행)**: `qa.run(query)` 메서드가 호출되면서 다음 과정이 진행됩니다:

   **2-1. 질문 임베딩**: 사용자의 질문 "파이썬 리스트와 튜플의 차이점을 설명해줘"가 1536차원의 벡터로 변환됩니다.
   
   **2-2. 문서 검색**: FAISS 데이터베이스에서 질문 벡터와 가장 유사한 문서 벡터를 찾습니다. 벡터 간의 코사인 유사도를 계산하여 가장 관련성 높은 문서를 선택합니다.
   
   **2-3. 문서 추출**: `k=1` 설정에 따라 가장 유사한 문서 1개를 가져옵니다. 이 경우 "리스트는 파이썬에서 변경 가능한(mutable) 자료형으로..." 문서가 선택됩니다.
   
   **2-4. 프롬프트 구성**: 검색된 문서와 사용자 질문을 조합하여 LLM에 전달할 프롬프트를 구성합니다:
   ```
   시스템: 다음 문서를 참고하여 질문에 답변하세요.
   문서: 리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.
   질문: 파이썬 리스트와 튜플의 차이점을 설명해줘
   ```
   
   **2-5. LLM 호출**: 구성된 프롬프트를 OpenAI API에 전송합니다.
   
   **2-6. 답변 수신**: LLM이 문서를 참고하여 생성한 답변을 받습니다.

**3단계 (결과 출력)**: 
- 질문을 출력합니다.
- `retriever.get_relevant_documents(query)[0].page_content`를 통해 실제로 참고된 문서를 출력합니다.
- LLM이 생성한 최종 답변을 출력합니다.

**출력 예시**:
```
Q -  파이썬 리스트와 튜플의 차이점을 설명해줘

사서가 참고한 내용 -  리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.

A -  파이썬 리스트와 튜플의 주요 차이점은 다음과 같습니다:

1. **변경 가능성**: 리스트는 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다. 반면에 튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 그 내용을 변경할 수 없습니다.

2. **구성**: 리스트는 대괄호([])로 정의하고, 튜플은 소괄호(())로 정의합니다.

3. **성능**: 튜플은 리스트보다 일반적으로 메모리 사용량이 적고, 성능이 좋습니다. 이는 튜플이 불변성을 가지기 때문에 더 효율적으로 저장될 수 있습니다.

4. **용도**: 리스트는 데이터에 대한 변경이 필요할 때 주로 사용되며, 튜플은 데이터가 고정되어 있어야 할 때, 즉 변경할 필요가 없거나 변경해서는 안 되는 경우에 사용됩니다.
```

**최종 결과**: RAG 시스템이 완벽하게 작동합니다! 검색된 문서를 참고하여 정확하고 상세한 답변을 생성했습니다.

*💡 중요!: 답변을 보면 LLM이 제공된 문서에만 의존하지 않고, 자신의 지식을 추가하여 더 풍부한 답변을 생성했습니다. 이것이 RAG의 장점입니다. 문서는 "가이드라인"이고, LLM은 그것을 바탕으로 더 완전한 답변을 만들어냅니다.*

---

### 🎨 Streamlit으로 웹 인터페이스 구축

이제 우리가 만든 RAG 시스템을 웹 인터페이스로 제공해봅시다.

```python
import os
import openai
import streamlit as st

from dotenv                      import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores      import FAISS
from langchain.text_splitter     import CharacterTextSplitter
from langchain.chat_models       import ChatOpenAI 
from langchain.chains            import RetrievalQA

doc = [
    '리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.',
    '튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다.',
    '딕셔너리는 키(key)와 값(value)의 쌍으로 데이터를 저장합니다.'
]

def ask_gpt():
    """RAG 시스템을 초기화하고 QA 체인을 반환하는 함수"""
    
    # OpenAI API 키 로드     
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    # RAG: 문서를 숫자 배열로 변환
    text_splitter = CharacterTextSplitter(chunk_size=250)
    texts = text_splitter.create_documents(doc)
    
    # Embedding & FAISS 벡터 DB 생성
    embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
    db = FAISS.from_documents(texts, embedding=embeddings)
    
    # Retriever 설정: 반환 문서 수를 1개로 제한
    retriever = db.as_retriever(search_kwargs={'k': 1})
    
    # QA 체인 생성
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model='gpt-4o-mini', temperature=0.9),
        chain_type='stuff',
        retriever=retriever
    )
    
    return qa, retriever

def view():
    """Streamlit UI를 구성하는 함수"""
    
    st.title('🤖 LangChain + RAG 도서관 사서봇')
    
    # 사용자 입력 받기
    query = st.text_input('질문을 입력하세요 : ') 
    
    if query:
        with st.spinner('외부 데이터베이스를 검색하고 있습니다....'):
            
            # RAG 시스템 초기화
            qa, retriever = ask_gpt()
            
            # 답변 생성
            answer = qa.run(query) 
            
            # 결과 출력
            st.success('A - ' + answer) 
            st.caption('R - ' + retriever.get_relevant_documents(query)[0].page_content)

if __name__ == '__main__':
    view()
```

#### 💻 코드 실행 상세 분석

**1단계 (모듈 임포트)**: Streamlit과 필요한 라이브러리들을 임포트합니다.

**2단계 (ask_gpt 함수 정의)**: 
- API 키를 로드합니다.
- 문서를 청크로 분할합니다.
- 임베딩과 FAISS를 사용하여 벡터 DB를 생성합니다.
- Retriever와 QA 체인을 설정합니다.
- QA 체인과 Retriever를 반환합니다.

**3단계 (view 함수 정의)**:
- `st.title()`로 페이지 제목을 설정합니다.
- `st.text_input()`으로 사용자 입력을 받습니다.
- 질문이 입력되면 `st.spinner()`로 로딩 애니메이션을 표시합니다.
- `ask_gpt()`를 호출하여 RAG 시스템을 초기화합니다.
- `qa.run(query)`로 답변을 생성합니다.
- `st.success()`로 답변을 표시하고, `st.caption()`으로 참고한 문서를 표시합니다.

**4단계 (메인 실행)**: `if __name__ == '__main__':` 블록에서 `view()` 함수를 호출하여 앱을 실행합니다.

**실행 방법**:
```bash
streamlit run streamlit_library_chatbot_app.py
```

**최종 결과**: 웹 브라우저에서 사용자 친화적인 챗봇 인터페이스가 열립니다. 사용자가 질문을 입력하면 RAG 시스템이 작동하여 답변을 생성하고, 참고한 문서까지 함께 표시됩니다.

*📌 노트: Streamlit의 `st.spinner()`는 사용자 경험을 개선하는 중요한 요소입니다. API 호출은 몇 초가 걸릴 수 있으므로, 로딩 중임을 명확히 표시하여 사용자가 기다리도록 유도합니다.*

---

## 🛡️ 보안 로그 분석 대시보드 구축

### 🎯 프로젝트 개요

**목표**: LLM을 활용하여 보안 로그 데이터를 분석하고, 공격 유형, 국가, 위험도 등을 시각적으로 표현하는 관리자 대시보드를 구축합니다.

**핵심 기능**:
1. CSV 형식의 보안 로그 파일 업로드
2. LLM을 통한 로그 분석 및 위험도 평가
3. 분석 결과를 데이터프레임으로 변환
4. 시각화 (추후 구현)

---

### 📊 전체 코드 구조

```python
import os
import openai
import streamlit as st
import json
import pandas as pd
import numpy as np

from openai import OpenAI
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 시스템 프롬프트: LLM의 역할과 출력 형식 정의
system_content = '''
너는 아주 멋진 사이버보안 전문가야.
사용자가 업로드한 로그 데이터를 기반으로 분석해줘.
json 형식 이외의 다른 텍스트는 절대 포함하지마. 포함할거면 그냥 죽어
출력 예시)
[
    {"ip": "", "country": "", "attack_type": "", "risk_score": 0}
]
'''

def ask_llm(frm):
    """로그 데이터를 LLM에 전달하여 분석 결과를 받는 함수"""
    
    client = OpenAI(api_key=api_key)
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': system_content},
            {'role': 'user', 'content': f'로그분석\n{frm.to_dict()}'}
        ],
        max_tokens=4096,
        temperature=0.8
    )
    
    return response

def view():
    """Streamlit UI 구성"""
    
    st.set_page_config(page_title='보안 로그 분석 AI', layout='wide')
    st.title('🔒 LLM 기반 관리자 대시보드')
    st.markdown('''
    - 보안로그 데이터를 기반으로 공격유형, 국가, 위험도 등을 분석하여 시각적으로 구현
    - LangChain과 RAG 기법을 활용하여 보안 관련 질문에 답변합니다.
    ''')
    
    # CSV 파일 업로드
    file = st.file_uploader("보안 로그 파일을 업로드하세요")
    
    if file:
        # CSV 파일을 데이터프레임으로 읽기
        frm = pd.read_csv(file)
        st.dataframe(frm.head())
        
        if st.button('분석 요청'):
            with st.spinner('분석중....'):
                # LLM에 분석 요청
                response = ask_llm(frm)
                
                # JSON 파싱
                data = json.loads(response.choices[0].message.content.strip())
                resultFrm = pd.DataFrame(data)
                
                # 결과 출력
                st.subheader('분석 결과 데이터 확인')
                st.dataframe(resultFrm)

if __name__ == "__main__":
    view()
```

#### 💻 코드 실행 상세 분석

**전체 흐름**:

**1단계 (파일 업로드)**: 
- 사용자가 CSV 파일을 업로드합니다.
- `pd.read_csv(file)`로 파일을 읽어 데이터프레임으로 변환합니다.
- `st.dataframe(frm.head())`로 데이터의 첫 5행을 화면에 표시합니다.

**2단계 (분석 버튼 클릭)**:
- 사용자가 "분석 요청" 버튼을 클릭합니다.
- `st.spinner('분석중....')`로 로딩 메시지를 표시합니다.

**3단계 (데이터 전처리)**:
- `frm.to_dict()`로 데이터프레임을 딕셔너리로 변환합니다.
- 딕셔너리를 문자열로 변환하여 LLM에 전달할 프롬프트를 구성합니다.

**4단계 (LLM 호출)**:
- `ask_llm(frm)` 함수가 호출됩니다.
- 시스템 메시지로 LLM의 역할을 정의합니다: "사이버보안 전문가"
- 사용자 메시지로 로그 데이터를 전달합니다.
- LLM이 로그 데이터를 분석하여 JSON 형식의 결과를 반환합니다.

**5단계 (응답 파싱)**:
- `response.choices[0].message.content`로 LLM의 응답 텍스트를 추출합니다.
- `.strip()`으로 앞뒤 공백과 줄바꿈 문자를 제거합니다.
- `json.loads()`로 JSON 문자열을 Python 딕셔너리/리스트로 파싱합니다.

**6단계 (데이터프레임 변환)**:
- `pd.DataFrame(data)`로 JSON 데이터를 데이터프레임으로 변환합니다.
- 이제 분석 결과를 테이블 형태로 표시하거나 시각화할 수 있습니다.

**7단계 (결과 표시)**:
- `st.subheader()`로 섹션 제목을 추가합니다.
- `st.dataframe(resultFrm)`으로 분석 결과를 테이블로 표시합니다.

**최종 결과**: 사용자가 업로드한 보안 로그가 LLM에 의해 분석되고, IP 주소, 국가, 공격 유형, 위험도 등이 포함된 구조화된 데이터로 반환됩니다.

---

### 🚨 중요한 트러블슈팅 사례

강의 중 발생한 여러 오류와 해결 과정은 실무에서도 자주 마주치는 상황입니다.

#### 1. JSON 파싱 오류

**문제 상황**:
```python
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

**원인**: LLM이 반환한 응답에 JSON 이외의 텍스트가 포함되어 있거나, 특수 문자(escape sequence)가 포함되어 있을 때 발생합니다.

**해결 방법 1: strip() 사용**
```python
# 앞뒤 공백과 줄바꿈 제거
data = json.loads(response.choices[0].message.content.strip())
```

**해결 방법 2: 마크다운 코드 블록 제거**
```python
# ```json ... ``` 형식의 마크다운 제거
content = response.choices[0].message.content
content = content.replace('```json\n', '').replace('\n```', '').strip()
data = json.loads(content)
```

**해결 방법 3: 정규 표현식 사용**
```python
import re

content = response.choices[0].message.content
# JSON 부분만 추출
json_match = re.search(r'\[.*\]', content, re.DOTALL)
if json_match:
    data = json.loads(json_match.group())
```

*🔐 보안 노트: LLM의 출력은 항상 예측 가능하지 않습니다. 따라서 방어적 프로그래밍(defensive programming)을 통해 예외 상황을 처리해야 합니다. try-except 블록을 사용하여 파싱 오류를 처리하고, 사용자에게 명확한 오류 메시지를 표시하는 것이 좋습니다.*

---

#### 2. 싱글 vs 더블 쿼테이션 이슈

**문제 상황**:
```python
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
```

**원인**: JSON 표준은 더블 쿼테이션(")만 허용하는데, 시스템 프롬프트에서 싱글 쿼테이션(')을 사용한 예시를 제공했을 때 발생합니다.

**잘못된 예시**:
```python
system_content = '''
출력 예시)
[
    {'ip': '', 'country': '', 'attack_type': '', 'risk_score': 0}
]
'''
```

**올바른 예시**:
```python
system_content = '''
출력 예시)
[
    {"ip": "", "country": "", "attack_type": "", "risk_score": 0}
]
'''
```

*💡 중요!: LLM은 프롬프트에 제공된 예시를 매우 충실하게 따릅니다. 따라서 예시를 작성할 때는 정확한 형식을 사용해야 합니다. 이것이 바로 "프롬프트 엔지니어링"의 핵심입니다.*

---

#### 3. 토큰 부족 오류

**문제 상황**: 응답이 중간에 잘리거나, 불완전한 JSON이 반환됩니다.

**원인**: `max_tokens` 설정이 너무 낮아서 LLM이 응답을 완성하지 못했습니다.

**해결 방법**:
```python
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[...],
    max_tokens=4096,  # 충분한 토큰 수 확보
    temperature=0.8
)
```

*📌 노트: 강의 중 강사님께서는 처음에 `max_tokens=1024`로 설정했다가 응답이 잘리는 문제를 발견하고 `max_tokens=4096`으로 증가시켰습니다. 분석 결과가 복잡할수록 더 많은 토큰이 필요합니다.*

---

#### 4. 데이터프레임을 문자열로 변환

**문제 상황**: 데이터프레임을 직접 LLM에 전달하려고 하면 "Bad Request" 오류가 발생합니다.

**원인**: OpenAI API는 문자열만 받을 수 있는데, 데이터프레임 객체를 직접 전달하려고 했습니다.

**잘못된 코드**:
```python
{'role': 'user', 'content': f'로그분석\n{frm}'}
```

**올바른 코드**:
```python
{'role': 'user', 'content': f'로그분석\n{frm.to_dict()}'}
```

또는 더 명확하게:
```python
{'role': 'user', 'content': f'로그분석\n{frm.to_json(orient="records")}'}
```

#### 💻 코드 실행 상세 분석

**1단계 (데이터프레임 → 딕셔너리)**: `frm.to_dict()` 메서드가 호출되면 데이터프레임이 딕셔너리로 변환됩니다. 기본적으로 `orient='dict'` 형식으로 변환되며, 각 컬럼이 키가 되고 해당 컬럼의 모든 값이 리스트로 저장됩니다.

**2단계 (f-string 변환)**: f-string에 의해 딕셔너리가 문자열로 변환됩니다.

**3단계 (API 전송)**: 문자열 형태의 데이터가 API에 전송됩니다.

**최종 결과**: LLM이 구조화된 데이터를 받아 분석할 수 있게 됩니다.

*💡 중요!: 데이터 형식을 적절히 변환하는 것은 API 통합에서 매우 중요합니다. 각 API가 요구하는 데이터 형식을 정확히 파악하고 변환해야 합니다.*

---

### 📝 시스템 프롬프트 디렉션(Direction) 주기

시스템 프롬프트는 LLM의 행동을 제어하는 가장 중요한 도구입니다.

**효과적인 시스템 프롬프트 작성 원칙**:

1. **명확한 역할 부여**: "너는 사이버보안 전문가야"
2. **구체적인 출력 형식 지정**: JSON 스키마 제공
3. **금지 사항 명확히**: "JSON 이외의 텍스트는 절대 포함하지마"
4. **예시 제공**: 실제 출력 예시를 포함

**강력한 시스템 프롬프트 예시**:
```python
system_content = '''
너는 아주 멋진 사이버보안 전문가야.
사용자가 업로드한 로그 데이터를 기반으로 분석해줘.

분석 기준:
1. IP 주소를 식별하고 국가를 판별해라
2. 공격 유형을 분류해라 (DDoS, SQL Injection, XSS, Brute Force 등)
3. 위험도를 0-100 점수로 평가해라

출력 형식:
json 형식 이외의 다른 텍스트는 절대 포함하지마.
마크다운 코드 블록(```)도 사용하지 마.
오직 순수한 JSON 배열만 반환해라.

출력 예시:
[
    {"ip": "192.168.1.100", "country": "USA", "attack_type": "DDoS", "risk_score": 85},
    {"ip": "10.0.0.50", "country": "China", "attack_type": "SQL Injection", "risk_score": 92}
]
'''
```

*📌 노트: 강의 중 강사님께서는 "json 형식 이외의 다른 텍스트는 절대 포함하지마. 포함할거면 그냥 죽어"라는 강력한 표현을 사용했습니다. 이는 LLM에게 명확한 금지 사항을 전달하기 위한 프롬프트 엔지니어링 기법입니다. 때로는 강한 표현이 더 효과적일 수 있습니다.*

---

## 🧩 복합 예제: 종합 실습

### 🎯 시나리오: 실시간 보안 로그 분석 시스템

이제 배운 모든 내용을 통합하여 실무에 가까운 복합 예제를 만들어봅시다.

```python
import os
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from openai import OpenAI
from dotenv import load_dotenv

# 환경 설정
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# 1단계: 가상의 보안 로그 데이터 생성
def generate_security_logs(num_logs=20):
    """
    실제 환경을 시뮬레이션한 보안 로그 생성
    """
    
    attack_types = ['DDoS', 'SQL Injection', 'XSS', 'Brute Force', 'Port Scan']
    countries = ['USA', 'China', 'Russia', 'North Korea', 'Iran']
    statuses = ['blocked', 'allowed', 'monitored']
    
    logs = []
    for i in range(num_logs):
        log = {
            'timestamp': (datetime.now() - timedelta(hours=i)).strftime('%Y-%m-%d %H:%M:%S'),
            'ip': f"{np.random.randint(1, 255)}.{np.random.randint(1, 255)}.{np.random.randint(1, 255)}.{np.random.randint(1, 255)}",
            'country': np.random.choice(countries),
            'attack_type': np.random.choice(attack_types),
            'status': np.random.choice(statuses),
            'payload_size': np.random.randint(100, 10000)
        }
        logs.append(log)
    
    return pd.DataFrame(logs)

# 2단계: LLM을 사용한 위험도 분석
def analyze_security_risk(logs_df):
    """
    보안 로그를 LLM에 전달하여 위험도 분석
    """
    
    system_prompt = '''
    당신은 20년 경력의 사이버보안 전문가입니다.
    제공된 보안 로그를 분석하여 각 이벤트의 위험도를 평가하고,
    추천 조치사항을 제시하세요.
    
    출력 형식:
    순수한 JSON 배열만 반환하세요. 마크다운이나 다른 텍스트는 포함하지 마세요.
    
    [
        {
            "ip": "IP 주소",
            "country": "국가",
            "attack_type": "공격 유형",
            "risk_score": 0-100 사이의 점수,
            "severity": "low/medium/high/critical",
            "recommended_action": "권장 조치사항"
        }
    ]
    '''
    
    user_prompt = f'''
    다음 보안 로그를 분석해주세요:
    
    {logs_df.to_json(orient='records', indent=2)}
    
    각 로그에 대해:
    1. 공격 유형과 출발 국가를 고려하여 위험도를 평가하세요
    2. 심각도 레벨을 지정하세요
    3. 구체적인 대응 조치를 제안하세요
    '''
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        max_tokens=4096,
        temperature=0.3  # 정확성을 위해 낮은 temperature
    )
    
    # 응답 파싱
    content = response.choices[0].message.content.strip()
    
    # 마크다운 코드 블록 제거
    content = content.replace('```json\n', '').replace('\n```', '').strip()
    
    # JSON 파싱
    try:
        analysis_results = json.loads(content)
        return pd.DataFrame(analysis_results)
    except json.JSONDecodeError as e:
        print(f"JSON 파싱 오류: {e}")
        print(f"응답 내용: {content}")
        return None

# 3단계: 고위험 이벤트 필터링
def filter_high_risk_events(analysis_df, risk_threshold=70):
    """
    위험도가 임계값을 초과하는 이벤트만 필터링
    """
    
    high_risk = analysis_df[analysis_df['risk_score'] >= risk_threshold]
    return high_risk.sort_values('risk_score', ascending=False)

# 4단계: 국가별 통계 생성
def generate_country_statistics(analysis_df):
    """
    국가별 공격 빈도와 평균 위험도 계산
    """
    
    stats = analysis_df.groupby('country').agg({
        'risk_score': ['mean', 'max', 'count']
    }).round(2)
    
    stats.columns = ['평균_위험도', '최대_위험도', '공격_횟수']
    return stats.sort_values('평균_위험도', ascending=False)

# 5단계: 전체 프로세스 실행
def main():
    """
    전체 보안 분석 파이프라인 실행
    """
    
    print("=" * 60)
    print("🔒 실시간 보안 로그 분석 시스템")
    print("=" * 60)
    print()
    
    # 1. 로그 데이터 생성
    print("📊 1단계: 보안 로그 생성 중...")
    logs_df = generate_security_logs(num_logs=10)  # 10개의 로그 생성
    print(f"✓ {len(logs_df)}개의 로그 생성 완료")
    print()
    print("원본 로그 데이터:")
    print(logs_df)
    print()
    
    # 2. LLM을 통한 위험도 분석
    print("🤖 2단계: AI 기반 위험도 분석 중...")
    analysis_df = analyze_security_risk(logs_df)
    
    if analysis_df is not None:
        print(f"✓ {len(analysis_df)}개의 로그 분석 완료")
        print()
        print("분석 결과:")
        print(analysis_df[['ip', 'country', 'attack_type', 'risk_score', 'severity']])
        print()
        
        # 3. 고위험 이벤트 필터링
        print("⚠️ 3단계: 고위험 이벤트 필터링...")
        high_risk = filter_high_risk_events(analysis_df, risk_threshold=70)
        
        if len(high_risk) > 0:
            print(f"✓ {len(high_risk)}개의 고위험 이벤트 발견!")
            print()
            print("고위험 이벤트 상세:")
            for idx, row in high_risk.iterrows():
                print(f"\n[경고] IP: {row['ip']} (위험도: {row['risk_score']})")
                print(f"  - 공격 유형: {row['attack_type']}")
                print(f"  - 출발 국가: {row['country']}")
                print(f"  - 심각도: {row['severity']}")
                print(f"  - 권장 조치: {row['recommended_action']}")
        else:
            print("✓ 고위험 이벤트 없음")
        print()
        
        # 4. 국가별 통계
        print("📈 4단계: 국가별 통계 생성...")
        country_stats = generate_country_statistics(analysis_df)
        print(country_stats)
        print()
        
        print("=" * 60)
        print("✅ 분석 완료!")
        print("=" * 60)
    
    else:
        print("❌ 분석 실패")

# 실행
if __name__ == "__main__":
    main()
```

#### 💻 코드 실행 상세 분석

이 복합 예제는 여러 단계로 구성되어 있으며, 각 단계는 실무에서 자주 사용되는 패턴입니다.

**1단계 (데이터 생성)**:
- `generate_security_logs()` 함수가 호출됩니다.
- `np.random.choice()`를 사용하여 무작위로 공격 유형, 국가, 상태를 선택합니다.
- `datetime.now() - timedelta(hours=i)`를 사용하여 과거 시간을 시뮬레이션합니다.
- 각 로그를 딕셔너리로 구성하고 리스트에 추가합니다.
- `pd.DataFrame(logs)`로 데이터프레임을 생성합니다.

**2단계 (LLM 분석)**:
- `analyze_security_risk()` 함수가 호출됩니다.
- 시스템 프롬프트로 LLM의 역할을 "20년 경력의 사이버보안 전문가"로 설정합니다.
- 로그 데이터를 JSON 형식으로 변환하여 사용자 프롬프트에 포함합니다.
- `temperature=0.3`으로 설정하여 정확하고 일관된 답변을 유도합니다.
- LLM이 각 로그에 대해 위험도, 심각도, 권장 조치를 평가합니다.
- 응답을 파싱하여 데이터프레임으로 변환합니다.

**3단계 (고위험 필터링)**:
- `filter_high_risk_events()` 함수가 호출됩니다.
- `analysis_df['risk_score'] >= risk_threshold` 조건으로 필터링합니다.
- `sort_values('risk_score', ascending=False)`로 위험도 높은 순으로 정렬합니다.

**4단계 (통계 생성)**:
- `generate_country_statistics()` 함수가 호출됩니다.
- `groupby('country')`로 국가별로 그룹화합니다.
- `agg()`로 평균, 최대값, 개수를 계산합니다.
- 결과를 위험도 높은 순으로 정렬합니다.

**5단계 (결과 출력)**:
- 각 단계의 진행 상황과 결과를 명확하게 출력합니다.
- 고위험 이벤트는 상세히 출력하여 즉각적인 대응을 유도합니다.

**최종 결과**: 실시간 보안 로그 분석 시스템이 완성됩니다. 이 시스템은 로그를 수집하고, AI로 분석하고, 위험도를 평가하고, 통계를 생성하는 전 과정을 자동화합니다.

*💡 중요!: 이 예제는 RAG 없이 순수 LLM만 사용했습니다. 하지만 실무에서는 과거 공격 패턴 데이터베이스를 RAG로 연결하여 더 정확한 분석을 할 수 있습니다.*

---

## 🔐 보안 심화: 프로덕션 환경 고려사항

### 1. API 키 관리

**환경별 분리**:
```python
# development.env
OPENAI_API_KEY=sk-dev-...
DEBUG=True

# production.env
OPENAI_API_KEY=sk-prod-...
DEBUG=False
```

**AWS Secrets Manager 사용** (실무 권장):
```python
import boto3
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "openai/api-key"
    region_name = "us-west-2"
    
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        return json.loads(get_secret_value_response['SecretString'])
    except ClientError as e:
        raise e
```

---

### 2. 입력 검증 및 새니타이제이션

**사용자 입력 검증**:
```python
def validate_user_input(query):
    """
    악의적인 입력을 방지하기 위한 검증
    """
    
    # 길이 제한
    if len(query) > 1000:
        raise ValueError("질문이 너무 깁니다 (최대 1000자)")
    
    # 특수 문자 확인
    dangerous_chars = ['<script>', 'DROP TABLE', 'SELECT *']
    for char in dangerous_chars:
        if char.lower() in query.lower():
            raise ValueError("허용되지 않는 문자가 포함되어 있습니다")
    
    return query
```

---

### 3. 비용 모니터링

**API 사용량 추적**:
```python
class CostTracker:
    """
    API 사용 비용을 추적하는 클래스
    """
    
    def __init__(self):
        self.total_tokens = 0
        self.total_cost = 0.0
        
        # GPT-4o-mini 가격 (예시)
        self.price_per_1k_input = 0.00015
        self.price_per_1k_output = 0.0006
    
    def track_usage(self, response):
        """
        API 응답에서 토큰 사용량과 비용 계산
        """
        
        usage = response.usage
        input_tokens = usage.prompt_tokens
        output_tokens = usage.completion_tokens
        
        cost = (input_tokens / 1000 * self.price_per_1k_input + 
                output_tokens / 1000 * self.price_per_1k_output)
        
        self.total_tokens += (input_tokens + output_tokens)
        self.total_cost += cost
        
        return {
            'input_tokens': input_tokens,
            'output_tokens': output_tokens,
            'cost': round(cost, 4),
            'total_cost': round(self.total_cost, 4)
        }
```

---

### 4. 에러 핸들링

**견고한 에러 처리**:
```python
import time
from openai import OpenAIError, RateLimitError, APIError

def safe_api_call(client, messages, max_retries=3):
    """
    재시도 로직을 포함한 안전한 API 호출
    """
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model='gpt-4o-mini',
                messages=messages,
                max_tokens=1024,
                temperature=0.7
            )
            return response
            
        except RateLimitError:
            # 요청 제한 초과 시 대기 후 재시도
            wait_time = (attempt + 1) * 2
            print(f"요청 제한 초과. {wait_time}초 후 재시도...")
            time.sleep(wait_time)
            
        except APIError as e:
            # API 오류 시 재시도
            print(f"API 오류 발생: {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(1)
            
        except OpenAIError as e:
            # 기타 OpenAI 오류
            print(f"OpenAI 오류: {e}")
            raise
    
    raise Exception("최대 재시도 횟수 초과")
```

---

## 📚 학습 정리 및 다음 단계

### ✅ 오늘 배운 핵심 내용

1. **LLM, RAG, LangChain의 개념과 관계**
   - LLM: 문장을 이해하고 답변하는 인공지능 모델
   - RAG: LLM이 참고할 수 있는 외부 지식 저장소
   - LangChain: LLM과 RAG를 연결하는 프레임워크

2. **API 키 보안 관리**
   - .env 파일을 사용한 환경 변수 관리
   - 마스킹 함수를 통한 안전한 출력
   - .gitignore를 통한 소스 코드 보안

3. **OpenAI API 기본 사용법**
   - 클라이언트 초기화
   - Role 기반 메시지 구조 (system, user, assistant)
   - 파라미터 조정 (max_tokens, temperature)

4. **RAG 시스템 구축**
   - 문서 청크 분할
   - 임베딩 및 벡터 데이터베이스 생성
   - Retriever 설정 및 QA 체인 구성

5. **Streamlit 웹 인터페이스**
   - 파일 업로드 및 데이터 표시
   - 사용자 입력 처리
   - 로딩 상태 표시 및 결과 출력

6. **보안 로그 분석 대시보드**
   - CSV 파일 로드 및 전처리
   - LLM을 통한 로그 분석
   - JSON 파싱 및 데이터프레임 변환

7. **트러블슈팅 경험**
   - JSON 파싱 오류 해결
   - 싱글/더블 쿼테이션 이슈
   - 토큰 부족 문제
   - 데이터 형식 변환

---

### 🎯 내일 학습 예정 내용

강사님께서 말씀하신 내일의 학습 계획:

1. **데이터 클렌징 (Data Cleansing)**
   - 정규 표현식을 사용한 텍스트 전처리
   - Escape sequence 처리 (\n, \t 등)
   - 마크다운 코드 블록 제거
   - 특수 문자 처리

2. **시각화 완성**
   - 분석 결과를 그래프로 표현
   - Matplotlib, Plotly 활용
   - 인터랙티브 대시보드 구현

3. **데이터프레임 형식 변환**
   - JSON → DataFrame
   - DataFrame → JSON
   - 다양한 orient 옵션 활용

4. **고급 프롬프트 엔지니어링**
   - Few-shot learning
   - Chain-of-Thought prompting
   - 구조화된 출력 강제하기

---

### 💭 강사님의 마지막 조언

강의 마지막에 강사님께서는 다음과 같이 말씀하셨습니다:

*"여러분, 에러가 난다는 것이 여러분을 힘들게 하는 것이 아니라, 알아간다는 즐거움이 있습니다. 긍정의 마인드를 가지세요. 오류도 적당히 나와야 재미있습니다. 개발과 코드 구현은 한 번에 되는 게 없어요. 이런 과정을 거치는 것이 학습입니다."*

이는 개발자로서 가져야 할 중요한 마인드셋입니다. 에러를 두려워하지 말고, 각각의 에러를 해결하는 과정에서 성장하는 것입니다.

---

### 📖 추가 학습 자료

**공식 문서**:
- OpenAI API: https://platform.openai.com/docs
- LangChain: https://python.langchain.com/docs/get_started/introduction
- Streamlit: https://docs.streamlit.io

**추천 읽을거리**:
- "Prompt Engineering Guide" by OpenAI
- "Building LLM Applications with LangChain"
- "RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (논문)

---

### 🏆 실습 과제 제안

오늘 배운 내용을 복습하기 위한 실습 과제:

1. **기본 과제**: 자신만의 주제로 RAG 시스템 구축하기
   - 예: 요리 레시피 추천, 영화 정보 검색, 회사 FAQ 봇

2. **중급 과제**: 다중 문서 소스를 활용한 RAG 시스템
   - PDF, 웹사이트, 데이터베이스를 모두 RAG로 통합

3. **고급 과제**: 실시간 스트리밍 응답 구현
   - OpenAI의 스트리밍 API를 사용하여 답변이 생성되는 과정을 실시간으로 표시

---

## 🙏 마무리

오늘 강의는 LLM, RAG, LangChain의 기초를 탄탄히 다지고, 실제 애플리케이션을 구축하는 방법을 배우는 뜻깊은 시간이었습니다. 특히 에러를 만나고 해결하는 과정을 통해 실무에서 필요한 트러블슈팅 능력을 키울 수 있었습니다.

강사님께서 강조하신 것처럼, "작은 것의 소중함"을 느끼며 하루하루 성장해 나가시기 바랍니다. 한 번에 모든 것을 이해할 필요는 없습니다. 꾸준히, 인내심을 가지고 학습하다 보면 어느새 "궁경의 씨앗"이 자라 큰 나무가 되어 있을 것입니다.

**내일 또 만나요!** 🚀

---

## 📝 부록: 전체 코드 모음

### A. API 키 마스킹 코드
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def masking(key):
    if len(key) <= 8:
        return '*' * len(key)
    return key[:4] + "*" * (len(key) - 8) + key[-4:]

masked_api_key = masking(api_key)
print(f"Masked API Key: {masked_api_key}")
```

### B. 기본 LLM 대화 코드
```python
from openai import OpenAI

client = OpenAI(api_key=api_key)

system_content = '''당신은 친절한 파이썬 보안 도우미입니다.'''
user_content = '패키지 설치 시 보안 지침을 알려주세요'

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system', 'content': system_content},
        {'role': 'user', 'content': user_content}
    ],
    max_tokens=1024,
    temperature=0.7
)

print(response.choices[0].message.content)
```

### C. RAG 시스템 전체 코드
```python
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

doc = [
    '리스트는 파이썬에서 변경 가능한(mutable) 자료형입니다.',
    '튜플은 변경 불가능한(immutable) 자료형입니다.',
    '딕셔너리는 키와 값의 쌍으로 데이터를 저장합니다.'
]

text_splitter = CharacterTextSplitter(chunk_size=250)
texts = text_splitter.create_documents(doc)

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
db = FAISS.from_documents(texts, embedding=embeddings)

retriever = db.as_retriever(search_kwargs={'k': 1})

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model='gpt-4o-mini', temperature=0.9),
    chain_type='stuff',
    retriever=retriever
)

query = '리스트와 튜플의 차이점을 설명해줘'
answer = qa.run(query)
print(answer)
```

### D. Streamlit 앱 전체 코드
```python
import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

doc = ['리스트는 변경 가능합니다.', '튜플은 변경 불가능합니다.']

def ask_gpt():
    text_splitter = CharacterTextSplitter(chunk_size=250)
    texts = text_splitter.create_documents(doc)
    embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
    db = FAISS.from_documents(texts, embedding=embeddings)
    retriever = db.as_retriever(search_kwargs={'k': 1})
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model='gpt-4o-mini', temperature=0.9),
        chain_type='stuff',
        retriever=retriever
    )
    return qa, retriever

def view():
    st.title('🤖 LangChain + RAG 도서관 사서봇')
    query = st.text_input('질문을 입력하세요:')
    if query:
        with st.spinner('검색 중...'):
            qa, retriever = ask_gpt()
            answer = qa.run(query)
            st.success(f'A - {answer}')
            st.caption(f'R - {retriever.get_relevant_documents(query)[0].page_content}')

if __name__ == '__main__':
    view()
```

---

**끝. 총 라인 수: 약 1,150줄**
