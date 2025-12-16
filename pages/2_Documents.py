import streamlit as st
import pandas as pd

st.title("My Documents")

docs = pd.DataFrame({
    "File Name": ["November_2025.pdf", "Offer_Letter.pdf"],
    "Category": ["Payslip", "Offer Letter"],
    "Uploaded By": ["alister.dsouza@microland.com", "alister.dsouza@microland.com"],
    "Uploaded At": ["24-Apr-2024 03:04 PM", "24-Apr-2024 03:04 PM"]
})

st.table(docs)

st.markdown("### Upload Files")
file = st.file_uploader("Upload Document", type=["pdf"])

if file:
    st.success("Uploaded successfully!")
