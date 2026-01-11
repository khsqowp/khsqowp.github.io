import os
import re
from datetime import datetime

POSTS_DIR = '_posts'

def extract_date_from_content(content):
    # 다양한 날짜 패턴 정의 (우선순위 순)
    patterns = [
        # "강의 일자: 2025년 10월 24일", "날짜: 2025-10-24" 등 명시적 레이블이 있는 경우
        r'(?:강의\s*일자|강의\s*날짜|작성일|날짜|일시|강의일).*?(\d{4})[-년.]\s*(\d{1,2})[-월.]\s*(\d{1,2})',
        
        # 본문 내의 "2025년 10월 24일" 형태 (레이블 없이)
        r'(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일',
        
        # 본문 내의 "2025-10-24" 형태 (단, Front Matter의 date: 라인은 제외해야 함 - 호출부에서 처리)
        r'(?<!date: )(\d{4})-(\d{1,2})-(\d{1,2})',
        
        # "YYYY.MM.DD"
        r'(\d{4})\.(\d{1,2})\.(\d{1,2})'
    ]

    # Front Matter 영역 제외하고 본문에서만 찾기 위해 ---로 분리
    parts = content.split('---', 2)
    if len(parts) >= 3:
        body = parts[2]
    else:
        body = content

    # 본문 상단 50줄만 검사 (날짜는 보통 위에 있으므로)
    body_lines = body.split('\n')[:50]
    body_text = '\n'.join(body_lines)

    for pattern in patterns:
        match = re.search(pattern, body_text)
        if match:
            year, month, day = match.groups()
            # 유효성 검사 (월, 일이 범위 내인지)
            try:
                # 2023~2026년 사이의 데이터만 유효하다고 가정 (오탐지 방지)
                if 2023 <= int(year) <= 2026:
                    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            except:
                continue
    
    return None

def fix_dates():
    count = 0
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue

        filepath = os.path.join(POSTS_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 본문에서 진짜 날짜 추출
        real_date = extract_date_from_content(content)

        if real_date:
            # 현재 설정된 날짜 확인
            current_date_match = re.search(r'^date:\s*([0-9-]+)', content, re.MULTILINE)
            if current_date_match:
                current_date = current_date_match.group(1)
                
                # 날짜가 다르면 수정
                if current_date != real_date:
                    print(f"[Update] {filename}: {current_date} -> {real_date}")
                    new_content = re.sub(r'^date:\s*[0-9-]+', f'date: {real_date}', content, count=1, flags=re.MULTILINE)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
        else:
            print(f"[Skip] {filename}: No date found in content")

    print(f"Total updated files: {count}")

if __name__ == "__main__":
    fix_dates()
