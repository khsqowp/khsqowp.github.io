import os
import re

# 날짜 매핑
DATE_MAP = {
    'Dell': '2025-09-17',
    'DIC 2025': '2025-09-18',
    'REAL Summit 2025': '2025-09-11'
}

ARCHIVE_DIR = 'Archive/conference'

def add_front_matter():
    for root, dirs, files in os.walk(ARCHIVE_DIR):
        for file in files:
            if not file.endswith('.md'):
                continue
            
            filepath = os.path.join(root, file)
            parent_dir = os.path.basename(root)
            
            # 날짜 결정
            date_str = DATE_MAP.get(parent_dir, '2025-01-01')
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 이미 Front Matter가 있는지 확인
            if content.startswith('---'):
                print(f"Skipping (already has FM): {file}")
                continue
                
            # 제목 추출 (파일명 또는 첫 헤더)
            title = os.path.splitext(file)[0]
            # 파일명 앞의 숫자 제거 (예: "1. 제목" -> "제목")
            title = re.sub(r'^\d+\.\s*', '', title)
            
            match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
            if match:
                title = match.group(1).strip()
            
            # 요약 추출 (본문 첫 부분)
            # 헤더 제외하고 텍스트만 추출 시도
            body = re.sub(r'^#+.*', '', content, flags=re.MULTILINE).strip()
            excerpt = body[:200].replace('\n', ' ').strip() + "..."
            excerpt = excerpt.replace('"', "'") # 따옴표 이스케이프
            
            # 카테고리 결정
            category = f"Conference-{parent_dir.replace(' ', '-')}"
            
            front_matter = f"""---
title: \"{title}\"\ndate: {date_str}\nexcerpt: \"{excerpt}\"\ncategories:\n  - {category}\ntags:\n  - Conference
---

"""

            new_content = front_matter + content
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated: {file} ({date_str})")

if __name__ == "__main__":
    add_front_matter()
