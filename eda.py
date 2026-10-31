"""
eda.py - Workstream 2: exploratory data analysis and visualizations.

Owner: Sarvagya Dubey

Needs at least 3 different chart types, clearly labeled.
"""

from data_prep import load_clean_data

import matplotlib.pyplot as plt
import seaborn as sns
import os


if __name__ == "__main__":
    # Load the cleaned dataset
    df = load_clean_data()

    # Create charts folder if it does not exist
    os.makedirs("charts", exist_ok=True)

    # Display basic information about the dataset
    print("\n--- Dataset Information ---")
    df.info() #shows columns, data types and missing values

    # Display descriptive statistics
    print("\n--- Descriptive Statistics ---")
    print(df.describe()) #Shows mean, standard deviation, minimum, maximum, etc.

    # Display churn counts
    print("\n--- Churn Counts ---")
    print(df['Churn'].value_counts()) #Counts customers who stayed vs. left

    # Calculate churn percentage
    print("\n--- Churn Percentage ---")
    print(df['Churn'].value_counts(normalize=True) * 100) #Converts counts into proportions and Converts proportions into percentages

    # Chart 1: Customer Churn Distribution
    #The churn distribution shows that approximately 73.46% of customers stayed 
    #with the company, while 26.54% discontinued their services. 
    #This indicates a class imbalance in the dataset, which should be 
    #considered when building and evaluating classification models.

    plt.figure(figsize=(7, 5))

    sns.countplot(data=df, x='Churn')

    plt.title('Customer Churn Distribution')
    plt.xlabel('Churn Status')
    plt.ylabel('Number of Customers')

    plt.savefig('charts/churn_distribution.png')
    plt.show()

    # Chart 2: Customer Tenure Distribution by Churn
    # The tenure distribution indicates that customer churn is concentrated 
    # among customers with shorter service histories. Customers with longer 
    # tenure are more likely to remain with the company, suggesting that 
    # early customer engagement and retention strategies could help reduce churn.


    plt.figure(figsize=(8, 5)) #Sets chart dimensions

    sns.histplot(
        data=df,
        x='tenure', # Uses customer tenure in months
        hue='Churn',# Separates customers who stayed and left
        bins=20, # Divides tenure into 20 interval
        multiple='layer', # Overlays the two distributions
        alpha=0.6 # Makes bars slightly transparent
    )   

    plt.title('Customer Tenure Distribution by Churn')
    plt.xlabel('Tenure (Months)')
    plt.ylabel('Number of Customers')

    plt.savefig('charts/tenure_by_churn.png') #Saves the chart as a PNG
    plt.show()

    # Chart 3: Monthly Charges by Churn
    # The box plot indicates that customers who churn tend to have 
    # higher monthly charges than customers who remain. The median monthly 
    # charge for churned customers is approximately $80, compared with approximately 
    # $64 for retained customers. 
    # This suggests that pricing and service costs may be factors associated with customer churn.

    plt.figure(figsize=(8, 5)) # Sets chart size

    sns.boxplot(
        data=df,
        x='Churn', # Separates customers into Yes and No
        y='MonthlyCharges' # Compares monthly bills
    )

    plt.title('Monthly Charges by Churn Status')
    plt.xlabel('Churn Status')
    plt.ylabel('Monthly Charges ($)')

    plt.savefig('charts/monthly_charges_by_churn.png')
    plt.show()

    # Chart 4: Churn Rate by Contract Type
    # Contract type is strongly associated with customer churn. 
    # Month-to-month customers have the highest churn rate at approximately 42.7%, 
    # compared with 11.3% for one-year contracts and 2.8% for two-year contracts. 
    # This suggests that longer-term contracts are associated with better customer retention. 
    # The company could explore incentives to encourage customers to move toward longer-term contracts.

    # Calculate churn rate for each contract type
    contract_churn = df.groupby('Contract')['Churn'].apply(
        lambda x: (x == 'Yes').mean() * 100
    ).reset_index(name='ChurnRate')

    plt.figure(figsize=(8, 5))

    sns.barplot(
        data=contract_churn,
        x='Contract',
        y='ChurnRate'
    )

    plt.title('Churn Rate by Contract Type')
    plt.xlabel('Contract Type')
    plt.ylabel('Churn Rate (%)')

    plt.savefig('charts/churn_by_contract.png')
    plt.show()

    # Chart 5: Correlation Heatmap
    # Tenure and Total Charges had a strong positive correlation (0.83), 
    # while Monthly Charges and Total Charges had a positive correlation (0.65)

    # Select numerical columns and calculate correlations
    correlation = df.corr(numeric_only=True) # Calculates correlations between numerical columns only

    plt.figure(figsize=(8, 6)) #sets chart size

    sns.heatmap( # Creates the heatmap
        correlation,
        annot=True, # Displays correlation values inside cells
        cmap='coolwarm', # uses a color gradient from blue to red
        fmt='.2f', # formats correlation values to two decimal places
        linewidths=0.5 # adds lines between cells for better readability
    )

    plt.title('Correlation Heatmap of Numerical Variables')

    plt.savefig('charts/correlation_heatmap.png')
    plt.show()