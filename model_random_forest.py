"""
model_random_forest.py - Workstream 4: Random Forest model, tuning, comparison.

Owner: (fill in)

Use the same split and metrics as model_logistic.py so the two compare fairly.
"""

from data_prep import load_clean_data

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    df = load_clean_data()
    # TODO: split, fit, predict, tune and evaluate here