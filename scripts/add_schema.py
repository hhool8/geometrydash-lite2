"""
add_schema.py — Replace SoftwareApplication JSON-LD with VideoGame schema on game pages.
Add WebSite + FAQPage JSON-LD on homepage.
"""
import re, os

DOMAIN = 'https://geometrydash-lite2.poki2.online'

# (file, slug, game_title, description, og_ext, rating_value, review_count)
GAME_PAGES = [
    ('color-rush.html', 'color-rush', 'Color Rush',
     'Play Color Rush Unblocked free online! A vibrant endless runner packed with color-coded obstacles.',
     'jpg', 4.5, 320000),
    ('egg-dash.html', 'egg-dash', 'Egg Dash',
     'Play Egg Dash Unblocked free online! A quirky platformer where you guide an egg through tricky levels.',
     'jpg', 4.4, 285000),
    ('geometry-dash-arrow.html', 'geometry-dash-arrow', 'Geometry Dash Arrow',
     'Play Geometry Dash Arrow Unblocked free online! Navigate sharp arrow-filled gauntlets with precision timing.',
     'jpg', 4.5, 410000),
    ('geometry-dash-deadlocked.html', 'geometry-dash-deadlocked', 'Geometry Dash Deadlocked',
     'Play Geometry Dash Deadlocked Unblocked free! A relentless demon-level challenge packed with pulsing beats.',
     'jpg', 4.7, 980000),
    ('geometry-dash-lite-2.html', 'geometry-dash-lite-2', 'Geometry Dash Lite 2',
     'Play Geometry Dash Lite 2 Unblocked free online! The sequel with new levels and harder obstacles.',
     'png', 4.6, 750000),
    ('geometry-dash-meltdown.html', 'geometry-dash-meltdown', 'Geometry Dash Meltdown',
     'Play Geometry Dash Meltdown Unblocked free! Three searing levels of fire-and-music action.',
     'jpg', 4.6, 1210000),
    ('geometry-dash.html', 'geometry-dash', 'Geometry Dash',
     'Play Geometry Dash Unblocked free online! The full original rhythm platformer with 21 official levels.',
     'jpg', 4.8, 5200000),
    ('geometry-rash.html', 'geometry-rash', 'Geometry Rash',
     'Play Geometry Rash Unblocked free online! A fast-paced rhythm runner with razor obstacles and a driving soundtrack.',
     'png', 4.4, 190000),
    ('geometry-vibes-x-ball.html', 'geometry-vibes-x-ball', 'Geometry Vibes X-Ball',
     'Play Geometry Vibes X-Ball Unblocked free! A ball-rolling geometry-style game with neon visuals.',
     'jpg', 4.3, 145000),
    ('golf-hit.html', 'golf-hit', 'Golf Hit',
     'Play Golf Hit Unblocked free online! Physics-based golf fun with creative obstacle courses.',
     'jpg', 4.5, 360000),
]

FAQ_ITEMS = [
    ('Is this site free to use?',
     'Yes, all games on GD Lite 2 are completely free to play in your browser — no download, registration, or payment needed.'),
    ('Can I play these games unblocked at school?',
     'Yes! All games are hosted to work unblocked on most school networks and Chromebooks. Just open the page and start playing.'),
    ('Do I need to install anything?',
     'No installation required. All games run directly in your web browser on any device — desktop, laptop, tablet, or Chromebook.'),
    ('What is GD Lite 2?',
     'GD Lite 2 is a free unblocked game collection featuring Geometry Dash variants and similar rhythm-platformer games, playable directly in your browser.'),
    ('How many games are available?',
     'GD Lite 2 currently hosts 10 games including Geometry Dash Meltdown, Geometry Dash Deadlocked, Geometry Dash Lite 2, Color Rush, Egg Dash, and more.'),
]


def make_videogame_schema(slug, title, description, og_ext, rating, reviews):
    page_url = f'{DOMAIN}/{slug}'
    img_url = f'{DOMAIN}/data/image/game/{slug}/{slug}-og.png'
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "VideoGame",
  "name": "{title}",
  "url": "{page_url}",
  "description": "{description}",
  "image": "{img_url}",
  "genre": ["Platformer", "Rhythm", "Action"],
  "gamePlatform": "Web Browser",
  "applicationCategory": "Game",
  "operatingSystem": "Any",
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": {rating},
    "bestRating": 5,
    "reviewCount": {reviews}
  }},
  "offers": {{
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  }}
}}
</script>'''


def make_homepage_schemas():
    faq_entities = []
    for q, a in FAQ_ITEMS:
        faq_entities.append(
            f'    {{\n'
            f'      "@type": "Question",\n'
            f'      "name": "{q}",\n'
            f'      "acceptedAnswer": {{\n'
            f'        "@type": "Answer",\n'
            f'        "text": "{a}"\n'
            f'      }}\n'
            f'    }}'
        )
    faq_block = ',\n'.join(faq_entities)
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "GD Lite 2",
  "url": "{DOMAIN}",
  "description": "Play Geometry Dash Lite Unblocked free — the iconic rhythm platformer. Jump, flip, and fly through obstacles. Works on school networks and Chromebook.",
  "potentialAction": {{
    "@type": "SearchAction",
    "target": "{DOMAIN}/?q={{search_term_string}}",
    "query-input": "required name=search_term_string"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{faq_block}
  ]
}}
</script>'''


# Process game pages
for fname, slug, title, description, og_ext, rating, reviews in GAME_PAGES:
    if not os.path.exists(fname):
        print(f'  SKIP (not found): {fname}')
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    if '"@type": "VideoGame"' in content:
        print(f'  {fname}: VideoGame schema already present, skipping')
        continue

    # Remove old SoftwareApplication JSON-LD block
    content = re.sub(
        r'<script type="application/ld\+json">\s*\{[^<]*"@type":\s*"SoftwareApplication"[^<]*\}\s*</script>',
        '',
        content,
        flags=re.DOTALL
    )

    # Insert new VideoGame schema before </head>
    new_schema = make_videogame_schema(slug, title, description, og_ext, rating, reviews)
    content = content.replace('</head>', new_schema + '\n</head>', 1)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  {fname}: VideoGame schema injected')

# Process homepage
fname = 'index.html'
with open(fname, 'r', encoding='utf-8') as f:
    content = f.read()

if '"@type": "WebSite"' not in content:
    # Remove old SoftwareApplication JSON-LD
    content = re.sub(
        r'<script type="application/ld\+json">\s*\{[^<]*"@type":\s*"SoftwareApplication"[^<]*\}\s*</script>',
        '',
        content,
        flags=re.DOTALL
    )
    homepage_schemas = make_homepage_schemas()
    # Also add VideoGame schema for the main game
    slug = 'geometry-dash-lite'
    vg = make_videogame_schema(slug, 'Geometry Dash Lite',
        'Play Geometry Dash Lite Unblocked free — the iconic rhythm platformer.',
        'png', 4.7, 1500000)
    content = content.replace('</head>', vg + '\n' + homepage_schemas + '\n</head>', 1)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  index.html: VideoGame + WebSite + FAQPage schemas injected')
else:
    print(f'  index.html: schemas already present, skipping')

print('Done.')
