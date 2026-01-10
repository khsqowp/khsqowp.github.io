# 📘 프로젝트 인수인계 자료 (2026-01-09)

## 1. 프로젝트 개요
- **목표:** 보안 및 개발 학습 로그(SK Rookies)를 위한 포트폴리오 겸 기술 블로그 운영.
- **기반 기술:** Jekyll (Ruby 기반 정적 사이트 생성기).
- **테마:** [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) (Remote Theme 방식).
- **호스팅:** GitHub Pages (`https://khsqowp.github.io`).

## 2. 핵심 디렉토리 구조
```text
.
├── SK_Rookies/          # [원본] 사용자가 작성한 마크다운 노트 (강의 자료 등)
├── _posts/              # [생성] Jekyll이 빌드할 실제 포스트 파일들 (스크립트로 자동 생성됨)
├── _config.yml          # [설정] 사이트 제목, 저자, 테마, 플러그인 설정
├── Gemfile              # [설정] Jekyll 및 플러그인 의존성 목록
├── categories.md        # [페이지] 카테고리 아카이브 (폴더 트리 구조 디자인 적용)
├── tags.md              # [페이지] 태그 아카이브 (태그 아이콘 디자인 적용)
├── index.md             # [페이지] 메인 홈페이지 (최근 글 목록 포함)
├── migrate_posts.py     # [도구] SK_Rookies -> _posts 변환 스크립트
├── update_dates.py      # [도구] 파일 내용에서 '강의 날짜' 추출 및 적용 스크립트
└── fix_liquid_syntax.py # [도구] Jekyll Liquid 문법 충돌 방지 스크립트
```

## 3. 운영 및 관리 가이드

### 3.1. 글 작성 프로세스
1. `SK_Rookies` 폴더 내 적절한 위치에 마크다운 파일(`.md`)을 작성하거나 추가합니다.
2. 파일명은 자유롭게 작성해도 됩니다 (스크립트가 알아서 정리함).
3. 파일 상단에 `날짜: 2024년 10월 23일` 형식으로 날짜를 적어두면 자동으로 인식합니다.

### 3.2. 배포 프로세스 (자동화)
새로운 글을 추가하거나 수정했다면, 다음 명령어를 순서대로 실행하여 반영합니다.

```bash
# 1. _posts 폴더 초기화 (삭제된 파일 반영을 위해)
rm -rf _posts/*

# 2. 원본 데이터 변환 및 복사
python3 migrate_posts.py

# 3. 날짜 추출 및 메타데이터 업데이트
python3 update_dates.py

# 4. Jekyll 빌드 에러 방지 (Liquid 태그 이스케이프)
python3 fix_liquid_syntax.py

# 5. GitHub 배포
git add .
git commit -m "Update: New posts"
git push
```

### 3.3. 주요 이슈 및 해결법
- **404 오류:** `_config.yml`의 `permalink` 설정 확인. 현재는 폴더 방식이 아닌 간소화된 방식 사용 중.
- **빌드 에러:** GitHub Actions 탭 확인. 주로 `Gemfile`에 플러그인이 누락되었거나, 마크다운 내 `{{ }}` 같은 특수문자 때문에 발생함 (`fix_liquid_syntax.py`로 해결).

## 4. 커스터마이징 내역
- **Categories/Tags:** 기본 테마 레이아웃 대신, 직접 HTML/Liquid를 작성하여 폴더 트리 구조처럼 보이도록 `categories.md`와 `tags.md`를 수정함.
- **Navigation:** `_data/navigation.yml`에서 상단 메뉴 관리 (Study Notes, Portfolio, CV).
- **Date Handling:** 파일명에 날짜가 없어도, 본문 상단 20줄을 읽어 날짜를 추출하는 로직 구현 (`update_dates.py`).

---
**주의:** `_posts` 폴더의 파일은 직접 수정하지 마세요. `SK_Rookies` 원본을 수정한 후 스크립트를 돌려야 관리하기 편합니다.
