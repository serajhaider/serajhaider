# The Cipher Stack — Setup

This package implements the original prompt's requested file structure and automation.

## 1. Create the profile repository
Create a **public repository named exactly `serajhaider`** under your GitHub account. GitHub will use its `README.md` as your profile README.

## 2. Copy the files
Copy all files from this package into that repository.

## 3. Add your portrait
Place your portrait at the repository root as `hero.png`.

Install full dependencies locally:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r scripts/requirements.txt
```

Then run:

```bash
python scripts/prep_photo.py hero.png
python scripts/make_ascii_svg.py
python scripts/make_info_card.py
python scripts/fetch_contributions.py
python scripts/render_heatmap_svg.py
```

## 4. Push
Commit and push the generated `source-prepped.png`, `hxni-ascii.svg`, `info-card.svg`, `contrib-heatmap.svg`, and `data/contributions.json`.

## 5. Enable automation
GitHub Actions will run `.github/workflows/update-profile-art.yml` daily at **06:17 UTC** and can also be run manually using **Run workflow**.

The CI intentionally installs only the lightweight requirements because the portrait preparation is a local asset-generation step.

## 6. Personal links
The original prompt asks for LinkedIn, Instagram, Facebook and email. Exact values were not available, so those are left as safe placeholders rather than inventing URLs.

## 7. Important GitHub limitation
GitHub sanitizes/restricts some HTML, CSS and SVG behavior inside README rendering. The generated SVG files are self-contained, while the README uses standard externally hosted SVG widgets for the typing and header effects. The daily workflow is independent of those external widgets.
