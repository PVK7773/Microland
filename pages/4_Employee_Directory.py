import streamlit as st
import pandas as pd
from components.sidebar import load_sidebar

load_sidebar()

st.title("Employee Directory")

df = pd.DataFrame({
    "Name": ["Alister Noel Dsouza", "John Peter", "Rohit Kumar"],
    "Email": [
        "alister.dsouza@microland.com",
        "john.peter@microland.com",
        "rohit.kumar@microland.com"
    ],
    "Department": ["IT", "Operations", "Finance"]
})

st.dataframe(df, use_container_width=True)
