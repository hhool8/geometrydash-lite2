"""
gen_og_cover.py — Generate homepage og-cover.png (1200x630).
"""
from PIL import Image, ImageDraw, ImageFont
import os

DOMAIN = 'geometrydash-lite2.poki2.online'
OUTPUT = 'og-cover.png'
W, H = 1200, 630
BG_TOP    = (20, 60, 20)
BG_BOTTOM = (10, 20, 40)
ACCENT    = (50, 205, 50)  # lime green

img = Image.new('RGB', (W, H), BG_BOTTOM)
draw = ImageDraw.Draw(img)

# Gradient background
for y in range(H):
    t = y / H
    r = int(BG_TOP[0] * (1 - t) + BG_BOTTOM[0] * t)
    g = int(BG_TOP[1] * (1 - t) + BG_BOTTOM[1] * t)
    b = int(BG_TOP[2] * (1 - t) + BG_BOTTOM[2] * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Decorative circle (top-right)
draw.ellipse([(1050, -80), (1250, 120)], outline=ACCENT, width=4)

# Paste game thumbnail (top-right area)
thumb_path = 'data/image/game/geometry-dash-lite/geometry-dash-lite-m186x186.png'
if os.path.exists(thumb_path):
    thumb = Image.open(thumb_path).convert('RGBA')
    thumb = thumb.resize((230, 230), Image.LANCZOS)
    img.paste(thumb, (900, 200), thumb)

# Title text
try:
    font_title = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 80)
    font_sub   = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 42)
    font_url   = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 30)
except Exception:
    font_title = ImageFont.load_default()
    font_sub   = font_title
    font_url   = font_title

draw.text((80, 200), 'Geometry Dash Lite', font=font_title, fill=(255, 255, 255))
draw.text((80, 310), 'Play Unblocked Free Online', font=font_sub, fill=ACCENT)
draw.text((80, 580), DOMAIN, font=font_url, fill=(180, 180, 180))

img.save(OUTPUT, 'PNG', optimize=True)
print(f'Generated {OUTPUT} ({W}x{H})')
