# Test Automation Framework

## Overview

Welcome to the PyTest Automation Framework repository! This project leverages Python, Selenium, pytest, pytest-bdd, pytest-html, and pytest-xdist to automate the testing of web applications. The framework is integrated with GitHub Actions for Continuous Integration (CI), ensuring that tests are executed automatically on every push and pull request.

## Folder Structure

Here's an overview of the project's folder structure:

- **`Testcases/`**: Contains all the test case scripts.
- **`Data/`**: Holds test data files used by the test cases.
- **`Resources/`**: Includes utility files, such as page objects and custom functions.
- **`features/`**: Contains BDD feature files written in Gherkin syntax.
- **`Report/`**: Directory where test reports (HTML and other formats) are generated.
- **`.github/workflows/Manifest.yml`**: GitHub Actions workflow files for CI/CD.

## Requirements

- **Selenium**
  - [Selenium](https://pypi.org/project/selenium/) is used for browser automation.
  - Install it using pip:
    ```bash
    pip install selenium
    ```

- **pytest**
  - [pytest](https://pypi.org/project/pytest/) is a framework for writing and running tests.
  - Install it using pip:
    ```bash
    pip install pytest
    ```

- **pytest-bdd**
  - [pytest-bdd](https://pypi.org/project/pytest-bdd/) adds behavior-driven development (BDD) capabilities to pytest.
  - Install it using pip:
    ```bash
    pip install pytest-bdd
    ```

- **pytest-html**
  - [pytest-html](https://pypi.org/project/pytest-html/) generates HTML reports from your test results.
  - Install it using pip:
    ```bash
    pip install pytest-html
    ```

- **pytest-xdist**
  - [pytest-xdist](https://pypi.org/project/pytest-xdist/) allows for parallel test execution and other advanced features.
  - Install it using pip:
    ```bash
    pip install pytest-xdist

## Installation

To set up the test automation framework, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone repositaryname
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd your-repo
    ```

3. **Create a Virtual Environment (optional but recommended):**
    ```bash
    python -m venv ENV_Name
    source ENV_Name/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```



## Usage

### Running Tests Locally

To run the tests locally, execute the following command:

```bash
pytest
