---
title: "Posts by Tag"
layout: archive
permalink: /tags/
author_profile: true
---

{% for tag in site.tags %}
  <h2 id="{{ tag[0] | slugify }}" class="archive__subtitle">{{ tag[0] }}</h2>
  {% for post in tag[1] %}
    {% include archive-single.html %}
  {% endfor %}
{% endfor %}