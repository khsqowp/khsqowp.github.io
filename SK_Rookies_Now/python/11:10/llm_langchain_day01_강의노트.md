# 📝 생성형 AI, LangChain, RAG 첫걸음 강의 노트 (1일차)

오늘 강의에서는 드디어 3주차 수업에 접어들며, 생성형 AI의 세계로 첫발을 내딛는 시간을 가졌습니다. 지난주까지 데이터 분석과 시각화의 기초를 다졌다면, 이번 주부터는 그 기술들을 바탕으로 **LangChain**, **RAG**, 그리고 **Streamlit**을 결합하여 직접 AI 애플리케이션을 만들어보는 흥미진진한 여정이 시작됩니다. 강사님께서는 본격적인 실습에 앞서, 우리가 왜 이 기술들을 배워야 하는지, 그리고 이 기술들이 어떤 배경에서 등장했는지에 대한 깊이 있는 설명을 해주셨습니다.

> 💡 **이번 주 학습 목표**
> 1.  **생성형 AI 활용법 이해**: 단순히 API를 호출하는 것을 넘어, 그 원리와 구조를 파악합니다.
> 2.  **LLM 개발을 위한 가상환경 구축**: 버전 충돌 없는 안정적인 개발 환경을 직접 구성합니다.
> 3.  **LangChain + RAG 활용**: LLM의 한계를 극복하고 외부 지식을 활용하는 RAG의 개념을 배우고 LangChain으로 구현합니다.
> 4.  **Streamlit 연동**: 우리가 만든 AI 모델을 웹 애플리케이션으로 시각화하고 직접 상호작용하는 경험을 합니다.

---

## 1. 왜 생성형 AI를 배워야 하는가? (The "Why")

강사님께서는 기술을 배우기에 앞서 '왜?'라는 질문을 던지는 것이 매우 중요하다고 강조하셨습니다. 우리가 앞으로 다룰 LangChain과 RAG가 어떤 문제를 해결하기 위해 등장했는지 이해한다면, 기술을 훨씬 깊이 있게 활용할 수 있기 때문입니다.

### 1.1. 모든 것의 시작: AI, 머신러닝, 딥러닝

오늘날 AI는 우리 삶 곳곳에 스며들었지만, 그 시작과 발전에 대해 명확히 이해하는 것이 중요합니다. 강사님께서는 2016년, 이세돌 9단과 알파고의 대국을 기점으로 대한민국에서 인공지능에 대한 대중적 관심이 폭발적으로 증가했다고 설명하셨습니다.

> 📌 **노트: AI, 머신러닝, 딥러닝의 포함 관계**
> 많은 사람들이 AI와 딥러닝을 동일한 개념으로 생각하지만, 이는 잘못된 이해입니다. 강사님께서는 세 개념의 관계를 명확히 정리해주셨습니다.
> -   **AI (Artificial Intelligence, 인공지능)**: 가장 포괄적인 개념으로, 인간의 지능을 모방하는 모든 기술을 의미합니다.
> -   **ML (Machine Learning, 기계학습)**: AI의 한 분야로, 명시적인 규칙 없이 **데이터를 기반으로 패턴을 학습**하여 결과를 추론하는 알고리즘 기법입니다.
> -   **DL (Deep Learning, 딥러닝)**: 머신러닝의 한 분야로, 인간의 뇌 신경망을 모방한 **인공신경망(Artificial Neural Network)**을 활용하여 더 깊게 학습하는 알고리즘입니다.

우스갯소리로 "기계학습보다 좀 더 딥(deep)하게 학습하면 딥러닝"이라는 강사님의 설명처럼, 딥러닝은 인공신경망이라는 복잡한 구조를 통해 기계학습의 성능을 한 단계 끌어올린 기술입니다.

### 1.2. 딥러닝의 두 갈래: CNN과 RNN

딥러닝이 발전하면서, 처리하는 데이터의 종류에 따라 특화된 신경망 구조가 등장했습니다.

-   **CNN (Convolutional Neural Network, 합성곱 신경망)**: 주로 **이미지 처리**에 사용됩니다. 이미지의 공간적 특징(점, 선, 면 등)을 효과적으로 추출하여 객체를 인식하거나 분류하는 데 뛰어난 성능을 보입니다.
-   **RNN (Recurrent Neural Network, 순환 신경망)**: **순서가 있는 데이터(Sequence Data)**, 즉 **자연어(텍스트)나 시계열 데이터** 처리에 특화되어 있습니다. 이전 단계의 정보를 기억하여 다음 단계의 예측에 활용하는 '순환' 구조를 가지고 있어 문맥을 파악하는 데 유리합니다.

### 1.3. LLM의 등장과 명확한 한계

오늘날 생성형 AI의 핵심인 **LLM (Large Language Model, 거대 언어 모델)**은 바로 이 **RNN** 기술이 발전하여 탄생한 것입니다. 수많은 텍스트 데이터를 학습하여 인간처럼 자연스러운 문장을 생성하고 이해할 수 있게 된 것이죠.

하지만 강사님께서는 LLM이 만능이 아니며, 명확한 한계점을 가지고 있다고 강조하셨습니다.

> 💡 **중요! LLM의 핵심 문제점**
> 1.  **최신성 부족**: LLM은 특정 시점까지의 데이터로 **사전 학습(Pre-trained)**된 모델입니다. 따라서 학습 시점 이후의 최신 정보나 사건에 대해서는 알지 못합니다.
> 2.  **환각 (Hallucination)**: 모델이 학습하지 않은 내용이나 잘못된 정보를 마치 사실인 것처럼 그럴듯하게 생성하는 현상입니다. 이는 LLM이 '이해'해서 답변하는 것이 아니라, 학습한 데이터의 통계적 확률에 기반하여 단어를 예측하기 때문에 발생합니다.
> 3.  **비용 문제**: 이러한 한계를 극복하기 위해 추가적인 데이터를 학습시키는 **파인 튜닝(Fine-tuning)**을 할 수 있지만, 이는 엄청난 양의 데이터와 컴퓨팅 자원, 즉 막대한 비용을 필요로 합니다.

### 1.4. 한계를 극복하는 열쇠, RAG (Retrieval-Augmented Generation)

이러한 LLM의 한계를 비교적 저렴하고 효과적으로 보완하기 위해 등장한 기술이 바로 **RAG (Retrieval-Aumented Generation, 검색 증강 생성)**입니다.

-   **검색 (Retrieval)**: 사용자의 질문과 관련된 정보를 외부 데이터 소스(DB, 문서, API 등)에서 실시간으로 **검색**합니다.
-   **증강 (Augmented)**: 검색된 최신 정보를 기존의 프롬프트에 **추가(증강)**하여 LLM에게 전달합니다.
-   **생성 (Generation)**: LLM은 보강된 정보를 바탕으로 훨씬 더 정확하고 사실에 기반한 답변을 **생성**합니다.

쉽게 말해, LLM에게 '오픈북 시험'을 볼 수 있게 해주는 기술입니다. LLM이 모든 것을 외우고 있지 않아도, RAG를 통해 최신 정보나 내부 데이터를 참고하여 답변을 생성할 수 있게 되는 것입니다.

### 1.5. RAG의 핵심, 임베딩과 벡터 DB

RAG가 외부 문서를 검색하기 위해서는 컴퓨터가 텍스트의 '의미'를 이해하고 비교할 수 있어야 합니다. 이 과정에서 **임베딩(Embedding)**과 **벡터 DB(Vector Database)**라는 핵심 개념이 사용됩니다.

-   **임베딩 (Embedding)**: 인공지능은 텍스트를 직접 이해할 수 없기 때문에, 문장이나 단어를 **숫자로 된 벡터(Vector)로 변환**하는 과정입니다. 이 벡터는 단어의 의미를 다차원 공간상의 좌표로 표현합니다. 의미가 비슷한 단어들은 공간상에서 가까운 위치에 존재하게 됩니다.
-   **벡터 DB (Vector Database)**: 이렇게 임베딩된 벡터 값들을 저장하고, 특정 벡터와 **유사도(Cosine Similarity 등)**가 높은 다른 벡터들을 효율적으로 검색할 수 있도록 설계된 데이터베이스입니다. `FAISS`(Facebook AI Similarity Search), `ChromaDB` 등이 대표적인 벡터 DB입니다.

> 📌 **노트: RAG 동작 흐름 요약**
> 1.  사용자가 질문(텍스트)을 입력합니다.
> 2.  질문 텍스트를 **임베딩**하여 벡터로 변환합니다.
> 3.  **벡터 DB**에서 이 벡터와 의미적으로 가장 유사한 문서 벡터들을 검색합니다.
> 4.  검색된 문서의 원본 텍스트를 사용자의 원래 질문과 함께 LLM에 전달합니다.
> 5.  LLM은 풍부해진 정보를 바탕으로 정확한 답변을 생성합니다.

### 1.6. 모든 것을 연결하는 접착제, LangChain

그렇다면 LLM, RAG, 벡터 DB, 프롬프트 등 이 복잡한 요소들을 어떻게 연결하여 하나의 애플리케이션으로 만들 수 있을까요? 바로 이 역할을 하는 것이 **LangChain**입니다.

강사님께서는 LangChain을 인공지능 모델 자체가 아니라, LLM을 활용한 애플리케이션을 쉽게 개발할 수 있도록 도와주는 **프레임워크(Framework)**라고 정의하셨습니다. LangChain은 LLM과 외부 데이터 소스, 다른 API들을 마치 사슬(Chain)처럼 연결하여 복잡한 작업 흐름(Pipeline)을 손쉽게 구축할 수 있도록 다양한 도구와 인터페이스를 제공합니다.

---

## 2. 완벽한 개발 환경 구축 (실습)

본격적인 실습에 앞서, 가장 중요한 것은 안정적인 개발 환경을 구축하는 것입니다. 강사님께서는 버전 충돌 문제를 방지하기 위해, 기존 `conda` 환경이 아닌 완전히 새로운 가상환경을 구축하는 과정을 단계별로 설명해주셨습니다.

### 2.1. 왜 새로운 가상환경이 필요한가?

우리가 사용할 `LangChain`, `OpenAI` 등의 라이브러리들은 서로 의존하는 버전이 매우 민감합니다. 현재 기본 `conda` 환경에 설치된 Python 버전(`3.13`)이나 다른 라이브러리들과 충돌을 일으킬 가능성이 매우 높습니다. 따라서 프로젝트별로 독립된 가상환경을 만들어 필요한 라이브러리 버전을 정확히 명시하여 설치하는 것이 현업의 표준 방식입니다.

### 2.2. Conda 가상환경 생성

먼저 아나콘다 프롬프트(Anaconda Prompt)를 실행하여 새로운 가상환경을 생성합니다.

```bash
conda create -n langchain_env python=3.10
```

#### 💻 코드 실행 상세 분석
1.  **`conda create`**: Anaconda 환경 관리 도구에게 새로운 가상환경을 생성하라고 지시하는 명령어입니다.
2.  **`-n langchain_env`**: `-n` (또는 `--name`) 옵션은 생성할 가상환경의 이름을 `langchain_env`로 지정합니다.
3.  **`python=3.10`**: 생성될 가상환경에 설치할 Python의 버전을 `3.10`으로 명확히 지정합니다. LLM 관련 라이브러리들이 이 버전에 가장 안정적이기 때문입니다.
4.  **최종 결과**: `langchain_env`라는 이름의 독립된 공간이 만들어지고, 그 안에는 Python 3.10 버전이 설치됩니다. 실행 중간에 관련 패키지들을 설치할지 묻는 프롬프트가 나타나면 `y`를 입력하여 진행합니다.

### 2.3. 가상환경 활성화 및 확인

생성한 가상환경을 사용하기 위해서는 먼저 활성화해야 합니다.

```bash
conda activate langchain_env
```

#### 💻 코드 실행 상세 분석
1.  **`conda activate`**: 지정된 이름의 가상환경으로 진입하라는 명령어입니다.
2.  **`langchain_env`**: 우리가 방금 생성한 가상환경의 이름입니다.
3.  **최종 결과**: 명령어 실행 후, 프롬프트 앞부분이 `(base)`에서 `(langchain_env)`로 변경된 것을 확인할 수 있습니다. 이는 현재 작업 공간이 `base` 환경에서 `langchain_env`라는 독립된 환경으로 전환되었음을 의미합니다. 이제부터 설치하는 모든 라이브러리는 이 환경 안에만 설치됩니다.

현재 conda에 어떤 가상환경들이 있는지 확인하려면 아래 명령어를 사용합니다.
```bash
conda env list
```

### 2.4. 핵심 라이브러리 설치

이제 `langchain_env` 환경 안에서 실습에 필요한 라이브러리들을 `pip`을 이용해 정확한 버전으로 설치합니다. 강사님께서는 2025년 기준으로 가장 안정적인 버전 조합을 테스트하여 공유해주셨습니다.

> 🔐 **보안 노트: 버전 명시의 중요성**
> `pip install` 시에 `==버전`을 명시하는 것은 보안과 안정성 측면에서 매우 중요합니다. 버전을 명시하지 않으면 항상 최신 버전이 설치되는데, 이 경우 라이브러리의 갑작스러운 변경으로 인해 기존 코드가 동작하지 않거나 새로운 보안 취약점이 발생할 수 있습니다. 프로젝트의 요구사항 파일을 통해 버전을 통일하면 모든 팀원이 동일한 환경에서 개발할 수 있어 "제 컴퓨터에서는 됐는데..."와 같은 문제를 예방할 수 있습니다.

#### 1단계: OpenAI 라이브러리 설치
LLM 모델을 사용하기 위한 OpenAI의 공식 라이브러리입니다.
```bash
pip install openai==1.5.2
```

#### 2단계: LangChain 관련 라이브러리 설치
LangChain 프레임워크의 핵심 및 커뮤니티 패키지를 설치합니다.
```bash
pip install langchain==0.2.16 langchain-core==0.2.38 langchain-community==0.2.16
```

#### 3단계: RAG 및 Vector DB 라이브러리 설치
RAG 구현에 사용할 `FAISS`와 `ChromaDB`를 설치합니다. `faiss-cpu`는 CPU 버전의 FAISS입니다.
```bash
pip install faiss-cpu==1.8.0 chromadb==0.5.5
```

#### 4단계: 문서 처리 및 토크나이저 라이브러리 설치
PDF나 다른 형식의 문서를 로드하고, 텍스트를 토큰으로 분리하는 데 필요한 라이브러리들입니다.
```bash
pip install tiktoken==0.7.0 pypdf==4.3.1 unstructured==0.14.10
```

#### 5단계: Jupyter 및 시각화 라이브러리 설치
Jupyter Notebook 환경과 데이터 시각화, Streamlit 앱 구동에 필요한 라이브러리들을 설치합니다.
```bash
pip install notebook==7.2.2 jupyterlab==4.2.4 ipykernel==6.29.5
pip install matplotlib==3.9.2 pandas==2.2.3 seaborn==0.13.2 streamlit==1.27.0 streamlit-audiorecorder
```

#### 6단계: 환경변수 관리 라이브러리 설치
`.env` 파일로부터 API 키와 같은 민감한 정보를 안전하게 로드하기 위한 라이브러리입니다.
```bash
pip install python-dotenv==1.0.0
```

### 2.5. 버전 충돌 해결: `httpx` 사례

강사님께서는 `openai` 라이브러리를 설치할 때 의존성 패키지인 `httpx`의 버전이 자동으로 `0.28`대로 설치되면서, 추후 코드 실행 시 `TypeError`를 발생시키는 문제가 있다고 알려주셨습니다. 이는 `openai` 1.x 버전대와 `httpx` 최신 버전 간의 호환성 문제입니다.

> 📌 **노트: 버전 충돌 해결 과정**
> 만약 코드 실행 중 `httpx` 관련 에러가 발생하면, 아래의 절차에 따라 버전을 다운그레이드하여 해결할 수 있습니다.
> 1.  **기존 버전 삭제**: `pip uninstall httpx`
> 2.  **안정 버전 재설치**: `pip install httpx==0.27.0`
>
> 이처럼 개발 과정에서 발생하는 버전 충돌은 흔한 일이며, 에러 메시지를 잘 읽고 어떤 라이브러리가 문제인지 파악하여 버전을 조정하는 능력이 중요합니다.

### 2.6. API 키를 위한 `.env` 파일 설정

OpenAI API를 사용하려면 API 키가 필요합니다. 이 키는 비밀번호와 같아서 코드에 직접 하드코딩하거나 Git과 같은 버전 관리 시스템에 올리는 것은 매우 위험한 행동입니다.

> 🔐 **보안 노트: API 키 절대 노출 금지!**
> API 키가 외부에 노출되면, 악의적인 사용자가 내 키를 사용하여 엄청난 비용을 발생시킬 수 있습니다. 따라서 API 키는 항상 환경 변수나 `.env` 파일과 같은 외부 설정 파일을 통해 관리해야 하며, `.gitignore` 파일에 `.env`를 추가하여 Git 저장소에 포함되지 않도록 해야 합니다.

**`.env` 파일 생성 및 사용법**
1.  **파일 생성**: 프로젝트의 루트 디렉터리(아나콘다 설치 경로 또는 프로젝트 폴더)에 `.env` 라는 이름의 파일을 생성합니다. 파일 이름이 `.`으로 시작하며 확장자는 없습니다.
2.  **키 저장**: 파일 내부에 아래와 같은 형식으로 키를 저장합니다.
    ```
    OPENAI_API_KEY="sk-..."
    ```
3.  **코드에서 로드**: Python 코드에서 `dotenv` 라이브러리를 사용하여 이 값을 불러옵니다.

```python
# llm_langchain_day01.py
import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# os.getenv() 함수를 사용하여 "OPENAI_API_KEY" 값을 읽어옵니다.
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")

print("API 키를 성공적으로 로드했습니다.")
```

#### 💻 코드 실행 상세 분석
1.  **`import os`**: 운영체제의 환경 변수에 접근하기 위해 `os` 모듈을 임포트합니다.
2.  **`from dotenv import load_dotenv`**: `python-dotenv` 라이브러리에서 `load_dotenv` 함수를 임포트합니다.
3.  **`load_dotenv()`**: 이 함수가 실행되면, 현재 작업 디렉터리나 상위 디렉터리에서 `.env` 파일을 찾아 그 안에 정의된 변수들을 환경 변수로 로드합니다.
4.  **`os.getenv("OPENAI_API_KEY")`**: `os` 모듈의 `getenv` 함수를 사용하여 `OPENAI_API_KEY`라는 이름의 환경 변수 값을 가져옵니다. `load_dotenv()`가 먼저 실행되었기 때문에 이 값을 읽어올 수 있습니다.
5.  **`if not api_key:`**: 만약 `.env` 파일이 없거나 키가 잘못되어 `api_key` 변수가 비어있다면, `ValueError`를 발생시켜 프로그램을 중단시킵니다. 이는 키가 없을 때 발생할 수 있는 후속 오류를 미리 방지하는 좋은 방어 코드입니다.
6.  **최종 결과**: `api_key` 변수에 `.env` 파일에 저장된 실제 키 값이 문자열 형태로 할당됩니다.

---

## 3. OpenAI API와 LangChain 핵심 개념 실습 (Jupyter)

환경 구축이 완료된 후, 강사님께서는 Jupyter Notebook을 실행하여 LangChain의 핵심 개념들을 코드로 직접 확인하는 시간을 가졌습니다.

> 📌 **노트: 가상환경에서 Jupyter Notebook 실행하기**
> 반드시 `conda activate langchain_env`로 가상환경에 진입한 상태에서 `jupyter notebook` 명령어를 실행해야 합니다. 그렇지 않으면 `base` 환경의 Jupyter가 실행되어 새로 설치한 라이브러리들을 인식하지 못하는 `ModuleNotFoundError`가 발생합니다.

### 3.1. OpenAI 모델 목록 확인하기

먼저, `openai` 라이브러리를 직접 사용하여 우리가 사용할 수 있는 모델들의 목록을 확인해보았습니다.

```python
# llm_langchain_day01.py
import openai

# 클라이언트 객체 생성 (openai 1.x 버전 이상)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 모델 목록 가져오기
models = client.models.list()

print(f'사용 가능한 모델 개수: {len(models.data)}')

# 모델 ID만 리스트로 출력
model_ids = [model.id for model in models.data]
print(model_ids[:10]) # 처음 10개만 출력
```

#### 💻 코드 실행 상세 분석
1.  **`client = openai.OpenAI(...)`**: `openai` 라이브러리 버전 1.x부터는 API와 상호작용하기 위해 `OpenAI` 클라이언트 객체를 생성해야 합니다. 이때 `api_key`를 인자로 전달합니다.
2.  **`client.models.list()`**: 생성된 클라이언트 객체를 통해 `models.list()` 메서드를 호출합니다. 이 메서드는 OpenAI 서버에 API 요청을 보내 현재 사용 가능한 모든 AI 모델의 목록을 받아옵니다.
3.  **`models.data`**: 반환된 `models` 객체는 `data`라는 속성에 실제 모델 정보 리스트를 담고 있습니다.
4.  **`[model.id for model in models.data]`**: 리스트 컴프리헨션을 사용하여 각 `model` 객체에서 `id` 속성(모델의 이름)만 추출하여 새로운 리스트 `model_ids`를 생성합니다.
5.  **최종 결과**: `gpt-4o`, `gpt-3.5-turbo`, `dall-e-3`, `whisper-1` 등 텍스트 생성, 이미지 생성, 음성 인식과 관련된 다양한 모델들의 이름을 확인할 수 있습니다. 이를 통해 우리가 어떤 모델을 사용할 수 있는지 파악할 수 있습니다.

### 3.2. 임베딩(Embedding) 실습

다음으로, 텍스트를 벡터로 변환하는 임베딩 과정을 코드로 직접 확인했습니다.

```python
# llm_langchain_day01.py

# 임베딩할 텍스트 문장들
texts = [
    '아토는 너무 이쁜 강아지입니다.',
    '이제부터 초 겨울이네요',
    '고양이는 사랑스럽습니다.'
]

# 임베딩 생성 요청
response = client.embeddings.create(
    model='text-embedding-3-small',
    input=texts
)

# 첫 번째 문장의 임베딩 결과 확인
first_embedding = response.data[0].embedding

print(f"임베딩 벡터의 차원(길이): {len(first_embedding)}")
print(f"임베딩 벡터의 일부 값: {first_embedding[:10]}")
```

#### 💻 코드 실행 상세 분석
1.  **`client.embeddings.create(...)`**: 클라이언트 객체의 `embeddings.create` 메서드를 호출하여 임베딩 생성을 요청합니다.
2.  **`model='text-embedding-3-small'`**: 임베딩을 수행할 모델을 지정합니다. `text-embedding-3-small`은 작고 효율적인 최신 임베딩 모델 중 하나입니다.
3.  **`input=texts`**: 벡터로 변환할 텍스트(문자열 리스트)를 `input` 인자로 전달합니다.
4.  **`response.data[0].embedding`**: API 응답(`response`) 객체는 `data` 리스트를 포함하며, 각 요소는 입력된 각 문장에 대한 임베딩 결과를 담고 있습니다. `data[0]`은 첫 번째 문장("아토는...")에 대한 결과이며, `.embedding` 속성을 통해 실제 숫자 벡터(리스트)에 접근할 수 있습니다.
5.  **`len(first_embedding)`**: `text-embedding-3-small` 모델은 1536개의 숫자로 이루어진 벡터를 생성합니다. 따라서 벡터의 길이는 1536이 출력됩니다.
6.  **최종 결과**: "아토는 너무 이쁜 강아지입니다."라는 문장이 1536개의 실수로 구성된 숫자 배열로 변환된 것을 확인할 수 있습니다. 이 숫자 배열이 바로 AI가 문장의 '의미'를 이해하는 방식입니다.

### 3.3. LangChain과 RAG(FAISS) 연동 실습

드디어 오늘 수업의 하이라이트인 LangChain을 이용한 RAG 구현입니다. 사용자의 질문에 대해 미리 정의된 문서 내에서 근거를 찾아 답변하는 QA 챗봇을 만들어보았습니다.

```python
# llm_langchain_day01.py

# 필요한 LangChain 모듈 임포트
from langchain.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI

# 1. 임베딩 모델 준비
# LangChain은 OpenAI 임베딩을 쉽게 사용할 수 있는 래퍼(wrapper)를 제공합니다.
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

# 2. RAG를 위한 외부 문서(Vector DB) 준비
docs = [
    '인공지능의 RNN을 기반으로 한 LLM은 RAG와 결합한 질의 응답 방식',
    'CNN과 RNN 차이점을 설명'
]
# FAISS.from_texts()를 사용하여 텍스트로부터 직접 벡터 DB를 생성합니다.
# 내부적으로 각 문서를 임베딩하고 FAISS 인덱스에 저장합니다.
vectorDB = FAISS.from_texts(docs, embedding=embeddings)

# 3. Retriever 설정
# Retriever는 벡터 DB로부터 관련 문서를 검색하는 역할을 합니다.
# search_kwargs={'k': 1}는 가장 유사한 문서 1개만 가져오라는 옵션입니다.
retriever = vectorDB.as_retriever(search_kwargs={'k': 1})

# 4. QA Chain 생성
# RetrievalQA 체인은 Retriever와 LLM을 결합하여 RAG 파이프라인을 완성합니다.
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(model_name='gpt-3.5-turbo-instruct', temperature=0, api_key=os.getenv("OPENAI_API_KEY")),
    chain_type='stuff',  # 'stuff'는 검색된 모든 문서를 하나의 프롬프트로 묶어 LLM에 전달하는 방식입니다.
    retriever=retriever
)

# 5. 질문 실행 및 답변 확인
query = 'CNN과 RNN의 차이점은 뭐야?'
answer = qa.run(query)
print(answer)
```

#### 💻 코드 실행 상세 분석
1.  **1단계 (임베딩 모델 준비)**: `OpenAIEmbeddings` 클래스의 객체를 생성합니다. LangChain이 제공하는 이 클래스는 OpenAI의 임베딩 모델을 편리하게 사용할 수 있도록 추상화한 것입니다.
2.  **2단계 (Vector DB 준비)**: `FAISS.from_texts` 클래스 메서드를 사용합니다. 이 메서드는 `docs` 리스트에 있는 각 문장을 `embeddings` 모델을 사용해 벡터로 변환하고, 이 벡터들을 메모리상의 `FAISS` 인덱스에 저장하여 `vectorDB` 객체를 생성합니다. 이것이 우리의 소규모 외부 지식 베이스가 됩니다.
3.  **3단계 (Retriever 설정)**: `vectorDB.as_retriever()`를 호출하여 검색기(Retriever)를 생성합니다. 이 검색기는 "질문이 들어오면 `vectorDB`에서 가장 유사한 문서를 찾아주는 역할"을 수행하도록 설정됩니다. `k=1` 옵션으로 가장 관련성 높은 문서 1개만 반환하도록 지정했습니다.
4.  **4단계 (QA Chain 생성)**: `RetrievalQA.from_chain_type`을 사용하여 모든 조각을 하나로 합칩니다.
    *   `llm`: 답변 생성에 사용할 언어 모델(`gpt-3.5-turbo-instruct`)을 지정합니다. `temperature=0`은 모델이 최대한 결정론적이고 일관된 답변을 생성하도록 하는 설정입니다.
    *   `chain_type='stuff'`: 검색된 문서를 처리하는 방식으로, 가장 간단한 'stuff' 방식을 사용합니다. 이는 검색된 모든 문서를 질문과 함께 하나의 큰 프롬프트로 만들어 LLM에 전달합니다.
    *   `retriever`: 3단계에서 만든 검색기를 연결해줍니다.
5.  **5단계 (질문 실행)**: `qa.run(query)`를 실행하면 전체 RAG 파이프라인이 동작합니다.
    *   (a) `query`('CNN과 RNN의 차이점은 뭐야?')가 임베딩됩니다.
    *   (b) `retriever`가 이 벡터를 사용해 `vectorDB`에서 가장 유사한 문서인 'CNN과 RNN 차이점을 설명'을 찾아냅니다.
    *   (c) 'stuff' 체인 방식에 따라, 검색된 문서('CNN과 RNN 차이점을 설명')와 원본 질문('CNN과 RNN의 차이점은 뭐야?')이 합쳐져 LLM에게 전달됩니다.
    *   (d) `gpt-3.5-turbo-instruct` 모델은 이 보강된 정보를 바탕으로 CNN과 RNN의 차이점에 대한 상세한 답변을 생성합니다.
6.  **최종 결과**: `docs`에 명시적으로 답변이 없음에도 불구하고, `retriever`가 'CNN과 RNN 차이점을 설명'이라는 문서를 찾아 LLM에게 컨텍스트로 제공했기 때문에, LLM은 이를 바탕으로 두 신경망의 구조와 데이터 유형의 차이점에 대한 정확한 설명을 생성해냅니다.

---

## 4. Streamlit으로 챗봇 UI 만들기 (VSCode)

Jupyter에서 핵심 로직을 확인한 후, VSCode로 이동하여 이 기능을 사용자가 직접 이용할 수 있는 웹 UI로 만드는 작업을 진행했습니다.

### 4.1. VSCode와 가상환경 연동

먼저 VSCode에서 새 프로젝트 폴더(`langchain_pjt`)를 열고, `Ctrl+Shift+P`로 명령어 팔레트를 열어 `Python: Select Interpreter`를 선택한 뒤, 우리가 생성한 `langchain_env` 가상환경을 인터프리터로 지정해주었습니다. 이렇게 함으로써 VSCode 터미널과 코드 실행 환경이 우리가 설치한 라이브러리들을 모두 인식하게 됩니다.

### 4.2. Streamlit 앱 구조 분석

강사님께서는 `streamlit_chat_app.py` 파일을 통해 잘 구조화된 프로그램의 기본 형태를 설명해주셨습니다.

```python
# streamlit_chat_app.py
import streamlit as st
import openai

# 로직을 처리하는 함수
def askChat(query, key):
    # ... (OpenAI API 호출 로직)
    return response_content

# 화면 UI를 구성하고 전체 프로그램을 실행하는 함수
def main():
    # ... (Streamlit UI 코드)
    if st.button('요약해줘'):
        st.info(askChat(user_input, api_key))

# 이 파일이 직접 실행될 때만 main() 함수를 호출
if __name__ == '__main__':
    main()
```

> 💡 **중요! `if __name__ == '__main__':`의 의미**
> 이 구문은 파이썬 스크립트의 실행 시작점을 지정하는 관례적인 방법입니다.
> -   스크립트가 `python streamlit_chat_app.py`처럼 직접 실행될 때, 파이썬 인터프리터는 내부적으로 `__name__`이라는 특별한 변수를 `"__main__"`으로 설정합니다. 따라서 `if`문이 참이 되어 `main()` 함수가 호출됩니다.
> -   만약 이 파일이 다른 파일에서 `import streamlit_chat_app`과 같이 모듈로 임포트될 경우, `__name__` 변수는 파일 이름인 `"streamlit_chat_app"`이 됩니다. 따라서 `if`문이 거짓이 되어 `main()` 함수가 자동으로 실행되지 않습니다.
>
> 이를 통해 코드의 재사용성을 높이고, 파일이 직접 실행될 때와 모듈로 사용될 때의 동작을 명확히 구분할 수 있습니다.

### 4.3. `streamlit_chat_app.py` 코드 상세 분석

```python
# streamlit_chat_app.py
import streamlit as st
import openai
import os

# --- 로직 부분 ---
def askChat(query, key):
    """
    OpenAI의 ChatCompletion API를 호출하여 응답을 받아오는 함수
    """
    try:
        client = openai.OpenAI(api_key=key)
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': query}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"오류가 발생했습니다: {e}"

# --- 화면(View) 및 실행 부분 ---
def main():
    st.set_page_config(page_title="챗 모델을 이용한 응답")
    st.header("간단한 요약 봇")

    # 세션 상태를 이용하여 API 키를 관리
    if 'api_key' not in st.session_state:
        st.session_state['api_key'] = ''

    with st.sidebar:
        # 사이드바에서 API 키를 입력받음
        key = st.text_input(
            label='OpenAI API Key',
            placeholder='Your API Key',
            value=st.session_state['api_key'],
            type='password'
        )
        if key:
            st.session_state['api_key'] = key

    # 메인 화면에서 사용자 질문을 입력받음
    txt = st.text_area('요약할 내용을 입력하세요:')

    if st.button('요약해줘'):
        if not st.session_state['api_key']:
            st.error("사이드바에 OpenAI API 키를 입력해주세요.")
        elif not txt:
            st.warning("요약할 내용을 입력해주세요.")
        else:
            with st.spinner('요약 중...'):
                response = askChat(txt, st.session_state['api_key'])
                st.info(response)

if __name__ == '__main__':
    main()
```

#### 💻 코드 실행 상세 분석
1.  **`main()` 함수 (화면 구성)**:
    *   `st.set_page_config()`: 웹 브라우저 탭의 제목을 설정합니다.
    *   `st.header()`: 페이지에 큰 제목을 표시합니다.
    *   `st.session_state`: Streamlit은 스크립트를 위에서 아래로 다시 실행하는 방식으로 동작하는데, 이때 변수 값을 유지하기 위해 `session_state`를 사용합니다. 여기서는 API 키를 저장하여 페이지가 새로고침 되어도 값이 사라지지 않게 합니다.
    *   `with st.sidebar:`: 이 블록 안에 있는 모든 `st.` 요소들은 화면 좌측의 사이드바에 표시됩니다.
    *   `st.text_input(type='password')`: API 키를 입력받는 텍스트 상자를 만듭니다. `type='password'` 옵션으로 입력 내용이 가려지도록 합니다.
    *   `st.text_area()`: 여러 줄의 텍스트를 입력받을 수 있는 큰 텍스트 상자를 만듭니다.
    *   `st.button('요약해줘')`: '요약해줘'라는 이름의 버튼을 만듭니다. 이 `if` 블록 안의 코드는 버튼이 클릭되었을 때만 실행됩니다.
    *   `with st.spinner(...)`: API 응답을 기다리는 동안 사용자에게 로딩 중임을 알려주는 스피너 애니메이션을 표시합니다.
2.  **`askChat(query, key)` 함수 (로직 처리)**:
    *   사용자가 입력한 `query`(질문)와 `key`(API 키)를 인자로 받습니다.
    *   `openai.OpenAI(api_key=key)`: 전달받은 키로 클라이언트 객체를 생성합니다.
    *   `client.chat.completions.create(...)`: 대화형 응답을 생성하는 엔드포인트를 호출합니다.
        *   `model='gpt-3.5-turbo'`: 사용할 모델을 지정합니다.
        *   `messages=[{'role': 'user', 'content': query}]`: 대화의 내용을 전달합니다. `role`이 'user'인 것은 사용자가 한 말을 의미합니다.
    *   `response.choices[0].message.content`: API 응답은 복잡한 객체 구조를 가집니다. 이 코드는 그중에서 우리가 실제로 원하는 텍스트 답변 부분만 정확히 추출하는 경로입니다.
3.  **실행 흐름**:
    *   사용자가 '요약해줘' 버튼을 클릭합니다.
    *   `main` 함수는 `text_area`에 입력된 내용(`txt`)과 `session_state`에 저장된 API 키를 `askChat` 함수에 전달하며 호출합니다.
    *   `askChat` 함수는 OpenAI 서버와 통신하여 응답을 받아오고, 순수 텍스트 답변만 `main` 함수에 반환합니다.
    *   `main` 함수는 반환된 답변을 `st.info()`를 통해 파란색 정보 상자 안에 표시합니다.

---

## 5. 🧩 복합 및 심화 예제: RAG 기반의 Streamlit 챗봇

오늘 배운 모든 것을 종합하여, Jupyter에서 만들었던 RAG 기반의 QA 체인을 Streamlit 웹 앱과 결합하는 최종 예제를 구상해볼 수 있습니다.

아래 코드는 `llm_langchain_day01.py`의 RAG 로직과 `streamlit_chat_app.py`의 UI 로직을 합친 완전한 애플리케이션입니다.

```python
# rag_streamlit_app.py

import streamlit as st
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI

# --- 로직 부분 ---

# @st.cache_resource 데코레이터는 리소스(모델, DB 등)를 캐싱하여
# 앱이 재실행될 때마다 다시 로드하는 것을 방지합니다.
@st.cache_resource
def initialize_rag_chain(_api_key):
    """
    API 키를 사용하여 RAG 체인을 초기화하고 캐싱합니다.
    """
    # 1. 임베딩 모델 준비
    embeddings = OpenAIEmbeddings(api_key=_api_key)

    # 2. RAG를 위한 외부 문서(Vector DB) 준비
    docs = [
        '인공지능의 RNN을 기반으로 한 LLM은 RAG와 결합한 질의 응답 방식',
        'CNN과 RNN 차이점을 설명'
    ]
    vectorDB = FAISS.from_texts(docs, embedding=embeddings)

    # 3. Retriever 설정
    retriever = vectorDB.as_retriever(search_kwargs={'k': 1})

    # 4. QA Chain 생성
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(model_name='gpt-3.5-turbo-instruct', temperature=0, api_key=_api_key),
        chain_type='stuff',
        retriever=retriever
    )
    return qa_chain

# --- 화면(View) 및 실행 부분 ---
def main():
    st.set_page_config(page_title="RAG 기반 QA 챗봇")
    st.header("RAG 기반 QA 챗봇")

    if 'api_key' not in st.session_state:
        st.session_state['api_key'] = ''

    with st.sidebar:
        key = st.text_input(
            label='OpenAI API Key',
            placeholder='Your API Key',
            value=st.session_state['api_key'],
            type='password'
        )
        if key:
            st.session_state['api_key'] = key

    query = st.text_input('질문을 입력하세요:')

    if st.button('질문하기'):
        if not st.session_state['api_key']:
            st.error("사이드바에 OpenAI API 키를 입력해주세요.")
        elif not query:
            st.warning("질문을 입력해주세요.")
        else:
            with st.spinner('답변 생성 중...'):
                try:
                    # API 키가 제공되면 RAG 체인을 초기화
                    qa_chain = initialize_rag_chain(st.session_state['api_key'])
                    # 체인을 실행하여 답변 생성
                    answer = qa_chain.run(query)
                    st.success(answer)
                except Exception as e:
                    st.error(f"오류가 발생했습니다: {e}")

if __name__ == '__main__':
    main()
```

#### 💻 코드 실행 상세 분석
1.  **`@st.cache_resource`**: 이 데코레이터는 Streamlit의 강력한 캐싱 기능입니다. `initialize_rag_chain` 함수는 무거운 작업(모델 로딩, 벡터 DB 생성)을 수행하므로, 이 데코레이터를 붙여주면 함수의 실행 결과(생성된 `qa_chain` 객체)가 메모리에 저장됩니다. 앱이 재실행되더라도 API 키가 동일하다면 이 함수를 다시 실행하지 않고 캐시된 객체를 즉시 반환하여 속도를 크게 향상시킵니다.
2.  **`initialize_rag_chain(_api_key)`**: Jupyter에서 실습했던 RAG 체인 생성 코드를 그대로 함수로 감쌌습니다. API 키를 인자로 받아 체인을 생성하고 반환합니다.
3.  **`main()` 함수**:
    *   UI 구성은 이전 예제와 유사합니다.
    *   '질문하기' 버튼이 클릭되면, 먼저 API 키와 질문이 모두 입력되었는지 확인합니다.
    *   `qa_chain = initialize_rag_chain(st.session_state['api_key'])`를 호출하여 RAG 체인을 가져옵니다. (캐시 덕분에 두 번째 실행부터는 매우 빠릅니다.)
    *   `answer = qa_chain.run(query)`를 통해 사용자의 질문을 RAG 파이프라인에 태워 최종 답변을 얻습니다.
    *   `st.success(answer)`를 사용하여 성공적인 답변을 초록색 상자에 표시합니다.
    *   `try...except` 블록을 사용하여 API 호출 중 발생할 수 있는 오류(잘못된 키, 네트워크 문제 등)를 잡아 사용자에게 친절한 에러 메시지를 보여줍니다.
4.  **최종 결과**: 이 코드를 실행하면, 사용자는 웹 UI를 통해 질문을 입력할 수 있고, 시스템은 하드코딩된 `docs`의 내용을 근거로 RAG를 통해 답변을 생성하여 화면에 보여주는 완벽한 미니 AI 애플리케이션이 완성됩니다.

오늘 수업은 생성형 AI의 기본 개념부터 실제 코드 구현, 그리고 웹 UI 연동까지 전체적인 흐름을 경험해볼 수 있는 매우 유익한 시간이었습니다. 특히, 각 기술 요소들이 왜 필요하며 어떻게 유기적으로 연결되는지를 이해하게 된 것이 가장 큰 수확이었습니다.