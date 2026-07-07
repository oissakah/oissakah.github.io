# Obed Issakah — Personal Academic Website

A static, dependency-free website (plain HTML + CSS) ready for GitHub Pages.

## Structure

```
index.html          Home (hero, research snapshot, news)
about.html          Academic journey + personal section
research.html       Research experience (5 projects)
publications.html   Journal articles with DOI links
projects.html       Research & side projects
teaching.html       Teaching & mentoring
blog.html           Blog (scaffold — add posts)
talks.html          Talks & presentations (scaffold — add entries)
gallery.html        Photo albums (scaffold — add images)
fun.html            Hobbies / travel / books (scaffold to fill in)
cv.html             Condensed CV + PDF download
contact.html        Contact info & profiles
assets/
  style.css         All styling
  Obed_Issakah_CV.pdf
```

## Deploy on GitHub Pages

**Option A — main personal site (recommended):**
1. Create a repository named exactly `oissakah.github.io` (public).
2. Upload all files in this folder to the repository root.
3. Wait a minute or two; the site will be live at `https://oissakah.github.io/`.

**Option B — project site:**
1. Create any repository (e.g. `website`) and upload the files.
2. Go to Settings → Pages → set Source to "Deploy from a branch", branch `main`, folder `/ (root)`.
3. The site will be live at `https://oissakah.github.io/website/`.

Note: you already have a repo serving `oissakah.github.io/myportfolio/`. If you use Option A, that project site keeps working at its own URL; the new site takes the root URL.

## Things to customize

- **Photo:** add a headshot to `assets/` and place it in the hero on `index.html`.
- **Placeholders:** the About, Fun, Projects, and Contact pages contain clearly marked dashed boxes for personal content (hobbies, books, gallery, Google Scholar/ORCID links). Replace them with your own material.
- **News:** add new items to the list on `index.html` as things happen.
- **Colors/fonts:** everything is controlled by the CSS variables at the top of `assets/style.css`.
