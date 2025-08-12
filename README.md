# Elysium Nova - A Portfolio

Welcome to my portfolio of end-to-end projects. 

Since I can't showcase proprietary code and workflow from my professional career (NDA), I have decided to make this project. 

It's purpose is mostly to give a glimpse of my experience to anyone whom it may concern as well as for me to have fun!

This repository showcases my skills across multiple disciplines, including:
- Machine Learning Engineering
- Data Processing and Data Engineering
- Manual and Automated Testing (QA)
- Data Analysis and Data Science
- Image Processing and Computer Vision

Each project is self-contained and demonstrates a specific set of technical skills and a professional workflow.

The projects are categorised based on the Discipline and Tier (T1, T2, T3...)

The Tiers roughly correspond to difficulty (subjective) and I plan to add more more projects (and possibly more Tiers) periodically.

For a detailed overview of all planned projects, please see the [**Full Project Roadmap**](./PROJECT_ROADMAP.md).

---

## Completed Projects

### The MLOps Forge (Machine Learning Engineering)

| Project Name | Tier | Description |
| :--- | :--- | :--- |
| **[Project: Iris Core](./The%20MLOps%20Forge%20-%20Machine%20Learning/Tier%201/iris-core/)** | T1 | A simple but robust API built with FastAPI to serve a Scikit-learn classification model. |

### The Quality Citadel (Manual & Automated Testing - QA)

| Project Name | Tier | Description |
| --- | --- | --- |
| **[Project: Citadel Blueprint](./The%20Quality%20Citadel%20-%20Quality%20Assurance/Tier%201/citadel-blueprint/)** | T1 | A comprehensive manual test suite designed for a public e-commerce website. |
| **[Project: Citadel Guard](./The%20Quality%20Citadel%20-%20Quality%20Assurance/Tier%201/citadel-guard/)** | T1 | An initial automated UI test suite for a web application's login functionality, built with Robot Framework. |
| **[Project: Citadel Architect](./The%20Quality%20Citadel%20-%20Quality%20Assurance/Tier%202/citadel-architect/)** | T2 | A refactored UI test suite implementing the professional Page Object Model (POM) for enhanced maintainability. |
| **[Project: Citadel Dispatch](./The%20Quality%20Citadel%20-%20Quality%20Assurance/Tier%202/citadel-dispatch/)** | T2 | An automated API test suite using Python and pytest to verify the functionality of a public REST API. |
| **[Project: Citadel Corridor](./The%20Quality%20Citadel%20-%20Quality%20Assurance/Tier%203/citadel-corridor/)** | T3 | A CI/CD pipeline using GitHub Actions to automatically run the 'Citadel Architect' test suite. |
| **[Project: Citadel Siege](./The%20Quality%20Citadel%20-%20Quality%20Assurance/Tier%203/citadel-siege/)** | T3 | A performance test suite using Locust to simulate user load on a public API. |
| **[Project: Citadel Keystone](./The%20Quality%20Citadel%20-%20Quality%20Assurance/Tier%204/citadel-keystone/)** | T4 | A professional, hybrid test automation framework built from scratch using Python and pytest. |

## Setup and Installation

This repository is a "monorepo," meaning it contains multiple, independent projects. You can either clone the entire repository or use Git's Sparse Checkout feature to download only a specific project or tier.

### 1. Cloning the Entire Portfolio

This is the simplest method and is recommended if you want to explore all the projects.

```bash
git clone https://github.com/PineappleBirch/Elysium-Nova.git
cd Elysium-Nova
```
Each project is self-contained in its respective sub-folder and includes its own `README.md` with instructions for setting up its environment and running it.

### 2. Cloning a Single Project

If you only want to download a specific project (e.g., `iris-core`), you can use Git's Sparse Checkout feature.

```bash
# Create a folder for the project and navigate into it
mkdir iris-core-project
cd iris-core-project

# Initialize Git and connect to the remote repository
git init
git remote add origin https://github.com/PineappleBirch/Elysium-Nova.git

# Enable Sparse Checkout and specify the project path
git config core.sparseCheckout true
echo "The MLOps Forge - Machine Learning/Tier 1/iris-core/" >> .git/info/sparse-checkout

# Pull the specified project files
git pull origin main
```
This will create a folder containing only the `iris-core` project and its files.

### 3. Cloning an Entire Tier

You can also use Sparse Checkout to download all projects within a specific tier (e.g., all Tier 1 projects in "The Quality Citadel").

```bash
# Create a folder for the projects and navigate into it
mkdir qa-tier-1-projects
cd qa-tier-1-projects

# Initialize Git and connect to the remote repository
git init
git remote add origin https://github.com/PineappleBirch/Elysium-Nova.git
# Enable Sparse Checkout and specify the tier path
git config core.sparseCheckout true
echo "The Quality Citadel - Quality Assurance/Tier 1/" >> .git/info/sparse-checkout

# Pull all project files from that tier
git pull origin main
```

### 4. Cloning an Entire Discipline

You can also use Sparse Checkout to download all projects within a specific discipline category (e.g., the whole "The Quality Citadel" group).

```bash
# Create a folder for the projects and navigate into it
mkdir qa-projects
cd qa-projects

# Initialize Git and connect to the remote repository
git init
git remote add origin https://github.com/PineappleBirch/Elysium-Nova.git

# Enable Sparse Checkout and specify the tier path
git config core.sparseCheckout true
echo "The Quality Citadel - Quality Assurance/" >> .git/info/sparse-checkout

# Pull all project files from that tier
git pull origin main
```