# Obed Issakah — Academic Research Portfolio

GitHub Pages portfolio for **Obed Issakah**, focused on computational materials, physics-informed AI, graph-based transport, atomistic simulation, and materials design.

Live site: `https://oissakah.github.io/`

## Primary site structure

```text
index.html            Research-focused homepage
research.html         Current research program and selected earlier work
projects.html         Selected projects with methods, outcomes, paper/code links
nanonecklace.html     Flagship nanonecklace transport project
pfas-catalysis.html   Computational catalysis project for PFAS remediation
publications.html     Journal articles and preprints
about.html            Academic journey and research identity
cv.html               Condensed CV + downloadable PDF
contact.html          Contact and professional links
assets/
  style.css           Shared design system
  Obed_Issakah_CV.pdf Downloadable CV
  img/                Portrait and supporting imagery
```

Legacy pages such as `blog.html`, `talks.html`, `teaching.html`, and `gallery.html` remain in the repository but are intentionally **not included in the primary navigation** until they contain polished, current material.

## Design system

The site uses a restrained academic/scientific visual system:

- Zilla Slab for display typography
- IBM Plex Sans for body text
- IBM Plex Mono for research labels and metadata
- Teal / slate / gold palette
- Responsive static HTML and CSS
- Scientific project cards, method tags, direct paper/code links, and research-story layouts

All primary pages reference the shared stylesheet:

```html
<link rel="stylesheet" href="assets/style.css">
```

Edit `assets/style.css` once to change the visual system across the primary site.

## Editing workflow

The static HTML files are the source of truth. Edit the relevant `.html` file directly and update `assets/style.css` for shared styling.

The previous page generator was retired because generated content and manually edited pages had diverged. `site_gen.py` is now a **non-destructive audit helper** and does not write or overwrite site files.

Run locally with:

```bash
python3 site_gen.py
```

The audit checks primary pages for:

- shared stylesheet references
- required primary navigation items
- local broken-link targets
- GitHub profile links
- legacy `myportfolio` URLs

## Current research emphasis

The portfolio is intentionally organized around the current research identity:

1. **Nanomaterial electron transport** — graph-based Kirchhoff modeling, voltage-driven percolation, internal current dynamics, and GNN surrogates.
2. **Computational catalysis for PFAS remediation** — DFT, VASP, ASE, machine-learned interatomic potentials, adsorption energetics, and surface screening.
3. **AI for materials discovery** — graph learning, interpretable ML, high-throughput screening, and materials informatics.
4. **Earlier materials research** — sustainable composites, batteries, and porous-material catalyst screening.

## Featured research assets

The nanonecklace project page uses the real causal-framework image stored in the public research repository:

```text
https://github.com/oissakah/graph-based-nanoparticle-necklace-network/tree/main/framework_diagram
```

The PFAS page intentionally presents the scientific workflow without publishing unpublished numerical results. Public adsorption structures, benchmark figures, code, or manuscript links can be added later when released.

## Deployment

This repository is named `oissakah.github.io`, so the `main` branch root is served through GitHub Pages at:

```text
https://oissakah.github.io/
```