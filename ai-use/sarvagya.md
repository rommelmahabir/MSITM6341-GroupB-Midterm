# AI Usage Log – Sarvagya

## Session 1 – Exploratory Data Analysis (EDA)

**Date:** October 31, 2026

**Tool:** ChatGPT

**What I asked:**
I asked ChatGPT for guidance on completing the Exploratory Data Analysis (EDA) portion of our Telco Customer Churn classification project. I requested help understanding the dataset, calculating descriptive statistics, creating visualizations, and interpreting the results.

**What I used:**
- Guidance on using pandas to inspect the dataset and calculate descriptive statistics.
- Python code examples using Matplotlib and Seaborn to create five visualizations:
  1. Customer churn distribution.
  2. Customer tenure distribution by churn.
  3. Monthly charges by churn status.
  4. Churn rate by contract type.
  5. Correlation heatmap of numerical variables.
- Explanations of Python functions, visualization parameters, and statistical concepts.

**What I changed/fixed:**
I added the suggested code to my `eda.py` file and adjusted it to work with our group's `load_clean_data()` function. I also corrected a missing comma in the histogram code and made sure the chart folder name matched the save path.

**How I checked it works:**
I ran `python3 eda.py` in the VS Code terminal, reviewed the dataset statistics, and confirmed that all five charts were generated and saved in the `charts` folder. I reviewed the visualizations and interpreted the key findings, including customer churn distribution, tenure patterns, monthly charges, contract type, and numerical correlations.

**My contribution:**
I implemented and tested the EDA code, reviewed the generated charts, and identified key insights to share with the project team.

## Session – November 1, 2026

- **Tool:** ChatGPT
- **Purpose:** Assistance with drafting Section 3 – EDA & Key Insights.
- **What I asked:** Help interpreting descriptive statistics and chart findings, organizing the EDA report, and troubleshooting Python environment issues.
- **What I used:** Guidance on report structure, explanations of dataset statistics, and assistance with Markdown formatting.
- **What I changed or checked:** Reviewed the report against the actual EDA output, verified the five chart filenames, installed the missing scikit-learn dependency, and reran the Python script.