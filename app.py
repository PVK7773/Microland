import streamlit as st
from PIL import Image

st.set_page_config(page_title="Microland HR Portal", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Dummy Login for Alister
if not st.session_state.logged_in:
    st.image("static/microland_logo_full.png", width=220)
    st.title("Microland HR Portal Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email == "alister.dsouza@microland.com" and password == "welcome123":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials.")
else:
    st.sidebar.image("static/microland_logo_icon.png", width=100)
    st.sidebar.title("Microland HR Portal")
    selection = st.sidebar.radio("Go to", ["Dashboard", "My Documents", "Leave Application", "Announcements"])

    if selection == "Dashboard":
        st.title("🏠 Employee Dashboard")
        st.markdown("### Welcome, Alister Noel Dsouza")
        st.markdown("**Employee ID:** ICON2135")
        st.markdown("**Designation:** Major Incident Manager")
        st.markdown("**Location:** Bengaluru")
        st.success("You are successfully logged in.")

    elif selection == "My Documents":
        st.title("📄 My Documents")
        st.markdown("Access and download your official HR documents below:")
        with open("docs/Offer_Letter_Alister.pdf", "rb") as f:
            st.download_button("Download Offer Letter", f, file_name="Offer_Letter.pdf")
        with open("docs/Payslip_November_2025.pdf", "rb") as f:
            st.download_button("Download November 2025 Payslip", f, file_name="Payslip_November_2025.pdf")

    elif selection == "Leave Application":
        st.title("📝 Leave Application")
        with st.form("leave_form"):
            leave_type = st.selectbox("Leave Type", ["Casual Leave", "Sick Leave", "Earned Leave"])
            from_date = st.date_input("From Date")
            to_date = st.date_input("To Date")
            reason = st.text_area("Reason")
            submitted = st.form_submit_button("Submit Leave Request")
        if submitted:
            st.success("Leave request submitted successfully!")

    elif selection == "Announcements":
        st.title("📢 Announcements")
        st.info("🎯 FY25 review cycle ends Dec 31.")
        st.info("📆 Leave balances reset on July 1st.")
        st.success("🚀 Workday-style portal live for Alister!")
