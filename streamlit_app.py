import streamlit as st
import json

# -------------------------
# Page configuration
# -------------------------
st.set_page_config(layout="wide", page_title="Microland HR Portal")

# Load Custom CSS
with open("static/styles.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Load Users
with open("data/users.json") as f:
    USERS = json.load(f)

# -------------------------
# LOGIN SCREEN
# -------------------------
def login_screen():
    st.markdown(
        """
        <div style='text-align:center; margin-top:40px;'>
            <img src='static/logo.png' width='220'>
            <h2 style='margin-top:20px; color:#0057B7;'>Microland HR Portal</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    email = st.text_input("Email Address")
    pwd = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):
        if email in USERS and USERS[email]["password"] == pwd:
            st.session_state.logged_in = True
            st.session_state.user = USERS[email]
            st.experimental_rerun()
        else:
            st.error("Invalid email or password")


# -------------------------
# AUTH STATE CHECK
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# If NOT logged in → show login screen
if not st.session_state.logged_in:
    login_screen()

# If logged in → go to Dashboard
else:
    st.switch_page("pages/1_Dashboard.py")
