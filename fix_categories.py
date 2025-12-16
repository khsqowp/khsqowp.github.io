#!/usr/bin/env python3
"""
카테고리를 폴더 구조 기반으로 수정하는 스크립트
"""

import os
import re
from pathlib import Path

# 카테고리 매핑 (원본 폴더명 -> URL safe 카테고리)
CATEGORY_MAPPING = {
    "1_AI_기본_역량": "ai-fundamentals",
    "1-1_파이썬": "python",
    "1-2_머신러닝_딥러닝": "ml-dl",
    "2_보안_기본_역량": "security-fundamentals",
    "2-1_네트워크_보안": "network-security",
    "2-2_클라우드_보안": "cloud-security",
    "2-3_애플리케이션_보안": "application-security",
    "2-4_개인정보보호": "privacy",
    "3_응용_기술_심화": "advanced-applications",
    "3-1_AI_보안관제_및_로그_분석": "ai-soc-logs",
    "3-2_악성코드_분석_및_대응": "malware-analysis",
    "3-3_취약점_진단_및_모의해킹": "pentesting",
    "4_실무_프로젝트": "projects",
    "4-1_최종_프로젝트": "final-project",
}

# 카테고리 한글명 매핑
CATEGORY_NAMES = {
    "ai-fundamentals": "AI 기본 역량",
    "python": "파이썬",
    "ml-dl": "머신러닝/딥러닝",
    "security-fundamentals": "보안 기본 역량",
    "network-security": "네트워크 보안",
    "cloud-security": "클라우드 보안",
    "application-security": "애플리케이션 보안",
    "privacy": "개인정보보호",
    "advanced-applications": "응용 기술 심화",
    "ai-soc-logs": "AI 보안관제 및 로그분석",
    "malware-analysis": "악성코드 분석 및 대응",
    "pentesting": "취약점 진단 및 모의해킹",
    "projects": "실무 프로젝트",
    "final-project": "최종 프로젝트",
}

def extract_original_path_from_content(content):
    """원본 파일 경로에서 카테고리 정보 추출"""
    # 파일명에서 카테고리 추정
    categories = []

    if "파이썬" in content[:500]:
        categories = ["ai-fundamentals", "python"]
    elif "머신러닝" in content[:500] or "딥러닝" in content[:500]:
        categories = ["ai-fundamentals", "ml-dl"]
    elif "네트워크" in content[:500] and "보안" in content[:500]:
        categories = ["security-fundamentals", "network-security"]
    elif "클라우드" in content[:500]:
        categories = ["security-fundamentals", "cloud-security"]
    elif "웹" in content[:500] or "OWASP" in content[:500] or "시큐어 코딩" in content[:500]:
        categories = ["security-fundamentals", "application-security"]
    elif "개인정보" in content[:500]:
        categories = ["security-fundamentals", "privacy"]
    elif "SIEM" in content[:500] or "로그" in content[:500]:
        categories = ["advanced-applications", "ai-soc-logs"]
    elif "악성코드" in content[:500] or "리버스" in content[:500] or "Yara" in content[:500]:
        categories = ["advanced-applications", "malware-analysis"]
    elif "모의해킹" in content[:500] or "취약점" in content[:500]:
        categories = ["advanced-applications", "pentesting"]
    elif "프로젝트" in content[:500]:
        if "최종" in content[:500] or "발표" in content[:500] or "멘토링" in content[:500]:
            categories = ["projects", "final-project"]
        else:
            categories = ["projects"]

    return categories

def fix_post_category(file_path):
    """포스트의 카테고리 수정"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # frontmatter 추출
    if not content.startswith('---'):
        return False

    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    frontmatter = parts[1]
    body = parts[2]

    # 카테고리 추출
    categories = extract_original_path_from_content(body)

    if not categories:
        # 기본 카테고리
        categories = ["general"]

    # frontmatter에서 기존 categories 라인 찾아서 교체
    lines = frontmatter.split('\n')
    new_lines = []

    for line in lines:
        if line.startswith('categories:'):
            # 새 카테고리로 교체
            new_lines.append(f'categories: [{", ".join(categories)}]')
        else:
            new_lines.append(line)

    # 새 컨텐츠 생성
    new_content = '---\n' + '\n'.join(new_lines) + '\n---' + body

    # 파일 쓰기
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    posts_dir = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/study/_posts")

    fixed_count = 0
    for post_file in posts_dir.glob("*.md"):
        try:
            if fix_post_category(post_file):
                print(f"✓ Fixed: {post_file.name}")
                fixed_count += 1
        except Exception as e:
            print(f"✗ Error fixing {post_file.name}: {e}")

    print(f"\n총 {fixed_count}개 포스트의 카테고리를 수정했습니다!")

    # 카테고리 페이지 생성
    print("\n카테고리 페이지를 생성합니다...")
    create_category_pages()

def create_category_pages():
    """각 카테고리별 페이지 생성"""
    base_dir = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/study")
    category_dir = base_dir / "category"
    category_dir.mkdir(exist_ok=True)

    for cat_slug, cat_name in CATEGORY_NAMES.items():
        cat_file = category_dir / f"{cat_slug}.md"
        content = f"""---
layout: category
title: {cat_name}
category: {cat_slug}
permalink: /category/{cat_slug}/
---
"""
        with open(cat_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created category page: {cat_slug}.md")

if __name__ == "__main__":
    main()
