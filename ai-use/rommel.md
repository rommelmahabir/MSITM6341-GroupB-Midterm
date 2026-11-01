# Rommel's AI Use Log

Tool for all entries: Claude (Anthropic). I kept a detailed session-by-session log separately; this is the summary for the repository.

## 10/25–10/27: Setup and cleaning
- What I asked: help planning the project, setting up the repo structure and team workflow, and cleaning the data
- What I used: the project roadmap, kickoff agenda, setup guides for teammates, and the TotalCharges cleaning code in data_prep.py
- What I changed or checked myself: confirmed the 11 blank TotalCharges values all had tenure 0, checked for duplicates, verified the cleaned shape (7043, 20)

## 10/28: Preprocessing
- What I asked: code for one shared preprocessing function for both models
- What I used: get_model_data() (one-hot encoding, stratified split, scaling) and DECISION_LOG rows 4–7
- What I changed or checked myself: inspected the text columns first, ran it and confirmed (5634, 30) / (1409, 30) and a 0.265 churn rate in both sets

## 10/29: Models
- What I asked: Logistic Regression and Random Forest code, a class-weight comparison, and GridSearchCV tuning
- What I used: model_logistic.py, model_random_forest.py and DECISION_LOG rows 8–14
- What I changed or checked myself: ran both on my machine, worked through the confusion matrices, and used my own results where they differed slightly from the AI's test run

## 10/30: Reviews and report
- What I asked: help reviewing teammates' pull requests and drafting report Sections 2 and 4
- What I used: review checklists, and drafts of report/02_cleaning_preprocessing.md and report/04_models.md
- What I changed or checked myself: ran Rejin's tests (all 5 passed), checked Rajendra's data dictionary against the code, and edited Sections 2 and 4 so I can explain every part of them

## 10/31–11/1: Reviews, merges and final report
- What I asked: help reviewing and testing teammates' pull requests, resolving a merge conflict, checking the dataset license, and compiling the final report
- What I used: review checklists, conflict-resolution steps, and a build script that formats the report sections and charts into Word and PDF
- What I changed or checked myself: ran Sarvagya's EDA from a fresh state before approving, resolved the DECISION_LOG conflict, confirmed the IBM Apache 2.0 license on the dataset, and reviewed every page of the compiled report