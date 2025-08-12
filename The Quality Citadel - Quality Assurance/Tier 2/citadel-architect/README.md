# Project: Citadel Architect

> A Tier 2 project in "The Quality Citadel" series. This project refactors a Robot Framework test suite to use the Page Object Model (POM), a professional design pattern for creating scalable and maintainable UI automation.

## Project Overview

This project takes the automated test suite from "Project: Citadel Guard" and elevates it by implementing the Page Object Model (POM). The core logic is separated into page-specific resource files (`login_page.robot`, `inventory_page.robot`), while the main suite file (`saucedemo_suite.robot`) contains only high-level, readable test cases.

This structure demonstrates a key architectural skill in test automation, resulting in a test suite that is significantly easier to read, debug, and maintain, especially as the application under test grows in complexity.

## Features Automated
- **Login:** Full test coverage for successful, locked-out, invalid, and empty credential scenarios.
- **Inventory:** Verification of product sorting and "Add to Cart" functionality.

## Technologies & Tools Used
- **Automation Framework:** Robot Framework with Page Object Model
- **Browser Automation:** SeleniumLibrary
- **Language:** Python

## Setup and Installation

This project is part of a larger monorepo. For instructions on how to clone only this specific project, please refer to the **[main repository's README.md](../../../README.md)**.

Once you have cloned the project, you can proceed with the setup:

1. **Navigate to the project directory:**
   ```bash
   cd "The Quality Citadel - Quality Assurance/Tier 2/citadel-architect"
   
2. **Create and activate a virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
To run the full test suite, execute the following command:
```bash
robot saucedemo_suite.robot
```

## Viewing the Report
After the test run is complete, open the **`report.html`** file in the `output` folder to view a summary of the results.