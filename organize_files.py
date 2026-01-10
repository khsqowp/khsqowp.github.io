import os
import re

ROOT_DIR = 'SK_Rookies'
OUTPUT_FILE = os.path.join(ROOT_DIR, 'INDEX.md')

def get_title_from_content(filepath):
    """파일 내용에서 H1(# ) 제목을 추출"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for _ in range(10): # 상단 10줄만 탐색
                line = f.readline()
                if line.startswith('# '):
                    # 특수문자 제거 및 공백을 언더바(_)로 변경
                    title = line.strip('# ').strip()
                    title = re.sub(r'[^\w\s\-_]', '', title) # 특수문자 제거 (한글,영문,숫자,공백,_, - 허용)
                    return title
    except:
        pass
    return None

def generate_index():
    index_content = ["# 📚 SK Rookies 학습 목차\n"]
    
    # 폴더 정렬
    dirs = sorted([d for d in os.listdir(ROOT_DIR) if os.path.isdir(os.path.join(ROOT_DIR, d)) and not d.startswith('.')])
    
    for d in dirs:
        dir_path = os.path.join(ROOT_DIR, d)
        index_content.append(f"\n## 📂 {d}\n")
        
        # 파일 정렬
        files = sorted([f for f in os.listdir(dir_path) if f.endswith('.md')])
        
        for f in files:
            filepath = os.path.join(dir_path, f)
            
            # 순서 번호 추출 (예: "01) ")
            match = re.match(r'^(\d+[\):])\s*(.*)', f)
            if match:
                prefix = match.group(1)
                current_name = match.group(2).replace('.md', '')
            else:
                prefix = "- "
                current_name = f.replace('.md', '')
            
            # 내용 기반 추천 제목 가져오기
            suggested_title = get_title_from_content(filepath)
            
            display_name = suggested_title if suggested_title else current_name
            
            # 링크 생성 (URL 인코딩 처리)
            # GitHub 등에서 보기 편하게 상대 경로 사용
            link = f"{d}/{f}"
            
            index_content.append(f"- [{prefix} {display_name}]({link})")
            
            # 실제 파일명 변경 제안 (로그 출력만)
            # if suggested_title and suggested_title != current_name:
            #     print(f"Suggestion: {f} -> {prefix} {suggested_title}.md")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_content))
    
    print(f"✅ Generated index file at: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_index()
