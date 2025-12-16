
import streamlit as st
import json
import os
from utils import login, show_dashboard, show_admin_dashboard

st.set_page_config(page_title="Microland HR Portal", layout="wide")

# Logo
st.image("static/microland_logo_full.png", width=200)

# Authentication
user_info = login()

if user_info:
    if user_info['role'] == "admin":
        show_admin_dashboard(user_info)
    else:
        show_dashboard(user_info)
