---
layout: default
---

<header>
  <h1 id="top">~ Christmas Singalong! ~</h1>

  <nav>
    <ul>
    {% assign sorted_songs = site.songs | sort: 'title' %}
    {% for song in sorted_songs %}
      <li><a href="#{{ song.title | slugify }}">{{ song.title }}</a></li>
    {% endfor %}
    </ul>
  </nav>

  <p><button onclick="darkMode()">&#x1F4A1; Dark/Light Mode</button></p>
</header>

<main>
  <hr>
  {% for song in sorted_songs %}
  <article class="song" id="{{ song.title | slugify }}">
    <h2 class="song-title">{{ song.title }}</h2>
    {{ song.content }}
    <p><a href="#">Back to Top ^</a></p>
    <hr>
  </article>
  {% endfor %}
</main>
