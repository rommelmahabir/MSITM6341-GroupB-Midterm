# Decision Log

One line per cleaning or preprocessing decision, with the reason. This feeds the report's Cleaning and Preprocessing section.

| # | Column | Problem found | Decision | Why |
| --- | --- | --- | --- | --- |
| 1 | TotalCharges | Stored as text; 11 values were blank spaces, so `isnull()` reported 0 missing | Strip spaces, set the 11 blanks to 0, convert to float | All 11 blanks belong to customers with tenure 0, who have not been billed yet, so their total charges are 0. This keeps all 7,043 customers. |
| 2 | All columns | Checked for duplicates while customerID was present: 7,043 rows, 7,043 unique IDs, 0 exact duplicates | Removed nothing | Every row is a different customer. Ignoring the ID, 22 rows look identical, but they are different customers with the same details, so they stay. |
| 3 | customerID | An identifier, not a property of the customer | Dropped the column (7,043 rows, 20 columns remain) | A label cannot help predict churn, and leaving it in could mislead the models. |
| 4 | Churn (target) | Stored as "Yes"/"No" text; models need numbers | Mapped Yes to 1, No to 0 | Standard binary target for classification. Churn rate is 26.5%, so the classes are imbalanced. |
| 5 | 15 text feature columns | Models cannot read text categories such as "Month-to-month" | One-hot encoded with `pd.get_dummies(drop_first=True)` | Gives each category its own 0/1 column without implying an order. Dropping one category per column avoids duplicate information (the dummy variable trap). Result: 30 feature columns. |
| 6 | All rows | Need a fair test of how the models handle unseen customers | 80/20 train/test split, `stratify=y`, `random_state=42` | Stratifying keeps the churn rate at 26.5% in both sets. The fixed seed means both models use the identical split, so their scores are comparable. |
| 7 | tenure, MonthlyCharges, TotalCharges | Very different ranges (0–72 vs. up to about 8,700) | Standardized with `StandardScaler`, fit on the training set only | Puts the columns on a similar scale for Logistic Regression. Fitting on train only prevents test data leaking into training. Random Forest is unaffected by scale. |