import streamlit as st
import json

st.set_page_config(page_title="Microland HR Portal", layout="wide")

# Load CSS
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

    email = st.text_input("Email Address")
    pwd = st.text_input("Password", type="password")

    login_button = st.button("Login", use_container_width=True)

    if login_button:
        if email in USERS and USERS[email]["password"] == pwd:
            st.session_state["logged_in"] = True
            st.session_state["user"] = USERS[email]
        else:
            st.error("Invalid email or password")


# -------------------------
# INITIAL SESSION STATE
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


# -------------------------
# PAGE ROUTING (NO RERUN)
# -------------------------
if not st.session_state["logged_in"]:
    # Show login page
    login_screen()

else:
    # Go to dashboard (safe redirect)
    st.switch_page("pages/1_Dashboard.py")
