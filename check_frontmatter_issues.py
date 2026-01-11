import os
import re

POSTS_DIR = '_posts'

def check_and_fix():
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Front Matter 추출
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                fm = parts[1]
                body = parts[2]
                
                new_fm = fm
                changed = False
                
                # title이나 excerpt에 따옴표 없이 콜론(:)이 포함된 경우 찾기
                # 예: title: 01:06 프로젝트 (위험) -> title: "01:06 프로젝트" (안전)
                # 하지만 이미 migrate_posts.py에서 따옴표를 붙였으므로, 
                # 따옴표 안의 내용을 검사해야 함.
                
                # 단순히 "01" 같은 문자가 문제가 아니라, URL 생성 시 사용되는 permalink 등에 영향 줄 수 있음.
                # 여기서는 특수문자나 숫자 시작 패턴을 다시 한번 확인.
                
                # excerpt: "01: ... " 같은 건 괜찮음.
                # 문제는 파일명일 확률이 가장 높았음.
                
                # 혹시 모르니 excerpt나 title에 이상한 문자가 있는지 확인만.
                pass

if __name__ == "__main__":
    check_and_fix()
