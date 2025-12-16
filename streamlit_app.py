import streamlit as st
import json
from pathlib import Path

# Load CSS
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load users
with open("data/users.json") as f:
    USERS = json.load(f)

st.set_page_config(layout="wide")

def login():
    st.image("static/logo.png", width=180)
    st.markdown("### Login to Microland HR Portal")
    
    email = st.text_input("Email")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if email in USERS and USERS[email]["password"] == pwd:
            st.session_state.logged_in = True
            st.session_state.user = USERS[email]
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    st.switch_page("pages/1_Dashboard.py")
