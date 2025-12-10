---
layout: default
---

<header>
  <h1 id="top">~ Christmas Singalong! ~</h1>

  <div class="tabs">
    <button class="tab-button active" onclick="showTab('alphabetical')">Alphabetical</button>
    <button class="tab-button" onclick="showTab('category')">By Category</button>
  </div>

  <nav id="alphabetical-nav" class="tab-content">
    <ul>
    {% assign sorted_songs = site.songs | sort: 'title' %}
    {% for song in sorted_songs %}
      <li><a href="#{{ song.title | slugify }}">{{ song.title }}</a></li>
    {% endfor %}
    </ul>
  </nav>

  <nav id="category-nav" class="tab-content" style="display: none;">
    {% assign categorized_songs = site.songs | where_exp: "item", "item.category != nil" | where_exp: "item", "item.category != ''" %}
    {% assign songs_by_category = categorized_songs | group_by: "category" | sort: "name" %}

    {% for category in songs_by_category %}
    <section>
      <h3>{{ category.name | capitalize }}</h3>
      <ul>
        {% assign category_songs = category.items | sort: "title" %}
        {% for song in category_songs %}
          <li><a href="#{{ song.title | slugify }}">{{ song.title }}</a></li>
        {% endfor %}
      </ul>
    </section>
    {% endfor %}

    {% assign uncategorized = site.songs | where_exp: "item", "item.category == nil" %}
    {% if uncategorized.size > 0 %}
    <section>
      <h3>Uncategorized</h3>
      <ul>
        {% assign sorted_uncategorized = uncategorized | sort: "title" %}
        {% for song in sorted_uncategorized %}
          <li><a href="#{{ song.title | slugify }}">{{ song.title }}</a></li>
        {% endfor %}
      </ul>
    </section>
    {% endif %}
  </nav>

  <p><button onclick="darkMode()">&#x1F4A1; Dark/Light Mode</button></p>
</header>

<main>
  {% for song in sorted_songs %}
  <hr>
  <article class="song" id="{{ song.title | slugify }}">
    <h2 class="song-title">{{ song.title }}</h2>
    {{ song.content }}
    <p><a href="#">Back to Top ^</a></p>
  </article>
  {% endfor %}
</main>
