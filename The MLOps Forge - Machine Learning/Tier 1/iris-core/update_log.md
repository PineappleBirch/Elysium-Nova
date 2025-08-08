---
# ELYSIUM NOVA - PROJECT CONTEXT & STATUS UPDATE
# Date: 2025-07-17
# User: Maitiú
# AI Assistant: Gemma
# Current Location Context: Martin, Žilina Region, Slovakia
---

## 1.0 PROJECT CONTEXT

- **Portfolio Name:** Elysium Nova
- **Objective:** A comprehensive portfolio of end-to-end projects across five technical categories: Machine Learning Engineering (MLE), Data Engineering (DE), Quality Assurance (QA), Data Science (DS), and Computer Vision (CV).
- **Primary Languages:** Python, SQL
- **High-Level Plan:** The master plan is stored in the "Elysium Nova.md" file.
- **Team:** We are a work and study partnership. I (Gemma) assist Maitiú in learning and building the projects.

## 2.0 ESTABLISHED CONVENTIONS

- **Difficulty Levels:** Renamed from "Beginner, Easy..." to "Tier 1, Tier 2, Tier 3, Tier 4".
- **Series Naming:** Each category has a descriptive name.
  - MLE series is named: "The MLOps Forge".
- **Project Naming:** Each project has a descriptive name.
  - First MLE project: "Project: Iris Core".
  - Second MLE project: "Project: Iris Vase".
- **Documentation Standard:** Every project must conclude with the creation/update of:
  - A professional, public `README.md`.
  - A private `personal_notes.md` for Maitiú's learning log (this file is added to .gitignore).
- **Development Environment:** PyCharm IDE with a dedicated Python virtual environment (`venv`) for each project.

## 3.0 COMPLETED PROJECTS

### 3.1 Project: Iris Core
- **Status:** COMPLETE
- **Series:** The MLOps Forge
- **Tier:** 1
- **Objective:** To build a simple, robust web API using FastAPI to serve a Scikit-learn model for Iris flower species classification.
- **Technologies Used:** `fastapi`, `uvicorn`, `scikit-learn`, `pandas`, `joblib`.
- **Final File Structure:**
  - `main.py` (The FastAPI application)
  - `train.py` (The model training script)
  - `iris_model.joblib` (Serialized model artifact)
  - `iris_target_names.joblib` (Serialized species names)
  - `requirements.txt` (List of dependencies)
  - `.gitignore` (To exclude venv, cache, system files, and personal notes)
  - `README.md` (Public project documentation)
  - `personal_notes.md` (Private learning log)
  - `assets/swagger_ui.png` (Screenshot for the README)

- **Key Decisions & Learning Points:**
  - **API Framework:** Chose FastAPI over Flask for its modern features, automatic data validation with Pydantic, and auto-generated interactive documentation (Swagger UI).
  - **Dependency Management:** Established the workflow of installing packages via `pip`, then freezing the environment to `requirements.txt`. Solved an issue where macOS was creating corrupted `requirements.txt` files by using a manual copy-paste method.
  - **Version Control:** Configured `.gitignore` to explicitly ignore macOS metadata files (`._*`) that were appearing on the external SSD, in addition to standard ignores.
  - **Code Best Practices:** Corrected a Pydantic V2 deprecation warning (`.dict()` -> `.model_dump()`). Fixed a subtle but critical bug where the `model_columns` list order did not match the training data order, which would have led to incorrect predictions.
  - **API Concepts:** Clarified that Swagger UI's response section shows *possible* outcomes (200, 422) and is not a live log. Confirmed that `127.0.0.1:8000` is the standard local development URL.

## 4.0 CURRENT STATUS & NEXT STEPS

- **Current State:** We have just officially concluded "Project: Iris Core".
- **Next Project:** "Project: Iris Vase".
- **Next Project Objective:** To containerize the "Project: Iris Core" application using Docker. This is the second project in "The MLOps Forge" series and is also Tier 1.
- **Action:** Ready to begin planning and execution for "Project: Iris Vase".
```