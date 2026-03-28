# geometrydash-lite2.poki2.online — SEO Optimization Plan

Live site: https://geometrydash-lite2.poki2.online  
Repository: https://github.com/hhool8/geometrydash-lite2  
GA4 ID: `G-THHTQLKSDJ`

---

## Site Overview

This is a secondary clone site targeting the Geometry Dash unblocked niche.  
It hosts **11 HTML pages** (1 homepage + 10 game detail pages), each embedding a game via iframe.  
Thumbnails exist in `rs/imgs/` at various non-standard sizes (240–512 px).  
The site structure mirrors `geometrydash-lite.poki2.online` (the primary site) but carries a different game catalog.

**Games hosted:**

| File | Game Title |
|---|---|
| `index.html` | Geometry Dash Lite (homepage) |
| `color-rush.html` | Color Rush |
| `egg-dash.html` | Egg Dash |
| `geometry-dash-arrow.html` | Geometry Dash Arrow |
| `geometry-dash-deadlocked.html` | Geometry Dash Deadlocked |
| `geometry-dash-lite-2.html` | Geometry Dash Lite 2 |
| `geometry-dash-meltdown.html` | Geometry Dash Meltdown |
| `geometry-dash.html` | Geometry Dash |
| `geometry-rash.html` | Geometry Rash |
| `geometry-vibes-x-ball.html` | Geometry Vibes X-Ball |
| `golf-hit.html` | Golf Hit |

---

## Current SEO Audit (2026-03-28 — Pre-Optimization Baseline)

| Check | Status | Detail |
|---|---|---|
| Domain migration | CRITICAL | All pages + `robots.txt` + `sitemap.xml` still reference `geometrydash-lite2.github.io` |
| Meta `<title>` | WARNING | Titles exist but not keyword-optimized; use generic `{Game} - Geometry Dash Lite` pattern |
| Meta `description` | CRITICAL | Descriptions are copies of the title text (not descriptive) |
| `og:title` / `og:description` / `og:url` | CRITICAL | Absent on all 11 pages |
| `og:image` | CRITICAL | Absent on all 11 pages — no Social sharing preview image on any page |
| `twitter:card` | CRITICAL | Absent on all 11 pages |
| `link rel="canonical"` | CRITICAL | Absent on all 11 pages |
| VideoGame JSON-LD schema | CRITICAL | Absent on all 11 pages |
| WebSite + FAQPage JSON-LD | WARNING | Absent on `index.html` |
| Core Web Vitals tracking (LCP/CLS/INP) | WARNING | Absent on all pages |
| `robots.txt` | WARNING | Sitemap URL points to old GitHub Pages domain |
| `sitemap.xml` | WARNING | All 11 `<loc>` URLs point to old GitHub Pages domain |
| Game thumbnails (standardized) | WARNING | Exist in `rs/imgs/` but non-standard sizes (240–512 px); not in `data/image/game/` convention |
| 1200×630 og covers per game | CRITICAL | Not generated |
| Homepage og-cover.png (1200×630) | CRITICAL | Missing |
| Visible FAQ section (HTML) | WARNING | Missing from homepage |
| Related games internal links | WARNING | Missing from all game pages |
| SEO audit script | NOT STARTED | No `scripts/seo_verify.py` |
| Duplicate content risk | HIGH | Near-identical page structure to primary site — requires unique titles, descriptions, and page copy |

---

## Full SEO Task Plan

### Phase 1 — Critical Foundation (Blocking)

> These must be completed before any other work has value. Pages with missing domain, broken og:image, and no schema cannot rank or be shared correctly.

#### 1.1 Domain Migration
- **Replace all `geometrydash-lite2.github.io` → `geometrydash-lite2.poki2.online`** across:
  - All 11 `.html` files
  - `robots.txt` (Sitemap URL)
  - `sitemap.xml` (all 11 `<loc>` entries)
- Script: `scripts/fix_domain.py`

#### 1.2 Canonical URLs
- Add `<link rel="canonical" href="https://geometrydash-lite2.poki2.online/{slug}">` to all 11 pages
- Homepage canonical: `https://geometrydash-lite2.poki2.online`

#### 1.3 Title Rewrites (Unique + Keyword-Rich)
Each page needs a distinct, search-intent title. Pattern:
- Game pages: `{Game Title} Unblocked - Play Free Online | Geometry Dash`
- Homepage: `Geometry Dash Lite Unblocked - Play Free Online | GD Lite 2`

| Page | New Title |
|---|---|
| `index.html` | `Geometry Dash Lite Unblocked – Play Free Online \| GD Lite 2` |
| `color-rush.html` | `Color Rush Unblocked – Play Free Online` |
| `egg-dash.html` | `Egg Dash Unblocked – Play Free Online` |
| `geometry-dash-arrow.html` | `Geometry Dash Arrow Unblocked – Play Free Online` |
| `geometry-dash-deadlocked.html` | `Geometry Dash Deadlocked Unblocked – Play Free Online` |
| `geometry-dash-lite-2.html` | `Geometry Dash Lite 2 Unblocked – Play Free Online` |
| `geometry-dash-meltdown.html` | `Geometry Dash Meltdown Unblocked – Play Free Online` |
| `geometry-dash.html` | `Geometry Dash Unblocked – Play Free Online` |
| `geometry-rash.html` | `Geometry Rash Unblocked – Play Free Online` |
| `geometry-vibes-x-ball.html` | `Geometry Vibes X-Ball Unblocked – Play Free Online` |
| `golf-hit.html` | `Golf Hit Unblocked – Play Free Online` |

#### 1.4 Meta Description Rewrites (Unique, 120–160 chars)
All descriptions are currently set to the title text — this is a duplicate-content penalty.  
Each must be unique with a call-to-action and target keywords.

| Page | Meta Description |
|---|---|
| `index.html` | `Play Geometry Dash Lite Unblocked free — the iconic rhythm platformer. Jump, flip, and fly through obstacles. Works on school networks and Chromebook.` |
| `color-rush.html` | `Play Color Rush Unblocked free online! A vibrant endless runner packed with color-coded obstacles. Match, dash, and survive every wave.` |
| `egg-dash.html` | `Play Egg Dash Unblocked free online! A quirky platformer where you guide an egg through tricky levels. No download needed — fun for all ages.` |
| `geometry-dash-arrow.html` | `Play Geometry Dash Arrow Unblocked free online! Navigate sharp arrow-filled gauntlets with precision timing. Dodge every spike and conquer the level.` |
| `geometry-dash-deadlocked.html` | `Play Geometry Dash Deadlocked Unblocked free! A relentless demon-level challenge packed with death traps and pulsing beats. Can you survive?` |
| `geometry-dash-lite-2.html` | `Play Geometry Dash Lite 2 Unblocked free online! The sequel sensation with new levels and harder obstacles. Rhythm-based platforming at its best.` |
| `geometry-dash-meltdown.html` | `Play Geometry Dash Meltdown Unblocked free! Three searing levels — Molten Rock, Nock Em, and Power Trip. Pure fire-and-music action.` |
| `geometry-dash.html` | `Play Geometry Dash Unblocked free online! The full original rhythm platformer — tap to jump, fly, and flip through 21 official levels. No install needed.` |
| `geometry-rash.html` | `Play Geometry Rash Unblocked free online! A fast-paced rhythm runner with razor obstacles and a driving soundtrack. React fast or restart.` |
| `geometry-vibes-x-ball.html` | `Play Geometry Vibes X-Ball Unblocked free! A ball-rolling geometry-style game with neon visuals and reactive music. Test your reflexes now.` |
| `golf-hit.html` | `Play Golf Hit Unblocked free online! Aim, drag, and smash the ball through creative obstacle courses. Physics-based golf fun with no download needed.` |

#### 1.5 Open Graph Tags (og:title, og:description, og:url, og:image)
- Add complete OG block to all 11 pages
- Script: `scripts/add_og_tags.py`

#### 1.6 Twitter Card Meta Tags
- Add `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image` to all 11 pages
- Account: `@geometrydashlite2` (to be created)

---

### Phase 2 — Image Assets

#### 2.1 Normalize Game Thumbnails
- Resize all `rs/imgs/` thumbnails to **186×186 px** and copy to `data/image/game/{slug}/{slug}-m186x186.{ext}`
- Source images exist; need resize via Pillow
- Script: `scripts/normalize_thumbs.py`

Game → thumbnail mapping:

| Slug | Source File | Source Size |
|---|---|---|
| `geometry-dash-lite` | `rs/imgs/geometry-dash-lite.png` | 512×512 |
| `color-rush` | `rs/imgs/color-rush.jpg` | 444×444 |
| `egg-dash` | `rs/imgs/egg-dash.jpg` | 512×512 |
| `geometry-dash-arrow` | `rs/imgs/geometry-arrow.jpg` | 369×369 |
| `geometry-dash-deadlocked` | `rs/imgs/geometry-dash-deadlocked.jpg` | 294×295 |
| `geometry-dash-lite-2` | `rs/imgs/geometrydash-lite-2.png` | 279×279 |
| `geometry-dash-meltdown` | `rs/imgs/geometry-dash-meltdown.jpg` | 332×332 |
| `geometry-dash` | `rs/imgs/geometrydash.jpg` | 246×243 |
| `geometry-rash` | `rs/imgs/geometryrash.png` | 240×240 |
| `geometry-vibes-x-ball` | `rs/imgs/geometry-vibes-x-ball.jpg` | 419×419 |
| `golf-hit` | `rs/imgs/golf-hit.jpg` | 448×448 |

#### 2.2 Generate Homepage og-cover.png (1200×630)
- Brand cover image for `og:image` on `index.html` and `twitter:image`
- Script: `scripts/gen_og_cover.py` (adapted from geometry-dashlite)

#### 2.3 Generate Per-Game og Covers (1200×630)
- One image per game: `data/image/game/{slug}/{slug}-og.png`
- Uses normalized 186×186 thumbnail + game title text overlay on dark background
- Script: `scripts/gen_game_og_covers.py` (adapted from geometry-dashlite)

---

### Phase 3 — Structured Data (JSON-LD)

#### 3.1 VideoGame Schema on All 10 Game Pages
Add `<script type="application/ld+json">` block with:
```json
{
  "@context": "https://schema.org",
  "@type": "VideoGame",
  "name": "{Game Title}",
  "url": "https://geometrydash-lite2.poki2.online/{slug}",
  "image": "https://geometrydash-lite2.poki2.online/data/image/game/{slug}/{slug}-og.png",
  "description": "{meta description text}",
  "genre": "Platformer",
  "gamePlatform": "Web Browser",
  "applicationCategory": "Game",
  "operatingSystem": "Any",
  "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
}
```

#### 3.2 WebSite + FAQPage Schema on Homepage
- `WebSite` schema with `SearchAction` potential
- `FAQPage` with 5 Q&A items targeting "unblocked / free / school / Chromebook" queries
- Script: `scripts/add_schema.py`

---

### Phase 4 — Performance & Tracking

#### 4.1 Core Web Vitals Tracking (LCP / CLS / INP)
- Add `PerformanceObserver` code to all 10 game pages
- Sends events to GA4 (`G-THHTQLKSDJ`) via `gtag('event', ...)`
- Script: `scripts/add_cwv.py`

---

### Phase 5 — Duplicate Content Differentiation

> This site is structurally a clone of `geometrydash-lite.poki2.online`. Google can penalize near-duplicate sites. Differentiation strategy:

#### 5.1 Unique Page Copy
- Each game page needs at least one unique descriptive paragraph (not templated)
- Add `<section class="game-description">` with 2–3 unique sentences per game below the iframe
- Different keyword focus from primary site (e.g., target "full version", "original", "sequel")

#### 5.2 Unique Site Branding
- Site name in meta/schema: `"GD Lite 2"` or `"Geometry Dash Online"` (not `"Geometry Dash Lite"`)
- `og:site_name` content should differ from the primary site
- H1/subtitle text on each page should differ

#### 5.3 Noindex Consideration (Optional)
- If duplicate penalty risk is too high initially, temporarily add `<meta name="robots" content="noindex">` on pages with no unique content until copy is written
- Remove once unique content sections are added

---

### Phase 6 — On-Page Engagement

#### 6.1 Visible FAQ Section on Homepage
- 5 `<details>/<summary>` accordion items with microdata (`itemscope`, `itemtype`, `itemprop`)
- Questions: free/unblocked/school/download/Chromebook
- To be added via `scripts/add_faq_and_related.py`

#### 6.2 Related Games Section on All 11 Pages
- 4 game cards per page (thumbnail + title + link), excluding current game
- Internal cross-linking improves crawl depth and dwell time
- To be added via `scripts/add_faq_and_related.py`

---

### Phase 7 — Infrastructure

#### 7.1 Regenerate sitemap.xml
- Replace all `geometrydash-lite2.github.io` → `geometrydash-lite2.poki2.online`
- Add all 11 pages with correct `<loc>`, `<changefreq>`, `<priority>`, `<lastmod>`
- Script: `scripts/gen_sitemap.py`

#### 7.2 Fix robots.txt
- Replace Sitemap URL with new domain:
  `Sitemap: https://geometrydash-lite2.poki2.online/sitemap.xml`

#### 7.3 Create SEO Audit Script
- Port `seo_verify.py` from geometry-dashlite to this repo
- Checks: title, meta desc, canonical, og tags, twitter card, GA4, schema, CWV, og image file existence
- Output: `docs/seo-audit-report.md`
- Script: `scripts/seo_verify.py`

---

### Phase 8 — Manual Off-Page

| Priority | Task |
|---|---|
| High | Register `geometrydash-lite2.poki2.online` with Google Search Console; submit sitemap |
| High | Submit site to CrazyGames, itch.io, Newgrounds game directories |
| High | Reddit posts: r/WebGames, r/geometrydash, r/teenagers, r/unblocked |
| Medium | Create @geometrydashlite2 social accounts (Twitter/X, YouTube) |
| Medium | Cross-link between `geometrydash-lite.poki2.online` and `geometrydash-lite2.poki2.online` in footer/about pages |
| Low | YouTube gameplay walkthroughs (organic backlink source) |
| Low | Comment in geometry-dash community threads with site link |

---

## Scripts Plan

| Script | Purpose | Based On |
|---|---|---|
| `scripts/fix_domain.py` | Replace old GitHub Pages domain in all files | New |
| `scripts/normalize_thumbs.py` | Resize `rs/imgs/` → `data/image/game/{slug}/{slug}-m186x186.{ext}` | New |
| `scripts/gen_og_cover.py` | Generate 1200×630 homepage og-cover.png | Adapt geometry-dashlite |
| `scripts/gen_game_og_covers.py` | Generate 1200×630 per-game og covers | Port from geometry-dashlite |
| `scripts/add_og_tags.py` | Inject og:* and twitter:* meta blocks into all 11 pages | New |
| `scripts/add_schema.py` | Inject VideoGame + WebSite + FAQPage JSON-LD | Port from geometry-dashlite |
| `scripts/add_cwv.py` | Inject Core Web Vitals PerformanceObserver code | Port from geometry-dashlite |
| `scripts/add_faq_and_related.py` | Add visible FAQ + related games sections | Port from geometry-dashlite |
| `scripts/gen_sitemap.py` | Regenerate sitemap.xml with correct domain | Port from geometry-dashlite |
| `scripts/seo_verify.py` | Full audit — output `docs/seo-audit-report.md` | Port from geometry-dashlite |

---

## Execution Order

```
Phase 1.1  fix_domain.py             ← unblocks everything else
Phase 2.1  normalize_thumbs.py       ← required before og cover gen
Phase 2.2  gen_og_cover.py           ← homepage og:image
Phase 2.3  gen_game_og_covers.py     ← per-game og:image
Phase 1.2–1.6  add_og_tags.py        ← canonical + OG + twitter (uses og covers)
Phase 3    add_schema.py             ← VideoGame + WebSite + FAQ JSON-LD
Phase 4    add_cwv.py                ← CWV tracking
Phase 5.1–5.2  (manual) unique copy per game page
Phase 6    add_faq_and_related.py    ← visible FAQ + related games
Phase 7.1–7.2  gen_sitemap.py + fix robots.txt
Phase 7.3  seo_verify.py             ← audit; fix any remaining issues
Phase 8    manual off-page
```

---

## Work Status

### Session 1 — 2026-03-28 (Plan)

- [x] Full baseline audit completed
- [x] SEO task plan written to `README.md`
- [ ] Phase 1.1 — Domain migration (`fix_domain.py`)
- [ ] Phase 1.2 — Canonical URLs  
- [ ] Phase 1.3 — Title rewrites (all 11 pages)  
- [ ] Phase 1.4 — Meta description rewrites (all 11 pages)  
- [ ] Phase 1.5 — Open Graph tags (all 11 pages)  
- [ ] Phase 1.6 — Twitter Cards (all 11 pages)  
- [ ] Phase 2.1 — Normalize thumbnails → `data/image/game/`  
- [ ] Phase 2.2 — Homepage og-cover.png  
- [ ] Phase 2.3 — Per-game og covers (11 × 1200×630)  
- [ ] Phase 3.1 — VideoGame JSON-LD on all 10 game pages  
- [ ] Phase 3.2 — WebSite + FAQPage JSON-LD on homepage  
- [ ] Phase 4.1 — Core Web Vitals tracking  
- [x] Phase 1.1 — Domain migration (`fix_domain.py`)
- [x] Phase 1.2 — Canonical URLs
- [x] Phase 1.3 — Title rewrites (all 11 pages)
- [x] Phase 1.4 — Meta description rewrites (all 11 pages)
- [x] Phase 1.5 — Open Graph tags (all 11 pages)
- [x] Phase 1.6 — Twitter Cards (all 11 pages)
- [x] Phase 2.1 — Normalize thumbnails → `data/image/game/`
- [x] Phase 2.2 — Homepage og-cover.png
- [x] Phase 2.3 — Per-game og covers (11 × 1200×630)
- [x] Phase 3.1 — VideoGame JSON-LD on all 10 game pages
- [x] Phase 3.2 — WebSite + FAQPage JSON-LD on homepage
- [x] Phase 4.1 — Core Web Vitals tracking
- [ ] Phase 5 — Unique page copy / duplicate differentiation *(manual, pending)*
- [x] Phase 6.1 — Visible FAQ section (homepage)
- [x] Phase 6.2 — Related games sections (all 11 pages)
- [x] Phase 7.1 — Regenerate sitemap.xml
- [x] Phase 7.2 — Fix robots.txt
- [x] Phase 7.3 — SEO audit script (`seo_verify.py`)
- [ ] Phase 8 — Manual off-page / GSC submission *(not started)*

---

## Execution Status — Session 2 (Complete)

> Last updated: 2026-03-28 | Commit: `515b7f6` | Branch: `main`

### What Was Done

All automated SEO phases were executed end-to-end:

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | Domain migration + canonical + OG + Twitter Cards (11 pages) | ✅ Done |
| 2 | Thumbnail normalization (186×186) + OG covers (1200×630, 12 images) | ✅ Done |
| 3 | VideoGame / WebSite / FAQPage JSON-LD structured data | ✅ Done |
| 4 | Core Web Vitals tracking (LCP / CLS / INP → GA4 `G-THHTQLKSDJ`) | ✅ Done |
| 5 | Unique body copy per page | ⏳ Pending (manual review needed) |
| 6 | Visible FAQ accordion (homepage) + related game cards (all 11 pages) | ✅ Done |
| 7 | Regenerate `sitemap.xml` + `robots.txt` + `seo_verify.py` (162/162 pass) | ✅ Done |
| 8 | Off-page SEO / Google Search Console submission | ❌ Not started |

### Audit Result

```
Pages: 11  |  Checks OK: 157  |  Issues: 0
162/162 seo_verify.py assertions pass
```

All 11 pages pass every check:
- Unique title with "Unblocked" keyword, ≤ 70 chars
- Meta description 100–165 chars
- Correct canonical URL (`geometrydash-lite2.poki2.online`)
- `og:title`, `og:description`, `og:url`, `og:image` present and correct
- `og:image` file exists on disk
- `twitter:card` present
- `VideoGame` JSON-LD on all game pages
- `WebSite` + `FAQPage` JSON-LD on homepage
- Related games section on all 11 pages
- CWV tracking + GA4 ID on all 11 pages
- Zero references to old domain (`geometrydash-lite2.github.io`) in any HTML/XML/txt

### Assets Produced

| Asset | Count |
|-------|-------|
| `data/image/game/{slug}/{slug}-m186x186.*` | 11 thumbnails |
| `data/image/game/{slug}/{slug}-og.png` | 11 OG covers |
| `og-cover.png` (homepage) | 1 |
| Scripts in `scripts/` | 10 |
| `docs/seo-audit-report.md` | 1 |

### Remaining Work

1. **Phase 5 — Body copy quality**: Each page has ~14–16 KB of body text. The text is present but has not been manually reviewed for thin or duplicated content. Recommend reading each page's `<main>` section and rewriting game-specific paragraphs to differentiate them.

2. **Phase 8 — Google Search Console**:
   - Submit `https://geometrydash-lite2.poki2.online/sitemap.xml`
   - Request indexing for homepage and all 11 game pages
   - Monitor Core Web Vitals report in GSC and GA4
