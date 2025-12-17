#!/usr/bin/env python3
"""
SK_Rookies_Now 파일들을 Jekyll 포스트로 변환하는 스크립트 (수정본)
카테고리: python, linux-network, linux-network-추가학습, application-security
"""

import os
import re
from datetime import datetime
from pathlib import Path

def extract_date_from_filename(filename):
    """파일명에서 날짜 추출"""
    # 10-23), 11-24), 12-01) 형식 찾기
    match = re.search(r'(\d{1,2})[:-](\d{1,2})\)', filename)
    if match:
        month = int(match.group(1))
        day = int(match.group(2))
        # 2024년으로 고정
        year = 2024
        return datetime(year, month, day, 9, 0, 0)
    return None

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

def determine_category(filepath):
    """파일 경로로 카테고리 결정"""
    path_str = str(filepath)

    # 01_python 디렉토리
    if '/01_python/' in path_str:
        return ['python']

    # 02_linux-network/추가학습 디렉토리
    elif '/02_linux-network/추가학습/' in path_str or '/02_linux-network/추가학습' in path_str:
        return ['linux-network-추가학습']

    # 02_linux-network 디렉토리 (추가학습 제외)
    elif '/02_linux-network/' in path_str:
        return ['linux-network']

    # 03_application-security 디렉토리
    elif '/03_application-security/' in path_str:
        return ['application-security']

    # 기본값
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

        # 카테고리 결정 (경로 기반)
        categories = determine_category(source_file)

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

        print(f"✓ Converted: {source_file.name} -> {new_filename} [{', '.join(categories)}]")
        return True

    except Exception as e:
        print(f"✗ Error converting {source_file.name}: {e}")
        return False

def main():
    base_dir = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/study")
    source_dir = base_dir / "SK_Rookies_Now"
    posts_dir = base_dir / "_posts"

    # 기존 _posts 디렉토리 백업
    posts_backup = base_dir / "_posts_backup_new"
    if posts_dir.exists():
        import shutil
        if posts_backup.exists():
            shutil.rmtree(posts_backup)
        shutil.copytree(posts_dir, posts_backup)
        print(f"✓ 기존 _posts 백업 완료: {posts_backup}")

    # _posts 디렉토리 비우기 (새로 생성)
    if posts_dir.exists():
        import shutil
        shutil.rmtree(posts_dir)
    posts_dir.mkdir(exist_ok=True)

    # 모든 .md 파일 찾기
    md_files = []
    for md_file in source_dir.rglob("*.md"):
        # STT 프롬프트 파일 제외
        if "프롬프트" not in md_file.name and ".DS_Store" not in md_file.name:
            md_files.append(md_file)

    # 날짜순 정렬
    md_files.sort(key=lambda x: x.name)

    print(f"\n총 {len(md_files)}개 파일 발견")
    print("=" * 60)

    converted_count = 0
    for md_file in md_files:
        if convert_file_to_post(md_file, posts_dir):
            converted_count += 1

    print("=" * 60)
    print(f"\n✓ 총 {converted_count}개 파일 변환 완료!")
    print(f"✓ 위치: {posts_dir}")

    # 카테고리별 통계
    print("\n카테고리별 통계:")
    categories_count = {}
    for post in posts_dir.glob("*.md"):
        with open(post, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'categories: \[(.*?)\]', content)
            if match:
                cats = [c.strip() for c in match.group(1).split(',')]
                for cat in cats:
                    categories_count[cat] = categories_count.get(cat, 0) + 1

    for cat, count in sorted(categories_count.items()):
        print(f"  - {cat}: {count}개")

if __name__ == "__main__":
    main()
