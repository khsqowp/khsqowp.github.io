---
title: "Linux_Collected_Courses"
date: 2026-01-09
permalink: /posts/2026/01/09/Linux_Collected_Courses/
tags:
  - Linux-Network
  - SK_Rookies
---

# Linux 종합 강의 자료

## 목차

- [Day 2: 권한(Permission)의 해부와 ACL, 특수 권한](#day-2-권한permission의-해부와-acl-특수-권한)
  - [1. UGO와 Octal Mode의 심층 분석](#1-ugo와-octal-mode의-심층-분석)
  - [2. 특수 권한의 위험성과 활용](#2-특수-권한의-위험성과-활용)
  - [3. `chattr`: 불변(Immutable) 속성으로 파일 잠금](#3-chattr-불변immutable-속성으로-파일-잠금)
  - [4. POSIX ACL (Access Control Lists): UGO의 한계를 넘어서](#4-posix-acl-access-control-lists-ugo의-한계를-넘어서)
  - [5. 실습 예제: 협업 디렉토리 구축](#5-실습-예제-협업-디렉토리-구축)
- [Day 3: 스토리지, 파티셔닝, 그리고 RAID](#day-3-스토리지-파티셔닝-그리고-raid)
  - [1. 블록 디바이스와 파티셔닝: `lsblk`, `fdisk`](#1-블록-디바이스와-파티셔닝-lsblk-fdisk)
  - [2. 파일 시스템 생성과 마운트](#2-파일-시스템-생성과-마운트)
  - [3. LVM (Logical Volume Management): 유연한 스토리지 관리](#3-lvm-logical-volume-management-유연한-스토리지-관리)
  - [4. RAID (Redundant Array of Independent Disks)의 이해](#4-raid-redundant-array-of-independent-disks의-이해)
  - [5. 실습 예제: LVM을 이용한 웹로그 파티션 생성](#5-실습-예제-lvm을-이용한-웹로그-파티션-생성)
- [Day 4: 네트워크 심층 분석과 보안](#day-4-네트워크-심층-분석과-보안)
  - [1. `ss`를 이용한 소켓 상태 정밀 분석](#1-ss를-이용한-소켓-상태-정밀-분석)
  - [2. 리눅스 방화벽: `iptables`의 상태 추적과 `firewalld`](#2-리눅스-방화벽-iptables의-상태-추적과-firewalld)
  - [3. `tcpdump`와 BPF(Berkeley Packet Filter)를 이용한 패킷 캡처](#3-tcpdump와-bpfberkeley-packet-filter를-이용한-패킷-캡처)
  - [4. `nmap`을 이용한 포트 스캐닝과 시스템 탐지](#4-nmap을-이용한-포트-스캐닝과-시스템-탐지)
  - [5. 실습 예제: 로그 기반의 동적 IP 차단 스크립트](#5-실습-예제-로그-기반의-동적-ip-차단-스크립트)
- [Day 4: 시스템 서비스와 로그 관리: systemd와 journald](#day-4-시스템-서비스와-로그-관리-systemd와-journald)
  - [1. `systemd`의 이해: 유닛(Unit) 기반 아키텍처](#1-systemd의-이해-유닛unit-기반-아키텍처)
  - [2. `systemctl`을 이용한 서비스 관리](#2-systemctl을-이용한-서비스-관리)
  - [3. `systemd` 유닛 파일 작성법](#3-systemd-유닛-파일-작성법)
  - [4. 중앙화된 로그 시스템: `journald`와 `journalctl`](#4-중앙화된-로그-시스템-journald와-journalctl)
  - [5. 실습 예제: Python 웹 앱을 `systemd` 서비스로 등록하기](#5-실습-예제-python-웹-앱을-systemd-서비스로-등록하기)
- [Day 5: 쉘 스크립트 고급 테크닉과 자동화](#day-5-쉘-스크립트-고급-테크닉과-자동화)
  - [1. 방어적 Bash 프로그래밍 (Defensive Bash Programming)](#1-방어적-bash-프로그래밍-defensive-bash-programming)
  - [2. `getopts`: 표준 유틸리티 스타일의 인자 파싱](#2-getopts-표준-유틸리티-스타일의-인자-파싱)
  - [3. `trap`: 예외 처리와 정리(Cleanup) 작업](#3-trap-예외-처리와-정리cleanup-작업)
  - [4. 고급 자동화 기법](#4-고급-자동화-기법)
  - [5. 실습 예제: 고급 백업 스크립트](#5-실습-예제-고급-백업-스크립트)
- [Day 5: 시스템 관리 자동화와 쉘 스크립트](#day-5-시스템-관리-자동화와-쉘-스크립트)
  - [1. 작업 스케줄링의 정석: `cron`](#1-작업-스케줄링의-정석-cron)
  - [2. 일회성 작업 예약: `at`](#2-일회성-작업-예약-at)
  - [3. `xargs`: 파이프라인의 슈퍼차저](#3-xargs-파이프라인의-슈퍼차저)
  - [4. 지능형 동기화 및 백업: `rsync`](#4-지능형-동기화-및-백업-rsync)
  - [5. 실습 예제: 로그 로테이션(Log Rotation) 스크립트](#5-실습-예제-로그-로테이션log-rotation-스크립트)


# Day 2: 권한(Permission)의 해부와 ACL, 특수 권한

리눅스 시스템 보안의 근간은 파일 권한이다. 누가 파일을 읽고, 쓰고, 실행할 수 있는지를 통제하는 것은 시스템을 안정적으로 유지하고 민감한 데이터를 보호하는 첫걸음이다. 이 장에서는 기본적인 `rwx` 권한의 심층적인 의미부터, 전통적인 UGO 모델의 한계를 극복하는 ACL까지 다룬다.

## 1. UGO와 Octal Mode의 심층 분석

`ls -l`을 실행했을 때 가장 먼저 보이는 `-rwxr-xr-x`와 같은 10개의 문자는 파일의 타입과 세 종류의 사용자에 대한 권한을 나타낸다. (User, Group, Other)

### 1.1. 파일과 디렉토리: `r, w, x`의 다른 의미

동일한 권한 비트라도 대상이 파일이냐 디렉토리이냐에 따라 그 의미와 영향이 완전히 달라진다.

| 권한 | 파일에 적용될 때 | 디렉토리에 적용될 때 |
| :--- | :--- | :--- |
| **`r` (Read)** | 파일의 내용을 읽을 수 있다. (`cat`, `less`, `more` 등) | 디렉토리 내의 **파일 목록을 조회**할 수 있다. (`ls`) |
| **`w` (Write)** | 파일의 내용을 **수정하거나 덮어 쓸 수 있다**. 파일 크기를 0으로 만드는 `> file`도 쓰기 권한에 포함된다. | 디렉토리 내에서 파일을 **생성, 삭제, 이름 변경**할 수 있다. (`touch`, `rm`, `mv`, `mkdir`). |
| **`x` (Execute)** | 파일을 **프로세스로서 실행**할 수 있다. (쉘 스크립트, 컴파일된 바이너리 등) | 디렉토리에 **접근하거나 진입**할 수 있다. (`cd`). 경로의 일부로서 해당 디렉토리를 통과할 권한. |

**핵심 시나리오: 디렉토리의 `x` 권한**

- `r` 권한은 있으나 `x` 권한이 없는 디렉토리: `ls`로 내용물 목록은 볼 수 있지만, `cd`로 들어갈 수도 없고, `ls -l` 로 파일의 상세 정보(inode 정보)를 볼 수도 없으며, `cat dir/file.txt` 처럼 파일에 접근할 수도 없다. 디렉토리를 '통과'할 수 없기 때문이다.
- `x` 권한은 있으나 `r` 권한이 없는 디렉토리: `ls`로 목록을 볼 수는 없다. 하지만 파일명을 정확히 안다면 `cat dir/known_file.txt` 처럼 파일에 접근하는 것은 가능하다. (물론 파일 자체에 대한 읽기 권한이 있어야 한다).

**파일 삭제의 본질**: 파일을 삭제하는 것은 파일 자체의 권한이 아니라, 그 파일이 포함된 **디렉토리의 쓰기(`w`) 권한**에 의해 결정된다. `dir/file.txt`를 삭제하는 것은 `dir`의 내용을 변경하는 행위이기 때문이다.

### 1.2. `umask`: 창조의 기본값 제어

`umask`는 새로 생성되는 파일과 디렉토리의 기본 권한을 제어하는 마스크다. 이는 '허용할 권한'이 아니라, '제거할 권한'을 지정한다.

- **기본 최대 권한**:
  - 파일: `666` (`rw-rw-rw-`). 실행 권한은 위험할 수 있어 기본적으로 부여되지 않는다.
  - 디렉토리: `777` (`rwxrwxrwx`).
- **계산법**: `기본 권한 - umask = 최종 권한` (단, 비트 연산의 NOT과 AND로 동작 `permission = default & ~umask`)
- **일반적인 `umask` 값 `0022`**:
  - 파일: `666 - 022 = 644` (`rw-r--r--`). 소유자는 읽기/쓰기, 그룹과 다른 사용자는 읽기만 가능.
  - 디렉토리: `777 - 022 = 755` (`rwxr-xr-x`).
- **보안 강화 `umask` 값 `0027`**:
  - 파일: `666 - 027 = 640` (`rw-r-----`). 다른 사용자(Others)는 아무 권한도 갖지 못한다.
  - 디렉토리: `777 - 027 = 750` (`rwxr-x---`).
- 설정 위치: `/etc/profile`, `/etc/bashrc` (전역 설정), `~/.bashrc` (사용자별 설정).

## 2. 특수 권한의 위험성과 활용

일반적인 `rwx` 권한 외에, 특정 상황에서 프로세스의 권한을 일시적으로 상승시키는 특수 권한이 존재한다.

### 2.1. SetUID (`4000`), SetGID (`2000`), Sticky Bit (`1000`)

| 특수권한 | Octal | `ls -l` 표시 | 설명 |
| :--- | :--- | :--- | :--- |
| **SetUID** | `4000` | `rws` | 파일을 실행하는 동안, 실행한 사용자가 아닌 **파일 소유자의 권한**으로 프로세스가 실행됨. (`x` 권한 자리에 `s`). 실행 권한이 없으면 `S`(대문자)로 표시. |
| **SetGID** | `2000` | `r-s` | 파일을 실행하는 동안, **파일 그룹의 권한**으로 실행됨. 디렉토리에 설정 시, **내부에서 생성되는 모든 파일/디렉토리의 그룹 소유권이 해당 디렉토리의 그룹으로 상속**됨. |
| **Sticky Bit** | `1000` | `rwt` | 디렉토리에만 적용. 디렉토리 내에 누구나 파일 생성이 가능하지만, **파일 삭제는 오직 파일 소유자와 root만 가능**. (`t`로 표시) |

- **SetUID 활용과 위험**: `passwd` 명령어가 대표적인 예. 일반 사용자가 자신의 비밀번호를 변경하려면 root만 쓰기 가능한 `/etc/shadow` 파일을 수정해야 한다. `passwd` 명령어는 소유자가 `root`이고 SetUID 비트가 설정되어 있어, 일반 사용자가 실행하는 순간만 root 권한을 얻어 shadow 파일을 수정할 수 있다. 만약 SetUID가 설정된 프로그램에 버그가 있다면, 공격자는 이를 통해 root 권한을 탈취할 수 있다.
- **SetGID와 협업**: 여러 사용자가 속한 `developers` 그룹이 공유하는 디렉토리에 SetGID를 설정하면, `userA`가 생성한 파일도 그룹 소유자가 `developers`가 되므로 `userB`가 그룹 권한으로 수정할 수 있다.
- **Sticky Bit와 공용 공간**: `/tmp` 디렉토리가 대표적인 예. 모든 사용자가 임시 파일을 생성할 수 있지만, 다른 사용자의 임시 파일을 함부로 삭제할 수 없는 이유가 바로 Sticky Bit 때문이다.

### 2.2. 잠재적 백도어 탐지: `find`로 SetUID 파일 찾기

공격자들은 시스템을 장악한 후, 일반 프로그램(예: `/bin/bash`)을 복사하여 SetUID를 설정해두고 숨겨진 백도어로 사용하곤 한다. 주기적으로 시스템의 SetUID 파일을 검사하는 것은 중요한 보안 감사 절차다.

```bash
# -perm /4000 또는 -perm -u=s 를 사용
find / -type f -perm -u=s -ls 2>/dev/null
```
- `-perm -u=s`: SetUID 비트가 설정된 파일을 찾는다. `-4000`과 동일하게 동작하지만 더 명시적이다.
- `-type f`: 일반 파일만 대상으로 한다.
- `-ls`: 찾은 파일의 상세 정보를 `ls -lids` 형식으로 출력.
- `2>/dev/null`: 권한이 없는 디렉토리 검색 시 발생하는 에러 메시지를 숨긴다.

## 3. `chattr`: 불변(Immutable) 속성으로 파일 잠금

`chattr` (Change Attribute)는 POSIX 권한보다 한 단계 낮은 파일시스템 레벨(ext2/3/4 등)에서 파일의 속성을 제어한다. `root`조차도 이 속성을 먼저 해제하지 않으면 파일을 변경하거나 삭제할 수 없다.

- `lsattr [file]`: 파일의 확장 속성을 확인.
- `chattr [+-=][attributes] [file]`: 속성을 추가(+), 제거(-), 설정(=)한다.

- **불변 속성 (`i`)**: `chattr +i /etc/resolv.conf`
  - `+i` (immutable) 속성이 설정된 파일은 수정, 삭제, 이름 변경, 링크 생성이 모두 불가능하다.
  - 악성코드가 DNS 설정을 변경하는 것을 원천적으로 차단하거나, 시스템의 핵심 설정 파일이 실수로 변경되는 것을 방지하기 위해 사용된다.
  - 변경하려면 `root`가 `chattr -i /etc/resolv.conf`를 먼저 실행해야 한다.

- **추가 전용 속성 (`a`)**: `chattr +a /var/log/security.log`
  - `+a` (append only) 속성이 설정된 파일은 내용을 덧붙이는 것만 가능하다. 기존 내용을 수정하거나 파일을 삭제하는 것은 불가능하다.
  - 공격자가 로그를 삭제하거나 변조하여 침입 흔적을 지우는 것을 방지하는 데 매우 효과적이다.

## 4. POSIX ACL (Access Control Lists): UGO의 한계를 넘어서

"이 파일은 `alice`와 `developers` 그룹은 수정 가능하지만, 특별히 `bob`에게만 읽기 권한을 추가로 주고 싶다." -> 이런 시나리오에서 UGO 모델은 한계를 보인다. `bob`을 `developers` 그룹에 넣고 싶지는 않기 때문이다. ACL은 사용자/그룹별로 개별적인 권한을 설정하는 기능을 제공한다.

- **전제 조건**: 파일시스템이 `acl` 옵션으로 마운트되어 있어야 한다. (최신 배포판은 대부분 기본값) `mount | grep ' / '` 로 확인.
- `getfacl [file]`: 파일의 ACL 정보를 확인. `+` 기호가 `ls -l` 권한 뒤에 붙어있으면 ACL이 설정되어 있다는 의미.
- `setfacl`: ACL을 설정.
  - `-m` (modify): ACL 항목을 추가하거나 수정.
    - `setfacl -m u:bob:rx project.conf`: 사용자 `bob`에게 읽기/실행(`rx`) 권한을 부여.
    - `setfacl -m g:auditors:r project.conf`: `auditors` 그룹에게 읽기(`r`) 권한을 부여.
  - `-x` (remove): ACL 항목을 제거.
    - `setfacl -x u:bob project.conf`
  - `-b` (remove-all): 모든 확장 ACL 항목을 제거하고 기본 UGO 권한으로 되돌린다.

- **Default ACL: 권한 상속의 구현**: 디렉토리에 Default ACL을 설정하면, 그 디렉토리 내에 새로 생성되는 모든 파일과 하위 디렉토리는 해당 ACL을 자동으로 상속받는다.
  - `setfacl -d -m g:developers:rwx /srv/projects`
  - 이제 `/srv/projects` 디렉토리 아래에 생성되는 모든 것들은 `developers` 그룹에 `rwx` 권한을 자동으로 부여받는다.

## 5. 실습 예제: 협업 디렉토리 구축

**요구사항**: `developers` 그룹을 위한 `/shared/project_alpha` 디렉토리를 생성한다. 이 디렉토리는 다음 조건을 만족해야 한다:
1. `developers` 그룹의 모든 멤버는 파일과 디렉토리를 생성/수정할 수 있다.
2. 새로 생성된 파일/디렉토리의 그룹 소유권은 자동으로 `developers`가 되어야 한다.
3. 멤버들은 다른 사람이 만든 파일은 수정할 수 있지만, 삭제할 수는 없다. (오직 파일 소유자나 root만 삭제 가능)

### 해결 과정

```bash
# 1. 디렉토리 생성 및 그룹 소유권 설정
mkdir -p /shared/project_alpha
chown root:developers /shared/project_alpha

# 2. SetGID와 Sticky Bit를 포함한 기본 권한 설정
# 3775 = (Sticky Bit: 1) + (SetGID: 2) | (Owner: 7) | (Group: 7) | (Other: 5)
chmod 3775 /shared/project_alpha

# 3. 확인
ls -ld /shared/project_alpha
```

### 결과 및 분석

- `ls -ld`의 예상 출력: `drwxrwsr-t 2 root developers 4096 Nov 25 10:00 /shared/project_alpha`
- **`drwxrwsr-t` 분석**:
  - `d`: 디렉토리
  - `rwx`: 소유자(`root`)는 모든 권한을 가짐.
  - `rws`: 그룹(`developers`)은 읽기/쓰기/실행 권한을 가지며, **`s` (SetGID)**가 설정되어 있다. 이로 인해 이 디렉토리 내에 생성되는 모든 파일과 디렉토리는 자동으로 `developers` 그룹 소유가 된다.
  - `r-t`: 다른 사용자(Others)는 읽기/실행 권한만 있으며, **`t` (Sticky Bit)**가 설정되어 있다. `developers` 그룹 멤버들은 다른 멤버의 파일을 삭제할 수 없다. (자신이 소유한 파일만 삭제 가능)

- 이로써 `chmod 3775 /shared/project_alpha` 단 한 줄의 명령어로 SetGID와 Sticky Bit를 동시에 적용하여 복잡한 협업 규칙을 완벽하게 구현했다.
# Day 3: 스토리지, 파티셔닝, 그리고 RAID

서버의 성능과 안정성은 데이터를 저장하는 스토리지 시스템에 크게 좌우된다. 물리적 디스크를 어떻게 나누고(파티셔닝), 어떤 파일 시스템을 사용하며, 여러 디스크를 어떻게 조합하여(LVM, RAID) 사용하는지에 따라 시스템의 확장성, 속도, 데이터 안정성이 결정된다. 이 장에서는 하드웨어부터 논리적 볼륨에 이르기까지 스토리지 스택 전체를 다룬다.

## 1. 블록 디바이스와 파티셔닝: `lsblk`, `fdisk`

리눅스는 하드 디스크, SSD, USB 메모리 등의 저장 장치를 블록 단위로 데이터를 읽고 쓰는 '블록 디바이스'로 취급한다.

- **디바이스 명명 규칙**:
  - `sdX`: SATA, SCSI, SAS, USB 드라이브. `a`부터 순서대로 `sda`, `sdb`, ...
  - `nvmeXnY`: NVMe SSD. `X`는 컨트롤러 번호, `Y`는 네임스페이스 번호. `nvme0n1`과 같이 표시.
  - `vdX`: KVM 가상화 환경에서의 VirtIO 블록 디바이스.
  - `...N`: 디바이스 이름 뒤에 붙는 숫자 `N`은 파티션 번호를 의미 (`sda1`, `nvme0n1p2`).

- **`lsblk`: 블록 디바이스 목록의 현대적 접근**
  - `lsblk`는 시스템에 연결된 블록 디바이스와 그 관계를 트리 구조로 명확하게 보여준다.
  - `lsblk -f`: 파일 시스템 종류(FSTYPE), 라벨(LABEL), UUID, 마운트 지점(MOUNTPOINT) 등 상세 정보를 함께 출력. UUID는 영구적인 마운트를 위해 필수적인 정보다.

### 1.1. 파티션 테이블: MBR vs GPT

- **MBR (Master Boot Record)**: 구형 파티션 방식.
  - **한계**: ① 최대 2TB 디스크만 지원. ② 최대 4개의 주(Primary) 파티션만 생성 가능 (또는 3개 주 파티션 + 1개 확장(Extended) 파티션).
  - 더 이상 현대적인 서버 환경에서는 사용되지 않는다.
- **GPT (GUID Partition Table)**: 현대 표준.
  - **장점**: ① 사실상 무제한의 디스크 크기 지원. ② 기본 128개 파티션 지원. ③ 파티션 테이블 정보가 디스크의 시작과 끝, 두 곳에 복제되어 저장되므로 안정성이 높다. ④ CRC32 체크섬을 통해 파티션 테이블의 손상 여부를 감지할 수 있다.

### 1.2. 파티셔닝 도구: `fdisk`와 `parted`

- **`fdisk`**: 대화형 인터페이스를 가진 전통적이고 신뢰성 높은 도구.
  - `fdisk /dev/sdb`로 진입하여 대화형으로 파티션을 관리한다.
  - **주요 명령어(대화형 모드)**:
    - `g`: 새로운 GPT 파티션 테이블 생성.
    - `n`: 새 파티션 생성.
    - `d`: 파티션 삭제.
    - `p`: 현재 파티션 테이블 정보 출력.
    - `t`: 파티션 타입 변경 (예: `8e`는 Linux LVM, `83`은 Linux 기본).
    - `w`: 변경 사항을 디스크에 쓰고 종료. (가장 중요)
    - `q`: 변경 사항을 저장하지 않고 종료.

- **`parted`**: `fdisk`보다 강력하며, 스크립트를 통한 비대화형 작업에 용이하다.
  - `parted /dev/sdb --script -- mklabel gpt mkpart primary ext4 1MiB 100%`
  - 위 명령어는 `/dev/sdb` 디스크에 GPT 라벨을 만들고, 디스크 전체(1MiB ~ 100%)를 ext4 파일 시스템용 주 파티션으로 할당하는 작업을 스크립트로 한번에 처리한다.

## 2. 파일 시스템 생성과 마운트

파티션은 단순히 공간을 나눈 것이며, 파일을 저장하려면 해당 공간을 특정 파일 시스템으로 '포맷'해야 한다.

- **주요 파일 시스템**:
  - **Ext4**: 가장 널리 쓰이는 리눅스 표준 파일 시스템. 안정성과 범용성이 뛰어나다.
  - **XFS**: 대용량 파일 및 대규모 파일 시스템에서 뛰어난 성능을 보이는 고성능 저널링 파일 시스템. 병렬 I/O 처리에 강점이 있다.

- **`mkfs` (Make Filesystem)**: `mkfs.ext4 /dev/sdb1` 또는 `mkfs -t xfs /dev/sdb1`
  - 이 과정에서 슈퍼블록, inode 테이블, 데이터 블록 등 파일 시스템의 핵심 메타데이터 구조가 파티션에 기록된다.

- **`mount`와 `/etc/fstab`**: 파일 시스템을 디렉토리 트리에 연결(마운트)하여 사용 가능하게 만든다.
  - `mount /dev/sdb1 /data`: `/dev/sdb1` 파티션을 `/data` 디렉토리에 마운트.
  - `/etc/fstab`: 부팅 시 자동으로 마운트될 파일 시스템을 등록하는 파일. 6개의 필드로 구성된다.

| 필드 | 설명 | 예시 |
| :--- | :--- | :--- |
| **1. Device** | 마운트할 디바이스. **UUID를 사용하는 것이 절대적으로 권장됨.** | `UUID=...` |
| **2. Mount Point** | 마운트될 디렉토리 경로. | `/data` |
| **3. Type** | 파일 시스템 종류. | `xfs`, `ext4` |
| **4. Options** | 마운트 옵션. | `defaults,noatime`|
| **5. Dump** | `dump` 유틸리티의 백업 대상 여부. `0` (사용 안 함). | `0` |
| **6. Pass** | 부팅 시 `fsck` 파일 시스템 검사 순서. `0`(검사 안 함), `1`(root), `2`(기타). | `2` |

- **UUID 사용**: `blkid /dev/sdb1` 또는 `lsblk -f` 명령으로 파티션의 고유 UUID를 확인. 디스크 순서가 바뀌어도 항상 같은 파티션을 참조할 수 있어 안정적이다.
- **`noatime` 옵션**: 파일을 읽을 때마다 기록되는 접근 시간(access time)을 갱신하지 않도록 하여 디스크 I/O를 줄이고 성능을 향상시키는 필수적인 튜닝 옵션이다.

## 3. LVM (Logical Volume Management): 유연한 스토리지 관리

LVM은 여러 개의 물리 디스크나 파티션을 하나의 거대한 스토리지 풀(Pool)로 묶고, 그 안에서 필요한 만큼의 논리적 볼륨(파티션)을 동적으로 생성, 확장, 축소할 수 있게 해주는 강력한 스토리지 가상화 기술이다.

- **LVM의 3단 구조**:
  - **PV (Physical Volume)**: 물리 볼륨. `/dev/sda1`, `/dev/sdb1` 등 실제 파티션. `pvcreate`로 생성.
  - **VG (Volume Group)**: 볼륨 그룹. 여러 PV를 모아 만든 스토리지 풀. `vgcreate`로 생성.
  - **LV (Logical Volume)**: 논리 볼륨. VG에서 필요한 크기만큼 할당받는 가상 파티션. `lvcreate`로 생성. 이 LV를 포맷하고 마운트하여 사용한다.

- **LVM의 핵심 장점**:
  - **온라인 리사이징**: 서비스 중단 없이 파일 시스템의 크기를 늘리거나 줄일 수 있다.
  - **유연성**: 여러 디스크에 걸쳐 하나의 파일 시스템을 구성할 수 있다.
  - **스냅샷**: 특정 시점의 LV 상태를 그대로 복사한 스냅샷을 생성하여, 안전한 백업이나 테스트에 활용할 수 있다.

- **LVM 리사이징 절차**:
  1. `lvextend -L +10G /dev/my_vg/my_lv`: 논리 볼륨 크기를 10GB 늘린다.
  2. `resize2fs /dev/my_vg/my_lv`: (Ext4의 경우) 파일 시스템 크기를 늘어난 LV 크기에 맞게 확장한다.
  3. `xfs_growfs /mount/point`: (XFS의 경우) 마운트된 경로를 대상으로 파일 시스템을 확장한다.

## 4. RAID (Redundant Array of Independent Disks)의 이해

RAID는 여러 개의 물리 디스크를 하나의 논리적 단위로 묶어 성능(Performance), 이중화(Redundancy), 또는 둘 모두를 향상시키는 기술이다. 하드웨어 RAID 컨트롤러를 사용하는 하드웨어 RAID와, OS의 기능(`mdadm` 등)을 이용하는 소프트웨어 RAID로 나뉜다.

| RAID 레벨 | 최소 디스크 | 용량 효율성 | 장애 허용 | 장점 | 단점 | 주요 용도 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RAID 0** | 2 | N | 0 (없음) | **최상의 I/O 성능** (읽기/쓰기 모두 향상) | 디스크 하나만 고장나도 모든 데이터 손실 | 고속 임시 저장소, 비디오 편집 등 |
| **RAID 1** | 2 | 1/N | N-1 | **높은 안정성**, 빠른 읽기 성능 | 쓰기 성능은 단일 디스크와 동일, 비용 비효율 | OS, 데이터베이스 등 고가용성 중요 데이터 |
| **RAID 5** | 3 | N-1 | 1 | 공간 효율성과 안정성의 균형 | 쓰기 성능 저하(패리티 계산), 1개 고장 시 성능 저하 | 파일 서버, 백업 서버 등 일반적인 용도 |
| **RAID 6** | 4 | N-2 | 2 | **RAID 5보다 높은 안정성** (2개 디스크 장애 허용) | 쓰기 성능 저하가 더 심함 | 대용량 아카이브, 장기 보관용 데이터 |
| **RAID 10** | 4 | N/2 | 각 미러 셋당 1 | **매우 빠른 읽기/쓰기 성능과 높은 안정성을 모두 제공** | 비용이 가장 비쌈 | 고성능 데이터베이스, 가상화 환경 |

## 5. 실습 예제: LVM을 이용한 웹로그 파티션 생성

**요구사항**: 새로 추가된 디스크 `/dev/sdb`와 `/dev/sdc`를 사용하여, `log_vg`라는 볼륨 그룹을 만들고, 그 안에 `web_logs`라는 이름의 20GB 논리 볼륨을 생성한다. 이 볼륨을 XFS 파일 시스템으로 포맷하여 `/var/log/web`에 영구적으로 마운트하라.

### 해결 과정

```bash
# 1. 각 디스크에 LVM용 파티션 생성 (타입 8e)
# /dev/sdb
fdisk /dev/sdb <<EOF
g
n
1


t
8e
w
EOF

# /dev/sdc
fdisk /dev/sdc <<EOF
g
n
1


t
8e
w
EOF

# 2. Physical Volume(PV) 생성
pvcreate /dev/sdb1 /dev/sdc1

# 3. Volume Group(VG) 생성
vgcreate log_vg /dev/sdb1 /dev/sdc1

# 4. Logical Volume(LV) 생성
lvcreate -n web_logs -L 20G log_vg

# 5. XFS 파일 시스템으로 포맷
mkfs.xfs /dev/log_vg/web_logs

# 6. 마운트 포인트 생성 및 임시 마운트
mkdir -p /var/log/web
mount /dev/log_vg/web_logs /var/log/web

# 7. 영구 마운트를 위해 /etc/fstab에 등록
# LV의 UUID를 가져온다.
UUID=$(blkid -s UUID -o value /dev/log_vg/web_logs)

# fstab 파일에 추가한다.
echo "UUID=${UUID} /var/log/web xfs defaults,noatime 0 2" >> /etc/fstab

# 8. 최종 확인
mount -a
df -h | grep /var/log/web
```

### 분석
- `fdisk`의 here document(`<<EOF...EOF`) 구문을 사용하여 비대화형으로 파티셔닝을 자동화했다.
- `pvcreate`, `vgcreate`, `lvcreate` 명령어를 순차적으로 사용하여 LVM 스택을 구성했다.
- `-L 20G` 옵션으로 정확히 20GB 크기의 LV를 할당했다.
- `blkid`로 LV의 UUID를 동적으로 조회하여 `fstab`에 등록함으로써, 재부팅 시에도 안정적으로 마운트되도록 설정했다.
- 이 LVM 구성은 향후 로그 데이터가 증가하여 20GB를 초과할 경우, 새로운 디스크를 `log_vg`에 추가하고 `lvextend`와 `xfs_growfs`를 통해 서비스 중단 없이 용량을 확장할 수 있는 유연성을 제공한다.
# Day 4: 네트워크 심층 분석과 보안

네트워크는 현대 시스템의 동맥이자 가장 큰 공격 표면(Attack Surface)이다. 이 장에서는 소켓 레벨의 연결 상태를 정밀하게 추적하고, 커널 레벨의 방화벽을 통해 트래픽을 제어하며, 네트워크 패킷을 직접 검사하여 문제를 진단하고, 외부의 위협을 탐지하는 실무적인 네트워크 분석 및 보안 기술을 다룬다.

## 1. `ss`를 이용한 소켓 상태 정밀 분석

`netstat`이 `/proc` 파일시스템을 파싱하여 정보를 제공하는 반면, `ss`는 커널과 직접 통신하는 `netlink` 인터페이스를 사용하여 훨씬 빠르고 상세한 정보를 제공한다. 대규모 연결이 발생하는 서버에서 `netstat`은 그 자체로 부하가 될 수 있기에 `ss` 사용은 필수적이다.

- **`TIME-WAIT` 상태의 중요성**: `ss -tn state time-wait`
  - `TIME-WAIT`는 TCP 연결이 정상적으로 종료된 후, 동일한 포트와 주소를 사용하는 후속 연결에서 발생할 수 있는 패킷 중복 문제를 방지하기 위해 소켓이 잠시 대기하는 상태다.
  - 웹서버처럼 짧은 연결이 매우 빈번하게 일어나는 시스템에서는 `TIME-WAIT` 상태의 소켓이 과도하게 많아져 사용 가능한 포트를 고갈시킬 수 있다. 이는 새로운 연결을 맺지 못하는 심각한 장애로 이어진다. `ss`를 통한 `TIME-WAIT` 상태 모니터링은 서비스의 안정성을 진단하는 중요한 지표다.

- **정교한 상태 및 주소 필터링**:
  - `ss -tn '( dport = :443 or sport = :443 )'`
    - 대상 포트(`dport`) 혹은 출발지 포트(`sport`)가 443(HTTPS)인 모든 TCP 연결 조회. 괄호와 `or`를 이용해 복잡한 조건을 구성할 수 있다.
  - `ss -tp dst 1.2.3.4:80`
    - 목적지가 `1.2.3.4`의 80번 포트인 연결을 해당 프로세스 정보(`-p`)와 함께 조회.

## 2. 리눅스 방화벽: `iptables`의 상태 추적과 `firewalld`

### 2.1. `iptables` 상태 기반 필터링 (Stateful Inspection)

단순히 포트와 IP만으로 패킷을 허용/차단하는 것을 넘어, 연결의 '상태'를 추적하여 방화벽 규칙을 적용하는 것이 현대 방화벽의 핵심이다. 이는 `conntrack` 커널 모듈을 통해 이루어진다.

- **`RELATED,ESTABLISHED`의 마법**:
  - `iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT`
  - 이 단 한 줄의 규칙은, 이미 허용된 세션의 일부이거나(`ESTABLISHED`), 그 세션에 의해 파생된(`RELATED`, 예: FTP 데이터 채널) 모든 패킷을 허용한다.
  - **효과**: 외부에서 서버로 들어오는 새로운 연결(예: SSH, HTTP)에 대한 `ACCEPT` 규칙만 만들어두면, 서버가 그에 대한 응답으로 외부로 보내는 패킷이나 이후의 모든 양방향 통신은 이 규칙에 의해 자동으로 허용된다. 수많은 `OUTPUT` 규칙을 만들 필요가 없어진다.

- **로그 및 속도 제한을 통한 방어**:
  - **LOG Target**: 의심스러운 패킷을 버리기(`DROP`) 전에 로그로 남겨 공격 시도를 추적한다.
    - `iptables -A INPUT -p tcp --dport 22 -j LOG --log-prefix "SSH_ATTEMPT: "`
  - **Rate Limiting**: Brute-force 공격을 완화하기 위해 특정 시간 동안의 연결 수를 제한한다.
    - 아래 두 규칙은 60초 안에 4번 이상의 새로운 SSH 연결 시도를 하는 IP를 차단한다.
    ```bash
    # 새로운 SSH 연결 시도 IP를 'recent' 목록에 기록
    iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set --name SSH
    # 60초 내 4번 이상 목록에 기록된 IP의 새로운 연결은 차단
    iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 --name SSH -j DROP
    ```

### 2.2. `firewalld`와 Rich Rules

`firewalld`는 `iptables`나 `nftables`를 백엔드에서 제어하는 사용자 친화적인 방화벽 관리 도구다. Zone 개념을 통해 네트워크 인터페이스별로 다른 정책을 쉽게 적용할 수 있으며, 복잡한 규칙은 'Rich Rules'를 통해 구현한다.

- `firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" service name="ssh" accept'`
  - `192.168.1.0/24` 대역에서 들어오는 `ssh` 서비스 요청을 허용한다는 규칙을 직관적으로 추가할 수 있다.

## 3. `tcpdump`와 BPF(Berkeley Packet Filter)를 이용한 패킷 캡처

`tcpdump`는 단순히 `host`나 `port`로 필터링하는 것을 넘어, BPF 구문을 통해 패킷의 거의 모든 필드를 조건으로 사용할 수 있다.

- **TCP 플래그 필터링**: TCP 연결 과정(3-way handshake)이나 종료 과정을 분석할 때 매우 유용하다.
  - `tcpdump -nn 'tcp[tcpflags] & (tcp-syn|tcp-fin) != 0'`
  - `tcp-syn`: 연결 시작 패킷. `tcp-fin`: 연결 종료 패킷. `tcp-rst`: 연결 리셋 패킷.
  - 위 명령어는 `SYN` 또는 `FIN` 플래그가 설정된 패킷만 캡처하여 연결의 시작과 끝을 추적할 수 있다.

- **패킷 크기 필터링**: 비정상적으로 작거나 큰 패킷을 탐지할 때 사용.
  - `tcpdump -nn 'less 64'` : 64바이트 미만의 작은 패킷 캡처.

- **전문가의 워크플로우**: `tcpdump -i any -w capture.pcap 'host 1.2.3.4 and port 443'`
  - 서버에서는 BPF를 이용해 필요한 패킷만 최소한으로 캡처하여 `.pcap` 파일로 저장하고(`-w`), 이 파일을 로컬 PC로 가져와 그래픽 인터페이스를 제공하는 `Wireshark`에서 열어 심층 분석하는 것이 일반적인 표준 워크플로우다.

## 4. `nmap`을 이용한 포트 스캐닝과 시스템 탐지

`nmap`(Network Mapper)은 네트워크를 스캔하여 어떤 호스트가 살아있는지, 어떤 포트가 열려 있으며 어떤 서비스가 동작하는지 등을 알아내는 강력한 네트워크 탐사 도구다. 방어자의 입장에서 자신의 시스템이 외부에 어떻게 보이는지 점검하는 데 필수적이다. **(주의: 허가되지 않은 네트워크에 대한 스캔은 공격 행위로 간주될 수 있다.)**

- **기본 스캔**:
  - `nmap -sS target.com`: TCP SYN 스캔. 3-way handshake를 완료하지 않고 응답을 통해 포트 상태(open, closed, filtered)를 파악. 빠르고 비교적 은밀하여 가장 널리 쓰인다.
  - `nmap -sT target.com`: TCP Connect 스캔. 완전한 연결을 시도하므로 로그에 남기 쉽지만, SYN 스캔이 막힌 경우에 사용.
  - `nmap -sU target.com`: UDP 포트 스캔.
  - `nmap -p 1-1024 target.com`: 1번부터 1024번까지의 특정 포트 범위를 스캔.

- **상세 정보 스캔**:
  - `nmap -sV target.com`: 열려있는 포트에서 실행 중인 **서비스의 버전 정보**를 파악하려 시도.
  - `nmap -O target.com`: TCP/IP 스택 핑거프린팅을 통해 대상 호스트의 **운영체제**를 추측.
  - **`nmap -A target.com`**: `-sV`, `-O`, `traceroute`, 스크립트 스캔을 모두 포함하는 공격적인(Aggressive) 스캔.

- **NSE (Nmap Scripting Engine)**: `nmap`의 가장 강력한 기능. Lua 스크립트를 이용해 특정 취약점을 탐지하거나 더 많은 정보를 수집할 수 있다.
  - `nmap -sV --script=vuln target.com`: `vuln` 카테고리에 속한 모든 스크립트를 실행하여 알려진 취약점을 탐지.

## 5. 실습 예제: 로그 기반의 동적 IP 차단 스크립트

**요구사항**: `/var/log/secure` 로그 파일(또는 Debian/Ubuntu의 `/var/log/auth.log`)을 감시하여, 'Failed password'가 5회 이상 발생한 IP 주소를 찾아 `iptables`를 사용해 10분간 차단하는 스크립트를 작성하라. (10분 후 해제하는 로직은 `cron`이나 별도 데몬이 필요하므로, 이 예제에서는 차단 로직에 집중한다.)

### 스크립트: `simple_fail2ban.sh`

```bash
#!/bin/bash
set -euo pipefail

# 시스템에 따라 로그 파일 경로 변경
LOG_FILE="/var/log/auth.log" 
# LOG_FILE="/var/log/secure" 
LIMIT=5

# 'Failed password' 로그에서 IP를 추출하고, 횟수를 세어, LIMIT 이상인 IP만 골라냄
IP_LIST=$(grep "Failed password" "${LOG_FILE}" | grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}" | sort | uniq -c | awk -v limit="$LIMIT" '$1 >= limit {print $2}')

# 차단할 IP가 없으면 종료
if [ -z "${IP_LIST}" ]; then
    echo "No IPs to block."
    exit 0
fi

for IP in ${IP_LIST}
do
    # 이미 차단 규칙이 있는지 확인 (-C, --check)
    if ! iptables -C INPUT -s "${IP}" -j DROP > /dev/null 2>&1; then
        echo "Blocking IP: ${IP}"
        # INPUT 체인의 맨 위에(-I) 규칙을 삽입하여 가장 먼저 적용되도록 함
        iptables -I INPUT 1 -s "${IP}" -j DROP
    else
        echo "IP already blocked: ${IP}"
    fi
done
```

### 분석
1.  **`grep "Failed password"`**: 먼저 실패 로그가 포함된 라인을 필터링.
2.  **`grep -E -o "..."`**: 정규표현식을 이용해 해당 라인에서 IP 주소 형식의 문자열만 추출(`-o`).
3.  **`sort | uniq -c`**: 추출된 IP 목록을 정렬한 뒤, `uniq -c`를 통해 각 IP의 중복 발생 횟수를 카운트. (출력: `5 1.2.3.4`)
4.  **`awk -v limit="$LIMIT" '$1 >= limit {print $2}'`**: `awk`를 이용해 첫 번째 필드(카운트)가 설정한 `$LIMIT` 이상인 라인만 선택하여, 두 번째 필드(IP 주소)를 출력.
5.  **`for IP in ${IP_LIST}`**: 차단 대상 IP 목록을 순회.
6.  **`iptables -C INPUT ...`**: `-C` 옵션은 규칙이 존재하는지 '확인(Check)'만 한다. 규칙이 없으면 0이 아닌 코드를 반환하므로 `if`문의 조건으로 활용. 불필요한 중복 규칙 생성을 방지.
7.  **`iptables -I INPUT 1 ...`**: `-I`(Insert) 옵션은 규칙을 체인의 맨 위(1번)에 삽입한다. `-A`(Append)로 맨 뒤에 추가할 경우, 이전에 설정된 `ACCEPT` 규칙(예: `RELATED,ESTABLISHED`)에 먼저 매치되어 `DROP` 규칙이 무시될 수 있으므로, 차단 규칙은 맨 위에 두는 것이 안전하다.
8.  **실제 환경**: 이 스크립트를 `cron`으로 주기적으로 실행하고, 차단된 IP와 시간을 별도 파일에 기록한 뒤 다른 `cron` 작업이 일정 시간 후 `-D`(Delete) 옵션으로 규칙을 삭제하도록 구현하면 간단한 `fail2ban`이 완성된다. `fail2ban`은 이 과정을 훨씬 정교하게 처리해주는 전문 도구다.
# Day 4: 시스템 서비스와 로그 관리: systemd와 journald

현대 리눅스 시스템의 심장은 `systemd`다. `systemd`는 단순한 `init` 프로세스 대체재를 넘어, 시스템의 부팅 과정, 서비스 관리, 로그 수집, 예약 작업 등 시스템 전반을 제어하는 통합 관리 플랫폼이다. 과거의 복잡한 셸 스크립트 기반 `SysVinit` 체계를 대체하고, 선언적이고 의존성 기반의 유닛(Unit) 관리 방식을 도입하여 시스템을 더 빠르고, 안정적이며, 예측 가능하게 만들었다.

## 1. `systemd`의 이해: 유닛(Unit) 기반 아키텍처

`systemd`의 모든 관리 대상은 '유닛(Unit)'이라는 단위로 표현된다. 각 유닛은 설정 파일을 통해 정의되며, 이들의 관계를 통해 시스템의 상태가 결정된다.

- **주요 유닛(Unit) 타입**:
  - **`.service`**: 가장 일반적인 유닛. 시스템에서 데몬 형태로 실행되는 서비스. (예: `nginx.service`, `sshd.service`)
  - **`.socket`**: 특정 소켓(IP 주소와 포트)을 감시하다가, 연결 요청이 들어오면 해당 `.service` 유닛을 활성화시키는 유닛. (Socket Activation)
  - **`.target`**: 여러 유닛을 그룹화하는 논리적인 동기화 지점. 과거 SysVinit의 '런레벨(Runlevel)'을 대체한다. (예: `multi-user.target`, `graphical.target`)
  - **`.timer`**: `cron`과 같이 특정 시간이나 주기에 따라 다른 유닛을 활성화시키는 타이머 유닛.
  - **`.mount`**, **`.automount`**: 파일 시스템 마운트 포인트를 제어하는 유닛. `/etc/fstab`과 연동된다.

- **`systemctl`: `systemd` 제어 센터**
  `systemctl`은 이 모든 유닛을 관리하고 시스템의 상태를 조회하며 제어하는 중앙 집중식 커맨드라인 도구다.

## 2. `systemctl`을 이용한 서비스 관리

`systemctl`은 서비스의 생명주기(시작, 종료, 재시작)와 부팅 시 자동 실행 여부를 관리한다.

- **기본 명령어**:
  - `systemctl start [unit]`: 유닛 시작.
  - `systemctl stop [unit]`: 유닛 중지.
  - `systemctl restart [unit]`: 유닛 재시작.
  - `systemctl reload [unit]`: 유닛의 설정 파일을 다시 로드 (서비스 중단 없음). `ExecReload` 지시어가 정의되어 있어야 함.
  - `systemctl status [unit]`: **가장 중요한 명령어**. 유닛의 현재 상태(활성화 여부, PID), 최근 로그, CGroup을 통한 자원 사용량 등 종합적인 정보를 보여준다.

- **부팅 시 서비스 관리**:
  - `systemctl enable [unit]`: 부팅 시 유닛이 자동으로 시작되도록 활성화. (`[Install]` 섹션에 정의된 `.target`의 `.wants` 디렉토리에 심볼릭 링크를 생성하는 방식으로 동작)
  - `systemctl disable [unit]`: 자동 시작 비활성화.
  - `systemctl is-enabled [unit]`: 자동 시작 활성화 여부 확인.
  - `systemctl mask [unit]`: 유닛을 완전히 비활성화. `start`나 `enable`로도 절대 실행되지 않도록 `/dev/null`로 링크.

- **시스템 상태 조회**:
  - `systemctl list-units --type=service --state=running`: 현재 실행 중인 모든 서비스 유닛 목록.
  - `systemctl list-unit-files --type=service`: 설치된 모든 서비스 유닛과 그들의 `enable` 상태 목록.
  - `systemctl list-dependencies graphical.target`: 특정 타겟이 어떤 유닛들에 의존하고 있는지, 또는 어떤 유닛들이 해당 타겟에 의존하는지 트리 구조로 보여준다.

## 3. `systemd` 유닛 파일 작성법

패키지를 통해 설치된 유닛 파일은 `/usr/lib/systemd/system/`에 위치하며, 시스템 관리자가 직접 작성하거나 수정하는 파일은 `/etc/systemd/system/`에 위치한다. 후자의 경로가 우선순위가 높다.

- **유닛 파일의 3단 구조**:

  ```ini
  # /etc/systemd/system/my-app.service

  [Unit]
  Description=My Custom Application Service
  After=network.target

  [Service]
  Type=simple
  ExecStart=/usr/bin/python3 /opt/my-app/app.py
  User=www-data
  Group=www-data
  Restart=on-failure
  RestartSec=5s
  Environment="APP_ENV=production"

  [Install]
  WantedBy=multi-user.target
  ```

- **`[Unit]` 섹션**: 유닛의 메타데이터와 의존성 정의.
  - `Description`: `systemctl status` 등에서 표시될 설명.
  - `After=network.target`: 이 유닛이 `network.target`이 활성화된 *이후에* 시작되어야 함을 명시.
  - `Wants=`: 약한 의존성. `Wants`에 명시된 유닛이 실패해도 이 유닛은 시작을 시도함.
  - `Requires=`: 강한 의존성. `Requires`에 명시된 유닛이 시작에 실패하면 이 유닛도 시작되지 않음.

- **`[Service]` 섹션**: 서비스의 실행 동작 정의.
  - `Type`: 서비스의 프로세스 시작 방식.
    - `simple` (기본값): `ExecStart`에 지정된 프로세스가 주 프로세스.
    - `forking`: `ExecStart`의 프로세스가 자식 프로세스를 생성(fork)하고 자신은 종료하는 전통적인 데몬 방식. PIDFile 지시어와 함께 사용.
    - `oneshot`: 한 번만 실행되고 종료되는 스크립트에 사용.
  - `ExecStart`: 서비스를 시작할 명령어. **반드시 절대 경로를 사용해야 한다.**
  - `User`, `Group`: 보안을 위해 `root`가 아닌 특정 사용자의 권한으로 서비스를 실행.
  - `Restart=on-failure`: 서비스가 비정상 종료(non-zero exit code)되었을 때 자동으로 재시작. `always`는 정상 종료 시에도 재시작. 서비스의 안정성을 보장하는 핵심 기능.
  - `RestartSec=5s`: 재시작 전 5초를 대기.
  - `Environment`: 해당 서비스 프로세스에 적용될 환경 변수 설정.

- **`[Install]` 섹션**: `systemctl enable` 명령을 실행할 때의 동작 정의.
  - `WantedBy=multi-user.target`: `systemctl enable my-app.service` 실행 시, `multi-user.target`이 이 서비스를 원하도록(wants) 설정. 즉, 다중 사용자 모드로 부팅될 때 이 서비스가 시작되도록 함.

- **변경사항 적용**: 유닛 파일을 수정하거나 새로 생성한 후에는 반드시 `systemctl daemon-reload` 명령어를 실행하여 `systemd`가 변경사항을 인지하도록 해야 한다.

## 4. 중앙화된 로그 시스템: `journald`와 `journalctl`

`journald`는 `systemd`의 로그 관리 데몬이다. 커널 메시지(`dmesg`), 모든 서비스의 표준 출력(stdout)/표준 에러(stderr), `syslog`를 통해 들어오는 로그 등 시스템의 모든 로그를 중앙에서 수집하여 구조화된 바이너리 형식으로 저장한다.

- **`journald`의 장점**:
  - **구조화된 로깅**: 모든 로그 항목에 PID, UID, 서비스 유닛 이름, 시간 등이 메타데이터로 자동 첨부되어 정밀한 필터링이 가능.
  - **중앙 관리**: `/var/log` 아래에 흩어져 있던 로그 파일들을 단일 시스템(`journal`)에서 관리.
  - **빠른 검색**: 바이너리 형식과 인덱싱을 통해 텍스트 파일 기반 로그보다 검색 속도가 월등히 빠름.

- **`journalctl`: 저널을 조회하는 만능 도구**
  - `journalctl`: 전체 저널을 시간 순(오래된 것부터)으로 출력.
  - `journalctl -f`: 새로운 로그를 실시간으로 스트리밍 (`tail -f`와 동일).
  - `journalctl -u nginx.service`: **(가장 많이 사용)** 특정 유닛의 로그만 필터링.
  - `journalctl -u nginx --since "1 hour ago"`: 시간 기반 필터링. `"yesterday"`, `"2025-11-25 10:00:00"` 등 다양한 형식 지원.
  - `journalctl -p err`: 에러(err) 등급 이상의 로그만 필터링. (`-p 3`와 동일).
  - `journalctl -k`: 커널 메시지(`dmesg`의 대체재)만 출력.
  - `journalctl -o json-pretty`: 로그를 JSON 형식으로 예쁘게 출력. 스크립트로 처리하거나 외부 로그 시스템으로 전송할 때 유용.

- **로그 영구 보존**: 일부 시스템에서는 기본적으로 저널이 메모리에만 저장되어 재부팅 시 사라진다. 로그를 영구적으로 보존하려면:
  - `mkdir -p /var/log/journal`
  - 위 디렉토리를 생성하기만 하면 `systemd-journald`가 자동으로 인식하여 해당 디렉토리에 저널 파일을 저장하기 시작한다. 세부 설정은 `/etc/systemd/journald.conf` 파일에서 관리(예: 최대 저장 용량 `SystemMaxUse`).

## 5. 실습 예제: Python 웹 앱을 `systemd` 서비스로 등록하기

**요구사항**: 간단한 Python 웹 애플리케이션을 만들고, 부팅 시 자동으로 시작되며, 비정상 종료 시 자동으로 재시작되는 `systemd` 서비스로 등록한다. 모든 출력은 `journald`를 통해 확인한다.

### 1. Python 웹 앱 생성

```bash
# 디렉토리 및 파일 생성
mkdir -p /opt/webapp
cat > /opt/webapp/app.py <<EOF
import http.server
import socketserver
import time
import random

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 10% 확률로 "crash" 발생
        if random.random() < 0.1:
            print("Simulating a random crash!")
            # 비정상 종료를 위해 0이 아닌 코드로 exit
            exit(1)
            
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = f"Hello from systemd service! Current time is {time.asctime()}"
        self.wfile.write(bytes(message, "utf8"))
        print(f"Responded to {self.client_address[0]}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server starting on port {PORT}")
    httpd.serve_forever()
EOF
```
이 앱은 8080 포트에서 간단한 웹 서버를 실행하며, 요청 시 10% 확률로 스스로 비정상 종료하여 `Restart=on-failure` 기능을 테스트할 수 있게 한다.

### 2. `systemd` 유닛 파일 작성

```bash
cat > /etc/systemd/system/webapp.service <<EOF
[Unit]
Description=My Simple Python Web App
After=network.target

[Service]
Type=simple
User=nobody
Group=nogroup
WorkingDirectory=/opt/webapp
ExecStart=/usr/bin/python3 -u /opt/webapp/app.py
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
EOF
```
- `WorkingDirectory`: 서비스가 실행될 작업 디렉토리를 지정.
- `python3 -u`: `-u` 옵션은 출력을 버퍼링하지 않도록 하여 로그가 `journald`에 즉시 전달되게 하는 중요한 옵션.

### 3. 서비스 관리 및 테스트

```bash
# 1. systemd에 새 유닛 파일 알림
systemctl daemon-reload

# 2. 서비스 시작 및 상태 확인
systemctl start webapp.service
systemctl status webapp.service

# 3. 서비스 동작 테스트 (정상 응답 확인)
curl http://127.0.0.1:8080

# 4. 로그 확인
journalctl -u webapp.service -f

# 5. 자동 재시작 테스트
# curl을 여러 번 실행하여 10% 확률의 crash를 유도하거나,
# 직접 PID를 찾아 강제 종료
# pkill -f /opt/webapp/app.py
# 5초 후 'systemctl status webapp.service'를 다시 실행하면
# Active: active (running) 상태이며 PID가 변경된 것을 통해 재시작되었음을 확인 가능.

# 6. 부팅 시 자동 시작 활성화
systemctl enable webapp.service
```

### 분석
이 예제를 통해 우리는 단순히 스크립트를 실행하는 것을 넘어, `systemd`를 통해 서비스의 생명주기를 관리하고(`Restart=on-failure`), 보안을 강화하며(`User=nobody`), 로그를 중앙에서 효율적으로 수집하는 현대적인 리눅스 서비스 관리의 전 과정을 실습했다.
# Day 5: 쉘 스크립트 고급 테크닉과 자동화

단순한 명령어의 나열을 넘어, 쉘 스크립트를 하나의 완전한 애플리케이션처럼 견고하고, 예측 가능하며, 안전하게 만드는 고급 기법들을 익힌다. 이 장에서는 에러 처리, 표준 인자 파싱, 예외 처리, 동시성 제어 등 실무 스크립팅의 핵심 요소를 다룬다.

## 1. 방어적 Bash 프로그래밍 (Defensive Bash Programming)

스크립트가 예기치 않은 상황에서도 치명적인 오작동을 일으키지 않도록 방어 장치를 마련하는 것은 전문가의 기본 소양이다.

### 1.1. `set -euo pipefail`: 스크립트의 안전벨트

모든 실무용 쉘 스크립트의 시작은 이 한 줄이어야 한다.

```bash
#!/bin/bash
set -euo pipefail
```

- **`set -e` (`errexit`)**: 명령어가 0이 아닌 종료 코드로 실패할 경우, 즉시 스크립트 전체를 중단시킨다. `cd`가 실패했는데도 뒤따르는 `rm -rf *`가 실행되는 대참사를 막아준다.
- **`set -u` (`nounset`)**: 초기화되지 않은 변수를 사용하려고 할 때, 에러로 간주하고 스크립트를 중단시킨다. 변수명 오타로 인한 버그를 원천 차단한다.
- **`set -o pipefail`**: 파이프라인(`|`)에 연결된 명령어 중 하나라도 실패하면, 전체 파이프라인의 종료 코드가 그 실패한 명령어의 코드로 설정된다. 파이프라인 중간의 실패를 무시하고 지나가는 것을 방지한다.

### 1.2. 변수 확장(Parameter Expansion)을 이용한 입력값 검증 및 처리

- **`${variable:?error_message}`**: 변수가 설정되지 않았거나 비어있으면 `error_message`를 표준 에러로 출력하고 스크립트를 즉시 중단시킨다. 스크립트에 필수적인 인자나 환경 변수가 주어졌는지 검증하는 가장 간결하고 강력한 방법이다.
  - `REQUIRED_VAR="${REQUIRED_VAR:?이 환경 변수는 반드시 설정해야 합니다.}"`
- **`${variable:-default}`**: 변수가 설정되지 않았거나 비어있으면 `default` 값을 사용한다.
  - `LOG_LEVEL="${LOG_LEVEL:-INFO}"`
- **`${variable##pattern}`, `${variable%pattern}`**: 변수의 내용에서 특정 패턴을 제거. 파일 경로를 다룰 때 매우 유용하다.
  - `FULL_PATH="/var/log/nginx/access.log"`
  - `FILENAME="${FULL_PATH##*/}"` # 결과: `access.log` (가장 긴 `*/` 패턴을 앞에서부터 제거)
  - `DIR_PATH="${FULL_PATH%/*}"` # 결과: `/var/log/nginx` (가장 짧은 `/*` 패턴을 뒤에서부터 제거)

## 2. `getopts`: 표준 유틸리티 스타일의 인자 파싱

`$1`, `$2`로 인자를 직접 처리하는 방식은 순서가 바뀌거나 옵션이 복잡해지면 금방 한계에 부딪힌다. `getopts`는 `ls -l -a`처럼 표준적인 짧은 옵션(`-l`, `-a` 등)과 옵션에 대한 인자(예: `-f file.txt`)를 파싱하는 쉘 내장 기능이다.

- **`getopts` 기본 사용법**:
  ```bash
  #!/bin/bash
  
  # 사용법 안내 함수
  usage() {
      echo "Usage: $0 [-s SOURCE_DIR] [-o OUTPUT_FILE] [-v]"
      exit 1
  }

  VERBOSE=false
  # getopts의 첫 인자 문자열에서, 콜론(:)이 앞에 오면 쉘이 에러를 직접 처리하지 않게 함.
  # 글자 뒤에 콜론이 오면 해당 옵션은 인자를 필요로 함을 의미 (예: s:, o:)
  while getopts ":s:o:vh" opt; do
      case ${opt} in
          s) SOURCE_DIR="${OPTARG}" ;;
          o) OUTPUT_FILE="${OPTARG}" ;;
          v) VERBOSE=true ;;
          h) usage ;;
          \?) echo "에러: 유효하지 않은 옵션입니다: -${OPTARG}" >&2; usage ;;
          :) echo "에러: -${OPTARG} 옵션은 인자가 필요합니다." >&2; usage ;;
      esac
  done
  shift $((OPTIND - 1)) # 파싱된 옵션들을 인자 목록에서 제거

  # 필수 인자 검증
  : "${SOURCE_DIR:?Source directory (-s) is required.}"
  : "${OUTPUT_FILE:?Output file (-o) is required.}"
  
  echo "Source: ${SOURCE_DIR}"
  echo "Output: ${OUTPUT_FILE}"
  echo "Verbose: ${VERBOSE}"
  echo "Remaining args: $@"
  ```
- **`OPTARG`**: 옵션이 인자를 가질 때, 그 인자 값이 저장되는 변수.
- **`OPTIND`**: 다음에 처리할 인자의 인덱스. `shift`와 함께 사용하여 옵션 파싱이 끝난 후 남은 일반 인자들을 처리할 수 있게 한다.

## 3. `trap`: 예외 처리와 정리(Cleanup) 작업

`trap`은 스크립트가 특정 시그널을 받았을 때 미리 지정해둔 명령어를 실행하게 하는 기능이다. 스크립트가 비정상적으로 종료되더라도 임시 파일을 삭제하거나 DB 커넥션을 닫는 등의 정리 작업을 보장하기 위해 필수적으로 사용된다.

- **`trap 'cleanup_function' EXIT`**: 가장 일반적인 사용법. 스크립트가 어떤 방식(정상 종료, 에러, `Ctrl+C`)으로든 **종료(EXIT)**될 때 `cleanup_function`을 실행한다.
- **`trap 'echo "Ctrl-C pressed!"; exit 1' SIGINT`**: `Ctrl+C`에 해당하는 `SIGINT` 시그널을 받았을 때 특정 동작을 수행하도록 지정.

- **`mktemp`과 `trap`을 이용한 안전한 임시 디렉토리 활용**:
  ```bash
  # 스크립트 시작 부분
  TMP_DIR=$(mktemp -d)

  # 정리 함수 정의
  cleanup() {
      echo "Cleaning up temporary directory: ${TMP_DIR}"
      rm -rf "${TMP_DIR}"
  }

  # 스크립트 종료 시 cleanup 함수가 실행되도록 예약
  trap cleanup EXIT

  # 스크립트 본문...
  echo "Working in ${TMP_DIR}"
  # ...
  ```
  이 구조를 사용하면 스크립트가 중간에 실패하더라도 임시 디렉토리는 항상 안전하게 삭제된다.

## 4. 고급 자동화 기법

- **프로세스 치환 (Process Substitution) `<(command)`**: 명령어의 출력을 파이프가 아닌, 임시 파일처럼 다룰 수 있게 해준다. `diff`처럼 두 개의 파일명을 인자로 받는 명령어에 매우 유용하다.
  - `diff <(sort fileA.txt) <(sort fileB.txt)`: `fileA.txt`와 `fileB.txt`를 각각 정렬한 후 그 결과를 비교. 임시 파일을 만들 필요가 없다.

- **배열(Array)과 `mapfile`**: 공백이 포함된 파일 목록 등을 안전하게 처리하려면 배열을 사용하는 것이 좋다.
  - `mapfile -t files_array < <(find . -type f -name "*.log")`
  - `find`의 결과를 한 줄씩 읽어 `files_array`라는 배열에 담는다.
  - `for file in "${files_array[@]}"; do echo "Processing: ${file}"; done`

- **`flock`을 이용한 중복 실행 방지**: `cron` 작업이 예상보다 길어져 이전 작업이 끝나기 전에 다음 작업이 시작되는 것을 막기 위한 가장 간단하고 효과적인 방법이다.
  - **Cron에서의 사용**:
    `* * * * * /usr/bin/flock -n /var/run/my_cron.lock /path/to/my_script.sh`
    - `-n`: lock을 즉시 얻을 수 없으면 기다리지 않고 실패.
  - **스크립트 내부에서의 사용**: 스크립트 전체를 서브쉘과 파일 디스크립터를 이용해 잠글 수 있다.
    ```bash
    (
        flock -n 200 || { echo "Script is already running."; exit 1; }
        # --- 실제 스크립트 로직 ---
        echo "Script started. PID: $$"
        sleep 10
        echo "Script finished."
        # -------------------------
    ) 200>/var/run/my_script.lock
    ```

## 5. 실습 예제: 고급 백업 스크립트

**요구사항**: 아래 기능을 모두 포함하는 견고한 백업 스크립트 `backup.sh`를 작성한다.
1. 소스 디렉토리(`-s`)와 대상 디렉토리(`-d`)를 필수로 받는다.
2. 아카이브 파일명(`-n`)을 옵션으로 받으며, 지정하지 않으면 `backup-YYYY-MM-DD.tar.gz` 형식으로 자동 생성된다.
3. 상세 정보 출력 모드(`-v`)를 지원한다.
4. 임시 디렉토리를 사용하며, 스크립트 종료 시 반드시 정리되도록 `trap`을 사용한다.
5. 스크립트가 동시에 중복 실행되지 않도록 `flock`을 사용한다.

### 최종 스크립트: `backup.sh`

```bash
#!/bin/bash
set -euo pipefail

# --- 기본 변수 및 함수 ---
APP_NAME="${0##*/}"
LOCK_FILE="/var/run/${APP_NAME}.lock"
VERBOSE=false

usage() {
    cat <<EOF
Usage: ${APP_NAME} -s SOURCE_DIR -d DEST_DIR [-n ARCHIVE_NAME] [-v] [-h]
    -s  Source directory to back up.
    -d  Destination directory for the backup file.
    -n  Optional: Name of the archive file. Defaults to backup-YYYY-MM-DD.tar.gz.
    -v  Verbose mode.
    -h  Show this help message.
EOF
    exit 1
}

log() {
    # ${VERBOSE}가 true일 때만 메시지 출력
    [[ "${VERBOSE}" = true ]] && echo "$(date '+%F %T') - $*"
}

# --- 인자 파싱 ---
while getopts ":s:d:n:vh" opt; do
    case ${opt} in
        s) SOURCE_DIR="${OPTARG}" ;;
        d) DEST_DIR="${OPTARG}" ;;
        n) ARCHIVE_NAME="${OPTARG}" ;;
        v) VERBOSE=true ;;
        h) usage ;;
        \?) echo "Error: Invalid option: -${OPTARG}" >&2; usage ;;
        :) echo "Error: Option -${OPTARG} requires an argument." >&2; usage ;;
    esac
done
shift $((OPTIND - 1))

# --- 필수 인자 검증 ---
: "${SOURCE_DIR:?Source directory (-s) must be provided.}"
: "${DEST_DIR:?Destination directory (-d) must be provided.}"
[[ ! -d "${SOURCE_DIR}" ]] && { echo "Error: Source directory '${SOURCE_DIR}' not found." >&2; exit 1; }
mkdir -p "${DEST_DIR}" # 대상 디렉토리가 없으면 생성

# --- 파일명 기본값 설정 ---
ARCHIVE_NAME="${ARCHIVE_NAME:-backup-$(date +%F).tar.gz}"
FINAL_BACKUP_PATH="${DEST_DIR}/${ARCHIVE_NAME}"

# --- 정리 작업 및 동시 실행 방지 ---
TMP_DIR=$(mktemp -d)
trap 'log "Cleaning up temporary directory..."; rm -rf "${TMP_DIR}"' EXIT

(
    flock -n 200 || { echo "Script is already running." >&2; exit 1; }

    log "Starting backup..."
    log "Source: ${SOURCE_DIR}"
    log "Destination: ${FINAL_BACKUP_PATH}"

    # tar 아카이브 생성
    # -C 옵션: 해당 디렉토리로 이동한 후 압축을 시작하여, 경로가 포함되지 않게 함.
    tar_opts="-cf"
    [[ "${VERBOSE}" = true ]] && tar_opts="-cvf"
    tar "${tar_opts}" "${TMP_DIR}/${ARCHIVE_NAME}" -C "${SOURCE_DIR}" .

    log "Moving archive to destination..."
    mv "${TMP_DIR}/${ARCHIVE_NAME}" "${FINAL_BACKUP_PATH}"

    log "Backup complete: ${FINAL_BACKUP_PATH}"
    ls -lh "${FINAL_BACKUP_PATH}"

) 200>"${LOCK_FILE}"
```

### 분석
- 이 스크립트는 `getopts`로 표준 인자를 파싱하고, 변수 확장(`:?`)으로 필수 인자를 검증하며, `mktemp`과 `trap`으로 안전한 임시 공간을 확보/정리한다.
- 스크립트의 핵심 로직 전체가 `( ... ) 200>lockfile` 구문으로 감싸여 있어, `flock`이 스크립트 실행 동안 잠금을 유지하여 `cron` 등으로 인한 중복 실행을 완벽하게 방지한다.
- `tar` 명령어에서 `-C` 옵션을 활용하여 불필요한 상위 경로 없이 깔끔하게 소스 디렉토리의 내용만 압축하는 실무 테크닉을 사용했다.
- `log` 함수를 통해 `-v` 옵션이 있을 때만 상세 메시지가 출력되도록 제어한다.
# Day 5: 시스템 관리 자동화와 쉘 스크립트

시스템 관리의 궁극적인 목표는 안정적이고 예측 가능한 시스템을 최소한의 노력으로 운영하는 것이다. 이를 위해 반복적인 작업을 자동화하고, 대량의 데이터를 효율적으로 처리하며, 재해로부터 시스템을 복구할 수 있는 안정적인 백업 체계를 구축하는 것은 필수적이다. 이 장에서는 `cron`, `at`, `xargs`, `rsync` 등 자동화와 데이터 처리를 위한 핵심 도구들을 마스터한다.

## 1. 작업 스케줄링의 정석: `cron`

`cron`은 특정 시간에 특정 명령어를 주기적으로 실행하도록 예약하는 리눅스의 표준 스케줄러다. 매일 새벽의 백업, 매시간 로그 분석 등 모든 종류의 정기적인 작업을 `cron`을 통해 자동화할 수 있다.

- **Crontab 구조**: `분(0-59) 시(0-23) 일(1-31) 월(1-12) 요일(0-7) /실행할/명령어`
  - `*`: 모든 값을 의미. (예: `*`가 '분' 필드에 있으면 '매 분마다')
  - `*/n`: n 간격으로. (예: `*/5`가 '분' 필드에 있으면 '5분마다')
  - `n,m`: n과 m일 때. (예: `1,30`이 '분' 필드에 있으면 '1분과 30분에')

- **`crontab` 관리**:
  - `crontab -e`: 현재 사용자의 crontab 파일을 편집.
  - `crontab -l`: 현재 사용자의 crontab 목록을 출력.
  - `crontab -r`: **(매우 위험)** 현재 사용자의 crontab을 **묻지도 않고 모두 삭제**하므로 극히 주의해야 한다.

- **`cron` 실행 환경의 함정**:
  - **최소 환경 변수**: `cron`은 매우 제한된 `PATH` 환경 변수(`PATH=/usr/bin:/bin`)를 가지고 실행된다. 따라서 스크립트나 명령어는 `/usr/local/bin/my_script.sh` 와 같이 항상 절대 경로로 지정하는 것이 안전하다.
  - **출력 처리**: `cron` 작업의 모든 표준 출력(stdout)과 표준 에러(stderr)는 시스템 메일로 전송된다. 메일 시스템이 설정되어 있지 않으면 이 출력들은 유실되거나 시스템 어딘가에 쌓인다.
    - **Best Practice**: 출력은 항상 명시적으로 리다이렉션한다.
      - `... > /dev/null 2>&1`: 모든 출력을 버린다.
      - `... >> /var/log/my_job.log 2>&1`: 모든 출력을 로그 파일에 기록한다.

## 2. 일회성 작업 예약: `at`

`cron`이 주기적인 작업을 위한 것이라면, `at`은 미래의 특정 시간에 단 한 번만 실행될 작업을 예약하는 명령어다. "10분 후에 시스템을 재부팅해라" 와 같은 작업에 사용된다.

- **`at` 사용법**:
  - `at now + 30 minutes`: 30분 후에 실행할 작업을 대화형 모드로 입력 시작. 원하는 명령어들을 입력한 후 `Ctrl+D`로 입력을 마친다.
  - `echo "shutdown -h now" | at 2:00am tomorrow`: 파이프를 이용해 특정 시간에 실행될 명령어를 예약.
  - `at -f /path/to/script.sh 16:00`: 특정 시간에 스크립트 파일을 실행.

- **작업 관리**:
  - `atq`: 현재 예약된 작업 목록을 확인.
  - `atrm <작업번호>`: 예약된 작업을 취소.

## 3. `xargs`: 파이프라인의 슈퍼차저

`xargs`는 표준 입력(stdin)으로부터 텍스트를 읽어들여, 이를 후속 명령어의 인자(argument)로 넘겨주는 강력한 도구다. `find`와 조합하여 대량의 파일에 대한 일괄 작업을 수행할 때 그 진가가 드러난다.

- **`find`와의 연동**:
  - `find . -name "*.tmp" -print0 | xargs -0 rm`: `find`의 결과(파일명)를 `xargs`가 받아서 `rm` 명령어의 인자로 넘겨 삭제한다.
  - **`-print0`과 `-0`**: 파일명에 공백이나 특수문자가 포함된 경우를 안전하게 처리하기 위한 필수적인 조합. `find`는 파일명을 NULL 문자로 구분하여 출력하고(`-print0`), `xargs`는 NULL 문자를 기준으로 인자를 읽어들인다(`-0`).

- **병렬 처리 (`-P`)**: `xargs`의 가장 강력한 기능 중 하나. 여러 개의 작업을 동시에 실행하여 처리 속도를 극적으로 높일 수 있다.
  - `cat url-list.txt | xargs -P 8 -n 1 wget`
  - `-P 8`: 최대 8개의 `wget` 프로세스를 동시에 실행.
  - `-n 1`: `url-list.txt`에서 한 줄씩 읽어 각 `wget` 명령어에 하나의 인자로 전달.
  - CPU 코어 수에 맞춰 `-P` 옵션을 조절하면, 수백 개의 URL을 다운로드하거나 수천 개의 이미지를 리사이징하는 등의 작업을 매우 빠르게 처리할 수 있다.

## 4. 지능형 동기화 및 백업: `rsync`

`rsync`는 단순한 파일 복사(`cp`)를 넘어, 소스와 대상의 차이점만 계산하여 전송하는 '델타 전송 알고리즘'을 사용하는 지능형 동기화 도구다. 원격지 백업, 서버 미러링 등에서 절대적인 위치를 차지한다.

- **핵심 옵션 `-avz`**:
  - `-a` (archive mode): 아카이브 모드. `-rlptgoD` 옵션을 모두 합친 것과 같다. 퍼미션, 소유권, 타임스탬프, 심볼릭 링크 등 파일의 모든 속성을 그대로 보존하며 재귀적으로 복사한다.
  - `-v` (verbose): 진행 과정을 상세히 보여준다.
  - `-z` (compress): 전송 중에 데이터를 압축하여 네트워크 대역폭을 절약한다.

- **사용 패턴**:
  - **Trailing Slash의 중요성**: `rsync -av /src/ /dest`는 `/src`의 **내용물**을 `/dest`로 복사하지만, `rsync -av /src /dest`는 `/src` **디렉토리 자체**를 `/dest` 아래에 복사한다.
  - **원격 서버로 Push**: `rsync -avz /local/data user@remote:/remote/backup/`
  - **원격 서버에서 Pull**: `rsync -avz user@remote:/remote/data /local/backup/`

- **고급 기능**:
  - `--delete`: 소스에 존재하지 않는 파일은 대상 디렉토리에서 **삭제한다**. 완벽한 미러링을 구성할 때 사용하지만, 데이터 유실의 위험이 있으므로 신중하게 사용해야 한다.
  - `--exclude=PATTERN`: 특정 패턴과 일치하는 파일을 제외한다. (`--exclude='*.log'`)
  - `--link-dest=DIR`: 증분 백업(Incremental Backup)의 핵심. 이전 백업본이 있는 디렉토리를 지정하면, 변경되지 않은 파일은 새로 복사하는 대신 이전 백업본의 파일에 대한 하드 링크를 생성한다. 이를 통해 매일 백업을 받아도 변경된 파일만 용량을 차지하는 효율적인 백업 시스템을 구축할 수 있다.

## 5. 실습 예제: 로그 로테이션(Log Rotation) 스크립트

**요구사항**: `/var/log/app.log` 파일이 무한정 커지는 것을 막기 위해, 이 파일을 주기적으로 백업하고 비우는 로그 로테이션 스크립트를 작성한다.
1. `app.log`는 `app.log.1`로 이름을 바꾼다.
2. 이미 `app.log.1`이 존재하면 `app.log.2`로, `app.log.2`는 `app.log.3`으로 순차적으로 밀어낸다. (최대 5개까지 보관)
3. `app.log.5`는 삭제된다.
4. 기존 `app.log`를 옮긴 후, 새로운 빈 `app.log` 파일을 생성한다.
5. 로그 파일을 사용하는 애플리케이션(PID 파일로 식별)에 `SIGHUP` 시그널을 보내 로그 파일을 다시 열도록 한다.

### 스크립트: `simple_logrotate.sh`

```bash
#!/bin/bash
set -e # 에러 발생 시 즉시 중단

LOG_FILE="/var/log/app.log"
PID_FILE="/var/run/app.pid"
MAX_ROTATIONS=5

# 로그 파일이 없으면 실행할 필요 없음
[ ! -f "${LOG_FILE}" ] && exit 0

# 가장 오래된 백업 파일 삭제
[ -f "${LOG_FILE}.${MAX_ROTATIONS}" ] && rm "${LOG_FILE}.${MAX_ROTATIONS}"

# 기존 백업 파일들을 하나씩 뒤로 밀어내기 (4 -> 5, 3 -> 4 ...)
for i in $(seq $((MAX_ROTATIONS - 1)) -1 1); do
    if [ -f "${LOG_FILE}.${i}" ]; then
        echo "Rotating ${LOG_FILE}.${i} to ${LOG_FILE}.$((i+1))"
        mv "${LOG_FILE}.${i}" "${LOG_FILE}.$((i+1))"
    fi
done

# 현재 로그 파일을 첫 번째 백업 파일로 로테이트
echo "Rotating ${LOG_FILE} to ${LOG_FILE}.1"
mv "${LOG_FILE}" "${LOG_FILE}.1"

# 새로운 빈 로그 파일 생성 및 권한 설정
touch "${LOG_FILE}"
# 필요시 chown, chmod로 권한 설정

# 데몬에게 로그 파일을 다시 열도록 SIGHUP 시그널 전송
if [ -f "${PID_FILE}" ]; then
    kill -HUP "$(cat ${PID_FILE})"
    echo "Sent SIGHUP to process $(cat ${PID_FILE})"
else
    echo "Warning: PID file '${PID_FILE}' not found. Could not send SIGHUP." >&2
fi
```

### 분석
- **파일 이동 순서**: 가장 오래된 파일부터 삭제하고, 뒤에서부터 순서대로 `mv`를 실행해야 파일 덮어쓰기를 방지할 수 있다. `seq $((MAX_ROTATIONS - 1)) -1 1`은 4, 3, 2, 1 순서의 숫자열을 생성한다.
- **`touch`의 역할**: `mv`로 로그 파일을 옮긴 후, 새로운 빈 파일을 즉시 생성하여 애플리케이션이 로그를 기록할 때 파일이 없어 발생하는 에러를 방지한다.
- **`kill -HUP`의 중요성**: 단순히 `mv`로 로그 파일을 옮겨도, 기존에 실행 중이던 애플리케이션은 여전히 과거 파일(`app.log.1`이 된)을 가리키는 파일 디스크립터(File Descriptor)를 계속 붙들고 있다. `SIGHUP` 시그널을 보내야 애플리케이션이 설정(및 로그 파일 핸들)을 다시 로드하여 새로 생성된 `app.log` 파일에 로그를 쓰기 시작한다.
- **실제 환경**: 이 스크립트를 `cron`에 등록하여 매일 자정(`0 0 * * *`)에 실행하면 수동 로그 로테이션 시스템이 된다. 실제로는 이 모든 기능을 훨씬 정교하게 제공하는 표준 유틸리티 `logrotate`를 사용하는 것이 일반적이지만, 위 스크립트는 그 내부 동작 원리를 이해하는 데 훌륭한 예제다.
