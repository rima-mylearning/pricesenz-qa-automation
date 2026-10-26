# PriceSenz QA Automation Project

## 1. Project Overview

This project contains manual and automated testing for the PriceSenz QA application.

The main objective is to verify the functionality of the Login Page and Product Catalogue Page. The project uses Python, Playwright, and Pytest to automate functional test scenarios.

The project follows the Page Object Model (POM) approach to keep page locators, page actions, test data, and test cases organised.

### Application Under Test

- **Application:** PriceSenz QA
- **Base URL:** https://pzqa.vercel.app
- **Login Page:** https://pzqa.vercel.app/login
- **Product Catalogue Page:** https://pzqa.vercel.app/dashboard

## 2. Technologies and Tools

The following technologies and tools are used in this project:

- **Programming Language:** Python 3.11.5
- **Automation Tool:** Playwright for Python
- **Test Framework:** Pytest
- **Browser:** Chromium
- **Development Environment:** PyCharm
- **Version Control:** Git and GitHub
- **Test Case Documentation:** Excel
- **Test Type:** Functional Testing

## 3. Project Structure

The project is organised as follows:


```text
pricesenz-qa-automation/
│
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
│
├── config/
│   └── configuration.py
│
├── pages/
│   ├── login_page.py
│   └── product_catalog_page.py
│
├── test_data/
│   └── login_data.py
│
├── tests/
│   ├── test_login.py
│   └── test_product_catalog.py
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 4. Folder and File Description

| Folder/File | Description |
|---|---|
| `config/configuration.py` | Stores the base URL and application page URLs. |
| `pages/login_page.py` | Contains login page locators and reusable login actions. |
| `pages/product_catalog_page.py` | Contains product catalogue locators and reusable page actions. |
| `test_data/login_data.py` | Stores valid and invalid login test data. |
| `tests/test_login.py` | Contains automated login test cases. |
| `tests/test_product_catalog.py` | Contains automated product catalogue test cases. |
| `conftest.py` | Configures shared Pytest fixtures, including browser and page setup. |
| `requirements.txt` | Lists the Python packages required to run the project. |
| `reports/` | Intended for storing test reports and related output. |
| `README.md` | Provides project documentation and execution instructions. |

## 5. Prerequisites

Before running the automation tests, make sure the following are installed:

1. Python 3.11 or a compatible Python version.
2. PyCharm or another Python IDE.
3. Git, if you want to manage the project using version control.
4. An internet connection to access the application and install dependencies.

The project was developed and tested using Python 3.11.5 on Windows.

## 6. Installation and Setup

### Step 1: Open the Project

Open the `pricesenz-qa-automation` project folder in PyCharm.

### Step 2: Create a Virtual Environment

If a virtual environment has not already been created, run:

```powershell
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell, run:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should display `(.venv)`.

If PowerShell blocks activation, use the appropriate execution policy permitted on your system, or activate the environment through PyCharm.

### Step 4: Install Dependencies

Run the following command:

```powershell
python -m pip install -r requirements.txt
```

### Step 5: Install the Playwright Chromium Browser

Run:

```powershell
python -m playwright install chromium
```

The project is now ready for test execution.

## 7. Configuration

The application URLs are maintained in:

`config/configuration.py`

The configuration includes:

- Base application URL
- Login page URL
- Product catalogue page URL

Keeping the URLs in one configuration file makes maintenance easier if the application address changes.

## 8. Test Data

Login test data is maintained separately in:

`test_data/login_data.py`

The test data covers the following scenarios:

- Valid email and password
- Valid email with an incorrect password
- Invalid email format
- Empty email and password fields

Keeping test data separate from test logic makes the test cases easier to maintain and extend.

## 9. Test Scenarios Covered

### 9.1 Login Page

The automated login tests cover:

- Login page visibility
- Successful login using valid credentials
- Login attempt using an incorrect password
- Login attempt using an invalid email format
- Login attempt with empty fields
- Password field masking

### 9.2 Product Catalogue Page

The automated product catalogue tests cover:

- Successful access to the product catalogue
- Product catalogue heading visibility
- Product card visibility
- Visibility of the five identified products
- Initial cart count
- Add-to-cart button visibility
- Adding two different products to the cart
- Logout functionality
- Access restriction for unauthenticated users
- Verification of the expected product count

The expected product count scenario is marked as XFAIL in the current test run because the page reports six available products while five product cards were identified.

This result requires confirmation against the live application before it is reported as a confirmed application defect.

## 10. Test Execution

Run the following commands from the project root directory.

### Run All Tests

```powershell
python -m pytest tests -v
```

### Run Login Tests Only

```powershell
python -m pytest tests/test_login.py -v
```

### Run Product Catalogue Tests Only

```powershell
python -m pytest tests/test_product_catalog.py -v
```

### Run Tests in Headed Browser Mode

The browser configuration is managed through the shared fixtures in `conftest.py`. If headed mode is configured, the Chromium browser will open during test execution.

## 11. Latest Test Execution Results

The latest recorded test execution produced the following results:

| Result | Count |
|---|---:|
| Passed | 23 |
| Expected failures (XFAIL) | 1 |
| Unexpected failures | 0 |
| Total tests | 24 |

**Note:** These results represent the latest recorded run. Test results may change if the application, test code, configuration, or test data changes.

The XFAIL result relates to the product count verification. It is not a confirmed defect until the observed behaviour is reproduced and supported by evidence.

## 12. Page Object Model (POM)

The automation framework follows the Page Object Model approach.

Page locators and reusable page actions are maintained in separate page classes.

For example:

- `login_page.py` manages login page interactions.
- `product_catalog_page.py` manages product catalogue interactions.
- Test files contain the test scenarios and assertions.

### Benefits of Using POM

- Improves code readability.
- Reduces duplication of page interaction code.
- Makes maintenance easier when locators change.
- Separates page implementation from test logic.
- Supports future expansion of the automation framework.

## 13. Assumptions

The following assumptions are used in the current implementation:

1. The application is accessible at the configured base URL.
2. The provided login credentials are valid for the test environment.
3. The test environment is available during execution.
4. Product cards and interactive elements can be identified using the locators implemented in the page classes.
5. The product catalogue and cart behaviour should be verified against the application's actual requirements.
6. The expected product count should be confirmed before reporting a defect.

## 14. Limitations

The current automation implementation has the following limitations:

- Automation is limited to the scenarios implemented in the two test files.
- The current implementation primarily covers functional UI testing.
- Cross-browser execution has not been established; the current setup uses Chromium.
- Automated screenshot capture and a formal HTML test report are not confirmed as configured.
- The `reports/` directory is intended for test output, but reporting functionality must be configured separately.
- Additional scenarios, including detailed cart quantity validation, checkout workflows, and broader boundary testing, may require further implementation.
- The product count discrepancy requires manual verification and supporting evidence before it can be classified as a confirmed bug.

## 15. Manual Test Cases and Bug Reports

Manual test cases should be documented separately from the automation code.

The manual test case document should include:

- Test Case ID
- Module
- Scenario Type
- Test Scenario
- Test Steps
- Expected Result
- Execution Status
- Actual Result / Notes
- Bug ID

Any defects identified during testing should be recorded separately with:

- Bug ID
- Bug Title
- Description
- Preconditions
- Steps to Reproduce
- Expected Result
- Actual Result
- Severity and Priority
- Screenshot or other supporting evidence
- Status

Only reproducible observations should be reported as confirmed defects.

Potential enhancements should be documented separately from defects.

## 16. Future Improvements

The following improvements can be considered for future versions:

- Add more positive, negative, and boundary test scenarios.
- Expand cart functionality testing.
- Add data-driven tests using Pytest parameterisation.
- Configure automated screenshot capture on failure.
- Generate HTML test reports.
- Add cross-browser testing for Firefox and WebKit.
- Automated test execution is integrated with GitHub Actions and runs on pushes and pull requests targeting the main branch.
- Expand API testing coverage where suitable endpoints are available.

## 17. Conclusion

This project demonstrates the use of Python, Playwright, Pytest, and the Page Object Model to automate functional testing of the PriceSenz Login Page and Product Catalogue Page.

The project separates configuration, page objects, test data, and test cases to support maintainability and future expansion.

The automated tests provide an initial level of functional validation, while manual testing and supporting evidence can be used to investigate and document additional defects and enhancements.
