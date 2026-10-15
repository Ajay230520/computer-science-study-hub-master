# Contribution and Content Quality Standard

This repository should be a reliable learning resource, not an unreviewed dump of generated text.

## Standard for a substantial topic
1. **Metadata:** title, subject, status, prerequisites, learning objectives, last reviewed.
2. **Intuition:** everyday explanation and where its analogy breaks.
3. **Formal definition:** precise terms, notation, assumptions, and units when relevant.
4. **Why it matters:** problem solved and when it should be used.
5. **Worked examples:** easy to hard, with steps and explanations for each step.
6. **Visual model:** diagram, table, or plot when it genuinely helps.
7. **Implementation:** matching code folder, setup/run instructions, expected output, edge cases, tests.
8. **Application:** realistic inputs, trade-offs, failure modes, implications.
9. **Practice:** exercises, answers or hints, misconceptions, revision prompts.
10. **References:** authoritative links, publication date when relevant, access date for changing information.

Short revision cards need not contain every section; substantial lessons should include precision, useful worked examples, and sources when needed.

## Research and accuracy
- Never invent papers, authors, URLs, dataset availability, case studies, numbers, or results.
- Prefer original papers, publisher pages, official documentation, standards bodies, and original dataset pages.
- Verify changing topics when written and record the access date.
- Label fact, assumption, interpretation, hypothesis, and limitation when the distinction matters.
- For paper reviews, capture question, method, data, evaluation protocol, baseline, metrics, results, limitations, reproducibility, and valid conclusions.
- Summarize in original wording, quote sparingly, and link to originals. Do not add pirated papers or restricted data.
- Never commit credentials, API keys, private data, or secrets.

## Code quality
- Keep examples small and runnable; state runtime and dependencies when version-sensitive.
- Include commands, expected output, and tests for nontrivial logic and edge cases.
- Explain time/space complexity for algorithms and numerical issues for scientific code.
- Use small redistributable datasets; link to large or restricted data.
- Use deterministic random seeds where useful, while explaining environment-dependent limits.
- Distinguish educational examples from production-ready solutions.

## Style
Use clear English and define technical vocabulary. Hinglish intuition is welcome where useful, but retain standard terminology. Keep notation consistent. Explain wrong approaches and why they fail. Avoid filler and unsupported “best” claims.

## Git
Use focused commits where possible:
- docs(probability): add conditional probability examples
- feat(code): add tested Bayes theorem demo
- docs(research): summarize image segmentation paper

Review equations, links, spelling, tests, and output before committing.
