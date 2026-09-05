from pathlib import Path
import re

root = Path('/workspace/path-guard')
html_path = root / 'index.html'
html = html_path.read_text()

# Create simple SVG icon
icon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="96" fill="#0f1419"/>
  <path d="M80 360 C140 280, 200 280, 256 320 C312 360, 372 360, 432 280" stroke="#38bdf8" stroke-width="36" fill="none" stroke-linecap="round"/>
  <circle cx="160" cy="300" r="34" fill="#22c55e"/>
  <circle cx="340" cy="250" r="34" fill="#f59e0b"/>
  <circle cx="250" cy="180" r="28" fill="#f87171"/>
</svg>
'''
(root / 'icon.svg').write_text(icon_svg)

manifest = '''{
  "name": "Path Guard",
  "short_name": "Path Guard",
  "description": "Tiny phone tower defense trial",
  "start_url": "./index.html",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait",
  "background_color": "#0f1419",
  "theme_color": "#0f1419",
  "icons": [
    {
      "src": "icon.svg",
      "sizes": "any",
      "type": "image/svg+xml",
      "purpose": "any maskable"
    }
  ]
}
'''
(root / 'manifest.webmanifest').write_text(manifest)

sw = '''self.addEventListener('install', (e) => {
  e.waitUntil(caches.open('path-guard-v1').then((c) => c.addAll([
    './', './index.html', './manifest.webmanifest', './icon.svg'
  ])));
  self.skipWaiting();
});
self.addEventListener('activate', (e) => {
  e.waitUntil(self.clients.claim());
});
self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((r) => r || fetch(e.request))
  );
});
'''
(root / 'sw.js').write_text(sw)

head_inject = '''<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<meta name="theme-color" content="#0f1419">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Path Guard">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon.svg">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<title>Path Guard</title>'''

html = re.sub(
    r'<meta charset="UTF-8">\s*<meta name="viewport"[^>]*>\s*<title>Path Guard</title>',
    head_inject,
    html,
    count=1,
)

# CSS tweaks for standalone fullscreen feel
css_extra = '''
  html, body {
    height: 100%;
    height: 100dvh;
    overscroll-behavior: none;
  }
  #app {
    min-height: 100%;
    min-height: 100dvh;
    max-width: none;
    padding-top: env(safe-area-inset-top);
    padding-bottom: env(safe-area-inset-bottom);
  }
  @media (display-mode: standalone), (display-mode: fullscreen) {
    body { background: #0f1419; }
    #app { border-radius: 0; }
    canvas { border-radius: 0; border-left: none; border-right: none; }
  }
'''

html = html.replace(
    'touch-action: manipulation;\n  }',
    'touch-action: manipulation;\noverscroll-behavior: none;\n  }' + css_extra,
    1,
)

# Add install hint + fullscreen button near controls if start-btn exists
# Inject SW registration before </body>
sw_script = '''
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./sw.js').catch(() => {});
}
function goFullscreen() {
  const el = document.documentElement;
  const req = el.requestFullscreen || el.webkitRequestFullscreen || el.msRequestFullscreen;
  if (req) req.call(el).catch(() => {});
  // iOS / Android: prefer Add to Home Screen for true chrome-less mode
}
</script>
'''

if 'serviceWorker' not in html:
    html = html.replace('</body>', sw_script + '</body>')

# Add a subtle install tip in HTML if #hint exists - update README instead for instructions
html_path.write_text(html)
print('updated index.html, manifest, icon, sw')
