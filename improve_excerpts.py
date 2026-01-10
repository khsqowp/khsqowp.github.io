import os
import re

POSTS_DIR = '_posts'

# 요약문으로 쓰기 부적절한 패턴들
BAD_EXCERPT_PATTERNS = [
    r'강의\s*일자',
    r'강의\s*날짜',
    r'작성일',
    r'날짜',
    r'일시'
]

def improve_excerpts():
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(POSTS_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 현재 excerpt 확인
        current_excerpt_match = re.search(r'^excerpt:\s*"(.*)"', content, re.MULTILINE)
        if not current_excerpt_match:
            continue
            
        current_excerpt = current_excerpt_match.group(1)
        
        # 나쁜 요약문인지 확인
        is_bad = False
        for pattern in BAD_EXCERPT_PATTERNS:
            if re.match(pattern, current_excerpt):
                is_bad = True
                break
        
        if not is_bad:
            continue
            
        # 나쁜 요약문이라면, 본문에서 더 좋은 문장 찾기
        print(f"Improving excerpt for {filename}...")
        
        # Front Matter 제거 후 본문만 분리
        parts = content.split('---', 2)
        if len(parts) < 3: continue
        body = parts[2]
        
        lines = body.split('\n')
        new_excerpt = ""
        
        # 본문 탐색 (최대 50줄)
        for line in lines[:50]:
            clean_line = line.strip()
            
            # 메타데이터, 제목, 빈 줄 건너뛰기
            if not clean_line or clean_line.startswith('#') or clean_line.startswith('---'):
                continue
            # 기존에 잡힌 나쁜 패턴도 건너뛰기
            is_meta_line = False
            for pattern in BAD_EXCERPT_PATTERNS:
                if re.match(pattern, clean_line) or clean_line.startswith('**' + pattern) or clean_line.startswith('> **' + pattern):
                    is_meta_line = True
                    break
            if is_meta_line: continue
            
            # 이미지, 링크 제외
            if clean_line.startswith('!') or clean_line.startswith('['):
                continue
                
            # 학습 목표, 개요, 요약 등의 키워드가 포함된 문장이나
            # 적당히 긴 문장(20자 이상)을 찾으면 당첨
            if len(clean_line) > 20:
                # 인용문 기호 제거
                new_excerpt = clean_line.lstrip('>').strip().replace('"', "'")
                # 마크다운 제거
                new_excerpt = re.sub(r'\*\*|__', '', new_excerpt)
                break
        
        if new_excerpt:
            # excerpt 교체
            new_content = content.replace(f'excerpt: "{current_excerpt}"', f'excerpt: "{new_excerpt}"')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  -> {new_excerpt[:50]}...")

if __name__ == "__main__":
    improve_excerpts()
