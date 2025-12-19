---
layout: post
title: "Phase 3-3: VPN (Virtual Private Network)"
date: 2024-12-30 09:00:03 +0900
categories: [network, security]
tags: [SK-Rookies, Lecture-Notes]
---

# Phase 3-3: VPN (Virtual Private Network)

## 학습 목표
- VPN의 개념과 필요성 이해
- Site-to-Site VPN과 Remote Access VPN 차이점 파악
- IPsec 프로토콜 구조와 동작 원리 학습
- SSL/TLS VPN의 특징과 장단점 이해
- VPN 프로토콜 비교 (PPTP, L2TP, OpenVPN, WireGuard)
- VPN 구축 실습 및 보안 설정

---

## 1. VPN 개요

### 1.1 정의

**VPN (Virtual Private Network)**
- 공용 네트워크(인터넷)를 통한 사설 네트워크 구축
- 암호화 터널로 안전한 통신
- 논리적으로 전용선처럼 동작

**필요성**
```
문제: 지사 간 전용선 비용
- 물리적 전용선: 매우 비쌈
- 유지보수 어려움

해결: VPN
- 인터넷 활용 (저렴)
- 암호화로 보안 확보
- 유연한 구성
```

### 1.2 VPN 유형

**Site-to-Site VPN (거점 간)**
```
본사 ←──────── VPN Tunnel ──────────→ 지사
  |                                    |
Router                              Router
  |                                    |
LAN                                  LAN

용도: 지사 연결, 데이터센터 연결
특징: 항상 연결, Gateway 기반
```

**Remote Access VPN (원격 접속)**
```
재택 근무자 ←── VPN Tunnel ──→ 회사 네트워크
   (Client)                      (VPN Server)

용도: 재택근무, 모바일 접속
특징: 필요 시 연결, Client 소프트웨어 필요
```

### 1.3 VPN 터널링

**터널링 (Tunneling)**
```
원본 패킷을 캡슐화 + 암호화

[원본 IP][TCP][Data]
         ↓ 캡슐화
[새 IP][VPN Header][암호화된 원본 패킷]
         ↓ 전송
인터넷을 통해 안전하게 전달
         ↓ 복호화
[원본 IP][TCP][Data]
```

---

## 2. IPsec

### 2.1 개요

**IPsec (IP Security)**
- IP 계층(L3) 보안 프로토콜
- IETF 표준 (RFC 4301)
- 가장 널리 사용되는 VPN 프로토콜

**제공 기능**
```
1. 기밀성 (Confidentiality)
   - 암호화 (AES, 3DES)

2. 무결성 (Integrity)
   - HMAC (SHA-256)

3. 인증 (Authentication)
   - 송신자 확인

4. Replay 방지
   - Sequence Number
```

### 2.2 IPsec 구성 요소

**AH (Authentication Header)**
```
기능:
- 인증
- 무결성
- Replay 방지

제외: 암호화 (평문 전송)

사용: 거의 안 함 (암호화 없어서)
```

**ESP (Encapsulating Security Payload)**
```
기능:
- 암호화
- 인증
- 무결성
- Replay 방지

사용: 주로 사용 (AH보다 우수)
```

**비교**
```
AH:
[IP Header][AH Header][TCP][Data]
            └── 인증 범위 ──┘

ESP:
[IP Header][ESP Header][암호화: TCP + Data][ESP Trailer][ESP Auth]
            └────────── 암호화 범위 ────────┘
            └──────────── 인증 범위 ──────────┘
```

### 2.3 IPsec 모드

**Transport Mode (전송 모드)**
```
원본 IP 헤더 유지
페이로드만 암호화

[원본 IP Header][IPsec Header][암호화: TCP + Data]

용도: Host-to-Host (개별 호스트 간)
```

**Tunnel Mode (터널 모드)**
```
전체 원본 패킷 암호화
새로운 IP 헤더 추가

[새 IP Header][IPsec Header][암호화: 원본 IP + TCP + Data]

용도: Site-to-Site VPN (Gateway 간)
```

**비교 예시**
```
원본: 192.168.1.10 → 192.168.2.20

Transport Mode:
Src: 192.168.1.10
Dst: 192.168.2.20
Payload: 암호화됨

Tunnel Mode:
Src: Gateway A (203.0.113.1)
Dst: Gateway B (198.51.100.1)
Payload: 암호화된 전체 원본 패킷
```

### 2.4 IKE (Internet Key Exchange)

**Phase 1: ISAKMP SA 구성**
```
목적: 안전한 채널 구축 (관리 트래픽용)

Main Mode (6 메시지):
1-2. SA Proposal 교환
     - 암호화 알고리즘 협상 (AES-256)
     - 해시 알고리즘 (SHA-256)
     - 인증 방법 (PSK, Certificate)
     - DH Group (DH 14)

3-4. Diffie-Hellman Key Exchange
     - 공개키 교환
     - 세션키 생성

5-6. ID 교환 + 인증
     - 암호화된 신원 확인

결과: ISAKMP SA (안전한 채널)
```

**Phase 2: IPsec SA 구성**
```
목적: 실제 데이터 보호 (사용자 트래픽용)

Quick Mode (3 메시지):
1. IPsec Proposal 교환
   - ESP/AH 선택
   - 암호화 알고리즘
   - Perfect Forward Secrecy (PFS)

2-3. 키 교환 + 확인

결과: IPsec SA (양방향 2개)
  - Inbound SA
  - Outbound SA
```

**IKEv2 (개선)**
```
장점:
- 4 메시지만 (빠름)
- NAT Traversal 내장
- MOBIKE (모바일 지원)
- 재연결 빠름

IKEv1 vs IKEv2:
IKEv1: 9 메시지 (Main + Quick)
IKEv2: 4 메시지
```

### 2.5 IPsec 설정 예시 (Linux strongSwan)

**설치**
```bash
sudo apt install strongswan strongswan-pki
```

**설정 파일 (/etc/ipsec.conf)**
```
config setup
    charondebug="all"
    uniqueids=yes

conn site-to-site
    # 일반 설정
    type=tunnel
    auto=start
    
    # Phase 1 (IKE)
    keyexchange=ikev2
    ike=aes256-sha256-modp2048!
    
    # Phase 2 (ESP)
    esp=aes256-sha256-modp2048!
    
    # 로컬 (본사)
    left=%defaultroute
    leftid=@site-a.example.com
    leftsubnet=192.168.1.0/24
    leftauth=psk
    
    # 원격 (지사)
    right=203.0.113.1
    rightid=@site-b.example.com
    rightsubnet=192.168.2.0/24
    rightauth=psk
```

**Pre-Shared Key (/etc/ipsec.secrets)**
```
@site-a.example.com @site-b.example.com : PSK "VeryStrongPassword123!"
```

**시작**
```bash
sudo ipsec start
sudo ipsec up site-to-site
sudo ipsec status
```

---

## 3. SSL/TLS VPN

### 3.1 개요

**SSL VPN**
- Application Layer (L7)
- HTTPS 기반 (Port 443)
- 웹 브라우저로 접속 가능

**vs IPsec**
```
IPsec:
- L3, 모든 트래픽
- Client 소프트웨어 필요
- 방화벽 통과 어려움 (특정 포트)

SSL VPN:
- L7, 특정 Application
- 웹 브라우저만 (경우에 따라)
- 방화벽 통과 쉬움 (Port 443)
```

### 3.2 SSL VPN 유형

**Portal VPN**
```
웹 기반 접근
- 브라우저로 로그인
- 웹 인터페이스로 리소스 접근
- 파일 공유, 웹메일 등

장점: Client 불필요
단점: 기능 제한적
```

**Tunnel VPN**
```
전체 네트워크 접근
- VPN Client 설치
- 가상 네트워크 어댑터
- 모든 프로토콜 지원

장점: 완전한 네트워크 접근
단점: Client 필요
```

### 3.3 OpenVPN

**특징**
```
- 오픈소스 SSL VPN
- OpenSSL 기반
- UDP/TCP 지원
- 강력한 암호화
- 크로스 플랫폼
```

**설치 (Server)**
```bash
# Ubuntu
sudo apt install openvpn easy-rsa

# CA 및 인증서 생성
make-cadir ~/openvpn-ca
cd ~/openvpn-ca
./easyrsa init-pki
./easyrsa build-ca
./easyrsa gen-req server nopass
./easyrsa sign-req server server
./easyrsa gen-dh
openvpn --genkey secret ta.key
```

**서버 설정 (/etc/openvpn/server.conf)**
```
port 1194
proto udp
dev tun

ca ca.crt
cert server.crt
key server.key
dh dh2048.pem
tls-auth ta.key 0

server 10.8.0.0 255.255.255.0
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 8.8.8.8"

keepalive 10 120
cipher AES-256-GCM
auth SHA256
user nobody
group nogroup
persist-key
persist-tun

status /var/log/openvpn-status.log
verb 3
```

**시작**
```bash
sudo systemctl start openvpn@server
sudo systemctl enable openvpn@server
```

**클라이언트 설정 (client.ovpn)**
```
client
dev tun
proto udp
remote vpn.example.com 1194

ca ca.crt
cert client.crt
key client.key
tls-auth ta.key 1

cipher AES-256-GCM
auth SHA256
verb 3
```

**클라이언트 연결**
```bash
sudo openvpn --config client.ovpn
```

---

## 4. VPN 프로토콜 비교

### 4.1 PPTP (Point-to-Point Tunneling Protocol)

**특징**
```
- 오래된 프로토콜 (1999)
- Windows 내장
- Port 1723 (TCP)
- 빠름

보안:
- MPPE (RC4 128-bit)
- MS-CHAPv2 인증
- 취약! (2012년 크랙됨)

결론: 사용 금지
```

### 4.2 L2TP/IPsec

**L2TP (Layer 2 Tunneling Protocol)**
```
- PPTP 후속
- 자체 암호화 없음
- IPsec과 결합 사용

Port:
- UDP 500 (IKE)
- UDP 4500 (NAT-T)
- UDP 1701 (L2TP)

보안: IPsec (AES-256)
성능: 이중 캡슐화로 느림
```

### 4.3 OpenVPN

**특징**
```
장점:
- 오픈소스
- 강력한 암호화 (AES-256)
- 유연성 (UDP/TCP, 포트 변경 가능)
- 크로스 플랫폼

단점:
- Client 설치 필요
- 설정 복잡

권장: 일반적 사용
```

### 4.4 WireGuard

**특징 (2020 Linux 커널 통합)**
```
장점:
- 매우 빠름 (경량)
- 간단한 코드 (4,000줄)
- 최신 암호화 (ChaCha20, Curve25519)
- 쉬운 설정

단점:
- 비교적 새로움
- IP 주소 고정

성능: OpenVPN보다 3~5배 빠름
```

**설치**
```bash
sudo apt install wireguard
```

**서버 설정**
```bash
# 키 생성
wg genkey | tee server_private.key | wg pubkey > server_public.key

# /etc/wireguard/wg0.conf
[Interface]
PrivateKey = <server_private_key>
Address = 10.0.0.1/24
ListenPort = 51820
SaveConfig = true

[Peer]
PublicKey = <client_public_key>
AllowedIPs = 10.0.0.2/32
```

**클라이언트 설정**
```bash
# /etc/wireguard/wg0.conf
[Interface]
PrivateKey = <client_private_key>
Address = 10.0.0.2/24

[Peer]
PublicKey = <server_public_key>
Endpoint = vpn.example.com:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

**시작**
```bash
sudo wg-quick up wg0
sudo wg show
```

### 4.5 프로토콜 비교표

| 프로토콜 | 암호화 | 속도 | 보안 | 설정 | 권장 |
|---------|--------|------|------|------|------|
| PPTP | RC4 128 | ★★★★★ | ★☆☆☆☆ | ★★★★★ | ❌ 사용 금지 |
| L2TP/IPsec | AES-256 | ★★★☆☆ | ★★★★☆ | ★★★☆☆ | ✅ 호환성 필요 시 |
| OpenVPN | AES-256 | ★★★★☆ | ★★★★★ | ★★☆☆☆ | ✅ 일반 사용 |
| WireGuard | ChaCha20 | ★★★★★ | ★★★★★ | ★★★★★ | ✅ 최신 선택 |
| IPsec | AES-256 | ★★★★☆ | ★★★★★ | ★★☆☆☆ | ✅ Site-to-Site |

---

## 5. VPN 보안 고려사항

### 5.1 Split Tunneling

**Full Tunnel**
```
모든 트래픽이 VPN 통과

Client → VPN → Internet
Client → VPN → 회사 네트워크

장점: 보안
단점: VPN 서버 부하, 느림
```

**Split Tunnel**
```
회사 트래픽만 VPN
인터넷은 직접

Client → 회사 네트워크: VPN
Client → Internet: Direct

장점: 빠름, 효율적
단점: 보안 위험 (Client 공격 → 회사망)
```

**설정 (OpenVPN)**
```
# Full Tunnel
push "redirect-gateway def1 bypass-dhcp"

# Split Tunnel
push "route 192.168.1.0 255.255.255.0"
```

### 5.2 DNS Leak 방지

**DNS Leak**
```
문제:
- VPN 연결 중
- DNS 쿼리가 ISP DNS로 전송
- ISP가 방문 사이트 알 수 있음

방어:
- VPN DNS 서버 강제
```

**OpenVPN 설정**
```
push "dhcp-option DNS 10.8.0.1"
push "block-outside-dns"
```

**테스트**
```
https://dnsleaktest.com
→ VPN 서버 IP만 표시되어야 함
```

### 5.3 Kill Switch

**목적**
```
VPN 연결 끊김 시
→ 인터넷 차단
→ 실제 IP 노출 방지
```

**구현 (iptables)**
```bash
#!/bin/bash

# VPN 인터페이스만 허용
iptables -F
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

# Loopback 허용
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# VPN 허용
iptables -A OUTPUT -o tun0 -j ACCEPT
iptables -A INPUT -i tun0 -j ACCEPT

# VPN 서버 연결 허용
iptables -A OUTPUT -d <VPN_SERVER_IP> -p udp --dport 1194 -j ACCEPT
iptables -A INPUT -s <VPN_SERVER_IP> -p udp --sport 1194 -j ACCEPT
```

### 5.4 인증 강화

**Multi-Factor Authentication**
```
OpenVPN + Google Authenticator (OTP)

1. 인증서
2. OTP (6자리 코드)

설치:
sudo apt install libpam-google-authenticator

OpenVPN 설정:
plugin /usr/lib/openvpn/openvpn-plugin-auth-pam.so openvpn
```

---

## 6. 실습 과제

### 과제 1: OpenVPN Site-to-Site
```bash
# 본사 (Site A)
sudo apt install openvpn
# 서버 설정
# 지사와 터널 구성

# 지사 (Site B)
# 클라이언트 설정

# 테스트
ping <Site B 내부 IP>
```

### 과제 2: WireGuard Remote Access
```bash
# 서버
sudo apt install wireguard
wg genkey | tee server_key | wg pubkey > server_pub

# 클라이언트
wg genkey | tee client_key | wg pubkey > client_pub

# 설정 파일 작성
# 연결 테스트
```

### 과제 3: VPN 성능 비교
```bash
# OpenVPN 속도 테스트
iperf3 -c <VPN Server> -t 30

# WireGuard 속도 테스트
# 비교
```

---

## 7. 연결 포인트

### Phase 1.3: Information Security
→ **암호화**: VPN 터널 암호화
→ **TLS**: SSL VPN 기반

### Phase 2.2: Spoofing
→ **MITM 방어**: VPN으로 암호화

### Phase 3.1: Firewall
→ **VPN과 방화벽**: 통합 구성

### Phase 4.2: Network Monitoring
→ **VPN 트래픽 분석**: 암호화된 트래픽

---

## 8. 핵심 요약

**VPN 유형**
- Site-to-Site: 거점 간 (항상 연결)
- Remote Access: 개인 접속 (필요 시)

**IPsec**
- L3 프로토콜
- AH (인증) + ESP (암호화)
- Transport vs Tunnel Mode
- IKE Phase 1 + Phase 2

**SSL VPN**
- L7 프로토콜
- HTTPS 기반 (Port 443)
- Portal vs Tunnel

**프로토콜 선택**
- PPTP: ❌ 사용 금지
- L2TP/IPsec: 호환성
- OpenVPN: 일반 권장
- WireGuard: 최신 권장

**보안**
- Kill Switch
- DNS Leak 방지
- Split Tunneling 주의
- MFA

---

**다음 학습**: Phase 4-1 Packet Analysis
