
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Microland HR Portal", layout="wide")

# Branding
st.image("static/microland_logo.png", width=160)
st.markdown("<h2 style='color: black;'>Microland HR Portal</h2>", unsafe_allow_html=True)
st.markdown("---")

# Login simulation
def login():
    st.sidebar.header("Employee Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if email == "alister.dsouza@microland.com" and password == "microland123":
            st.session_state.logged_in = True
        else:
            st.sidebar.error("Invalid credentials")

# Display dashboard
def dashboard():
    st.success("✅ Logged in as Alister Dsouza")
    st.markdown("### 📁 HR Documents")
    st.markdown("- [📄 Offer Letter](static/Offer Letter.pdf)")
    st.markdown("- [🗓️ November 2025 Report](static/November 2025.pdf)")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    dashboard()
