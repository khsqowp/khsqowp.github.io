import os
import re
import shutil
from datetime import datetime

# 소스 디렉토리와 타겟 디렉토리
SOURCE_DIR = 'SK_Rookies'
TARGET_DIR = '_posts'
DEFAULT_YEAR = '2024' # 파일명에 연도가 없으면 사용할 기본 연도

# 디렉토리 매핑 (카테고리 태그로 사용)
CATEGORY_MAP = {
    '01_python': 'Python',
    '02_linux-network': 'Linux-Network',
    '03_cloud-aws': 'AWS-Cloud',
    '04_application-security': 'App-Security',
    '98_mini_pjt_2': 'Project'
}

def clean_filename(filename):
    # 확장자 제거
    name = os.path.splitext(filename)[0]
    # 특수문자 및 불필요한 접두어 제거
    name = re.sub(r'^[0-9]+[\)\:]\s*', '', name) # "01) " 제거
    name = re.sub(r'[\(\)\[\]]', '', name) # 괄호 제거
    name = re.sub(r'\s+', '-', name) # 공백을 하이픈으로
    name = re.sub(r'[^\w\-\u3131-\u3163\uac00-\ud7a3]', '', name) # 한글, 영문, 숫자, 하이픈 외 제거
    return name

def extract_date(filename):
    # 다양한 날짜 패턴 찾기
    
    # 1. 20251203 형식
    match = re.search(r'(202[0-9])([01][0-9])([0-3][0-9])', filename)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    
    # 2. 10-23 형식 (월-일) -> 기본 연도 붙임
    match = re.search(r'([01]?[0-9])-([0-3][0-9])', filename)
    if match:
        return f"{DEFAULT_YEAR}-{match.group(1).zfill(2)}-{match.group(2).zfill(2)}"
        
    # 3. 12:03 형식 (월:일) -> 가끔 날짜를 이렇게 쓰기도 함
    match = re.search(r'([01]?[0-9]):([0-3][0-9])', filename)
    if match:
        return f"{DEFAULT_YEAR}-{match.group(1).zfill(2)}-{match.group(2).zfill(2)}"

    return datetime.now().strftime('%Y-%m-%d')

def process_files():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if not file.endswith('.md'):
                continue
            
            source_path = os.path.join(root, file)
            
            # 카테고리 결정
            parent_dir = os.path.basename(root)
            category = CATEGORY_MAP.get(parent_dir, 'Study')
            
            # 메타데이터 추출
            date_str = extract_date(file)
            clean_title = clean_filename(file)
            
            # Jekyll용 파일명 생성 (YYYY-MM-DD-title.md)
            new_filename = f"{date_str}-{clean_title}.md"
            target_path = os.path.join(TARGET_DIR, new_filename)
            
            # Front Matter 생성
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 이미 Front Matter가 있는지 확인
            if not content.startswith('---'):
                front_matter = f"""---
title: "{clean_title.replace('-', ' ')}"
date: {date_str}
permalink: /posts/{date_str.replace('-', '/')}/{clean_title}/
tags:
  - {category}
  - SK_Rookies
---

"""
                new_content = front_matter + content
            else:
                new_content = content

            # 파일 쓰기
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"Processed: {file} -> {new_filename}")

if __name__ == "__main__":
    process_files()
