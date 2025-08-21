# Model-Wise Analysis on Marketing Data

![license](https://img.shields.io/badge/license-Apache--2.0-blue)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1z7EGRORU73TyEfgNBkVswOSrBArDEzy-?usp=sharing)

> Group project analyzing customer demographics and behavior to predict spending scores and loyalty program participation using multiple machine learning models.  
>This project has been built by Anam Ahamed, Mihika Grover, Preksha, Siddhant Grover and Siddhi.
---

## 🔍 Project Overview
This project explores how different models perform in understanding and predicting customer behavior in a marketing dataset. We applied clustering, regression, and classification methods to gain insights into customer spending patterns and loyalty program participation.

Key components:
- **Clustering (K-Means):** Segmented customers into 5 clusters using the elbow method; standardized variables ensured uniform analysis.  
- **ANOVA & Normality Testing:** Validated assumptions for regression; confirmed normal distribution through ANOVA and Q-Q plots.  
- **Multiple Linear Regression:** Modeled spending score with predictors Age, Income, and Online Shopping Frequency; explained 94.8% of variance.  
- **KNN:** Determined optimal `k=11`; analyzed accuracy, precision, recall, and F1 scores at cluster level.  
- **Naive Bayes:** Compared cluster-wise accuracy and recall; highlighted challenges with false negatives.  
- **CART (Decision Trees):** Derived interpretable decision rules; Income and Spending Score emerged as strongest loyalty predictors.  
- **Logistic Regression:** Modeled probability of loyalty program participation; moderate predictive accuracy (45–55%).  

<img width="713" height="470" alt="image" src="https://github.com/user-attachments/assets/ae684865-6d57-4055-b3dd-56f3e27f19da" />

<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/2ac5ab69-4527-4d8d-bc7f-60f23e910f08" />

<img width="562" height="461" alt="image" src="https://github.com/user-attachments/assets/c99bd524-49e0-460d-9faa-9220f4b21faa" />

---

## 🚀 Quickstart

### Run in Colab (Recommended)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1z7EGRORU73TyEfgNBkVswOSrBArDEzy-?usp=sharing)

### Run Locally
```bash
git clone https://github.com/<your-username>/<repo-name>
cd <Marketing_Data_Analysis>
pip install -r requirements.txt
Marketing_Analysis.ipynb
```
🧰 Tech Stack
Python, Google Colab → core environment
Libraries: NumPy, Pandas, Matplotlib, seaborn, scikit-learn
Methods Applied:
K-Means clustering
Multiple Linear Regression
K-Nearest Neighbors (KNN)
Naive Bayes
CART (Decision Trees)
Logistic Regression

📊 Key Findings

**Spending Score Predictors:**
* Online Shopping Frequency (+0.914 SD) and Income (+0.3429 SD) had the strongest positive effect on spending score.
* Age was statistically insignificant.

**Model Performance:**
* Regression: R² = 0.948 → strong explanatory power.
* KNN: Optimal k=11, but accuracy ~50%.
* Naive Bayes: Accuracy peaked at ~54%, but recall varied across clusters.
* CART: Cluster 0 performed best (53% accuracy), with clear decision rules based on Income & Spending Score.
* Logistic Regression: Accuracies between 45–55%, F1 scores between 0.37–0.55.

<img width="576" height="435" alt="image" src="https://github.com/user-attachments/assets/713f394e-6132-480a-8ac3-c55aaab7f3bc" />

<img width="565" height="432" alt="image" src="https://github.com/user-attachments/assets/ace0c764-97db-4d2f-8ea9-210773e1d693" />

For further key visualizations:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1z7EGRORU73TyEfgNBkVswOSrBArDEzy-?usp=sharing)


**Recommendations:**

* Retain high-income, frequent shoppers with exclusive loyalty offers.
* Promote cost-saving campaigns for low-income/infrequent shoppers.
* Use CART decision rules for real-time, personalized marketing strategies.

📂 **Repo Structure**:

*Marketing_Analysis.ipynb → main notebook with full workflow
*Marketing_DA.pdf → project presentation slides
*AIDA_Dataset(2).xlsx → dataset
*requirements.txt → Python dependencies

**ACKNOWLEDGEMENT**
Project completed as part of the Ariificial Intelligence in Data Analytics(AIDA) course under the guidance of Professor [Tushar Jaruhar](https://www.linkedin.com/in/tushar-jaruhar-9362959/) 
