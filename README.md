# Python UI Automation Framework

Проект для портфолио Junior QA Automation.  

## Technology stack
- Python
- Selenium 4
- Pytest
- Pytest-HTML

## Structure
Page/ - POM
tests/ - Tests
conftest.py/ - confs and screens
reports/ - HTML report


## Test launch
```bash
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html -v
