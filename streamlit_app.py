import streamlit as st
import json
import os
import base64
from router import load_page


# ------------------------------------------------------------
# REMOVE STREAMLIT DEFAULT PADDING + MENU
# ------------------------------------------------------------
st.set_page_config(page_title="Microland HR Portal", layout="wide")

hide_streamlit = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit, unsafe_allow_html=True)


# ------------------------------------------------------------
# LOAD USERS
# ------------------------------------------------------------
def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)


# ------------------------------------------------------------
# AUTHENTICATION
# ------------------------------------------------------------
def login_screen():
    st.markdown("<h1 style='text-align:center; color:#0A2342;'>Microland HR Portal</h1>", unsafe_allow_html=True)

    # Load login page HTML
    login_html = load_page("login")

    st.components.v1.html(login_html, height=650, scrolling=False)

    # Get login input from query params
    email = st.query_params.get("email", [""])[0]
    password = st.query_params.get("password", [""])[0]

    if email and password:
        users = load_users()

        if email in users and users[email]["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = email
            st.experimental_set_query_params()
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")


# ------------------------------------------------------------
# RENDER MAIN APP LAYOUT
# ------------------------------------------------------------
def render_app():
    user = st.session_state["user"]

    # LOAD BASE TEMPLATE
    base_html = load_page("base")

    # Inject page content dynamically
    current_page = st.session_state.get("current_page", "dashboard")
    page_html = load_page(current_page)

    full_html = base_html.replace("{{PAGE_CONTENT}}", page_html)

    st.components.v1.html(full_html, height=2000, scrolling=True)


# ------------------------------------------------------------
# PAGE NAVIGATION HANDLER
# ------------------------------------------------------------
def navigate(page):
    st.session_state["current_page"] = page
    st.experimental_rerun()


# ------------------------------------------------------------
# SIDEBAR NAVIGATION ACTIONS
# ------------------------------------------------------------
nav = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "My Documents", "Leave Request", "Directory", "Announcements", "Logout"],
    label_visibility="collapsed"
)

if nav == "Dashboard":
    st.session_state["current_page"] = "dashboard"
elif nav == "My Documents":
    st.session_state["current_page"] = "documents"
elif nav == "Leave Request":
    st.session_state["current_page"] = "leaves"
elif nav == "Directory":
    st.session_state["current_page"] = "directory"
elif nav == "Announcements":
    st.session_state["current_page"] = "announcements"
elif nav == "Logout":
    st.session_state.clear()
    st.experimental_rerun()


# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------
if "logged_in" not in st.session_state:
    login_screen()
else:
    render_app()
