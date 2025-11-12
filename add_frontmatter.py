#!/usr/bin/env python3
"""
Just-the-Docs 테마를 위한 front matter 자동 추가 스크립트
"""
import os
import re

# 카테고리 구조 정의
structure = {
    "2_보안_기본_역량/2-1_네트워크_보안": {"parent": "2-1. 네트워크 보안", "grand_parent": "2. 보안 기본 역량"},
    "2_보안_기본_역량/2-2_클라우드_보안": {"parent": "2-2. 클라우드 보안", "grand_parent": "2. 보안 기본 역량"},
    "2_보안_기본_역량/2-3_애플리케이션_보안": {"parent": "2-3. 애플리케이션 보안", "grand_parent": "2. 보안 기본 역량"},
    "2_보안_기본_역량/2-4_개인정보보호": {"parent": "2-4. 개인정보보호", "grand_parent": "2. 보안 기본 역량"},
    "1_AI_기본_역량/1-1_파이썬": {"parent": "1-1. 파이썬", "grand_parent": "1. AI 기본 역량"},
    "1_AI_기본_역량/1-2_머신러닝_딥러닝": {"parent": "1-2. 머신러닝/딥러닝", "grand_parent": "1. AI 기본 역량"},
    "3_응용_기술_심화/3-1_AI_보안관제_및_로그_분석": {"parent": "3-1. AI 보안관제", "grand_parent": "3. 응용 기술 심화"},
    "3_응용_기술_심화/3-2_악성코드_분석_및_대응": {"parent": "3-2. 악성코드 분석", "grand_parent": "3. 응용 기술 심화"},
    "3_응용_기술_심화/3-3_취약점_진단_및_모의해킹": {"parent": "3-3. 취약점 진단", "grand_parent": "3. 응용 기술 심화"},
    "4_실무_프로젝트/4-1_최종_프로젝트": {"parent": "4-1. 최종 프로젝트", "grand_parent": "4. 실무 프로젝트"},
}

def extract_title_from_content(content):
    """마크다운 내용에서 첫 번째 # 제목 추출"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        # 이모지와 제목 번호를 제외한 실제 제목 추출
        title = match.group(1).strip()
        # "🐍 1. 파이썬 기초 문법: ..." -> "1. 파이썬 기초 문법"
        title = re.sub(r'^[^\w\d]+\s*', '', title)  # 앞의 이모지 제거
        title = re.sub(r':.*$', '', title)  # 콜론 이후 제거
        return title.strip()
    return None

def has_frontmatter(content):
    """이미 front matter가 있는지 확인"""
    return content.strip().startswith('---')

def add_frontmatter_to_file(filepath, base_dir):
    """파일에 front matter 추가"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 이미 front matter가 있으면 스킵
        if has_frontmatter(content):
            print(f"⏭️  Skipping (already has front matter): {filepath}")
            return

        # 파일의 상대 경로 추출
        rel_path = os.path.relpath(filepath, base_dir)

        # 카테고리 구조에서 parent 정보 찾기
        parent_info = None
        for key, value in structure.items():
            if key in rel_path:
                parent_info = value
                break

        if not parent_info:
            print(f"⚠️  Skipping (no parent info): {filepath}")
            return

        # 제목 추출
        title = extract_title_from_content(content)
        if not title:
            print(f"⚠️  Skipping (no title found): {filepath}")
            return

        # Front matter 생성
        frontmatter = f"""---
layout: default
title: {title}
parent: {parent_info['parent']}
grand_parent: {parent_info['grand_parent']}
---

"""

        # 파일에 front matter 추가
        new_content = frontmatter + content

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✅ Added front matter: {filepath}")

    except Exception as e:
        print(f"❌ Error processing {filepath}: {str(e)}")

def main():
    base_dir = "SK_Rookies"

    # 모든 .md 파일 찾기
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md') and file != 'index.md':
                filepath = os.path.join(root, file)
                add_frontmatter_to_file(filepath, base_dir)

if __name__ == "__main__":
    main()
    print("\n✨ Front matter 추가 작업 완료!")
