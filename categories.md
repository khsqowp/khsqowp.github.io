---
title: "Posts by Category"
layout: archive
permalink: /categories/
author_profile: true
---

{% for category in site.categories %}
  <h2 id="{{ category[0] | slugify }}" class="archive__subtitle">{{ category[0] }}</h2>
  {% for post in category[1] %}
    {% include archive-single.html %}
  {% endfor %}
{% endfor %}