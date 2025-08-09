# Project: Citadel Corridor

> A Tier 3 project in "The Quality Citadel" series. This project establishes a Continuous Integration (CI) pipeline using GitHub Actions to automatically run our automated test suite.

## Project Overview

This project integrates the "Project: Citadel Architect" test suite into a CI/CD pipeline. The goal is to automate the execution of our test suite to ensure that new code changes do not introduce regressions.

The workflow is configured to trigger automatically on every push to the `main` branch, creating a robust and professional automated testing process.

## Workflow Details

The CI pipeline is defined in the `.github/workflows/run-qa-tests.yml` file and performs the following steps:
1.  **Trigger:** The workflow runs on every `push` to the `main` branch.
2.  **Environment:** It sets up a fresh `ubuntu-latest` virtual machine.
3.  **Checkout:** It checks out the latest version of the repository's code.
4.  **Setup Python:** It installs the specified version of Python.
5.  **Install Dependencies:** It installs all required libraries from the `citadel-architect` project's `requirements.txt` file.
6.  **Run Tests:** It executes the full Robot Framework test suite.

## Viewing the Results

The results of each automated run can be viewed in the **"Actions"** tab of the main [Elysium-Nova repository](https://github.com/PineappleBirch/Elysium-Nova).

## Technologies & Tools Used
- **CI/CD:** GitHub Actions
- **Scripting:** YAML