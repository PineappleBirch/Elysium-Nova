# Project: Citadel Alchemist

> A Tier 5 project in "The Quality Citadel" series. This project involves building a "test data factory" using Python and the Faker library to generate large amounts of realistic, structured fake data for testing purposes.

## Project Overview

This project demonstrates the ability to programmatically generate realistic test data, a critical skill for setting up complex and robust test scenarios. The data factory is designed to be extensible, with clear data models and generic functions for generating and saving data in different formats.

This tool can be used to seed databases, populate UIs with varied user data, or create payloads for API testing, ensuring that tests are not reliant on static, hardcoded data.

## Features
- **User Data Generation:** Creates realistic user profiles with fields like name, email, address, and join date.
- **Product Data Generation:** Creates realistic product data with fields like product name, price, and description.
- **Multiple Output Formats:** The factory can save the generated data as both `.csv` and `.json` files.

## Technologies & Tools Used
- **Data Generation:** Faker
- **Language:** Python

## Setup and Installation
This project is part of a larger monorepo. Please refer to the main repository's `README.md` for instructions on cloning individual projects.

1. **Navigate to the project directory:**
   ```bash
   cd "The Quality Citadel - Quality Assurance/Tier 5/citadel-alchemist"
   ```
2. **Create and activate a virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
To run the script and generate new data files, execute the following command from the root of the project directory:
```bash
python main.py
```
New `users.csv` and `products.json` files will be created in the `output/` directory.