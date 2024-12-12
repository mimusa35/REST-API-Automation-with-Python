# API Automation Testing with Playwright

## **Overview**
This project demonstrates automated API testing for the JSONPlaceholder (`https://jsonplaceholder.typicode.com`) public mock API using Playwright. The tests cover CRUD operations (Create, Read, Update, Delete) for the `/todos` endpoint and validate response status codes, body content, response structure, and performance metrics (response time).

## **Environment Setup**

To set up the environment for running the tests, follow these steps:

1. **Install Python**:
   Ensure Python 3.12 or later is installed. Version 3.12.6 is used in this project. You can download it from [python.org](https://www.python.org/downloads/). To check the Python version, use the following command:
     ```bash
     python --version
     ```

2. **Install Dependencies**:
   - Clone this repository to your local machine.
   ```bash
     git clone <repository_url>
     cd <repository_directory>
     ```
   - Create a virtual environment on the project root directory using the following command:
        ```bash
     python -m venv venv
     ```
   - Activate the virtual environment using the following command:
   ```bash
     venv\Scripts\activate
     ```
   
   - Once the virtual environment is activated, you can install the required dependencies using the following command:
     ```bash
     pip install -r requirements.txt
     ```

## **Running Tests**

1. **Run a single test**:
   - To run a single test file, use the following command:
     ```bash
     python -m pytest path_to_test_file.py
     
     #detailed information about the test results
     pytest -v -s path_to_test_file.py
     ```
     Example:
    ```bash
     pytest -v -s tests/test_get_todos.py
     ```

2. **Run all tests**:
   - To run all tests in the project, navigate to the test folder and run:
     ```bash
     python -m pytest
     ```
     
## **Test Scenarios Covered**

The following scenarios are covered for the **/todos** endpoint:

**GET Requests**
1. GET /todos:
   - Validate that the API returns a list of todos.
   - Verify the response structure includes **userId**, **id**, **title**, and **completed** for each todo item.
   - Validate the response time is under 500ms.

2. GET /todos/{id} (Valid):
   - Verify that the API returns the correct to-do item by ID.
   - Validate the response status is **200 OK**.

3. GET /todos/{id} (Invalid):
   - Verify that a non-existent resource returns a **404 Not Found** status.

**POST Requests**
1. POST /todos (Valid):
   - Validate that a new to-do item is created with the correct data.
   - Verify the response status is **201 Created**.

2. POST /todos (Empty Payload):
   - Test behavior when sending an empty payload.
   - Log any discrepancies due to the mock API.

**PUT Requests**
1. PUT /todos/{id} (Valid):
   - Validate that an existing to-do item is updated with the correct data.
   - Verify the response status is **200 OK**.

2. PUT /todos/{id} (Invalid):
   - Verify that updating a non-existent resource returns a **404 Not Found** or appropriate error.

**DELETE Requests**
1. DELETE /todos/{id} (Valid):
   - Validate that an existing to-do item is deleted successfully.
   - Verify the response status is **200 OK**.

2. DELETE /todos/{id} (Invalid):
   - Verify that attempting to delete a non-existent resource returns a **404 Not Found**.

## **Assumptions Made**
   - The JSONPlaceholder API mock does not enforce strict validation, which is why some tests (like the empty payload POST) may behave differently than expected in a real-world API.
   - All the tests assume that the API is reachable and responsive at `https://jsonplaceholder.typicode.com`.
   - A response time threshold of **500ms** is used for validating API performance, assuming network latency.
   - Tests are designed to run in a local development environment. Network issues may impact performance metrics.

