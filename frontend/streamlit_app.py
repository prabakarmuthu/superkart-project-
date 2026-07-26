import streamlit as st
import requests

st.title("SuperKart Sales Forecast")

product_weight = st.number_input("Product Weight")
product_mrp = st.number_input("Product MRP")

if st.button("Predict"):

    payload = {
        "Product_Weight": product_weight,
        "Product_MRP": product_mrp
    }

    response = requests.post(
        "http://BACKEND_URL/predict",
        json=payload
    )

    st.success(response.json())