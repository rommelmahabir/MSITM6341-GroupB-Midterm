"""
data_prep.py - Workstream 1: data acquisition, cleaning and preprocessing.

Owner: Rommel Mahabir

Handoff for teammates:
- eda.py calls load_clean_data() to get the cleaned, human-readable DataFrame.
- The model files call get_model_data() to get encoded, scaled train/test sets.
Every cleaning or preprocessing choice gets one line in DECISION_LOG.md.
"""

import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Build the path from this file's location, so it works on any machine
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Settings shared by both models, so they are trained and tested the same way
TARGET_COLUMN = "Churn"
SCALE_COLUMNS = ["tenure", "MonthlyCharges", "TotalCharges"]
TEST_SIZE = 0.2      # 20% of customers held back for testing
RANDOM_STATE = 42    # fixed seed, so everyone gets the identical split


def load_raw_data():
    """Read the raw Telco CSV exactly as downloaded, with no changes."""
    return pd.read_csv(RAW_DATA_PATH)


def load_clean_data():
    """
    Return the cleaned DataFrame used by eda.py and the model files.

    Cleaning steps:
    1. TotalCharges: convert from text to numbers. The 11 blank values all
       belong to customers with tenure 0 (not yet billed), so they become 0.
    2. Duplicates: checked while customerID was present. 7,043 rows and
       7,043 unique IDs, 0 exact duplicates, so nothing is removed.
    3. customerID: dropped, because it labels a customer but does not
       describe them, so it cannot help predict churn.
    """
    df = load_raw_data()

    # --- TotalCharges: text with 11 blanks -> numbers ---
    # Remove stray spaces, so " " becomes "" and is easy to find
    df["TotalCharges"] = df["TotalCharges"].str.strip()
    # Blank means a new customer (tenure 0) who has paid nothing yet
    df["TotalCharges"] = df["TotalCharges"].replace("", "0")
    # Now every value is a number written as text, so convert to float
    df["TotalCharges"] = df["TotalCharges"].astype(float)

    # --- customerID: an identifier, not a feature ---
    # Do NOT drop duplicates after this line: 22 different customers share
    # identical details once the ID is gone, and they are real people.
    df = df.drop("customerID", axis=1)

    return df


def get_model_data():
    """
    Return X_train, X_test, y_train, y_test, ready for both models.

    Preprocessing steps:
    1. Target: Churn "Yes"/"No" becomes 1/0.
    2. Encoding: the 15 text columns become 0/1 columns with one-hot
       encoding (pd.get_dummies). drop_first=True drops one category per
       column, because it is implied when all the others are 0.
    3. Split: 80% train, 20% test, stratified so both sets keep the same
       churn rate (about 26%).
    4. Scaling: tenure, MonthlyCharges and TotalCharges are standardized
       (mean 0, std 1). The scaler learns from the training set only, then
       applies the same numbers to the test set.
    """
    df = load_clean_data()

    # --- 1. Target: Yes/No -> 1/0 ---
    y = df[TARGET_COLUMN].map({"Yes": 1, "No": 0})
    X = df.drop(TARGET_COLUMN, axis=1)

    # --- 2. One-hot encode every remaining text column ---
    # dtype=int gives 0/1 instead of True/False, which is easier to read
    X = pd.get_dummies(X, drop_first=True, dtype=int)

    # --- 3. One shared train/test split ---
    # stratify=y keeps the churn rate the same in train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    # --- 4. Scale the large-number columns ---
    # .copy() avoids pandas' SettingWithCopyWarning when we overwrite columns
    X_train = X_train.copy()
    X_test = X_test.copy()
    scaler = StandardScaler()
    # fit_transform on train: learn the mean/std, then apply them
    X_train[SCALE_COLUMNS] = scaler.fit_transform(X_train[SCALE_COLUMNS])
    # transform only on test: reuse the training mean/std, never re-learn
    X_test[SCALE_COLUMNS] = scaler.transform(X_test[SCALE_COLUMNS])

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    data = load_clean_data()
    print("Clean data:", data.shape)
    print(data.head())

    X_train, X_test, y_train, y_test = get_model_data()
    print("\nX_train:", X_train.shape, " X_test:", X_test.shape)
    print("Churn rate - train:", round(y_train.mean(), 3), " test:", round(y_test.mean(), 3))
    print("\nFirst 5 feature columns:", list(X_train.columns[:5]))