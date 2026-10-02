# PRIVION — Coming soon

Standalone, responsive landing page for https://test.privion.ch.

Plain HTML and CSS; no build step, JavaScript, tracking, cookies, remote fonts or dependencies. Abstract animated artwork is drawn in CSS and SVG. Respects reduced-motion preferences.

## Local preview

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Open http://127.0.0.1:8080.

## Deployment

Hosted on Cloudflare Pages, project `privion-coming-soon`, using Direct Upload.

- Public domain: https://test.privion.ch
- Fallback URL: https://privion-coming-soon.pages.dev
- DNS: `test` CNAME → `privion-coming-soon.pages.dev`, managed by Cloudflare.
- HTTPS certificates are managed by Cloudflare.
- Website hosting runs independently of this workstation and the backend prototype.

To publish changes, commit the updated files to GitHub, then run:

```sh
python3 package-site.py
```

In Cloudflare, open **Workers & Pages → privion-coming-soon → Create deployment**, choose production, upload `site.zip` and deploy. Only the six public assets are packaged. No credentials are stored in this repository. GitHub commits do not automatically deploy; this project uses Direct Upload.

Check the page, CSS, favicon and privacy page over HTTPS after publishing, and inspect mobile layout. `_headers` supplies CSP, referrer policy and permissions restrictions. The site has no forms, launch date or claims that the app is already available.
