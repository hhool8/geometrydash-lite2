#!/usr/bin/env python3
"""Code walkthrough audit for geometrydash-lite2"""
import os, re, glob

DOMAIN = 'https://geometrydash-lite2.poki2.online'
OLD_DOMAIN = 'geometrydash-lite2.github.io'
GA4_ID = 'G-THHTQLKSDJ'

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

pages = sorted(glob.glob('*.html'))
all_issues = {}
all_ok = {}

for fname in pages:
    with open(fname) as f:
        content = f.read()
    slug = fname.replace('.html', '')
    if slug == 'index':
        slug = ''
    expected_canonical = DOMAIN if not slug else f'{DOMAIN}/{slug}'

    def get1(pattern):
        m = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        return m.group(1).strip() if m else ''

    title   = get1(r'<title>(.*?)</title>')
    desc    = get1(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']')
    canon   = get1(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']')
    og_t    = get1(r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']')
    og_d    = get1(r'<meta\s+property=["\']og:description["\']\s+content=["\'](.*?)["\']')
    og_u    = get1(r'<meta\s+property=["\']og:url["\']\s+content=["\'](.*?)["\']')
    og_img  = get1(r'<meta\s+property=["\']og:image["\']\s+content=["\'](.*?)["\']')
    tw_card = get1(r'<meta\s+(?:name|property)=["\']twitter:card["\']\s+content=["\'](.*?)["\']')
    vg      = '"@type": "VideoGame"' in content
    ws      = '"@type": "WebSite"' in content
    faqjson = '"@type": "FAQPage"' in content
    cwv     = 'Core Web Vitals tracking' in content
    faq_vis = 'gd-faq-section' in content
    related = 'gd-related-section' in content
    ga4     = GA4_ID in content
    old_cnt = content.count(OLD_DOMAIN)
    img_file = og_img.replace(DOMAIN + '/', '') if og_img else ''
    img_ok   = os.path.exists(img_file) if img_file else False

    issues = []
    ok = []

    # Title
    if title and 'Unblocked' in title and len(title) <= 70:
        ok.append(f'title: "{title}"')
    else:
        issues.append(f'title: "{title}" (len={len(title)}, needs "Unblocked")')

    # Desc
    if 100 <= len(desc) <= 165:
        ok.append(f'meta description: {len(desc)} chars')
    else:
        issues.append(f'meta description: {len(desc)} chars (want 100-165)')

    # Canonical
    if canon == expected_canonical:
        ok.append(f'canonical: {canon}')
    else:
        issues.append(f'canonical mismatch — got "{canon}", want "{expected_canonical}"')

    # OG
    if og_t: ok.append('og:title present')
    else: issues.append('og:title MISSING')
    if og_d: ok.append('og:description present')
    else: issues.append('og:description MISSING')
    if og_u == expected_canonical: ok.append('og:url correct')
    else: issues.append(f'og:url mismatch: "{og_u}"')
    if og_img and DOMAIN in og_img: ok.append(f'og:image: {og_img}')
    else: issues.append(f'og:image MISSING or wrong domain: "{og_img}"')
    if img_ok: ok.append('og:image file exists on disk')
    else: issues.append(f'og:image file NOT on disk: {img_file}')

    # Twitter
    if tw_card: ok.append(f'twitter:card: {tw_card}')
    else: issues.append('twitter:card MISSING')

    # Schema
    if vg: ok.append('VideoGame JSON-LD present')
    else: issues.append('VideoGame JSON-LD MISSING')

    if fname == 'index.html':
        if ws: ok.append('WebSite JSON-LD present')
        else: issues.append('WebSite JSON-LD MISSING')
        if faqjson: ok.append('FAQPage JSON-LD present')
        else: issues.append('FAQPage JSON-LD MISSING')
        if faq_vis: ok.append('visible FAQ section present')
        else: issues.append('visible FAQ section MISSING')

    if related: ok.append('related games section present')
    else: issues.append('related games section MISSING')

    if cwv: ok.append('CWV tracking present')
    else: issues.append('CWV tracking MISSING')

    if ga4: ok.append(f'GA4 ({GA4_ID}) present')
    else: issues.append(f'GA4 ({GA4_ID}) MISSING')

    if old_cnt == 0: ok.append('no old domain refs')
    else: issues.append(f'{old_cnt} old domain ref(s) still present')

    all_issues[fname] = issues
    all_ok[fname] = ok

# Print summary
total_issues = sum(len(v) for v in all_issues.values())
print(f"\n{'='*70}")
print(f"WALKTHROUGH RESULTS — geometrydash-lite2.poki2.online")
print(f"{'='*70}")
print(f"Pages: {len(pages)} | Total checks OK: {sum(len(v) for v in all_ok.values())} | Issues: {total_issues}\n")

for fname in pages:
    issues = all_issues[fname]
    status = '✅ PASS' if not issues else f'⚠️  {len(issues)} ISSUE(S)'
    print(f"  {fname:<40} {status}")
    for i in issues:
        print(f"    └─ {i}")

# Check non-HTML assets
print(f"\n{'─'*70}")
print("ASSET CHECKS")
print(f"{'─'*70}")

# og-cover.png
if os.path.exists('og-cover.png'):
    sz = os.path.getsize('og-cover.png')
    print(f"  og-cover.png ✅  ({sz//1024} KB)")
else:
    print("  og-cover.png ❌  MISSING")

# per-game og covers
slugs = [
    ('geometry-dash-lite', 'png'), ('color-rush', 'jpg'), ('egg-dash', 'jpg'),
    ('geometry-dash-arrow', 'jpg'), ('geometry-dash-deadlocked', 'jpg'),
    ('geometry-dash-lite-2', 'png'), ('geometry-dash-meltdown', 'jpg'),
    ('geometry-dash', 'jpg'), ('geometry-rash', 'png'),
    ('geometry-vibes-x-ball', 'jpg'), ('golf-hit', 'jpg'),
]
for slug, ext in slugs:
    og_path = f'data/image/game/{slug}/{slug}-og.png'
    th_path = f'data/image/game/{slug}/{slug}-m186x186.{ext}'
    og_ok = '✅' if os.path.exists(og_path) else '❌'
    th_ok = '✅' if os.path.exists(th_path) else '❌'
    print(f"  {slug:<35} og:{og_ok}  thumb:{th_ok}")

# sitemap + robots
print(f"\n{'─'*70}")
for f in ['sitemap.xml', 'robots.txt', 'CNAME']:
    if os.path.exists(f):
        with open(f) as fp: txt = fp.read()
        old_ok = '✅' if OLD_DOMAIN not in txt else f'❌ ({txt.count(OLD_DOMAIN)} old refs)'
        new_ok = '✅' if DOMAIN.replace('https://','') in txt else '❌'
        print(f"  {f:<15} new_domain:{new_ok}  no_old:{old_ok}")
    else:
        print(f"  {f:<15} ❌ MISSING")

# scripts
print(f"\n{'─'*70}")
print("SCRIPTS")
scripts = [
    'fix_domain.py','normalize_thumbs.py','gen_og_cover.py',
    'gen_game_og_covers.py','add_og_tags.py','add_schema.py',
    'add_cwv.py','add_faq_and_related.py','gen_sitemap.py','seo_verify.py',
]
for s in scripts:
    path = f'scripts/{s}'
    exists = '✅' if os.path.exists(path) else '❌'
    sz = os.path.getsize(path) if os.path.exists(path) else 0
    print(f"  {s:<35} {exists}  ({sz} bytes)")

print(f"\n{'='*70}\n")
