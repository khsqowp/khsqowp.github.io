#!/usr/bin/env python3
"""
SK_Rookies 콘텐츠를 Jekyll 블로그 포스트 형식으로 변환하는 스크립트
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path

def sanitize_filename(title):
    """파일명에서 특수문자 제거 및 공백을 하이픈으로 변경"""
    # 이모지 및 특수문자 제거
    title = re.sub(r'[^\w\s\-가-힣]', '', title)
    # 공백을 하이픈으로 변경
    title = re.sub(r'\s+', '-', title.strip())
    return title

def extract_title_from_content(content):
    """마크다운 콘텐츠에서 첫 번째 # 헤딩 추출"""
    for line in content.split('\n'):
        if line.strip().startswith('# '):
            title = line.strip()[2:].strip()
            # 이모지 제거
            title = re.sub(r'[^\w\s\-가-힣:,./()]', '', title)
            return title
    return None

def get_category_from_path(file_path):
    """파일 경로에서 카테고리 추출"""
    parts = Path(file_path).parts

    # SK_Rookies 디렉토리 찾기
    try:
        idx = parts.index('SK_Rookies')
        # SK_Rookies 다음 경로들을 카테고리로 사용
        categories = []
        for i in range(idx + 1, len(parts) - 1):  # 파일명 제외
            part = parts[i]
            if part.startswith('SK_Rookies'):
                continue
            # 숫자와 언더스코어 제거
            clean_part = re.sub(r'^\d+[-_]', '', part)
            clean_part = clean_part.replace('_', ' ')
            categories.append(clean_part)

        return categories if categories else ['General']
    except ValueError:
        return ['General']

def convert_frontmatter(content, file_path, post_date):
    """기존 frontmatter를 블로그 포스트 형식으로 변환"""

    # 기존 frontmatter 제거
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()

    # 제목 추출
    title = extract_title_from_content(content)
    if not title:
        title = Path(file_path).stem

    # 카테고리 추출
    categories = get_category_from_path(file_path)

    # 새로운 frontmatter 생성
    new_frontmatter = f"""---
layout: post
title: "{title}"
date: {post_date.strftime('%Y-%m-%d %H:%M:%S +0900')}
categories: {' '.join(categories)}
tags: [AI, Cybersecurity, SK-Rookies]
---

"""

    return new_frontmatter + content

def main():
    # 경로 설정
    base_dir = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/study")
    source_dir = base_dir / "SK_Rookies" / "SK_Rookies"
    posts_dir = base_dir / "_posts"

    # _posts 디렉토리 생성
    posts_dir.mkdir(exist_ok=True)

    # 시작 날짜 (2024년 1월 1일부터 시작)
    current_date = datetime(2024, 1, 1, 9, 0, 0)

    # 모든 .md 파일 찾기 (index.md 제외)
    md_files = []
    for md_file in source_dir.rglob("*.md"):
        if md_file.name != "index.md":
            md_files.append(md_file)

    # 파일을 경로 순으로 정렬
    md_files.sort(key=lambda x: str(x))

    converted_count = 0

    for md_file in md_files:
        try:
            # 파일 읽기
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Frontmatter 변환
            new_content = convert_frontmatter(content, str(md_file), current_date)

            # 제목 추출
            title = extract_title_from_content(content)
            if not title:
                title = md_file.stem

            # 파일명 생성 (YYYY-MM-DD-title.md)
            safe_title = sanitize_filename(title)
            new_filename = f"{current_date.strftime('%Y-%m-%d')}-{safe_title}.md"
            new_file_path = posts_dir / new_filename

            # 파일 쓰기
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"✓ Converted: {md_file.name} -> {new_filename}")
            converted_count += 1

            # 날짜 증가 (하루씩)
            current_date += timedelta(days=1)

        except Exception as e:
            print(f"✗ Error converting {md_file}: {e}")

    print(f"\n총 {converted_count}개 파일 변환 완료!")
    print(f"위치: {posts_dir}")

if __name__ == "__main__":
    main()
