"""
add_faq_and_related.py
- Add visible FAQ accordion on index.html (before <footer>)
- Add related games cards on all game pages (before <footer>)
"""
import os

DOMAIN = 'https://geometrydash-lite2.poki2.online'

# (slug, display title, thumb_ext)
ALL_GAMES = [
    ('color-rush',              'Color Rush',                'jpg'),
    ('egg-dash',                'Egg Dash',                  'jpg'),
    ('geometry-dash-arrow',     'Geometry Dash Arrow',       'jpg'),
    ('geometry-dash-deadlocked','Geometry Dash Deadlocked',  'jpg'),
    ('geometry-dash-lite-2',    'Geometry Dash Lite 2',      'png'),
    ('geometry-dash-meltdown',  'Geometry Dash Meltdown',    'jpg'),
    ('geometry-dash',           'Geometry Dash',             'jpg'),
    ('geometry-rash',           'Geometry Rash',             'png'),
    ('geometry-vibes-x-ball',   'Geometry Vibes X-Ball',     'jpg'),
    ('golf-hit',                'Golf Hit',                  'jpg'),
]

# Homepage main game (not in ALL_GAMES since it's the home page itself)
HOME_GAME = ('geometry-dash-lite', 'Geometry Dash Lite', 'png')

FAQ_ITEMS = [
    ('Is this site free to use?',
     'Yes, all games on GD Lite 2 are completely free to play in your browser — no download, registration, or payment needed.'),
    ('Can I play games unblocked at school?',
     'Yes! All games are hosted to work unblocked on most school networks and Chromebooks. Just open the page and start playing.'),
    ('Do I need to install anything?',
     'No installation required. All games run directly in your web browser on any device — desktop, laptop, tablet, or Chromebook.'),
    ('What is GD Lite 2?',
     'GD Lite 2 is a free unblocked game collection featuring Geometry Dash variants and similar rhythm-platformer games, playable in your browser.'),
    ('How many games are available?',
     'GD Lite 2 currently hosts 10 games including Geometry Dash Meltdown, Geometry Dash Deadlocked, Geometry Dash Lite 2, Color Rush, Egg Dash, and more.'),
]

FAQ_SENTINEL = 'gd-faq-section'
RELATED_SENTINEL = 'gd-related-section'


def faq_html():
    items_html = ''
    for q, a in FAQ_ITEMS:
        items_html += f'''    <details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
      <summary itemprop="name">{q}</summary>
      <div itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
        <p itemprop="text">{a}</p>
      </div>
    </details>
'''
    return f'''
<!-- {FAQ_SENTINEL} -->
<section class="faq-section" itemscope itemtype="https://schema.org/FAQPage" style="max-width:900px;margin:40px auto;padding:0 20px">
  <h2 style="font-size:1.4rem;margin-bottom:16px">Frequently Asked Questions</h2>
{items_html.rstrip()}
</section>
<style>
.faq-section details.faq-item {{border:1px solid #ddd;border-radius:6px;margin-bottom:8px;padding:0}}
.faq-section details.faq-item summary {{cursor:pointer;font-weight:600;padding:12px 16px;list-style:none;user-select:none}}
.faq-section details.faq-item summary::-webkit-details-marker {{display:none}}
.faq-section details.faq-item[open] summary {{border-bottom:1px solid #eee}}
.faq-section details.faq-item > div {{padding:12px 16px}}
.faq-section details.faq-item > div p {{margin:0;line-height:1.6}}
</style>
'''


def related_html(current_slug):
    # Pick 4 games that are not the current slug
    picks = [g for g in ALL_GAMES if g[0] != current_slug][:4]
    # If we're on homepage (no slug arg), include from ALL_GAMES
    cards_html = ''
    for slug, title, ext in picks:
        href = f'{DOMAIN}/{slug}'
        thumb = f'data/image/game/{slug}/{slug}-m186x186.{ext}'
        cards_html += f'''    <a href="{href}" class="related-card" style="display:block;text-decoration:none;color:inherit">
      <img src="{thumb}" alt="{title} thumbnail" width="186" height="186" loading="lazy" style="width:100%;height:auto;border-radius:6px;display:block">
      <p style="margin:8px 0 0;font-size:.9rem;text-align:center;font-weight:600">{title}</p>
    </a>
'''
    return f'''
<!-- {RELATED_SENTINEL} -->
<section class="related-section" style="max-width:900px;margin:40px auto;padding:0 20px">
  <h2 style="font-size:1.4rem;margin-bottom:16px">You Might Also Like</h2>
  <div class="related-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:16px">
{cards_html.rstrip()}
  </div>
</section>
'''


# ── index.html ─────────────────────────────────────────────────────────
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

changed = False
if FAQ_SENTINEL not in content:
    content = content.replace('<footer>', faq_html() + '\n<footer>', 1)
    changed = True
    print('  index.html: FAQ injected')

if RELATED_SENTINEL not in content:
    content = content.replace('<footer>', related_html('') + '\n<footer>', 1)
    changed = True
    print('  index.html: Related games injected')

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

# ── Game pages ──────────────────────────────────────────────────────────
for slug, title, ext in ALL_GAMES:
    fname = f'{slug}.html'
    if not os.path.exists(fname):
        print(f'  SKIP (not found): {fname}')
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    if RELATED_SENTINEL not in content:
        content = content.replace('<footer>', related_html(slug) + '\n<footer>', 1)
        changed = True
        print(f'  {fname}: Related games injected')

    if changed:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)

print('Done.')
