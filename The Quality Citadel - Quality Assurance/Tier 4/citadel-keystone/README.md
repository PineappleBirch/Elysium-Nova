# Project: Citadel Keystone

> A Tier 4 project in "The Quality Citadel" series. This project involves building a professional, hybrid test automation framework from scratch using Python and pytest.

## Project Overview

This project serves as a capstone for the QA discipline, demonstrating the ability to design and build a scalable and maintainable test automation framework. The framework is "hybrid," meaning it is designed to handle different types of testing, in this case, both UI and API tests.

The architecture separates concerns into distinct layers: core framework logic, page objects for UI interaction, configuration, and the tests themselves. This professional structure ensures that the test suite is easy to read, maintain, and expand.

## Framework Features
- **Core Logic:** A WebDriver factory to manage browser instances and a centralized configuration for settings like URLs.
- **UI Testing:** Implements the Page Object Model (POM) to create a clean and robust abstraction layer for UI elements. Includes comprehensive browser options to ensure a stable and pop-up-free testing environment.
- **API Testing:** Includes a suite of API tests using the `requests` library to directly verify backend functionality.
- **Unified Test Runner:** Uses `pytest`'s automatic discovery to find and run all tests (both UI and API) with a single command.

## Technologies & Tools Used
- **Testing Framework:** pytest
- **Browser Automation:** Selenium
- **API Testing:** requests
- **Language:** Python

## Setup and Installation
This project is part of a larger monorepo. Please refer to the main repository's `README.md` for instructions on cloning individual projects.

1. **Navigate to the project directory:**
   ```bash
   cd "The Quality Citadel - Quality Assurance/Tier 4/citadel-keystone"
   ```
2. **Create and activate a virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
To run the full test suite (both UI and API tests), execute the following command from the root of the project directory:
```bash
pytest
```