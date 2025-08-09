# Project: Citadel Guard

> A Tier 1 project in "The Quality Citadel" series. This project demonstrates automated UI testing using Python's Robot Framework to verify the login and inventory functionalities of the Sauce Demo e-commerce website.

## Project Overview

This project builds upon the manual test cases designed in "Project: Citadel Blueprint" by automating them. It demonstrates the ability to set up a test automation environment, write a readable and maintainable test suite using a keyword-driven and refactored approach, and generate professional test execution reports.

The test suite covers multiple features and user scenarios, showcasing how to structure a scalable test file with suite-level setup and teardown, and reusable keywords.

## Features Automated
- **Login:**
  - Successful login with standard user credentials.
  - Failed login with a locked-out user, incorrect password, invalid username, and empty credentials.
- **Inventory:**
  - Product sorting by name (A-Z and Z-A).
  - "Add to Cart" functionality from the inventory page.

## Technologies & Tools Used
- **Automation Framework:** Robot Framework
- **Browser Automation:** SeleniumLibrary
- **Language:** Python
- **IDE:** PyCharm

## Setup and Installation

This project is part of a larger monorepo. To clone only this specific project, please follow these steps using Git's Sparse Checkout feature.

1. **Create and navigate into a new directory for the project:**
   ```bash
   mkdir citadel-guard
   cd citadel-guard
   ```
2. **Initialize an empty Git repository:**
   ```bash
   git init
   ```
3. **Connect to the remote Elysium-Nova repository:**
   ```bash
   git remote add origin https://github.com/PineappleBirch/Elysium-Nova.git
   ```
4. **Enable Sparse Checkout and define the project path:**
   ```bash
   git config core.sparseCheckout true
   echo "The Quality Citadel - Quality Assurance/Tier 1/citadel-guard/" >> .git/info/sparse-checkout
   ```
5. **Pull the project files:**
   ```bash
   git pull origin main
   ```
6. **Navigate to the final project directory and proceed with setup:**
   ```bash
   cd "The Quality Citadel - Quality Assurance/Tier 1/citadel-guard"
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
To run the full test suite, execute the following command from the root of the project directory:
```bash
robot saucedemo_suite.robot
```

## Viewing the Report
After the test run is complete, the detailed results can be found in the `output` folder. Open the **`report.html`** file in a web browser to view a summary of the test results.