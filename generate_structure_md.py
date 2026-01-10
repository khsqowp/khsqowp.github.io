import os
import re

ROOT_DIR = 'SK_Rookies'
OUTPUT_FILE = os.path.join(ROOT_DIR, '구조.md')

def get_title_from_content(filepath):
    """파일 내용에서 H1(# ) 제목을 추출"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # 상단 20줄 탐색
            for _ in range(20):
                line = f.readline()
                # # 제목, # **제목**, # 📝 제목 등 다양한 패턴 처리
                if line.lstrip().startswith('# '):
                    title = line.strip().lstrip('#').strip()
                    # 이모지 제거 (선택 사항, 깔끔하게 하려면 제거)
                    # title = re.sub(r'[^Waranted titles]', '', title) 
                    return title
    except:
        pass
    return None

def generate_structure_md():
    content_lines = ["# 📚 SK Rookies 파일 구조 및 추천 제목 정리\n"]
    
    # 폴더 정렬 (숨김 폴더 제외)
    dirs = sorted([d for d in os.listdir(ROOT_DIR) if os.path.isdir(os.path.join(ROOT_DIR, d)) and not d.startswith('.')])
    
    for d in dirs:
        dir_path = os.path.join(ROOT_DIR, d)
        content_lines.append(f"\n## 📂 {d}\n")
        
        # 마크다운 파일만 정렬
        files = sorted([f for f in os.listdir(dir_path) if f.endswith('.md')])
        
        for f in files:
            filepath = os.path.join(dir_path, f)
            
            # 내용에서 제목 추출
            suggested_title = get_title_from_content(filepath)
            
            if not suggested_title:
                suggested_title = "(내용에서 제목을 찾을 수 없음)"
            
            # 포맷: - `파일명` -> **추천 제목**
            content_lines.append(f"- `{f}` -> **{suggested_title}**")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content_lines))
    
    print(f"✅ Generated structure file at: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_structure_md()
