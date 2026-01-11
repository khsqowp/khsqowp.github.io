import os
import re
import difflib

POSTS_DIR = '_posts'
SOURCE_DIR = 'SK_Rookies'

def clean_name(name):
    # 파일명 비교를 위해 특수문자, 날짜 제거하고 순수 텍스트만 남김
    name = os.path.splitext(name)[0]
    name = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', name) # _posts 날짜 제거
    name = re.sub(r'^[0-9]+[):]\s*', '', name) # SK_Rookies 순서 번호 제거
    name = re.sub(r'[\[\]\(\)]', '', name)
    name = re.sub(r'\s+', '', name)
    name = re.sub(r'[^\w\u3131-\u3163\uac00-\ud7a3]', '', name)
    return name

def get_front_matter(content):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1]
    return None

def sync_back():
    # 1. _posts 파일 로드
    posts_map = {} # { clean_name : { 'front_matter': ..., 'filepath': ... } } 
    
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'): continue
        
        path = os.path.join(POSTS_DIR, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        fm = get_front_matter(content)
        if fm:
            c_name = clean_name(filename)
            posts_map[c_name] = {'front_matter': fm, 'filepath': path}

    # 2. SK_Rookies 원본 파일 순회 및 업데이트
    updated_count = 0
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        for filename in files:
            if not filename.endswith('.md'): continue
            
            source_path = os.path.join(root, filename)
            c_name = clean_name(filename)
            
            # 매칭 시도
            match = posts_map.get(c_name)
            
            # 정확한 일치가 없으면 유사도 비교 (파일명 변경되었을 가능성)
            if not match:
                best_ratio = 0
                best_key = None
                for key in posts_map.keys():
                    ratio = difflib.SequenceMatcher(None, c_name, key).ratio()
                    if ratio > 0.8 and ratio > best_ratio:
                        best_ratio = ratio
                        best_key = key
                
                if best_key:
                    match = posts_map[best_key]
            
            if match:
                # 원본 파일 읽기
                with open(source_path, 'r', encoding='utf-8') as f:
                    source_content = f.read()
                
                # 기존 Front Matter 제거 (있다면)
                if source_content.startswith('---'):
                    parts = source_content.split('---', 2)
                    if len(parts) >= 3:
                        body = parts[2]
                    else:
                        body = source_content
                else:
                    body = source_content
                
                # _posts의 Front Matter + 원본 Body 조합
                new_content = f"---\
{match['front_matter']}---\
\n{body.lstrip()}"
                
                # 파일 업데이트
                with open(source_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"Synced: {filename} <- {os.path.basename(match['filepath'])}")
                updated_count += 1
            else:
                print(f"Warning: No match found for source file {filename}")

    print(f"Total synced files: {updated_count}")

if __name__ == "__main__":
    sync_back()
