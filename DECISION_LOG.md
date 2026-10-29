# Decision Log

One line per cleaning or preprocessing decision, with the reason. This feeds the report's Cleaning and Preprocessing section.

| # | Column | Problem found | Decision | Why |
| --- | --- | --- | --- | --- |
| 1 | TotalCharges | Stored as text; 11 values were blank spaces, so `isnull()` reported 0 missing | Strip spaces, set the 11 blanks to 0, convert to float | All 11 blanks belong to customers with tenure 0, who have not been billed yet, so their total charges are 0. This keeps all 7,043 customers. |
| 2 | All columns | Checked for duplicates while customerID was present: 7,043 rows, 7,043 unique IDs, 0 exact duplicates | Removed nothing | Every row is a different customer. Ignoring the ID, 22 rows look identical, but they are different customers with the same details, so they stay. |
| 3 | customerID | An identifier, not a property of the customer | Dropped the column (7,043 rows, 20 columns remain) | A label cannot help predict churn, and leaving it in could mislead the models. |