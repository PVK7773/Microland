
import streamlit as st
import json

def login():
    with open("data/users.json") as f:
        users = json.load(f)

    st.sidebar.title("Login")
    username = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    login_btn = st.sidebar.button("Login")

    if login_btn:
        for user in users:
            if user["email"] == username and user["password"] == password:
                st.success(f"Welcome {user['name']}")
                return user
        st.error("Invalid credentials")
    return None

def show_dashboard(user_info):
    st.title("Employee Dashboard")
    st.subheader(f"Welcome, {user_info['name']}")
    st.write("📄 My Documents")
    st.write("📝 Leave Application")

def show_admin_dashboard(user_info):
    st.title("Admin Dashboard")
    st.write("📊 View all leave requests")
    st.write("📁 Manage employee documents")
