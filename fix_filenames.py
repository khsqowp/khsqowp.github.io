import os
import re
import unicodedata

POSTS_DIR = '_posts'

def normalize_filename(filename):
    # 1. NFD -> NFC 정규화 (한글 자소 합치기)
    filename = unicodedata.normalize('NFC', filename)
    
    # 2. 확장자 분리
    name, ext = os.path.splitext(filename)
    
    # 3. 날짜 분리 (YYYY-MM-DD)
    date_match = re.match(r'^(\d{4}-\d{2}-\d{2})-(.*)', name)
    if date_match:
        date_part = date_match.group(1)
        rest_part = date_match.group(2)
    else:
        # 날짜 없으면 오늘 날짜...가 아니라 그냥 둠 (이미 처리됐다고 가정)
        return filename

    # 4. 나머지 부분 정규화
    # 숫자+특수문자 시작 패턴 제거 (01. , 01) , 01: 등)
    rest_part = re.sub(r'^[0-9]+[).:\-_]\s*', '', rest_part)
    
    # 허용된 문자 외 모두 제거 (한글, 영문, 숫자, 하이픈)
    # 공백은 하이픈으로
    rest_part = rest_part.replace(' ', '-')
    rest_part = re.sub(r'[^\w\-\uac00-\ud7a3]', '', rest_part)
    
    # 중복 하이픈 제거
    rest_part = re.sub(r'-+', '-', rest_part).strip('-')
    
    return f"{date_part}-{rest_part}{ext}"

def fix_filenames():
    count = 0
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
            
        new_filename = normalize_filename(filename)
        
        if new_filename != filename:
            old_path = os.path.join(POSTS_DIR, filename)
            new_path = os.path.join(POSTS_DIR, new_filename)
            
            # 충돌 방지
            if os.path.exists(new_path) and new_filename != filename:
                print(f"Skipping {filename} -> {new_filename} (Target exists)")
                continue
                
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
            count += 1
            
    print(f"Total renamed files: {count}")

if __name__ == "__main__":
    fix_filenames()
