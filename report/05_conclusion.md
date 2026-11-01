# 5. Conclusion

The goal of this project was to figure out which telecom customers are likely to leave. We used the Telco Customer Churn dataset and built two models, Logistic Regression and Random Forest, both tested on the same data split.

Our pick is Logistic Regression with balanced class weights. The two models ended up almost tied on F1 (0.614 vs 0.616), but Logistic Regression caught more of the customers who actually left, 78% compared to 72%. It's also simpler, and it's easier to see how each factor affects churn. Balancing the class weights was a big part of this, since it pushed recall up from 56% to 78%.

Both models pointed to the same three reasons customers leave:

- **Tenure:** new customers are the most likely to leave. Extra support or a small welcome offer in the first few months could help.
- **Contract type:** month-to-month customers leave a lot more than those on two-year contracts. Offering a discount to switch to a longer contract could keep more of them.
- **Fiber optic internet:** these customers churn more than others. It would be worth looking into whether the price or the service is the problem.

 This is sample data from a made-up company, so real results could look different. The model also flags a lot of customers who end up staying, since its precision is only about 0.50. We're okay with that, because losing a customer costs more than sending someone an offer they didn't need.

In the future we can try other models like gradient boosting, do more tuning, and test on real or more recent customer data.