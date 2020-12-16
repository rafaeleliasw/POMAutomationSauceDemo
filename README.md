**SAUCEDEMO End to End testing**

This is an Automation Framework with Pytest using POM (Page Object Model) design pattern for www.saucedemo.com. 
SauceDemo is a website built by SauceLabs to practice automation testing.

Prerequisites

`pip install selenium`

`pip install pytest`

Update Config/config.py with the correct paths for

`CHROME_EXECUTABLE_PATH`

`FIREFOX_EXECUTABLE_PATH`

Html Report

`pip install pytest-html`

Parallel execution

`pip install pytest-xdist`

Run all test cases in Chrome and Firefox

`pytest -n 4 Tests/ -v --html=./report.html`