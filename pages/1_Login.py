
import streamlit as st

st.title("🔐 Login to HR Portal")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if username == "alister" and password == "microland123":
        st.success("Login successful!")
        st.session_state["logged_in"] = True
    else:
        st.error("Invalid credentials")
