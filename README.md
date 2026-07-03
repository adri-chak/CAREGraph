<!-- CAREGraph README -->
<div align="center">

# 🧠 CAREGraph
### Confidence-Aware Adaptive Reasoning Engine for Multi-Agent Clinical Intelligence

[![Status](https://img.shields.io/badge/Status-Research%20Prototype-blue)]()
[![Python](https://img.shields.io/badge/Python-3.11+-green)]()
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20AI-orange)]()
[![SDG](https://img.shields.io/badge/SDG3-Good%20Health-red)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

*A research-oriented multi-agent clinical reasoning system built to address
real gaps in Agentic AI for Healthcare (2022–2026)*

</div>

---

## 📌 Project Status

> 🔬 **Phase 0 — Foundation & Literature Review**
> Active development. Not yet production-ready.
> Built as a research prototype toward potential publication.

---

## 🧭 What is CAREGraph?

CAREGraph is **not** a healthcare chatbot.
CAREGraph is **not** a disease prediction model.

CAREGraph is an **intelligent multi-agent clinical reasoning system** that simulates the collaborative decision-making of a multidisciplinary medical team.

Instead of routing a patient query to a single LLM and returning an answer, CAREGraph deploys **specialized AI agents** that collaborate, debate, verify evidence, resolve disagreements, and produce **confidence-scored, explainable clinical reasoning reports**.

---

## 🔬 The Research Problem

Current healthcare AI systems suffer from one or more of the following limitations (documented across literature, 2020–2024):

| Limitation | Impact |
|---|---|
| Single-agent reasoning | No cross-verification of clinical conclusions |
| Static workflows | Cannot adapt to case complexity |
| Weak explainability | Clinicians cannot audit AI decisions |
| No confidence estimation | System cannot communicate uncertainty |
| Poor conflict resolution | Conflicting agent outputs are not handled |
| Weak human-in-the-loop | Clinician oversight is not built into the flow |
| No evidence grounding | Reasoning not tied to medical literature |

> CAREGraph is designed to address **all of the above** through a novel orchestration strategy built on top of LangGraph.

---

## 💡 Research Contribution

The novelty of CAREGraph lies **not** in using LangGraph — but in what is built **on top of it**:

1. **Adaptive Agent Routing** — the supervisor dynamically selects which agents to invoke based on case complexity and prior agent outputs
2. **Confidence-Aware Decision Fusion** — each agent emits a confidence score; the consensus engine weights outputs accordingly
3. **Disagreement Detection & Resolution** — when agents conflict, a dedicated Critic Agent and Verification Agent are invoked
4. **Evidence-Grounded Reasoning** — all conclusions are traceable to PubMed, WHO guidelines, or clinical literature via RAG
5. **Explainability Graph** — the full reasoning chain is preserved and surfaced in the clinical report

---

## 🏗️ System Architecture

```
Patient Query
      │
      ▼
┌─────────────────────┐
│   Supervisor Agent  │  ← adaptive routing logic
└─────────────────────┘
      │
      ▼
┌─────────────────────────────────────────────────────┐
│                  Specialist Agents                  │
│                                                     │
│  Symptom Analysis    │  Medical History             │
│  Medication Safety   │  Drug Interaction            │
│  Evidence Retrieval  │  Clinical Guideline          │
│  Lifestyle           │  Mental Health               │
│  Risk Assessment     │  Verification                │
│                      │  Critic                      │
└─────────────────────────────────────────────────────┘
      │
      ▼
┌──────────────────────┐
│   Consensus Engine   │  ← confidence-weighted fusion
└──────────────────────┘
      │
      ▼
┌──────────────────────┐
│ Explainability Engine│  ← reasoning chain tracing
└──────────────────────┘
      │
      ▼
┌──────────────────────────┐
│ Clinical Report Generator│
└──────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | LangGraph + custom orchestrator |
| LLM Framework | LangChain |
| Backend API | FastAPI + Pydantic |
| Knowledge Retrieval | RAG (PubMed, WHO, OpenFDA) |
| Vector Store | ChromaDB |
| Frontend | Next.js + TailwindCSS |
| Database | PostgreSQL (planned) |
| Containerization | Docker |

---

## 📚 Knowledge Sources

CAREGraph does **not** train on noisy public datasets.
Instead it reasons over curated, trustworthy evidence:

- [PubMed](https://pubmed.ncbi.nlm.nih.gov/) — peer-reviewed medical literature
- [OpenFDA](https://open.fda.gov/) — drug safety and adverse event data
- [WHO Guidelines](https://www.who.int/publications/guidelines) — global clinical guidelines
- Clinical Practice Guidelines from major medical bodies

---

## 📁 Repository Structure

```
caregraph/
├── backend/          # FastAPI backend, agents, orchestration
├── frontend/         # Next.js UI
├── research/
│   ├── literature_review/   # Annotated paper summaries
│   └── papers/              # Literature comparison matrix
├── docs/             # Architecture decisions, project journal
├── experiments/      # Isolated agent/RAG experiments
├── notebooks/        # Jupyter notebooks for exploration
├── data/             # Sample inputs (no patient data)
├── paper/            # Draft research paper
└── tests/            # Unit and integration tests
```

---

## 🎯 SDG Alignment

This project contributes toward **UN Sustainable Development Goal 3 — Good Health and Well-being** by building AI infrastructure that could support clinical decision-making in resource-constrained settings where specialist access is limited.

---

## 🚧 Roadmap

- [x] Project structure initialized
- [x] Repository foundation (README, .gitignore)
- [ ] Literature review completed
- [ ] Architecture document finalized
- [ ] Supervisor agent implemented
- [ ] RAG pipeline implemented
- [ ] Consensus engine implemented
- [ ] Explainability engine implemented
- [ ] FastAPI backend complete
- [ ] Frontend complete
- [ ] Research paper draft

---

## 👤 Author

**Adrija Chakraborty**
3rd Year B.Tech — Information Technology
*Research Prototype — Built for portfolio, publication, and SDG 3*

---

## ⚠️ Disclaimer

CAREGraph is a **research prototype**.
It is not a medical device. It is not intended for clinical use.
All outputs are for research and educational purposes only.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.