# Decision Log

One line per cleaning or preprocessing decision, with the reason. This feeds the report's Cleaning and Preprocessing section.

| # | Column | Problem found | Decision | Why |
| --- | --- | --- | --- | --- |
| 1 | TotalCharges | Stored as text; 11 values were blank spaces, so `isnull()` reported 0 missing | Strip spaces, set the 11 blanks to 0, convert to float | All 11 blanks belong to customers with tenure 0, who have not been billed yet, so their total charges are 0. This keeps all 7,043 customers. |