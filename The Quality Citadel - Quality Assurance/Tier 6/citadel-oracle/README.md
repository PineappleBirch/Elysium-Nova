# Project: Citadel Oracle

> A Tier 6 project in "The Quality Citadel" series. This project establishes a continuous, automated production monitoring suite using Python.

## Project Overview

This project demonstrates an advanced QA and SRE (Site Reliability Engineering) skill: creating an automated system to continuously monitor a live application's health. The script is designed to run on a schedule, performing critical "health checks" to ensure the application is available and functioning correctly for users.

This type of proactive monitoring is crucial for maintaining high uptime and quickly detecting production issues before they impact a large number of users.

## Features
- **Configuration Driven:** The target URL to be monitored is read from a simple `config.ini` file, making the script easy to adapt.
- **Scheduled Execution:** Uses the `schedule` library to run health checks automatically at a defined interval (e.g., every minute).
- **Health Checks:** Performs a basic but critical health check by sending an HTTP GET request and verifying that the response status code is `200 OK`.
- **Status Logging:** Prints clear PASS/FAIL status messages to the console with a timestamp for each check.

## Technologies & Tools Used
- **Scheduling:** schedule
- **HTTP Requests:** requests
- **Language:** Python

## Setup and Installation
This project is part of a larger monorepo. Please refer to the main repository's `README.md` for instructions on cloning individual projects.

1. **Navigate to the project directory:**
   ```bash
   cd "The Quality Citadel - Quality Assurance/Tier 6/citadel-oracle"
   ```
2. **Create and activate a virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
To start the continuous monitoring script, execute the following command from the root of the project directory:
```bash
python main.py
```
The script will run an initial check and then continue to run a new check every minute. Press `CTRL+C` to stop the monitor.