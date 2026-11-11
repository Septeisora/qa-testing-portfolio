# Demoblaze E2E Automation (Playwright)

## 1. Overview
This directory contains E2E automated tests for the Demoblaze e-commerce site. The framework is built using **Python**, **Playwright**, and **Pytest**, following the **Page Object Model (POM)** design pattern.

## 2. Architecture
- `pages/`: Contains Page Object classes (locators and interaction methods).
- `tests/`: Contains test scripts performing assertions.
- `conftest.py`: Contains the Pytest fixture for browser setup and teardown.

## 3. Prerequisites
Before running the test suite, the following precondition must be met:
- The test `test_successful_login` requires an existing user account on the Demoblaze website.
- Manually register the following credentials on the site: Username `test_user`, Password `test_pw`.

## 4. Local Execution

Run the following commands to set up the environment and execute the tests locally:

```bash
# Navigate to the framework directory
cd automation

# Set up virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies and Playwright browsers
pip install -r requirements.txt
playwright install chromium

# Run the test suite
pytest tests/ -v
```