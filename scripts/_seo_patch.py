import os, re

game_pages = [
    'color-rush.html','egg-dash.html','geometry-dash-arrow.html',
    'geometry-dash-deadlocked.html','geometry-dash-lite-2.html',
    'geometry-dash-meltdown.html','geometry-dash.html','geometry-rash.html',
    'geometry-vibes-x-ball.html','golf-hit.html'
]
all_pages = game_pages + ['index.html','about.html','privacy.html','404.html']

favicon_extra = (
    '\n    <link rel="apple-touch-icon" sizes="180x180" href="/rs/imgs/geometry-dash-lite.png">'
    '\n    <link rel="icon" type="image/png" sizes="32x32" href="/rs/imgs/geometry-dash-lite.png">'
    '\n    <link rel="icon" type="image/png" sizes="16x16" href="/rs/imgs/geometry-dash-lite.png">'
)
icon_pattern = re.compile(r'(<link rel="icon" href="[^"]+">)')
preload_str = '<link rel="preload" href="rs/css/all.css" as="style">\n    '
css_str = '<link rel="stylesheet" type="text/css" href="rs/css/all.css">'
rating_str = '\n    <meta name="rating" content="General">'
manifest_str = '\n    <link rel="manifest" href="/manifest.json">'
theme_pattern = re.compile(r'(<meta name="theme-color" content="[^"]+">)')

for fname in all_pages:
    content = open(fname).read()
    original = content

    # Task 4: og:type -> article on game pages
    if fname in game_pages:
        content = content.replace(
            '<meta property="og:type" content="website">',
            '<meta property="og:type" content="article">'
        )

    # Task 5: favicon multi-size
    if 'apple-touch-icon' not in content:
        content = icon_pattern.sub(r'\1' + favicon_extra, content, count=1)

    # Task 6: preload all.css
    if 'rel="preload"' not in content and css_str in content:
        content = content.replace(css_str, preload_str + css_str)

    # Task 7: meta rating=General
    if 'name="rating"' not in content:
        content = theme_pattern.sub(r'\1' + rating_str, content, count=1)

    # Task 10: manifest link
    if 'manifest.json' not in content:
        content = theme_pattern.sub(r'\1' + manifest_str, content, count=1)

    if content != original:
        open(fname, 'w').write(content)
        print('patched:', fname)
    else:
        print('unchanged:', fname)
