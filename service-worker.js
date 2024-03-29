const CACHE_NAME = "v1.0.3";
const urlsToCache = ["/", "/index.html",];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return fetch(event.request).then((response) => {
        cache.put(event.request, response.clone());
      });
    })
  );
});
