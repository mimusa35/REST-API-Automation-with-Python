# API Automation Testing with Playwright

## Overview
This project demonstrates automated API testing for the JSONPlaceholder (`https://jsonplaceholder.typicode.com`) public mock API using Playwright. The tests cover CRUD operations (Create, Read, Update, Delete) for the `/todos` endpoint and validate response status codes, body content, response structure, 
and performance metrics (response time).
---

## **Environment Setup**

To set up the environment for running the tests, follow these steps:

1. **Install Python**:
   Ensure Python 3.12 or later is installed. Version  3.12.6 is used in this project. You can download it from [python.org](https://www.python.org/downloads/).

   To check the Python version from terminal:
     ```bash
     python --version
     ```

2. **Install Dependencies**:
   - Clone this repository to your local machine.
   - Install the required libraries by running the following command:
     pip install -r requirements.txt
     

3. **Install Playwright Browsers**:
   - Playwright requires browser binaries to run tests. Install them by running:
     ```bash
     python -m playwright install
     ```

## Running Tests

1. **Run a single test**:
   - To run a single test file, use the following command:
     ```bash
     python -m pytest path_to_test_file.py
     ```

2. **Run all tests**:
   - To run all tests in the project, navigate to the test folder and run:
     ```bash
     python -m pytest
     ```

## Test Suite

- **GET /todos**: Validates retrieving a list of to-do items.
- **POST /todos**: Verifies the creation of a new to-do item.
- **PUT /todos/{id}**: Tests updating an existing to-do item.
- **DELETE /todos/{id}**: Verifies deleting an existing to-do item.

## Assumptions Made

- The JSONPlaceholder API mock does not enforce strict validation, which is why some tests (like the empty payload POST) may behave differently than expected in a real-world API.
- All the tests assume that the API is reachable and responsive at `https://jsonplaceholder.typicode.com`.
- **Response time should be under 500ms** for all API requests. This is a performance assumption based on the expected behavior of the API and is validated in the tests. If any API request exceeds this time limit, it will be flagged as a failure.
