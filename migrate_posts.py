import os
import re
import shutil
from datetime import datetime

# 제외할 시스템 디렉토리
IGNORE_DIRS = {
    '_posts', '_site', '_includes', '_layouts', '_data', 
    '.git', '.github', '.obsidian', '.gemini', 'assets',
    '.claude', 'study', 'vendor'
}

TARGET_DIR = '_posts'
DEFAULT_YEAR = '2024'

# SK_Rookies 전용 매핑
SK_ROOKIES_MAP = {
    '01_python': 'Python',
    '02_linux-network': 'Linux-Network',
    '03_cloud-aws': 'AWS-Cloud',
    '04_application-security': 'App-Security',
    '05_privacy-security': 'Privacy-Security',
    '06_consulting-governance': 'Consulting-Governance',
    '97_mini_pjt_1': 'Project-AI',
    '98_mini_pjt_2': 'Project-Security'
}

def get_category(root_dir, parent_dir):
    """경로 기반 카테고리 결정"""
    parts = root_dir.split(os.sep)
    top_folder = next((p for p in parts if p and p != '.'), None)

    if top_folder == 'SK_Rookies':
        return SK_ROOKIES_MAP.get(parent_dir, 'SK_Rookies')
    
    if top_folder:
        return top_folder.replace(' ', '-')
        
    return 'Study'

def clean_filename(filename):
    name = os.path.splitext(filename)[0]
    name = re.sub(r'^[0-9]+[):]\s*', '', name)
    name = re.sub(r'[()\[\]]', '', name)
    name = re.sub(r'\s+', '-', name)
    name = re.sub(r'[^\w\-\u3131-\u3163\uac00-\ud7a3]', '', name)
    return name

def extract_front_matter(content):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1], parts[2] 
    return None, content

def extract_value_from_fm(fm, key):
    match = re.search(f'^{key}:\s*"(.*)"', fm, re.MULTILINE) or \
            re.search(f'^{key}:\s*(.*)', fm, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def extract_date_smart(content, filename):
    # 1. Front Matter가 있으면 거기서 날짜 추출 (가장 우선)
    fm, _ = extract_front_matter(content)
    if fm:
        date_val = extract_value_from_fm(fm, 'date')
        if date_val:
            return date_val

    # 2. 본문 내용에서 날짜 추출 (강력한 정규식)
    # Front Matter 영역 제외
    parts = content.split('---', 2)
    body = parts[2] if len(parts) >= 3 else content
    
    body_head = '\n'.join(body.split('\n')[:50]) # 상단 50줄
    
    patterns = [
        r'(?:강의\s*일자|강의\s*날짜|작성일|날짜|일시|강의일).*?(\d{4})[-년.]\s*(\d{1,2})[-월.]\s*(\d{1,2})',
        r'(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일',
        r'(\d{4})-(\d{1,2})-(\d{1,2})', # YYYY-MM-DD
        r'(\d{4})\.(\d{1,2})\.(\d{1,2})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, body_head)
        if match:
            try:
                y, m, d = match.groups()
                if 2023 <= int(y) <= 2026: # 유효 범위 체크
                    return f"{y}-{m.zfill(2)}-{d.zfill(2)}"
            except: continue

    # 3. 파일명에서 날짜 추출
    match = re.search(r'(202[0-9])([01][0-9])([0-3][0-9])', filename)
    if match: return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    
    match = re.search(r'([01]?[0-9])-([0-3][0-9])', filename)
    if match: return f"{DEFAULT_YEAR}-{match.group(1).zfill(2)}-{match.group(2).zfill(2)}"

    # 4. 최후의 수단: 오늘 날짜
    return datetime.now().strftime('%Y-%m-%d')

def process_files():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    # 기존 포스트 삭제
    for f in os.listdir(TARGET_DIR):
        os.remove(os.path.join(TARGET_DIR, f))

    for top_dir in os.listdir('.'):
        if top_dir in IGNORE_DIRS or top_dir.startswith('.') or os.path.isfile(top_dir):
            continue
            
        print(f"📂 Scanning directory: {top_dir}")

        for root, dirs, files in os.walk(top_dir):
            for file in files:
                if not file.endswith('.md'):
                    continue
                
                source_path = os.path.join(root, file)
                parent_dir = os.path.basename(root)
                category = get_category(root, parent_dir)
                
                with open(source_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 스마트 날짜 추출
                date_str = extract_date_smart(content, file)
                
                # Front Matter & Body 분리
                fm_str, body = extract_front_matter(content)
                
                # 제목 추출
                title = None
                excerpt = None
                
                if fm_str:
                    title = extract_value_from_fm(fm_str, 'title')
                    excerpt = extract_value_from_fm(fm_str, 'excerpt')
                
                if not title:
                    title = clean_filename(file) # TODO: 본문 H1 추출 로직 추가하면 좋음
                if not excerpt:
                    excerpt = ""

                safe_slug = clean_filename(file)
                
                # 파일명 결정 (날짜-제목.md)
                if re.match(r'\d{4}-\d{2}-\d{2}', str(date_str)):
                    new_filename = f"{date_str}-{safe_slug}.md"
                else:
                    new_filename = f"{DEFAULT_YEAR}-01-01-{safe_slug}.md"

                target_path = os.path.join(TARGET_DIR, new_filename)
                
                # Liquid 태그 처리
                body = body.replace('{{', '&#123;&#123;').replace('}}', '&#125;&#125;')
                body = body.replace('{%', '&#123;%').replace('%}', '%&#125;')

                tags = [category]
                if 'SK_Rookies' in root:
                    tags.append('SK_Rookies')

                front_matter = f"""---
title: "{title}"
date: {date_str}
excerpt: "{excerpt}"
categories:
  - {category}
tags:
{chr(10).join([f'  - {tag}' for tag in tags])}
---

"""
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(front_matter + body.lstrip())
                
                print(f"  -> {new_filename}")

if __name__ == "__main__":
    process_files()
