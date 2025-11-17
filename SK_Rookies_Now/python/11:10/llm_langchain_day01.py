import os
from dotenv import load_dotenv
import openai
from langchain_core.prompts import ChatPromptTemplate
import chromadb

from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA    # RAG에 특화된 체인
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
# import faiss # faiss는 보통 직접 import하기보다는
# langchain 등에서 내부적으로 사용됩니다.

# .env 파일 로드 (API 키 등을 사용하기 위해)
load_dotenv()

# OpenAI API 키 설정 (os.getenv로 .env 파일에서 가져옴)
openai.api_key = os.getenv("OPENAI_API_KEY")


# 학습 목표

# GenAI 활용방법
# LLM 가상환경 구축(feat vscode)
# Langchain + Rag 활용방법
# Streamli + Langchain + Rag

# 머신러닝 개념
# 알파고와
# AI는 머신러닝이다.
# 딥하게 학습하기 시작하면 딥러닝
# 기계학습 내에 딥러닝이 들어감
# 기계학습과 딥러닝의 차이는 딥하게 학습하느냐의 차이
# 인공신경망 알고리즘 방식
# CNN RNN이 나오게 됨
# Convolution Neural Network
# Recurrent Neural Network
# 자연어처리 분야에서 RNN이 많이 쓰임
# LLM도 RNN의 일종
# CNN은 이미지 처리에 많이 쓰임
# 머신러닝의 종류

# RNN에서 확장된게 LLM
# 파인튜닝 과정이 필요
# 보완 하기 위해 생긴것 -> RAG
# Retrieval Augmented Generation
# 즉 RAG는 외부 데이터

# 회사에서 LLM 아키텍처를 잡게 되면 내부 DB를 연결하는 RAG도 구축.
# 페이스북 AI인 FAISS를 많이 씀

# 벡터 DB
# 임베딩이 되어야 한다.

# 인공지능은 텍스트를 인식할 수 없기 때문에 텍스트를 숫자로 변환해주는 작업이 필요하다.
# 벡터DB는 임베딩 된 텍스트를 가지고 있는 데이터베이스
# 유사도 검색을 통해서 내가 원하는 답변을 찾아준다. cosine similarity

# 랭체인 안에 LLM이 있다 -> 인공지능이 있다.
# 랭체인은 그냥 프레임워크다.
# 인공지능과 LLM을 연결시켜주는.

# 퍼셉트론이라는 것을 활용하는 인공신경망
# 대규모 데이터를 기반으로 하는 LLM
# LLM을 통해 생성형 AI를 활용할 수 있게 됨.

# 인공지능이 데이터를 수집 -> 크롤링 -> 전처리 -> 학습 -> 재학습(파인튜닝)
# 이런 과정을 위해서 인프라가 중요

# LLM은 텍스트 기반 / 이미지도 있고, 음성도 있고, 비디오도 있다.

# 지도학습 : 분류, 회귀, 시각 음성 감지, 인지
# 비지도학습 : 군집화 (클러스터링) 차원축소

# 데이터에 너무 의존적 (Garbage in garbage out)
# 학습시에 최적의 결과를 도출하기 위해 수리보딘 머신러닝 모델은 실제 환경 데이터 적용시 과적합되기 쉽다.
# 복잡한 머신러닝 알고리즘으로 인해 도출된 결과에 대한 논리적인 이해가 어려울 수 있다. 머신러닝은 블랙박스

# 데이터만 집어넣으면 자동으로 최적화된 결과를 도출할 것이라는 것은 환상(특정 경우에는 개발자가 직접 만든 코드보다 정확도가 더 떨어질 수 있습니다.)
# 끊임없이 모델을 개선하기 위한 노력이 필요하기 때문에 데이터의 특성을 파악하고 최저그이 알고리즘과 파라미터를 구성할 수 있는 고급 노력이 필요.

# 머신러닝에서 딥러닝으로 넘어가며 keras , tensorflow 등장
# numpy pandas scikit learn 등도 생성됨.
# 분석 판다스
# 인공지능 넘파이
# 머신러닝 사이킷런

# Langchain(LLM) + RAG 개발환경
# python 3.10 사용 예정
# open ai = 1.52.0  (LLM)
# langchain = 0.2.16, langchain-core = 0.2.38, langchain-community = 0.2.16

# open ai를 이용하기 위해서는 .env 파일에 api key를 넣어줘야 한다.
# .env에서 키를 가져와주는 라이브러리 python-dotenv = 1.0.0

# faiss-cpu = 1.8.0 (RAG) / chromadb = 0.5.5

# pip install faiss-cpu==1.8.0 chromadb==0.5.5

# pip install tiktoken==0.7.0 pypdf==4.3.1 unstructured==0.14.10

# pip install notebook==7.2.2 jupyterlab==4.2.4 ipykernel==6.29.5

# pip install matplotlib==3.9.2 pandas==2.2.3 seaborn==0.13.2 streamlit==1.27.0 streamlit-audiorecorder

# pip install python-dotenv==1.0.0









# --------------------------------
# 키 값 읽어오기
import os
import openai

from dotenv import load_dotenv


# 환경변수에서 API 키를 읽어오기
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
print(api_key)



# 파이썬은 엔드포인트를 펑션으로 만듬
# 어떤 엔드포인트를 쓰느냐에 따라 챗봇 프롬프트 오디오 이미지등등 다양하게 가능하다.
# 오픈AI는 인공지능 모델을 서비스해준다.
# 이미 학습된 모델을 API형태로 제공

# 테스트 요청(모델목록)
models = openai.Model.list()
print('models - ', models, len(models.data))

# models -  SyncPage[Model](data=[Model(id='omni-moderation-latest', created=1731689265, object='model', owned_by='system'), Model(id='dall-e-2', created=1698798177, object='model', owned_by='system'), Model(id='gpt-4o-mini-search-preview', created=1741391161, object='model', owned_by='system'), Model(id='gpt-4o-mini-search-preview-2025-03-11', created=1741390858, object='model', owned_by='system'), Model(id='o3-mini-2025-01-31', created=1738010200, object='model', owned_by='system'), Model(id='gpt-4-turbo', created=1712361441, object='model', owned_by='system'), Model(id='gpt-4.1', created=1744316542, object='model', owned_by='system'), Model(id='gpt-4.1-mini-2025-04-14', created=1744317547, object='model', owned_by='system'), Model(id='gpt-5-nano-2025-08-07', created=1754426303, object='model', owned_by='system'), Model(id='gpt-4.1-mini', created=1744318173, object='model', owned_by='system'), Model(id='sora-2', created=1759708615, object='model', owned_by='system'), Model(id='sora-2-pro', created=1759708663, object='model', owned_by='system'), Model(id='gpt-4-turbo-2024-04-09', created=1712601677, object='model', owned_by='system'), Model(id='text-embedding-3-small', created=1705948997, object='model', owned_by='system'), Model(id='gpt-realtime-mini', created=1759517133, object='model', owned_by='system'), Model(id='o3-2025-04-16', created=1744133301, object='model', owned_by='system'), Model(id='o4-mini-2025-04-16', created=1744133506, object='model', owned_by='system'), Model(id='gpt-4.1-2025-04-14', created=1744315746, object='model', owned_by='system'), Model(id='gpt-4o-2024-05-13', created=1715368132, object='model', owned_by='system'), Model(id='gpt-4o-search-preview-2025-03-11', created=1741388170, object='model', owned_by='system'), Model(id='gpt-4o-search-preview', created=1741388720, object='model', owned_by='system'), Model(id='gpt-3.5-turbo-16k', created=1683758102, object='model', owned_by='openai-internal'), Model(id='o1-mini', created=1725649008, object='model', owned_by='system'), Model(id='o1-mini-2024-09-12', created=1725648979, object='model', owned_by='system'), Model(id='tts-1-1106', created=1699053241, object='model', owned_by='system'), Model(id='gpt-4o-mini-2024-07-18', created=1721172717, object='model', owned_by='system'), Model(id='o3', created=1744225308, object='model', owned_by='system'), Model(id='o4-mini', created=1744225351, object='model', owned_by='system'), Model(id='o4-mini-deep-research-2025-06-26', created=1750866121, object='model', owned_by='system'), Model(id='codex-mini-latest', created=1746673257, object='model', owned_by='system'), Model(id='gpt-5-nano', created=1754426384, object='model', owned_by='system'), Model(id='babbage-002', created=1692634615, object='model', owned_by='system'), Model(id='gpt-4-turbo-preview', created=1706037777, object='model', owned_by='system'), Model(id='chatgpt-4o-latest', created=1723515131, object='model', owned_by='system'), Model(id='tts-1-hd-1106', created=1699053533, object='model', owned_by='system'), Model(id='gpt-4o-mini-tts', created=1742403959, object='model', owned_by='system'), Model(id='o1-pro-2025-03-19', created=1742251504, object='model', owned_by='system'), Model(id='dall-e-3', created=1698785189, object='model', owned_by='system'), Model(id='o1', created=1734375816, object='model', owned_by='system'), Model(id='davinci-002', created=1692634301, object='model', owned_by='system'), Model(id='tts-1-hd', created=1699046015, object='model', owned_by='system'), Model(id='o1-pro', created=1742251791, object='model', owned_by='system'), Model(id='o4-mini-deep-research', created=1749685485, object='model', owned_by='system'), Model(id='gpt-4o-2024-11-20', created=1739331543, object='model', owned_by='system'), Model(id='gpt-4-0125-preview', created=1706037612, object='model', owned_by='system'), Model(id='gpt-5-mini', created=1754425928, object='model', owned_by='system'), Model(id='gpt-5-mini-2025-08-07', created=1754425867, object='model', owned_by='system'), Model(id='gpt-4o-realtime-preview-2024-12-17', created=1733945430, object='model', owned_by='system'), Model(id='gpt-image-1', created=1745517030, object='model', owned_by='system'), Model(id='text-embedding-ada-002', created=1671217299, object='model', owned_by='openai-internal'), Model(id='gpt-4o-mini', created=1721172741, object='model', owned_by='system'), Model(id='o3-mini', created=1737146383, object='model', owned_by='system'), Model(id='gpt-5', created=1754425777, object='model', owned_by='system'), Model(id='gpt-4.1-nano-2025-04-14', created=1744321025, object='model', owned_by='system'), Model(id='gpt-4.1-nano', created=1744321707, object='model', owned_by='system'), Model(id='gpt-4o-realtime-preview-2025-06-03', created=1748907838, object='model', owned_by='system'), Model(id='gpt-4o-transcribe', created=1742068463, object='model', owned_by='system'), Model(id='gpt-3.5-turbo-instruct', created=1692901427, object='model', owned_by='system'), Model(id='gpt-3.5-turbo-instruct-0914', created=1694122472, object='model', owned_by='system'), Model(id='gpt-4-1106-preview', created=1698957206, object='model', owned_by='system'), Model(id='gpt-5-codex', created=1757527818, object='model', owned_by='system'), Model(id='whisper-1', created=1677532384, object='model', owned_by='openai-internal'), Model(id='gpt-4o', created=1715367049, object='model', owned_by='system'), Model(id='gpt-5-2025-08-07', created=1754075360, object='model', owned_by='system'), Model(id='gpt-4o-2024-08-06', created=1722814719, object='model', owned_by='system'), Model(id='o1-2024-12-17', created=1734326976, object='model', owned_by='system'), Model(id='omni-moderation-2024-09-26', created=1732734466, object='model', owned_by='system'), Model(id='gpt-4o-audio-preview-2025-06-03', created=1748908498, object='model', owned_by='system'), Model(id='gpt-4o-audio-preview', created=1727460443, object='model', owned_by='system'), Model(id='text-embedding-3-large', created=1705953180, object='model', owned_by='system'), Model(id='gpt-4', created=1687882411, object='model', owned_by='openai'), Model(id='gpt-4-0613', created=1686588896, object='model', owned_by='openai'), Model(id='tts-1', created=1681940951, object='model', owned_by='openai-internal'), Model(id='gpt-5-search-api', created=1759514629, object='model', owned_by='system'), Model(id='gpt-3.5-turbo', created=1677610602, object='model', owned_by='openai'), Model(id='gpt-3.5-turbo-0125', created=1706048358, object='model', owned_by='system'), Model(id='gpt-realtime-mini-2025-10-06', created=1759517175, object='model', owned_by='system'), Model(id='gpt-4o-transcribe-diarize', created=1750798887, object='model', owned_by='system'), Model(id='gpt-3.5-turbo-1106', created=1698959748, object='model', owned_by='system'), Model(id='gpt-5-search-api-2025-10-14', created=1760043960, object='model', owned_by='system'), Model(id='gpt-4o-audio-preview-2024-10-01', created=1727389042, object='model', owned_by='system'), Model(id='gpt-4o-realtime-preview', created=1727659998, object='model', owned_by='system'), Model(id='gpt-5-pro', created=1759469822, object='model', owned_by='system'), Model(id='gpt-5-pro-2025-10-06', created=1759469707, object='model', owned_by='system'), Model(id='gpt-5-chat-latest', created=1754073306, object='model', owned_by='system'), Model(id='gpt-4o-mini-realtime-preview', created=1734387380, object='model', owned_by='system'), Model(id='gpt-4o-mini-audio-preview-2024-12-17', created=1734115920, object='model', owned_by='system'), Model(id='gpt-4o-mini-realtime-preview-2024-12-17', created=1734112601, object='model', owned_by='system'), Model(id='gpt-4o-mini-audio-preview', created=1734387424, object='model', owned_by='system'), Model(id='gpt-audio-mini', created=1759512027, object='model', owned_by='system'), Model(id='gpt-audio-mini-2025-10-06', created=1759512137, object='model', owned_by='system'), Model(id='gpt-4o-audio-preview-2024-12-17', created=1734034239, object='model', owned_by='system'), Model(id='gpt-4o-mini-transcribe', created=1742068596, object='model', owned_by='system'), Model(id='gpt-realtime-2025-08-28', created=1756271773, object='model', owned_by='system'), Model(id='gpt-realtime', created=1756271701, object='model', owned_by='system'), Model(id='gpt-audio', created=1756339249, object='model', owned_by='system'), Model(id='gpt-audio-2025-08-28', created=1756256146, object='model', owned_by='system'), Model(id='gpt-4o-realtime-preview-2024-10-01', created=1727131766, object='model', owned_by='system'), Model(id='gpt-image-1-mini', created=1758845821, object='model', owned_by='system')], object='list') 99
print('ai model - ', [models.data[idx].id for idx in range(len(models.data))])
# ai model -  ['omni-moderation-latest', 'dall-e-2', 'gpt-4o-mini-search-preview-2025-03-11', 'gpt-4o-mini-search-preview', 'o3-mini-2025-01-31', 'gpt-4-turbo', 'gpt-4.1', 'gpt-4.1-mini-2025-04-14', 'gpt-5-nano-2025-08-07', 'gpt-4.1-mini', 'sora-2', 'sora-2-pro', 'gpt-4-turbo-2024-04-09', 'text-embedding-3-small', 'gpt-realtime-mini', 'o3-2025-04-16', 'o4-mini-2025-04-16', 'gpt-4.1-2025-04-14', 'gpt-4o-2024-05-13', 'gpt-4o-search-preview-2025-03-11', 'gpt-4o-search-preview', 'gpt-3.5-turbo-16k', 'o1-mini', 'o1-mini-2024-09-12', 'tts-1-1106', 'gpt-4o-mini-2024-07-18', 'o3', 'o4-mini', 'o4-mini-deep-research-2025-06-26', 'codex-mini-latest', 'gpt-5-nano', 'babbage-002', 'gpt-4-turbo-preview', 'chatgpt-4o-latest', 'tts-1-hd-1106', 'gpt-4o-mini-tts', 'o1-pro-2025-03-19', 'dall-e-3', 'o1', 'davinci-002', 'tts-1-hd', 'o1-pro', 'o4-mini-deep-research', 'gpt-4o-2024-11-20', 'gpt-4-0125-preview', 'gpt-5-mini', 'gpt-5-mini-2025-08-07', 'gpt-4o-realtime-preview-2024-12-17', 'gpt-image-1', 'text-embedding-ada-002', 'gpt-4o-mini', 'o3-mini', 'gpt-5', 'gpt-4.1-nano-2025-04-14', 'gpt-4.1-nano', 'gpt-4o-realtime-preview-2025-06-03', 'gpt-4o-transcribe', 'gpt-3.5-turbo-instruct', 'gpt-3.5-turbo-instruct-0914', 'gpt-4-1106-preview', 'gpt-5-codex', 'whisper-1', 'gpt-4o', 'gpt-5-2025-08-07', 'gpt-4o-2024-08-06', 'o1-2024-12-17', 'omni-moderation-2024-09-26', 'gpt-4o-audio-preview-2025-06-03', 'gpt-4o-audio-preview', 'text-embedding-3-large', 'gpt-4', 'gpt-4-0613', 'tts-1', 'gpt-5-search-api', 'gpt-3.5-turbo', 'gpt-3.5-turbo-0125', 'gpt-realtime-mini-2025-10-06', 'gpt-4o-transcribe-diarize', 'gpt-3.5-turbo-1106', 'gpt-5-search-api-2025-10-14', 'gpt-4o-audio-preview-2024-10-01', 'gpt-4o-realtime-preview', 'gpt-5-pro', 'gpt-5-pro-2025-10-06', 'gpt-5-chat-latest', 'gpt-4o-mini-realtime-preview', 'gpt-4o-mini-audio-preview-2024-12-17', 'gpt-4o-mini-realtime-preview-2024-12-17', 'gpt-4o-mini-audio-preview', 'gpt-audio-mini', 'gpt-audio-mini-2025-10-06', 'gpt-4o-audio-preview-2024-12-17', 'gpt-4o-mini-transcribe', 'gpt-realtime-2025-08-28', 'gpt-realtime', 'gpt-audio', 'gpt-audio-2025-08-28', 'gpt-4o-realtime-preview-2024-10-01', 'gpt-image-1-mini']

# end point에 무엇이 있느냐
# endpoint를 URL로 쓰지만 파이썬에서는 펑션으로 쓴다.
# 만약 client를 통해서 대화를 하고싶다.
# client.chat.completions (대화형)
# https에서는 보통 http://v1/chat/completions
# client.completions(단일 프롬프트)
# client.embeddings(텍스트를 임베딩 벡터 변환)
# client.images(이미지 관련 내용에 대한 접근)
# client.audio.transcriptions (음성, TTS(Text to Speech), STT(Speech to Text) 관련 내용에 대한 접근)
# 이런 대화를 할 때 내부적으로 정보를 주고받는 포맷이 있음. -> 이를 통해 응답을 받을 수 있다.


# 모델을 활용하고 연계하는 능력이 중요하다.
# 모델을 호라용하여 분석하고 시각화 하는것 등등
# RAG로 DB를 가질 수 없다면 가상의 DB를 chroma DB에 연결하는 방법들.
# 우리에게는 FAISS가 있기 때문에 RAG로 작업 가능

# 피쳐(feature) = 속성
# 피처는 데이터 세트의 일반 속성
# 머신러닝은 2차원 이상의 다차원 데이터에서도 많이 사용되므로 타겟값을 제외한 나머지 속성을 모두 피처로 지칭

# 레이블 클레스 타겟값 결정ㄱ밧
# 타겟값 또는 결정값은 지도 학습시 데이터의 학습을 위해 주어지는 ...

# 분류(Classification)는 대표적인 지도학습(Supervised Learning) 방법의 하나입니다. 지도학습은 학습을 위한 다양한 피처와 분류 결정값인 레이블(Label) 데이터로 모델을 학습한 뒤, 별도의 테스트 데이터 세트에서 미지의 레이블을 예측합니다.
# 즉 지도학습은 명확한 정답이 주어진 데이터를 먼저 학습한 뒤.미지의 정답을 예측하는 방식입니다. 이 때 학습을 위해 주어진 데이터 세트를 학습 데이터 세트,머신러닝 모델의 예측 성능을 평가하기 위해 별도로 주어진 데이터 세트들 테스트 데이터 세트로 지칭합니다

# 특정한 데이터를 위해서 전처리
# 데이터 클렌징
# 결손값 처리 (Null, NaN 처리)
# 데이터 인코딩 (레이블, 원-핫 인코딩)
# 데이터 스케일링
# 이상치 제거
# Feature 선택 추출 및 가공

# 데이터 인코딩
# 머신러닝 알고리즘은 문자열 데이터 속성을 입력받지 않으며 모든 데이터는 숫자형으로 표현되어야 한다.
# 문자형 카테고리형 속성은 모두 숫자값으로 변환 / 인코딩 되어야 한다.
# 레이블 인코딩, 원-핫 인코딩

# 임베딩 : 텍스트(단어, 문장, 문서)를 숫자 배열로 변환하는 과정
# LLM 관점에서 보면 동작 흐름
# 사용자 : 텍스트를 입력하면 입력된 텍스트는 임베딩 벡터로 변환하고 이 값을 모델에게 전달하여 응답을 생성하는 흐름
# LLM + RAG를 하게 되면 (FAISS = RAG이다.)
# 사용자 : 텍스트를 입력하면 입력된 텍스트는 임베딩 벡터로 변환하고
# 외부 문서를 가지고 있는 벡터 DB에서 검색하고 증가 생성된 값을 모델에게 전달하여 응답을 생성하는 흐름

# 임베딩 할 수 있고 RAG에 대한 활용을 할 수 있게 된다면 LLM 모델로 사용할 수 있는 다양한 엔드포인트들이 존재한다.

# 유사도 검사 : 비슷한 유사도일수록 1에 가까운 값을 제공해준다.

texts = [
    '아토는 너무 이쁜 강아지입니다.',
    '이제부터 초 겨울이네요',
    '고양이는 사랑스럽습니다.'
]
print(texts)

response = openai.Embedding.create(
    model = 'text-embedding-3-large',
    input = texts
)

print('embedding len - ', len(response.data[0].embedding))
# embedding len -  3072
print('embedding value - ', response.data[0].embedding[:10])
# embedding value -  [-0.03402302414178848, -0.033126529306173325, -0.007232078816741705, 0.01284609641879797, 0.025364207103848457, 0.029781077057123184, -0.00788258295506239, -0.033432647585868835, -0.01557930838316679, -0.04491213709115982]

# RAG(Retrieval Augmented Generation) : LLM(대형 언어 모델)의 생산 능력과 외부 지식 검색 능력을 결합한 개념

# LLM 문제점 : 데이터를 기반으로 학습이 진행되고 답변함(최신정보에 대한 업데이트나 사실 정보에 대한 오류가 있다.

# RAG 장점 :
# - 외부지식(DB, 문서, API) : 임베딩 기반으로 한 Vector DB

# 전체적인 흐름
# 사용자 텍스트 입력 -> 임베딩 -> RAG 이용한 문서검색 -> LLM이 그 문서를 참조하여 질의에 대한 답변





# 모듈이 달라졌으므로 다시 작성



# embedding
embeddings = OpenAIEmbeddings()


docs = [
    {'content' : ' 인공지능의 RNN을 기반으로 한 LLM은 RAG와 결합한 질의 응답 방식', 'metadata' : {'source' : 'doc1'}},
    {'content' : ' CNN과 RNN 차이점을 설명 ', 'metadata' : {'source' : 'doc1'}},
]
# RAG
vectorDB = FAISS.from_texts([d['content'] for d in docs],   embedding = embeddings)     # 벡터 DB를 llm과 연결한다. / 따라서 검색할 수 있도록 연결해주는 인터페이스가 필요.
print(type(vectorDB))
print(vectorDB.docstore._dict)
# <class 'langchain_community.vectorstores.faiss.FAISS'>
# {'655070b1-8b14-4c84-94fe-70070691554b': Document(page_content=' 인공지능의 RNN을 기반으로 한 LLM은 RAG와 결합한 질의 응답 방식'),
#  '7f4ffa96-8af0-4635-b430-6f12929d57cd': Document(page_content=' CNN과 RNN 차이점을 설명 ')}


for idx, (key, value) in enumerate(vectorDB.docstore._dict.items()):
    print(f'{idx} 문서 ID {key}')
    print(f'content : {value.page_content[:10]}')
# 0 문서 ID 622e00c7-1b6b-4a85-b768-592926da18d9
# content :  인공지능의 RNN
# 1 문서 ID 835f4efb-8b35-4407-9c3a-35cbeeaf3bc3
# content :  CNN과 RNN

# 벡터 수
print(vectorDB.index.ntotal)
# 2
result = vectorDB.index.reconstruct(0)
print('vector extract - ', result)
# vector extract -  [-0.02625474 -0.00373176  0.0047029  ... -0.01746694 -0.01034298
#  -0.00589815]

# as_retriever() : 검색 인터페이스를 이용해서 LLM 연결하는 것
# Retriever 설정
retriever = vectorDB.as_retriever(search_kwargs = {'k' : 1})   # k는 검색할 개수 / 반환 문서 수
print(retriever)
# tags=['FAISS', 'OpenAIEmbeddings'] vectorstore=<langchain_community.vectorstores.faiss.FAISS object at 0x117fc59f0> search_kwargs={'k': 1}


qa = RetrievalQA.from_chain_type(       # LLM과 RAG가 연결되는 구조가 된다.
    llm = OpenAI(model_name = 'gpt-4o-mini', temperature=0.9),
    chain_type = 'stuff',
    retriever = retriever
)

print(qa)

query = 'cnn rnn'
answer = qa.run(query)
print('answer - ', answer)
# answer -  CNN(Convolutional Neural Network)과 RNN(Recurrent Neural Network)의 차이점은 주로 그들의 구조와 처리하는 데이터 유형에 있습니다.

# 1. **구조**:
#    - **CNN**: 주로 이미지와 같은 2차원 데이터 처리에 최적화되어 있습니다. CNN은 합성곱 레이어와 풀링 레이어로 구성되어 있으며, 공간적 구조를 보존하면서 특징을 추출하는 데 초점을 맞춥니다.
#    - **RNN**: 시퀀스 데이터를 처리하는 데 적합합니다. RNN은 순환 구조를 가지고 있어 이전 입력의 정보를 기억하고 현재의 입력과 결합하여 처리합니다. 따라서 시간적 의존성을 가진 데이터(예: 텍스트, 음성)에서 효과적입니다.

# 2. **데이터 유형**:
#    - **CNN**: 주로 이미지, 비디오, 2D 배열 데이터 처리에 사용됩니다.
#    - **RNN**: 시계열 데이터, 언어 모델링, 음성 인식 등과 같이 연속적인 데이터나 순서가 중요한 데이터에 사용됩니다.

# 이러한 차이로 인해 두 네트워크는 다양한 작업과 문제에 적합한 모델로 활용됩니다.


# 데이터베이스를 쓰느냐 안쓰느나는 자유.
# 데이터베이스를 쓰는게 낫다.
# 챗봇 기본적인 형태의 경우 파인튜닝까지는 아니더라도 특정 정보를 데이터베이스화 하는것이 중요.
# 로그를 찾아라. / 로그를 못찾으면 임시로 만들어라.
# 추가점수는 없지만, 역량을 늘릴 수 있는 기회.


# 현재까지 진행 내용
# 환경설정
# 임베딩 개념 전달
# 모델은 필요에 따라 지정





# [공지사항]
# 1. 1차 인성평가 11.13(목) 18시 30분 평가 진행. (아직 1차 인성평가 미실시 인원)
# 2. 1차 사후평가 안내. 11.14(금) 17:10~17:40 총 60문제 진행
# 3. 교재 수령 확인
# 4. 미니프로젝트 안내

# ---------------------------
# 1. 1차 인성평가 11.13(목) 18시 30분
# 지난 11.8(토)에 1차 인성평가 못보신 7명은 잊지 마시고,
# 11.13(목)에 인성평가 진행해 주세요.

# 2. 1차 사후평가 안내. 11.14(금) 17:10~17:40 총 60문제 진행
# 11.14(금)에 1차 사후 평가 진행 합니다. 사후평가는 성적에 반영됩니다.
# 사전 공지 없이 시험에 응시하지 않는 경우 재응시가 불가하니
# 반드시 응시해 주시길 바랍니다.

# 3. 교재 수령 확인
# OT때 교제를 수령하지 못하신 분들에게 택배를 보내드렸습니다.
# 수령 받으셨다면 "V"로 체크해주시길 바랍니다.

# 4. 미니프로젝트 안내
# 11.17(월)~11.21(금)에 미니프로젝트 진행합니다.
# 11.21에 미니프로젝트 발표 진행합니다.
# 강의자료실 > 좌측 "팀 빌딩" > 1차 미니프로젝트 에서 팀을 확인하시면 됩니다.
# 11.17 프로젝트 시작 전에는 수업 이후에 아이디어 회의 할수 있는 시간을 종종 드릴 예정입니다.
# 프로젝트 진행할 때 출결에 이슈가 있으신 경우 팀원들에게 공유 주세요.
