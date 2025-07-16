
self.addEventListener("install", e => {
  e.waitUntil(
    caches.open("mrealm-cache").then(cache => {
      return cache.addAll([
        "./",
        "./index.html",
        "./emotion.html",
        "./mirror.html",
        "./heartbeat.html",
        "./alert.html",
        "./contact.html"
      ]);
    })
  );
});

self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request).then(response => {
      return response || fetch(e.request);
    })
  );
});
