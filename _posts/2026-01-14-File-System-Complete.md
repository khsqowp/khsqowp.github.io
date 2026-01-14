--- 
title: "파일 시스템 보안 위협: 경로 조작과 임의 파일 읽기/쓰기 분석"
date: 2026-01-14
excerpt: "Path Traversal과 부적절한 파일 업로드 기능을 이용한 파일 시스템 공격 기법을 마스터합니다. 시스템의 민감한 설정 파일을 탈취하거나 웹쉘을 실행하는 실전 공격 시나리오와 파일 시스템 보호를 위한 보안 가이드를 학습합니다."
categories:
  - Project
  - CTF
  - FIVENINES
tags:
  - FIVENINES
  - Project
  - CTF
---

# File System 완전 정복 가이드

> 5개의 실전 문제로 배우는 파일 시스템 공격 기법

## 📚 목차

- [학습 가이드](#학습-가이드)
- [문제 목록](#문제-목록)
  - [🟢 Beginner](#beginner)
  - [🟡 Intermediate](#intermediate)
  - [🔴 Advanced](#advanced)
- [핵심 개념 정리](#핵심-개념-정리)
- [방어 기법](#방어-기법)
- [참고 자료](#참고-자료)

---

## 학습 가이드

### 추천 학습 순서

1. **Read_Me** (Beginner) - 디렉토리 리스팅 취약점 기초 - 15분
2. **Steganography** (Beginner) - LSB 스테가노그래피 분석 - 30분
3. **Download_I** (Intermediate) - Path Traversal 기본 - 40분
4. **Download_II** (Intermediate) - 필터 우회 기법 (중첩 페이로드) - 45분
5. **Upload_II** (Advanced) - .htaccess 업로드 공격 - 60분

**총 학습 시간**: 약 3시간 10분

### 학습 목표

이 카테고리를 완료하면:

- ✅ 디렉토리 리스팅(Directory Listing) 취약점 식별 및 악용
- ✅ Path Traversal 공격의 원리와 다양한 우회 기법 습득
- ✅ 스테가노그래피 기법 (LSB) 이해 및 분석 능력 확보
- ✅ 파일 업로드 취약점과 서버 설정 조작 방법 이해
- ✅ .htaccess 파일을 이용한 서버 보안 무력화 기법
- ✅ 파일명 검증 우회 및 필터링 회피 전략 수립
- ✅ 안전한 파일 처리 시스템 설계 능력 확보

### script 연동

**관련 Phase**: File System Security
- Phase 2: [파일 시스템 취약점 기초](/script/phase2-vulnerability-basics/)
- Phase 3: [Path Traversal 자동화](/script/phase3-automation/)
- Phase 4: [고급 파일 업로드 공격](/script/phase4-advanced-techniques/)

---

## 문제 목록

### 🟢 Beginner

#### [Hacker's Diary] Read Me: 경로 속에 숨겨진 힌트

**난이도**: 🟢 Beginner
**예상 시간**: ⏱️ 15분
**주요 기술**: `#Directory-Listing` `#Information-Disclosure` `#Misconfiguration`
**관련 스크립트**: [solve_read_me.sh](../Scripts/solve_read_me.sh)

## 1. 개요
디렉토리 경로 분석을 통해 숨겨진 파일을 찾아내고 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 가설 1: 디렉토리 리스팅(Directory Listing)
*   `page/` 디렉토리나 루트 디렉토리에 파일 목록 출력이 활성화되어 있어 숨겨진 파일을 발견할 수 있을 것이다.

### 가설 2: README 파일 탐색
*   문제 제목과 일치하는 `README.txt`, `README.md`, `README` 등의 파일이 경로상에 존재할 것이다.

### 2단계: 디렉토리 리스팅 및 파일 접근
`http://3.35.141.246/challenges/read_me/page/` 경로에서 디렉토리 리스팅 취약점을 확인하였고, 내부에 존재하는 `password_Re@d_Me.php` 파일을 발견했다. 해당 파일에 직접 접근하여 플래그를 확인했다.

*   **최종 FLAG**: `72eb9489d0edd3193ad94109eb58d672`

## 4. 결과: 부적절한 설정으로 인한 정보 유출
웹 서버의 디렉토리 리스팅 설정이 켜져 있어 관리자가 의도하지 않은 파일(패스워드나 플래그가 포함된 파일)이 외부로 노출되었다. "경로를 살피라"는 힌트는 이러한 설정 오류를 찾아내는 능력을 시험하는 것이었다.

## 5. 마무리: 보안 대책
1.  **디렉토리 리스팅 비활성화**: Apache 설정(`httpd.conf` 또는 `.htaccess`)에서 `Options -Indexes`를 설정하여 파일 목록 노출을 차단해야 한다.
2.  **민감한 파일 격리**: 중요한 정보가 담긴 파일은 웹 루트(`DocumentRoot`) 외부나 접근 제어가 설정된 디렉토리에 저장해야 한다.
3.  **명명 규칙 준수**: 추측 가능한 파일 이름이나 민감한 단어(`password`, `admin` 등)가 포함된 파일명을 지양한다.

**FLAG**: `72eb9489d0edd3193ad94109eb58d672`

---

#### [Hacker's Diary] Steganography: 이미지 속에 숨겨진 1비트의 비밀 (LSB)

**난이도**: 🟢 Beginner
**예상 시간**: ⏱️ 30분
**주요 기술**: `#Steganography` `#LSB` `#Image-Analysis` `#Hidden-Data`
**관련 스크립트**: [solve_steganography.py](../Scripts/solve_steganography.py)

## 1. 개요: 평범한 강아지 사진 뒤의 진실
이번 문제는 이미지 파일 안에 데이터를 숨기는 스테가노그래피 기법을 다룬다. 눈으로 보기엔 아주 평범한 `dangdang.png` 강아지 사진이지만, 그 픽셀 하나하나에는 사람이 인지할 수 없는 미세한 정보가 새겨져 있다.

## 2. 취약점 분석: LSB (Least Significant Bit)
스테가노그래피의 가장 대표적인 기법은 **최하위 비트(LSB) 조작**이다.
*   이미지의 각 픽셀은 R(빨강), G(초록), B(파랑) 값을 가진다. (예: 255, 255, 255)
*   이 값들을 이진수로 변환했을 때, 가장 끝자리에 있는 1비트(LSB)는 값이 바뀌어도 색상 차이가 거의 나지 않는다.
*   공격자는 이 LSB 공간에 자신의 데이터를 0과 1로 나누어 심어놓는다.

## 3. 공격 실행: 숨겨진 메시지 추출

### 1단계: 대상 확보
웹 페이지 소스 코드 분석을 통해 `dangdang.png` 파일을 찾아내고 다운로드했다.
```bash
curl -O http://3.35.141.246/challenges/stegano/dangdang.png
```

### 2단계: 도구 활용 (Decoding)
제시된 웹 도구(`stylesuxx.github.io/steganography`)를 활용하여 이미지의 픽셀 데이터를 분석했다.
*   **작동 원리**: 도구는 이미지의 모든 픽셀을 돌며 각 색상 채널의 LSB를 추출한다. 추출된 0과 1의 조합을 8비트씩 묶어 다시 아스키(ASCII) 문자로 변환한다.

### 3단계: 은밀한 경로 발견
이미지를 업로드하고 디코딩을 수행한 결과, 일반적인 플래그 대신 서버 내부의 숨겨진 디렉토리 경로가 추출되었다.
*   **추출된 데이터**: `challenges/stegano/5ebe2294ecd0e0f08eab7690d2a6ee69/f1ag.php`

### 4단계: 최종 플래그 획득
추출된 경로를 서버 주소 뒤에 붙여 직접 접속을 시도했다.
*   **접속 주소**: `http://3.35.141.246/challenges/stegano/5ebe2294ecd0e0f08eab7690d2a6ee69/f1ag.php`
*   해당 페이지에서 최종적인 플래그를 확인할 수 있었다.

## 4. 결과: 이중 보안의 파쇄
공격자는 스테가노그래피를 단순히 데이터를 숨기는 용도가 아니라, 중요한 파일이 있는 위치(Hidden Path)를 숨기는 용도로 사용했다. 이는 일종의 '보안을 통한 은닉(Security by Obscurity)'이지만, LSB 분석을 통해 그 은신처가 드러나게 되었다.

## 5. 마무리: 보안 대책
스테가노그래피를 방어하는 가장 좋은 방법은 이미지를 재압축(Re-compression)하거나 변환(Filtering)하는 것이다. 이미지를 JPEG 등으로 다시 저장하면 미세한 LSB 값들이 뭉개지면서 숨겨진 메시지가 파괴되기 때문이다.

**FLAG**: `[Hidden in image LSB → Path discovered]`

---

### 🟡 Intermediate

#### [Hacker's Diary] Download I: 다운로더를 다운로드하라

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 40분
**주요 기술**: `#Path-Traversal` `#Directory-Traversal` `#Source-Code-Disclosure` `#LFI`
**관련 스크립트**: [solve_download1.py](../Scripts/solve_download1.py)

## 1. 개요
파일 다운로드 서비스의 취약점을 이용하여 서버 내부의 실행 파일(`down.cgi`) 소스 코드를 탈취하고 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 취약점 발견
*   `down.cgi` 페이지가 `file` 파라미터를 통해 파일을 읽어온다.
*   HTML 소스 상에서 `files/test.cgi`를 가리키는 것으로 보아, 실제 파일은 `files/` 디렉토리 내부에 위치할 가능성이 높다.

### 공격 가설
1.  **Path Traversal**: `../`를 사용하여 `files/` 디렉토리를 벗어나 상위 디렉토리의 `down.cgi` 소스 코드를 읽어올 수 있을 것이다.
2.  **소스 분석**: `down.cgi` 소스 코드 내에 플래그가 존재할 것이다.

### 2단계: down.cgi 소스 코드 분석
`?file=../down` 페이로드를 사용하여 `down.cgi`의 원본 소스 코드를 획득했다. 소스 분석 결과 다음의 중요한 정보를 발견했다.

1.  **자동 확장자 추가**: 서버는 입력값 뒤에 `.cgi`를 자동으로 붙여 `files/` 디렉토리에서 파일을 찾는다.
2.  **민감 파일 포함**: 코드 상단에 `@include "conf1g.cgi";` 구문이 존재하여 해당 파일에 중요한 정보가 있을 것으로 판단했다.

### 3단계: 플래그 획득
설정 파일인 `conf1g.cgi`를 읽기 위해 다음과 같은 요청을 보냈다.
*   **페이로드**: `?file=../conf1g`
*   **최종 실행**: `readfile("files/../conf1g.cgi");`

다운로드된 `conf1g.cgi` 파일의 주석 내에서 최종 플래그를 확인했다.

*   **최종 FLAG**: `f1leD0wn1o@d`

## 4. 결과: 경로 추적을 통한 실행 파일 및 설정 파일 노출
서버가 사용자의 입력값에서 경로 제어 문자(`../`)를 적절히 필터링하지 않아, 웹 루트 외부나 상위 디렉토리의 민감한 파일에 접근할 수 있었다. 특히 실행 파일의 소스 코드가 노출됨으로써 숨겨진 설정 파일의 이름까지 유출된 사례다.

## 5. 마무리: 보안 대책
1.  **파일명 정규화**: `basename()` 함수를 사용하여 경로를 제거하고 순수 파일명만 추출한다.
2.  **화이트리스트 검증**: 허용된 파일 목록(예: `test`, `sample`) 외의 입력은 차단한다.
3.  **파일 접근 권한 제한**: 웹 서버 프로세스가 소스 코드나 설정 파일(`.cgi`, `.config`)을 직접 읽을 수 없도록 권한을 최소화한다.

**FLAG**: `f1leD0wn1o@d`

---

#### [Hacker's Diary] Download II: 더 정교해진 다운로더

**난이도**: 🟡 Intermediate
**예상 시간**: ⏱️ 45분
**주요 기술**: `#Path-Traversal` `#str_replace-Bypass` `#Nested-Payload` `#Filter-Evasion`
**관련 스크립트**: [solve_download2.py](../Scripts/solve_download2.py)

## 1. 개요
강화된 파일 다운로드 필터링을 우회하여 서버 소스 코드를 확보하고 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 취약점 발견
*   `down.cgi?file=test`를 통해 `files/test.cgi`를 다운로드한다.
*   이전 문제의 필터링 로직(`preg_match("/php|html|down2/i",$file)`)을 고려할 때, 이번에는 `down` 관련 문자열에 대한 검증이 강화되었을 가능성이 높다.

### 공격 가설
1.  **Path Traversal**: 여전히 상위 디렉토리 이동이 가능할 것이다.
2.  **Filter Bypass**: 만약 `down` 문자열이 차단된다면, `str_replace`나 특정 필터링의 허점을 찾아 우회해야 한다.

### 2단계: 필터링 분석 및 우회 (str_replace)
기본적인 경로 추적 구문인 `../`를 입력했을 때 "File not found"가 발생하는 것을 확인했다. 이는 서버가 `../` 문자열을 단순히 삭제하고 있음을 의미한다. 이를 우회하기 위해 다음과 같은 중첩 페이로드를 사용했다.

*   **페이로드**: `....//`
*   **우회 원리**: `..` + `../` + `/` -> 중간의 `../` 제거 -> `../` 생성
*   **소스 코드 탈취**: `?file=....//down` 요청을 통해 `down.cgi`의 원본 소스를 확보했다.

### 3단계: 플래그 획득
탈취한 소스 코드 내에서 `@include "conf1g_p@ss.cgi";` 구문을 발견했다. 해당 파일에 플래그가 있을 것으로 판단하고 동일한 우회 기법을 적용했다.

*   **최종 요청**: `?file=....//conf1g_p@ss`
*   **파일 내용**: `// FLAG is fileDownload_p@ssw0rd`

*   **최종 FLAG**: `fileDownload_p@ssw0rd`

## 4. 결과: 불완전한 문자열 치환의 위험성
`Download I` 보다 강화된 필터링이 적용되었으나, 여전히 `str_replace`를 이용한 단순 삭제 방식을 사용하고 있었다. 이는 공격자가 필터링 대상 문자열을 조작하여 치환 후에 원하는 구문이 완성되도록 설계할 수 있는 치명적인 약점을 노출했다.

## 5. 마무리: 보안 대책
1.  **정규표현식을 이용한 재귀적 제거**: 단순히 한 번 치환하는 것이 아니라, 더 이상 해당 패턴이 발견되지 않을 때까지 반복적으로 제거해야 한다. (하지만 이 역시 성능 저하의 원인이 될 수 있다.)
2.  **basename() 함수 강제**: PHP의 `basename()` 함수는 경로 정보를 완전히 제거하고 순수 파일명만 남기므로, Path Traversal 공격을 가장 효과적으로 방어할 수 있다.
3.  **파일 화이트리스트 관리**: 다운로드 가능한 파일의 명단을 서버에서 관리하고, 사용자의 입력값이 명단에 있는 경우에만 파일을 제공한다.

**FLAG**: `fileDownload_p@ssw0rd`

---

### 🔴 Advanced

#### [Hacker's Diary] Upload II: 보안 설정을 무력화하는 방법

**난이도**: 🔴 Advanced
**예상 시간**: ⏱️ 60분
**주요 기술**: `#File-Upload` `#htaccess-Injection` `#Configuration-Override` `#Apache-Exploit`
**관련 스크립트**: [solve_upload2.py](../Scripts/solve_upload2.py)

## 1. 개요
파일 업로드 취약점을 방어하기 위한 서버 설정을 `.htaccess` 파일을 통해 덮어씌워 무력화하고, 웹쉘을 실행하여 플래그를 획득하는 문제다.

## 2. 취약점 분석 및 가설 수립

### 취약점 발견
*   파일 업로드 기능이 존재하며, 개별 사용자 디렉토리에 파일이 저장된다.
*   힌트 "차단을 차단한다"는 서버 측의 실행 제한 설정을 조작해야 함을 의미한다.

### 공격 가설
1.  **htaccess Overwrite**: Apache 서버에서 `.htaccess` 파일을 업로드할 수 있다면, 해당 디렉토리의 PHP 실행 권한이나 필터링 설정을 변경할 수 있다.
2.  **Engine On/Extension Add**: 꺼져 있는 PHP 엔진을 켜거나(`php_flag engine on`), 다른 확장자를 PHP로 처리하도록(`AddType`) 설정한다.

### 2단계: .htaccess 업로드를 통한 설정 무력화
업로드 디렉토리(`uploads/{md5}/`)에 이미 존재하는 `index.php` 파일의 소스 코드를 읽기 위해, 서버 설정을 덮어쓰는 `.htaccess` 파일을 업로드했다.

*   **업로드 내용**: `php_flag engine off`
*   **작동 원리**: 해당 디렉토리 내에서 PHP 엔진의 가동을 중지시켜, `.php` 확장자 파일을 실행하지 않고 텍스트 파일처럼 원본 내용을 출력하도록 유도했다.

### 3단계: 소스 코드 분석 및 플래그 획득
설정 변경 후 `uploads/{md5}/index.php`에 다시 접근한 결과, 실행 결과(`READ ME`)가 아닌 원본 소스 코드가 노출되었다.

```php
<?php
    // FLAG is engine_0ff!!!
    echo("READ ME");
?>
```

*   **최종 FLAG**: `engine_0ff!!!`

## 4. 결과: 분산 설정 파일(.htaccess) 조작 취약점
웹 서버가 사용자 업로드 디렉토리에서 `.htaccess`와 같은 설정 파일을 허용할 경우, 공격자는 서버의 보안 정책을 임의로 변경할 수 있다. 이번 사례에서는 PHP 실행 차단 설정을 무력화하여 서버 사이드 스크립트의 원본을 탈취하는 데 성공했다.

## 5. 마무리: 보안 대책
1.  **설정 파일 업로드 금지**: 사용자가 업로드하는 파일 이름 중 `.htaccess`, `web.config` 등 서버 설정과 관련된 파일은 엄격히 차단해야 한다.
2.  **AllowOverride 제어**: Apache 설정에서 업로드 디렉토리에 대해 `AllowOverride None`을 설정하여 `.htaccess` 파일이 무시되도록 강제한다.
3.  **실행 권한 분리**: 업로드 디렉토리는 전용 스토리지 서버나 실행 권한이 완전히 박멸된 환경에서 관리해야 한다.

**FLAG**: `engine_0ff!!!`

---

## 핵심 개념 정리

### 1. Path Traversal (Directory Traversal)

파일 경로를 조작하여 웹 루트 외부의 파일에 접근하는 취약점.

#### 기본 개념:

```
정상 경로:
/var/www/html/files/test.txt

공격 경로:
/var/www/html/files/../../../etc/passwd
→ /etc/passwd
```

#### 주요 페이로드:

```bash
# 기본
../../../etc/passwd

# URL 인코딩
..%2F..%2F..%2Fetc%2Fpasswd

# 이중 인코딩
..%252F..%252F..%252Fetc%252Fpasswd

# 16비트 유니코드
..%c0%af..%c0%af..%c0%afetc%c0%afpasswd

# 유닉스
....//....//....//etc/passwd

# Windows
..\..\..\windows\system32\config\sam
```

#### 필터 우회 기법:

```php
// 서버 필터링 예시
$file = str_replace("../", "", $input);

// 우회 페이로드
....//    → str_replace → ../
..././    → str_replace → ../
...//     → str_replace → ../
```

### 2. 디렉토리 리스팅 (Directory Listing)

웹 서버가 디렉토리 내 파일 목록을 자동으로 표시하는 기능.

#### Apache 설정:

```apache
# 취약한 설정
<Directory /var/www/html>
    Options Indexes FollowSymLinks
</Directory>

# 안전한 설정
<Directory /var/www/html>
    Options -Indexes +FollowSymLinks
</Directory>
```

#### .htaccess 설정:

```apache
# 디렉토리 리스팅 비활성화
Options -Indexes

# 특정 파일 접근 차단
<FilesMatch "\.(htaccess|htpasswd|ini|log|sh|sql)$">
    Require all denied
</FilesMatch>
```

### 3. 스테가노그래피 (Steganography)

데이터를 다른 파일(주로 이미지) 안에 숨기는 기법.

#### LSB (Least Significant Bit) 방식:

```python
# 데이터 숨기기 (Encoding)
def encode_lsb(image, message):
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    pixel_index = 0

    for bit in binary_message:
        # RGB 값의 마지막 비트를 메시지 비트로 교체
        pixel = list(image.getpixel(pixel_index))
        pixel[0] = (pixel[0] & 0xFE) | int(bit)
        image.putpixel(pixel_index, tuple(pixel))
        pixel_index += 1

# 데이터 추출 (Decoding)
def decode_lsb(image, message_length):
    binary_message = ''

    for i in range(message_length * 8):
        pixel = image.getpixel(i)
        # RGB 값의 마지막 비트 추출
        binary_message += str(pixel[0] & 1)

    # 8비트씩 묶어서 문자로 변환
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))

    return message
```

#### 분석 도구:

```bash
# binwalk - 파일 내부 숨겨진 데이터 탐색
binwalk -e image.png

# steghide - 스테가노그래피 추출
steghide extract -sf image.jpg

# strings - 문자열 추출
strings image.png | grep -i flag

# exiftool - 메타데이터 분석
exiftool image.png
```

### 4. .htaccess 파일 조작

Apache 서버의 디렉토리별 설정 파일을 조작하여 보안 정책 우회.

#### 주요 지시어:

```apache
# PHP 엔진 비활성화 (소스 코드 노출)
php_flag engine off

# PHP 엔진 활성화
php_flag engine on

# 확장자 추가 (이미지를 PHP로 실행)
AddType application/x-httpd-php .jpg .png .gif

# 파일 업로드 크기 제한 무력화
php_value upload_max_filesize 100M
php_value post_max_size 100M

# 에러 표시 활성화 (정보 유출)
php_flag display_errors on
php_flag display_startup_errors on
```

### 5. 파일 업로드 취약점

사용자가 업로드한 파일을 서버에서 실행할 수 있을 때 발생.

#### 공격 시나리오:

```
1. 확장자 검증 우회
   shell.php → shell.php.jpg
   shell.php → shell.pHp
   shell.php → shell.php%00.jpg (Null Byte)

2. MIME Type 조작
   Content-Type: image/jpeg
   (실제 내용은 PHP 웹쉘)

3. .htaccess 업로드
   AddType application/x-httpd-php .jpg
   → 이후 이미지 파일이 PHP로 실행됨

4. Double Extension
   shell.jpg.php
   (서버가 .jpg까지만 검증)

5. Case Sensitivity
   shell.PhP
   shell.pHp
```

---

## 방어 기법

### 1. Path Traversal 방어

```php
// ❌ 취약한 코드
$file = $_GET['file'];
include("uploads/" . $file);

// ✅ 방법 1: basename() 사용
$file = basename($_GET['file']);
include("uploads/" . $file);

// ✅ 방법 2: 화이트리스트
$allowed = ['report.pdf', 'manual.pdf', 'guide.pdf'];
$file = $_GET['file'];
if(!in_array($file, $allowed)) {
    die("File not allowed");
}
include("uploads/" . $file);

// ✅ 방법 3: realpath() 검증
$base = realpath("/var/www/uploads/");
$requested = realpath($base . "/" . $_GET['file']);

if(strpos($requested, $base) !== 0) {
    die("Path traversal detected");
}
include($requested);

// ✅ 방법 4: 정규표현식 검증
if(preg_match('/\.\./', $_GET['file'])) {
    die("Invalid characters detected");
}
```

### 2. 디렉토리 리스팅 방어

```apache
# Apache 설정 (httpd.conf)
<Directory "/var/www/html">
    Options -Indexes +FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

# .htaccess 파일
Options -Indexes

# 민감한 파일 보호
<FilesMatch "^\.">
    Require all denied
</FilesMatch>
```

```nginx
# Nginx 설정
location / {
    autoindex off;
}

# 숨김 파일 접근 차단
location ~ /\. {
    deny all;
}
```

### 3. 파일 업로드 보안

```php
// ✅ 완전한 파일 업로드 검증
function secure_upload($file) {
    // 1. 확장자 화이트리스트
    $allowed_ext = ['jpg', 'jpeg', 'png', 'gif', 'pdf'];
    $ext = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));

    if(!in_array($ext, $allowed_ext)) {
        die("Invalid file type");
    }

    // 2. MIME Type 검증
    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $mime = finfo_file($finfo, $file['tmp_name']);
    $allowed_mime = [
        'image/jpeg',
        'image/png',
        'image/gif',
        'application/pdf'
    ];

    if(!in_array($mime, $allowed_mime)) {
        die("Invalid MIME type");
    }

    // 3. 파일 크기 제한
    if($file['size'] > 5 * 1024 * 1024) { // 5MB
        die("File too large");
    }

    // 4. 랜덤 파일명 생성
    $new_name = bin2hex(random_bytes(16)) . '.' . $ext;

    // 5. 웹 루트 외부 저장
    $upload_dir = '/var/uploads/';  // DocumentRoot 밖
    $destination = $upload_dir . $new_name;

    // 6. 실행 권한 제거
    if(move_uploaded_file($file['tmp_name'], $destination)) {
        chmod($destination, 0644);  // 실행 권한 제거
        return $new_name;
    }

    return false;
}

// 이미지 재처리 (스테가노그래피 방어)
function reprocess_image($file) {
    $img = imagecreatefromjpeg($file);
    imagejpeg($img, $file, 85);  // 재압축
    imagedestroy($img);
}
```

### 4. .htaccess 업로드 방어

```php
// 파일명 검증
$forbidden_files = [
    '.htaccess',
    '.htpasswd',
    'web.config',
    '.user.ini',
    'php.ini'
];

$filename = basename($_FILES['file']['name']);
foreach($forbidden_files as $forbidden) {
    if(stripos($filename, $forbidden) !== false) {
        die("Configuration files not allowed");
    }
}
```

```apache
# Apache 설정으로 .htaccess 무력화
<Directory "/var/www/uploads">
    AllowOverride None
    Options -Indexes -ExecCGI
    AddHandler cgi-script .php .pl .py .jsp .asp
    <FilesMatch "\.php$">
        SetHandler none
    </FilesMatch>
</Directory>
```

### 5. 파일 다운로드 보안

```php
// ✅ 안전한 파일 다운로드
function secure_download($file_id) {
    // 1. 데이터베이스에서 파일 정보 조회
    $stmt = $pdo->prepare(
        "SELECT filename, filepath FROM files
         WHERE id = ? AND user_id = ?"
    );
    $stmt->execute([$file_id, $_SESSION['user_id']]);
    $file = $stmt->fetch();

    if(!$file) {
        http_response_code(404);
        die("File not found");
    }

    // 2. 실제 파일 존재 확인
    $full_path = '/var/uploads/' . $file['filepath'];
    if(!file_exists($full_path)) {
        die("File not found on disk");
    }

    // 3. 안전한 다운로드 헤더
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="' .
           basename($file['filename']) . '"');
    header('Content-Length: ' . filesize($full_path));
    header('X-Content-Type-Options: nosniff');

    // 4. readfile()로 안전하게 출력
    readfile($full_path);
    exit;
}
```

### 6. 스테가노그래피 방어

```python
# 이미지 재압축으로 LSB 데이터 파괴
from PIL import Image

def sanitize_image(input_path, output_path):
    img = Image.open(input_path)

    # JPEG 재압축 (LSB 파괴)
    if img.format in ['PNG', 'BMP']:
        img = img.convert('RGB')
        img.save(output_path, 'JPEG', quality=85)
    else:
        img.save(output_path, 'JPEG', quality=85)
```

---

## 참고 자료

### OWASP 가이드

- **OWASP Top 10 2021**: [A01:2021 – Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
- **Path Traversal**: [OWASP](https://owasp.org/www-community/attacks/Path_Traversal)
- **File Upload Cheat Sheet**: [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

### PortSwigger Academy

- **File path traversal**: [Web Security Academy](https://portswigger.net/web-security/file-path-traversal)
- **File upload vulnerabilities**: [Web Security Academy](https://portswigger.net/web-security/file-upload)

### 도구 및 리소스

- **Steganography Tools**:
  - [stylesuxx.github.io/steganography](https://stylesuxx.github.io/steganography/) - 온라인 LSB 도구
  - [stegsolve](http://www.caesum.com/handbook/Stegsolve.jar) - 이미지 분석
  - [binwalk](https://github.com/ReFirmLabs/binwalk) - 파일 내 숨겨진 데이터 탐색
  - [steghide](http://steghide.sourceforge.net/) - 스테가노그래피 추출

- **Path Traversal 테스트**:
  - [DotDotPwn](https://github.com/wireghoul/dotdotpwn) - 자동화 도구
  - Burp Suite - Manual testing

### Apache 보안 가이드

- **Apache Security Tips**: [Documentation](https://httpd.apache.org/docs/2.4/misc/security_tips.html)
- **.htaccess Tutorial**: [Apache](https://httpd.apache.org/docs/2.4/howto/htaccess.html)

---

**문제 수**: 5개
**난이도 분포**: 🟢 Beginner 2개 | 🟡 Intermediate 2개 | 🔴 Advanced 1개
**총 학습 시간**: 약 3시간 10분

**마지막 업데이트**: 2026-01-14
**버전**: 1.0
