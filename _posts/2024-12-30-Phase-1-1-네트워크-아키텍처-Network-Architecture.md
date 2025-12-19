---
layout: post
title: "Phase 1-1: 네트워크 아키텍처 (Network Architecture)"
date: 2024-12-30 09:00:01 +0900
categories: [general]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 1-1: 네트워크 아키텍처 (Network Architecture)

## 학습 목표
- OSI 7계층 모델의 각 계층별 역할과 프로토콜을 정확히 이해
- TCP/IP 4계층 모델과 OSI 모델의 매핑 관계 파악
- 데이터 캡슐화/역캡슐화 과정의 단계별 동작 원리 습득
- 각 계층에서 사용되는 PDU(Protocol Data Unit)의 구조와 특징 분석
- 프로토콜 스택의 계층적 구조가 제공하는 이점 이해

---

## 1. OSI 7계층 모델 (OSI Reference Model)

### 1.1 OSI 모델 개요

**OSI (Open Systems Interconnection) 참조 모델**
- **제정 기관**: ISO (International Organization for Standardization)
- **제정 연도**: 1984년
- **목적**: 서로 다른 벤더 규격들 간의 국제적 표준화
- **현재 상태**: TCP/IP 모델에 밀려 주로 교육용으로 활용

**계층 분리의 핵심 원칙**
1. **기능별 분리**: 특정 작업만 수행하는 계층으로 나눔
2. **독립성 보장**: 각 계층은 인접 계층과만 통신
3. **투명성 확보**: 하위 계층의 구현 세부사항을 상위 계층에서 알 필요 없음
4. **유지보수 용이성**: 특정 계층 변경 시 다른 계층에 영향 최소화

---

### 1.2 계층별 상세 분석

## Layer 7: 애플리케이션 계층 (Application Layer)

### 역할
- 사용자에게 네트워크 서비스 직접 제공
- 애플리케이션 프로토콜을 통해 데이터 교환
- 사용자 인터페이스와 네트워크 간의 접점

### PDU (Protocol Data Unit)
- **명칭**: Message (메시지) 또는 Data
- **구성**: 순수 애플리케이션 데이터

### 주요 프로토콜

**HTTP/HTTPS (HyperText Transfer Protocol)**
- **포트**: 80 (HTTP), 443 (HTTPS)
- **목적**: 웹 리소스 전송
- **특징**: 
  - Stateless 프로토콜 (상태 유지 안 함)
  - Request-Response 구조
  - HTTPS는 TLS/SSL을 통한 암호화 제공

**DNS (Domain Name System)**
- **포트**: 53 (UDP/TCP)
- **목적**: 도메인 이름을 IP 주소로 변환
- **동작**:
  - 재귀 쿼리 (Recursive Query): 클라이언트 → DNS 서버
  - 반복 쿼리 (Iterative Query): DNS 서버 간 조회

**FTP (File Transfer Protocol)**
- **포트**: 20 (Data), 21 (Control)
- **목적**: 파일 전송
- **모드**:
  - Active Mode: 서버가 클라이언트에 데이터 연결
  - Passive Mode: 클라이언트가 서버에 데이터 연결
- **보안 이슈**: 평문 전송 → SFTP/FTPS 권장

**SMTP (Simple Mail Transfer Protocol)**
- **포트**: 25 (전통적), 587 (제출용)
- **목적**: 이메일 전송
- **특징**: 송신 전용 프로토콜

**POP3/IMAP (Post Office Protocol / Internet Message Access Protocol)**
- **포트**: 110 (POP3), 143 (IMAP)
- **목적**: 이메일 수신
- **차이**:
  - POP3: 메일 다운로드 후 서버에서 삭제
  - IMAP: 서버에 메일 유지, 동기화 지원

**SSH (Secure Shell)**
- **포트**: 22
- **목적**: 안전한 원격 접속
- **제공 기능**:
  - 원격 명령 실행
  - 파일 전송 (SCP, SFTP)
  - 포트 포워딩 (터널링)

### 관련 장비
- L7 스위치 (Load Balancer)
- WAF (Web Application Firewall)
- 차세대 방화벽 (NGFW)
- IDS/IPS (침입 탐지/차단 시스템)

### 용어 설명
- **Client-Server Model**: 요청자(클라이언트)와 제공자(서버)로 역할 분리
- **Request-Response**: 요청에 대한 응답 구조
- **API (Application Programming Interface)**: 애플리케이션 간 통신 규약
- **Payload**: 실제 전송하려는 데이터 (헤더 제외)

---

## Layer 6: 프레젠테이션 계층 (Presentation Layer)

### 역할
- 애플리케이션 데이터를 네트워크 전송 가능한 형식으로 변환
- 데이터 표현 방식의 차이 해결
- 암호화/복호화, 압축/압축 해제 수행

### 주요 기능

**데이터 변환 (Data Translation)**
- 서로 다른 시스템 간 데이터 형식 변환
- 문자 인코딩 변환: ASCII ↔ EBCDIC ↔ UTF-8

**압축 (Compression)**
- 데이터 크기 축소로 전송 효율 향상
- 알고리즘:
  - **Lossless** (무손실): gzip, deflate, LZMA
  - **Lossy** (손실): JPEG, MP3 (멀티미디어 압축)

**암호화 (Encryption)**
- 데이터 기밀성 보장
- **SSL/TLS**: 전송 계층 보안
  - TLS 1.2, TLS 1.3 (현재 권장)
  - Cipher Suite: 암호화 알고리즘 조합
  - Handshake: 암호화 협상 과정

### 주요 프로토콜/표준
- **ASCII (American Standard Code for Information Interchange)**
  - 7비트 문자 인코딩
  - 128개 문자 표현 (0-127)
  
- **JPEG (Joint Photographic Experts Group)**
  - 이미지 손실 압축 표준
  - 압축률과 화질의 균형

- **MPEG (Moving Picture Experts Group)**
  - 비디오/오디오 압축 표준
  - MPEG-1, MPEG-2, MPEG-4

- **XDR (External Data Representation)**
  - 데이터 직렬화 표준
  - 플랫폼 독립적 데이터 표현

### 용어 설명
- **Character Encoding**: 문자를 숫자 코드로 매핑하는 방식
- **Serialization**: 데이터 구조를 전송 가능한 형식으로 변환
- **Cipher Suite**: TLS에서 사용하는 암호화 알고리즘 조합
  - 예: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  - 키 교환(ECDHE) + 인증(RSA) + 암호화(AES-128-GCM) + 해시(SHA256)

---

## Layer 5: 세션 계층 (Session Layer)

### 역할
- 애플리케이션 간 논리적 통신로(세션) 관리
- 세션 연결, 유지, 종료 제어
- 대화 제어 및 동기화

### 주요 기능

**세션 수립 (Session Establishment)**
- 통신 양 종단 간 세션 설정
- 세션 파라미터 협상
- 인증 및 권한 부여

**세션 유지 (Session Maintenance)**
- 연결 상태 모니터링
- Keep-Alive 메커니즘
- 재연결 처리

**세션 종료 (Session Termination)**
- 정상 종료 절차
- 리소스 해제
- 종료 후 정리 작업

**동기화 (Synchronization)**
- Checkpoint 설정: 재전송 시작점 표시
- 장애 발생 시 마지막 Checkpoint부터 재개
- 대량 데이터 전송 시 유용

**대화 제어 (Dialog Control)**
- **Simplex**: 단방향 통신
- **Half-Duplex**: 양방향 교대 통신
- **Full-Duplex**: 양방향 동시 통신

### 주요 프로토콜
- **NetBIOS (Network Basic Input/Output System)**
  - Windows 네트워크의 세션 관리
  - 이름 해석, 세션 서비스 제공

- **RPC (Remote Procedure Call)**
  - 원격 프로시저 호출 메커니즘
  - 네트워크를 통한 함수 실행

- **PPTP (Point-to-Point Tunneling Protocol)**
  - VPN 세션 수립

### 용어 설명
- **Session ID**: 세션을 고유하게 식별하는 값
- **Token**: 데이터 전송 권한을 나타내는 제어 신호
- **Checkpoint**: 복구 가능한 지점 표시
- **Dialog Separation**: 대화 단위 구분

---

## Layer 4: 전송 계층 (Transport Layer)

### 역할
- 종단 간(End-to-End) 데이터 전송 보장
- 애플리케이션 프로세스 식별 (포트 번호)
- 데이터 전송 품질 제어 (신뢰성, 순서, 흐름 제어)

### PDU (Protocol Data Unit)
- **TCP**: Segment (세그먼트)
- **UDP**: Datagram (데이터그램)

---

### TCP (Transmission Control Protocol)

#### TCP 특징
- **연결 지향 (Connection-Oriented)**
- **신뢰성 보장 (Reliable)**
  - 순서 보장: Sequence Number
  - 전송 확인: Acknowledgment
  - 오류 검출: Checksum
  - 재전송: Timeout & Retransmission
- **흐름 제어 (Flow Control)**: Sliding Window
- **혼잡 제어 (Congestion Control)**: Slow Start, Congestion Avoidance

#### TCP 세그먼트 구조

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |       |C|E|U|A|P|R|S|F|                               |
| Offset| Rsvd  |W|C|R|C|S|S|Y|I|            Window             |
|       |       |R|E|G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (가변)                  |  Padding |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             Data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**필드별 상세 설명**

1. **Source Port (16비트)**
   - 송신 프로세스의 포트 번호
   - 0~65535 범위

2. **Destination Port (16비트)**
   - 수신 프로세스의 포트 번호
   - Well-Known Ports (0-1023)
   - Registered Ports (1024-49151)
   - Dynamic/Private Ports (49152-65535)

3. **Sequence Number (32비트)**
   - 전송하는 데이터의 첫 번째 바이트 번호
   - 바이트 단위로 증가
   - 초기값(ISN): 무작위 생성 (보안 목적)
   - 순서 보장에 사용

4. **Acknowledgment Number (32비트)**
   - 다음에 수신하기를 기대하는 바이트 번호
   - "SEQ + 1"을 ACK로 전송
   - ACK 플래그가 1일 때만 유효

5. **Data Offset (4비트)**
   - TCP 헤더 길이 (32비트 워드 단위)
   - 최소값: 5 (20바이트 헤더)
   - 최대값: 15 (60바이트 헤더, 옵션 포함)

6. **Reserved (3비트)**
   - 미래 사용을 위해 예약
   - 항상 0

7. **Control Flags (9비트)**
   - **CWR (Congestion Window Reduced)**: 혼잡 윈도우 감소 알림
   - **ECE (ECN-Echo)**: ECN 지원 표시
   - **URG (Urgent)**: Urgent Pointer 유효
   - **ACK (Acknowledgment)**: ACK 번호 유효
   - **PSH (Push)**: 수신 즉시 상위 계층 전달
   - **RST (Reset)**: 연결 강제 종료
   - **SYN (Synchronize)**: 연결 요청
   - **FIN (Finish)**: 연결 정상 종료 요청

8. **Window Size (16비트)**
   - 수신 가능한 데이터 크기 (바이트)
   - 흐름 제어용
   - 수신 버퍼의 여유 공간 표시
   - 0이면 송신 중지 요청

9. **Checksum (16비트)**
   - 헤더와 데이터의 오류 검출
   - Pseudo Header 포함 계산
     - Source IP, Dest IP, Protocol, TCP Length

10. **Urgent Pointer (16비트)**
    - URG 플래그가 1일 때 유효
    - 긴급 데이터의 마지막 바이트 위치

11. **Options (가변 길이)**
    - 최대 40바이트
    - 주요 옵션:
      - **MSS (Maximum Segment Size)**: 수신 가능한 최대 세그먼트 크기
      - **Window Scale**: Window Size 확장 (최대 1GB)
      - **Timestamp**: RTT 측정, PAWS (Protect Against Wrapped Sequences)
      - **SACK (Selective Acknowledgment)**: 선택적 재전송

#### TCP 3-Way Handshake (연결 수립)

```
Client                                Server
  |                                      |
  |      SYN, SEQ=100                    |
  |------------------------------------->|
  |                                      | (1) SYN 수신
  |                                      | - CLOSED → SYN_RECEIVED
  |                                      | - 포트 리스닝 확인
  |                                      | - 자원 할당
  |                                      |
  |      SYN+ACK, SEQ=300, ACK=101       |
  |<-------------------------------------|
  | (2) SYN+ACK 수신                     |
  | - SYN_SENT → ESTABLISHED             |
  | - 서버의 SEQ 확인                    |
  |                                      |
  |      ACK, SEQ=101, ACK=301           |
  |------------------------------------->|
  |                                      | (3) ACK 수신
  |                                      | - SYN_RECEIVED → ESTABLISHED
  |                                      | - 연결 완전 수립
  |                                      |
  | <===== 데이터 전송 가능 =====>       |
  |                                      |
```

**상세 과정**

**Step 1: Client → Server (SYN)**
- **TCP Flags**: SYN = 1
- **SEQ**: 100 (임의의 초기 시퀀스 번호, ISN)
- **ACK**: 0 (아직 ACK 아님)
- **의미**: "연결을 시작하고 싶습니다. 내 SEQ는 100부터 시작합니다."
- **Client 상태**: CLOSED → SYN_SENT
- **보안**: SYN Flooding 공격 가능 지점

**Step 2: Server → Client (SYN+ACK)**
- **TCP Flags**: SYN = 1, ACK = 1
- **SEQ**: 300 (서버의 ISN)
- **ACK**: 101 (클라이언트 SEQ + 1)
- **의미**: "연결 요청 수락합니다. 내 SEQ는 300부터 시작하고, 당신의 다음 SEQ 101을 기다립니다."
- **Server 상태**: LISTEN → SYN_RECEIVED
- **리소스 할당**: 연결을 위한 메모리 및 버퍼 할당

**Step 3: Client → Server (ACK)**
- **TCP Flags**: ACK = 1
- **SEQ**: 101
- **ACK**: 301 (서버 SEQ + 1)
- **의미**: "연결 수립 완료. 이제 데이터를 보낼 수 있습니다."
- **Client 상태**: SYN_SENT → ESTABLISHED
- **Server 상태**: SYN_RECEIVED → ESTABLISHED

**핵심 개념**
- **Sequence Number 교환**: 양방향 데이터 전송을 위한 시작점 합의
- **Full Duplex**: 연결 수립 후 양방향 동시 전송 가능
- **SYN Queue**: 서버는 SYN_RECEIVED 상태의 연결을 큐에 보관 (SYN Flooding 공격 대상)

#### TCP 4-Way Handshake (연결 종료)

```
Client                                Server
  |                                      |
  |      FIN, SEQ=500                    |
  |------------------------------------->|
  | (1) 클라이언트가 종료 시작           | (2) FIN 수신
  | - ESTABLISHED → FIN_WAIT_1           | - ESTABLISHED → CLOSE_WAIT
  |                                      | - 애플리케이션에 종료 알림
  |                                      |
  |      ACK, ACK=501                    |
  |<-------------------------------------|
  | (3) ACK 수신                         |
  | - FIN_WAIT_1 → FIN_WAIT_2            | - 아직 전송할 데이터 있을 수 있음
  |                                      | - 애플리케이션 종료 대기
  |                                      |
  |      FIN, SEQ=700                    |
  |<-------------------------------------|
  |                                      | (4) 서버도 종료 준비 완료
  | (5) FIN 수신                         | - CLOSE_WAIT → LAST_ACK
  | - FIN_WAIT_2 → TIME_WAIT             |
  |                                      |
  |      ACK, ACK=701                    |
  |------------------------------------->|
  | (6) TIME_WAIT 시작                   | (7) ACK 수신
  | - 2MSL 대기 (보통 60초~4분)          | - LAST_ACK → CLOSED
  |   Why? 지연 패킷 처리 위해           |
  |                                      |
  | (8) TIME_WAIT 종료                   |
  | - TIME_WAIT → CLOSED                 |
  |                                      |
```

**상세 과정**

**Step 1: Client → Server (FIN)**
- **TCP Flags**: FIN = 1, ACK = 1
- **SEQ**: 500 (마지막 전송 데이터의 다음 번호)
- **의미**: "더 이상 보낼 데이터가 없습니다."
- **Client 상태**: ESTABLISHED → FIN_WAIT_1
- **주의**: 클라이언트는 여전히 데이터 수신 가능 (Half-Close)

**Step 2: Server → Client (ACK)**
- **TCP Flags**: ACK = 1
- **ACK**: 501
- **의미**: "종료 요청 확인했습니다."
- **Server 상태**: ESTABLISHED → CLOSE_WAIT
- **처리**: 남은 데이터 전송 완료 대기

**Step 3: Server → Client (FIN)**
- **TCP Flags**: FIN = 1, ACK = 1
- **SEQ**: 700
- **의미**: "저도 이제 종료합니다."
- **Server 상태**: CLOSE_WAIT → LAST_ACK

**Step 4: Client → Server (ACK)**
- **TCP Flags**: ACK = 1
- **ACK**: 701
- **의미**: "종료 확인했습니다."
- **Client 상태**: FIN_WAIT_2 → TIME_WAIT

**TIME_WAIT 상태의 중요성**
- **지속 시간**: 2 × MSL (Maximum Segment Lifetime)
  - MSL: 30초~2분 (일반적으로 30초)
  - 총 TIME_WAIT: 1~4분
- **존재 이유**:
  1. 지연된 패킷 처리: 이전 연결의 패킷이 새 연결에 영향 방지
  2. 마지막 ACK 재전송: 서버가 ACK를 못 받으면 FIN 재전송, 클라이언트는 TIME_WAIT에서 재응답
  3. 포트 재사용 방지: 같은 포트를 즉시 재사용 시 혼선 방지

#### TCP 신뢰성 보장 메커니즘

**1. Sequence Number와 Acknowledgment**
```
Sender                          Receiver
  |  SEQ=100, Data(10바이트)      |
  |------------------------------>|
  |                               | Data 수신 확인
  |      ACK=110                  | "다음은 110부터 주세요"
  |<------------------------------|
  |  SEQ=110, Data(20바이트)      |
  |------------------------------>|
  |                               |
  |      ACK=130                  |
  |<------------------------------|
```

**2. Timeout과 재전송 (Retransmission)**
```
Sender                          Receiver
  |  SEQ=100, Data               |
  |------------------------------>| (패킷 손실!)
  |                               |
  | <타임아웃 대기>               |
  |                               |
  |  SEQ=100, Data (재전송)       |
  |------------------------------>|
  |                               |
  |      ACK=110                  |
  |<------------------------------|
```

**RTT (Round Trip Time) 기반 Timeout 계산**
- **측정**: SYN-SYN/ACK, 데이터-ACK 간 시간 측정
- **계산**: Exponential Weighted Moving Average (EWMA)
  ```
  EstimatedRTT = (1-α) × EstimatedRTT + α × SampleRTT
  DevRTT = (1-β) × DevRTT + β × |SampleRTT - EstimatedRTT|
  Timeout = EstimatedRTT + 4 × DevRTT
  ```
- **적응형**: 네트워크 상태에 따라 동적 조정

**3. 순서 보장 (Ordering)**
```
Sender                          Receiver
  |  SEQ=100 (패킷 1)            |
  |----------------------------->|
  |  SEQ=110 (패킷 2)            |
  |----------X (지연)            |
  |  SEQ=120 (패킷 3)            |
  |----------------------------->| 수신: 100, 120
  |                              | 버퍼에 120 보관
  |         (패킷 2 도착)        |
  |<-----------------------------|
  |                              | 수신: 110
  |      ACK=130                 | 순서 맞춰 상위 계층 전달
  |<-----------------------------|
```

**4. 중복 ACK와 Fast Retransmit**
```
Sender                          Receiver
  |  SEQ=100                     |
  |----------------------------->| ACK=110
  |  SEQ=110 (손실!)             |
  |----------X                   |
  |  SEQ=120                     |
  |----------------------------->| ACK=110 (중복)
  |  SEQ=130                     |
  |----------------------------->| ACK=110 (중복)
  |  SEQ=140                     |
  |----------------------------->| ACK=110 (중복, 3번째)
  |                              |
  | <3 Duplicate ACKs 감지>      |
  |  SEQ=110 (즉시 재전송!)      |
  |----------------------------->|
  |                              |
  |      ACK=150                 | 모든 데이터 수신 완료
  |<-----------------------------|
```

#### TCP 흐름 제어 (Flow Control)

**Sliding Window 메커니즘**

```
Sender's View:
[이미 ACK 받음][전송했으나 ACK 대기 중][전송 가능][전송 불가]
                └──────── Window Size ────────┘

Receiver's View:
[이미 수신][수신 가능 (버퍼 여유)][버퍼 초과]
           └──── Window Size ────┘
```

**동작 예시**
```
Sender                               Receiver (Window=4000)
  |  Data(1000바이트), SEQ=1          |
  |--------------------------------->| Buffer: 1000/4000
  |  Data(1000바이트), SEQ=1001       |
  |--------------------------------->| Buffer: 2000/4000
  |  Data(1000바이트), SEQ=2001       |
  |--------------------------------->| Buffer: 3000/4000
  |                                  |
  |      ACK=3001, Window=1000       | Buffer: 3000/4000
  |<---------------------------------| (Window 축소!)
  |                                  |
  |  Data(1000바이트), SEQ=3001       |
  |--------------------------------->| Buffer: 4000/4000 (Full!)
  |                                  |
  |      ACK=4001, Window=0          | (송신 중지 요청)
  |<---------------------------------|
  |                                  |
  | <송신 대기>                      | 애플리케이션이 데이터 읽음
  |                                  | Buffer: 0/4000
  |      Window Update, Window=4000  |
  |<---------------------------------|
  |  Data(1000바이트), SEQ=4001       | (재개!)
  |--------------------------------->|
```

**Zero Window 처리**
- **Zero Window Probe**: 주기적으로 1바이트 데이터 전송
- **Window Update**: 수신자가 Window > 0 알림

#### TCP 혼잡 제어 (Congestion Control)

**목적**: 네트워크 혼잡 방지 및 공평한 대역폭 사용

**1. Slow Start (느린 시작)**
```
초기 cwnd (Congestion Window) = 1 MSS

Round 1:  cwnd = 1    → 1 세그먼트 전송
          ACK 수신   → cwnd = 2

Round 2:  cwnd = 2    → 2 세그먼트 전송
          ACK 수신   → cwnd = 4

Round 3:  cwnd = 4    → 4 세그먼트 전송
          ACK 수신   → cwnd = 8

...지수적 증가 (cwnd 2배씩)...

ssthresh (Slow Start Threshold) 도달 시
→ Congestion Avoidance로 전환
```

**2. Congestion Avoidance (혼잡 회피)**
```
cwnd >= ssthresh 이후:

Round N:   cwnd = 16   → 16 세그먼트 전송
           ACK 수신   → cwnd = 17 (1 MSS씩 증가)

Round N+1: cwnd = 17   → 17 세그먼트 전송
           ACK 수신   → cwnd = 18

...선형 증가 (1 MSS씩)...

패킷 손실 감지 시 → 혼잡 발생으로 판단
```

**3. Fast Retransmit (빠른 재전송)**
```
3 Duplicate ACKs 수신:
→ 즉시 해당 세그먼트 재전송
→ ssthresh = cwnd / 2
→ cwnd = ssthresh + 3 MSS
→ Fast Recovery로 전환
```

**4. Fast Recovery (빠른 회복)**
```
Fast Retransmit 후:
- 중복 ACK 수신마다 cwnd += 1 MSS (일시적 증가)
- 새로운 ACK 수신 시:
  → cwnd = ssthresh
  → Congestion Avoidance로 복귀

Timeout 발생 시:
- ssthresh = cwnd / 2
- cwnd = 1 MSS
- Slow Start로 재시작
```

**혼잡 제어 그래프**
```
cwnd
 │
 │     /\      /\      /\
 │    /  \    /  \    /  \
 │   /    \  /    \  /    \
 │  /      \/      \/      \
 │ /    CA  |\  CA  |\  CA  \
 │/SS       | \     | \      \
 └──────────┴──┴────┴──┴──────→ Time
            │      │      │
         Timeout 3DupACK Timeout

SS: Slow Start
CA: Congestion Avoidance
```

---

### UDP (User Datagram Protocol)

#### UDP 특징
- **비연결형 (Connectionless)**
  - 사전 연결 수립 없음
  - 즉시 데이터 전송
- **비신뢰성 (Unreliable)**
  - 전송 보장 안 함
  - 순서 보장 안 함
  - 재전송 없음
- **낮은 오버헤드**
  - 헤더 8바이트 (TCP는 최소 20바이트)
  - 빠른 전송 속도
- **적합한 용도**:
  - 실시간 스트리밍 (VoIP, 동영상)
  - DNS 쿼리
  - DHCP
  - SNMP
  - 온라인 게임

#### UDP 데이터그램 구조

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|             Length            |           Checksum            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                             Data                              |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**필드별 설명**

1. **Source Port (16비트)**
   - 송신 프로세스의 포트 번호
   - 응답이 필요 없으면 0 가능

2. **Destination Port (16비트)**
   - 수신 프로세스의 포트 번호
   - 필수 항목

3. **Length (16비트)**
   - UDP 헤더 + 데이터의 총 길이
   - 최소값: 8바이트 (헤더만)
   - 최대값: 65535바이트

4. **Checksum (16비트)**
   - 오류 검출용
   - IPv4에서는 선택 사항 (IPv6에서는 필수)
   - Pseudo Header 포함 계산

#### TCP vs UDP 비교

| 특징 | TCP | UDP |
|------|-----|-----|
| **연결 방식** | 연결 지향 (3-Way Handshake) | 비연결형 |
| **신뢰성** | 보장 (ACK, 재전송) | 보장 안 함 |
| **순서** | 보장 (Sequence Number) | 보장 안 함 |
| **흐름 제어** | 있음 (Sliding Window) | 없음 |
| **혼잡 제어** | 있음 (Slow Start, CA) | 없음 |
| **헤더 크기** | 20~60바이트 | 8바이트 |
| **속도** | 느림 (오버헤드 큼) | 빠름 |
| **오버헤드** | 높음 | 낮음 |
| **사용 사례** | HTTP, FTP, SSH, Email | DNS, VoIP, 스트리밍, DHCP |
| **브로드캐스트** | 지원 안 함 | 지원 |
| **멀티캐스트** | 지원 안 함 | 지원 |

### 관련 장비
- 방화벽 (Firewall)
- L4 스위치 (Load Balancer)

### 용어 설명
- **Port Number**: 프로세스 식별자 (0~65535)
- **Socket**: IP 주소 + Port 번호 조합
  - 예: 192.168.1.100:80
- **Ephemeral Port**: 클라이언트가 사용하는 임시 포트 (49152~65535)
- **MSS (Maximum Segment Size)**: 수신 가능한 최대 세그먼트 크기
  - 일반적으로 MTU - IP 헤더 - TCP 헤더 = 1460바이트
- **RTT (Round Trip Time)**: 패킷이 왕복하는 시간
- **Throughput**: 단위 시간당 전송되는 데이터양

---

## Layer 3: 네트워크 계층 (Network Layer)

### 역할
- 서로 다른 네트워크 간의 통신 경로 설정
- 패킷의 라우팅 (경로 결정)
- 논리적 주소 (IP 주소) 지정
- 패킷 단편화 및 재조립

### PDU (Protocol Data Unit)
- **명칭**: Packet (패킷)

### 주요 프로토콜

**IP (Internet Protocol)**
- **IPv4**: 32비트 주소 (약 43억 개)
- **IPv6**: 128비트 주소 (3.4×10^38개)
- **역할**:
  - 논리적 주소 지정
  - 라우팅
  - 패킷 단편화

**ICMP (Internet Control Message Protocol)**
- **목적**: 네트워크 진단 및 오류 보고
- **주요 메시지**:
  - Type 0: Echo Reply (Ping 응답)
  - Type 3: Destination Unreachable
  - Type 8: Echo Request (Ping 요청)
  - Type 11: Time Exceeded (TTL 만료)

**IGMP (Internet Group Management Protocol)**
- **목적**: 멀티캐스트 그룹 관리
- **동작**: 호스트와 라우터 간 그룹 멤버십 정보 교환

**ARP (Address Resolution Protocol)**
- **목적**: IP 주소 → MAC 주소 변환
- **동작**: Broadcast Request, Unicast Reply
- **위치**: 논리적으로는 L3이지만 L2와 L3 사이

**라우팅 프로토콜**
- **RIP (Routing Information Protocol)**
  - Distance Vector 알고리즘
  - 최대 15 홉
- **OSPF (Open Shortest Path First)**
  - Link State 알고리즘
  - 대규모 네트워크 적합
- **BGP (Border Gateway Protocol)**
  - AS (Autonomous System) 간 라우팅
  - 인터넷 백본 프로토콜

### 관련 장비
- 라우터 (Router)
- L3 스위치

### 용어 설명
- **Routing**: 패킷의 최적 경로 결정
- **Forwarding**: 결정된 경로로 패킷 전달
- **Hop**: 라우터를 거치는 단계
- **TTL (Time To Live)**: 패킷의 생존 시간 (홉 카운트)
- **Fragmentation**: MTU 초과 시 패킷 분할
- **Routing Table**: 경로 정보를 저장하는 테이블

---

## Layer 2: 데이터 링크 계층 (Data Link Layer)

### 역할
- 같은 네트워크 내 노드 간 데이터 전송
- 물리 주소 (MAC 주소) 지정
- 오류 검출 및 정정
- 프레임 동기화
- 매체 접근 제어 (MAC)

### PDU (Protocol Data Unit)
- **명칭**: Frame (프레임)

### Ethernet 프레임 구조

```
┌─────────────┬───────────────┬──────────────┬──────┬─────────┬─────┐
│  Preamble   │ Dest MAC (6B) │ Src MAC (6B) │ Type │ Payload │ FCS │
│  (7 bytes)  │               │              │ (2B) │(46-1500)│(4B) │
│     +       │               │              │      │         │     │
│  SFD (1B)   │               │              │      │         │     │
└─────────────┴───────────────┴──────────────┴──────┴─────────┴─────┘
```

**필드별 설명**

1. **Preamble (7바이트)**
   - 비트 패턴: 10101010 × 7
   - 송수신 동기화

2. **SFD (Start Frame Delimiter, 1바이트)**
   - 비트 패턴: 10101011
   - 프레임 시작 표시

3. **Destination MAC Address (6바이트)**
   - 수신자 MAC 주소
   - Unicast / Multicast / Broadcast

4. **Source MAC Address (6바이트)**
   - 송신자 MAC 주소

5. **EtherType/Length (2바이트)**
   - 상위 프로토콜 식별
   - 0x0800: IPv4
   - 0x0806: ARP
   - 0x86DD: IPv6

6. **Payload (46~1500바이트)**
   - 실제 데이터
   - 최소: 46바이트 (미달 시 패딩)
   - 최대: 1500바이트 (MTU)

7. **FCS (Frame Check Sequence, 4바이트)**
   - CRC-32 오류 검출
   - 프레임 무결성 확인

### 주요 프로토콜
- **IEEE 802.3 (Ethernet)**
- **IEEE 802.11 (무선 LAN)**
- **PPP (Point-to-Point Protocol)**

### 관련 장비
- 브리지 (Bridge)
- L2 스위치 (Switch)

### 용어 설명
- **MAC Address**: 48비트 물리 주소 (예: 00:1A:2B:3C:4D:5E)
- **Collision Domain**: 충돌이 발생하는 범위
- **Broadcast Domain**: 브로드캐스트가 전파되는 범위
- **MTU (Maximum Transmission Unit)**: 최대 전송 단위 (일반적으로 1500바이트)
- **CSMA/CD**: 이더넷의 매체 접근 제어 방식

---

## Layer 1: 물리 계층 (Physical Layer)

### 역할
- 비트 스트림을 물리적 신호로 변환
- 전송 매체를 통한 신호 전송
- 전기적, 기계적 사양 정의

### PDU (Protocol Data Unit)
- **명칭**: Bit Stream (비트 스트림)

### 전송 매체

**유선**
- **UTP 케이블 (Unshielded Twisted Pair)**
  - Cat 5e: 1Gbps
  - Cat 6: 10Gbps (55m)
  - Cat 6A: 10Gbps (100m)
- **광케이블 (Fiber Optic)**
  - 단일 모드: 장거리 (~70km)
  - 다중 모드: 단거리 (~550m)

**무선**
- **2.4GHz 대역**: 802.11b/g/n
- **5GHz 대역**: 802.11a/n/ac/ax

### 관련 장비
- 리피터 (Repeater)
- 허브 (Hub)
- NIC (Network Interface Card)
- 미디어 컨버터 (Media Converter)
- 액세스 포인트 (AP)

### 용어 설명
- **Bit Rate (bps)**: 초당 전송 비트 수
- **Bandwidth**: 전송 가능한 주파수 범위
- **Attenuation**: 신호 감쇠
- **Duplex Mode**:
  - Simplex: 단방향
  - Half-Duplex: 양방향 교대
  - Full-Duplex: 양방향 동시

---

## 2. TCP/IP 4계층 모델

### 2.1 TCP/IP 모델 개요

**역사**
- ARPANET에서 개발한 NCP의 후속 버전
- 실용성 중심의 설계
- 현재 인터넷의 표준 프로토콜 스택

**OSI 7계층과의 매핑**

```
OSI 7계층                TCP/IP 4계층
┌──────────────┐
│ Application  │
├──────────────┤        ┌──────────────┐
│Presentation  │        │              │
├──────────────┤   →    │ Application  │
│   Session    │        │              │
├──────────────┤        └──────────────┘
│  Transport   │   →    │  Transport   │
├──────────────┤        ├──────────────┤
│   Network    │   →    │   Internet   │
├──────────────┤        ├──────────────┤
│  Data Link   │        │              │
├──────────────┤   →    │Network Access│
│   Physical   │        │              │
└──────────────┘        └──────────────┘
```

### 2.2 TCP/IP 계층별 설명

**Layer 4: Application Layer (응용 계층)**
- OSI의 5~7계층 통합
- 사용자 애플리케이션에 네트워크 서비스 제공
- 프로토콜: HTTP, FTP, SMTP, DNS, SSH 등

**Layer 3: Transport Layer (전송 계층)**
- OSI의 4계층과 동일
- 프로세스 간 통신
- 프로토콜: TCP, UDP

**Layer 2: Internet Layer (인터넷 계층)**
- OSI의 3계층과 유사
- 패킷 라우팅
- 프로토콜: IP, ICMP, ARP, IGMP

**Layer 1: Network Access Layer (네트워크 접근 계층)**
- OSI의 1~2계층 통합
- 물리적 네트워크 접근
- 프로토콜: Ethernet, WiFi

---

## 3. 데이터 캡슐화와 역캡슐화

### 3.1 캡슐화 (Encapsulation) 과정

**송신 측에서 일어나는 일**

```
Application Layer
     │
     │ Application Data
     ▼
┌──────────────┐
│  HTTP Data   │
└──────────────┘
     │
     │ (7→4 계층)
     ▼
Transport Layer
┌─────┬──────────────┐
│ TCP │  HTTP Data   │  ← TCP Segment
└─────┴──────────────┘
     │
     │
     ▼
Network Layer
┌────┬─────┬──────────────┐
│ IP │ TCP │  HTTP Data   │  ← IP Packet
└────┴─────┴──────────────┘
     │
     │
     ▼
Data Link Layer
┌─────┬────┬─────┬──────────────┬─────┐
│ Eth │ IP │ TCP │  HTTP Data   │ FCS │  ← Ethernet Frame
└─────┴────┴─────┴──────────────┴─────┘
     │
     │
     ▼
Physical Layer
01010101010101010...  ← Bit Stream
```

**단계별 상세**

**Step 1: Application Layer**
- 애플리케이션 데이터 생성
- 예: "GET /index.html HTTP/1.1"

**Step 2: Transport Layer**
- TCP 헤더 추가
  - Source Port: 50000 (클라이언트 임시 포트)
  - Dest Port: 80 (HTTP)
  - SEQ, ACK, Flags, Window, Checksum 등
- PDU: Segment

**Step 3: Network Layer**
- IP 헤더 추가
  - Source IP: 192.168.1.100
  - Dest IP: 93.184.216.34
  - TTL, Protocol (6=TCP), Checksum 등
- PDU: Packet

**Step 4: Data Link Layer**
- Ethernet 헤더 추가
  - Source MAC: 00:1A:2B:3C:4D:5E
  - Dest MAC: Gateway MAC (ARP로 획득)
  - EtherType: 0x0800 (IPv4)
- Ethernet 트레일러 추가
  - FCS (CRC-32 오류 검출)
- PDU: Frame

**Step 5: Physical Layer**
- 프레임을 비트 스트림으로 변환
- 전기 신호, 광 신호 또는 전파로 전송

### 3.2 역캡슐화 (Decapsulation) 과정

**수신 측에서 일어나는 일**

```
Physical Layer
01010101010101010...  ← Bit Stream 수신
     │
     │ 비트를 프레임으로 재조립
     ▼
Data Link Layer
┌─────┬────┬─────┬──────────────┬─────┐
│ Eth │ IP │ TCP │  HTTP Data   │ FCS │
└─────┴────┴─────┴──────────────┴─────┘
     │
     │ 1. FCS 검증
     │ 2. Dest MAC 확인 (내 MAC인가?)
     │ 3. Ethernet 헤더 제거
     ▼
Network Layer
┌────┬─────┬──────────────┐
│ IP │ TCP │  HTTP Data   │
└────┴─────┴──────────────┘
     │
     │ 1. Checksum 검증
     │ 2. TTL 감소
     │ 3. Dest IP 확인 (내 IP인가?)
     │ 4. Protocol 확인 (6=TCP)
     │ 5. IP 헤더 제거
     ▼
Transport Layer
┌─────┬──────────────┐
│ TCP │  HTTP Data   │
└─────┴──────────────┘
     │
     │ 1. Checksum 검증
     │ 2. SEQ, ACK 확인
     │ 3. Dest Port 확인 (80=HTTP 프로세스)
     │ 4. TCP 헤더 제거
     ▼
Application Layer
┌──────────────┐
│  HTTP Data   │  ← 애플리케이션으로 전달
└──────────────┘
```

### 3.3 계층별 PDU 정리

| OSI 계층 | PDU 명칭 | 주요 정보 |
|----------|---------|----------|
| L7-L5 (Application~Session) | Message/Data | 애플리케이션 데이터 |
| L4 (Transport) | Segment (TCP)<br>Datagram (UDP) | Port 번호, SEQ, ACK |
| L3 (Network) | Packet | IP 주소, TTL, Protocol |
| L2 (Data Link) | Frame | MAC 주소, EtherType, FCS |
| L1 (Physical) | Bit Stream | 전기/광 신호, 비트열 |

---

## 4. 프로토콜의 핵심 개념

### 4.1 Connection-Oriented vs Connectionless

**연결 지향 (Connection-Oriented)**
- **대표**: TCP
- **특징**:
  - 사전 연결 수립 (3-Way Handshake)
  - 신뢰성 보장
  - 순서 보장
  - 오버헤드 큼
- **적합**: 파일 전송, 웹, 이메일

**비연결형 (Connectionless)**
- **대표**: UDP
- **특징**:
  - 연결 수립 없음
  - 신뢰성 보장 안 함
  - 순서 보장 안 함
  - 오버헤드 작음
- **적합**: 실시간 스트리밍, DNS, DHCP

### 4.2 프로토콜 스택의 장점

**1. 모듈화 (Modularity)**
- 계층별 독립 개발 가능
- 특정 계층 변경 시 다른 계층 영향 최소화

**2. 표준화 (Standardization)**
- 벤더 독립적
- 상호 운용성 보장

**3. 재사용성 (Reusability)**
- 하위 계층 서비스를 여러 상위 계층에서 활용

**4. 유지보수 용이성**
- 문제 발생 시 특정 계층 격리
- 디버깅 용이

---

## 5. 실전 예제: 웹 브라우저 접속 시 계층별 동작

### 시나리오
사용자가 "https://www.example.com" 입력

### 단계별 처리

**Step 1: DNS 조회 (Application Layer)**
```
1. 브라우저가 www.example.com의 IP 주소 필요
2. DNS Resolver에 쿼리 (UDP 53번 포트)
3. DNS 응답: 93.184.216.34
```

**Step 2: TCP 연결 수립 (Transport Layer)**
```
Client (192.168.1.100:50000) → Server (93.184.216.34:443)

1. SYN, SEQ=1000
2. SYN+ACK, SEQ=5000, ACK=1001
3. ACK, SEQ=1001, ACK=5001

→ ESTABLISHED
```

**Step 3: TLS Handshake (Application/Presentation)**
```
1. ClientHello: 지원하는 암호화 알고리즘 목록
2. ServerHello: 선택한 암호화 알고리즘, 인증서
3. 키 교환, 암호화 시작
4. HTTP 데이터는 TLS로 암호화되어 전송
```

**Step 4: HTTP 요청 (Application Layer)**
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
```

**Step 5: 캡슐화 (각 계층)**
```
[TLS Header | HTTP Data]
     ↓ (TCP)
[TCP Header | TLS | HTTP]
     ↓ (IP)
[IP Header | TCP | TLS | HTTP]
     ↓ (Ethernet)
[Eth Header | IP | TCP | TLS | HTTP | FCS]
     ↓ (Physical)
01010101...
```

**Step 6: 라우팅 (Network Layer)**
```
1. 라우팅 테이블 확인
2. Default Gateway로 전송
3. 여러 라우터를 거쳐 목적지까지 (각 홉마다 TTL -1)
```

**Step 7: 서버 수신 및 응답**
```
1. 역캡슐화
2. HTTP 요청 처리
3. HTTP 응답 생성
4. 캡슐화하여 클라이언트로 전송
```

---

## 6. 실습 과제

### 과제 1: Wireshark로 TCP 3-Way Handshake 캡처
```bash
# 실습 환경
1. Wireshark 실행
2. 네트워크 인터페이스 선택
3. Display Filter: tcp.flags.syn == 1 or tcp.flags.fin == 1
4. 웹 브라우저로 http://example.com 접속
5. SYN, SYN+ACK, ACK 패킷 확인
```

**확인 사항**
- [ ] SYN 패킷의 Flags 확인 (SYN=1, ACK=0)
- [ ] Sequence Number 값 기록
- [ ] SYN+ACK 패킷의 Acknowledgment Number 확인 (SEQ+1)
- [ ] 최종 ACK 패킷 확인

### 과제 2: OSI 7계층 별 프로토콜 매핑
```
각 계층에 속하는 프로토콜 3개씩 나열하고 역할 설명
```

### 과제 3: Ping 명령어로 ICMP 패킷 분석
```bash
# Windows
ping -n 4 8.8.8.8

# Linux
ping -c 4 8.8.8.8
```

**확인 사항**
- [ ] ICMP Echo Request (Type 8) 패킷 구조
- [ ] ICMP Echo Reply (Type 0) 응답
- [ ] TTL 값 확인 (라우터 홉 수 추정)
- [ ] RTT (Round Trip Time) 측정

### 과제 4: TCP vs UDP 비교표 작성
```
항목별로 두 프로토콜의 차이점을 상세히 비교
```

---

## 7. 연결 포인트 (다른 Phase와의 관계)

### Phase 1.2: Address System과의 연결
→ **MAC 주소 (L2)**: 같은 네트워크 내 통신
→ **IP 주소 (L3)**: 다른 네트워크 간 통신
→ **Port 번호 (L4)**: 프로세스 식별

### Phase 2.1: Scanning/Sniffing과의 연결
→ **Port Scanning**: L4의 Port 개념 악용
→ **Sniffing**: L2의 Promiscuous Mode 악용

### Phase 2.2: Spoofing과의 연결
→ **IP Spoofing**: L3의 출발지 IP 위조
→ **ARP Spoofing**: L2-L3 간 주소 매핑 조작

### Phase 2.3: Session Hijacking과의 연결
→ **TCP Sequence Number** 예측 공격
→ 3-Way Handshake 메커니즘 이해 필수

### Phase 2.4: DoS/DDoS와의 연결
→ **SYN Flooding**: TCP 3-Way Handshake 악용
→ **UDP Flooding**: UDP의 비연결 특성 악용

### Phase 3.1: Firewall과의 연결
→ 각 계층별 필터링 규칙 적용
→ L3 (IP 주소), L4 (Port 번호), L7 (Application 데이터)

### Phase 4.1: Packet Analysis와의 연결
→ Wireshark로 실제 캡슐화/역캡슐화 과정 확인
→ 각 계층의 헤더 필드 분석

---

## 8. 핵심 요약

### 반드시 기억해야 할 개념

**OSI 7계층**
1. Physical: 비트 스트림, 전기 신호
2. Data Link: MAC 주소, Frame, 오류 검출
3. Network: IP 주소, Packet, 라우팅
4. Transport: Port 번호, Segment/Datagram, 신뢰성
5. Session: 세션 관리, 동기화
6. Presentation: 데이터 변환, 암호화
7. Application: 사용자 서비스

**TCP/IP 4계층**
1. Network Access = Physical + Data Link
2. Internet = Network
3. Transport = Transport
4. Application = Session + Presentation + Application

**TCP의 핵심**
- 3-Way Handshake: SYN → SYN+ACK → ACK
- 4-Way Handshake: FIN → ACK → FIN → ACK
- 신뢰성: SEQ, ACK, Timeout, 재전송
- 흐름 제어: Sliding Window
- 혼잡 제어: Slow Start, Congestion Avoidance

**캡슐화**
- Data → Segment → Packet → Frame → Bits
- 각 계층에서 헤더 추가
- 수신 측에서 역순으로 헤더 제거

---

## 9. 자가 점검

### 이해도 체크리스트
- [ ] OSI 7계층의 각 계층 역할을 설명할 수 있다
- [ ] TCP와 UDP의 차이를 명확히 설명할 수 있다
- [ ] TCP 3-Way Handshake 과정을 그림으로 그릴 수 있다
- [ ] 데이터 캡슐화 과정을 단계별로 설명할 수 있다
- [ ] 각 계층의 PDU 명칭을 정확히 말할 수 있다
- [ ] Sequence Number와 Acknowledgment의 관계를 이해한다
- [ ] 흐름 제어와 혼잡 제어의 차이를 설명할 수 있다
- [ ] 웹 브라우저 접속 시 각 계층에서 일어나는 일을 설명할 수 있다

---

**다음 학습**: Phase 1-2 Address System (주소 체계)
