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

    login_clicked = st.button("Login", use_container_width=True)

    if login_clicked:
        if email in USERS and USERS[email]["password"] == pwd:
            st.session_state.logged_in = True
            st.session_state.user = USERS[email]
            return True   # Rerun handled outside
        else:
            st.error("Invalid email or password")
            return False

    return False


# -------------------------
# INITIAL STATE
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# -------------------------
# LOGIN FLOW CONTROL
# -------------------------
if not st.session_state.logged_in:
    success = login_screen()
    if success:
        st.experimental_rerun()

else:
    st.switch_page("pages/1_Dashboard.py")
