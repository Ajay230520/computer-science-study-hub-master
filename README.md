# M.Tech Software Engineering — Semester 1 Study Hub

A structured, practical, research-aware repository for the six subjects in my M.Tech Software Engineering Semester 1. The first four are the **core technical subjects**; Technical Report Writing and Research Methodology support academic writing and research.

## Semester 1 dashboard

### Core technical subjects
1. **[Advanced Data Structures](advanced-data-structures/README.md)** — concepts, invariants, worked traces, complexity, implementation, labs, and exam practice.
2. **[Machine Learning](machine-learning/README.md)** — mathematical foundations, algorithms, evaluation, Python labs, and research-aware case studies.
3. **[Mathematical Foundations of Computer Science](mathematics/README.md)** — logic, proofs, sets, relations, functions, graphs, combinatorics, recurrences, probability/statistics, and ML mathematics.
4. **[Digital Image Processing](digital-image-processing/README.md)** — image fundamentals, enhancement, filtering, transforms, segmentation, morphology, compression, and practical labs.

### Supporting academic subjects
5. **[Technical Report Writing](technical-report-writing/README.md)** — report structure, technical clarity, figures/tables, citations, IEEE-style formatting, and presentations.
6. **[Research Methodology](research-methodology/README.md)** — research questions, literature reviews, methods, experimental design, ethics, reproducibility, and research-paper evaluation.

## Study website

- **Website source:** [`docs/`](docs/index.html)
- **MFCS practical register:** [`docs/practicals.html`](docs/practicals.html)
- The GitHub Pages deployment workflow is in [`.github/workflows/deploy-study-site.yml`](.github/workflows/deploy-study-site.yml). After enabling **Settings → Pages → Build and deployment → GitHub Actions** and allowing the workflow to finish, the expected site URL is `https://ajay230520.github.io/computer-science-study-hub-master/`. The site is not confirmed live until GitHub Pages reports a successful deployment.

## Official syllabus references

Searchable Markdown references transcribed from the six files shared for this study hub are in [syllabus/](syllabus/README.md). Note that the uploaded Technical Report Writing document is a Summer 2026 exam paper, not a syllabus. The GTU syllabus PDFs state A.Y. 2024–25, so confirm current applicability with LDCE/GTU.

## How each topic should be taught and documented

- Start from prerequisites and a plain-language explanation.
- Give a precise definition, notation, assumptions, and a diagram when helpful.
- Work through examples from easy to intermediate to challenging, explaining every meaningful step.
- Connect theory to realistic engineering problems and verified case studies.
- Put runnable implementations, tests, and setup instructions in the relevant code/lab folder.
- Add exercises, hints/solutions, common mistakes, revision cards, and exam-style questions.
- Cite credible original papers, official documentation, standards, and dataset sources. Never invent results or references.

## Repository structure

Each subject has its own roadmap. As material grows, keep `notes/`, `code/` or `labs/`, `exercises/`, and `case-studies/` separate where useful. Shared standards are in [CONTRIBUTING.md](CONTRIBUTING.md); reusable formats are in [templates/](templates/); study reflections go in [learning-log/](learning-log/).

## Progress policy

A roadmap is not a completed course. We will mark topics as planned, in progress, or reviewed honestly. After each study session, the studied material should be added to the correct subject and checked for accuracy before committing.

## Suggested cross-subject order

Mathematical foundations support Machine Learning and Image Processing. Advanced Data Structures develops independent algorithmic reasoning. Research Methodology and Technical Report Writing should be used throughout the semester to document experiments and communicate results.
