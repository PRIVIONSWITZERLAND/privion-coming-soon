"""Package only public website assets for Cloudflare Pages Direct Upload."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parent
output = root / "site.zip"
assets = ("index.html", "style.css", "favicon.svg", "datenschutz.html", "robots.txt", "_headers")
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    for asset in assets:
        archive.write(root / asset, asset)
print(f"Created {output} with {len(assets)} public assets")
