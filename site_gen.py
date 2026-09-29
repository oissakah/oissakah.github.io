#!/usr/bin/env python3
"""Safe site audit helper for Obed Issakah's GitHub Pages portfolio.

The portfolio is maintained directly as static HTML + assets/style.css.
This script intentionally DOES NOT regenerate or overwrite pages. It checks
for common consistency problems so manual edits remain the source of truth.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
PRIMARY_PAGES = [
    "index.html",
    "research.html",
    "projects.html",
    "publications.html",
    "about.html",
    "cv.html",
    "contact.html",
    "nanonecklace.html",
    "pfas-catalysis.html",
    "ml-composites.html",
]
REQUIRED_NAV = ["Home", "Research", "Projects", "Publications", "About", "CV", "Contact"]


def audit_page(path: Path) -> list[str]:
    issues = []
    text = path.read_text(encoding="utf-8")
    if 'href="assets/style.css"' not in text:
        issues.append("missing shared stylesheet link")
    if "oissakah.github.io/myportfolio" in text:
        issues.append("contains legacy myportfolio URL")
    if "https://github.com/oissakah" not in text:
        issues.append("missing GitHub profile link")
    for label in REQUIRED_NAV:
        if f">{label}<" not in text:
            issues.append(f"navigation missing {label}")
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = href.split("#", 1)[0].split("?", 1)[0]
        if not clean:
            continue
        target = ROOT / clean
        if not target.exists():
            issues.append(f"local link target not found: {clean}")
    return issues


def main() -> int:
    failures = 0
    print("Portfolio audit\n===============")
    for name in PRIMARY_PAGES:
        path = ROOT / name
        if not path.exists():
            print(f"FAIL  {name}: file missing")
            failures += 1
            continue
        issues = audit_page(path)
        if issues:
            failures += 1
            print(f"FAIL  {name}")
            for issue in issues:
                print(f"      - {issue}")
        else:
            print(f"OK    {name}")
    if not (ROOT / "assets" / "style.css").exists():
        print("FAIL  assets/style.css: file missing")
        failures += 1
    print()
    if failures:
        print(f"Audit completed with {failures} page/file issue group(s).")
        return 1
    print("Audit passed. Primary portfolio pages are internally consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())