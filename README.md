# MSITM6341-GroupB-Midterm
Group B midterm project - MSITM 6341 Python, 
Sarvagya TestPush
Team member: Rajendra Konduru
## Project Overview

This project analyzes customer churn using Python and machine learning. Our goal is to understand why customers leave a telecommunications company and compare different models to identify customers who may be at risk of leaving.

## Dataset

- **Dataset:** Telco Customer Churn
- **Source:** Telco Customer Churn dataset used in our project
- **Also published by IBM** on GitHub under the Apache 2.0 license (same data): [https://github.com/IBM/telco-customer-churn-on-icp4d](https://github.com/IBM/telco-customer-churn-on-icp4d)
- **Records:** 7,043 customers
- **Target variable:** Churn (Yes or No)

The dataset includes customer information such as tenure, monthly charges, contract type, and services.

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

Install the required Python packages:

`pip install -r requirements.txt`

Run the exploratory data analysis:

`python eda.py`

Run the Logistic Regression model:

`python model_logistic.py`

Run the Random Forest model:

`python model_random_forest.py`

Run the data preparation tests:

`python test_data_prep.py`

## Testing

The project includes five automated checks in `test_data_prep.py` to verify the cleaned dataset's shape, missing values, TotalCharges data type, customer ID removal, and Churn values.

All five checks passed during the team's review.

## Conclusion

This project helped our team understand how data preparation, visualization, and machine learning can support customer retention decisions. Our results also demonstrated why recall and F1 score are important when evaluating imbalanced classification problems.
