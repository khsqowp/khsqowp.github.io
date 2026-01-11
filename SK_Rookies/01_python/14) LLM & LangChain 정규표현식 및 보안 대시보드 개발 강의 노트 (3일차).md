---
title: "📝 LLM & LangChain 정규표현식 및 보안 대시보드 개발 강의 노트 (3일차)"
date: 2025-11-12
excerpt: "오늘 강의에서는 다음과 같은 핵심 내용들을 배웠습니다:"
categories:
  - Python
tags:
  - Python
  - SK_Rookies
---

# 📝 LLM & LangChain 정규표현식 및 보안 대시보드 개발 강의 노트 (3일차)

> **강의 날짜**: 2025년 11월 12일  
> **주요 주제**: LLM/LangChain 복습, 정규표현식, 보안 로그 분석, Streamlit/Plotly 시각화

---

## 📚 학습 목표 및 오늘의 여정

오늘 강의에서는 다음과 같은 핵심 내용들을 배웠습니다:

- **LLM(Large Language Model)과 LangChain 프레임워크 복습**: 지난 시간에 배운 내용을 다시 한번 정리하고 심화 학습을 진행합니다
- **정규표현식(Regular Expression)**: 문자열 패턴 매칭의 핵심 도구를 마스터합니다
- **보안 로그 데이터 분석 및 시각화**: 실제 보안 데이터를 AI로 분석하고 시각화하는 방법을 학습합니다
- **AI 응답 결과 전처리**: AI가 반환한 데이터를 실제로 사용 가능한 형태로 가공하는 기술을 습득합니다

💡 **중요!**: 강사님께서 강조하신 점은 "보안을 하시는 분들도 코드를 보는 관점이 중요하다"는 것입니다. 개발을 하지 않더라도 코드를 보안적 관점에서 분석할 수 있어야 하며, 특히 민감 정보 처리, 예외 처리, 데이터 검증 등이 핵심입니다.

---

## 🔧 개발 환경 설정

### 필수 패키지 임포트

오늘 강의에서 사용할 모든 패키지들을 정리해보겠습니다. 이 패키지들은 크게 두 가지 카테고리로 나뉩니다:

#### 1. LLM 관련 패키지

```python
# LLM 기본 패키지
import os
import re
import openai
import json
from openai import OpenAI
from dotenv import load_dotenv
```

#### 💻 코드 실행 상세 분석

**1단계 (모듈 임포트)**: 
- `os` 모듈은 운영체제와 상호작용하기 위해 사용됩니다. 주로 환경 변수를 읽어오는 데 활용됩니다.
- `re` 모듈은 정규표현식(Regular Expression)을 처리하기 위한 핵심 모듈입니다.
- `openai`와 `OpenAI`는 OpenAI API를 호출하기 위한 클라이언트 라이브러리입니다.
- `json` 모듈은 JSON 형식의 데이터를 파싱하고 생성하는 데 사용됩니다.
- `load_dotenv`는 `.env` 파일에서 환경 변수를 로드하여 코드 내에서 API 키 같은 민감한 정보를 안전하게 관리할 수 있게 해줍니다.

**2단계 (보안 고려사항)**: 
- API 키를 코드에 직접 하드코딩하지 않고 `.env` 파일을 통해 관리하는 것은 보안의 기본입니다.
- 이렇게 하면 Git 저장소에 민감한 정보가 올라가는 것을 방지할 수 있습니다.

#### 2. LangChain 관련 패키지

```python
# LangChain 프레임워크
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models       import ChatOpenAI
from langchain.prompts           import ChatPromptTemplate
from langchain.vectorstores      import FAISS
from langchain.text_splitter     import CharacterTextSplitter
from langchain.chains            import RetrievalQA, LLMChain
```

#### 💻 코드 실행 상세 분석

**1단계 (LangChain 컴포넌트 이해)**:
- `OpenAIEmbeddings`: 텍스트를 벡터로 변환하는 임베딩 모델입니다. RAG(Retrieval-Augmented Generation)에서 문서를 검색 가능한 형태로 만들 때 사용됩니다.
- `ChatOpenAI`: OpenAI의 채팅 모델을 LangChain에서 사용할 수 있도록 래핑한 클래스입니다.
- `ChatPromptTemplate`: 프롬프트를 템플릿화하여 재사용 가능하게 만드는 도구입니다.
- `FAISS`: Facebook에서 개발한 벡터 검색 라이브러리로, 문서 검색에 사용됩니다.
- `CharacterTextSplitter`: 긴 텍스트를 작은 청크로 분할하는 도구입니다.
- `RetrievalQA`, `LLMChain`: LangChain의 체인 구조로, 여러 작업을 연결할 수 있게 해줍니다.

**2단계 (아키텍처 이해)**:
- LangChain은 LLM을 더 쉽게 활용할 수 있도록 추상화한 프레임워크입니다.
- 체인(Chain) 구조를 통해 복잡한 워크플로우를 단순하게 구성할 수 있습니다.

📌 **노트**: 강사님께서 말씀하신 것처럼, 패키지 임포트는 항상 코드 최상단에 정리해두는 것이 좋습니다. 이렇게 하면 의존성을 한눈에 파악할 수 있고, 나중에 패키지 설치 문제를 트러블슈팅할 때도 편리합니다.

---

## 🔐 API 키 관리 및 마스킹

### API 키 로드 및 보안 처리

API 키는 매우 민감한 정보이므로 반드시 안전하게 관리해야 합니다. 다음은 API 키를 로드하고 마스킹 처리하는 코드입니다:

```python
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def masking(key):
    """API 키를 마스킹하여 출력할 때 보안을 유지합니다."""
    if len(key) <= 8:
        return '*' * len(key)
    return key[:4] + "*" * (len(key) - 8) + key[-4:]

if api_key:
    masked_api_key = masking(api_key)
    print(f"Masked API Key: {masked_api_key}")
else:
    print("API key not found. Please check your .env file.")
```

#### 💻 코드 실행 상세 분석

**1단계 (환경 변수 로드)**:
- `load_dotenv()` 함수가 실행되면, 프로젝트 루트 디렉토리에 있는 `.env` 파일을 찾아서 그 안의 모든 환경 변수를 메모리에 로드합니다.
- `.env` 파일 예시: `OPENAI_API_KEY=sk-proj1234...`

**2단계 (API 키 추출)**:
- `os.getenv("OPENAI_API_KEY")`를 호출하면, 환경 변수 중에서 `OPENAI_API_KEY`라는 이름의 값을 가져옵니다.
- 만약 해당 환경 변수가 없으면 `None`을 반환합니다.

**3단계 (마스킹 로직)**:
- `masking()` 함수는 API 키의 앞 4자리와 뒤 4자리만 보여주고, 중간 부분은 모두 `*`로 처리합니다.
- 예: `sk-proj****************************dv0A`
- 이렇게 하면 로그나 콘솔 출력에서 API 키가 노출되더라도 실제 키 값은 보호됩니다.

**4단계 (검증)**:
- `if api_key:` 조건문으로 API 키가 제대로 로드되었는지 확인합니다.
- API 키가 없으면 사용자에게 `.env` 파일을 확인하라는 메시지를 출력합니다.

🔐 **보안 노트**: 
- **절대 API 키를 코드에 직접 작성하지 마세요**: 코드가 Git에 올라가면 전 세계에 공개될 수 있습니다.
- **`.env` 파일은 `.gitignore`에 추가**: `.env` 파일이 버전 관리 시스템에 포함되지 않도록 반드시 `.gitignore`에 추가해야 합니다.
- **마스킹 처리의 중요성**: 디버깅이나 로깅 시 API 키가 콘솔에 출력될 수 있으므로, 항상 마스킹 처리된 값을 출력하는 습관을 들여야 합니다.
- **권한 최소화 원칙**: API 키에는 필요한 최소한의 권한만 부여하고, 정기적으로 키를 로테이션해야 합니다.

---

## 📖 정규표현식 (Regular Expression) 완벽 가이드

### 정규표현식이란?

정규표현식(Regular Expression, 줄여서 regex 또는 regexp)은 **문자열에서 특정 패턴을 찾고, 추출하고, 변환하기 위한 강력한 도구**입니다. 강사님께서 "정규표현식은 보안 전문가에게 필수적인 도구"라고 강조하셨는데, 그 이유는 다음과 같습니다:

1. **로그 분석**: 보안 로그에서 특정 패턴의 IP 주소, 이메일, 전화번호 등을 추출
2. **데이터 검증**: 사용자 입력이 올바른 형식인지 검증
3. **데이터 클린징**: AI가 반환한 결과에서 불필요한 텍스트를 제거하고 필요한 데이터만 추출
4. **민감정보 마스킹**: 로그에서 개인정보를 자동으로 찾아서 마스킹 처리

💡 **중요!**: 강의에서 강조된 점은 "AI 모델의 반환 결과는 자유로운 영혼의 문자열"이라는 것입니다. AI는 우리가 요청한 형식으로 답변을 주려고 하지만, 항상 완벽하게 그 형식을 지키는 것은 아닙니다. 따라서 정규표현식을 통해 필요한 데이터만 정확하게 추출하는 능력이 필수적입니다.

### 정규표현식 메타문자

메타문자는 정규표현식에서 특별한 의미를 가지는 문자들입니다:

| 메타문자 | 설명 | 예시 | 매칭 예시 |
|---------|------|------|----------|
| `.` | 임의의 한 문자 (줄바꿈 제외) | `a.c` | `abc`, `a1c`, `a c` |
| `^` | 문자열의 시작 | `^Hello` | `Hello World` (문자열이 Hello로 시작) |
| `$` | 문자열의 끝 | `World$` | `Hello World` (문자열이 World로 끝남) |
| `*` | 앞 문자가 0회 이상 반복 | `ab*c` | `ac`, `abc`, `abbc` |
| `+` | 앞 문자가 1회 이상 반복 | `ab+c` | `abc`, `abbc` (하지만 `ac`는 매칭 안 됨) |
| `?` | 앞 문자가 0회 또는 1회 | `ab?c` | `ac`, `abc` |
| `{m,n}` | 앞 문자가 m회 이상 n회 이하 반복 | `a{2,4}` | `aa`, `aaa`, `aaaa` |
| `[]` | 문자 집합 (OR 조건) | `[abc]` | `a`, `b`, `c` 중 하나 |
| `()` | 그룹화 | `(abc)+` | `abc`, `abcabc` |

#### 💻 코드 실행 상세 분석

**메타문자 동작 원리**:
1. **`.` (점)**: 정규표현식 엔진이 패턴을 읽을 때, 점은 "어떤 문자든 하나"를 의미합니다. 예를 들어 `a.c` 패턴은 'a'로 시작하고 'c'로 끝나며 중간에 어떤 문자든 하나가 있는 문자열과 매칭됩니다.

2. **`^`와 `$`**: 이 두 앵커(anchor)는 문자열의 위치를 지정합니다. `^`는 문자열의 시작 위치를, `$`는 끝 위치를 나타냅니다.

3. **수량자 (`*`, `+`, `?`, `{m,n}`)**: 이들은 앞에 오는 패턴이 몇 번 반복될 수 있는지를 지정합니다.
   - `*`: 0번 이상 (없어도 됨)
   - `+`: 1번 이상 (최소 1번은 있어야 함)
   - `?`: 0번 또는 1번 (선택적)
   - `{m,n}`: 정확히 m번 이상 n번 이하

### 정규표현식 특수 패턴

| 패턴 | 설명 | 동등한 표현 | 예시 |
|------|------|-------------|------|
| `\d` | 숫자 (digit) | `[0-9]` | `0`, `1`, `9` |
| `\D` | 숫자가 아닌 문자 | `[^0-9]` | `a`, `!`, ` ` |
| `\w` | 단어 문자 (word) | `[a-zA-Z0-9_]` | `a`, `Z`, `5`, `_` |
| `\W` | 단어 문자가 아닌 것 | `[^a-zA-Z0-9_]` | `!`, `@`, ` ` |
| `\s` | 공백 문자 (space) | 스페이스, 탭, 줄바꿈 | ` `, `\t`, `\n` |
| `\S` | 공백이 아닌 문자 | 공백 제외한 모든 문자 | `a`, `1`, `!` |

📌 **노트**: `\d`, `\w` 같은 특수 패턴은 가독성을 높여줍니다. 예를 들어, `[0-9]` 대신 `\d`를 쓰면 코드가 훨씬 간결해집니다.

### 정규표현식 함수들

Python의 `re` 모듈은 다양한 함수를 제공합니다:

#### 1. `re.search()` - 첫 번째 매칭 찾기

```python
import re

txt = "문의하신 고객의 전화번호는 010-1234-5678이고, 추가 문의사항이 있으면 help@example.com 으로 연락주세요."

# 이메일 패턴 정의
patternEmail = r'\w+@\w+\.\w+'

# search: 문자열 전체에서 패턴을 찾되, 첫 번째 매칭만 반환
email = re.search(patternEmail, txt)

if email:
    print(email)  # <re.Match object; span=(54, 70), match='help@example.com'>
    print(email.group())  # help@example.com
    print(f"위치: {email.span()}")  # 위치: (54, 70)
```

#### 💻 코드 실행 상세 분석

**1단계 (패턴 정의)**:
- `r'\w+@\w+\.\w+'` 패턴을 분석해봅시다:
  - `\w+`: 하나 이상의 단어 문자 (이메일의 로컬 파트, 예: `help`)
  - `@`: 골뱅이 기호 (리터럴)
  - `\w+`: 하나 이상의 단어 문자 (도메인 이름, 예: `example`)
  - `\.`: 점 (메타문자 `.`가 아닌 실제 점을 매칭하기 위해 이스케이프)
  - `\w+`: 하나 이상의 단어 문자 (최상위 도메인, 예: `com`)

**2단계 (검색 실행)**:
- `re.search()`는 문자열 전체를 스캔하면서 패턴과 일치하는 부분을 찾습니다.
- 첫 번째 매칭을 찾으면 즉시 `Match` 객체를 반환하고 검색을 중단합니다.

**3단계 (결과 추출)**:
- `email.group()`: 매칭된 전체 문자열을 반환합니다.
- `email.span()`: 매칭된 문자열의 시작 인덱스와 끝 인덱스를 튜플로 반환합니다.
- `email.start()`, `email.end()`: 각각 시작 인덱스와 끝 인덱스를 개별적으로 반환합니다.

#### 2. `re.findall()` - 모든 매칭 찾기

```python
# 전화번호 패턴
patternPhone = r'\d{3}-\d{3,4}-\d{4}'

# findall: 패턴과 일치하는 모든 부분을 리스트로 반환
phones = re.findall(patternPhone, txt)
print(phones)  # ['010-1234-5678']
print(type(phones))  # <class 'list'>
```

#### 💻 코드 실행 상세 분석

**1단계 (전화번호 패턴 분석)**:
- `\d{3}`: 정확히 3자리 숫자 (예: `010`)
- `-`: 하이픈 (리터럴)
- `\d{3,4}`: 3자리 또는 4자리 숫자 (예: `1234`)
- `-`: 하이픈
- `\d{4}`: 정확히 4자리 숫자 (예: `5678`)

**2단계 (전체 스캔)**:
- `re.findall()`은 `re.search()`와 달리 첫 번째 매칭에서 멈추지 않고 문자열 전체를 스캔합니다.
- 매칭되는 모든 부분을 리스트에 담아 반환합니다.

**3단계 (반환 형식)**:
- 항상 리스트를 반환합니다. 매칭이 없으면 빈 리스트 `[]`를 반환합니다.
- 이는 `for` 루프로 처리하기에 매우 편리합니다.

#### 3. `re.sub()` - 치환

```python
# 마크다운 코드 블록 제거 예시
csv_text = """```csv
name,age
John,30
```"""

# 시작 부분의 ```csv 또는 ``` 제거
csv_text = re.sub(r"^```[a-zA-Z]*\n?", "", csv_text)
# 끝 부분의 ``` 제거
csv_text = re.sub(r"```$", "", csv_text).strip()

print(csv_text)
# name,age
# John,30
```

#### 💻 코드 실행 상세 분석

**1단계 (첫 번째 치환)**:
- `r"^```[a-zA-Z]*\n?"` 패턴 분석:
  - `^`: 문자열의 시작
  - ` ``` `: 세 개의 백틱 (리터럴)
  - `[a-zA-Z]*`: 0개 이상의 알파벳 (예: `csv`, `python` 등, 또는 없을 수도 있음)
  - `\n?`: 줄바꿈이 있을 수도, 없을 수도 있음
- 이 패턴은 마크다운 코드 블록의 시작 부분 (예: ` ```csv\n`)을 찾습니다.
- `re.sub()`의 두 번째 인자 `""`는 빈 문자열로, 찾은 패턴을 빈 문자열로 치환합니다 (즉, 삭제).

**2단계 (두 번째 치환)**:
- `r"```$"` 패턴은 문자열 끝에 있는 세 개의 백틱을 찾습니다.
- 마찬가지로 빈 문자열로 치환하여 제거합니다.
- `.strip()`은 양쪽 끝의 공백이나 줄바꿈을 제거합니다.

**최종 결과**:
- AI가 반환한 마크다운 형식의 CSV 데이터에서 코드 블록 마커를 제거하여 순수한 CSV 텍스트만 남깁니다.

🔐 **보안 노트 - 정규표현식 활용**:
정규표현식은 보안 분야에서 다음과 같이 활용됩니다:
1. **입력 검증**: 사용자 입력이 예상한 형식인지 검증하여 인젝션 공격을 방지
2. **로그 분석**: 보안 로그에서 특정 패턴의 공격 시도를 자동으로 탐지
3. **민감정보 탐지 및 마스킹**: 로그나 데이터베이스에서 개인정보를 찾아 자동으로 마스킹
4. **데이터 클린징**: 외부에서 받은 데이터에서 악의적인 패턴을 제거

⚠️ **주의사항**: 정규표현식은 강력하지만, 잘못 작성하면 ReDoS(Regular Expression Denial of Service) 공격에 취약할 수 있습니다. 특히 중첩된 수량자(`(a+)+`)나 과도한 백트래킹을 유발하는 패턴은 피해야 합니다.

### 실전 예제: 이메일과 전화번호 추출

```python
txt = "문의하신 고객의 전화번호는 010-1234-5678이고, 추가 문의사항이 있으면 help@example.com 으로 연락주세요."

# 이메일 패턴
patternEmail = r'\w+@\w+\.\w+'
# 전화번호 패턴
patternPhone = r'\d{3}-\d{3,4}-\d{4}'

# 이메일 추출 (첫 번째만)
email = re.search(patternEmail, txt)
if email:
    print(f"이메일: {email.group()}")

# 전화번호 추출 (모든 경우)
phones = re.findall(patternPhone, txt)
for phone in phones:
    print(f"전화번호: {phone}")

# 숫자만 추출
numbers = re.findall(r'\d+', txt)
print(f"모든 숫자: {numbers}")
# 결과: ['010', '1234', '5678']
```

#### 💻 코드 실행 상세 분석

**전체 실행 흐름**:

**1단계 (이메일 검색)**:
- `re.search(patternEmail, txt)`가 실행되면, 정규표현식 엔진이 문자열을 왼쪽에서 오른쪽으로 스캔합니다.
- 패턴 `\w+@\w+\.\w+`와 일치하는 첫 번째 부분인 `help@example.com`을 찾습니다.
- `Match` 객체를 반환하고, `email.group()`으로 매칭된 문자열을 추출합니다.

**2단계 (전화번호 검색)**:
- `re.findall(patternPhone, txt)`는 문자열 전체를 스캔합니다.
- 패턴 `\d{3}-\d{3,4}-\d{4}`와 일치하는 모든 부분을 찾아 리스트로 반환합니다.
- 이 경우 `['010-1234-5678']`이 반환됩니다.

**3단계 (순수 숫자 추출)**:
- `\d+` 패턴은 "하나 이상의 연속된 숫자"를 의미합니다.
- 문자열에서 하이픈 없이 숫자 덩어리만 추출합니다.
- 결과: `['010', '1234', '5678']`

**실용적 활용**:
- 전화번호를 데이터베이스에 저장할 때는 하이픈을 제거한 순수 숫자만 저장하는 경우가 많습니다.
- 이렇게 하면 다양한 형식의 전화번호(예: `010-1234-5678`, `010.1234.5678`, `01012345678`)를 통일된 형식으로 관리할 수 있습니다.

---

## 🤖 LLM과 LangChain 통합

### Temperature 파라미터의 이해

LLM의 `temperature` 파라미터는 모델의 출력 다양성을 조절합니다:

```python
# Temperature: 0 ~ 2 (일반적으로 0 ~ 1 사용)
# 낮을수록 보수적(deterministic), 높을수록 창의적(random)

chat_uncreative = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=api_key, temperature=0)
chat_creative = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=api_key, temperature=1)

prompt = "인공지능을 간단히 설명해줘."

print('보수적 응답:', chat_uncreative.predict(prompt))
# 보수적 응답: 인공지능은 인간의 학습능력, 추론능력, 지각능력, 언어능력 등을 
# 컴퓨터 프로그램이나 기계에 구현한 기술을 말합니다...

print('창의적 응답:', chat_creative.predict(prompt))
# 창의적 응답: 인공지능은 기계가 지능적인 작업을 수행할 수 있도록 하는 기술이며, 
# 기계가 인간의 학습, 추리, 해결, 판단 등의 인지 능력을 모방하도록 고안된 분야입니다...
```

#### 💻 코드 실행 상세 분석

**Temperature 동작 원리**:

**1단계 (토큰 예측)**:
- LLM은 다음에 올 단어(토큰)를 예측할 때, 각 토큰에 대한 확률 분포를 생성합니다.
- 예를 들어: "인공지능은" 다음에 올 단어로 "기계"(30%), "컴퓨터"(25%), "시스템"(20%) 등

**2단계 (Temperature 적용)**:
- **Temperature = 0**: 
  - 가장 높은 확률의 토큰을 항상 선택합니다 (greedy decoding).
  - 같은 입력에 대해 항상 거의 같은 출력을 생성합니다.
  - 사실 기반 질문, 코드 생성, 번역 등에 적합합니다.

- **Temperature = 1**: 
  - 확률 분포를 그대로 사용하여 토큰을 샘플링합니다.
  - 높은 다양성과 창의성을 보입니다.
  - 창작, 브레인스토밍, 다양한 아이디어 생성에 적합합니다.

- **Temperature = 0.8** (중간값):
  - 적당한 창의성과 일관성을 유지합니다.
  - 대부분의 일반적인 용도에 적합합니다.

**3단계 (반복 실행 시 차이)**:
- Temperature가 0일 때: 같은 질문을 여러 번 해도 거의 동일한 답변
- Temperature가 높을 때: 같은 질문을 반복해도 매번 다른 뉘앙스의 답변

💡 **중요!**: 강사님께서 강조하신 점은 "보안 로그 분석처럼 일관성이 중요한 작업에서는 temperature를 0으로 설정하고, 창의적인 보고서 작성이나 다양한 시나리오 생성이 필요할 때는 높게 설정한다"는 것입니다.

### LangChain 체인 구성

```python
# LangChain 모델 초기화
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# 프롬프트 템플릿 정의
question = '섭섭님과 사담이 필요하면 jslim9413@naver.com 또는 jslim9413@gmail.com 으로 문의 부탁드립니다.'
prompt = ChatPromptTemplate.from_template(
    """
    해당 텍스트에서 이메일을 추출해줘 : {text}
    """
)

# 체인 생성 (RAG 없이)
chain = LLMChain(llm=chat, prompt=prompt)

# 실행
result = chain.run(text=question)
print(result)
# 출력: jslim9413@naver.com, jslim9413@gmail.com
```

#### 💻 코드 실행 상세 분석

**LangChain 체인의 동작 흐름**:

**1단계 (템플릿 준비)**:
- `ChatPromptTemplate.from_template()`은 문자열 템플릿을 받아서 `PromptTemplate` 객체를 생성합니다.
- 템플릿 안의 `{text}`는 플레이스홀더로, 나중에 실제 값으로 치환됩니다.

**2단계 (체인 구성)**:
- `LLMChain`은 `llm`(언어 모델)과 `prompt`(프롬프트 템플릿)를 연결합니다.
- 이는 "프롬프트 생성 → LLM 실행 → 결과 반환"의 파이프라인을 자동화합니다.

**3단계 (실행)**:
- `chain.run(text=question)`을 호출하면:
  1. `text` 파라미터가 템플릿의 `{text}` 자리에 삽입됩니다.
  2. 완성된 프롬프트가 LLM에 전달됩니다.
  3. LLM의 응답이 반환됩니다.

**4단계 (결과)**:
- LLM은 프롬프트를 이해하고, 텍스트에서 이메일 주소를 추출하여 반환합니다.
- 결과는 문자열 형태입니다.

📌 **노트**: LangChain을 사용하면 프롬프트를 재사용하기 쉽고, 복잡한 워크플로우를 체계적으로 관리할 수 있습니다. 하지만 간단한 작업에서는 OpenAI API를 직접 사용하는 것이 더 간단할 수 있습니다.

### 문제점: AI 응답의 일관성 부족

```python
# 이메일 추출을 요청했지만...
answer = chain.run(text='오늘 날씨 알려줘')
print(answer)
# 출력: "오늘 날씨는 맑고 화창합니다."
# (이메일이 아닌 날씨 정보를 반환!)

# 정규표현식으로 검증
emails = re.findall(r'\w+@\w+\.\w+', answer)
print(emails)  # []
```

#### 💻 코드 실행 상세 분석

**문제 상황 분석**:

**1단계 (잘못된 입력)**:
- 사용자가 "오늘 날씨 알려줘"라는 텍스트를 전달했습니다.
- 이 텍스트에는 이메일 주소가 포함되어 있지 않습니다.

**2단계 (AI의 응답)**:
- 프롬프트는 "해당 텍스트에서 이메일을 추출해줘"였지만, 텍스트에 이메일이 없습니다.
- AI는 맥락을 이해하고 "이메일이 없으므로 날씨에 대해 답변하는 것이 더 도움이 될 것"이라고 판단할 수 있습니다.
- 또는 프롬프트를 무시하고 입력 텍스트의 의도를 따라 날씨 정보를 제공합니다.

**3단계 (검증 실패)**:
- `re.findall()`로 이메일 패턴을 찾으려 하지만, 날씨 정보에는 이메일이 없으므로 빈 리스트가 반환됩니다.

**핵심 교훈**:
- **AI는 항상 우리가 원하는 대로 응답하지 않습니다.**
- **따라서 AI의 응답을 항상 검증하고 전처리해야 합니다.**
- 이것이 바로 정규표현식이 필요한 이유입니다!

💡 **중요!**: 강사님께서 "AI 모델의 반환 결과는 자유로운 영혼의 문자열"이라고 표현하신 것처럼, AI는 우리가 기대한 형식을 항상 지키지 않습니다. 따라서 **응답 검증과 전처리가 필수**입니다.

---

## 📊 실전 예제: 예약 정보를 JSON으로 변환

### 문제 정의

다음과 같은 예약 정보를 AI에게 전달하고, 구조화된 JSON 형식으로 반환받아야 합니다:

```python
reservation = """
이름  : 임섭순
연락처: 010-1234-5678
예약일: 2025-11-15
문의 이메일: jslim9413@naver.com
추가 이메일: jslim9413@gmail.com
"""
```

### 해결 방법 1: 프롬프트 엔지니어링

```python
chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_template('''
당신은 친절한 데이터 분석가입니다.
사용자가 업로드한 로그 데이터를 기반으로 분석해줘.
json 형식 이외의 다른 텍스트는 절대 포함하지마. 포함할거면 그냥 죽어
{reservation}
출력 예시)
[
    {% raw %}{{ "name" : "", "phone" : "", "date" : "", "email1" : "", "email2" : "" }}{% endraw %}
]
''')

chain = LLMChain(llm=chat, prompt=prompt)
response = chain.run(reservation=reservation)
print('response -', response)
```

#### 💻 코드 실행 상세 분석

**프롬프트 엔지니어링 기법**:

**1단계 (역할 부여)**:
- "당신은 친절한 데이터 분석가입니다"로 AI에게 역할을 명확히 부여합니다.
- 이렇게 하면 AI가 그 역할에 맞는 톤과 방식으로 응답합니다.

**2단계 (명확한 지시)**:
- "json 형식 이외의 다른 텍스트는 절대 포함하지마"는 매우 강력한 제약 조건입니다.
- "포함할거면 그냥 죽어"는 다소 강한 표현이지만, AI에게 중요성을 강조하는 효과가 있습니다.

**3단계 (출력 예시 제공)**:
- 구체적인 JSON 구조를 예시로 보여줍니다.
- 이렇게 하면 AI가 원하는 형식을 정확히 이해할 수 있습니다.
- 중괄호를 이중으로 `{% raw %}{{`{% endraw %} 쓰는 이유는 Python 문자열 포맷팅에서 중괄호가 특수 문자이므로 이스케이프하기 위함입니다.

**4단계 (변수 주입)**:
- `{reservation}` 자리에 실제 예약 데이터가 삽입됩니다.
- LangChain이 자동으로 이 치환을 처리합니다.

**예상 응답**:
```json
[
    {
        "name": "임섭순",
        "phone": "010-1234-5678",
        "date": "2025-11-15",
        "email1": "jslim9413@naver.com",
        "email2": "jslim9413@gmail.com"
    }
]
```

그러나 AI가 항상 순수한 JSON만 반환하는 것은 아닙니다. 때로는 이런 식으로 반환할 수 있습니다:

```
입력받은 텍스트에서 추출한 정보를 JSON 형식으로 정리하면 다음과 같습니다:

```json
[
    {
        "name": "임섭순",
        "phone": "010-1234-5678",
        "date": "2025-11-15",
        "email1": "jslim9413@naver.com",
        "email2": "jslim9413@gmail.com"
    }
]
```
```

이렇게 불필요한 설명 텍스트와 마크다운 코드 블록이 포함될 수 있습니다. 이제 정규표현식으로 이를 처리해야 합니다.

### 해결 방법 2: 정규표현식으로 JSON 추출

```python
# AI 응답을 받은 후
response = chain.run(reservation=reservation)
print('response -', response)

# 정규표현식으로 대괄호 안의 JSON만 추출
pattern = r'\[.*\]'  # 대괄호로 감싸진 부분만 추출
match = re.search(pattern, response, re.DOTALL)  # re.DOTALL: 줄바꿈 포함 모든 문자 매칭

if match:
    json_str = match.group(0)
    print('>>> json 형식 데이터 추출 성공')
    print(json_str)
    
    # JSON 문자열을 Python 객체로 변환
    data = json.loads(json_str)
    print('type:', type(data))  # <class 'list'>
    print('data:', data)
else:
    print('>>> json 형식 데이터 추출 실패')
```

#### 💻 코드 실행 상세 분석

**정규표현식 매칭 과정**:

**1단계 (패턴 정의)**:
- `r'\[.*\]'` 패턴 분석:
  - `\[`: 여는 대괄호 (메타문자 `[`를 리터럴로 사용하기 위해 이스케이프)
  - `.*`: 임의의 문자가 0개 이상 (greedy 방식으로 최대한 많이 매칭)
  - `\]`: 닫는 대괄호

**2단계 (re.DOTALL 플래그)**:
- 기본적으로 `.`은 줄바꿈(`\n`)을 매칭하지 않습니다.
- `re.DOTALL` 플래그를 사용하면 `.`이 줄바꿈도 포함한 모든 문자와 매칭됩니다.
- 이렇게 하면 여러 줄에 걸친 JSON도 정확히 추출할 수 있습니다.

**3단계 (매칭 확인)**:
- `match.group(0)`: 전체 매칭 결과를 반환합니다.
- 이것이 JSON 배열 문자열입니다.

**4단계 (JSON 파싱)**:
- `json.loads()`는 JSON 문자열을 Python 객체로 변환합니다.
- JSON 배열 `[...]`은 Python의 리스트로 변환됩니다.
- JSON 객체 `{...}`는 Python의 딕셔너리로 변환됩니다.

**최종 결과**:
```python
data = [
    {
        'name': '임섭순',
        'phone': '010-1234-5678',
        'date': '2025-11-15',
        'email1': 'jslim9413@naver.com',
        'email2': 'jslim9413@gmail.com'
    }
]
```

### 해결 방법 3: 더 정교한 JSON 추출

때로는 AI가 JSON을 중괄호로만 반환할 수도 있습니다. 이 경우 다른 패턴이 필요합니다:

```python
# 중괄호로 감싸진 JSON 객체 추출
pattern = r'json\s*(\{[\s\S]*?\})'  # 'json' 키워드 뒤의 중괄호 추출
match = re.search(pattern, response)

if match:
    result = match.group(1)  # 첫 번째 그룹 (중괄호 부분)
    print('result -', result)
    
    # JSON 문자열을 파싱
    data = json.loads(result)
    print('type -', type(data))  # <class 'dict'>
    print(data)
```

#### 💻 코드 실행 상세 분석

**고급 패턴 분석**:

**1단계 (패턴 구성 요소)**:
- `json`: 리터럴 문자열 "json"
- `\s*`: 0개 이상의 공백 문자 (줄바꿈 포함)
- `(...)`: 캡처 그룹 - 괄호 안의 매칭 결과를 별도로 추출할 수 있습니다
- `\{`: 여는 중괄호 (이스케이프)
- `[\s\S]*?`: 모든 문자(공백 포함)를 non-greedy 방식으로 매칭
- `\}`: 닫는 중괄호

**2단계 (Non-greedy vs Greedy)**:
- `.*`: greedy - 가능한 한 많이 매칭 (닫는 중괄호를 여러 개 만나면 마지막 것까지 매칭)
- `.*?`: non-greedy - 가능한 한 적게 매칭 (첫 번째 닫는 중괄호에서 멈춤)
- JSON이 중첩된 경우 non-greedy가 더 안전할 수 있습니다.

**3단계 (그룹 추출)**:
- `match.group(0)`: 전체 매칭 결과 (예: `json {...}`)
- `match.group(1)`: 첫 번째 캡처 그룹 (예: `{...}`)
- 캡처 그룹을 사용하면 "json" 키워드는 제외하고 JSON 부분만 추출할 수 있습니다.

### 해결 방법 4: 마크다운 코드 블록 제거

```python
# AI가 마크다운 코드 블록으로 감싼 경우
response = """
```json
{
    "name": "임섭순",
    "phone": "010-1234-5678"
}
```
"""

# 시작 부분의 ```json 또는 ``` 제거
answer = re.sub(r"^```[a-zA-Z]*\n?", "", response)
# 끝 부분의 ``` 제거
result = re.sub(r"```$", "", answer).strip()

print(result)
# {
#     "name": "임섭순",
#     "phone": "010-1234-5678"
# }

# 이제 파싱 가능
data = json.loads(result)
```

#### 💻 코드 실행 상세 분석

**마크다운 제거 프로세스**:

**1단계 (첫 번째 정규표현식)**:
- `r"^```[a-zA-Z]*\n?"` 패턴:
  - `^`: 문자열의 시작
  - ` ``` `: 세 개의 백틱
  - `[a-zA-Z]*`: 0개 이상의 알파벳 (언어 지정자, 예: `json`, `python`)
  - `\n?`: 선택적 줄바꿈
- 이는 마크다운 코드 블록의 시작 부분을 찾아 제거합니다.

**2단계 (두 번째 정규표현식)**:
- `r"```$"` 패턴:
  - ` ``` `: 세 개의 백틱
  - `$`: 문자열의 끝
- 코드 블록의 닫는 부분을 찾아 제거합니다.

**3단계 (공백 제거)**:
- `.strip()`: 양쪽 끝의 공백, 탭, 줄바꿈 등을 제거합니다.
- 이렇게 하면 순수한 JSON 텍스트만 남습니다.

**최종 결과**:
- 깨끗한 JSON 문자열이 생성되어 `json.loads()`로 파싱할 수 있습니다.

🔐 **보안 노트 - JSON 파싱**:
JSON 파싱 시 주의사항:
1. **JSON Injection 방지**: 신뢰할 수 없는 소스의 JSON을 파싱할 때는 검증이 필수입니다.
2. **DoS 공격 방지**: 매우 큰 JSON이나 깊게 중첩된 JSON은 파싱 시 메모리나 CPU를 과도하게 사용할 수 있습니다.
3. **데이터 타입 검증**: JSON 파싱 후에는 각 필드의 데이터 타입과 값의 범위를 검증해야 합니다.
4. **에러 처리**: `json.loads()`는 잘못된 JSON에 대해 `JSONDecodeError`를 발생시키므로, 반드시 try-except 블록으로 감싸야 합니다.

---

## 🛡️ Streamlit 보안 대시보드 개발

### 프로젝트 구조

오늘 강의에서 개발한 보안 대시보드는 다음과 같은 구조로 되어 있습니다:

```
llm/
├── data/
│   └── security_log.csv
├── streamlit_security_dashboard_app.py
└── plotly_security_dashboard_app.py
```

### 기본 대시보드 구현

```python
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

def ask_llm(frm):
    """DataFrame을 LLM에 전달하여 분석 요청"""
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
    st.set_page_config(page_title='보안 로그 분석 AI', layout='wide')
    st.title('LLM기반 관리자 대시보드')
    st.markdown('''
    - 보안로그 데이터를 기반으로 공격유형, 국가, 위험도 등을 분석하여 시각적으로 구현
    - LangChain과 RAG 기법을 활용하여 보안 관련 질문에 답변합니다.
    ''')
    
    # CSV 파일 업로드
    file = st.file_uploader("보안 로그 파일을 업로드하세요")
    if file:
        frm = pd.read_csv(file)
        st.dataframe(frm.head())
        
        if st.button('분석 요청'):
            with st.spinner('분석중....'):
                response = ask_llm(frm)
                
                try:
                    data = json.loads(response.choices[0].message.content.strip())
                    resultFrm = pd.DataFrame(data)
                    
                    st.subheader('분석 결과 데이터 확인')
                    st.dataframe(resultFrm)
                    
                    # 3개의 컬럼으로 시각화
                    typeCol, countryCol, riskCol = st.columns(3)
                    
                    with typeCol:
                        st.subheader('공격 유형 분포')
                        st.bar_chart(resultFrm['attack_type'].value_counts())
                    
                    with countryCol:
                        st.subheader('국가 분포')
                        st.bar_chart(resultFrm['country'].value_counts())
                    
                    with riskCol:
                        st.subheader('위험도 분포')
                        riskMean = resultFrm.groupby('attack_type')['risk_score'].mean()
                        st.bar_chart(riskMean)
                    
                    # 고위험 IP 필터링
                    st.subheader('고위험 IP 목록')
                    riskFrm = resultFrm[resultFrm['risk_score'] >= 7]
                    st.dataframe(riskFrm)
                    
                except Exception as e:
                    st.error(e)

if __name__ == "__main__":
    view()
```

#### 💻 코드 실행 상세 분석

**전체 애플리케이션 실행 흐름**:

**1단계 (Streamlit 앱 초기화)**:
- `st.set_page_config()`: 페이지 제목과 레이아웃을 설정합니다.
  - `layout='wide'`: 와이드 레이아웃을 사용하여 화면을 넓게 활용합니다.

**2단계 (파일 업로드)**:
- `st.file_uploader()`: 사용자가 파일을 업로드할 수 있는 위젯을 생성합니다.
- 파일이 업로드되면, `file` 변수에 파일 객체가 저장됩니다.
- `pd.read_csv(file)`: 업로드된 CSV 파일을 Pandas DataFrame으로 읽습니다.

**3단계 (데이터 미리보기)**:
- `st.dataframe(frm.head())`: DataFrame의 처음 5행을 인터랙티브 테이블로 표시합니다.
- 사용자는 데이터를 확인하고 분석을 계속할지 결정할 수 있습니다.

**4단계 (분석 요청 버튼)**:
- `st.button('분석 요청')`: 클릭 가능한 버튼을 생성합니다.
- 버튼이 클릭되면, `if` 블록 내부의 코드가 실행됩니다.
- `with st.spinner('분석중....'):`: 분석하는 동안 스피너(로딩 애니메이션)를 표시합니다.

**5단계 (LLM 호출)**:
- `ask_llm(frm)` 함수를 호출하여 DataFrame을 LLM에 전달합니다.
- LLM은 로그 데이터를 분석하여 JSON 형식으로 결과를 반환합니다.

**6단계 (응답 파싱)**:
- `response.choices[0].message.content.strip()`: LLM의 응답 텍스트를 추출하고, 앞뒤 공백을 제거합니다.
- `json.loads()`: JSON 문자열을 Python 리스트/딕셔너리로 변환합니다.
- `pd.DataFrame(data)`: JSON 데이터를 DataFrame으로 변환합니다.

**7단계 (시각화)**:
- `st.columns(3)`: 화면을 3개의 컬럼으로 나눕니다.
- 각 컬럼에서:
  - `with typeCol:` 블록 내부의 코드는 첫 번째 컬럼에 렌더링됩니다.
  - `st.bar_chart()`: 막대 차트를 생성합니다.
  - `value_counts()`: 각 값의 빈도를 계산합니다.

**8단계 (고위험 IP 필터링)**:
- `resultFrm[resultFrm['risk_score'] >= 7]`: Pandas의 Boolean 인덱싱을 사용합니다.
- 조건식 `resultFrm['risk_score'] >= 7`은 각 행에 대해 True/False 값을 가진 Series를 반환합니다.
- 이 Boolean Series를 인덱스로 사용하면 True인 행만 선택됩니다.

**9단계 (예외 처리)**:
- `try-except` 블록으로 JSON 파싱 오류나 기타 예외를 처리합니다.
- `st.error(e)`: 에러가 발생하면 사용자에게 빨간색으로 에러 메시지를 표시합니다.

### 예외 처리 강화

강사님께서 강조하신 점은 "코드를 견고하게 만드는 것도 보안의 일부"라는 것입니다:

```python
def view():
    # ... (앞부분 생략)
    
    if st.button('분석 요청'):
        with st.spinner('분석중....'):
            response = ask_llm(frm)
            
            try:
                # JSON 파싱 시도
                data = json.loads(response.choices[0].message.content.strip())
                resultFrm = pd.DataFrame(data)
                st.success('분석 완료!!')
                
                # 시각화 코드...
                
            except json.JSONDecodeError as e:
                st.error(f"JSON 파싱 오류: {e}")
                st.error("AI 응답이 올바른 JSON 형식이 아닙니다.")
            except KeyError as e:
                st.error(f"데이터 키 오류: {e}")
                st.error("필요한 데이터 필드가 없습니다.")
            except Exception as e:
                st.error(f"예상치 못한 오류: {e}")
```

#### 💻 코드 실행 상세 분석

**예외 처리의 중요성**:

**1단계 (JSON 파싱 예외)**:
- `json.JSONDecodeError`: JSON 문자열이 잘못된 형식일 때 발생합니다.
- 예: 쉼표 누락, 따옴표 불일치, 잘못된 이스케이프 시퀀스 등
- 이 예외를 잡아서 사용자에게 친절한 메시지를 보여줍니다.

**2단계 (KeyError 예외)**:
- `KeyError`: 딕셔너리에서 존재하지 않는 키에 접근할 때 발생합니다.
- 예: AI가 `attack_type` 대신 `attackType`으로 반환한 경우
- 이런 경우를 대비하여 예외를 잡고 적절히 처리합니다.

**3단계 (일반 예외)**:
- `Exception`: 예상치 못한 모든 예외를 잡습니다.
- 이는 "catch-all" 역할을 하며, 프로그램이 갑자기 중단되는 것을 방지합니다.

**보안 관점에서의 예외 처리**:
- **정보 노출 방지**: 예외 메시지에 민감한 정보(예: API 키, 파일 경로)가 포함되지 않도록 주의합니다.
- **로깅**: 프로덕션 환경에서는 예외를 로그 파일에 기록하여 나중에 분석할 수 있도록 합니다.
- **Graceful Degradation**: 일부 기능이 실패하더라도 앱 전체가 중단되지 않도록 합니다.

🔐 **보안 노트 - Streamlit 앱 보안**:
Streamlit 앱을 배포할 때 고려해야 할 보안 사항:
1. **API 키 관리**: `.env` 파일은 절대 Git에 올리지 않고, 배포 시 환경 변수로 설정합니다.
2. **파일 업로드 검증**: 업로드된 파일의 크기, 타입, 내용을 검증하여 악의적인 파일을 차단합니다.
3. **입력 검증**: 사용자 입력을 신뢰하지 말고, 항상 검증하고 새니타이징합니다.
4. **HTTPS 사용**: 배포 시 반드시 HTTPS를 사용하여 데이터 전송을 암호화합니다.
5. **인증 및 권한**: 민감한 데이터를 다루는 앱은 인증 및 권한 관리를 구현해야 합니다.

---

## 🗺️ Plotly를 이용한 지도 시각화

### Plotly 설치 및 설정

```bash
pip install plotly
```

### 지도 시각화 코드

```python
import plotly.express as px

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

def view():
    # ... (앞부분 동일)
    
    # 지도 시각화 추가
    st.subheader('공격 위치 지도(위험도 색상표시)')
    fig = px.scatter_geo(
        resultFrm,
        lat='latitude',
        lon='longitude',
        color='risk_score',
        hover_name='ip',
        hover_data=['country', 'attack_type'],
        title='Attack Map',
        projection='natural earth',
        color_continuous_scale='Reds',
        size='risk_score'
    )
    st.plotly_chart(fig, use_container_width=True)
```

#### 💻 코드 실행 상세 분석

**Plotly 지도 시각화 과정**:

**1단계 (데이터 준비)**:
- AI에게 위도(latitude)와 경도(longitude) 정보를 포함하도록 요청합니다.
- 예: 한국의 경우 `latitude: 37.5`, `longitude: 127.0` (서울 중심 좌표)

**2단계 (px.scatter_geo 함수)**:
- `scatter_geo`는 지리적 좌표에 점을 찍는 산점도를 생성합니다.
- 주요 파라미터:
  - `lat`, `lon`: DataFrame의 위도/경도 컬럼 이름
  - `color`: 점의 색상을 결정할 컬럼 (여기서는 `risk_score`)
  - `hover_name`: 마우스를 올렸을 때 표시될 주요 정보 (여기서는 `ip`)
  - `hover_data`: 추가로 표시될 정보들 (리스트)

**3단계 (시각화 옵션)**:
- `projection='natural earth'`: 지도 투영법을 설정합니다.
  - 다른 옵션: `'orthographic'` (지구본 모양), `'mercator'` (일반적인 지도)
- `color_continuous_scale='Reds'`: 색상 스케일을 빨간색 계열로 설정합니다.
  - 낮은 위험도는 연한 빨강, 높은 위험도는 진한 빨강으로 표시됩니다.
- `size='risk_score'`: 점의 크기를 위험도에 비례하게 설정합니다.

**4단계 (Streamlit 렌더링)**:
- `st.plotly_chart(fig, use_container_width=True)`: Plotly 차트를 Streamlit에 표시합니다.
- `use_container_width=True`: 차트가 컨테이너 너비에 맞게 자동으로 조정됩니다.

**인터랙티브 기능**:
- **줌**: 마우스 휠로 확대/축소 가능
- **팬**: 드래그하여 지도 이동
- **호버**: 점 위에 마우스를 올리면 상세 정보 표시
- **다운로드**: 차트 오른쪽 상단의 카메라 아이콘으로 이미지 저장 가능

💡 **중요!**: 강사님께서 "지도 시각화는 글로벌 보안 모니터링에서 매우 효과적"이라고 강조하셨습니다. 공격의 지리적 분포를 한눈에 파악할 수 있어, 특정 지역에서 집중적으로 발생하는 공격을 빠르게 식별할 수 있습니다.

### 위도/경도 데이터 처리

AI가 항상 정확한 위도/경도를 제공하는 것은 아니므로, 검증과 보정이 필요할 수 있습니다:

```python
# 국가별 중심 좌표 딕셔너리
COUNTRY_COORDS = {
    'South Korea': {'latitude': 37.5665, 'longitude': 126.9780},
    'United States': {'latitude': 37.0902, 'longitude': -95.7129},
    'China': {'latitude': 35.8617, 'longitude': 104.1954},
    'Russia': {'latitude': 61.5240, 'longitude': 105.3188},
    # ... 더 많은 국가들
}

# AI 응답 후 좌표 보정
for idx, row in resultFrm.iterrows():
    country = row['country']
    if country in COUNTRY_COORDS:
        resultFrm.at[idx, 'latitude'] = COUNTRY_COORDS[country]['latitude']
        resultFrm.at[idx, 'longitude'] = COUNTRY_COORDS[country]['longitude']
    else:
        # 기본 좌표 설정 (또는 경고 표시)
        resultFrm.at[idx, 'latitude'] = 0
        resultFrm.at[idx, 'longitude'] = 0
```

#### 💻 코드 실행 상세 분석

**좌표 보정 프로세스**:

**1단계 (딕셔너리 준비)**:
- 주요 국가들의 중심 좌표를 미리 딕셔너리에 저장합니다.
- 이는 AI가 잘못된 좌표를 제공하거나 좌표를 제공하지 않을 경우의 fallback입니다.

**2단계 (DataFrame 순회)**:
- `iterrows()`를 사용하여 각 행을 순회합니다.
- `idx`는 인덱스, `row`는 Series 객체입니다.

**3단계 (좌표 검증 및 보정)**:
- 국가명이 딕셔너리에 있으면, 해당 좌표로 업데이트합니다.
- `resultFrm.at[idx, 'latitude']`: 특정 행의 특정 컬럼 값을 업데이트합니다.

**4단계 (기본값 설정)**:
- 국가명을 찾을 수 없으면 (0, 0) 좌표를 설정하거나, 경고를 표시합니다.
- (0, 0)은 대서양 한가운데(아프리카 서쪽 해안 근처)입니다.

🔐 **보안 노트 - 데이터 검증**:
외부 소스(여기서는 AI)로부터 받은 좌표 데이터는 다음과 같이 검증해야 합니다:
1. **범위 검증**: 위도는 -90 ~ 90, 경도는 -180 ~ 180 범위 내에 있어야 합니다.
2. **데이터 타입 검증**: 좌표는 숫자형이어야 합니다.
3. **NULL 체크**: 좌표가 누락되지 않았는지 확인합니다.
4. **이상치 탐지**: 예를 들어, 한국의 공격인데 좌표가 미국으로 나오면 이상한 것입니다.

---

## 🧩 복합 예제: RAG 기반 보안 도서관 챗봇

### RAG (Retrieval-Augmented Generation) 이해

RAG는 LLM이 외부 지식 베이스를 참조하여 답변하도록 하는 기법입니다. 이는 다음과 같은 장점이 있습니다:

1. **최신 정보 제공**: LLM의 학습 데이터 이후의 정보도 제공 가능
2. **도메인 특화**: 특정 분야(예: 회사 내부 보안 정책)의 정보를 학습시킬 수 있음
3. **환각(Hallucination) 감소**: 실제 문서를 참조하므로 잘못된 정보를 생성할 가능성이 줄어듦

### RAG 챗봇 구현

```python
import os
from dotenv import load_dotenv
import streamlit as st

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores      import FAISS
from langchain.text_splitter     import CharacterTextSplitter
from langchain.chat_models       import ChatOpenAI
from langchain.chains            import RetrievalQA

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 지식 베이스 (예: Python 자료형에 대한 설명)
doc = [
    '리스트는 파이썬에서 변경 가능한(mutable) 자료형으로, 요소를 추가하거나 삭제할 수 있습니다.',
    '튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다.',
    '딕셔너리는 키(key)와 값(value)의 쌍으로 데이터를 저장합니다.'
]

def ask_gpt():
    # 문서를 청크(chunk) 단위로 분할
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.create_documents(doc)
    
    # OpenAI 임베딩 모델 초기화
    embeddings = OpenAIEmbeddings(
        openai_api_key=api_key,
        model='text-embedding-3-small'
    )
    
    # FAISS 벡터 스토어 생성
    db = FAISS.from_documents(texts, embeddings)
    
    # 리트리버 설정 (상위 1개 문서 검색)
    retriever = db.as_retriever(search_kwargs={"k": 1})
    
    # RetrievalQA 체인 생성
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-4o-mini", temperature=0.9),
        chain_type="stuff",
        retriever=retriever
    )
    
    return qa, retriever

def view():
    st.title('LangChain + RAG 도서관 사서봇')
    
    query = st.text_input('질문을 입력하세요 : ')
    if query:
        with st.spinner('외부 데이터베이스를 검색하고 있습니다...'):
            qa, retriever = ask_gpt()
            answer = qa.run(query)
            st.success(' A - ' + answer)
            
            # 참조한 문서도 표시
            st.caption(' R - ' + retriever.get_relevant_documents(query)[0].page_content)

if __name__ == "__main__":
    view()
```

#### 💻 코드 실행 상세 분석

**RAG 파이프라인 단계별 분석**:

**1단계 (문서 청킹)**:
- `CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)`:
  - `chunk_size`: 각 청크의 최대 문자 수
  - `chunk_overlap`: 인접한 청크 간의 겹치는 문자 수 (0이면 겹치지 않음)
- `create_documents(doc)`: 문자열 리스트를 Document 객체 리스트로 변환합니다.
- 청킹은 긴 문서를 처리 가능한 크기로 나누기 위한 것입니다.

**2단계 (임베딩 생성)**:
- `OpenAIEmbeddings()`: OpenAI의 임베딩 모델을 사용합니다.
- `model='text-embedding-3-small'`: 작고 빠른 임베딩 모델을 사용합니다.
- 임베딩은 텍스트를 고차원 벡터로 변환하는 과정입니다.
- 의미적으로 유사한 텍스트는 벡터 공간에서 가까이 위치합니다.

**3단계 (벡터 스토어 생성)**:
- `FAISS.from_documents(texts, embeddings)`:
  - 각 문서를 임베딩하여 벡터로 변환합니다.
  - 이 벡터들을 FAISS 인덱스에 저장합니다.
  - FAISS는 빠른 유사도 검색을 위한 라이브러리입니다.

**4단계 (리트리버 설정)**:
- `db.as_retriever(search_kwargs={"k": 1})`:
  - 벡터 스토어를 리트리버로 변환합니다.
  - `k=1`: 가장 유사한 상위 1개의 문서만 검색합니다.

**5단계 (QA 체인 생성)**:
- `RetrievalQA.from_chain_type()`:
  - `llm`: 답변 생성에 사용할 LLM
  - `chain_type="stuff"`: 검색된 모든 문서를 프롬프트에 포함시키는 방식
  - `retriever`: 문서 검색을 담당하는 리트리버

**6단계 (질문 처리)**:
- 사용자가 질문을 입력하면:
  1. 질문이 임베딩으로 변환됩니다.
  2. FAISS에서 가장 유사한 문서를 검색합니다.
  3. 검색된 문서와 질문을 함께 LLM에 전달합니다.
  4. LLM이 문서를 참조하여 답변을 생성합니다.

**7단계 (결과 표시)**:
- `qa.run(query)`: 최종 답변을 반환합니다.
- `retriever.get_relevant_documents(query)`: 참조한 문서를 반환합니다.
- 사용자는 답변과 함께 어떤 문서를 참조했는지 확인할 수 있습니다.

### RAG 작동 예시

**질문**: "튜플은 수정할 수 있나요?"

**RAG 처리 과정**:
1. **임베딩**: 질문 "튜플은 수정할 수 있나요?"를 벡터로 변환
2. **검색**: 벡터 스토어에서 가장 유사한 문서 검색
   - 결과: "튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다."
3. **프롬프트 구성**:
   ```
   Context: 튜플은 변경 불가능한(immutable) 자료형으로, 한 번 생성하면 수정할 수 없습니다.
   Question: 튜플은 수정할 수 있나요?
   Answer:
   ```
4. **답변 생성**: LLM이 컨텍스트를 참조하여 답변 생성
   - "아니요, 튜플은 변경 불가능한(immutable) 자료형이므로 한 번 생성하면 수정할 수 없습니다."

💡 **중요!**: 강사님께서 "RAG는 회사 내부 보안 정책이나 매뉴얼을 학습시켜 직원들의 질문에 자동으로 답변하는 챗봇을 만들 때 매우 유용하다"고 강조하셨습니다.

🔐 **보안 노트 - RAG 시스템**:
RAG 시스템을 구축할 때 고려해야 할 보안 사항:
1. **데이터 접근 제어**: 민감한 문서는 권한이 있는 사용자만 검색할 수 있도록 제한해야 합니다.
2. **Prompt Injection 방지**: 사용자 질문이 시스템 프롬프트를 조작하지 못하도록 검증해야 합니다.
3. **데이터 암호화**: 벡터 스토어에 저장되는 문서가 민감한 경우, 암호화가 필요할 수 있습니다.
4. **로깅 및 모니터링**: 누가 어떤 질문을 했고, 어떤 문서를 검색했는지 로그를 남겨야 합니다.
5. **데이터 유출 방지**: LLM이 문서의 내용을 그대로 출력하지 않고, 요약이나 해석만 제공하도록 프롬프트를 설계해야 합니다.

---

## 🎯 학습 정리 및 프로젝트 아이디어

### 오늘 배운 핵심 내용

1. **정규표현식**: 문자열 패턴 매칭, 추출, 치환의 핵심 도구
2. **LLM Temperature**: 출력의 다양성과 일관성을 조절하는 파라미터
3. **LangChain**: LLM을 더 쉽게 활용할 수 있는 프레임워크
4. **RAG**: 외부 지식 베이스를 참조하여 답변하는 기법
5. **Streamlit**: 빠르게 웹 앱을 만들 수 있는 프레임워크
6. **Plotly**: 인터랙티브한 지도 시각화 라이브러리
7. **데이터 전처리**: AI 응답을 실제로 사용 가능한 형태로 가공하는 기술

### 프로젝트 아이디어

강사님께서 제안하신 프로젝트 진행 방법:

**단계 1: 아이디어 구상**
- 해결하고 싶은 문제나 분석하고 싶은 주제를 정합니다.
- 예: "우리 회사의 웹 서버 로그를 분석하여 비정상적인 접근 패턴을 탐지하고 싶다"

**단계 2: 데이터 준비**
- 실제 데이터가 없다면 AI에게 요청합니다:
  ```
  "웹 서버 보안 로그 데이터를 CSV 형식으로 100건 만들어줘.
  컬럼은 timestamp, ip, url, method, status_code, user_agent가 있어야 하고,
  그 중 10%는 SQL Injection 시도, 5%는 XSS 시도가 포함되어야 해."
  ```
- AI가 생성한 가상 데이터로 프로토타입을 만듭니다.

**단계 3: 분석 및 시각화**
- Streamlit으로 대시보드를 만듭니다.
- LLM을 활용하여 로그를 분석하고 인사이트를 추출합니다.
- Plotly나 다른 시각화 라이브러리로 결과를 시각화합니다.

**단계 4: RAG 추가 (선택사항)**
- 보안 정책 문서나 매뉴얼을 지식 베이스로 추가합니다.
- 사용자가 보안 관련 질문을 하면 RAG를 통해 답변합니다.

### 프로젝트 예시

```python
# 가상 데이터 생성 프롬프트
prompt = """
웹 서버 보안 로그 데이터를 CSV 형식으로 생성해줘.
총 100건의 로그가 필요하며, 다음 컬럼이 포함되어야 해:
- timestamp: 2025-11-01부터 2025-11-12까지의 랜덤 시간
- ip: 랜덤 IP 주소
- url: 접근한 URL
- method: GET, POST, PUT, DELETE 중 하나
- status_code: HTTP 상태 코드 (200, 404, 500 등)
- user_agent: 브라우저 정보
- attack_type: "Normal", "SQL Injection", "XSS", "Path Traversal" 중 하나
- risk_score: 1-10 사이의 위험도 점수

다음 비율로 공격 유형을 분포시켜줘:
- Normal: 80%
- SQL Injection: 10%
- XSS: 5%
- Path Traversal: 5%

CSV 형식으로만 출력하고 다른 설명은 포함하지 마.
"""
```

이렇게 AI에게 요청하면 프로젝트에 바로 사용할 수 있는 CSV 데이터를 받을 수 있습니다!

---

## 🔍 고급 주제: 보안 관점에서의 코드 리뷰

### 입력 검증의 중요성

```python
def validate_dataframe(df, required_columns):
    """DataFrame의 구조와 데이터를 검증합니다."""
    # 1. 필수 컬럼 확인
    missing_cols = set(required_columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"필수 컬럼 누락: {missing_cols}")
    
    # 2. 데이터 타입 검증
    if 'risk_score' in df.columns:
        if not pd.api.types.is_numeric_dtype(df['risk_score']):
            raise TypeError("risk_score는 숫자형이어야 합니다.")
        
        # 3. 값의 범위 검증
        if (df['risk_score'] < 1).any() or (df['risk_score'] > 10).any():
            raise ValueError("risk_score는 1-10 사이여야 합니다.")
    
    # 4. NULL 값 확인
    if df.isnull().any().any():
        raise ValueError("NULL 값이 포함되어 있습니다.")
    
    return True
```

#### 💻 코드 실행 상세 분석

**입력 검증 단계**:

**1단계 (컬럼 검증)**:
- `set(required_columns) - set(df.columns)`: 집합 연산으로 누락된 컬럼을 찾습니다.
- 필수 컬럼이 없으면 `ValueError`를 발생시킵니다.

**2단계 (데이터 타입 검증)**:
- `pd.api.types.is_numeric_dtype()`: 컬럼이 숫자형인지 확인합니다.
- 숫자형이어야 하는 컬럼이 문자열이면 `TypeError`를 발생시킵니다.

**3단계 (값의 범위 검증)**:
- `(df['risk_score'] < 1).any()`: 1보다 작은 값이 있는지 확인합니다.
- `.any()`: 하나라도 True이면 True를 반환합니다.
- 범위를 벗어난 값이 있으면 `ValueError`를 발생시킵니다.

**4단계 (NULL 값 확인)**:
- `df.isnull()`: 각 셀이 NULL인지 Boolean DataFrame을 반환합니다.
- `.any().any()`: 행 방향으로 any(), 그 결과에 다시 any()를 적용합니다.
- NULL 값이 있으면 `ValueError`를 발생시킵니다.

**사용 예시**:
```python
try:
    validate_dataframe(resultFrm, ['ip', 'country', 'attack_type', 'risk_score'])
    st.success("데이터 검증 완료!")
except (ValueError, TypeError) as e:
    st.error(f"데이터 검증 실패: {e}")
```

### API 요청 제한 (Rate Limiting)

```python
import time
from functools import wraps

def rate_limit(max_calls=5, time_window=60):
    """API 호출을 제한하는 데코레이터"""
    calls = []
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            # 시간 윈도우 밖의 호출 기록 제거
            calls[:] = [c for c in calls if c > now - time_window]
            
            if len(calls) >= max_calls:
                raise Exception(f"API 호출 제한 초과: {time_window}초당 최대 {max_calls}번")
            
            calls.append(now)
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@rate_limit(max_calls=5, time_window=60)
def ask_llm(frm):
    """Rate limiting이 적용된 LLM 호출"""
    # ... LLM 호출 코드
    pass
```

#### 💻 코드 실행 상세 분석

**Rate Limiting 동작 원리**:

**1단계 (데코레이터 구조)**:
- `rate_limit()`은 데코레이터 팩토리입니다.
- 이는 파라미터를 받아서 실제 데코레이터를 반환합니다.

**2단계 (호출 기록 관리)**:
- `calls` 리스트는 각 함수 호출의 타임스탬프를 저장합니다.
- 오래된 호출 기록(시간 윈도우 밖)은 제거됩니다.
- 리스트 슬라이싱 `calls[:]`을 사용하여 원본 리스트를 수정합니다.

**3단계 (제한 검사)**:
- 현재 시간 윈도우 내의 호출 횟수를 확인합니다.
- 제한을 초과하면 예외를 발생시킵니다.

**4단계 (호출 실행)**:
- 제한 내라면, 현재 시간을 기록하고 원래 함수를 실행합니다.

**실제 적용**:
```python
# 사용자가 짧은 시간에 여러 번 분석 버튼을 클릭해도
# API 호출은 60초당 최대 5번으로 제한됩니다.
try:
    response = ask_llm(frm)
except Exception as e:
    st.warning(str(e))
    st.info("잠시 후 다시 시도해주세요.")
```

🔐 **보안 노트**: Rate limiting은 다음을 방지합니다:
- **비용 초과**: API 비용이 급증하는 것을 방지
- **DoS 공격**: 악의적인 사용자가 시스템을 과부하시키는 것을 방지
- **공정한 사용**: 모든 사용자가 공평하게 리소스를 사용할 수 있도록 보장

---

## 📚 추가 학습 자료 및 권장 사항

### 정규표현식 연습 사이트
- **Regex101** (https://regex101.com/): 실시간으로 정규표현식을 테스트하고 설명을 볼 수 있습니다.
- **RegexOne** (https://regexone.com/): 인터랙티브한 정규표현식 튜토리얼

### LangChain 공식 문서
- **LangChain Documentation** (https://python.langchain.com/): 최신 사용법과 예제
- **LangChain Cookbook** (https://github.com/langchain-ai/langchain/tree/master/cookbook): 다양한 실전 예제

### Streamlit 학습
- **Streamlit Documentation** (https://docs.streamlit.io/): 공식 문서
- **Streamlit Gallery** (https://streamlit.io/gallery): 다양한 앱 예제

### 보안 관련 추천 도서
- 강의에서 제공된 앵무새 로봇 표지의 책: LLM 활용 예제가 풍부합니다.

### 실습 팁

강사님께서 강조하신 실습 팁:

1. **소스코드 활용**: 제공된 책의 소스코드를 다운로드하여 직접 실행해보세요.
2. **트러블슈팅 연습**: 에러가 발생하면 당황하지 말고, 에러 메시지를 읽고 해결해보세요.
3. **패키지 버전 확인**: 라이브러리 버전이 다르면 코드가 작동하지 않을 수 있습니다.
4. **점진적 개선**: 한 번에 완벽한 코드를 작성하려 하지 말고, 작동하는 프로토타입부터 만들어보세요.

---

## 🎓 총정리 및 다음 단계

### 3일차 학습 요약

오늘 우리는 다음과 같은 여정을 거쳤습니다:

1. **정규표현식의 기초부터 실전 활용**까지 학습했습니다.
2. **LLM과 LangChain을 통합**하여 실제 문제를 해결하는 방법을 배웠습니다.
3. **보안 로그 분석 대시보드**를 Streamlit으로 구현했습니다.
4. **Plotly를 이용한 지도 시각화**로 글로벌 보안 위협을 시각화했습니다.
5. **RAG 기법**으로 외부 지식 베이스를 활용하는 챗봇을 만들었습니다.
6. **데이터 전처리와 검증**의 중요성을 배웠습니다.
7. **보안 관점에서의 코드 리뷰** 방법을 익혔습니다.

### 내일 학습 예고

강사님께서 말씀하신 내일의 주제:

1. **CSV 데이터 생성부터 시각화까지**: AI에게 데이터를 생성하도록 요청하고, 이를 분석하고 시각화하는 전체 파이프라인을 구축합니다.
2. **프로젝트 준비**: 금요일부터는 팀별 아이디어 투어와 프로젝트 기획이 시작됩니다.

### 프로젝트를 위한 체크리스트

- [ ] 팀 구성 및 역할 분담
- [ ] 해결하고 싶은 문제 정의
- [ ] 필요한 데이터 확인 (또는 생성 계획)
- [ ] 기술 스택 선정 (Streamlit, Plotly, LangChain 등)
- [ ] 프로토타입 계획 수립
- [ ] 발표 자료 구성 계획

### 강사님의 마지막 조언

"여러분이 지금 배우고 있는 것들은 단순한 코딩이 아닙니다. 보안 전문가로서 AI를 활용하는 능력, 데이터를 분석하는 능력, 그리고 문제를 해결하는 능력입니다. 완벽하게 이해하지 못했더라도 괜찮습니다. 듣는 것만으로도 여러분의 시야가 넓어지고 있습니다. 중요한 것은 끝까지 포기하지 않고 계속 도전하는 것입니다."

---

## 🎯 마무리 퀴즈

스스로 학습을 점검해보세요:

1. **정규표현식** `\d{3}-\d{4}-\d{4}`는 무엇을 매칭하나요?
2. **Temperature 파라미터**가 0과 1일 때의 차이는 무엇인가요?
3. **LangChain의 체인(Chain)**이란 무엇인가요?
4. **RAG의 주요 장점** 3가지는 무엇인가요?
5. **Streamlit에서 예외 처리**가 왜 중요한가요?
6. **Plotly의 scatter_geo 함수**에서 `color` 파라미터의 역할은 무엇인가요?

### 정답 및 해설

1. **전화번호 형식**: 3자리-4자리-4자리 패턴의 숫자를 매칭합니다. (예: 010-1234-5678)

2. **Temperature 차이**:
   - Temperature = 0: 가장 확률이 높은 토큰을 항상 선택 (일관성↑, 창의성↓)
   - Temperature = 1: 확률 분포대로 샘플링 (일관성↓, 창의성↑)

3. **LangChain 체인**: 여러 작업(프롬프트 생성, LLM 호출, 문서 검색 등)을 순차적으로 연결하여 복잡한 워크플로우를 구성하는 구조입니다.

4. **RAG 장점**:
   - 최신 정보를 제공할 수 있음
   - 도메인 특화 지식을 활용할 수 있음
   - 환각(Hallucination)을 줄일 수 있음

5. **Streamlit 예외 처리**: 앱이 예상치 못한 에러로 중단되는 것을 방지하고, 사용자에게 친절한 에러 메시지를 보여주며, 보안 취약점을 줄이기 위해 필수적입니다.

6. **Plotly color 파라미터**: 점의 색상을 결정할 데이터 컬럼을 지정합니다. 연속형 데이터의 경우 색상 그라데이션으로 표현되어, 예를 들어 위험도를 시각적으로 구분할 수 있게 해줍니다.

---

## 📝 추가 노트 및 팁

### 강의 중 자주 나온 질문들

**Q: AI가 항상 JSON 형식을 지키지 않는데 어떻게 하나요?**
A: 프롬프트를 더 강하게 작성하고 (예: "절대 다른 텍스트 포함하지 마"), `response_format={'type': 'json_object'}` 옵션을 사용하며, 정규표현식으로 후처리하는 3중 안전장치를 사용하세요.

**Q: 정규표현식이 너무 어려운데 꼭 배워야 하나요?**
A: 네, 보안 분야에서 로그 분석, 데이터 클린징, 패턴 탐지 등에 필수적입니다. 처음에는 간단한 패턴부터 시작하여 점진적으로 복잡한 패턴을 익히세요.

**Q: Streamlit과 Flask/Django의 차이는 무엇인가요?**
A: Streamlit은 데이터 앱과 대시보드를 빠르게 만들기 위한 도구로, 프론트엔드 코드 없이 Python만으로 웹 앱을 만들 수 있습니다. Flask/Django는 더 복잡한 웹 애플리케이션을 만들기 위한 풀스택 프레임워크입니다.

### 실습 시 주의사항

1. **API 키 관리**: 절대 Git에 올리지 말고, `.gitignore`에 `.env` 추가
2. **패키지 버전**: 강의 자료와 다른 버전을 사용하면 에러가 날 수 있음
3. **파일 경로**: 절대 경로보다는 상대 경로 사용 권장
4. **데이터 백업**: 중요한 데이터는 항상 백업
5. **점진적 테스트**: 한 번에 많은 기능을 추가하지 말고, 작은 단위로 테스트

### 성능 최적화 팁

```python
# DataFrame 처리 최적화
@st.cache_data  # Streamlit의 캐싱 데코레이터
def load_data(file):
    """데이터 로딩을 캐싱하여 성능 향상"""
    return pd.read_csv(file)

# LLM 호출 최적화
@st.cache_data(ttl=3600)  # 1시간 동안 캐싱
def analyze_logs(data_hash):
    """같은 데이터에 대한 중복 API 호출 방지"""
    # ... LLM 호출 코드
    pass
```

---

**📌 학습 완료!** 

오늘 배운 내용을 바탕으로 여러분만의 보안 대시보드를 만들어보세요. 질문이 있으면 언제든지 강사님께 여쭤보시고, 동료들과 함께 문제를 해결해보세요. 내일 더 발전된 모습으로 만나요! 💪

---

**작성자**: 강의 노트 정리  
**날짜**: 2025년 11월 12일  
**강의**: LLM & LangChain 보안 대시보드 개발 (3일차)  
**참고 자료**: 강의 STT, Jupyter Notebook, Python 코드 파일들
