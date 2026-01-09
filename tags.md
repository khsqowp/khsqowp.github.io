---
title: "Posts by Tag"
layout: archive
permalink: /tags/
author_profile: true
---

<div class="entries-list">
  {% assign tags_list = site.tags %}
  {% if tags_list.first[0] == null %}
    {% for tag in tags_list %}
      <section id="{{ tag | slugify }}" class="taxonomy__section">
        <h2 class="archive__subtitle" style="border-bottom: 2px solid #f2f3f3; padding-bottom: 10px;">
          <i class="fas fa-tag" style="color: #6c757d;"></i> {{ tag }}
          <span class="taxonomy__count" style="font-size: 0.6em; vertical-align: middle; background: #e9ecef; color: #495057; padding: 2px 8px; border-radius: 10px;">{{ site.tags[tag].size }}</span>
        </h2>
        <ul style="list-style: none; padding-left: 20px; border-left: 2px solid #f8f9fa;">
          {% for post in site.tags[tag] %}
            <li style="margin-bottom: 8px;">
              <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #495057;">
                <i class="fas fa-file-alt" style="color: #adb5bd; margin-right: 8px;"></i>
                {{ post.title }}
              </a>
              <span style="font-size: 0.7em; color: #adb5bd; margin-left: 10px;">{{ post.date | date: "%Y-%m-%d" }}</span>
            </li>
          {% endfor %}
        </ul>
      </section>
      <div style="height: 30px;"></div>
    {% endfor %}
  {% else %}
    {% for tag in tags_list %}
      <section id="{{ tag[0] | slugify }}" class="taxonomy__section">
        <h2 class="archive__subtitle" style="border-bottom: 2px solid #f2f3f3; padding-bottom: 10px;">
          <i class="fas fa-tag" style="color: #6c757d;"></i> {{ tag[0] }}
          <span class="taxonomy__count" style="font-size: 0.6em; vertical-align: middle; background: #e9ecef; color: #495057; padding: 2px 8px; border-radius: 10px;">{{ tag[1].size }}</span>
        </h2>
        <ul style="list-style: none; padding-left: 20px; border-left: 2px solid #f8f9fa;">
          {% for post in tag[1] %}
            <li style="margin-bottom: 8px;">
              <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #495057;">
                <i class="fas fa-file-alt" style="color: #adb5bd; margin-right: 8px;"></i>
                {{ post.title }}
              </a>
              <span style="font-size: 0.7em; color: #adb5bd; margin-left: 10px;">{{ post.date | date: "%Y-%m-%d" }}</span>
            </li>
          {% endfor %}
        </ul>
      </section>
      <div style="height: 30px;"></div>
    {% endfor %}
  {% endif %}
</div>
