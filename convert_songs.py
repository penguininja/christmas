#!/usr/bin/env python3
"""
Convert old HTML song format to new markdown format.
Usage: python convert_songs.py <input_file.html> <output_directory>
"""

import re
import sys
from pathlib import Path


def slugify(text):
    """Convert text to slug format."""
    return text.lower().replace(' ', '-').replace("'", '')


def extract_title_from_id(song_id):
    """Convert slug ID back to title."""
    return song_id.replace('-', ' ').title()


def convert_html_to_markdown(html_content):
    """Convert HTML song sections to individual markdown files."""
    # Split by sections
    sections = re.findall(r'<section class="song">.*?</section>', html_content, re.DOTALL)

    songs = []

    for section in sections:
        # Extract title from h2
        title_match = re.search(r'<h2 class="song-title" id="([^"]+)">([^<]+)</h2>', section)
        if not title_match:
            continue

        song_id = title_match.group(1)
        title = title_match.group(2)

        # Start markdown content
        md_content = f'---\ntitle: "{title}"\n---\n\n'

        # Extract all h3 sections and their content
        # Find all h3 tags and the p tags that follow them
        parts = re.findall(r'<h3 class="section-title">([^<]+)</h3>\s*<p>(.*?)</p>', section, re.DOTALL)

        for section_title, lyrics in parts:
            # Add section header
            md_content += f'## {section_title}\n'

            # Convert <br/> to line breaks and clean up
            lyrics = re.sub(r'<br\s*/?>\s*', '\n', lyrics)
            # Remove extra whitespace
            lyrics = re.sub(r'\n\s+', '\n', lyrics)
            lyrics = lyrics.strip()

            md_content += f'{lyrics}\n\n'

        songs.append({
            'title': title,
            'slug': song_id,
            'content': md_content
        })

    return songs


def main():
    if len(sys.argv) != 3:
        print("Usage: python convert_songs.py <input_file.html> <output_directory>")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    if not input_file.exists():
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Read HTML content
    html_content = input_file.read_text()

    # Convert to markdown
    songs = convert_html_to_markdown(html_content)

    # Write individual markdown files
    for song in songs:
        output_file = output_dir / f"{song['slug']}.md"
        output_file.write_text(song['content'])
        print(f"Created: {output_file}")

    print(f"\nConverted {len(songs)} songs successfully!")


if __name__ == '__main__':
    main()
