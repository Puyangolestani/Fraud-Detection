# Fraud-Detection

# Fraud Detection Project

---

## Overview

This project focuses on detecting **fraudulent transactions** in financial data using advanced **machine learning techniques**. The dataset contains over **6 million transactions** with diverse features that help identify potentially fraudulent activities.

The main goal is to build a predictive model that can accurately classify transactions as **fraudulent** or **legitimate**.

---

## Dataset

The dataset used in this project was sourced from Kaggle:

🔗 [Fraud Detection Dataset on Kaggle](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download)

### Features Included:

- `step`: Represents a unit of time (1 hour)
- `type`: Type of transaction (CASH_IN, CASH_OUT, DEBIT, PAYMENT, TRANSFER)
- `amount`: Amount of the transaction
- `nameOrig`: Customer who initiated the transaction
- `oldbalanceOrg`: Initial balance before the transaction
- `newbalanceOrig`: New balance after the transaction
- `nameDest`: Recipient of the transaction
- `oldbalanceDest`: Initial balance of recipient before transaction
- `newbalanceDest`: New balance of recipient after transaction
- `isFraud`: Whether the transaction is fraudulent (`1`) or not (`0`)
- `isFlaggedFraud`: Whether the transaction was flagged as fraud

---

## Key Findings

- The dataset contains **6,362,620** transactions, with only **8,213 (0.13%)** being fraudulent, highlighting a **highly imbalanced dataset**.
- Fraudulent transactions primarily occur in:
  - `TRANSFER` transactions (**0.77%** fraud rate)
  - `CASH_OUT` transactions (**0.18%** fraud rate)
- The average transaction amount is approximately **179,861**, with a maximum value of **92,445,516**.

---

## Methodology

- **Data Exploration**  
  Initial analysis of transaction types, fraud distribution, and amount statistics.
  
- **Feature Engineering**  
  Creation of new features to improve fraud detection accuracy.
  
- **Model Building**  
  Development and training of machine learning models for transaction classification.
  
- **Evaluation**  
  Performance assessment using metrics tailored for imbalanced datasets, ensuring robustness.

---

## Interactive Demo

Experience the project interactively through the Streamlit web application:

🔗 [Fraud Detection Web App](https://fraud-detection-np3ugedhcpri9mazedwxbu.streamlit.app/)

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Streamlit (for the web app)

---


