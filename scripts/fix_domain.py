"""
fix_domain.py — Replace geometrydash-lite2.github.io with geometrydash-lite2.poki2.online
in all HTML pages, robots.txt, and sitemap.xml.
"""
import os, re

OLD = 'geometrydash-lite2.github.io'
NEW = 'geometrydash-lite2.poki2.online'

targets = [f for f in os.listdir('.') if f.endswith('.html')]
targets += ['robots.txt', 'sitemap.xml']

for fname in targets:
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    count = content.count(OLD)
    if count:
        new_content = content.replace(OLD, NEW)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  {fname}: replaced {count} occurrences')
    else:
        print(f'  {fname}: no change')

print('Done.')
