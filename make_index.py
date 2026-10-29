"""Build index.html (the GitHub Pages copy) from olm_trainer.html.

olm_trainer.html is written for Claude artifacts, which add the page skeleton when publishing.
A normal website needs that skeleton in the file, so this adds the doctype, <html> and the
mobile viewport tag. Run it after every change to olm_trainer.html, then commit and push.
"""
from pathlib import Path

here = Path(__file__).parent
page = (here / "olm_trainer.html").read_text(encoding="utf-8")

head = (
    "<!doctype html>\n"
    '<html lang="en">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
)
(here / "index.html").write_text(head + page + "\n</html>\n", encoding="utf-8")
print("index.html written")
