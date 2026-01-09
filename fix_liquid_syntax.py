import os

TARGET_DIR = '_posts'

def escape_liquid_tags():
    for filename in os.listdir(TARGET_DIR):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(TARGET_DIR, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Jekyll Liquid 태그 충돌 방지
        # {{ -> {{"{{"}}
        # {% -> {{"{% "}}
        # 이렇게 바꾸면 Jekyll이 "문자열 그대로 출력해라"라고 이해함.
        # 하지만 이미 Front Matter에 있는 건 건드리면 안 됨.
        
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            body = parts[2]
            
            # 본문에서만 치환
            # 단순하게 {{ 를 {{"{{"}} 로 바꾸는 건 위험할 수 있음 (이미 감싸져 있을 수 있으니)
            # 대신 HTML Entity로 바꾸는 게 가장 안전함.
            # {{ -> &#123;&#123;
            # }} -> &#125;&#125;
            # {% -> &#123;%
            # %} -> %&#125;
            
            new_body = body.replace('{{', '&#123;&#123;').replace('}}', '&#125;&#125;')
            new_body = new_body.replace('{%', '&#123;%').replace('%}', '%&#125;')
            
            new_content = f"---{front_matter}---{new_body}"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Fixed: {filename}")

if __name__ == "__main__":
    escape_liquid_tags()
