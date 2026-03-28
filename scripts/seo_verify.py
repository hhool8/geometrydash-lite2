"""
seo_verify.py — Full SEO audit for geometrydash-lite2.poki2.online
Writes results to docs/seo-audit-report.md
"""
import os, re, glob
from pathlib import Path

DOMAIN = 'https://geometrydash-lite2.poki2.online'
GA4_ID = 'G-THHTQLKSDJ'
OLD_DOMAIN = 'geometrydash-lite2.github.io'

GAME_PAGES = [
    'color-rush.html',
    'egg-dash.html',
    'geometry-dash-arrow.html',
    'geometry-dash-deadlocked.html',
    'geometry-dash-lite-2.html',
    'geometry-dash-meltdown.html',
    'geometry-dash.html',
    'geometry-rash.html',
    'geometry-vibes-x-ball.html',
    'golf-hit.html',
]

RESULTS = []

def check(name, ok, detail=''):
    status = '✅' if ok else '❌'
    RESULTS.append((name, status, detail))
    return ok


def audit_page(fname, is_home=False):
    label = fname
    if not os.path.exists(fname):
        check(f'{label} — file exists', False, 'File not found')
        return

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    slug = fname.replace('.html', '')
    if slug == 'index':
        slug = ''

    # Title
    m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = m.group(1).strip() if m else ''
    title_ok = bool(title) and 'Unblocked' in title and len(title) < 70
    check(f'{label} — title ({len(title)} chars)', title_ok, title[:80])

    # Meta description
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    desc = m.group(1).strip() if m else ''
    desc_ok = bool(desc) and len(desc) >= 100 and len(desc) <= 165
    check(f'{label} — meta description ({len(desc)} chars)', desc_ok, desc[:120])

    # Canonical
    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content, re.IGNORECASE)
    canonical = m.group(1).strip() if m else ''
    expected_canonical = DOMAIN if not slug else f'{DOMAIN}/{slug}'
    canonical_ok = canonical == expected_canonical
    check(f'{label} — canonical', canonical_ok, canonical or 'MISSING')

    # og:title
    m = re.search(r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    og_title = m.group(1).strip() if m else ''
    check(f'{label} — og:title', bool(og_title), og_title[:80] or 'MISSING')

    # og:description
    m = re.search(r'<meta\s+property=["\']og:description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
    og_desc = m.group(1).strip() if m else ''
    check(f'{label} — og:description', bool(og_desc), og_desc[:80] or 'MISSING')

    # og:url
    m = re.search(r'<meta\s+property=["\']og:url["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    og_url = m.group(1).strip() if m else ''
    og_url_ok = og_url == expected_canonical
    check(f'{label} — og:url', og_url_ok, og_url or 'MISSING')

    # og:image
    m = re.search(r'<meta\s+property=["\']og:image["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    og_image = m.group(1).strip() if m else ''
    og_image_ok = bool(og_image) and DOMAIN in og_image
    check(f'{label} — og:image', og_image_ok, og_image or 'MISSING')

    # og:image file exists on disk
    if og_image and DOMAIN in og_image:
        rel_path = og_image.replace(DOMAIN + '/', '')
        check(f'{label} — og:image file on disk', os.path.exists(rel_path), rel_path)
    else:
        check(f'{label} — og:image file on disk', False, 'No og:image to check')

    # twitter:card
    m = re.search(r'<meta\s+(?:name|property)=["\']twitter:card["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    twitter_card = m.group(1).strip() if m else ''
    check(f'{label} — twitter:card', bool(twitter_card), twitter_card or 'MISSING')

    # GA4
    check(f'{label} — GA4 tag', GA4_ID in content, GA4_ID if GA4_ID in content else 'MISSING')

    # No old domain references
    old_count = content.count(OLD_DOMAIN)
    check(f'{label} — no old domain refs', old_count == 0, f'{old_count} occurrences found' if old_count else 'clean')

    # CWV tracking
    check(f'{label} — CWV tracking', 'Core Web Vitals tracking' in content, '')

    # VideoGame schema
    if not is_home:
        check(f'{label} — VideoGame schema', '"@type": "VideoGame"' in content, '')
    else:
        check(f'{label} — VideoGame schema', '"@type": "VideoGame"' in content, '')
        check(f'{label} — WebSite schema', '"@type": "WebSite"' in content, '')
        check(f'{label} — FAQPage schema', '"@type": "FAQPage"' in content, '')
        check(f'{label} — FAQ visible section', 'gd-faq-section' in content, '')

    # Related games section
    check(f'{label} — related games section', 'gd-related-section' in content, '')


# Run audit
print('Running SEO audit...\n')
audit_page('index.html', is_home=True)
for page in GAME_PAGES:
    audit_page(page, is_home=False)

# sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sm = f.read()
check('sitemap.xml — new domain', DOMAIN in sm, '')
check('sitemap.xml — no old domain', OLD_DOMAIN not in sm, f'{OLD_DOMAIN} found!' if OLD_DOMAIN in sm else 'clean')
game_url_count = sm.count('<loc>')
check('sitemap.xml — 11 URLs', game_url_count == 11, f'{game_url_count} URLs found')

# robots.txt
if os.path.exists('robots.txt'):
    with open('robots.txt') as f:
        rb = f.read()
    check('robots.txt — new domain', DOMAIN in rb, '')
    check('robots.txt — no old domain', OLD_DOMAIN not in rb, f'{OLD_DOMAIN} found!' if OLD_DOMAIN in rb else 'clean')

# Summary
total = len(RESULTS)
passed = sum(1 for _, s, _ in RESULTS if s == '✅')
failed = total - passed

print(f'\nAudit complete: {passed}/{total} checks passed, {failed} failed\n')

# Write report
os.makedirs('docs', exist_ok=True)
lines = ['# SEO Audit Report — geometrydash-lite2.poki2.online\n',
         f'**Passed:** {passed}/{total}  **Failed:** {failed}\n',
         '',
         '| Check | Status | Detail |',
         '|-------|--------|--------|']

for name, status, detail in RESULTS:
    lines.append(f'| {name} | {status} | {detail} |')

lines.append('')
lines.append(f'_Generated automatically by seo_verify.py_')

with open('docs/seo-audit-report.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Report written to docs/seo-audit-report.md')
