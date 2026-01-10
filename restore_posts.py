import os
import re

POSTS_DIR = '_posts'

def restore_posts():
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(POSTS_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. 진짜 본문 찾기 (기존의 망가진 Front Matter 덩어리들을 모두 건너뛰기)
        # 전략: '# ' (H1 제목) 또는 실제 내용이 시작되는 부분을 찾는다.
        # Front Matter는 'title:', 'date:', 'excerpt:', 'categories:', 'tags:', '---' 로 구성됨.
        
        lines = content.split('\n')
        body_start_idx = 0
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            # Front Matter 키워드나 구분선이면 건너뜀
            if stripped.startswith('title:') or stripped.startswith('date:') or \
               stripped.startswith('excerpt:') or stripped.startswith('categories:') or \
               stripped.startswith('tags:') or stripped == '---' or stripped == '':
                continue
            # 리스트 아이템인데 위쪽이 다 Front Matter 키워드였다면 이것도 설정의 일부일 수 있음
            if stripped.startswith('- '):
                continue
                
            # 여기까지 왔으면 본문 시작점
            body_start_idx = i
            break
            
        real_body = '\n'.join(lines[body_start_idx:])
        
        # 2. 날짜 추출 (파일명에서)
        # 파일명이 YYYY-MM-DD-제목.md 형식이므로 여기서 날짜를 가져오는 게 가장 정확함
        date_match = re.match(r'^(\d{4}-\d{2}-\d{2})', filename)
        if date_match:
            date = date_match.group(1)
        else:
            # 파일명에 날짜가 없으면 본문에서 찾기 (아까 로직)
            date = "2026-01-10" # Default
            # ... (본문 검색 로직 생략, 일단 파일명 우선)

        # 3. 제목 추출 (본문의 첫 번째 # 제목)
        title = filename.replace('.md', '') # 기본값
        for line in real_body.split('\n')[:20]:
            if line.strip().startswith('# '):
                title = line.strip().lstrip('#').strip().replace('"', "'")
                break
        
        # 4. 요약문(Excerpt) 추출 (본문에서)
        excerpt = ""
        for line in real_body.split('\n')[:20]:
            clean_line = line.strip()
            if clean_line.startswith('>'):
                excerpt = clean_line.lstrip('>').strip().replace('"', "'")
                if len(excerpt) > 10: break
        
        if not excerpt:
            # 인용문 없으면 첫 문단
            for line in real_body.split('\n')[:30]:
                clean_line = line.strip()
                if clean_line and not clean_line.startswith('#') and not clean_line.startswith('!'):
                    excerpt = clean_line.replace('"', "'")
                    if len(excerpt) > 150: excerpt = excerpt[:147] + "..."
                    break
        
        # 5. 카테고리 추출 (기존 파일 내용에서 'categories:' 뒤에 있는 값 찾기)
        # 이건 기존 파일이 망가졌어도 정보는 남아있을 확률이 높음
        category = "Study"
        cat_match = re.search(r'categories:\s*\n\s*-\s*(.*)', content)
        if cat_match:
            category = cat_match.group(1)
            
        # 6. 파일 재작성 (Clean Front Matter + Body)
        # 맨 앞에 공백 없이 --- 로 시작해야 함!
        new_content = f"""
---
title: \"{title}\"\ndate: {date}\nexcerpt: \"{excerpt}\"\ncategories:\n  - {category}\ntags:\n  - {category}\n  - SK_Rookies
---

{real_body}
"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Restored: {filename} -> {date} / {title}")

if __name__ == "__main__":
    restore_posts()
