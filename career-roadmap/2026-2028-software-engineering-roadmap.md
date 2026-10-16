# Software Engineering Career Roadmap (2026–2028)

> **Primary direction:** Full-Stack / Backend Software Engineer, then grow into an AI-enabled Software Engineer.
>
> **Purpose:** Build employable engineering skills while completing M.Tech Software Engineering. This roadmap is designed for someone with existing React/MERN project experience, some professional experience, beginner-level DSA, and approximately 3–4 hours per day for focused preparation.
>
> **Important:** This is a learning and job-search plan, not a guarantee of a job, salary, or future market demand. Reprioritize using actual interview feedback and current job descriptions.

## Target roles

### Primary roles — apply now when requirements fit
- Software Engineer I / Associate Software Engineer
- Full-Stack Developer / Full-Stack Software Engineer (React, Node.js, TypeScript)
- Backend Engineer (Node.js / TypeScript)
- Product Engineer

### Secondary roles — pursue after building relevant evidence
- AI Application Engineer / Generative AI Software Engineer
- Python Backend Engineer (FastAPI)
- Geospatial Software Engineer, especially where web mapping and research data are relevant

Do not target senior/staff roles requiring several years of experience merely because they mention AI. Read the actual responsibilities, experience requirements, degree eligibility, and location before applying.

## Language strategy

| Language | Use | Priority |
|---|---|---|
| JavaScript | DSA for the first 90 days and existing application development | Start now |
| TypeScript | Main professional language for React/Next.js and Node.js backend engineering | High |
| Python | AI integration, data processing, FastAPI, ML experiments and research | After the initial DSA foundation; learn incrementally |
| Java | Learn if target roles specifically require Java/Spring Boot or a chosen recruitment path justifies it | Optional |

Avoid switching languages repeatedly during DSA preparation. The goal is to learn problem-solving patterns, not to collect languages.

## 12-month roadmap

### Phase 1 — DSA foundation and job readiness (Weeks 1–12)
- Study time complexity, arrays, strings, hash maps/sets, sorting and binary search.
- Continue with two pointers, sliding window, linked lists, stacks, queues, recursion, trees and basic backtracking.
- Cover heaps, graphs and introductory dynamic programming as time allows.
- Target roughly 100–140 carefully selected problems with revision and independent re-solving; quality matters more than a raw problem count.
- Revise JavaScript, React, REST APIs, authentication, SQL and existing projects.
- Audit the résumé, GitHub repositories and deployed projects.
- Start applying in the first month; do not wait for the 90-day plan to finish.

**Exit evidence:** Explain solutions and complexity, solve common easy problems independently, discuss one deployed project clearly, and have active applications.

### Phase 2 — Backend and production engineering (Months 4–6)
- TypeScript fundamentals, types, generics, async behavior and error handling.
- Node.js; Express or NestJS; modular architecture and API contracts.
- PostgreSQL: schema design, joins, indexes, constraints, transactions and migrations.
- Authentication and authorization, input validation, secure secrets and rate limiting.
- Automated unit and API integration tests.
- Git workflows, Docker, CI/CD, deployment, logging and debugging.
- Core CS interview revision: OOP, DBMS, operating systems and computer networks.
- LLD: SOLID, separation of concerns, design patterns and testable code.
- HLD foundations: HTTP, DNS, caching, queues, load balancing, availability and scalability trade-offs.

**Exit evidence:** Build and explain a secure, tested, deployed application with a documented database schema and API contract.

### Phase 3 — Practical AI application engineering (Months 7–9)
- Python fundamentals, virtual environments, package management and pytest.
- FastAPI, Pydantic, async APIs and service boundaries.
- LLM API integration, structured outputs, tool calling, streaming and failure handling.
- Retrieval-augmented generation (RAG): document ingestion, chunking, embeddings, retrieval and source citations.
- Evaluation: representative test sets, retrieval quality, answer correctness, latency and cost.
- AI security: prompt injection, authorization boundaries, privacy and secret management.
- Use one framework only when useful; understand the underlying concepts rather than learning every agent framework.

**Exit evidence:** A working AI-enabled feature with automated tests, documented limitations, evaluation cases and cost/failure handling.

### Phase 4 — Interview conversion and specialization (Months 10–12)
- Use interview feedback to address the biggest gap: DSA, project discussion, backend depth or communication.
- Practice system-design prompts appropriate to early-career roles.
- Strengthen deployment, observability, performance and security.
- Apply to full-stack/backend roles and selected AI application roles whose requirements match demonstrated skills.
- If a suitable job is secured earlier, prioritize work performance and continue learning around the job.
- Review technical government recruitment only if there is a specific role/exam with a credible eligibility and preparation plan; do not split effort across multiple unrelated exams by default.

## Daily study template (3–4 hours)

| Activity | Initial daily allocation |
|---|---:|
| DSA and reviewing previous problems | 75 minutes |
| Full-stack/backend implementation | 75 minutes |
| Core CS or system design | 30 minutes |
| Applications, referrals, mock interview or review | 30 minutes |
| **Total** | **3 hours 30 minutes** |

Adapt around M.Tech deadlines and exams. Protect sleep. On a busy academic day, reduce the session rather than abandoning the routine.

After the first 90 days, gradually reduce daily DSA time if fundamentals are improving and shift more time to backend depth, system design, AI skills and interviews.

## System design roadmap

### Level 1 — LLD and practical design (start immediately)
- OOP, SOLID, interfaces, modularity and common design patterns.
- API contracts, validation, error handling and data modelling.
- Testability, dependency boundaries and maintainability.
- Practice explaining design decisions and trade-offs.

### Level 2 — HLD fundamentals (Months 2–6)
- Client/server, HTTP, REST, DNS and load balancing.
- Relational database design, indexing, transactions and query performance.
- Caching, Redis, queues, background jobs and idempotency.
- Authentication, authorization, rate limits and secure data access.
- Availability, observability, logging, failure handling and basic capacity estimates.

### Level 3 — Advanced topics (only when useful)
- Replication, partitioning, consistency, distributed transactions and event-driven systems.
- Study advanced distributed systems in response to job requirements or practical project needs; do not let it delay applications.

Practice designing a URL shortener, notification service, rate limiter, file-upload workflow and a small multi-tenant SaaS backend. Explain why each component exists rather than adding infrastructure without a requirement.

## Portfolio: two flagship projects

### Project A — AI-enabled business SaaS
Build a focused customer-support, lead-management or workflow application.

- Frontend: Next.js/React + TypeScript.
- Backend: Node.js + TypeScript; PostgreSQL and an ORM with migrations.
- Essentials: authentication, role-based access, validation, pagination, audit-relevant events, tests and clear error handling.
- AI feature: structured output, summarization or knowledge retrieval, with source citations where appropriate.
- Reliability: timeouts, retries where safe, provider failure handling, usage/cost tracking and evaluation tests.
- Delivery: Docker/local setup, CI, deployment instructions, architecture diagram and short demo.

### Project B — AquaPredict / groundwater analytics platform
Extend the groundwater research into a reproducible application instead of starting an unrelated project.

- Map and time-series views with clear units, data provenance and limitations.
- Documented ingestion and cleaning pipeline; explicit missing-data handling.
- Baseline ML models and honest evaluation; avoid claiming causal drivers from predictive correlations alone.
- API, database schema, tests and reproducible environment.
- Use verified open datasets and respect their licenses/terms.
- Connect the implementation to M.Tech research and document the methodology.

Prefer these two polished projects over many incomplete tutorial clones. Do not claim production scale or accuracy without evidence. Free tiers and model APIs have limits; verify costs before deployment and use mocks or locally runnable models when needed.

## Job search and employer strategy

Search by role and requirements, not only company brand. Monitor official career pages and reputable job boards for:
- Software Engineer I / Associate Software Engineer
- Full-Stack Engineer — React/Node/TypeScript
- Backend Engineer — Node.js/TypeScript
- Product Engineer
- Associate Software Engineer — GenAI / AI Application Engineer
- Python Backend Engineer — FastAPI, where skills match

Example employer groups to monitor (not claims of current vacancies): product/SaaS and fintech firms, developer-tool companies, GCCs, IT services companies, and smaller software/AI startups. Always verify current postings, eligibility, location, required experience and legitimacy of the application route.

### Weekly starting targets
- 8–12 relevant applications, adjusted for actual opening quality.
- 3–5 personalized messages to alumni, former colleagues, recruiters or engineers.
- 2 mock interviews or timed assessments.
- One concrete résumé/project improvement based on feedback.
- Track company, role, required skills, location, date, referral/contact, status and next action.

If relevant applications receive no responses, review targeting, résumé and referrals. If interviews fail at coding, focus on DSA. If coding is fine but technical rounds fail, strengthen project explanation, backend fundamentals, system design and communication.

Never pay a recruiter for a job; verify the employer and posting.

## Compensation planning

Use compensation targets as planning hypotheses, not promises. Offers vary with location, employer, role level, experience, interview performance and the fixed/variable composition of CTC. Compare fixed pay, take-home, benefits, learning, working hours, stability and commute—not CTC alone. Do not invent or inflate prior compensation.

## Monthly progress review

Record:
1. DSA problems solved independently and later re-solved.
2. Mock interviews and coding assessments completed.
3. Applications, recruiter responses and interview conversion.
4. Features shipped and tests written.
5. Skills gaps identified from real feedback.
6. M.Tech milestones and workload.
7. One adjustment for the next month.

A roadmap is not proof of completion. Mark a topic complete only when you can explain it, implement or solve a representative task independently, and identify its limitations.

## Free learning references

- [System Design Primer](https://github.com/donnemartin/system-design-primer) — system design concepts and interview practice.
- [roadmap.sh System Design](https://roadmap.sh/system-design) — topic map.
- [Refactoring.Guru](https://refactoring.guru/design-patterns) — design patterns.
- [LeetCode Study Plans](https://leetcode.com/studyplan/) — structured DSA practice.
- [MDN Web Docs](https://developer.mozilla.org/) — JavaScript and web platform.
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) — TypeScript.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — Python basics.
- [FastAPI Documentation](https://fastapi.tiangolo.com/) — Python APIs.
- [PostgreSQL Documentation](https://www.postgresql.org/docs/) — SQL and database fundamentals.
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — common web application security risks.

## Decision rule

Primary path: **Full-Stack / Backend Software Engineer**.
Specialization: **AI application engineering** after core software skills are demonstrable.
Language sequence: **JavaScript for initial DSA → TypeScript for professional development → Python for AI**.
Keep job applications running while learning. Review the plan every month using evidence, not anxiety about trends.
