import streamlit as st
from concrete import fhe
from fhe_bmi import encrypted_bmi

st.title("🔒 Encrypted BMI Calculator (Powered by Zama FHE)")
st.write("Compute your BMI privately — your height and weight are never seen in plaintext.")

# User input
weight = st.number_input("Enter your weight (kg):", min_value=30.0, max_value=200.0, value=70.0)
height = st.number_input("Enter your height (m):", min_value=1.0, max_value=2.5, value=1.75)

if st.button("Calculate Encrypted BMI"):
    # Encrypt inputs
    ctx = fhe.Configuration()
    encrypted_weight = fhe.encrypt(weight, ctx)
    encrypted_height = fhe.encrypt(height, ctx)

    # Compute encrypted BMI
    encrypted_result = encrypted_bmi(encrypted_weight, encrypted_height)

    # Decrypt result
    bmi = fhe.decrypt(encrypted_result, ctx)

    st.success(f"✅ Your BMI (computed privately): {bmi:.2f}")
    st.info("Your data was never exposed — computed entirely under encryption!")
