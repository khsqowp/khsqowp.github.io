---
layout: home
author_profile: true
header:
  overlay_image: https://images.unsplash.com/photo-1550751827-4bd374c3f58b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80
  overlay_filter: 0.5
excerpt: "EveryDAI: Security & Development Learning Log"
---

## 👋 Welcome to 에브리DAI

안녕하세요, 보안과 개발을 공부하며 성장하는 공간 **에브리DAI**입니다.

---

## 📚 Recent Notes

{% for post in site.posts limit:5 %}
* [{{ post.title }}]({{ post.url }}) <span style="font-size:0.8em; color:gray;">{{ post.date | date: "%Y-%m-%d" }}</span>
{% endfor %}