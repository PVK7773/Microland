import streamlit as st
from streamlit_app import sidebar
import pandas as pd

sidebar()

st.title("Employee Directory")

df = pd.DataFrame({
    "Name": ["Alister Noel Dsouza", "John Peter", "Rohit Kumar"],
    "Email": ["alister.dsouza@microland.com", "john.p@microland.com", "rohit@microland.com"],
    "Department": ["IT", "Operations", "Finance"]
})

st.dataframe(df)
