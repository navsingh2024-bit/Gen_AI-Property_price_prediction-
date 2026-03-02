# Gen_AI-Property_price_prediction-
Intelligent Property Price Prediction is a machine learning–powered web application that estimates real estate prices based on property features such as location, area, number of bedrooms, amenities, and market trends.

# 🏠 Intelligent Property Price Prediction

An end-to-end Machine Learning system designed to predict residential property prices using structured housing data and regression algorithms.

---

## 📌 Project Overview

This project builds a complete machine learning pipeline for predicting property prices based on key features such as area, location, number of bedrooms, and amenities.

The system includes:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Model comparison
- Hyperparameter tuning
- Model evaluation
- Model serialization
- Deployment-ready structure

---

## 🎯 Problem Statement

Accurate property valuation is a complex problem influenced by multiple factors. Manual estimation methods are often inconsistent and subjective.

The objective of this project is to develop an intelligent ML-based system capable of predicting property prices accurately using historical housing data.

---

## 📊 Dataset Description

Source: Public Housing Dataset (e.g., Kaggle)

### Features:
- Location
- Area (sq ft)
- Bedrooms
- Bathrooms
- Furnishing Status
- Parking
- Property Type

### Target Variable:
- Price

---

## 📈 Exploratory Data Analysis

EDA techniques used:

- Correlation heatmap
- Distribution plots
- Outlier detection (IQR)
- Area vs Price analysis
- Location-wise pricing trends

### Key Insights:
- Area strongly correlates with price
- Location significantly impacts valuation
- Price distribution is right-skewed

---

## 🧠 Models Implemented

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

Models were compared using:

- MAE
- RMSE
- R² Score

Best performing model selected based on lowest RMSE and highest R².

---

## ⚙️ Optimization Techniques

- GridSearchCV for hyperparameter tuning
- 5-Fold Cross Validation
- Feature scaling
- Feature selection
- Overfitting prevention techniques

---

## 🏗 System Architecture

User Input → Data Preprocessing → Feature Encoding → Trained Model → Price Prediction → UI Output

---

## 💾 Model Serialization

Final trained model saved using Pickle:

```python
import pickle
pickle.dump(model, open("model.pkl", "wb"))
