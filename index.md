---
layout: default
---

<h1 id="top">~ Christmas Singalong! ~</h1>

<ul>
{% assign sorted_songs = site.songs | sort: 'title' %}
{% for song in sorted_songs %}
  <li><a href="#{{ song.title | slugify }}">{{ song.title }}</a></li>
{% endfor %}
</ul>
<p><button onclick="darkMode()">&#x1F4A1; Dark/Light Mode</button></p>

{% for song in sorted_songs %}
<section class="song">
  <h2 class="song-title" id="{{ song.title | slugify }}">{{ song.title }}</h2>
  <div class="song-content">
    {{ song.content }}
  </div>
  <p><a href="#">Back to Top ^</a></p>
</section>
{% endfor %}

<style>
.song-content h2 {
  font-size: 1.2em;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
  font-weight: normal;
  font-style: italic;
}
</style>
