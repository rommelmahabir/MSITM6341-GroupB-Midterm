# 4. Model Building & Evaluation

## 4.1 Approach

Both models were trained and tested on exactly the same data, using the shared `get_model_data()` function from Section 2: 30 encoded features, a stratified 80/20 split (5,634 training and 1,409 test customers), and a fixed random seed. This makes their scores directly comparable.

Because only 26.5% of customers churn, accuracy alone is misleading: a model that predicts "No churn" for everyone would score 73.5% while catching no churners at all. We therefore report four metrics for the churn class:

- **Accuracy:** the share of all predictions that were correct
- **Precision:** of the customers flagged as churners, the share who actually left
- **Recall:** of the customers who actually left, the share the model caught
- **F1:** a single score balancing precision and recall

For a churn problem, **recall matters most**. Missing a customer who is about to leave costs more than offering a retention deal to someone who would have stayed.

## 4.2 Model 1: Logistic Regression

We started with Logistic Regression as a simple, interpretable baseline (`max_iter=1000`). During the review of our preprocessing, Rajendra suggested trying `class_weight="balanced"`, which gives the rarer churners more weight during training. We trained both versions:

| Version | Accuracy | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| Default | 0.806 | 0.659 | 0.559 | 0.605 |
| Balanced | 0.738 | 0.504 | **0.783** | **0.614** |

The default model caught only 209 of the 374 churners in the test set and missed 165. Balanced weights raised recall from 56% to 78%. Accuracy fell because the model now flags more customers, including some who stay, but F1 improved slightly, and the model finds far more of the customers who matter.

Logistic Regression also shows the direction of each feature's effect. The strongest signals toward churn were **Fiber optic internet** and **electronic check payments**; the strongest away from churn were **two-year contracts**, **one-year contracts** and **longer tenure**. Some coefficients should be read with care: features such as MonthlyCharges and TotalCharges overlap heavily with the service and tenure columns (multicollinearity), so individual coefficients show patterns rather than exact effects.

*[Figure 4.1: Confusion matrices for Logistic Regression, default and balanced. Files: charts/cm_logistic_default.png, charts/cm_logistic_balanced.png]*

## 4.3 Model 2: Random Forest

Random Forest combines many decision trees and can capture interactions between features that Logistic Regression can't. We trained three versions:

| Version | Accuracy | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| Default | 0.789 | 0.629 | 0.503 | 0.559 |
| Balanced | 0.791 | 0.637 | 0.492 | 0.555 |
| Tuned | 0.760 | 0.536 | **0.725** | **0.616** |

Unlike with Logistic Regression, balanced weights alone barely changed the default Random Forest. Its trees grow without a depth limit until every leaf is pure, so the weights have almost nothing to act on.

We then tuned the model with `GridSearchCV`, testing 12 combinations of tree count, maximum depth and minimum leaf size. Each combination was scored on F1 using 5-fold cross-validation on the **training set only**, so the test set was never used for tuning. The best settings were `max_depth=10`, `min_samples_leaf=1` and `n_estimators=200` (cross-validated F1 of 0.636). Limiting the depth let the balanced weighting work: recall rose from 0.50 to 0.73. The tuned model caught 271 of the 374 churners. Random Forest results can differ slightly in the third decimal place between scikit-learn versions, because the trees are built from random samples; the figures above come from our development environment, and the conclusions are the same in either case.

The features the forest relied on most were **tenure**, **TotalCharges**, **MonthlyCharges**, **two-year contracts** and **Fiber optic internet**.

*[Figure 4.2: Random Forest (tuned) confusion matrix and top 10 feature importances. Files: charts/cm_random_forest_tuned.png, charts/rf_feature_importance.png]*

## 4.4 Comparison and Recommended Model

| Model | Accuracy | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| Logistic Regression (balanced) | 0.738 | 0.504 | **0.783** | 0.614 |
| Random Forest (tuned) | 0.760 | 0.536 | 0.725 | **0.616** |

The two models are effectively tied on F1. We recommend **Logistic Regression (balanced)** because it catches more of the customers who actually leave (78% vs 72%), it is simpler and faster, and it shows whether each factor increases or decreases churn risk. The more complex model did not earn its extra complexity on this dataset.

Both models agree on the main drivers of churn: **short tenure**, **month-to-month contracts** and **Fiber optic internet**. The main trade-off is precision: about half the customers the recommended model flags would not actually have left, so any retention offer should be low-cost enough to justify those false alarms.