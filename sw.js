const CACHE = 'path-guard-v163';
const ASSETS = [
  './manifest.webmanifest',
  './icon.svg',
  './sprites/archer.png',
  './sprites/crossbow.png',
  './sprites/cannon.png',
  './sprites/frost.png',
  './sprites/fire.png',
  './sprites/lightning.png',
  './sprites/sniper.png',
  './sprites/bazooka.png',
  './sprites/bank.png',
  './sprites/barrier.png',
  './sprites/droplet.png',
  './sprites/slime.png',
  './sprites/goo.png',
  './sprites/brute.png',
  './sprites/crusher.png',
  './sprites/mauler.png',
  './sprites/shell.png',
  './sprites/titan.png',
  './sprites/colossus.png',
  './sprites/grunt.png',
  './sprites/scout.png',
  './sprites/raider.png',
  './sprites/skitter.png',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  const isNav = e.request.mode === 'navigate' || url.pathname.endsWith('/') || url.pathname.endsWith('index.html');
  if (isNav) {
    e.respondWith(
      fetch(e.request, { cache: 'no-store' }).then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(e.request, copy));
        return res;
      }).catch(() => caches.match(e.request).then((r) => r || caches.match('./index.html')))
    );
    return;
  }
  if (url.pathname.endsWith('sw.js')) {
    e.respondWith(fetch(e.request, { cache: 'no-store' }));
    return;
  }
  e.respondWith(
    fetch(e.request).then((res) => {
      const copy = res.clone();
      caches.open(CACHE).then((c) => c.put(e.request, copy));
      return res;
    }).catch(() => caches.match(e.request))
  );
});
