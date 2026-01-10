import os
import re

POSTS_DIR = '_posts'

def fix_front_matter():
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(POSTS_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 문제 상황: Front Matter가 중복되거나 꼬여있음
        # 해결 전략: 
        # 1. 파일 전체에서 'title:', 'date:', 'categories:', 'tags:', 'excerpt:' 정보를 정규식으로 모두 추출
        # 2. 가장 마지막(최신) 정보를 기준으로 Front Matter를 새로 구성
        # 3. 본문은 Front Matter 키워드들이 없는 순수 마크다운 부분만 추출
        
        # 1. 메타데이터 추출 (마지막에 등장한 값을 사용)
        title_matches = re.findall(r'^title:\s*"(.*)"', content, re.MULTILINE)
        date_matches = re.findall(r'^date:\s*([0-9-]+)', content, re.MULTILINE)
        excerpt_matches = re.findall(r'^excerpt:\s*"(.*)"', content, re.MULTILINE)
        
        # 카테고리와 태그는 파싱이 좀 복잡할 수 있으니 단순하게 처리
        # (보통 스크립트로 생성했으니 포맷이 일정할 것임)
        
        if not title_matches:
            print(f"Skipping {filename} (No title found)")
            continue
            
        title = title_matches[-1] # 가장 마지막에 정의된 제목 사용
        date = date_matches[-1] if date_matches else datetime.now().strftime('%Y-%m-%d')
        excerpt = excerpt_matches[-1] if excerpt_matches else ""
        
        # 카테고리 추출 (간이 파싱)
        category = "Study"
        if "categories:" in content:
            # categories: 다음 줄에 - Value 형태 찾기
            cat_match = re.search(r'categories:\s*\n\s*-\s*(.*)', content)
            if cat_match:
                category = cat_match.group(1)
                
        # 2. 본문 추출
        # Front Matter 영역(--- ... ---)을 모두 제거하고 남은 텍스트
        # 하지만 단순히 제거하면 안 되고, 중복된 Front Matter 텍스트들을 지워야 함.
        
        lines = content.split('\n')
        body_lines = []
        is_front_matter_line = False
        
        for line in lines:
            stripped = line.strip()
            # Front Matter 키워드로 시작하는 라인은 건너뜀 (본문에는 이런 줄이 없을 것이라 가정)
            if stripped.startswith('title:') or stripped.startswith('date:') or \
               stripped.startswith('excerpt:') or stripped.startswith('categories:') or \
               stripped.startswith('tags:') or stripped == '---':
                continue
            # 카테고리/태그 리스트 아이템 (- Python 등)은 문맥을 봐야 하지만,
            # Front Matter 바로 뒤에 나오는 리스트 아이템일 확률이 높음.
            # 안전하게: 본문 시작(# 또는 글자) 전까지의 리스트 아이템은 무시
            if not body_lines and stripped.startswith('- '):
                continue
                
            body_lines.append(line)
            
        # 본문 앞뒤 공백 제거
        body = '\n'.join(body_lines).strip()
        
        # 3. 파일 재작성
        new_front_matter = f"""
---
title: \"{title}\"\ndate: {date}\nexcerpt: \"{excerpt}\"\ncategories:\n  - {category}\ntags:\n  - {category}\n  - SK_Rookies
---

"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_front_matter + body)
            
        print(f"Fixed: {filename}")

if __name__ == "__main__":
    fix_front_matter()
