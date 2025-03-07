# Test Automation framework using Behavex and Selenium
## Pre-Condition
- Install chromedriver
- Python 3.12

## Requirements
Before running the tests, make sure you have the necessary dependencies installed. You can do this by running:
```bash
pip3 install -r requirements.txt
```
This will install all the required packages specified in the requirements.txt.

## Running the Tests
To run all test scenarios:
```bash
behavex
```

To run only specific tests scenarios based on tag:
```bash
behavex -t <tag_name>
```

To run parallel scenarios:
```bash
behavex --parallel-processes <number_of_threads>
```

## HTML report from behavex
- To access HTML report, open [report.html](output/report.html) in a browser

## Disclaimer
The `output` folder has been pushed to this repository for the convenience of users who wish to quickly view the HTML report. However, in a real-time project, this folder should be excluded from version control. 

To do so, ensure that it is added to the  [.gitignore](.gitignore) to prevent the report from being tracked and committed to the repository. Or just un-comment the last line

## Description on test structure
There are 4 important files
- [search.feature](features/twitch/search.feature) - This is the place where we write our test scenarios in BDD format. Because it's easy for both technical and non-technical people to understand
- [twitch_steps.py](steps/twitch/twitch_steps.py) - This is the steps file where the entire logic for scenario is written. For example: assertions
- [twitch_page.py](pages/twitch/twitch_page.py) - This is the page file - a typical POM model, where we add selectors of the elements.
- [environment.py](features/environment.py) - This is a hooks file. You can add logic on what the framework has to do before/after scenario (Example: for setup and teardown), before/after tag (Example: for creating/deleting dummy data), before/after step (Example: for taking screenshot)