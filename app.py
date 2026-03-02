import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Intelligent Property Price Prediction")

area = st.number_input("Area (sq ft)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")

if st.button("Predict Price"):
    prediction = model.predict([[area, bedrooms, bathrooms]])
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")
