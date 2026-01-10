import os

POSTS_DIR = '_posts'

def fix_file_encoding_and_start():
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(POSTS_DIR, filename)
        
        # 1. 바이너리 모드로 읽어서 BOM 확인 및 제거
        with open(filepath, 'rb') as f:
            raw_content = f.read()
            
        # UTF-8 BOM (EF BB BF) 제거
        if raw_content.startswith(b'\xef\xbb\xbf'):
            raw_content = raw_content[3:]
            
        # 2. 텍스트로 디코딩
        try:
            content = raw_content.decode('utf-8')
        except UnicodeDecodeError:
            # EUC-KR일 수도 있으니 시도
            try:
                content = raw_content.decode('euc-kr')
            except:
                print(f"Error decoding {filename}")
                continue

        # 3. 맨 앞 공백/빈줄 제거 (lstrip)
        content = content.lstrip()
        
        # 4. --- 로 시작하는지 확인 (이중 체크)
        if not content.startswith('---'):
            # 만약 ---가 없다면, 제가 아까 만든 Front Matter가 날아갔거나 꼬인 것임
            # 이 경우엔 어쩔 수 없이 내용을 확인해봐야 함
            print(f"Warning: {filename} does not start with '---'")
            # 강제로 --- 를 붙여줄 수도 있지만, 내용이 꼬일 수 있어 일단 둠
        else:
            # 5. 파일 다시 쓰기 (UTF-8, No BOM)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {filename}")

if __name__ == "__main__":
    fix_file_encoding_and_start()
