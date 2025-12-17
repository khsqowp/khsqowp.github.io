# Chapter 5: 컴퓨팅 서비스 (상세판)

> **학습 목표**: AWS의 다양한 컴퓨팅 옵션을 이해하고, EC2부터 Lambda까지 각 서비스의 특징과 사용 사례를 익힌다.

---

## 📌 목차

1. [서버 기초 지식](#1-서버-기초-지식)
2. [Amazon EC2](#2-amazon-ec2)
3. [Amazon EBS](#3-amazon-ebs)
4. [Elastic Load Balancing](#4-elastic-load-balancing)
5. [EC2 Auto Scaling](#5-ec2-auto-scaling)
6. [AWS Lambda](#6-aws-lambda)
7. [컨테이너 서비스](#7-컨테이너-서비스)
8. [기타 컴퓨팅 서비스](#8-기타-컴퓨팅-서비스)
9. [요약](#9-요약)

---

## 1. 서버 기초 지식

### 1.1 서버와 클라이언트

**서버**: 서비스를 제공하는 컴퓨터
**클라이언트**: 서비스를 요청하는 컴퓨터

**서버의 종류**:
- 웹 서버: HTTP 서비스 제공
- 데이터베이스 서버: 데이터 저장 및 조회
- 파일 서버: 파일 공유
- 메일 서버: 이메일 서비스

### 1.2 서버 가상화

**가상화**: 물리적 서버를 여러 가상 서버로 분할

**장점**:
- 하드웨어 활용률 향상
- 빠른 프로비저닝
- 격리 및 보안
- 비용 절감

---

## 2. Amazon EC2

### 2.1 EC2란?

**EC2 (Elastic Compute Cloud)**: AWS의 가상 서버 서비스

**특징**:
- 다양한 인스턴스 유형
- 초 단위 과금
- 탄력적 확장
- 완전한 제어권

### 2.2 인스턴스 유형

**인스턴스 유형 명명 규칙**:
```
t3.medium
│ │  │
│ │  └─ 크기 (nano, micro, small, medium, large, xlarge, 2xlarge...)
│ └─ 세대 (숫자가 클수록 최신)
└─ 패밀리 (용도)
```

**주요 인스턴스 패밀리**:

| 패밀리 | 용도 | 특징 | 예시 |
|--------|------|------|------|
| **T** | 범용 | 버스트 가능 | t3.medium |
| **M** | 범용 | 균형잡힌 성능 | m5.large |
| **C** | 컴퓨팅 최적화 | 높은 CPU | c5.xlarge |
| **R** | 메모리 최적화 | 높은 RAM | r5.2xlarge |
| **I** | 스토리지 최적화 | 높은 I/O | i3.large |
| **G** | GPU | 그래픽 처리 | g4dn.xlarge |

**T 인스턴스 (버스트 가능)**:
- 기본 CPU 성능 제공
- CPU 크레딧 시스템
- 크레딧 소진 시 기본 성능으로 제한
- 웹 서버, 개발 환경에 적합

### 2.3 AMI (Amazon Machine Image)

**AMI**: EC2 인스턴스를 시작하는 데 필요한 정보를 포함하는 템플릿

**AMI 구성 요소**:
- 운영체제
- 애플리케이션
- 애플리케이션 서버
- 설정

**AMI 유형**:
- **AWS 제공 AMI**: Amazon Linux, Ubuntu, Windows Server
- **AWS Marketplace AMI**: 타사 제공
- **커뮤니티 AMI**: 사용자 공유
- **사용자 정의 AMI**: 직접 생성

### 2.4 EC2 인스턴스 생성

**생성 단계**:

**1. AMI 선택**:
```
- Amazon Linux 2023
- Ubuntu 22.04 LTS
- Windows Server 2022
- Red Hat Enterprise Linux
```

**2. 인스턴스 유형 선택**:
```
- t3.micro (1 vCPU, 1GB RAM) - 프리 티어
- t3.small (2 vCPU, 2GB RAM)
- t3.medium (2 vCPU, 4GB RAM)
```

**3. 네트워크 설정**:
```
- VPC 선택
- 서브넷 선택 (퍼블릭/프라이빗)
- 퍼블릭 IP 자동 할당 여부
```

**4. 스토리지 설정**:
```
- 루트 볼륨 크기 (기본 8GB)
- 볼륨 유형 (gp3, gp2, io2)
- 추가 볼륨
- 암호화 여부
```

**5. 보안 그룹 설정**:
```
인바운드 규칙:
- SSH (22): 내 IP
- HTTP (80): 0.0.0.0/0
- HTTPS (443): 0.0.0.0/0
```

**6. 키 페어**:
```
- 새 키 페어 생성
- 기존 키 페어 사용
- 키 페어 없이 진행 (비권장)
```

### 2.5 EC2 인스턴스 수명 주기

**인스턴스 상태**:

```
pending → running → stopping → stopped → terminating → terminated
          ↓
        rebooting
```

**상태별 과금**:
- **running**: 과금 O
- **stopped**: 인스턴스 과금 X, EBS 과금 O
- **terminated**: 과금 X (완전 삭제)

### 2.6 EC2 메타데이터

**메타데이터**: 인스턴스에 대한 정보

**접근 방법**:
```bash
# 인스턴스 내부에서
curl http://169.254.169.254/latest/meta-data/

# 인스턴스 ID
curl http://169.254.169.254/latest/meta-data/instance-id

# 퍼블릭 IP
curl http://169.254.169.254/latest/meta-data/public-ipv4

# IAM 역할 자격 증명
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

### 2.7 User Data

**User Data**: 인스턴스 시작 시 실행되는 스크립트

**예시: 웹 서버 자동 설치**:
```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from EC2!</h1>" > /var/www/html/index.html
```

### 2.8 EC2 요금 옵션

**1. 온디맨드 (On-Demand)**:
- 시간당 또는 초당 과금
- 약정 없음
- 가장 비쌈
- 단기, 예측 불가능한 워크로드

**2. 예약 인스턴스 (Reserved Instances)**:
- 1년 또는 3년 약정
- 최대 75% 할인
- 안정적인 워크로드

**3. Savings Plans**:
- 시간당 사용량 약정
- 최대 72% 할인
- 유연성 높음

**4. 스팟 인스턴스 (Spot Instances)**:
- 최대 90% 할인
- 중단 가능
- 배치 처리, 빅데이터 분석

**요금 비교 (t3.medium 기준)**:
```
온디맨드: $0.0416/시간
1년 예약 (선불 전체): $0.025/시간 (40% 할인)
3년 예약 (선불 전체): $0.015/시간 (64% 할인)
스팟: $0.0125/시간 (70% 할인, 변동)
```

---

## 3. Amazon EBS

### 3.1 EBS란?

**EBS (Elastic Block Store)**: EC2용 블록 스토리지

**특징**:
- 영구 스토리지
- 스냅샷 백업
- 암호화 지원
- 다양한 볼륨 유형

### 3.2 EBS 볼륨 유형

**SSD 기반**:

| 유형 | 용도 | IOPS | 처리량 | 크기 |
|------|------|------|--------|------|
| **gp3** | 범용 | 3,000-16,000 | 125-1,000 MB/s | 1GB-16TB |
| **gp2** | 범용 | 100-16,000 | 최대 250 MB/s | 1GB-16TB |
| **io2** | 고성능 | 100-64,000 | 최대 1,000 MB/s | 4GB-16TB |
| **io1** | 고성능 | 100-64,000 | 최대 1,000 MB/s | 4GB-16TB |

**HDD 기반**:

| 유형 | 용도 | 처리량 | 크기 |
|------|------|--------|------|
| **st1** | 처리량 최적화 | 최대 500 MB/s | 125GB-16TB |
| **sc1** | Cold HDD | 최대 250 MB/s | 125GB-16TB |

**선택 가이드**:
```
루트 볼륨: gp3 (범용, 비용 효율적)
데이터베이스: io2 (높은 IOPS)
빅데이터: st1 (높은 처리량)
아카이브: sc1 (저렴)
```

### 3.3 EBS 스냅샷

**스냅샷**: EBS 볼륨의 백업

**특징**:
- 증분 백업 (변경된 블록만)
- S3에 저장
- 리전 간 복사 가능
- AMI 생성 가능

**스냅샷 생명 주기**:
```
1. 첫 스냅샷: 전체 볼륨 복사
2. 두 번째 스냅샷: 변경된 블록만
3. 세 번째 스냅샷: 변경된 블록만
→ 스토리지 비용 절감
```

### 3.4 EBS 암호화

**암호화 기능**:
- AES-256 암호화
- KMS 키 사용
- 저장 데이터 암호화
- 전송 중 데이터 암호화
- 스냅샷 자동 암호화

---

## 4. Elastic Load Balancing

### 4.1 ELB란?

**ELB**: 트래픽을 여러 대상에 자동 분산

**장점**:
- 고가용성
- 자동 스케일링
- 헬스 체크
- SSL/TLS 종료

### 4.2 ELB 유형

**1. Application Load Balancer (ALB)**:
- Layer 7 (HTTP/HTTPS)
- 경로 기반 라우팅
- 호스트 기반 라우팅
- WebSocket 지원

**2. Network Load Balancer (NLB)**:
- Layer 4 (TCP/UDP)
- 초고성능 (수백만 요청/초)
- 고정 IP
- 낮은 지연시간

**3. Gateway Load Balancer (GWLB)**:
- Layer 3 (IP)
- 방화벽, IDS/IPS 통합

**4. Classic Load Balancer (CLB)**:
- 레거시 (사용 비권장)

### 4.3 ALB 구성 요소

**로드 밸런서**:
- 트래픽 진입점
- 여러 AZ에 배치

**리스너**:
- 프로토콜 및 포트 설정
- HTTP:80, HTTPS:443

**타겟 그룹**:
- 대상 인스턴스 그룹
- 헬스 체크 설정
- 라우팅 알고리즘

**라우팅 규칙**:
```
경로 기반:
- /api/* → API 서버 타겟 그룹
- /images/* → 이미지 서버 타겟 그룹
- /* → 웹 서버 타겟 그룹

호스트 기반:
- api.example.com → API 서버
- www.example.com → 웹 서버
```

### 4.4 헬스 체크

**헬스 체크**: 대상의 상태 확인

**설정**:
```
프로토콜: HTTP
경로: /health
포트: 80
간격: 30초
타임아웃: 5초
정상 임계값: 2회 연속 성공
비정상 임계값: 2회 연속 실패
```

**동작**:
```
1. 30초마다 /health 경로 확인
2. 2회 연속 성공 → 정상 (트래픽 전송)
3. 2회 연속 실패 → 비정상 (트래픽 중단)
4. 복구 시 자동으로 트래픽 재개
```

---

## 5. EC2 Auto Scaling

### 5.1 Auto Scaling이란?

**Auto Scaling**: EC2 인스턴스 수를 자동으로 조정

**장점**:
- 고가용성
- 비용 최적화
- 성능 유지

### 5.2 Auto Scaling 구성 요소

**1. 시작 템플릿 (Launch Template)**:
```
- AMI
- 인스턴스 유형
- 키 페어
- 보안 그룹
- User Data
```

**2. Auto Scaling 그룹 (ASG)**:
```
- 최소 용량 (Minimum): 2
- 원하는 용량 (Desired): 4
- 최대 용량 (Maximum): 10
```

**3. 스케일링 정책**:
- 대상 추적
- 단계 조정
- 단순 조정
- 예약된 조정

### 5.3 스케일링 정책

**대상 추적 정책**:
```
목표: CPU 사용률 70% 유지
- CPU > 70% → 인스턴스 추가
- CPU < 70% → 인스턴스 제거
```

**단계 조정 정책**:
```
CPU 50-60%: 인스턴스 1개 추가
CPU 60-70%: 인스턴스 2개 추가
CPU > 70%: 인스턴스 3개 추가
```

**예약된 조정**:
```
평일 09:00: 인스턴스 10개로 증가
평일 18:00: 인스턴스 2개로 감소
주말: 인스턴스 1개 유지
```

---

## 6. AWS Lambda

### 6.1 Lambda란?

**Lambda**: 서버리스 컴퓨팅 서비스

**특징**:
- 서버 관리 불필요
- 이벤트 기반 실행
- 자동 스케일링
- 사용한 시간만 과금

### 6.2 Lambda 함수

**지원 런타임**:
- Python 3.12
- Node.js 20
- Java 21
- Go 1.x
- .NET 8
- Ruby 3.2

**함수 구조 (Python)**:
```python
def lambda_handler(event, context):
    # event: 입력 데이터
    # context: 실행 환경 정보
    
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
```

### 6.3 Lambda 트리거

**이벤트 소스**:
- API Gateway: HTTP 요청
- S3: 파일 업로드
- DynamoDB: 데이터 변경
- CloudWatch Events: 스케줄
- SNS/SQS: 메시지

**예시: S3 이미지 리사이징**:
```
1. 사용자가 S3에 이미지 업로드
2. S3가 Lambda 함수 트리거
3. Lambda가 이미지 리사이징
4. 리사이징된 이미지를 S3에 저장
```

### 6.4 Lambda 설정

**메모리**:
- 128MB ~ 10,240MB
- CPU는 메모리에 비례

**타임아웃**:
- 1초 ~ 15분

**환경 변수**:
```
DB_HOST=mydb.example.com
DB_USER=admin
API_KEY=xxx
```

**IAM 역할**:
```
Lambda 실행 역할:
- CloudWatch Logs 쓰기
- S3 읽기/쓰기
- DynamoDB 액세스
```

### 6.5 Lambda 과금

**요청 수**:
- 월 100만 건 무료
- 이후 100만 건당 $0.20

**실행 시간**:
- 월 40만 GB-초 무료
- 이후 GB-초당 $0.0000166667

**예시**:
```
함수 설정:
- 메모리: 512MB (0.5GB)
- 실행 시간: 200ms (0.2초)
- 월 실행 횟수: 300만 회

요청 비용:
(3,000,000 - 1,000,000) × $0.20 / 1,000,000 = $0.40

실행 비용:
3,000,000 × 0.5GB × 0.2초 = 300,000 GB-초
(300,000 - 400,000) = 0 (무료 범위 내)

총 비용: $0.40/월
```

---

## 7. 컨테이너 서비스

### 7.1 컨테이너란?

**컨테이너**: 애플리케이션과 종속성을 패키징

**Docker**:
- 컨테이너 플랫폼
- 이미지 기반
- 가볍고 빠름

**컨테이너 vs 가상 머신**:

| 구분 | 컨테이너 | 가상 머신 |
|------|----------|----------|
| OS | 공유 | 각각 |
| 크기 | MB | GB |
| 시작 시간 | 초 | 분 |
| 격리 | 프로세스 | 하드웨어 |

### 7.2 Amazon ECS

**ECS (Elastic Container Service)**: 컨테이너 오케스트레이션

**구성 요소**:
- 클러스터: 컨테이너 실행 환경
- 태스크 정의: 컨테이너 설정
- 서비스: 태스크 관리
- 태스크: 실행 중인 컨테이너

**시작 유형**:
- **EC2**: 직접 EC2 관리
- **Fargate**: 서버리스 (권장)

### 7.3 Amazon EKS

**EKS (Elastic Kubernetes Service)**: 쿠버네티스 관리형 서비스

**특징**:
- 쿠버네티스 호환
- 자동 업그레이드
- 고가용성
- AWS 서비스 통합

---

## 8. 기타 컴퓨팅 서비스

### 8.1 Elastic Beanstalk

**Elastic Beanstalk**: PaaS

**특징**:
- 코드만 업로드
- 인프라 자동 구성
- 다양한 플랫폼 지원

**지원 플랫폼**:
- Java, .NET, PHP, Node.js
- Python, Ruby, Go
- Docker

### 8.2 AWS Batch

**Batch**: 배치 작업 실행

**사용 사례**:
- 대규모 데이터 처리
- 시뮬레이션
- 렌더링

### 8.3 Lightsail

**Lightsail**: 간소화된 VPS

**특징**:
- 고정 가격
- 간단한 설정
- 초보자 친화적

---

## 9. 요약

### 핵심 개념

**EC2**:
- 가상 서버
- 다양한 인스턴스 유형
- 온디맨드, 예약, 스팟

**EBS**:
- 블록 스토리지
- gp3, io2, st1, sc1
- 스냅샷 백업

**ELB**:
- 로드 밸런서
- ALB (Layer 7), NLB (Layer 4)
- 헬스 체크

**Auto Scaling**:
- 자동 확장/축소
- 시작 템플릿
- 스케일링 정책

**Lambda**:
- 서버리스
- 이벤트 기반
- 15분 제한

**컨테이너**:
- ECS, EKS
- Fargate (서버리스)

### 학습 체크리스트

- [ ] EC2 인스턴스 유형을 선택할 수 있다
- [ ] AMI의 역할을 이해했다
- [ ] EBS 볼륨 유형을 비교할 수 있다
- [ ] ELB의 종류와 차이를 안다
- [ ] Auto Scaling 정책을 설정할 수 있다
- [ ] Lambda의 사용 사례를 안다
- [ ] 컨테이너와 가상 머신의 차이를 설명할 수 있다

---

**이전**: [Chapter 4: VPC](./Chapter04_VPC_상세.md)  
**다음**: [Chapter 6: 스토리지 서비스](./Chapter06_스토리지서비스_상세.md)

## 10. EC2 고급 주제

### 10.1 배치 그룹 (Placement Groups)

**클러스터 배치 그룹**:
- 단일 AZ 내 인스턴스 밀집 배치
- 낮은 네트워크 지연시간
- 높은 네트워크 처리량
- HPC, 빅데이터 분석

**파티션 배치 그룹**:
- 논리적 파티션으로 분산
- 각 파티션은 별도 랙
- 장애 격리
- Hadoop, Cassandra, Kafka

**분산 배치 그룹**:
- 각 인스턴스를 별도 하드웨어에 배치
- 최대 7개 인스턴스/AZ
- 고가용성 중요 애플리케이션

### 10.2 Elastic IP

**특징**:
- 고정 공인 IP
- 계정에 할당
- 인스턴스 간 이동 가능
- 연결되지 않으면 과금

**사용 사례**:
- DNS 변경 없이 인스턴스 교체
- 장애 조치
- 화이트리스트 IP

**비용**:
- 실행 중인 인스턴스에 연결: 무료
- 미사용 또는 중지된 인스턴스: $0.005/시간

### 10.3 EC2 Instance Store

**특징**:
- 물리적으로 연결된 디스크
- 매우 높은 IOPS
- 임시 스토리지
- 인스턴스 중지/종료 시 데이터 삭제

**사용 사례**:
- 캐시
- 버퍼
- 임시 데이터
- 복제된 데이터

**vs EBS**:
| 구분 | Instance Store | EBS |
|------|---------------|-----|
| 영구성 | 임시 | 영구 |
| 성능 | 매우 높음 | 높음 |
| 백업 | 불가 | 스냅샷 |
| 크기 변경 | 불가 | 가능 |

---

## 11. 컨테이너 심화

### 11.1 ECS 심화

**태스크 정의 예시**:
```json
{
  "family": "web-app",
  "containerDefinitions": [{
    "name": "nginx",
    "image": "nginx:latest",
    "memory": 512,
    "cpu": 256,
    "portMappings": [{
      "containerPort": 80,
      "protocol": "tcp"
    }]
  }]
}
```

**서비스 생성**:
```
클러스터: my-cluster
태스크 정의: web-app:1
원하는 개수: 3
로드 밸런서: ALB
Auto Scaling: CPU 70% 유지
```

### 11.2 EKS 심화

**노드 그룹**:
- 관리형 노드 그룹 (권장)
- 자체 관리형 노드
- Fargate (서버리스)

**kubectl 명령어**:
```bash
# 클러스터 정보
kubectl cluster-info

# 노드 목록
kubectl get nodes

# 파드 배포
kubectl apply -f deployment.yaml

# 서비스 생성
kubectl expose deployment nginx --port=80 --type=LoadBalancer
```

---

## 12. 서버리스 심화

### 12.1 Lambda 고급 기능

**레이어 (Layers)**:
- 공통 코드, 라이브러리 공유
- 배포 패키지 크기 감소
- 버전 관리

**환경 변수**:
```python
import os

db_host = os.environ['DB_HOST']
api_key = os.environ['API_KEY']
```

**VPC 액세스**:
- Lambda를 VPC에 연결
- RDS, ElastiCache 접근
- NAT Gateway 필요 (인터넷 접근 시)

**동시성 제어**:
- 예약된 동시성: 특정 함수 보장
- 프로비저닝된 동시성: 콜드 스타트 제거

### 12.2 Lambda@Edge

**특징**:
- CloudFront에서 Lambda 실행
- 엣지 로케이션에서 코드 실행
- 낮은 지연시간

**사용 사례**:
- URL 리다이렉션
- A/B 테스트
- 헤더 조작
- 이미지 리사이징

---

## 13. 비용 최적화 전략

### 13.1 인스턴스 크기 최적화

**Right Sizing**:
```
현재: t3.2xlarge (8 vCPU, 32GB)
평균 CPU: 15%
평균 메모리: 8GB

권장: t3.large (2 vCPU, 8GB)
월 절감: $120
```

**CloudWatch 메트릭 활용**:
- CPU 사용률
- 메모리 사용률
- 네트워크 사용량
- 디스크 I/O

### 13.2 스팟 인스턴스 활용

**적합한 워크로드**:
- 배치 처리
- 데이터 분석
- CI/CD
- 웹 크롤링

**스팟 플릿**:
```
목표 용량: 10 인스턴스
인스턴스 유형: t3.medium, t3.large, t3.xlarge
최대 가격: 온디맨드의 50%
할당 전략: 최저 가격
```

### 13.3 Savings Plans

**Compute Savings Plans**:
- EC2, Lambda, Fargate
- 최대 66% 할인
- 인스턴스 유형 변경 가능

**EC2 Instance Savings Plans**:
- 특정 인스턴스 패밀리
- 최대 72% 할인
- 리전 내에서 유연

---

## 14. 모니터링 및 로깅

### 14.1 CloudWatch 메트릭

**기본 메트릭**:
- CPUUtilization
- NetworkIn/Out
- DiskReadOps/WriteOps
- StatusCheckFailed

**사용자 지정 메트릭**:
```python
import boto3

cloudwatch = boto3.client('cloudwatch')

cloudwatch.put_metric_data(
    Namespace='MyApp',
    MetricData=[{
        'MetricName': 'PageLoadTime',
        'Value': 0.5,
        'Unit': 'Seconds'
    }]
)
```

### 14.2 CloudWatch Logs

**로그 그룹 및 스트림**:
```
로그 그룹: /aws/ec2/web-server
로그 스트림: i-1234567890abcdef0
```

**로그 인사이트 쿼리**:
```
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 20
```

---

## 15. 보안 모범 사례

### 15.1 IAM 역할 사용

**EC2 Instance Profile**:
```
역할: EC2-S3-Access-Role
정책: AmazonS3ReadOnlyAccess

EC2에 연결:
- 자동으로 임시 자격 증명 제공
- Access Key 하드코딩 불필요
```

### 15.2 보안 그룹 최소화

**원칙**:
- 필요한 포트만 열기
- 출발지 IP 제한
- 정기적 검토

**예시**:
```
웹 서버:
- 80/443: 0.0.0.0/0 (전체 허용)
- 22: 관리자 IP만

데이터베이스:
- 3306: 웹 서버 보안 그룹만
```

### 15.3 암호화

**EBS 암호화**:
- 저장 데이터 암호화
- KMS 키 사용
- 스냅샷 자동 암호화

**전송 중 암호화**:
- HTTPS/TLS
- VPN
- Direct Connect

---

## 16. 요약

### 핵심 개념

**EC2**:
- 가상 서버
- 다양한 인스턴스 유형
- 온디맨드, 예약, 스팟, Savings Plans

**EBS**:
- 블록 스토리지
- gp3, io2, st1, sc1
- 스냅샷 백업

**ELB**:
- ALB (Layer 7)
- NLB (Layer 4)
- 헬스 체크, Auto Scaling

**Auto Scaling**:
- 자동 확장/축소
- 대상 추적, 단계 조정
- 고가용성, 비용 최적화

**Lambda**:
- 서버리스
- 이벤트 기반
- 15분 제한

**컨테이너**:
- ECS, EKS
- Fargate (서버리스)

### 학습 체크리스트

- [ ] EC2 인스턴스 유형을 선택할 수 있다
- [ ] EBS 볼륨 유형을 비교할 수 있다
- [ ] ELB를 설정할 수 있다
- [ ] Auto Scaling 정책을 구성할 수 있다
- [ ] Lambda 함수를 작성할 수 있다
- [ ] 컨테이너와 VM의 차이를 설명할 수 있다
- [ ] 비용 최적화 전략을 적용할 수 있다

---

**이전**: [Chapter 4: VPC](./Chapter04_VPC_상세.md)  
**다음**: [Chapter 6: 스토리지 서비스](./Chapter06_스토리지서비스_상세.md)

---

**문서 정보**:
- 작성일: 2025-12-10
- 버전: 1.0 (상세판)
- 총 줄 수: 1000줄 이상
- 학습 시간: 약 3-4시간

