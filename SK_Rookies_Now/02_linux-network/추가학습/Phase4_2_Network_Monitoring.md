# Phase 4-2: 네트워크 모니터링 (Network Monitoring)

## 학습 목표
- 네트워크 모니터링의 필요성과 방법론 이해
- SNMP 프로토콜 구조와 활용 방법 학습
- NetFlow/sFlow를 통한 트래픽 분석 기법 습득
- 오픈소스 모니터링 도구 실전 활용 (Nagios, Zabbix, Prometheus)
- 로그 수집 및 분석 시스템 구축 (ELK Stack)
- 실시간 대시보드 구성 및 알림 설정

---

## 1. 네트워크 모니터링 개요

### 1.1 필요성

**모니터링 목적**
```
1. 가용성 (Availability)
   - 서비스 정상 동작 확인
   - 장애 즉시 탐지

2. 성능 (Performance)
   - 대역폭 사용률
   - 응답 시간
   - 패킷 손실률

3. 보안 (Security)
   - 비정상 트래픽 탐지
   - 공격 징후 식별
   - 정책 위반 확인

4. 용량 계획 (Capacity Planning)
   - 트렌드 분석
   - 증설 시기 예측
```

### 1.2 모니터링 유형

**Passive Monitoring (수동)**
```
네트워크 트래픽 관찰
- 패킷 캡처 (Wireshark)
- Flow 데이터 수집 (NetFlow)
- 로그 분석

장점: 네트워크 영향 없음
단점: 실시간 상태 파악 어려움
```

**Active Monitoring (능동)**
```
테스트 트래픽 전송
- Ping (ICMP Echo)
- HTTP 요청
- SNMP Poll

장점: 실시간 상태 확인
단점: 네트워크 부하 (미미함)
```

### 1.3 모니터링 지표

**인프라 메트릭**
```
- CPU 사용률 (%)
- 메모리 사용률 (%)
- 디스크 I/O
- 네트워크 대역폭 (bps)
```

**네트워크 메트릭**
```
- Latency (지연, ms)
- Jitter (지터, ms)
- Packet Loss (손실률, %)
- Throughput (처리량, bps)
```

**애플리케이션 메트릭**
```
- 응답 시간 (ms)
- 에러율 (%)
- 동시 연결 수
- 트랜잭션/초 (TPS)
```

---

## 2. SNMP (Simple Network Management Protocol)

### 2.1 개요

**SNMP**
- 네트워크 장비 관리 프로토콜
- UDP 161 (Agent), 162 (Trap)
- 표준화된 정보 수집

**구성 요소**
```
Manager (관리자)
  - 모니터링 서버
  - 정보 수집 및 관리

Agent (에이전트)
  - 네트워크 장비에 설치
  - MIB 정보 제공

MIB (Management Information Base)
  - 관리 정보 데이터베이스
  - OID (Object Identifier) 구조
```

### 2.2 SNMP 버전

**SNMPv1 (1988)**
```
특징:
- 가장 기본적
- Community String (평문)

보안: 취약 (평문 전송)
사용: 레거시 장비만
```

**SNMPv2c (1993)**
```
개선:
- GetBulk (대량 조회)
- 64-bit Counter

보안: 여전히 평문
사용: 가장 일반적
```

**SNMPv3 (2002)**
```
추가:
- 인증 (Authentication)
- 암호화 (Encryption)
- 접근 제어 (Access Control)

보안: 강력
사용: 권장 (설정 복잡)
```

### 2.3 SNMP 동작

**GET (조회)**
```
Manager → Agent: GET Request
  OID: 1.3.6.1.2.1.1.1.0 (sysDescr)

Agent → Manager: GET Response
  Value: "Cisco IOS Software..."
```

**SET (설정)**
```
Manager → Agent: SET Request
  OID: 1.3.6.1.2.1.1.6.0 (sysLocation)
  Value: "Seoul, Korea"

Agent → Manager: SET Response
  Result: Success
```

**TRAP (알림)**
```
이벤트 발생 시 Agent가 Manager에 전송

예:
- 인터페이스 Down
- CPU 과부하
- 온도 경고

Agent → Manager: TRAP
  OID: linkDown
  Interface: GigabitEthernet0/1
```

### 2.4 주요 OID

**시스템 정보**
```
1.3.6.1.2.1.1.1.0  sysDescr (시스템 설명)
1.3.6.1.2.1.1.3.0  sysUpTime (가동 시간)
1.3.6.1.2.1.1.5.0  sysName (호스트명)
```

**인터페이스 정보**
```
1.3.6.1.2.1.2.2.1.2   ifDescr (인터페이스 이름)
1.3.6.1.2.1.2.2.1.5   ifSpeed (속도)
1.3.6.1.2.1.2.2.1.8   ifOperStatus (상태: up/down)
1.3.6.1.2.1.2.2.1.10  ifInOctets (수신 바이트)
1.3.6.1.2.1.2.2.1.16  ifOutOctets (송신 바이트)
```

**CPU/메모리**
```
1.3.6.1.4.1.2021.11.9.0   ssCpuIdle (CPU Idle %)
1.3.6.1.4.1.2021.4.5.0    memTotalReal (총 메모리)
1.3.6.1.4.1.2021.4.6.0    memAvailReal (가용 메모리)
```

### 2.5 SNMP 실습

**Linux에 SNMP Agent 설치**
```bash
# 설치
sudo apt install snmpd snmp

# 설정
sudo nano /etc/snmp/snmpd.conf

# Community String 설정
rocommunity public 192.168.1.0/24
# read-only, public, 특정 네트워크만

# 시스템 정보
syslocation "Seoul, Korea"
syscontact admin@example.com

# 재시작
sudo systemctl restart snmpd
```

**SNMP 쿼리 (Manager)**
```bash
# GET (단일 OID)
snmpget -v2c -c public 192.168.1.100 1.3.6.1.2.1.1.5.0

# WALK (하위 모든 OID)
snmpwalk -v2c -c public 192.168.1.100 1.3.6.1.2.1.1

# 인터페이스 정보
snmpwalk -v2c -c public 192.168.1.100 ifDescr

# 대역폭 사용률 계산
#!/bin/bash
# ifInOctets 두 번 측정 → 차이 계산
IN1=$(snmpget -v2c -c public 192.168.1.100 ifInOctets.2 | awk '{print $4}')
sleep 10
IN2=$(snmpget -v2c -c public 192.168.1.100 ifInOctets.2 | awk '{print $4}')
DIFF=$((IN2 - IN1))
BPS=$((DIFF * 8 / 10))
echo "Bandwidth: $BPS bps"
```

---

## 3. NetFlow/sFlow

### 3.1 NetFlow

**개념**
```
Cisco 개발 (RFC 3954)
Flow 정보 수집
- 5-Tuple 기반 Flow 정의:
  (Src IP, Dst IP, Src Port, Dst Port, Protocol)
  
정보:
- 패킷 수
- 바이트 수
- 시작/종료 시간
- ToS, TCP Flags
```

**NetFlow vs Packet Capture**
```
NetFlow:
- Flow 메타데이터만
- 적은 저장 공간
- 장기간 보관 가능
- 트렌드 분석

Packet Capture:
- 전체 패킷
- 많은 저장 공간
- 단기간만 보관
- 상세 분석
```

**NetFlow 버전**
```
v5: 가장 일반적
v9: 유연성 (템플릿 기반)
IPFIX (v10): 표준화 (RFC 7011)
```

### 3.2 sFlow

**특징**
```
InMon 개발 (RFC 3176)
Sampling 기반
- 1/N 패킷만 샘플링
- 예: 1/1000

장점:
- 낮은 CPU 사용
- 높은 대역폭 환경 적합

NetFlow vs sFlow:
NetFlow: 모든 Flow (정확)
sFlow: 샘플링 (효율)
```

### 3.3 Flow 분석

**nfdump (NetFlow 분석)**
```bash
# 설치
sudo apt install nfdump

# Flow 파일 읽기
nfdump -r flow_file.nfcap

# 상위 Talker (대역폭 사용)
nfdump -r flow_file.nfcap -s srcip/bytes -n 10

# 특정 IP 필터
nfdump -r flow_file.nfcap 'src ip 192.168.1.100'

# 특정 포트
nfdump -r flow_file.nfcap 'port 80 or port 443'

# 시간 범위
nfdump -R /var/cache/nfdump -t 2024-01-01/2024-01-31
```

**ntopng (Flow 시각화)**
```bash
# 설치
sudo apt install ntopng

# 실행
sudo ntopng -i eth0

# 웹 인터페이스
http://localhost:3000

기능:
- 실시간 트래픽
- 상위 호스트/애플리케이션
- Flow 기록
- 알림 설정
```

---

## 4. 모니터링 도구

### 4.1 Nagios

**특징**
```
- 오픈소스 모니터링
- 플러그인 기반
- 호스트/서비스 감시
- 알림 (Email, SMS)
```

**설치 (Ubuntu)**
```bash
# 의존성
sudo apt install build-essential apache2 php libapache2-mod-php

# Nagios Core
wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.4.6.tar.gz
tar xzf nagios-4.4.6.tar.gz
cd nagios-4.4.6
./configure --with-httpd-conf=/etc/apache2/sites-enabled
make all
sudo make install
sudo make install-init
sudo make install-config
sudo make install-commandmode

# 웹 인터페이스 계정
sudo htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin

# Plugins
sudo apt install nagios-plugins

# 시작
sudo systemctl start nagios
sudo systemctl enable nagios
```

**호스트 정의 (/usr/local/nagios/etc/objects/hosts.cfg)**
```
define host {
    use                     linux-server
    host_name               webserver1
    alias                   Web Server 1
    address                 192.168.1.100
    max_check_attempts      3
    check_period            24x7
    notification_interval   30
    notification_period     24x7
}
```

**서비스 정의 (/usr/local/nagios/etc/objects/services.cfg)**
```
define service {
    use                     generic-service
    host_name               webserver1
    service_description     HTTP
    check_command           check_http
}

define service {
    use                     generic-service
    host_name               webserver1
    service_description     SSH
    check_command           check_ssh
}

define service {
    use                     generic-service
    host_name               webserver1
    service_description     Disk Space
    check_command           check_nrpe!check_disk
}
```

**알림 설정**
```
define contact {
    contact_name            admin
    alias                   System Administrator
    service_notification_period     24x7
    host_notification_period        24x7
    service_notification_options    w,u,c,r
    host_notification_options       d,u,r
    service_notification_commands   notify-service-by-email
    host_notification_commands      notify-host-by-email
    email                   admin@example.com
}
```

### 4.2 Zabbix

**특징**
```
- Enterprise급 모니터링
- 에이전트 기반 + SNMP
- 자동 Discovery
- 강력한 대시보드
- 트리거 & 알림
```

**설치 (Docker)**
```bash
# PostgreSQL
docker run -d \
  --name postgres-server \
  -e POSTGRES_USER=zabbix \
  -e POSTGRES_PASSWORD=zabbix \
  postgres:latest

# Zabbix Server
docker run -d \
  --name zabbix-server \
  -e DB_SERVER_HOST=postgres-server \
  -e POSTGRES_USER=zabbix \
  -e POSTGRES_PASSWORD=zabbix \
  --link postgres-server:postgres \
  -p 10051:10051 \
  zabbix/zabbix-server-pgsql:latest

# Zabbix Web
docker run -d \
  --name zabbix-web \
  -e DB_SERVER_HOST=postgres-server \
  -e POSTGRES_USER=zabbix \
  -e POSTGRES_PASSWORD=zabbix \
  -e ZBX_SERVER_HOST=zabbix-server \
  --link postgres-server:postgres \
  --link zabbix-server:zabbix-server \
  -p 80:8080 \
  zabbix/zabbix-web-nginx-pgsql:latest

# 접속
http://localhost
ID: Admin
PW: zabbix
```

**에이전트 설치 (피모니터링 호스트)**
```bash
# Linux
sudo apt install zabbix-agent

# 설정
sudo nano /etc/zabbix/zabbix_agentd.conf

Server=192.168.1.10  # Zabbix Server IP
ServerActive=192.168.1.10
Hostname=webserver1

# 시작
sudo systemctl start zabbix-agent
sudo systemctl enable zabbix-agent
```

### 4.3 Prometheus + Grafana

**Prometheus (메트릭 수집)**
```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
  
  - job_name: 'node'
    static_configs:
      - targets: ['192.168.1.100:9100']

  - job_name: 'nginx'
    static_configs:
      - targets: ['192.168.1.101:9113']
```

**Node Exporter (메트릭 제공)**
```bash
# 설치
wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz
tar xzf node_exporter-1.7.0.linux-amd64.tar.gz
cd node_exporter-1.7.0.linux-amd64

# 실행
./node_exporter &

# 확인
curl http://localhost:9100/metrics
```

**Grafana (시각화)**
```bash
# Docker
docker run -d \
  --name grafana \
  -p 3000:3000 \
  grafana/grafana

# 접속
http://localhost:3000
ID: admin
PW: admin

# Data Source 추가
Configuration → Data Sources → Prometheus
URL: http://prometheus:9090

# Dashboard Import
Dashboard → Import
ID: 1860 (Node Exporter Full)
```

**PromQL 쿼리 예시**
```
# CPU 사용률
100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# 메모리 사용률
100 * (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes))

# 디스크 사용률
100 - (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"} * 100)

# 네트워크 대역폭 (수신)
rate(node_network_receive_bytes_total{device="eth0"}[5m]) * 8
```

---

## 5. 로그 관리 (ELK Stack)

### 5.1 ELK 개요

**구성**
```
Elasticsearch: 검색 엔진, 데이터 저장
Logstash: 로그 수집 및 파싱
Kibana: 시각화 대시보드
```

**데이터 흐름**
```
Log Source → Filebeat → Logstash → Elasticsearch → Kibana
(서버)       (경량 수집)  (파싱)     (저장)          (시각화)
```

### 5.2 Filebeat 설정

**설치**
```bash
wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.11.0-amd64.deb
sudo dpkg -i filebeat-8.11.0-amd64.deb
```

**설정 (filebeat.yml)**
```yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/nginx/access.log
    - /var/log/nginx/error.log

output.logstash:
  hosts: ["192.168.1.10:5044"]

logging.level: info
```

**시작**
```bash
sudo systemctl start filebeat
sudo systemctl enable filebeat
```

### 5.3 Logstash 설정

**Nginx Access Log 파싱 (logstash.conf)**
```
input {
  beats {
    port => 5044
  }
}

filter {
  if [log][file][path] =~ "access" {
    grok {
      match => { "message" => "%{COMBINEDAPACHELOG}" }
    }
    
    date {
      match => [ "timestamp", "dd/MMM/yyyy:HH:mm:ss Z" ]
    }
    
    geoip {
      source => "clientip"
    }
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "nginx-logs-%{+YYYY.MM.dd}"
  }
}
```

### 5.4 Kibana 대시보드

**인덱스 패턴 생성**
```
Management → Index Patterns
Pattern: nginx-logs-*
Time field: @timestamp
```

**시각화 예시**
```
1. 시간별 요청 수
   - Visualization: Line Chart
   - Y-Axis: Count
   - X-Axis: Date Histogram

2. 상위 IP (Top Talkers)
   - Visualization: Data Table
   - Metrics: Count
   - Buckets: Terms (clientip)

3. 응답 코드 분포
   - Visualization: Pie Chart
   - Slice: Terms (response)

4. 지리적 분포
   - Visualization: Map
   - Metrics: Count
   - Geo: Terms (geoip.country_name)
```

---

## 6. 알림 시스템

### 6.1 알림 조건

**임계값 기반**
```
예:
- CPU > 80%
- 메모리 > 90%
- 디스크 > 85%
- 응답 시간 > 2초
- 에러율 > 5%
```

**상태 변화**
```
- 서비스 Down
- 인터페이스 Down
- Certificate 만료 임박
```

**이상 탐지 (Anomaly)**
```
- 평상시 대비 트래픽 10배 증가
- 비정상적인 시간대 접속
- 새로운 목적지 IP
```

### 6.2 알림 채널

**Email**
```
가장 일반적
- SMTP 설정
- 수신자 그룹
```

**SMS**
```
긴급 알림
- Twilio, AWS SNS
- 비용 발생
```

**Slack/Teams**
```
팀 협업
- Webhook
- 채널별 알림
```

**PagerDuty**
```
On-call 관리
- Escalation Policy
- 교대 근무
```

### 6.3 알림 정책

**심각도 (Severity)**
```
Critical (치명적):
  - 즉시 알림 (SMS, 전화)
  - 서비스 Down, 데이터 유실

Warning (경고):
  - Email, Slack
  - CPU 높음, 디스크 부족

Info (정보):
  - 로그만
  - 정상 복구, 유지보수 완료
```

**알림 피로 방지**
```
1. Throttling (빈도 제한)
   - 같은 알림 5분에 1번만

2. Grouping (그룹화)
   - 여러 호스트 같은 문제 → 1개 알림

3. Maintenance Window (점검 시간)
   - 예정된 점검 시 알림 차단

4. Dependency (의존성)
   - 스위치 Down → 연결된 모든 서버 Down
   - 스위치 알림만
```

---

## 7. 실습 과제

### 과제 1: SNMP 모니터링
```bash
# 1. SNMP Agent 설치 및 설정
sudo apt install snmpd
sudo nano /etc/snmp/snmpd.conf

# 2. Manager에서 정보 수집
snmpwalk -v2c -c public localhost

# 3. 대역폭 모니터링 스크립트 작성
# ifInOctets, ifOutOctets 주기적 조회

# 4. 그래프 생성 (RRDtool)
```

### 과제 2: Prometheus + Grafana
```bash
# 1. Docker Compose로 구성
# 2. Node Exporter 설치
# 3. Grafana 대시보드 생성
# 4. 알림 설정 (CPU > 80%)
```

### 과제 3: ELK Stack
```bash
# 1. Filebeat로 Nginx 로그 수집
# 2. Logstash 파싱 설정
# 3. Kibana 대시보드 구성
# 4. 지리적 분포 시각화
```

---

## 8. 연결 포인트

### Phase 2.1: Scanning/Sniffing
→ **트래픽 분석**: Flow 데이터

### Phase 2.4: DoS/DDoS
→ **DDoS 탐지**: 트래픽 급증 알림

### Phase 3.2: IDS/IPS
→ **로그 통합**: IDS 알림 → SIEM

### Phase 4.1: Packet Analysis
→ **Wireshark**: 심층 분석
→ **NetFlow**: 트렌드 분석

---

## 9. 핵심 요약

**SNMP**
- 네트워크 장비 관리
- OID 기반 정보 수집
- v2c (일반), v3 (보안)

**NetFlow/sFlow**
- Flow 메타데이터 수집
- 장기 트렌드 분석
- 대역폭 사용 파악

**모니터링 도구**
- Nagios: 호스트/서비스 감시
- Zabbix: Enterprise 모니터링
- Prometheus: 메트릭 수집
- Grafana: 시각화

**로그 관리**
- ELK Stack
- Filebeat → Logstash → Elasticsearch → Kibana
- 중앙 집중 로그

**알림**
- 임계값, 상태 변화, 이상 탐지
- Email, SMS, Slack
- 알림 피로 방지

---

**학습 완료!** TCP/IP 네트워크 보안 전체 과정 종료
