# Project: Citadel Forgemaster

> A Tier 6 project in "The Quality Citadel" series. This project involves building a minimalist, functional test automation framework from scratch using only standard Python libraries.

## Project Overview

This project serves as a deep dive into the fundamental principles of test automation. Instead of using an existing framework like `pytest` or `Robot Framework`, this project builds a custom test runner from the ground up. This demonstrates a core understanding of how testing frameworks operate.

The framework is capable of discovering tests, executing them, catching failures, and generating a clean, custom HTML report to display the results.

## Framework Features
- **Test Discovery:** Automatically discovers test files (`test_*.py`) and test functions (`test_*`) within a specified directory.
- **Test Execution:** Runs all discovered tests, capturing their pass/fail status and any assertion errors.
- **Custom HTML Reporting:** Generates a simple, clean, and shareable `report.html` file that includes a summary of the test run and a detailed breakdown of any failures.

## Technologies & Tools Used
- **Language:** Python (standard libraries only, including `os`, `importlib`, `inspect`)

## Setup and Installation
This project is part of a larger monorepo. Please refer to the main repository's `README.md` for instructions on cloning individual projects.

1. **Navigate to the project directory:**
   ```bash
   cd "The Quality Citadel - Quality Assurance/Tier 6/citadel-forgemaster"
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   *(Note: No external dependencies are required for the core framework.)*

## Usage
To run the framework and generate a new test report, execute the following command from the root of the project directory:
```bash
python run_tests.py
```
A new `report.html` file will be created in the `reports/` directory.