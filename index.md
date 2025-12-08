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
  <div class="main-content">
    {% for song in sorted_songs %}
    <article class="song">
      <h2 class="song-title" id="{{ song.title | slugify }}">{{ song.title }}</h2>
      {{ song.content }}
      <p><a href="#">Back to Top ^</a></p>
      <hr>
    </article>
    {% endfor %}
  </div>
</main>
