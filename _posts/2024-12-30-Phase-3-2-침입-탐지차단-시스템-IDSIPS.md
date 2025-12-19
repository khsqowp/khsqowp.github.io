---
layout: post
title: "Phase 3-2: 침입 탐지/차단 시스템 (IDS/IPS)"
date: 2024-12-30 09:00:03 +0900
categories: [network, fundamentals]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 3-2: 침입 탐지/차단 시스템 (IDS/IPS)

## 학습 목표
- IDS와 IPS의 차이점과 동작 원리 이해
- Signature-based vs Anomaly-based 탐지 방법 파악
- Snort 규칙 작성 및 실전 활용
- False Positive/Negative 개념과 튜닝 방법 습득
- HIDS와 NIDS의 차이점 이해
- IDS/IPS 우회 기법과 대응 방안 학습

---

## 1. IDS/IPS 개요

### 1.1 정의

**IDS (Intrusion Detection System)**
- 침입 탐지 시스템
- 공격을 **탐지**하고 **경고**
- 수동적 (Passive)
- 로그, 알림 생성

**IPS (Intrusion Prevention System)**
- 침입 차단 시스템
- 공격을 **탐지**하고 **차단**
- 능동적 (Active)
- 패킷 DROP, 연결 차단

**비유**
```
IDS = 경보기
- 침입자 발견 → 소리 울림
- 실제 차단은 안 함

IPS = 자동 방어 시스템
- 침입자 발견 → 문 잠금
- 실시간 차단
```

### 1.2 IDS vs IPS

| 특성 | IDS | IPS |
|------|-----|-----|
| 모드 | Passive (수동) | Inline (능동) |
| 위치 | 네트워크 외부 (SPAN/TAP) | 트래픽 경로 내부 |
| 동작 | 탐지 + 알림 | 탐지 + 차단 |
| 지연 | 없음 | 약간 있음 (검사 시간) |
| False Positive 영향 | 알림만 | 정상 트래픽 차단 위험 |
| 우회 | 쉬움 (탐지만) | 어려움 (차단) |

**배치 위치**
```
IDS (Passive):
           ┌────────────┐
Internet ──┤  Firewall  ├── Internal Network
           └─────┬──────┘
                 │ (SPAN/Mirror Port)
             ┌───┴────┐
             │  IDS   │
             └────────┘
             (트래픽 복사본 수신)

IPS (Inline):
           ┌────────────┐    ┌─────┐
Internet ──┤  Firewall  ├────┤ IPS ├── Internal Network
           └────────────┘    └─────┘
                          (모든 트래픽 통과)
```

### 1.3 NIDS vs HIDS

**NIDS (Network-based IDS)**
```
위치: 네트워크 세그먼트
모니터링: 네트워크 트래픽
장점: 전체 네트워크 가시성
단점: 암호화 트래픽 분석 어려움

예: Snort, Suricata, Zeek
```

**HIDS (Host-based IDS)**
```
위치: 개별 호스트
모니터링: 시스템 로그, 파일 변경, 프로세스
장점: 암호화 후 데이터 확인, 정확한 탐지
단점: 각 호스트마다 설치 필요

예: OSSEC, Tripwire, Wazuh
```

---

## 2. 탐지 방법

### 2.1 Signature-based Detection (서명 기반)

**원리**
```
알려진 공격 패턴(Signature)과 매칭
→ 데이터베이스와 비교
→ 일치하면 탐지
```

**예시**
```
Signature: SQL Injection
Pattern: /\' OR 1=1 --/

Packet:
GET /login?username=admin' OR 1=1 -- HTTP/1.1

→ 매칭! → Alert
```

**Snort 규칙 예시**
```
alert tcp any any -> any 80 (msg:"SQL Injection Detected"; \
  content:"' OR 1=1"; nocase; sid:1000001;)

해석:
- alert: 경고
- tcp: TCP 프로토콜
- any any: 모든 출발지 IP:Port
- -> any 80: 모든 목적지 IP, Port 80
- msg: 메시지
- content: 매칭할 문자열
- nocase: 대소문자 무시
- sid: Signature ID
```

**장점**
```
- 정확함 (알려진 공격)
- False Positive 낮음
- 빠름
```

**단점**
```
- 새로운 공격(Zero-Day) 탐지 불가
- Signature DB 지속 업데이트 필요
- 변형 공격에 취약
```

### 2.2 Anomaly-based Detection (이상 기반)

**원리**
```
정상 행동 패턴 학습 (Baseline)
→ 이상 행동 탐지
```

**예시**
```
정상 패턴:
- 평균 트래픽: 100 Mbps
- 평균 연결 수: 500개
- 로그인 시간: 09:00~18:00

이상 행동:
- 갑자기 트래픽 1 Gbps → DDoS?
- 연결 수 10,000개 → Port Scan?
- 새벽 3시 로그인 → 계정 탈취?
```

**방법**

**통계 기반**
```
평균, 표준편차 계산
→ 임계값 이상 → 이상

예: 평균 + 3σ 초과
```

**Machine Learning**
```
정상 데이터로 학습
→ 분류 모델 생성
→ 새 데이터 분류 (정상/이상)

예: Isolation Forest, One-Class SVM
```

**장점**
```
- Zero-Day 공격 탐지 가능
- 새로운 공격에도 대응
```

**단점**
```
- False Positive 높음
- 학습 기간 필요
- 느림 (복잡한 계산)
```

### 2.3 Hybrid Approach (혼합)

**실전**
```
Signature + Anomaly

1. Signature로 알려진 공격 차단 (빠르고 정확)
2. Anomaly로 새로운 공격 탐지 (포괄적)
```

---

## 3. Snort

### 3.1 개요

**Snort**
- 오픈소스 NIDS/NIPS
- 가장 유명한 IDS
- Signature 기반
- Cisco 인수 (현재 무료)

**모드**
```
1. Sniffer Mode: 패킷 캡처만
2. Packet Logger: 패킷 로그 저장
3. NIDS Mode: 규칙 기반 탐지
```

### 3.2 Snort 규칙 구조

**기본 형식**
```
<action> <protocol> <src_ip> <src_port> <direction> <dst_ip> <dst_port> (options)
```

**Action**
```
alert: 경고 생성 + 로그
log: 로그만
pass: 무시
drop: 차단 (IPS 모드)
reject: 차단 + RST 전송
```

**예시**
```
alert tcp any any -> 192.168.1.0/24 22 (msg:"SSH Brute Force"; \
  flags:S; threshold:type both, track by_src, count 5, seconds 60; \
  sid:1000002;)

해석:
- alert tcp: TCP 패킷 경고
- any any: 모든 출발지
- -> 192.168.1.0/24 22: 내부 네트워크 SSH
- flags:S: SYN 플래그
- threshold: 60초 내 5번 이상
- 탐지: SSH Brute-Force
```

### 3.3 Snort 옵션

**content (문자열 매칭)**
```
content:"GET /admin"; nocase;
→ "GET /admin" 문자열 포함, 대소문자 무시
```

**pcre (정규표현식)**
```
pcre:"/\/admin\.(php|asp|jsp)/i";
→ /admin.php, /admin.asp, /admin.jsp
```

**flags (TCP 플래그)**
```
flags:S; → SYN
flags:SA; → SYN+ACK
flags:F; → FIN
flags:R; → RST
```

**flow**
```
flow:to_server,established;
→ 클라이언트 → 서버, 연결 수립됨
```

**threshold (임계값)**
```
threshold:type limit, track by_src, count 1, seconds 60;
→ 60초 동안 출발지당 1번만 알림

threshold:type threshold, track by_dst, count 10, seconds 60;
→ 60초 동안 목적지당 10번 초과 시 알림
```

**sid (Signature ID)**
```
sid:1000001;
→ 규칙 고유 ID (1,000,000 이상: 사용자 정의)
```

### 3.4 Snort 실전 규칙

**SQL Injection**
```
alert tcp any any -> any 80 (msg:"SQL Injection - UNION SELECT"; \
  flow:to_server,established; content:"UNION"; nocase; \
  content:"SELECT"; nocase; distance:0; \
  sid:1000010; rev:1;)
```

**XSS (Cross-Site Scripting)**
```
alert tcp any any -> any 80 (msg:"XSS - script tag"; \
  flow:to_server,established; content:"<script"; nocase; \
  sid:1000011; rev:1;)
```

**Port Scan 탐지**
```
alert tcp any any -> 192.168.1.0/24 any (msg:"Port Scan Detected"; \
  flags:S; threshold:type both, track by_src, count 20, seconds 10; \
  sid:1000012;)
```

**Reverse Shell**
```
alert tcp any any -> any any (msg:"Possible Reverse Shell"; \
  content:"bash -i"; content:"/dev/tcp/"; distance:0; \
  sid:1000013;)
```

### 3.5 Snort 설치 및 실행

**설치 (Ubuntu)**
```bash
sudo apt update
sudo apt install snort
```

**설정 파일**
```bash
sudo nano /etc/snort/snort.conf

# 네트워크 설정
ipvar HOME_NET 192.168.1.0/24
ipvar EXTERNAL_NET !$HOME_NET

# 규칙 파일 포함
include $RULE_PATH/local.rules
```

**사용자 규칙 작성**
```bash
sudo nano /etc/snort/rules/local.rules

# 규칙 추가
alert icmp any any -> $HOME_NET any (msg:"ICMP Ping Detected"; \
  itype:8; sid:1000001; rev:1;)

alert tcp any any -> $HOME_NET 22 (msg:"SSH Connection Attempt"; \
  flags:S; sid:1000002; rev:1;)
```

**실행**
```bash
# 규칙 테스트
sudo snort -T -c /etc/snort/snort.conf

# NIDS 모드 실행
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
# -A console: 콘솔에 경고 출력
# -q: Quiet
# -i: Interface

# 백그라운드 실행
sudo snort -D -c /etc/snort/snort.conf -i eth0 -l /var/log/snort
```

**로그 확인**
```bash
# 실시간 로그
sudo tail -f /var/log/snort/alert

# Barnyard2로 MySQL에 저장 (선택)
```

---

## 4. False Positive/Negative

### 4.1 개념

**Confusion Matrix**
```
                실제 공격    실제 정상
탐지 알림        TP          FP
탐지 안함        FN          TN

TP (True Positive): 공격을 공격으로 탐지 (정확)
FP (False Positive): 정상을 공격으로 탐지 (오탐)
FN (False Negative): 공격을 정상으로 간주 (미탐)
TN (True Negative): 정상을 정상으로 인식 (정확)
```

**False Positive (오탐)**
```
문제:
- 정상 트래픽을 공격으로 판단
- 알림 폭주
- 관리자 피로
- IPS: 정상 트래픽 차단 → 서비스 장애

예:
- 정상 스캔 도구 → Port Scan 탐지
- 정상 SQL 쿼리 → SQL Injection 탐지
```

**False Negative (미탐)**
```
문제:
- 실제 공격을 탐지 못 함
- 가장 위험

예:
- 변형된 공격
- 암호화된 공격
- Zero-Day
```

### 4.2 튜닝

**목표**
```
FP 감소 + FN 감소 (상충 관계)

Perfect IDS (불가능):
- FP = 0
- FN = 0
```

**FP 감소 방법**

**1. 임계값 조정**
```
before:
threshold:count 5, seconds 60

after:
threshold:count 20, seconds 60
→ 더 많은 이벤트 필요 → FP 감소, FN 증가 위험
```

**2. Whitelist**
```
pass tcp 192.168.1.100 any -> any 80 (msg:"Trusted Scanner"; \
  sid:2000001;)

→ 신뢰하는 IP는 무시
```

**3. Suppress (억제)**
```
suppress gen_id 1, sig_id 1000001, track by_src, ip 192.168.1.50

→ 특정 출발지 IP의 특정 규칙 무시
```

**FN 감소 방법**

**1. 규칙 추가**
```
- 다양한 변형 탐지
- 정규표현식 활용
```

**2. 민감도 증가**
```
임계값 낮춤
→ FN 감소, FP 증가
```

**3. Signature 업데이트**
```
최신 공격 패턴 반영
```

### 4.3 성능 지표

**Detection Rate (탐지율)**
```
= TP / (TP + FN)
= 실제 공격 중 탐지한 비율
```

**False Alarm Rate (오탐률)**
```
= FP / (FP + TN)
= 정상 중 오탐 비율
```

**Precision (정밀도)**
```
= TP / (TP + FP)
= 알림 중 실제 공격 비율
```

**목표**
```
Detection Rate ↑ (높게)
False Alarm Rate ↓ (낮게)
```

---

## 5. 기타 IDS/IPS 도구

### 5.1 Suricata

**특징**
```
- Snort 호환
- Multi-threading (빠름)
- IDS + IPS
- GPU 가속 지원
- 파일 추출 기능
```

**설치**
```bash
sudo apt install suricata

# 실행
sudo suricata -c /etc/suricata/suricata.yaml -i eth0

# 로그
tail -f /var/log/suricata/fast.log
```

### 5.2 Zeek (Bro)

**특징**
```
- Network Security Monitor
- 로그 중심 (Signature보다 분석)
- Scripting 언어 (정책 정의)
- 메타데이터 추출
```

**용도**
```
- 네트워크 가시성
- Forensics (포렌식)
- Threat Hunting
```

### 5.3 OSSEC (HIDS)

**특징**
```
- Host-based IDS
- 로그 분석
- 파일 무결성 검사
- Rootkit 탐지
- Active Response
```

**설치**
```bash
# 서버
wget https://github.com/ossec/ossec-hids/archive/3.7.0.tar.gz
tar -xzf 3.7.0.tar.gz
cd ossec-hids-3.7.0
sudo ./install.sh

# 설정
sudo /var/ossec/bin/ossec-control start
```

---

## 6. IDS/IPS 우회 기법

### 6.1 Fragmentation

**IP Fragmentation**
```
공격 패턴을 여러 Fragment로 분할
→ IDS가 재조립 안 하면 탐지 못 함

예:
"admin' OR 1=1"

Fragment 1: "adm"
Fragment 2: "in' OR"
Fragment 3: " 1=1"

→ 각 Fragment는 정상으로 보임
```

**방어**
```
Fragment 재조립 후 검사
Snort: frag3 preprocessor
```

### 6.2 Polymorphism (다형성)

**Encoding/Obfuscation**
```
공격 문자열 변형

SQL Injection:
' OR 1=1 --

변형:
%27%20OR%201%3D1%20--  (URL Encoding)
0x27204f522031 3d31202d2d  (Hex)
' OR 1=0x31  (Hex + Decimal)
```

**방어**
```
Normalization (정규화)
→ 모든 인코딩 디코딩 후 검사
```

### 6.3 Timing Attack

**Slow Attack**
```
매우 느리게 공격
→ Threshold 회피

예: Slowloris (HTTP DoS)
- 초당 1개 연결
- Threshold: 10개/초
→ 탐지 안 됨
```

**방어**
```
장기간 누적 분석
행동 기반 탐지
```

### 6.4 Encryption

**SSL/TLS**
```
암호화된 트래픽
→ IDS가 내용 확인 불가

공격자:
HTTPS로 Malware 다운로드
→ IDS Blind
```

**방어**
```
SSL Inspection (SSL Decryption)
→ Man-in-the-Middle (합법적)
→ Privacy 이슈
```

### 6.5 Evasion Tools

**Nmap 회피 옵션**
```bash
# Fragmentation
nmap -f target.com

# Decoy (디코이)
nmap -D RND:10 target.com
# 10개 가짜 IP와 함께 스캔

# Timing
nmap -T0 target.com
# 매우 느리게 (Paranoid)
```

---

## 7. 실습 과제

### 과제 1: Snort 설치 및 기본 탐지
```bash
# 1. Snort 설치
sudo apt install snort

# 2. 규칙 작성
sudo nano /etc/snort/rules/local.rules

alert icmp any any -> any any (msg:"ICMP Ping"; sid:1000001;)
alert tcp any any -> any 80 (msg:"HTTP Traffic"; sid:1000002;)

# 3. 실행
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0

# 4. 테스트
# 다른 터미널에서
ping localhost
curl http://localhost
```

### 과제 2: SQL Injection 탐지
```bash
# Snort 규칙
alert tcp any any -> any 80 (msg:"SQL Injection Detected"; \
  content:"UNION"; nocase; content:"SELECT"; nocase; \
  sid:1000010;)

# 테스트 (취약한 웹 앱 대상)
curl "http://localhost/search?q=test' UNION SELECT * FROM users--"

# Snort 로그 확인
```

### 과제 3: Port Scan 탐지
```bash
# Snort 규칙
alert tcp any any -> $HOME_NET any (msg:"Port Scan"; \
  flags:S; threshold:type both, track by_src, count 20, seconds 10; \
  sid:1000020;)

# 공격 시뮬레이션
nmap -sS 192.168.1.100

# 탐지 확인
```

---

## 8. 연결 포인트

### Phase 2.1: Scanning/Sniffing
→ **Port Scan 탐지**: SYN 플래그 임계값

### Phase 2.2: Spoofing
→ **ARP Spoofing 탐지**: ARP 패킷 이상

### Phase 2.4: DoS/DDoS
→ **SYN Flood 탐지**: SYN 패킷 급증

### Phase 3.1: Firewall
→ **통합**: NGFW = Firewall + IPS

### Phase 4.1: Packet Analysis
→ **로그 분석**: IDS 알림 조사

---

## 9. 핵심 요약

**IDS vs IPS**
- IDS: 탐지 + 알림
- IPS: 탐지 + 차단

**탐지 방법**
- Signature: 알려진 패턴 (정확, Zero-Day 취약)
- Anomaly: 이상 행동 (Zero-Day 가능, FP 높음)

**Snort**
- 오픈소스 NIDS
- Signature 기반
- 규칙: action protocol src → dst (options)

**False Positive/Negative**
- FP: 오탐 (정상 → 공격)
- FN: 미탐 (공격 → 정상)
- 튜닝: Threshold, Whitelist, Suppress

**우회**
- Fragmentation, Encoding, Encryption, Timing

---

**다음 학습**: Phase 3-3 VPN
