"""
gen_sitemap.py — Generate sitemap.xml for geometrydash-lite2.poki2.online
"""
import subprocess
from datetime import date

DOMAIN = 'https://geometrydash-lite2.poki2.online'

PAGES = [
    ('',                        '1.0', 'daily'),
    ('color-rush',              '0.9', 'weekly'),
    ('egg-dash',                '0.9', 'weekly'),
    ('geometry-dash-arrow',     '0.9', 'weekly'),
    ('geometry-dash-deadlocked','0.9', 'weekly'),
    ('geometry-dash-lite-2',    '0.9', 'weekly'),
    ('geometry-dash-meltdown',  '0.9', 'weekly'),
    ('geometry-dash',           '0.9', 'weekly'),
    ('geometry-rash',           '0.9', 'weekly'),
    ('geometry-vibes-x-ball',   '0.9', 'weekly'),
    ('golf-hit',                '0.9', 'weekly'),
]

today = date.today().isoformat()

urls = []
for slug, priority, changefreq in PAGES:
    loc = f'{DOMAIN}/{slug}' if slug else DOMAIN
    urls.append(
        f'  <url>\n'
        f'    <loc>{loc}</loc>\n'
        f'    <lastmod>{today}</lastmod>\n'
        f'    <changefreq>{changefreq}</changefreq>\n'
        f'    <priority>{priority}</priority>\n'
        f'  </url>'
    )

xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
       + '\n'.join(urls) + '\n'
       '</urlset>\n')

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml)

print(f'sitemap.xml written with {len(PAGES)} URLs')
