# Python API Automation Framework

Hybrid Customer API Automation Framework include the proper folder structure
![image](https://github.com/user-attachments/assets/2a9d0817-61af-4321-a981-52050660e982)

### Tech Stack
- Python 3.12
- Requests - HTTP Requests
- PyTest - Testing Framework
- Reporting - Allure Report, PyTest HTML
- Test Data - CSV, Excel, JSON,  Faker
- Advance API Testcase - jsonschema
- Parallel Execution - x distribute (xdist)

### Allure Report
![image](https://github.com/user-attachments/assets/00953970-0ac0-4d73-805e-0706780f241b)


### How to Install Packages

``` pip install requests pytest pytest-html faker allure-pytest jsonschema```

### How to run your Testcase Parallel

```pip install pytest-xdist```

### How to add the .gitignore File?

Copy the content from this to .gitignore file
https://www.toptal.com/developers/gitignore/api/pycharm+all

### How to run the Basic Test with Allure report

``` pytest tests/tests/crud/test_create_booking.py  --alluredir=allure_result -s```
