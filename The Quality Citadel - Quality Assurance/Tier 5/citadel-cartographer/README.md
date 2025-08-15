# Project: Citadel Cartographer

> A Tier 5 project in "The Quality Citadel" series. This project involves building a web-based "test coverage visualizer" using Python, Flask, and pandas to display the results of an automated test run.

## Project Overview

This project demonstrates the ability to analyze and present test execution data in a meaningful way. It parses a Robot Framework `output.xml` report, extracts key information for each test case (name, status, tags), and displays it in a clean, sorted, and user-friendly web dashboard.

This tool is a practical example of how to build internal QA tooling to improve the visibility of test results and communicate test coverage to a wider team.

## Features
- **XML Parsing:** Reads and parses a standard Robot Framework `output.xml` file.
- **Data Aggregation:** Uses the pandas library to structure the extracted test data.
- **Web Dashboard:** A simple, clean web interface built with Flask to display the test results in a sorted table.
- **Status Highlighting:** The dashboard uses CSS to color-code the "PASS" and "FAIL" statuses for easy readability.

## Technologies & Tools Used
- **Web Framework:** Flask
- **Data Processing:** pandas
- **Language:** Python

## Setup and Installation
This project is part of a larger monorepo. Please refer to the main repository's `README.md` for instructions on cloning individual projects.

1. **Navigate to the project directory:**
   ```bash
   cd "The Quality Citadel - Quality Assurance/Tier 5/citadel-cartographer"
   ```
2. **Create and activate a virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Add Data:** Place a Robot Framework `output.xml` file into the `data/` directory.

## Usage
To run the web application, execute the following command from the root of the project directory:
```bash
python main.py
```
Then, open your web browser and navigate to `http://127.0.0.1:5000` to view the dashboard.