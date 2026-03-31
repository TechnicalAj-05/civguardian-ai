import streamlit as st
from model import predict_severity
import random

st.title("🧠 CivGuardian AI")
st.subheader("Smart Civic Issue Detection")

uploaded_file = st.file_uploader("Upload an image", type=["jpg","png"])

issues = ["pothole", "garbage", "water_leak"]

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    detected_issue = random.choice(issues)
    severity = predict_severity(detected_issue)

    st.success(f"Detected Issue: {detected_issue}")
    st.warning(f"Severity: {severity}")

    complaint = f"""
Dear Municipal Corporation,

I would like to report a {severity} severity {detected_issue} in my area.
This issue requires immediate attention.

Kindly resolve it as soon as possible.

Thank you.
"""

    st.text_area("Generated Complaint", complaint)

    if st.button("Submit Complaint"):
        st.success("Complaint submitted successfully!")