"""
data_prep.py - Workstream 1: data acquisition, cleaning and preprocessing.

Owner: (fill in)

Handoff for teammates: call load_clean_data() to get the cleaned DataFrame.
Every cleaning choice gets one line in DECISION_LOG.md.
"""

import os

import pandas as pd

# Build the path from this file's location, so it works on any machine
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "WA_Fn-UseC_-Telco-Customer-Churn.csv")


def load_raw_data():
    """Read the raw Telco CSV exactly as downloaded, with no changes."""
    return pd.read_csv(RAW_DATA_PATH)


def load_clean_data():
    """
    Return the cleaned DataFrame used by eda.py and the model files.

    TODO (owner): convert TotalCharges to numbers, handle blanks and
    duplicates, and drop customerID.
    """
    df = load_raw_data()
    # TODO: cleaning steps go here
    return df


if __name__ == "__main__":
    data = load_clean_data()
    print(data.shape)
    print(data.head())