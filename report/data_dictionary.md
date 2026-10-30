# Data Dictionary

The raw file `data/WA_Fn-UseC_-Telco-Customer-Churn.csv` has 7,043 rows (one per customer) and 21 columns. Row numbers in brackets refer to `DECISION_LOG.md`.

| Column | What it means | Raw type | How we cleaned or encoded it |
| --- | --- | --- | --- |
| customerID | Unique ID for each customer | Text | Dropped: it labels a customer but doesn't describe them (Decision Log row 3) |
| gender | Customer's gender: Male or Female | Text | One-hot encoded into 1 column (row 5) |
| SeniorCitizen | Whether the customer is 65 or older: 1 = yes, 0 = no | Number (0/1) | Unchanged: already 0/1 |
| Partner | Whether the customer has a partner or spouse | Yes/No | One-hot encoded into 1 column (row 5) |
| Dependents | Whether the customer has dependents, such as children | Yes/No | One-hot encoded into 1 column (row 5) |
| tenure | Number of months the customer has been with the company (0–72) | Number | Scaled with StandardScaler, fit on the training set only (row 7) |
| Contract | Contract length: Month-to-month, One year or Two year | Text | One-hot encoded into 2 columns (row 5) |
| PaperlessBilling | Whether the customer gets bills online instead of on paper | Yes/No | One-hot encoded into 1 column (row 5) |
| PaymentMethod | How the customer pays: Electronic check, Mailed check, Bank transfer (automatic) or Credit card (automatic) | Text | One-hot encoded into 3 columns (row 5) |
| MonthlyCharges | Amount billed each month, in dollars (about $18–$119) | Number | Scaled with StandardScaler, fit on the training set only (row 7) |
| TotalCharges | Total amount billed to date | Text | 11 blanks (all tenure 0) set to 0, converted to a number, then scaled (rows 1, 7) |
| PhoneService | Whether the customer has phone service | Yes/No | One-hot encoded into 1 column (row 5) |
| MultipleLines | Whether the customer has more than one phone line: Yes, No, or No phone service (for customers without phone service) | Text | One-hot encoded into 2 columns (row 5) |
| InternetService | Type of internet service: DSL, Fiber optic, or No | Text | One-hot encoded into 2 columns (row 5) |
| OnlineSecurity | Whether the customer has the online security add-on: Yes, No, or No internet service | Text | One-hot encoded into 2 columns (row 5) |
| OnlineBackup | Whether the customer has the online backup add-on: Yes, No, or No internet service | Text | One-hot encoded into 2 columns (row 5) |
| DeviceProtection | Whether the customer has the device protection add-on: Yes, No, or No internet service | Text | One-hot encoded into 2 columns (row 5) |
| TechSupport | Whether the customer has the tech support add-on: Yes, No, or No internet service | Text | One-hot encoded into 2 columns (row 5) |
| StreamingTV | Whether the customer streams TV: Yes, No, or No internet service | Text | One-hot encoded into 2 columns (row 5) |
| StreamingMovies | Whether the customer streams movies: Yes, No, or No internet service | Text | One-hot encoded into 2 columns (row 5) |
| Churn | Whether the customer left in the last month | Yes/No | Target: Yes = 1, No = 0 (row 4) |

**Notes**

- One-hot encoding uses `drop_first=True`, so a column with 2 values becomes 1 column and a column with 3 values becomes 2. The 15 text columns become 26 columns; with SeniorCitizen, tenure, MonthlyCharges and TotalCharges, the models use 30 feature columns.
- "No phone service" and "No internet service" mean the customer doesn't have the base service, so the add-on doesn't apply. That is why those columns have 3 values instead of 2.
- No duplicate customers were found, so no rows were removed (row 2).