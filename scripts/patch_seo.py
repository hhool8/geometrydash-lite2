import os, re

pages_dir = '/Users/yanmenghou/Desktop/h5games/geometrydash-lite2'
html_files = sorted([f for f in os.listdir(pages_dir) if f.endswith('.html')])

FOOTER_OLD = (
    '  <a href="/privacy" style="color:#555;text-decoration:none;margin:0 10px">Privacy Policy</a>\n'
    '  <span style="color:#ccc">&middot;</span>\n'
    '  <span style="margin-left:10px">&copy; 2026 GD Lite 2</span>'
)
FOOTER_NEW = (
    '  <a href="/privacy" style="color:#555;text-decoration:none;margin:0 10px">Privacy Policy</a>\n'
    '  <span style="color:#ccc">&middot;</span>\n'
    '  <a href="https://geometrydash-lite.poki2.online" style="color:#555;text-decoration:none;margin:0 10px" rel="noopener">GD Lite</a>\n'
    '  <span style="color:#ccc">&middot;</span>\n'
    '  <span style="margin-left:10px">&copy; 2026 GD Lite 2</span>'
)

def add_lazy(m):
    tag = m.group(0)
    if 'loading=' in tag:
        return tag
    return tag[:-2].rstrip() + ' loading="lazy" />'

for fname in html_files:
    fpath = os.path.join(pages_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    modified = content

    # Step 4: theme-color
    if '<meta name="theme-color"' not in modified:
        modified = modified.replace(
            '<link rel="icon" href="rs/imgs/geometry-dash-lite.png">',
            '<link rel="icon" href="rs/imgs/geometry-dash-lite.png">\n    <meta name="theme-color" content="#1d1d2e">'
        )

    # Step 5: loading="lazy" on 95x95 grid thumbnails
    modified = re.sub(r'<img\s+width="95"\s+height="95"[^>]*/>', add_lazy, modified)

    # Step 6: footer sister site link
    modified = modified.replace(FOOTER_OLD, FOOTER_NEW)

    if modified != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(modified)
        print(f'Updated: {fname}')
    else:
        print(f'No change: {fname}')

print('Done.')
