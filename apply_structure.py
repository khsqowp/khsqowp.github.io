import os
import re
import shutil

STRUCTURE_FILE = '구조.txt'
SOURCE_DIR = 'SK_Rookies'
TARGET_DIR = '_posts'

# 구조.txt 파싱하여 매핑 데이터 생성
# { "원본파일명": {"title": "새제목", "date": "YYYY-MM-DD"} }
file_mapping = {}

def parse_structure():
    current_category = ""
    with open(STRUCTURE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # 카테고리 파싱 (📂 01_python)
        if line.startswith('📂'):
            current_category = line.split(' ')[1]
            continue
            
        # 파일 정보 파싱 (- 원본제목 (YYYY-MM-DD))
        # 정규식으로 '제목'과 '(날짜)' 추출
        # 예: - 생성형 AI 활용... (1일차) (2025-10-24)
        
        # 날짜 추출 (마지막 괄호)
        date_match = re.search(r'\((20\d{2}-\d{2}-\d{2})\)$', line)
        if date_match:
            date = date_match.group(1)
            # 날짜 부분을 제외한 나머지 제목
            title_part = line[:date_match.start()].strip()
            # 앞의 '- ' 제거
            if title_part.startswith('- '):
                title_part = title_part[2:]
            
            # 매핑 키 생성을 위해 원본 파일명 추적은 어렵지만,
            # 구조.txt의 순서와 실제 폴더의 파일 순서가 같다고 가정하거나
            # 제목 유사성을 비교해야 함.
            # 하지만 사용자님 요청은 "이대로 적용해줘"이므로, 
            # 구조.txt의 내용이 곧 "정답"임.
            # 따라서 SK_Rookies를 순회하며 매칭하는 게 아니라,
            # 구조.txt를 기준으로 _posts를 생성해야 함.
            
            # 문제: 구조.txt에는 "원본 파일명"이 없음. "추천 제목"만 있음.
            # 해결: 제가 아까 구조.txt를 만들 때 "추천 제목"을 적었으니,
            # SK_Rookies 폴더를 뒤져서 해당 내용을 담고 있는 파일을 찾아야 함.
            # 가장 확실한 건, "순서"대로 매칭하는 것임.
            
            if current_category not in file_mapping:
                file_mapping[current_category] = []
            
            file_mapping[current_category].append({
                "title": title_part,
                "date": date
            })

def apply_to_posts():
    parse_structure()
    
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)
    os.makedirs(TARGET_DIR)
    
    # 구조.txt의 카테고리 순서대로 처리
    for category, items in file_mapping.items():
        # 실제 폴더 경로
        src_dir_path = os.path.join(SOURCE_DIR, category)
        if not os.path.exists(src_dir_path):
            print(f"Warning: Directory not found {src_dir_path}")
            continue
            
        # 실제 파일 목록 (이름순 정렬)
        # 구조.txt도 이름순(순서번호순)으로 작성되었으므로 매칭됨
        src_files = sorted([f for f in os.listdir(src_dir_path) if f.endswith('.md')])
        
        # 개수 확인
        if len(src_files) != len(items):
            print(f"Warning: File count mismatch in {category}. Real: {len(src_files)}, Struct: {len(items)}")
            # 개수가 다르면 앞에서부터 차례대로 매칭 (최대한 노력)
        
        for i, src_file in enumerate(src_files):
            if i >= len(items): break
            
            item = items[i]
            title = item['title']
            date = item['date']
            
            # 원본 내용 읽기
            with open(os.path.join(src_dir_path, src_file), 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 기존 Front Matter 제거
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    body = parts[2]
                else:
                    body = content
            else:
                body = content
            
            # Liquid 태그 이스케이프
            body = body.replace('{{', '&#123;&#123;').replace('}}', '&#125;&#125;')
            body = body.replace('{%', '&#123;%').replace('%}', '%&#125;')
            
            # 새 Front Matter 작성
            front_matter = f"""---
title: "{title}"
date: {date}
categories:
  - {category}
tags:
  - {category}
  - SK_Rookies
---

"""
            # 파일명 생성 (YYYY-MM-DD-제목.md) - URL용
            # 제목에서 특수문자 제거하고 공백을 하이픈으로
            safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '-')
            new_filename = f"{date}-{safe_title}.md"
            
            with open(os.path.join(TARGET_DIR, new_filename), 'w', encoding='utf-8') as f:
                f.write(front_matter + body.lstrip())
                
            print(f"Created: {new_filename}")

if __name__ == "__main__":
    apply_to_posts()
