"""
eda.py - Workstream 2: exploratory data analysis and visualizations.

Owner: (fill in)

Needs at least 3 different chart types, clearly labeled.
"""

from data_prep import load_clean_data

import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == "__main__":
    df = load_clean_data()
    print(df.describe())
    # TODO: charts go here