import os

# 수동 매핑: _posts 파일명 -> SK_Rookies 상대 경로
MANUAL_MAP = {
    # NumPy/Pandas 3일차
    "2025-11-05-Pandas-데이터-프레임-조작-심화-3일차.md": "SK_Rookies/01_python/09) NumPy & Pandas Day 3 강의 노트 (3일차).md",
    
    # Secure Python 4일차
    "2025-10-30-Secure-Python-Day-4일차.md": "SK_Rookies/01_python/05) Secure Python Day 강의 노트 (4일차).md",
    
    # Streamlit 5일차
    "2025-11-07-Streamlit-웹-시각화-및-보안-대시보드-구축-5일차.md": "SK_Rookies/01_python/11) Streamlit 웹 시각화 및 보안 대시보드 구축 강의 노트 (5일차).md",
    
    # 파이썬 제어구문 3일차
    "2025-10-29-파이썬-제어구문-3일차.md": "SK_Rookies/01_python/04) 파이썬 제어구문 및 반복문 강의 노트 (3일차).md",
}

def get_front_matter(content):
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1]
    return None

def sync_manual():
    for post_name, source_rel_path in MANUAL_MAP.items():
        post_path = os.path.join('_posts', post_name)
        source_path = source_rel_path # 이미 상대 경로임
        
        if not os.path.exists(post_path):
            print(f"Skipping {post_name} (not found in _posts)")
            continue

        if not os.path.exists(source_path):
             print(f"Skipping source {source_path} (not found)")
             continue

        # Front Matter 추출 및 이식
        with open(post_path, 'r', encoding='utf-8') as f:
            post_content = f.read()
        
        fm = get_front_matter(post_content)
        if not fm:
            print(f"No front matter in {post_path}")
            continue
            
        with open(source_path, 'r', encoding='utf-8') as f:
            source_content = f.read()
            
        # 기존 Front Matter 제거
        if source_content.startswith('---'):
            parts = source_content.split('---', 2)
            if len(parts) >= 3:
                body = parts[2]
            else:
                body = source_content
        else:
            body = source_content
            
        new_content = f"---\"{fm}\"---\n\n{body.lstrip()}"
        
        with open(source_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Synced: {source_path}")

if __name__ == "__main__":
    sync_manual()