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

1. **Clone the repository:**
   ```bash
   git clone <this-repo-url>
   cd project-citadel-guard
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate 
   # On Windows use `.\venv\Scripts\activate`
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the full test suite, execute the following command from the root of the project directory:
```bash
robot saucedemo_suite.robot
```

## Viewing the Report
After the test run is complete, the detailed results can be found in the `output` folder. Open the **`report.html`** file in a web browser to view a summary of the test results.