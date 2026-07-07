#!/usr/bin/env python3
"""Generate Obed Issakah's static academic site (GitHub Pages ready)."""
import random, pathlib

OUT = pathlib.Path(__file__).resolve().parent

NAV = [
    ("index.html", "Home"), ("about.html", "About"), ("research.html", "Research"),
    ("publications.html", "Publications"), ("projects.html", "Projects"),
    ("teaching.html", "Teaching"), ("blog.html", "Blog"), ("talks.html", "Talks"),
    ("gallery.html", "Gallery"), ("fun.html", "Fun"), ("cv.html", "CV"),
    ("contact.html", "Contact"),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Obed Issakah</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<!--INLINE_CSS-->
</head>
<body>
<nav class="nav"><div class="nav-inner">
<a class="brand" href="index.html">Obed <span>Issakah</span></a>
<div class="nav-links">{links}</div>
</div></nav>
"""

FOOT = """<footer><div class="wrap">
<div>© 2026 Obed Issakah · Chemical &amp; Biomolecular Engineering, University of Nebraska–Lincoln</div>
<div><a href="mailto:issakahobed7@gmail.com">Email</a> · <a href="https://linkedin.com/in/issakahobed">LinkedIn</a> · <a href="https://oissakah.github.io/myportfolio/">GitHub</a></div>
</div></footer>
</body></html>"""


def navlinks(current):
    out = []
    for href, label in NAV:
        cls = ' class="active"' if href == current else ""
        out.append(f'<a href="{href}"{cls}>{label}</a>')
    return "".join(out)


def micrograph_svg(seed=7):
    """Subtle composite-micrograph dot field: two particle populations
    (a nod to the PKS / CaCO3 filler work)."""
    rng = random.Random(seed)
    dots = []
    for _ in range(46):  # large PKS-like particles
        x, y, r = rng.randint(0, 1200), rng.randint(0, 340), rng.randint(9, 17)
        o = rng.uniform(0.08, 0.16)
        dots.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#7fd8cb" opacity="{o:.2f}"/>')
    for _ in range(120):  # fine CaCO3-like particles
        x, y, r = rng.randint(0, 1200), rng.randint(0, 340), rng.randint(2, 4)
        o = rng.uniform(0.10, 0.20)
        dots.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#e8c268" opacity="{o:.2f}"/>')
    return ('<svg class="micrograph" viewBox="0 0 1200 340" preserveAspectRatio="xMidYMid slice" '
            'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' + "".join(dots) + "</svg>")


PAGES = {}

# ----------------------------------------------------------------- HOME
PAGES["index.html"] = {
    "title": "Home",
    "desc": "Obed Issakah — PhD student in Chemical and Biomolecular Engineering at the University of Nebraska–Lincoln, working on ML for catalysis and materials design.",
    "body": f"""
<header class="hero">
{micrograph_svg()}
<div class="hero-inner">
<div class="hero-grid">
<div>
<div class="kicker">PhD Student · Chemical &amp; Biomolecular Engineering · University of Nebraska–Lincoln</div>
<h1>Obed Issakah</h1>
<p class="lede">I'm a PhD student in Chemical and Biomolecular Engineering at the University of Nebraska–Lincoln (Ock Lab), where I use machine learning, DFT, and atomistic simulation to design catalysts and materials — from PFAS-remediation catalysts to self-assembled nanomaterials.</p>
<p class="sub">B.Sc. Materials Engineering (First Class Honors), KNUST, Ghana · Princeton Pathways to Graduate School Scholar.</p>
<div class="btn-row">
<a class="btn primary" href="assets/Obed_Issakah_CV.pdf">Download CV</a>
<a class="btn" href="publications.html">Publications</a>
<a class="btn" href="mailto:issakahobed7@gmail.com">Email me</a>
<a class="btn" href="https://linkedin.com/in/issakahobed">LinkedIn</a>
</div>
</div>
<figure class="portrait">
<img src="assets/img/obed.jpg" alt="Obed Issakah">
<figcaption>Obed Issakah · Lincoln, NE</figcaption>
</figure>
</div>
</div>
</header>

<div class="wrap">
<section class="block">
<div class="section-head">
<div class="tag">Research snapshot</div>
<h2>What I work on</h2>
<p>Four threads run through my research: polymers, batteries, catalysis, and the AI/ML methods that tie them together.</p>
</div>
<div class="grid cols-2">
<div class="card media">
<img class="card-img" src="assets/img/polymers.jpg" alt="Molecular structure illustration">
<div class="card-body">
<div class="meta">Polymers &amp; composites</div>
<h3>Sustainable polymer composites</h3>
<p class="quiet">HDPE composites reinforced with palm kernel shell and CaCO₃ — turning agricultural waste into engineered material, with ML models predicting tensile properties.</p>
</div>
</div>
<div class="card media">
<img class="card-img" src="assets/img/batteries.jpg" alt="Illuminated battery cell among battery cells">
<div class="card-body">
<div class="meta">Energy storage</div>
<h3>Battery materials</h3>
<p class="quiet">ML-assisted screening of solid electrolytes for sodium-ion batteries, and porous-electrode modeling plus solvothermal synthesis of LiMn₂O₄ cathodes.</p>
</div>
</div>
<div class="card media">
<img class="card-img" src="assets/img/catalysis.jpg" alt="Molecules adsorbing on a catalyst surface">
<div class="card-body">
<div class="meta">Catalysis</div>
<h3>Computational heterogeneous catalysis</h3>
<p class="quiet">DFT workflows and machine-learned interatomic potentials for catalyst screening — PFAS remediation at UNL's Ock Lab, and CO₂-to-fuels MOF catalysts before that.</p>
</div>
</div>
<div class="card media">
<img class="card-img" src="assets/img/ai-ml.jpg" alt="Vitruvian-style illustration of an AI figure with scientific instruments">
<div class="card-body">
<div class="meta">AI &amp; ML for materials design</div>
<h3>Machine learning for materials</h3>
<p class="quiet">Graph neural networks, reinforcement learning, and interpretable models for high-throughput screening and structure–property prediction.</p>
</div>
</div>
</div>
</section>

<section class="block">
<div class="section-head">
<div class="tag">News</div>
<h2>Recent updates</h2>
</div>
<ul class="news">
<li><time>2026</time><div>Began my <strong>PhD in Chemical and Biomolecular Engineering</strong> at the University of Nebraska–Lincoln, joining the Ock Lab to work on ML for heterogeneous catalysis and nanomaterials.</div></li>
<li><time>2026</time><div>Paper published in <em>Results in Materials</em>: “Tuning of the tensile property of HDPE/CaCO₃/PKS composite using machine learning.” <a href="https://doi.org/10.1016/j.rinma.2026.100950">DOI</a></div></li>
<li><time>2025</time><div>Co-authored “Development and characterization of sustainable PKS/CaCO₃/HDPE hybrid composites for enhanced thermal and mechanical performance.” <a href="https://doi.org/10.1177/26349833251411841">DOI</a></div></li>
<li><time>2025</time><div>Paper published in <em>Results in Materials</em> on the effect of partially replacing palm kernel shell with calcium carbonate in HDPE composites. <a href="https://doi.org/10.1016/j.rinma.2025.100668">DOI</a></div></li>
<li><time>2024</time><div>Selected as a <strong>Princeton Pathways to Graduate School Scholar</strong> — 1 of 40 chosen from 250+ applicants worldwide.</div></li>
<li><time>2024</time><div>Co-authored a review on covalent organic frameworks in <em>Coordination Chemistry Reviews</em>. <a href="https://doi.org/10.1016/j.ccr.2024.216121">DOI</a></div></li>
<li><time>2023</time><div>Received the <strong>Vice Chancellor's Excellence Award</strong> (one of 3 students university-wide) for contributions to SDG 12 and 13; graduated with First Class Honors.</div></li>
</ul>
</section>
</div>
""",
}

# ----------------------------------------------------------------- ABOUT
PAGES["about.html"] = {
    "title": "About",
    "desc": "About Obed Issakah — academic journey, research interests, and life outside the lab.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">About</div>
<h1>About me</h1>
<p>A materials engineer from Ghana, now a PhD student in Nebraska, who believes the next generation of materials will be designed with data as much as with furnaces and extruders.</p>
</header>

<section class="block">
<h2>Academic journey</h2>
<p>I studied Materials Engineering at the Kwame Nkrumah University of Science and Technology (KNUST) in Kumasi, Ghana, graduating in 2023 with First Class Honors. My undergraduate thesis — on partially replacing particulate palm kernel shell with calcium carbonate in HDPE composites — got me hooked on a simple question: <em>can we make better materials from what we already have?</em></p>
<p>That question has since pulled me in two directions at once. Experimentally, toward sustainable composites and battery materials. Computationally, toward machine learning and ab initio methods that let us search materials space far faster than trial-and-error allows. From 2022 to 2025 I worked as a research assistant across several groups at KNUST, collaborating with supervisors at KNUST and Virginia Tech, and served as a teaching and research assistant in the department.</p>
<p>In 2026 I began my PhD in Chemical and Biomolecular Engineering at the University of Nebraska–Lincoln, in Prof. Janghoon Ock's lab. My research focus is computational heterogeneous catalysis and ML/AI for materials design — currently machine learning for PFAS-remediation catalysis, and graph neural networks for percolation in self-assembled nanomaterials.</p>
</section>

<section class="block">
<h2>Research interests</h2>
<div class="grid cols-2">
<div class="card"><h3>Machine learning for materials design</h3><p class="quiet">Property prediction, high-throughput screening, and interpretable models that give physical insight — not just numbers.</p></div>
<div class="card"><h3>Sustainable composites</h3><p class="quiet">Valorizing agricultural waste like palm kernel shell as filler in polymer composites.</p></div>
<div class="card"><h3>Energy storage</h3><p class="quiet">Solid electrolytes for sodium-ion batteries; LiMn₂O₄ cathodes and porous-electrode modeling.</p></div>
<div class="card"><h3>Computational catalysis</h3><p class="quiet">DFT, machine-learned interatomic potentials, and graph neural networks for catalyst discovery — PFAS remediation and CO₂ reduction.</p></div>
</div>
</section>

<section class="block">
<h2>Beyond the lab</h2>
<p>Outside research, I mentor undergraduate students in the materials engineering department and stay active in my community.</p>
<div class="placeholder"><strong>Fill me in:</strong> add a short personal paragraph here — hobbies, favorite books or music, languages you speak, a fun fact or two. See the <a href="fun.html">Fun page</a> for a place to expand on these.</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- RESEARCH
PAGES["research.html"] = {
    "title": "Research",
    "desc": "Research experience of Obed Issakah: ML for composites, sodium-ion solid electrolytes, LiMn2O4 batteries, and computational catalysis.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Research</div>
<h1>Research experience</h1>
<p>Each project below pairs a materials problem with the tool best suited to it — sometimes an extruder and a tensile tester, sometimes a neural network.</p>
</header>

<section class="block">
<div class="entry">
<div class="meta">JAN 2026 – PRESENT · Ock Lab, University of Nebraska–Lincoln · Supervisor: Prof. Janghoon Ock</div>
<h3>Machine learning for heterogeneous catalysis (PFAS remediation)</h3>
<ul>
<li>Implemented DFT workflows and machine-learned interatomic potentials (UMA) to accelerate catalyst screening for PFAS remediation, enabling rapid evaluation of adsorption/activation energetics and reaction pathways.</li>
<li>Investigating governing principles of catalytic behavior by linking computed descriptors (binding energies, electronic-structure metrics, surface site motifs) to activity/selectivity trends, guiding rational catalyst design.</li>
</ul>
</div>

<div class="entry">
<div class="meta">JAN 2026 – PRESENT · Ock Lab, University of Nebraska–Lincoln · Supervisors: Prof. Ock &amp; Prof. Saraf</div>
<h3>Graph neural networks for percolation in self-assembled nanomaterials</h3>
<ul>
<li>Modeling self-assembled nanoparticle networks as graphs and training GNNs to quantify percolation onset, conductive cluster formation, and structure–property relationships from microstructure data.</li>
<li>Applying reinforcement learning to propose network growth paths that improve percolation probability and charge-transport efficiency, supporting design of high-performance electronic materials.</li>
</ul>
</div>

<div class="entry">
<div class="meta">JUN 2025 – JUL 2025 · KNUST · Supervisor: Dr. Eric Asare</div>
<h3>Machine learning for hybrid composite material design</h3>
<ul>
<li>Implemented classical ML models to predict tensile strength of HDPE/PKS/CaCO₃ hybrid composites using curated experimental datasets and feature engineering.</li>
<li>Optimized and validated models via systematic hyperparameter tuning (grid search), reporting strong predictive accuracy and robust generalization using cross-validation.</li>
</ul>
</div>

<div class="entry">
<div class="meta">AUG 2024 – DEC 2025 · KNUST · Supervisor: Prof. Luke Achenie (Virginia Tech)</div>
<h3>ML-assisted high-throughput screening of solid electrolytes for solid-state sodium-ion batteries</h3>
<ul>
<li>Integrated ML models with atomistic simulations (ab initio molecular dynamics) to screen candidate solid electrolytes, prioritizing compositions with favorable Na⁺ transport and stability descriptors.</li>
<li>Built end-to-end workflows for model training, evaluation, and uncertainty-aware selection of promising materials to accelerate down-selection versus brute-force computation.</li>
</ul>
</div>

<div class="entry">
<div class="meta">JUN 2024 – DEC 2024 · Energy Materials &amp; Sustainability Group, KNUST · Supervisor: Prof. Kwadwo Mensah-Darkwa</div>
<h3>High-energy-density LiMn₂O₄ batteries for tricycles</h3>
<ul>
<li>Used a multiphase porous electrode theory (MPET) simulator to study open-circuit voltage behavior of LMO cathodes under various conditions.</li>
<li>Synthesized porous microsphere LiMn₂O₄ cathode material via the solvothermal method.</li>
</ul>
</div>

<div class="entry">
<div class="meta">JUN 2023 – AUG 2023 · Undergraduate thesis, KNUST · Supervisor: Dr. Eric A. Asare</div>
<h3>Partial replacement of palm kernel shell with CaCO₃ in HDPE composites</h3>
<ul>
<li>Developed PKS/CaCO₃/HDPE hybrid composites and studied the effect of PKS addition.</li>
<li>Found an 80% improvement in hardness for large PKS particles (500 µm) versus small (125 µm), and a 5% tensile-strength improvement for small particles.</li>
</ul>
</div>

<div class="entry">
<div class="meta">AUG 2022 – SEP 2024 · Computational Catalysis, KNUST · Supervisor: Prof. Luke Achenie (Virginia Tech)</div>
<h3>High-throughput screening of porous materials for photoelectrochemical CO₂ reduction</h3>
<ul>
<li>Implemented a crystal graph convolutional neural network (CGCNN) and Monte Carlo simulation to accelerate the design of heterogeneous catalysts for CO₂ reduction.</li>
<li>Developed interpretability models to extract physical and chemical insight from MOF structures and their catalytic behavior.</li>
</ul>
</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- PUBLICATIONS
PAGES["publications.html"] = {
    "title": "Publications",
    "desc": "Peer-reviewed publications by Obed Issakah.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Publications</div>
<h1>Publications</h1>
<p>Peer-reviewed journal articles. A Google Scholar profile link can be added here once set up.</p>
</header>

<section class="block">
<div class="pub">
<div class="title">Tuning of the tensile property of HDPE/CaCO₃/PKS composite using machine learning</div>
<div class="authors"><strong>Issakah Obed</strong>, Abdul-Manan Kayaba, Eric Kwame Anokye Asare · <em>Results in Materials</em>, 2026</div>
<div class="links"><a href="https://doi.org/10.1016/j.rinma.2026.100950">DOI: 10.1016/j.rinma.2026.100950</a></div>
</div>

<div class="pub">
<div class="title">Development and characterization of sustainable PKS/CaCO₃/HDPE hybrid composites for enhanced thermal and mechanical performance</div>
<div class="authors">Emmanuel Kofi Frimpong, Abdul-Manan Kayaba, Stefania Akromah, Ezekiel Edward Nettey-Oppong, Emmanuel Essel Mensah, <strong>Obed Issakah</strong>, Eric Asare · 2025</div>
<div class="links"><a href="https://doi.org/10.1177/26349833251411841">DOI: 10.1177/26349833251411841</a></div>
</div>

<div class="pub">
<div class="title">Effect of partial replacement of particulate palm kernel shell with calcium carbonate on the mechanical properties of HDPE/CaCO₃ composite</div>
<div class="authors"><strong>Issakah Obed</strong>, Abdul M. Kayaba, Eric K. A. Asare · <em>Results in Materials</em>, 2025</div>
<div class="links"><a href="https://doi.org/10.1016/j.rinma.2025.100668">DOI: 10.1016/j.rinma.2025.100668</a></div>
</div>

<div class="pub">
<div class="title">Synergistic effects of micro- and macro-sized palm kernel shell fillers on the tensile properties of HDPE composites</div>
<div class="authors">A. M. Kayaba, <strong>Issakah Obed</strong>, S. Akromah, E. E. Nartey-Oppong, E. K. A. Asare · <em>Royal Society Open Science</em></div>
<div class="links"><a href="https://doi.org/10.1098/rsos.241911">DOI: 10.1098/rsos.241911</a></div>
</div>

<div class="pub">
<div class="title">Advances and challenges in covalent organic frameworks as an emerging class of materials for energy and environmental concerns</div>
<div class="authors">Daniel Nframah Ampong, Elijah Effah, Emmanuel Acheampong Tsiwah, Anuj Kumar, Emmanuel Agyekum, Esther Naa Ayorkor Doku, <strong>Issakah Obed</strong>, Frank Ofori Agyemang, Kwadwo Mensah-Darkwa, Ram K. Gupta · <em>Coordination Chemistry Reviews</em>, 2024</div>
<div class="links"><a href="https://doi.org/10.1016/j.ccr.2024.216121">DOI: 10.1016/j.ccr.2024.216121</a></div>
</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- PROJECTS
PAGES["projects.html"] = {
    "title": "Projects",
    "desc": "Research and side projects by Obed Issakah.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Projects</div>
<h1>Projects</h1>
<p>Selected research projects and initiatives. Code links can be added as repositories are made public.</p>
</header>

<section class="block">
<div class="grid cols-2">
<div class="card">
<div class="meta">Machine learning · Python</div>
<h3>Tensile-property prediction for hybrid composites</h3>
<p class="quiet">Classical ML pipeline with feature engineering and grid-search optimization, predicting tensile strength of HDPE/PKS/CaCO₃ composites with cross-validated accuracy. Basis of a 2026 <em>Results in Materials</em> paper.</p>
</div>
<div class="card">
<div class="meta">Deep learning · Simulation</div>
<h3>CGCNN screening of MOF catalysts</h3>
<p class="quiet">Crystal graph convolutional neural network plus Monte Carlo simulation for screening porous materials for photoelectrochemical CO₂ reduction, with interpretability models for physical insight.</p>
</div>
<div class="card">
<div class="meta">Battery modeling · MPET</div>
<h3>LiMn₂O₄ cathode simulation &amp; synthesis</h3>
<p class="quiet">Multiphase porous electrode theory simulations of LMO open-circuit voltage behavior, paired with solvothermal synthesis of porous microsphere LiMn₂O₄ cathodes.</p>
</div>
<div class="card">
<div class="meta">Team lead · Energy innovation</div>
<h3>KNUST Green Energy Challenge</h3>
<p class="quiet">Led a 4-member team proposing diesel fuel extraction from plastic waste as an alternative energy solution — top-3 ranking at the penultimate stage of the competition.</p>
</div>
</div>
<div class="placeholder" style="margin-top:1rem;"><strong>Optional:</strong> add personal or open-source side projects here, with screenshots and GitHub links.</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- TEACHING
PAGES["teaching.html"] = {
    "title": "Teaching",
    "desc": "Teaching and mentoring by Obed Issakah at KNUST.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Teaching &amp; mentoring</div>
<h1>Teaching &amp; mentoring</h1>
<p>I enjoy making difficult concepts click — whether in a metallurgy classroom or a one-on-one mentoring session.</p>
</header>

<section class="block">
<div class="entry">
<div class="meta">SEP 2023 – PRESENT · KNUST</div>
<h3>Teaching &amp; Research Assistant — Physical Metallurgy, Pyrometallurgy</h3>
<ul>
<li>Facilitated classroom discussions and assisted 100+ students in comprehending complex concepts, encouraging active learning and improving class performance.</li>
<li>Provided feedback on assignments and assessments to support students' academic growth.</li>
</ul>
</div>

<div class="entry">
<div class="meta">FEB 2023 – PRESENT · Plastic Electronics &amp; Photonics Student Club, KNUST</div>
<h3>Mentor</h3>
<ul>
<li>Conduct regular one-on-one sessions on academic challenges and personal development with 7 undergraduate students in the materials engineering department.</li>
</ul>
</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- FUN
PAGES["fun.html"] = {
    "title": "Fun",
    "desc": "Life outside research — hobbies, photos, books, and travel.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Fun</div>
<h1>Beyond the lab</h1>
<p>The 30% of the site that's about being a person, not a publication list.</p>
</header>

<section class="block">
<div class="grid cols-2">
<div class="card">
<div class="meta">Gallery</div>
<h3>Photos</h3>
<p class="quiet">Add curated albums here — conferences, lab life, campus, travel. Drop images into <code>assets/gallery/</code> and link them.</p>
</div>
<div class="card">
<div class="meta">Books</div>
<h3>Reading list</h3>
<p class="quiet">List books you've enjoyed with one-sentence reviews — fiction, non-fiction, science, philosophy.</p>
</div>
<div class="card">
<div class="meta">Travel</div>
<h3>Places I've been</h3>
<p class="quiet">Add a list or map of places you've visited — with photos, short stories, favorite food, and recommendations for each trip.</p>
</div>
<div class="card">
<div class="meta">Hobbies</div>
<h3>What I do for fun</h3>
<p class="quiet">Music? Football? Cooking? Chess? Add short write-ups or pictures here.</p>
</div>
<div class="card">
<div class="meta">Fun facts</div>
<h3>Rapid-fire</h3>
<p class="quiet">Favorite programming language, favorite quote, bucket list, morning routine — a few quick lines that make the page memorable.</p>
</div>
</div>
<div class="placeholder" style="margin-top:1rem;"><strong>This page is a scaffold:</strong> everything here is a placeholder waiting for your real photos, hobbies, and stories. Replace the card text above with your own content.</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- CV
PAGES["cv.html"] = {
    "title": "CV",
    "desc": "Curriculum vitae of Obed Issakah — education, awards, skills, and downloadable PDF.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Curriculum vitae</div>
<h1>CV</h1>
<p>A condensed version is below; the full PDF has complete research and publication details.</p>
<div class="btn-row"><a class="btn primary" href="assets/Obed_Issakah_CV.pdf">Download full CV (PDF)</a></div>
</header>

<section class="block">
<h2>Education</h2>
<table class="cv">
<tr><td>2026 – Present</td><td><strong>PhD, Chemical and Biomolecular Engineering</strong>, University of Nebraska–Lincoln (UNL), Lincoln, Nebraska<br>Research focus: computational heterogeneous catalysis, ML/AI for materials design</td></tr>
<tr><td>2019 – 2023</td><td><strong>B.Sc. Materials Engineering</strong>, Kwame Nkrumah University of Science and Technology (KNUST), Kumasi, Ghana<br>First Class Honors — CWA 73.02/100 (GPA 3.7/4.0)</td></tr>
</table>
</section>

<section class="block">
<h2>Awards, grants &amp; honors</h2>
<table class="cv">
<tr><td>2024</td><td><strong>Princeton Pathways to Graduate School Scholar</strong> — 1 of 40 scholars selected from 250+ applicants worldwide for graduate-application mentorship from Princeton's School of Engineering and Applied Science.</td></tr>
<tr><td>2023</td><td><strong>Vice Chancellor's Excellence Award</strong> — awarded to only 3 students university-wide for outstanding contribution to SDG 12 and 13.</td></tr>
<tr><td>2023</td><td><strong>Materials Innovation Hub Excellence Award</strong> — awarded to one person for high research involvement in a cohort of 100+.</td></tr>
<tr><td>2022</td><td><strong>Responsible Artificial Intelligence Laboratory (RAIL) Grant</strong> — $1,000 grant for research in computational catalysis for CO₂ reduction.</td></tr>
<tr><td>2019 – 2023</td><td><strong>Goldfields Ghana Scholar</strong> — awarded for high academic excellence in the West Africa Certificate Examination in the community.</td></tr>
</table>
</section>

<section class="block">
<h2>Skills &amp; tools</h2>
<div class="skills">
<span>Python</span><span>MATLAB</span><span>Microsoft Suite</span><span>Avogadro</span>
<span>Quantum ESPRESSO</span><span>ASE</span><span>VESTA</span>
<span>Machine learning</span><span>Ab initio molecular dynamics</span><span>MPET</span>
</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- BLOG
PAGES["blog.html"] = {
    "title": "Blog",
    "desc": "Blog by Obed Issakah — research explainers, tutorials, and notes on materials science and machine learning.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Blog</div>
<h1>Blog</h1>
<p>Notes on materials, machine learning, and the research journey — written for a broad audience.</p>
</header>

<section class="block">
<div class="placeholder"><strong>No posts yet.</strong> When you write your first post, copy the entry template below, save the post as its own HTML file (e.g. <code>posts/my-first-post.html</code>), and link it here.</div>

<div class="entry" style="margin-top:1rem;">
<div class="meta">TEMPLATE · DATE GOES HERE</div>
<h3><a href="#">Post title goes here</a></h3>
<p>One- or two-sentence teaser describing what the post covers. Ideas from your own work: explaining how ML predicts composite properties in plain language, what it's like doing computational research from Ghana, a Quantum ESPRESSO or ASE tutorial, or lessons from the Princeton Pathways program.</p>
</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- TALKS
PAGES["talks.html"] = {
    "title": "Talks",
    "desc": "Talks, posters, and presentations by Obed Issakah.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Talks &amp; presentations</div>
<h1>Talks &amp; presentations</h1>
<p>Conference talks, posters, seminar presentations, and guest lectures — with slides or video where available.</p>
</header>

<section class="block">
<div class="placeholder"><strong>Add your talks here.</strong> Your CV lists publications but no specific talks, so I didn't want to guess. Use the template below for each entry, and link slides (PDF) or a video if you have them.</div>

<div class="entry" style="margin-top:1rem;">
<div class="meta">TEMPLATE · EVENT · LOCATION · DATE</div>
<h3>Talk or poster title goes here</h3>
<p>One sentence on what was presented. <a href="#">[Slides]</a> <a href="#">[Video]</a></p>
</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- GALLERY
PAGES["gallery.html"] = {
    "title": "Gallery",
    "desc": "Photo gallery — curated albums from conferences, lab life, travel, and campus.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Gallery</div>
<h1>Gallery</h1>
<p>Curated albums rather than a photo dump — a few good pictures beat a hundred average ones.</p>
</header>

<section class="block">
<div class="grid cols-3">
<div class="card"><div class="meta">Album</div><h3>Conferences</h3><p class="quiet">Add photos to <code>assets/gallery/conferences/</code> and embed them here with <code>&lt;img&gt;</code> tags.</p></div>
<div class="card"><div class="meta">Album</div><h3>Lab life</h3><p class="quiet">Photos from the lab — synthesis, testing, the team.</p></div>
<div class="card"><div class="meta">Album</div><h3>Campus &amp; KNUST</h3><p class="quiet">Scenes from around the university.</p></div>
<div class="card"><div class="meta">Album</div><h3>Travel</h3><p class="quiet">Trips and places, paired with the Travel section on the Fun page.</p></div>
<div class="card"><div class="meta">Album</div><h3>Nature</h3><p class="quiet">Landscapes and outdoors shots.</p></div>
<div class="card"><div class="meta">Album</div><h3>Friends &amp; community</h3><p class="quiet">People and moments worth remembering.</p></div>
</div>
<div class="placeholder" style="margin-top:1rem;"><strong>How to add photos:</strong> create <code>assets/gallery/</code>, drop images in, then replace a card's text with e.g. <code>&lt;img src="assets/gallery/conferences/photo1.jpg" alt="..." style="width:100%; border-radius:3px;"&gt;</code>.</div>
</section>
</div>
""",
}

# ----------------------------------------------------------------- CONTACT
PAGES["contact.html"] = {
    "title": "Contact",
    "desc": "Contact Obed Issakah.",
    "body": """
<div class="wrap">
<header class="page-head">
<div class="tag">Contact</div>
<h1>Get in touch</h1>
<p>I'm happy to hear from potential collaborators, students, and anyone curious about catalysis, materials, and ML.</p>
</header>

<section class="block">
<div class="grid cols-2">
<div class="card">
<div class="meta">Email</div>
<h3><a href="mailto:issakahobed7@gmail.com">issakahobed7@gmail.com</a></h3>
<p class="quiet">The fastest way to reach me.</p>
</div>
<div class="card">
<div class="meta">Location</div>
<h3>University of Nebraska–Lincoln</h3>
<p class="quiet">Department of Chemical and Biomolecular Engineering, Lincoln, Nebraska.</p>
</div>
<div class="card">
<div class="meta">Profiles</div>
<h3>Online</h3>
<p class="quiet"><a href="https://linkedin.com/in/issakahobed">LinkedIn</a> · <a href="https://oissakah.github.io/myportfolio/">GitHub / Portfolio</a></p>
</div>
<div class="card">
<div class="meta">Academic profiles</div>
<h3>Scholar &amp; ORCID</h3>
<p class="quiet">Add your Google Scholar and ORCID links here once created.</p>
</div>
</div>
</section>
</div>
""",
}


def build():
    css = (OUT / "assets" / "style.css").read_text(encoding="utf-8")
    inline = "<style>\n" + css + "\n</style>"
    for fname, page in PAGES.items():
        html = (HEAD.format(title=page["title"], desc=page["desc"],
                            links=navlinks(fname)) + page["body"] + FOOT)
        html = html.replace("<!--INLINE_CSS-->", inline)
        (OUT / fname).write_text(html, encoding="utf-8")
        print("wrote", fname)


if __name__ == "__main__":
    build()
