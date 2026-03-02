import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("🏠 Gurgaon Property Price Prediction")

# Example inputs (adjust according to your dataset columns)
area = st.number_input("Area (sq ft)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")

if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms
    }])
    
    prediction = model.predict(input_df)
    st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Crores")
