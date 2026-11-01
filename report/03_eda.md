# 3. EDA & Key Insights

## 3.1 Overview of the Data
The dataset contains 7,043 customer records and 20 columns covering customer demographics, services, contract information, monthly charges, total charges, and churn status. The initial data inspection using df.info() showed that all columns contain 7,043 non-null values, indicating no missing values after cleaning. The numerical variables include SeniorCitizen, tenure, MonthlyCharges, and TotalCharges. Customer tenure ranges from 0 to 72 months, with an average of approximately 32.4 months. Monthly charges range from $18.25 to $118.75, with an average of $64.76. Total charges average approximately $2,279.73.

The target variable, Churn, is imbalanced: 5,174 customers (73.5%) stayed, while 1,869 customers (26.5%) left. This imbalance is important when evaluating classification models because accuracy alone may not adequately measure how well a model identifies customers who churn.

## 3.2 Key Insights

### 1. Customer Churn Distribution
The churn distribution shows that most customers stayed with the company, while approximately 26.5% discontinued their service. This class imbalance is important for model development because the classification models should identify customers who leave rather than simply favoring the larger group of customers who stay.

Figure 3.1: Customer Churn Distribution. File: charts/churn_distribution.png

### 2. Tenure by Churn
The tenure histogram shows that churn is concentrated among customers with shorter tenure. Customers who have stayed with the company for longer periods are more likely to remain customers. This suggests that the early stages of the customer relationship may be an important period for retention efforts.

Figure 3.2: Tenure by Churn. File: charts/tenure_by_churn.png

### 3. Monthly Charges by Churn
The box plot indicates that customers who churn generally pay higher monthly charges than customers who stay. The median monthly charge is approximately $80 for customers who left, compared with approximately $64 for customers who stayed. This suggests that monthly pricing may be associated with customer retention.

Figure 3.3: Monthly Charges by Churn. File: charts/monthly_charges_by_churn.png

### 4. Churn Rate by Contract
Contract type shows a substantial difference in churn rates. Month-to-month customers have the highest churn rate at approximately 42.7%, compared with 11.3% for one-year contracts and 2.8% for two-year contracts. Customers with longer-term contracts appear more likely to remain with the company.

Figure 3.4: Churn Rate by Contract. File: charts/churn_by_contract.png

### 5. Correlation Heatmap
The correlation heatmap shows a strong positive relationship between tenure and TotalCharges (approximately 0.83). This is reasonable because customers who remain longer generally accumulate higher total charges. MonthlyCharges and TotalCharges also show a positive correlation (approximately 0.65). These relationships help explain how customer duration and spending patterns are connected.

Figure 3.5: Correlation Heatmap. File: charts/correlation_heatmap.png

## 3.3 Summary
Overall, the EDA highlights customer tenure and contract type as important patterns associated with churn. The higher churn rate among month-to-month customers and the concentration of churn among newer customers suggest useful areas for retention strategies. These findings also align with the Section 4 model results, where tenure and contract type were among the strongest predictors in both Logistic Regression and Random Forest. The EDA therefore provides a useful foundation for understanding and interpreting the classification models.