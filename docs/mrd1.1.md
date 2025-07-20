## Market Requirements Document (MRD)

### Self‑Hosted Website Ingestion & Citation Service – v1.1 (Refined)

**Version 1.1 — 2025‑07‑20**
Author: Warlack
Supersedes v1.0 “Hardened Spec”

---

### 1  Purpose

Build a **sovereign, extensible retrieval‑augmented‑generation (RAG) engine** that crawls private or niche websites, indexes their content and serves answers **with ≥95 % verifiable citations**, all while running entirely on infrastructure the user controls.

---

### 2  Problem / Opportunity

Large‑language‑model (LLM) chat interfaces hallucinate, link‑rot is rampant, and SaaS RAG platforms compromise data sovereignty. *Technical operators want turnkey accuracy without surrendering control.*

---

### 3  Jobs‑to‑Be‑Done (JTBD)

| Rank      | Job Statement                                                                                                                                                                                                     | Type       |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
|  Primary  |  “When I manage a private or niche body of web knowledge, **help me create a trustworthy Q\&A system** so I get accurate answers with precise citations, **without data‑privacy compromises or vendor lock‑in**.” | Functional |
|  2        |  “**Let me feel confident and in control** of my knowledge infrastructure so I trust every answer.”                                                                                                               | Emotional  |
|  3        |  “Enable me to **demonstrate technical competence** to my team/community by deploying a reliable, self‑hosted research tool.”                                                                                     | Social     |

The service must advance these jobs better than open‑source archivers (SOSSE, Linkwarden) and managed RAG SaaS (Algolia, Denser.ai).

---

### 4  Key Differentiators

1. **Sovereign & Extensible RAG Engine** – 100 % self‑hosted under AGPLv3/community or commercial licence.
2. **Verifiable, Low‑Hallucination Q\&A** – ≥95 % citation accuracy target, validated by automated *CiteFix* post‑processing.
3. **Opinionated, Containerised Stack for Technical Users** – secure‑by‑default Docker/Helm packages; power‑user dashboards.
4. **Reduced Detection Footprint** – hybrid crawler respects robots.txt, configurable rate limits & proxies.

---

### 5  Functional Requirements (v1.1 Scope)

|  ID   |  User Story                                                                                                                                   |  Tier     |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
|  F‑1  |  As a researcher, schedule recurring hybrid crawls (Scrapy→Playwright fallback) to keep corpus current.                                       | Community |
|  F‑2  |  As a developer, automatic parse→semantic chunk→index pipeline using Unstructured.io.                                                         | Community |
|  F‑3  |  As a scientist, choose embedding model (OpenAI, BGE, local GGUF).                                                                            | Community |
|  F‑4  |  As an integrator, query via `/query` REST endpoint with hybrid (BM25+vector) retrieval, cross‑encoder re‑rank and Parent‑Document‑Retrieval. | Community |
|  F‑5  |  As an admin, inspect retrieval pipeline and citation validation in the UI.                                                                   | Community |
|  F‑6  |  Manual link‑rot & content‑drift scan via CLI.                                                                                                | Community |
|  F‑7  |  Automated deletion & drift detection scheduler.                                                                                              | **Pro**   |
|  F‑8  |  API‑key access control & Data‑Purge endpoint.                                                                                                | **Pro**   |
|  F‑9  |  Interactive crawler configuration + freshness dashboards.                                                                                    | **Pro**   |

---

### 6  Non‑Functional Requirements

* **Performance**
  *Static* queries ≤ 700 ms P95; *JS‑rendered* ≤ 2 s P95.
* **Citation Accuracy** ≥ 95 % on golden set; CI fails if < 95 %.
* **Security** – non‑root containers; automatic HTTPS (Caddy/Traefik); SBOM published each release.
* **Reliability** – 95 % queries within SLA; < 0.1 % unnoticed crawl failures.
* **Backup/DR** – daily snapshot of vector store + metadata; `make restore` script.

---

### 7  Architecture & Technology Stack

|  Stage           |  v1.0                         |  v1.1 Update                                                |
| ---------------- | ----------------------------- | ----------------------------------------------------------- |
|  Crawler         | Basic + Playwright fallback   | **Hybrid Scrapy/Playwright** with intelligent fallback      |
|  Parser          | HTML→Markdown                 | **Unstructured.io** structure‑aware parsing                 |
|  Chunking        | Recursive splitter 512 tokens | **Semantic chunking + Parent‑Document‑Retrieval**           |
|  Vector Store    | ChromaDB                      | **Qdrant (default for Pro)**, embedded Chroma for Community |
|  Retrieval       | Single‑stage vector           | **Hybrid BM25 + dense search → Cross‑encoder re‑rank**      |
|  Citation Check  |  N/A                          | **CiteFix** post‑generation verification & auto‑correction  |

---

### 8  Success Metrics

* Citation accuracy ≥ 95 %
* Setup time (HTTPS) ≤ 30 min
* Crawl coverage ≥ 99 %
* Mean time to restore < 15 min

---

### 9  Out of Scope (v1.1)

* CAPTCHA/Turnstile bypass
* Mobile UI, OCR, translation
* Enterprise SSO/RBAC (planned v1.5)
* Multimodal ingestion (v2.0)

---

### 10  Pricing & Licensing Strategy

|  Tier        |  Licence   |  Price                          |  Included Sites       |  Support                   |
| ------------ | ---------- | ------------------------------- | --------------------- | -------------------------- |
|  Community   | **AGPLv3** | Free                            | 2 sites / 50 k tokens | Community (GitHub/Discord) |
|  Pro         | Commercial | **US \$49 month** (US \$490 yr) | Unlimited             | Priority email (24 h SLA)  |
|  Enterprise  | Commercial | Contact                         | Unlimited + SSO/RBAC  | Dedicated Slack / SLA      |

---

### 11  Milestones & Roadmap

|  Date        |  Milestone                                                                 |
| ------------ | -------------------------------------------------------------------------- |
|  2025‑10‑30  | **RAG Core Prototype** (end‑to‑end advanced retrieval on single source)    |
|  2026‑02‑28  | **Integrated Beta Stack** (full Docker compose; Pro dashboards)            |
|  2026‑05‑31  | **v1.0 Public Release** (stable, Helm chart, subscription/ licence system) |
|  v1.5        | Enterprise edition (SSO, RBAC, audit logs)                                 |
|  v2.0        | Multimodal ingestion, observability integrations, adaptive RAG             |

---

### 12  Risks & Mitigations

|  Risk                            |  Mitigation                             |
| -------------------------------- | --------------------------------------- |
|  JS‑heavy sites resist scraping  | Hybrid crawler; proxy guidance          |
|  Vector store scalability        | Qdrant default; benchmark quantisation  |
|  Open‑source strip‑mining        | AGPLv3 + dual licensing                 |
|  Self‑hosting burden             | Opinionated Docker/Helm, SBOM, docs     |
|  Maintainer burnout              | Recurring revenue funds ongoing work    |

---

### 13  Change Log

|  Ver.  |  Date        |  Summary                                                                                                                            |
| ------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
|  1.1   |  2025‑07‑20  | Re‑wrote personas → JTBD, replaced stack (Scrapy + Unstructured + Qdrant), added CiteFix, subscription pricing, updated milestones. |
