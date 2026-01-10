import os
import re
import shutil
from datetime import datetime

# 소스 디렉토리와 타겟 디렉토리
SOURCE_DIR = 'SK_Rookies'
TARGET_DIR = '_posts'
DEFAULT_YEAR = '2024'

# 디렉토리 매핑 (카테고리 태그로 사용)
CATEGORY_MAP = {
    '01_python': 'Python',
    '02_linux-network': 'Linux-Network',
    '03_cloud-aws': 'AWS-Cloud',
    '04_application-security': 'App-Security',
    '05_privacy-security': 'Privacy-Security',
    '06_consulting-governance': 'Consulting-Governance',
    '97_mini_pjt_1': 'Project-AI',
    '98_mini_pjt_2': 'Project-Security'
}

def clean_filename(filename):
    """파일명을 URL 슬러그용으로 정리"""
    name = os.path.splitext(filename)[0]
    # 순서 번호 제거 (예: "01) ") - 정규식 안전하게 수정
    name = re.sub(r'^[0-9]+[):]\s*', '', name)
    name = re.sub(r'[()\[\]]', '', name)
    name = re.sub(r'\s+', '-', name)
    name = re.sub(r'[^\w\-\u3131-\u3163\uac00-\ud7a3]', '', name)
    return name

def extract_date(content, filename):
    """내용 또는 파일명에서 날짜 추출"""
    lines = content.split('\n')[:30]
    date_patterns = [
        r'(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일',
        r'(\d{4})-(\d{1,2})-(\d{1,2})',
        r'(\d{4})\.(\d{1,2})\.(\d{1,2})'
    ]
    for line in lines:
        for pattern in date_patterns:
            match = re.search(pattern, line)
            if match:
                return f"{match.group(1)}-{match.group(2).zfill(2)}-{match.group(3).zfill(2)}"

    match = re.search(r'(202[0-9])([01][0-9])([0-3][0-9])', filename)
    if match: return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    
    match = re.search(r'([01]?[0-9])-([0-3][0-9])', filename)
    if match: return f"{DEFAULT_YEAR}-{match.group(1).zfill(2)}-{match.group(2).zfill(2)}"

    return datetime.now().strftime('%Y-%m-%d')

def extract_title(content, filename):
    """내용에서 H1 제목 추출"""
    lines = content.split('\n')[:20]
    for line in lines:
        if line.lstrip().startswith('# '):
            title = line.strip().lstrip('#').strip()
            # 특수문자 중 제목에 쓰면 안되는 것들은 제거하거나 이스케이프
            title = title.replace('"', "'") 
            return title
            
    return clean_filename(filename).replace('-', ' ')

def process_files():
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)
    os.makedirs(TARGET_DIR)

    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if not file.endswith('.md'):
                continue
            
            source_path = os.path.join(root, file)
            parent_dir = os.path.basename(root)
            category = CATEGORY_MAP.get(parent_dir, 'Study')
            
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            date_str = extract_date(content, file)
            real_title = extract_title(content, file)
            
            safe_slug = clean_filename(file)
            new_filename = f"{date_str}-{safe_slug}.md"
            target_path = os.path.join(TARGET_DIR, new_filename)
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    body = parts[2]
                else:
                    body = content
            else:
                body = content
                
            body = body.replace('{{', '&#123;&#123;').replace('}}', '&#125;&#125;')
            body = body.replace('{%', '&#123;%').replace('%}', '%&#125;')

            front_matter = f"""
--- 
title: "{real_title}"
date: {date_str}
categories:
  - {category}
tags:
  - {category}
  - SK_Rookies
---

"""
            final_content = front_matter + body.lstrip()

            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
                
            print(f"[{category}] {date_str} : {real_title}")

if __name__ == "__main__":
    process_files()
