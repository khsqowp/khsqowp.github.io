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

---

## 📂 Categories

{% for category in site.categories %}
  <h3 class="archive__subtitle"><i class="fas fa-folder-open"></i> {{ category[0] }}</h3>
  <ul style="list-style-type: none; padding-left: 0;">
    {% for post in category[1] limit:3 %}
      <li style="margin-bottom: 0.5em; padding-left: 1em; border-left: 3px solid #eee;">
        <a href="{{ post.url }}" style="text-decoration: none;">{{ post.title }}</a>
      </li>
    {% endfor %}
    {% if category[1].size > 3 %}
      <li style="padding-left: 1em;"><a href="/categories/#{{ category[0] | slugify }}" style="font-size: 0.9em; color: #888;">More posts in {{ category[0] }}...</a></li>
    {% endif %}
  </ul>
{% endfor %}