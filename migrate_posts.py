import os
import re
import shutil
from datetime import datetime

SOURCE_DIR = 'SK_Rookies'
TARGET_DIR = '_posts'
DEFAULT_YEAR = '2024'

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
    name = os.path.splitext(filename)[0]
    name = re.sub(r'^[0-9]+[):]\s*', '', name)
    name = re.sub(r'[()\[\]]', '', name)
    name = re.sub(r'\s+', '-', name)
    name = re.sub(r'[^\w\-\u3131-\u3163\uac00-\ud7a3]', '', name)
    return name

def extract_date(content, filename):
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
    lines = content.split('\n')[:20]
    for line in lines:
        if line.lstrip().startswith('# '):
            title = line.strip().lstrip('#').strip()
            title = title.replace('"', "'") 
            return title
    return clean_filename(filename).replace('-', ' ')

def extract_excerpt(content):
    """본문에서 요약문(excerpt) 추출"""
    lines = content.split('\n')
    excerpt = ""
    
    for line in lines[:20]:
        if line.strip().startswith('>'):
            clean_line = line.strip().lstrip('>').strip()
            if '주제' in clean_line or '목표' in clean_line or '내용' in clean_line:
                excerpt = clean_line
                break
            if len(clean_line) > 20 and ':' not in clean_line:
                 excerpt = clean_line
                 break

    if not excerpt:
        for line in lines[:30]:
            clean_line = line.strip()
            if not clean_line or clean_line.startswith('#') or clean_line.startswith('---') or clean_line.startswith('>'):
                continue
            if clean_line.startswith('!') or clean_line.startswith('['):
                continue
            
            excerpt = clean_line
            break
    
    if excerpt:
        excerpt = re.sub(r'\*\*|__', '', excerpt)
        excerpt = excerpt.replace('"', "'")
        if len(excerpt) > 150:
            excerpt = excerpt[:147] + "..."
            
    return excerpt

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
            excerpt = extract_excerpt(content) 
            
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
excerpt: "{excerpt}"
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