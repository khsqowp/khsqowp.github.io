---
title: "Library Structure"
layout: archive
permalink: /categories/
author_profile: true
sidebar:
  nav: "docs"
---

<div class="entries-list">
  {% assign categories_list = site.categories %}
  {% if categories_list.first[0] == null %}
    {% for category in categories_list %}
      <section id="{{ category | slugify }}" class="taxonomy__section">
        <h2 class="archive__subtitle">
          <i class="fas fa-folder-open"></i> {{ category }} 
          <span class="taxonomy__count">({{ site.categories[category].size }})</span>
        </h2>
        <div class="entries-list">
          {% for post in site.categories[category] %}
            <div class="list__item">
              <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
                <h3 class="archive__item-title" itemprop="headline" style="font-size: 0.9em; margin-top: 0.5em;">
                  <a href="{{ post.url | relative_url }}" rel="permalink">
                    <i class="fas fa-file-alt" style="color: #7a8288; margin-right: 5px;"></i>
                    {{ post.title }}
                  </a>
                </h3>
                <span class="page__meta" style="font-size: 0.7em;">
                  <i class="far fa-calendar-alt" aria-hidden="true"></i> {{ post.date | date: "%Y-%m-%d" }}
                </span>
              </article>
            </div>
          {% endfor %}
        </div>
      </section>
      <hr style="margin: 2em 0;">
    {% endfor %}
  {% else %}
    {% for category in categories_list %}
      <section id="{{ category[0] | slugify }}" class="taxonomy__section">
        <h2 class="archive__subtitle" style="border-bottom: 2px solid #f2f3f3; padding-bottom: 10px;">
          <i class="fas fa-folder-open" style="color: #6c757d;"></i> {{ category[0] }}
          <span class="taxonomy__count" style="font-size: 0.6em; vertical-align: middle; background: #e9ecef; color: #495057; padding: 2px 8px; border-radius: 10px;">{{ category[1].size }} files</span>
        </h2>
        <ul style="list-style: none; padding-left: 20px; border-left: 2px solid #f8f9fa;">
          {% for post in category[1] %}
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
