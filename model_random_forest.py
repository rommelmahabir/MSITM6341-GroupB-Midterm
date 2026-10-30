"""
model_random_forest.py - Workstream 4: Random Forest model, tuning, comparison.

Owner: Rommel Mahabir

Uses the same split (get_model_data) and metrics as model_logistic.py, so the
two models compare fairly. Trains three versions:
1. Default settings.
2. class_weight="balanced" (Rajendra's PR #3 suggestion, as in Model 1).
3. Tuned: GridSearchCV tries combinations of settings with 5-fold
   cross-validation on the training set only, picking the best F1.

Reports accuracy, precision, recall and F1, saves a confusion matrix for the
tuned model, and charts the 10 most important features.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import GridSearchCV

from data_prep import RANDOM_STATE, get_model_data

# Save charts next to this file, in the git-ignored charts/ folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHARTS_DIR = os.path.join(BASE_DIR, "charts")

# Settings GridSearchCV will try: 2 x 3 x 2 = 12 combinations
PARAM_GRID = {
    "n_estimators": [100, 200],       # number of trees in the forest
    "max_depth": [None, 5, 10],       # how deep each tree can grow (None = no limit)
    "min_samples_leaf": [1, 5],       # fewest customers allowed in a final leaf
}


def train_forest(X_train, y_train, class_weight=None):
    """Fit and return a Random Forest with 100 trees."""
    # random_state fixes the randomness, so results are the same every run
    model = RandomForestClassifier(
        n_estimators=100, class_weight=class_weight, random_state=RANDOM_STATE
    )
    model.fit(X_train, y_train)
    return model


def tune_forest(X_train, y_train):
    """
    Try every combination in PARAM_GRID and return the best model.

    cv=5 splits the TRAINING set into 5 parts and tests each combination 5
    times, so the test set is never used for tuning. scoring="f1" picks the
    combination that best balances precision and recall for churn.
    """
    base_model = RandomForestClassifier(class_weight="balanced", random_state=RANDOM_STATE)
    # n_jobs=-1 uses all CPU cores, so the search runs faster
    search = GridSearchCV(base_model, PARAM_GRID, cv=5, scoring="f1", n_jobs=-1)
    search.fit(X_train, y_train)

    print("\nBest settings found:", search.best_params_)
    print("Best cross-validated F1:", round(search.best_score_, 3))
    # best_estimator_ is already refit on the full training set
    return search.best_estimator_


def evaluate(model, X_test, y_test, label):
    """
    Print the classification report and return the 4 main scores.

    Precision, recall and F1 are for the churn class (1 = Yes).
    """
    y_pred = model.predict(X_test)

    print(f"\n===== {label} =====")
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
    sns.heatmap(
        matrix,
        annot=True,
        fmt="d",
        cmap="Greens",
        xticklabels=["No churn", "Churn"],
        yticklabels=["No churn", "Churn"],
    )
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()

    os.makedirs(CHARTS_DIR, exist_ok=True)
    plt.savefig(os.path.join(CHARTS_DIR, filename))
    plt.show()


def plot_feature_importance(model, feature_names, n=10):
    """
    Bar chart of the n features the forest relied on most.

    Importance shows how much a feature helped the trees split customers,
    but not whether it pushes toward or away from churn.
    """
    importances = pd.Series(model.feature_importances_, index=feature_names)
    top = importances.sort_values(ascending=False).head(n)

    print(f"\nTop {n} features by importance:")
    print(top.round(3))

    plt.figure(figsize=(7, 5))
    # Reverse the order so the most important feature sits at the top
    plt.barh(top.index[::-1], top.values[::-1])
    plt.title(f"Random Forest: Top {n} Features")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.tight_layout()

    os.makedirs(CHARTS_DIR, exist_ok=True)
    plt.savefig(os.path.join(CHARTS_DIR, "rf_feature_importance.png"))
    plt.show()


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = get_model_data()

    # --- Version 1: default settings ---
    default_model = train_forest(X_train, y_train)
    default_scores = evaluate(default_model, X_test, y_test, "Random Forest (default)")

    # --- Version 2: balanced class weights ---
    balanced_model = train_forest(X_train, y_train, class_weight="balanced")
    balanced_scores = evaluate(balanced_model, X_test, y_test, "Random Forest (balanced)")

    # --- Version 3: tuned with GridSearchCV (takes about a minute) ---
    print("\nTuning with GridSearchCV (12 combinations x 5 folds)...")
    tuned_model = tune_forest(X_train, y_train)
    tuned_scores = evaluate(tuned_model, X_test, y_test, "Random Forest (tuned)")

    # --- Side-by-side comparison ---
    comparison = pd.DataFrame([default_scores, balanced_scores, tuned_scores])
    print("\n===== Comparison =====")
    print(comparison.to_string(index=False))

    # --- Charts for the tuned model ---
    plot_confusion_matrix(tuned_model, X_test, y_test,
                          "Random Forest (tuned)", "cm_random_forest_tuned.png")
    plot_feature_importance(tuned_model, X_train.columns)