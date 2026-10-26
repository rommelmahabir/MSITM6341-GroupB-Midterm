"""
model_logistic.py - Workstream 3: Logistic Regression model and evaluation.

Owner: (fill in)

Report precision, recall, F1 and a confusion matrix.
"""

from data_prep import load_clean_data

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    df = load_clean_data()
    # TODO: split, fit, predict and evaluate here