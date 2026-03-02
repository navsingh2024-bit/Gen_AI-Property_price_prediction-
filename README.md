# Gen_AI-Property_price_prediction-
Intelligent Property Price Prediction is a machine learning–powered web application that estimates real estate prices based on property features such as location, area, number of bedrooms, amenities, and market trends.


# 🏠 Intelligent Property Price Prediction

An end-to-end Machine Learning project that predicts residential property prices based on key features such as location, area, number of bedrooms, and amenities.

---

## 📌 Project Overview

This project builds a complete ML pipeline including:

- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Model Training & Comparison  
- Hyperparameter Tuning  
- Model Evaluation  
- Web Deployment  

The system provides real-time price predictions via an interactive web interface.

---

## 🎯 Problem Statement

Property price estimation is influenced by multiple factors and is often inconsistent when done manually.  
This project aims to develop an intelligent ML-based system to accurately predict housing prices using structured data.

---

## 📊 Dataset

**Source:** Public housing dataset (e.g., Kaggle)

### Features:
- Location  
- Area (sq. ft.)  
- Bedrooms  
- Bathrooms  
- Furnishing Status  
- Parking  
- Property Type  

### Target:
- Price  

---

## 📈 Exploratory Data Analysis

- Correlation Heatmap  
- Price Distribution Analysis  
- Outlier Detection (IQR Method)  
- Area vs Price Relationship  

### Key Insight:
Area and Location have the strongest impact on property prices.

---

## 🧠 Models Implemented

- Linear Regression  
- Ridge & Lasso Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- XGBoost Regressor  

Best model selected based on:
- MAE  
- RMSE  
- R² Score  

---

## 📊 Model Evaluation (Example)

| Model | MAE | RMSE | R² |
|-------|------|------|------|
| Linear Regression | XX | XX | XX |
| Random Forest | XX | XX | XX |
| XGBoost | XX | XX | XX |

---

## ⚙️ Optimization Techniques

- GridSearchCV  
- Cross Validation  
- Feature Selection  
- Log Transformation  
- Regularization  

---

## 🏗 System Architecture

User Input → Preprocessing → Feature Encoding → Trained Model → Prediction → UI Output

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- XGBoost  
- Streamlit  

---

## 🚀 Installation

```bash
git clone https://github.com/your-username/property-price-prediction.git
cd property-price-prediction
pip install -r requirements.txt
streamlit run app.py
