#!/usr/bin/env python3
"""
SK_Rookies_Now 파일들을 Jekyll 포스트로 변환하는 스크립트
"""

import os
import re
from datetime import datetime
from pathlib import Path

def extract_date_from_filename(filename):
    """파일명에서 날짜 추출"""
    # 1. 10-23), 11-24) 형식 찾기
    match = re.search(r'(\d{1,2})[:-](\d{1,2})\)', filename)
    if match:
        month = int(match.group(1))
        day = int(match.group(2))
        year = 2024
        return datetime(year, month, day, 9, 0, 0)
    
    # 2. ChapterXX, PhaseXX 처리 (임의의 날짜 할당)
    # AWS 추가학습 (Chapter) -> 2024-12-20 부터
    match_ch = re.search(r'Chapter(\d+)', filename)
    if match_ch:
        num = int(match_ch.group(1))
        # 1~11일까지 가능 (31일)
        return datetime(2024, 12, 20 + num, 9, 0, 0)

    # Phase (Phase) -> 2024-12-30 부터
    match_ph = re.search(r'Phase(\d+)', filename)
    if match_ph:
        num = int(match_ph.group(1))
        return datetime(2024, 12, 30, 9, 0, num) # 시간으로 구분

    # 3. 기타 파일 (기본값 또는 현재 날짜)
    return datetime(2025, 1, 1, 9, 0, 0)

def extract_title_from_content(content):
    """파일 내용에서 제목 추출"""
    lines = content.split('\n')
    for line in lines:
        if line.strip().startswith('# '):
            title = line.strip()[2:].strip()
            # 이모지 및 특수문자 제거
            title = re.sub(r'[📝🔹📚💡🎯⚡🚀🔥💻🛡️🌐🔐🏗️📊🎓🤖]', '', title)
            title = title.strip()
            return title
    # 제목이 없으면 파일명에서 추출
    return None

def sanitize_slug(title):
    """제목을 URL-safe slug로 변환"""
    # 날짜 및 특수문자 제거
    title = re.sub(r'^\d{1,2}-\d{1,2}\)', '', title)
    title = re.sub(r'[^\w\s가-힣-]', '', title)
    title = re.sub(r'\s+', '-', title.strip())
    return title[:100]  # 너무 길면 자르기

def determine_category(filename, content, parent_dir_name):
    """상위 디렉토리명을 기반으로 카테고리 결정"""
    
    if parent_dir_name == '01_python':
        return ['python']
    elif parent_dir_name == '02_linux-network':
        return ['linux-network']
    elif parent_dir_name == '추가학습': # 02_linux-network/추가학습
        return ['linux-network-study']
    elif parent_dir_name == '03_application-security':
        return ['application-security']
    
    # 기본값 (매칭되지 않는 경우)
    return ['general']

def convert_file_to_post(source_file, posts_dir):
    """단일 파일을 Jekyll 포스트로 변환"""
    try:
        # 파일 읽기
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 날짜 추출
        post_date = extract_date_from_filename(source_file.name)
        if not post_date:
            print(f"⚠ No date found in filename: {source_file.name}")
            return False

        # 제목 추출
        title = extract_title_from_content(content)
        if not title:
            # 파일명에서 제목 추출
            title = re.sub(r'📝\d{1,2}-\d{1,2}\)\s*', '', source_file.stem)
            title = re.sub(r'\(\d+일차\)', '', title).strip()

        # 카테고리 결정
        parent_dir_name = source_file.parent.name
        categories = determine_category(source_file.name, content, parent_dir_name)

        # Slug 생성
        slug = sanitize_slug(title)

        # Jekyll frontmatter 생성
        frontmatter = f"""---
layout: post
title: "{title}"
date: {post_date.strftime('%Y-%m-%d %H:%M:%S +0900')}
categories: [{', '.join(categories)}]
tags: [SK-Rookies, Lecture-Notes]
---

"""

        # 새 포스트 파일명 생성
        new_filename = f"{post_date.strftime('%Y-%m-%d')}-{slug}.md"
        new_filepath = posts_dir / new_filename

        # 포스트 작성
        with open(new_filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter + content)

        print(f"✓ Converted: {source_file.name} -> {new_filename}")
        return True

    except Exception as e:
        print(f"✗ Error converting {source_file.name}: {e}")
        return False

def main():
    base_dir = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/study")
    source_dir = base_dir / "SK_Rookies_Now"
    posts_dir = base_dir / "_posts"

    # _posts 디렉토리 확인
    posts_dir.mkdir(exist_ok=True)

    # 모든 .md 파일 찾기
    md_files = []
    for md_file in source_dir.rglob("*.md"):
        # STT 프롬프트 파일 제외
        if "프롬프트" not in md_file.name:
            md_files.append(md_file)

    # 날짜순 정렬
    md_files.sort(key=lambda x: x.name)

    converted_count = 0
    for md_file in md_files:
        if convert_file_to_post(md_file, posts_dir):
            converted_count += 1

    print(f"\n총 {converted_count}개 파일 변환 완료!")
    print(f"위치: {posts_dir}")

if __name__ == "__main__":
    main()
