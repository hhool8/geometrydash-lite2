"""
Replace <img src="rs/imgs/X.jpg"> and <img src="rs/imgs/X.png"> with
<picture><source srcset="rs/imgs/X.webp" type="image/webp"><img ...></picture>
in all HTML pages.
"""
import re, os

html_files = [
    'color-rush.html','egg-dash.html','geometry-dash-arrow.html',
    'geometry-dash-deadlocked.html','geometry-dash-lite-2.html',
    'geometry-dash-meltdown.html','geometry-dash.html','geometry-rash.html',
    'geometry-vibes-x-ball.html','golf-hit.html','index.html'
]

# Match <img ... src="rs/imgs/NAME.ext" ...> tags
img_re = re.compile(
    r'(<img\b[^>]* src="(rs/imgs/([^"]+)\.(jpg|png))"([^>]*)>)',
    re.IGNORECASE
)

def replace_img(m):
    full_tag = m.group(1)
    src = m.group(2)          # rs/imgs/X.jpg
    stem = m.group(3)         # X
    ext = m.group(4)          # jpg or png
    webp_src = f'rs/imgs/{stem}.webp'
    # Check webp file actually exists
    if not os.path.exists(webp_src):
        return full_tag
    # Don't double-wrap if already inside <picture>
    return f'<picture><source srcset="{webp_src}" type="image/webp">{full_tag}</picture>'

for fname in html_files:
    content = open(fname).read()
    original = content
    # Don't process files that already have <picture> wrapping for these imgs
    new_content = img_re.sub(replace_img, content)
    if new_content != original:
        open(fname, 'w').write(new_content)
        count = len(img_re.findall(original))
        print(f'patched ({count} imgs): {fname}')
    else:
        print(f'unchanged: {fname}')
