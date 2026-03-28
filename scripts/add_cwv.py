"""
add_cwv.py — Inject Core Web Vitals PerformanceObserver tracking into all HTML pages.
Metrics (LCP, CLS, INP) are sent to GA4 via gtag event.
GA4 ID: G-THHTQLKSDJ
"""
import os, glob

GA4_ID = 'G-THHTQLKSDJ'
SENTINEL = 'Core Web Vitals tracking'

CWV_SCRIPT = f"""<!-- {SENTINEL} -->
<script>
(function(){{
  function sendToGA(name, value, id) {{
    if (typeof gtag === 'function') {{
      gtag('event', name, {{
        event_category: 'Web Vitals',
        event_label: id,
        value: Math.round(name === 'CLS' ? value * 1000 : value),
        non_interaction: true
      }});
    }}
  }}
  var supported = typeof PerformanceObserver !== 'undefined';
  if (!supported) return;

  // LCP
  try {{
    var lcpObs = new PerformanceObserver(function(list) {{
      var entries = list.getEntries();
      var last = entries[entries.length - 1];
      sendToGA('LCP', last.startTime, last.id || 'lcp');
    }});
    lcpObs.observe({{type: 'largest-contentful-paint', buffered: true}});
  }} catch(e) {{}}

  // CLS
  try {{
    var clsValue = 0;
    var clsObs = new PerformanceObserver(function(list) {{
      list.getEntries().forEach(function(entry) {{
        if (!entry.hadRecentInput) clsValue += entry.value;
      }});
      sendToGA('CLS', clsValue, 'cls');
    }});
    clsObs.observe({{type: 'layout-shift', buffered: true}});
  }} catch(e) {{}}

  // INP (Interaction to Next Paint)
  try {{
    var inpObs = new PerformanceObserver(function(list) {{
      list.getEntries().forEach(function(entry) {{
        sendToGA('INP', entry.duration, entry.id || 'inp');
      }});
    }});
    inpObs.observe({{type: 'event', durationThreshold: 40, buffered: true}});
  }} catch(e) {{}}
}})();
</script>
"""

pages = glob.glob('*.html')
pages.sort()
count = 0
for fname in pages:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    if SENTINEL in content:
        print(f'  {fname}: CWV already present, skipping')
        continue
    if '</body>' not in content:
        print(f'  {fname}: no </body> tag, skipping')
        continue
    content = content.replace('</body>', CWV_SCRIPT + '\n</body>', 1)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  {fname}: CWV tracking injected')
    count += 1

print(f'Done. Injected CWV into {count} page(s).')
