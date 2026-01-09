import os
import re
import datetime

POSTS_DIR = '_posts'

DATE_PATTERNS = [
    r'(\\d{4})년\\s*(\\d{1,2})월\\s*(\\d{1,2})일',       
    r'(\\d{4})-(\\d{1,2})-(\\d{1,2})',                 
    r'(\\d{4})\\.(\\d{1,2})\\.(\\d{1,2})',               
    r'(\\d{4})/(\\d{1,2})/(\\d{1,2})',                 
    r'Date:\\s*(\\d{4})-(\\d{1,2})-(\\d{1,2})',         
    r'날짜[:\\s]*(\\d{4})년\\s*(\\d{1,2})월\\s*(\\d{1,2})일',
    r'날짜[:\\s]*(\\d{4})\\.\\s*(\\d{1,2})\\.\\s*(\\d{1,2})'
]

def find_date_in_content(content):
    lines = content.split('\n')[:30] 
    for line in lines:
        for pattern in DATE_PATTERNS:
            match = re.search(pattern, line)
            if match:
                year, month, day = match.groups()
                return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    return None

def update_posts():
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(POSTS_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        extracted_date = find_date_in_content(content)
        
        if not extracted_date:
            print(f"Skipping (No date found): {filename}")
            continue
            
        print(f"Found date {extracted_date} in {filename}")
        
        # Front Matter 수정
        if re.search(r'^date:', content, re.MULTILINE):
            new_content = re.sub(r'^date:.*$', f'date: {extracted_date}', content, count=1, flags=re.MULTILINE)
        else:
            # title 다음 줄에 date 추가
            new_content = re.sub(r'(^title:.*$)', f'\\1\ndate: {extracted_date}', content, count=1, flags=re.MULTILINE)
            
        # 파일명 변경
        old_date_match = re.match(r'(\\d{4}-\\d{2}-\\d{2})-(.*)', filename)
        if old_date_match:
            title_part = old_date_match.group(2)
        else:
            title_part = filename
            
        new_filename = f"{extracted_date}-{title_part}"
        
        # 파일 쓰기
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        if new_filename != filename:
            new_filepath = os.path.join(POSTS_DIR, new_filename)
            os.rename(filepath, new_filepath)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    update_posts()