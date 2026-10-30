# 1. Introduction to the Dataset

For this project we used the Telco Customer Churn dataset. It is sample data made by IBM about a made-up telecom company. Each row is one customer, with details about their account and the services they pay for.

We got the dataset from Kaggle (kaggle.com/datasets/blastchar/telco-customer-churn). We downloaded it as one CSV file on [date, ask Rommel] and saved it in our repo as `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`. We did not change the file itself. All cleaning is done in our Python code. The license on Kaggle is listed as “Data files © Original Authors”.

The data has 7,043 customers and 21 columns. Some columns are about the customer, like gender, whether they are a senior citizen, and whether they have a partner or dependents. Others are about their account, like how many months they have been a customer, their contract type, how they pay, and their monthly and total charges. The rest are about phone and internet services and add-ons like online security, tech support and streaming. There is also a customer ID, which we dropped because it is just a label.

We want to predict Churn, which means whether a customer left the company in the last month. About 26.5% of customers left, so around 1 in 4. This matters because it usually costs a telecom company more to get a new customer than to keep one. If the company knows who is likely to leave, it can try to keep them with better deals or support.