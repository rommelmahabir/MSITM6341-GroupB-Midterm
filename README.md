# Telco Customer Churn Prediction

MSITM 6341 (Python) midterm project, Group B, Dallas Baptist University.
## Project Overview

This project analyzes customer churn using Python and machine learning. Our goal is to understand why customers leave a telecommunications company and compare different models to identify customers who may be at risk of leaving.

## Team

| Member | Role |
| --- | --- |
| Rommel Mahabir | Data cleaning, preprocessing, both models, project coordination |
| Sarvagya Dubey | Exploratory data analysis and charts |
| Rajendra Konduru | Data dictionary, Introduction, Conclusion and References |
| Rejin Sudarsanan Reji | Data tests and README |

## Dataset

- **Dataset:** Telco Customer Churn (IBM sample data)
- **Source:** downloaded from Kaggle: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- **Also published by IBM** on GitHub under the Apache 2.0 license (same data): https://github.com/IBM/telco-customer-churn-on-icp4d
- **File:** `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`
- **Size:** 7,043 customers, 21 columns
- **Target variable:** Churn (Yes or No); about 26.5% of customers churned

The dataset includes customer information such as tenure, monthly charges, contract type, and services.

## Project Structure

| File or folder | What it does |
| --- | --- |
| `data/` | The raw dataset |
| `data_prep.py` | Loads and cleans the data, and prepares it for the models |
| `eda.py` | Summary statistics and 5 charts exploring churn |
| `model_logistic.py` | Logistic Regression model, default vs balanced class weights |
| `model_random_forest.py` | Random Forest model: default, balanced, and tuned with GridSearchCV |
| `test_data_prep.py` | Five checks that the cleaned data is correct |
| `DECISION_LOG.md` | Every cleaning, preprocessing and modeling decision, with the reason |
| `report/` | The report sections, one Markdown file per section |
| `ai-use/` | Each member's AI use log |
| `requirements.txt` | The Python libraries the project needs |

Charts are saved to a `charts/` folder when you run the code. They aren't stored in the repository.

## Data Preparation

We cleaned and prepared the dataset before training our models.

- Checked for missing values.
- Converted TotalCharges into a numeric data type.
- Removed customerID from the model features.
- Converted categorical variables into numerical features.
- Split the data into training and testing sets.

## Exploratory Data Analysis

We explored the dataset using Python visualizations to understand customer characteristics and identify patterns associated with churn.

## Machine Learning Models

We compared two classification algorithms:

**1. Logistic Regression**

We tested default and balanced class weights to understand how weighting affects churn prediction.

**2. Random Forest**

We tested default, balanced, and tuned versions to improve prediction performance.

## Model Evaluation

We evaluated the models using accuracy, precision, recall, F1 score, and confusion matrices.

| Model | Recall | F1 Score |
|---|---:|---:|
| Logistic Regression (balanced) | 0.783 | 0.614 |
| Random Forest (tuned) | 0.725 | 0.616 |

Although the tuned Random Forest had a slightly higher F1 score, balanced Logistic Regression achieved better recall and was easier to interpret. Therefore, Logistic Regression was recommended for identifying customers at risk of churn.

## How to Run the Project

1. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

2. Run each file from the project folder (on Windows, use `python` instead of `python3`):

   ```
   python3 data_prep.py
   python3 test_data_prep.py
   python3 eda.py
   python3 model_logistic.py
   python3 model_random_forest.py
   ```

## Testing

The project includes five automated checks in `test_data_prep.py` to verify the cleaned dataset's shape, missing values, TotalCharges data type, customer ID removal, and Churn values.

All five checks passed during the team's review.

## Conclusion

This project helped our team understand how data preparation, visualization, and machine learning can support customer retention decisions. Our results also demonstrated why recall and F1 score are important when evaluating imbalanced classification problems.
## AI Use

The course allows generative AI. Each team member documents their AI use in the `ai-use/` folder
