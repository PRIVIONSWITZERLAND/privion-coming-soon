# PRIVION — Coming soon

Standalone, responsive landing page for https://test.privion.ch.

Plain HTML and CSS; no build step, JavaScript, tracking, cookies, remote fonts or dependencies. Abstract animated artwork is drawn in CSS and SVG. Respects reduced-motion preferences.

## Local preview

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Open http://127.0.0.1:8080. Publish the static files with any HTTPS-capable static host. Only expose this directory, never the parent workspace or the backend prototype.
