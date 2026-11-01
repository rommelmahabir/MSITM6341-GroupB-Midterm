# 2. Data Cleaning & Preprocessing

All cleaning and preprocessing happens in `data_prep.py`. The raw CSV is never edited, so every change can be traced and re-run from the original file. Two functions hand the data to the rest of the project:

- `load_clean_data()` returns the cleaned table in readable form (for example, "Month-to-month"), used for EDA in Section 3.
- `get_model_data()` returns the encoded, scaled training and test sets used by both models in Section 4.

Each decision below is also recorded in `DECISION_LOG.md`, and every column is described in the data dictionary.

## 2.1 Data Cleaning

The raw file has 7,043 rows and 21 columns.

**Missing values.** `TotalCharges` loaded as text instead of numbers, because 11 rows contained a blank space. All 11 belonged to customers with a tenure of 0 months: new customers who had not yet been billed. Their true total is therefore 0, so we set the blanks to 0 rather than dropping the rows (which would lose real customers) or filling them with the average (which would invent charges they never paid). The column was then converted to a number. No other column had missing values.

**Duplicates.** We checked for duplicates while `customerID` was still present: 7,043 rows and 7,043 unique IDs, with no duplicate rows, so nothing was removed. Once the ID is dropped, 22 rows share identical details, but they are different customers who happen to have the same profile, so we kept them.

**Invalid entries.** We checked every text column's values. Each has between 2 and 4 expected categories (for example, Yes / No / No internet service), with no typos or unexpected values, and `Churn` contains only "Yes" and "No".

**Irrelevant columns.** `customerID` was dropped. It labels a customer but does not describe them, so it cannot help predict churn.

The cleaned table has **7,043 rows and 20 columns**.

## 2.2 Preprocessing

The models need numbers on comparable scales, so we applied four steps:

| Step | What we did | Why |
| --- | --- | --- |
| Target encoding | `Churn`: Yes became 1, No became 0 | Models predict numbers. 26.5% of customers churned, so the classes are imbalanced |
| One-hot encoding | The 15 text columns became 26 columns of 0s and 1s, using `pd.get_dummies(drop_first=True)` | Gives each category its own column without implying an order. Dropping one category per column avoids duplicate information (the dummy variable trap) |
| Train/test split | 80% training (5,634 customers), 20% test (1,409), stratified, `random_state=42` | Stratifying keeps the 26.5% churn rate in both sets. The fixed seed means both models use the identical split |
| Scaling | `tenure`, `MonthlyCharges` and `TotalCharges` standardized with `StandardScaler`, fit on the training set only | These range from 0 to over 8,000, while the other features are 0 or 1. Fitting on training data only prevents information about the test set leaking into training |

The result is **30 feature columns**: the 26 one-hot columns plus `SeniorCitizen` (already 0/1), `tenure`, `MonthlyCharges` and `TotalCharges`.

## 2.3 Testing

`test_data_prep.py` checks that the cleaning worked: 7,043 rows and 20 columns, no missing values, `TotalCharges` stored as a number, `customerID` removed, and `Churn` containing only Yes and No. All five checks pass.