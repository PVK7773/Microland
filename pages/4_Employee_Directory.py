import streamlit as st
import pandas as pd

st.title("Employee Directory")

df = pd.DataFrame({
    "Name":["Alister Dsouza","John Paul","Sanjay Kumar"],
    "Role":["Manager","Engineer","Finance"],
    "Email":["alister.dsouza@microland.com","john@microland.com","sanjay@microland.com"]
})

st.dataframe(df)
