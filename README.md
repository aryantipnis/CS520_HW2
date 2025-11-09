# Overview

This repository is organized into **3 main parts**:
**Part 1: Baseline Coverage**, **Part 2: Test Generation**,  **Part 3: Fault Detection**

---

## Folder: `Part1-Baseline-Coverage`

This folder has 20 files: 10 files of problem solutions from A1 and 10 files of test cases. 

For this part, we analyze 10 problems and their corresponding solutions from Assignment 1. 
Using the benchmark test suites provided in the datasets, we run automated tests with pytest and measure both line and branch coverage to establish a baseline. 
The results are shown in the report. 

To produce results locally, run this command in the terminal 
```bash
pytest --cov=. --cov-report=term-missing --cov-branch
```

From these results, we choose Problem 3 and 9 to work on for the other 2 parts since they have the largest gap between tests passed and branch coverage, 
indicating room for coverage improvement with LLM-generated tests. 

## Folder: `Part2-Test-Generation`

This folder has 4 files: 2 files of problem 3 and 9 solution from A1 and 2 files of newly generated test cases for each solution.

For this part, we use an LLM to generate or improve tests with the goal of increasing meaningful coverage.

The files `test_problem_3_new.py` and `test_problem_9_new.py` contain 3 iterations of test generated so that we get a more comprehensive and wide range of tests and coverage goes up. 

To produce results locally, run this command in the terminal 
```bash
pytest --cov=. --cov-report=term-missing --cov-branch
```

## Folder: `Part3-Fault-Detection`

This folder has 4 files: 2 files of bug infused problem 3 and 9 solution and 2 files of newly generated test cases for each solution.

For this part, we ntroduce a small, realistic bug (off-by-one, wrong boundary, wrong exception handling, etc.) into your A1 solution and re-run tests and see if our test suite failed. 

To produce results locally, run this command in the terminal 
```bash
pytest --cov=. --cov-report=term-missing --cov-branch
```




