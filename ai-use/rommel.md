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
- What I asked: help reviewing teammates' pull requests and drafting report Section 4
- What I used: review checklists, and a draft of report/04_models.md
- What I changed or checked myself: ran Rejin's tests (all 5 passed), checked Rajendra's data dictionary against the code, and edited Section 4 so I can explain every part of it