"""
add_og_tags.py — Inject canonical, og:*, twitter:* meta tags into all pages.
Also rewrites <title> and meta description to be unique and keyword-rich.
"""
import re, os

DOMAIN = 'https://geometrydash-lite2.poki2.online'
GA4_ID = 'G-THHTQLKSDJ'

# (file, slug_for_url, new_title, new_description, thumb_ext)
PAGES = [
    (
        'index.html',
        '',
        'Geometry Dash Lite Unblocked – Play Free Online | GD Lite 2',
        'Play Geometry Dash Lite Unblocked free — the iconic rhythm platformer. Jump, flip, and fly through obstacles. Works on school networks and Chromebook.',
        'geometry-dash-lite', 'png',
    ),
    (
        'color-rush.html',
        'color-rush',
        'Color Rush Unblocked – Play Free Online',
        'Play Color Rush Unblocked free online! A vibrant endless runner packed with color-coded obstacles. Match, dash, and survive every wave.',
        'color-rush', 'jpg',
    ),
    (
        'egg-dash.html',
        'egg-dash',
        'Egg Dash Unblocked – Play Free Online',
        'Play Egg Dash Unblocked free online! A quirky platformer where you guide an egg through tricky levels. No download needed — fun for all ages.',
        'egg-dash', 'jpg',
    ),
    (
        'geometry-dash-arrow.html',
        'geometry-dash-arrow',
        'Geometry Dash Arrow Unblocked – Play Free Online',
        'Play Geometry Dash Arrow Unblocked free online! Navigate sharp arrow-filled gauntlets with precision timing. Dodge every spike and conquer the level.',
        'geometry-dash-arrow', 'jpg',
    ),
    (
        'geometry-dash-deadlocked.html',
        'geometry-dash-deadlocked',
        'Geometry Dash Deadlocked Unblocked – Play Free Online',
        'Play Geometry Dash Deadlocked Unblocked free! A relentless demon-level challenge packed with death traps and pulsing beats. Can you survive?',
        'geometry-dash-deadlocked', 'jpg',
    ),
    (
        'geometry-dash-lite-2.html',
        'geometry-dash-lite-2',
        'Geometry Dash Lite 2 Unblocked – Play Free Online',
        'Play Geometry Dash Lite 2 Unblocked free online! The sequel sensation with new levels and harder obstacles. Rhythm-based platforming at its best.',
        'geometry-dash-lite-2', 'png',
    ),
    (
        'geometry-dash-meltdown.html',
        'geometry-dash-meltdown',
        'Geometry Dash Meltdown Unblocked – Play Free Online',
        'Play Geometry Dash Meltdown Unblocked free! Three searing levels — Molten Rock, Nock Em, and Power Trip. Pure fire-and-music action.',
        'geometry-dash-meltdown', 'jpg',
    ),
    (
        'geometry-dash.html',
        'geometry-dash',
        'Geometry Dash Unblocked – Play Free Online',
        'Play Geometry Dash Unblocked free online! The full original rhythm platformer — tap to jump, fly, and flip through 21 official levels. No install needed.',
        'geometry-dash', 'jpg',
    ),
    (
        'geometry-rash.html',
        'geometry-rash',
        'Geometry Rash Unblocked – Play Free Online',
        'Play Geometry Rash Unblocked free online! A fast-paced rhythm runner with razor obstacles and a driving soundtrack. React fast or restart.',
        'geometry-rash', 'png',
    ),
    (
        'geometry-vibes-x-ball.html',
        'geometry-vibes-x-ball',
        'Geometry Vibes X-Ball Unblocked – Play Free Online',
        'Play Geometry Vibes X-Ball Unblocked free! A ball-rolling geometry-style game with neon visuals and reactive music. Test your reflexes now.',
        'geometry-vibes-x-ball', 'jpg',
    ),
    (
        'golf-hit.html',
        'golf-hit',
        'Golf Hit Unblocked – Play Free Online',
        'Play Golf Hit Unblocked free online! Aim, drag, and smash the ball through creative obstacle courses. Physics-based golf fun with no download needed.',
        'golf-hit', 'jpg',
    ),
]


def make_og_block(page_url, title, description, og_image_url, thumb_img_url):
    """Return the canonical + OG + Twitter meta block as a string."""
    return (
        f'    <link rel="canonical" href="{page_url}">\n'
        f'    <link rel="image_src" href="{og_image_url}">\n'
        f'    <meta property="og:type" content="website">\n'
        f'    <meta property="og:url" content="{page_url}">\n'
        f'    <meta property="og:title" content="{title}">\n'
        f'    <meta property="og:description" content="{description}">\n'
        f'    <meta property="og:image" content="{og_image_url}">\n'
        f'    <meta property="og:image:width" content="1200">\n'
        f'    <meta property="og:image:height" content="630">\n'
        f'    <meta property="og:site_name" content="GD Lite 2">\n'
        f'    <meta name="twitter:card" content="summary_large_image">\n'
        f'    <meta name="twitter:site" content="@geometrydashlite2">\n'
        f'    <meta name="twitter:title" content="{title}">\n'
        f'    <meta name="twitter:description" content="{description}">\n'
        f'    <meta name="twitter:image" content="{thumb_img_url}">\n'
    )


for fname, url_slug, new_title, new_desc, img_slug, img_ext in PAGES:
    if not os.path.exists(fname):
        print(f'  SKIP (not found): {fname}')
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already processed
    if 'og:title' in content:
        print(f'  {fname}: already has og:title, skipping')
        continue

    # Build URLs
    if url_slug:
        page_url = f'{DOMAIN}/{url_slug}'
    else:
        page_url = DOMAIN

    og_image_url = f'{DOMAIN}/data/image/game/{img_slug}/{img_slug}-og.png'
    twitter_image_url = f'{DOMAIN}/data/image/game/{img_slug}/{img_slug}-m186x186.{img_ext}'

    # 1. Replace <title>
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content)

    # 2. Replace meta description
    content = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{new_desc}"',
        content
    )

    # 3. Insert OG block just before </head>
    og_block = make_og_block(page_url, new_title, new_desc, og_image_url, twitter_image_url)
    content = content.replace('</head>', og_block + '</head>', 1)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  {fname}: title + description + OG + twitter injected')

print('Done.')
