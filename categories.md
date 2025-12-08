---
layout: default
title: Categories
permalink: /categories/
---

<header>
  <h1>Song Categories</h1>
  <p><a href="/">← Back to All Songs</a></p>
</header>

<main>
  {% assign categorized_songs = site.songs | where_exp: "item", "item.category != nil" | where_exp: "item", "item.category != ''" %}
  {% assign songs_by_category = categorized_songs | group_by: "category" | sort: "name" %}

  {% for category in songs_by_category %}
  <section>
    <h2>{{ category.name | capitalize }}</h2>
    <ul>
      {% assign category_songs = category.items | sort: "title" %}
      {% for song in category_songs %}
        <li><a href="/#{{ song.title | downcase | replace: ' ', '-' | replace: "'", '' }}">{{ song.title }}</a></li>
      {% endfor %}
    </ul>
  </section>
  {% endfor %}

  {% assign uncategorized = site.songs | where_exp: "item", "item.category == nil" %}
  {% if uncategorized.size > 0 %}
  <section>
    <h2>Uncategorized</h2>
    <ul>
      {% assign sorted_uncategorized = uncategorized | sort: "title" %}
      {% for song in sorted_uncategorized %}
        <li><a href="/#{{ song.title | downcase | replace: ' ', '-' | replace: "'", '' }}">{{ song.title }}</a></li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}
</main>
