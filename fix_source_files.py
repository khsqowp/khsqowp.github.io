import os
import re

SOURCE_DIR = 'SK_Rookies'

def clean_filename(filename):
    name = os.path.splitext(filename)[0]
    name = re.sub(r'^[0-9]+[):]\s*', '', name)
    name = re.sub(r'[\[\]\(\)]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

def extract_metadata(content, filename):
    lines = content.split('\n')
    
    # 1. 제목 추출 (첫 번째 # )
    title = None
    for line in lines[:20]:
        if line.strip().startswith('# '):
            title = line.strip().lstrip('#').strip().replace('"', "'")
            break
    if not title:
        title = clean_filename(filename)

    # 2. 날짜 추출
    date_str = None
    # 본문 우선 검색
    date_patterns = [
        r'(?:강의\s*일자|강의\s*날짜|작성일|날짜|일시|강의일).*?(\d{4})[-년.]\s*(\d{1,2})[-월.]\s*(\d{1,2})',
        r'(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일',
        r'(\d{4})-(\d{1,2})-(\d{1,2})'
    ]
    for line in lines[:50]:
        for pattern in date_patterns:
            match = re.search(pattern, line)
            if match:
                try:
                    y, m, d = match.groups()
                    if 2023 <= int(y) <= 2026:
                        date_str = f"{y}-{m.zfill(2)}-{d.zfill(2)}"
                        break
                except: continue
        if date_str: break
    
    # 본문에 없으면 파일명에서 검색 (파일명에 날짜가 있는 경우)
    if not date_str:
        match = re.search(r'(202[0-9])[-_.]?([01][0-9])[-_.]?([0-3][0-9])', filename)
        if match:
            date_str = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    
    # 그래도 없으면 기본값 (나중에 수동 수정 필요할 수 있음)
    if not date_str:
        date_str = "2025-01-01" # 임시 기본값

    # 3. 요약문 추출
    excerpt = ""
    for line in lines[:30]:
        clean_line = line.strip()
        # 제외 패턴
        if not clean_line or clean_line.startswith('#') or clean_line.startswith('---') or clean_line.startswith('!'):
            continue
        if clean_line.startswith('>') or clean_line.startswith('**'):
             # "날짜:", "강의:" 등으로 시작하면 건너뜀
             if any(x in clean_line for x in ['날짜', '일자', '강의명', '작성일', '주제']):
                 continue
        
        # 적당한 길이의 텍스트 발견
        excerpt = clean_line.lstrip('>').strip().replace('"', "'")
        excerpt = re.sub(r'\*\*|__', '', excerpt) # 볼드체 제거
        if len(excerpt) > 10:
            break
            
    if len(excerpt) > 150:
        excerpt = excerpt[:147] + "..."

    return title, date_str, excerpt

def fix_sources():
    count = 0
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if not file.endswith('.md'):
                continue
            
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 기존 Front Matter 분리 (있다면 제거하고 새로 만듦)
            body = content
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    body = parts[2]
            
            # 메타데이터 추출
            title, date_str, excerpt = extract_metadata(body, file)
            
            # Front Matter 생성
            # 카테고리는 폴더명 기준이나 migrate_posts.py에서 처리하므로 여기선 생략해도 되지만
            # 원본 파일 자체에 정보를 심는 것이 목표이므로 넣지 않음 (migrate_posts.py가 처리하게 둠)
            # -> 아니다, migrate_posts.py가 "원본에 FM 있으면 그거 쓴다"고 했으니, 여기서 다 넣어줘야 함.
            
            # 카테고리 결정 (SK_Rookies 내부 폴더명 매핑)
            parent_dir = os.path.basename(root)
            category_map = {
                '01_python': 'Python',
                '02_linux-network': 'Linux-Network',
                '03_cloud-aws': 'AWS-Cloud',
                '04_application-security': 'App-Security',
                '05_privacy-security': 'Privacy-Security',
                '06_consulting-governance': 'Consulting-Governance',
                '97_mini_pjt_1': 'Project-AI',
                '98_mini_pjt_2': 'Project-Security',
                '00_안내사항': 'SK_Rookies' # 매핑 안된 경우 대비
            }
            # 한글 폴더명 처리가 어려울 수 있으니 contains로 대충 매핑
            category = 'Study'
            for k, v in category_map.items():
                if k in parent_dir: # 부분 일치라도
                    category = v
                    break
            
            tags = [category, 'SK_Rookies']
            
            new_fm = f"""---
title: "{title}"
date: {date_str}
excerpt: "{excerpt}"
categories:
  - {category}
tags:
{chr(10).join([f'  - {tag}' for tag in tags])}
---

"""

            # 파일 덮어쓰기
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_fm + body.lstrip())
            
            print(f"Fixed source: {file} -> {date_str} / {title}")
            count += 1

    print(f"Total fixed files: {count}")

if __name__ == "__main__":
    fix_sources()
