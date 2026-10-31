"""
model_logistic.py - Workstream 3: Logistic Regression model and evaluation.

Owner: Rommel Mahabir

Trains Logistic Regression twice on the shared split from get_model_data():
1. Default settings.
2. class_weight="balanced" (suggested by Rajendra in his review of PR #3),
   because only about 26.5% of customers churn.

Reports accuracy, precision, recall and F1 for each, saves a confusion
matrix chart for each, and lists the features that push churn up or down.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

from data_prep import get_model_data

# Save charts next to this file, in the git-ignored charts/ folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHARTS_DIR = os.path.join(BASE_DIR, "charts")


def train_logistic(X_train, y_train, class_weight=None):
    """
    Fit and return a Logistic Regression model.

    class_weight=None treats every customer equally.
    class_weight="balanced" gives the rarer churners more weight.
    """
    # max_iter=1000 gives the solver enough steps to finish (avoids a warning)
    model = LogisticRegression(max_iter=1000, class_weight=class_weight, random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test, label):
    """
    Print the classification report and return the 4 main scores.

    Precision, recall and F1 are for the churn class (1 = Yes).
    """
    y_pred = model.predict(X_test)

    print(f"\n===== {label} =====")
    # target_names labels the 0/1 rows so the report is easier to read
    print(classification_report(y_test, y_pred, target_names=["No churn", "Churn"]))

    return {
        "Model": label,
        "Accuracy": round(accuracy_score(y_test, y_pred), 3),
        "Precision": round(precision_score(y_test, y_pred), 3),
        "Recall": round(recall_score(y_test, y_pred), 3),
        "F1": round(f1_score(y_test, y_pred), 3),
    }


def plot_confusion_matrix(model, X_test, y_test, title, filename):
    """Draw the confusion matrix as a labeled heatmap, save it, then show it."""
    y_pred = model.predict(X_test)
    matrix = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(5, 4))
    # annot=True writes the count in each box; fmt="d" shows whole numbers
    sns.heatmap(
        matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["No churn", "Churn"],
        yticklabels=["No churn", "Churn"],
    )
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()

    # Create charts/ if needed, and save BEFORE show (show clears the figure)
    os.makedirs(CHARTS_DIR, exist_ok=True)
    plt.savefig(os.path.join(CHARTS_DIR, filename))
    plt.show()


def show_top_features(model, feature_names, n=5):
    """
    Print the features with the largest positive and negative coefficients.

    Positive = pushes the prediction toward churn.
    Negative = pushes it toward staying.
    """
    # model.coef_[0] holds one coefficient per feature column
    coefficients = pd.Series(model.coef_[0], index=feature_names).sort_values()

    print(f"\nTop {n} features pushing TOWARD churn:")
    print(coefficients.tail(n)[::-1].round(3))
    print(f"\nTop {n} features pushing AWAY from churn:")
    print(coefficients.head(n).round(3))


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = get_model_data()

    # --- Version 1: default settings ---
    default_model = train_logistic(X_train, y_train)
    default_scores = evaluate(default_model, X_test, y_test, "Logistic Regression (default)")

    # --- Version 2: balanced class weights ---
    balanced_model = train_logistic(X_train, y_train, class_weight="balanced")
    balanced_scores = evaluate(balanced_model, X_test, y_test, "Logistic Regression (balanced)")

    # --- Side-by-side comparison ---
    comparison = pd.DataFrame([default_scores, balanced_scores])
    print("\n===== Comparison =====")
    print(comparison.to_string(index=False))

    # --- What drives churn (from the balanced model) ---
    show_top_features(balanced_model, X_train.columns)

    # --- Confusion matrix charts ---
    plot_confusion_matrix(default_model, X_test, y_test,
                          "Logistic Regression (default)", "cm_logistic_default.png")
    plot_confusion_matrix(balanced_model, X_test, y_test,
                          "Logistic Regression (balanced)", "cm_logistic_balanced.png")