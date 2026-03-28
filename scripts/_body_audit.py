#!/usr/bin/env python3
"""Phase 5 body copy audit — similarity + thin content detection"""
import os, re, glob
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def extract_body_text(html):
    # remove script/style/json-ld blocks
    html = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.DOTALL)
    html = re.sub(r'<style[^>]*>.*?</style>', ' ', html, flags=re.DOTALL)
    # strip tags
    text = re.sub(r'<[^>]+>', ' ', html)
    # collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_main_sections(html):
    """Pull out key visible text blocks by id/class"""
    sections = {}
    # hero subtitle / description
    m = re.search(r'class=["\']gd-hero["\'][^>]*>.*?<p[^>]*>(.*?)</p>', html, re.DOTALL)
    if m: sections['hero_p'] = re.sub(r'<[^>]+>', '', m.group(1)).strip()

    # about section
    m = re.search(r'id=["\']about["\'][^>]*>(.*?)</section>', html, re.DOTALL)
    if not m: m = re.search(r'class=["\'][^"\']*about[^"\']*["\'][^>]*>(.*?)</(?:section|div)>', html, re.DOTALL)
    if m: sections['about'] = re.sub(r'<[^>]+>', '', m.group(1)).strip()[:300]

    # features list
    m = re.search(r'id=["\']features["\'][^>]*>(.*?)</(?:section|ul)>', html, re.DOTALL)
    if m: sections['features'] = re.sub(r'<[^>]+>', ' ', m.group(1)).strip()[:300]

    # FAQ first question
    m = re.search(r'<summary[^>]*>(.*?)</summary>', html, re.DOTALL)
    if m: sections['faq_q1'] = re.sub(r'<[^>]+>', '', m.group(1)).strip()

    return sections

def word_ngrams(text, n=3):
    words = re.sub(r'[^\w\s]', '', text.lower()).split()
    return set(zip(*[words[i:] for i in range(n)]))

pages = sorted(glob.glob('*.html'))
data = {}
for fname in pages:
    with open(fname) as f: html = f.read()
    body_text = extract_body_text(html)
    sections = extract_main_sections(html)
    data[fname] = {'text': body_text, 'len': len(body_text), 'sections': sections}

print(f"\n{'='*70}")
print("PHASE 5 — BODY COPY AUDIT")
print(f"{'='*70}\n")

print("BODY TEXT LENGTH (characters):")
for fname, d in data.items():
    bar = '█' * (d['len'] // 500)
    flag = '⚠️ ' if d['len'] < 2000 else '  '
    print(f"  {flag}{fname:<45} {d['len']:>6} chars  {bar}")

print(f"\n{'─'*70}")
print("SECTION EXTRACTS (first 120 chars):\n")
for fname, d in data.items():
    print(f"  [{fname}]")
    for sec, text in d['sections'].items():
        preview = text[:120].replace('\n', ' ')
        print(f"    {sec:<12}: {preview}")
    if not d['sections']:
        print("    (no named sections found)")
    print()

# Jaccard similarity on 3-grams across page pairs
print(f"{'─'*70}")
print("PAIRWISE SIMILARITY (3-gram Jaccard, > 0.4 = ⚠️ duplicate risk)\n")
fnames = list(data.keys())
high_sim = []
for i in range(len(fnames)):
    for j in range(i+1, len(fnames)):
        a = word_ngrams(data[fnames[i]]['text'])
        b = word_ngrams(data[fnames[j]]['text'])
        if not a or not b: continue
        sim = len(a & b) / len(a | b)
        if sim > 0.2:
            flag = '⚠️ ' if sim > 0.4 else '   '
            print(f"  {flag}{fnames[i]:<35} vs {fnames[j]:<35} sim={sim:.2f}")
            if sim > 0.4: high_sim.append((fnames[i], fnames[j], sim))

if not high_sim:
    print("  ✅  No high-similarity pairs found (all < 0.40)")

print(f"\n{'='*70}\n")
