"""
gen_game_og_covers.py — Generate 1200x630 og covers for all 10 game pages.
Output: data/image/game/{slug}/{slug}-og.png
"""
from PIL import Image, ImageDraw, ImageFont
import os

DOMAIN = 'geometrydash-lite2.poki2.online'
W, H = 1200, 630
BG_TOP    = (20, 60, 20)
BG_BOTTOM = (10, 20, 40)
ACCENT    = (50, 205, 50)

GAMES = [
    ('geometry-dash-lite',      'Geometry Dash Lite',      'png'),
    ('color-rush',              'Color Rush',              'jpg'),
    ('egg-dash',                'Egg Dash',                'jpg'),
    ('geometry-dash-arrow',     'Geometry Dash Arrow',     'jpg'),
    ('geometry-dash-deadlocked','Geometry Dash Deadlocked','jpg'),
    ('geometry-dash-lite-2',    'Geometry Dash Lite 2',    'png'),
    ('geometry-dash-meltdown',  'Geometry Dash Meltdown',  'jpg'),
    ('geometry-dash',           'Geometry Dash',           'jpg'),
    ('geometry-rash',           'Geometry Rash',           'png'),
    ('geometry-vibes-x-ball',   'Geometry Vibes X-Ball',   'jpg'),
    ('golf-hit',                'Golf Hit',                'jpg'),
]

try:
    font_title = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 80)
    font_sub   = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 42)
    font_url   = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 30)
except Exception:
    font_title = ImageFont.load_default()
    font_sub   = font_title
    font_url   = font_title


def make_og_cover(slug, title, thumb_ext):
    img = Image.new('RGB', (W, H), BG_BOTTOM)
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        r = int(BG_TOP[0] * (1 - t) + BG_BOTTOM[0] * t)
        g = int(BG_TOP[1] * (1 - t) + BG_BOTTOM[1] * t)
        b = int(BG_TOP[2] * (1 - t) + BG_BOTTOM[2] * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    draw.ellipse([(1050, -80), (1250, 120)], outline=ACCENT, width=4)

    thumb_path = f'data/image/game/{slug}/{slug}-m186x186.{thumb_ext}'
    if os.path.exists(thumb_path):
        conv = 'RGBA' if thumb_ext == 'png' else 'RGB'
        thumb = Image.open(thumb_path).convert('RGBA')
        thumb = thumb.resize((230, 230), Image.LANCZOS)
        # Use alpha_composite for png
        base = img.convert('RGBA')
        base.paste(thumb, (900, 200), thumb)
        img = base.convert('RGB')
        draw = ImageDraw.Draw(img)

    # Wrap title if long
    words = title.split()
    lines = []
    line = ''
    for w in words:
        test = (line + ' ' + w).strip()
        try:
            tw = font_title.getlength(test)
        except Exception:
            tw = len(test) * 40
        if tw > 750 and line:
            lines.append(line)
            line = w
        else:
            line = test
    lines.append(line)

    y_start = 200
    if len(lines) > 1:
        y_start = 160
    for ln in lines:
        draw.text((80, y_start), ln, font=font_title, fill=(255, 255, 255))
        y_start += 95

    draw.text((80, y_start + 10), 'Play Unblocked Free Online', font=font_sub, fill=ACCENT)
    draw.text((80, 580), DOMAIN, font=font_url, fill=(180, 180, 180))

    out_path = f'data/image/game/{slug}/{slug}-og.png'
    img.save(out_path, 'PNG', optimize=True)
    return out_path


print('Generating 1200x630 og covers...')
for slug, title, ext in GAMES:
    out = make_og_cover(slug, title, ext)
    print(f'  Generated {out}')
print('Done.')
