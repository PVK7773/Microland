
import streamlit as st
import os

st.set_page_config(page_title="Microland HR Portal", layout="wide")
st.image("static/microland_logo_full.png", width=200)

st.title("Welcome to Microland HR Portal")

menu = st.sidebar.selectbox("Navigate", ["Dashboard", "My Documents", "Apply Leave"])

if menu == "Dashboard":
    st.subheader("Employee Dashboard")
    st.markdown("**Employee Name:** Alister Dsouza")
    st.markdown("**Employee ID:** ICON2135")
    st.markdown("**Department:** IT")
elif menu == "My Documents":
    st.subheader("My Documents")
    doc_files = os.listdir("data")
    for file in doc_files:
        if file.endswith(".pdf"):
            with open(f"data/{file}", "rb") as f:
                st.download_button(label=f"Download {file}", data=f, file_name=file)
elif menu == "Apply Leave":
    st.subheader("Apply for Leave")
    with st.form("leave_form"):
        from_date = st.date_input("From Date")
        to_date = st.date_input("To Date")
        reason = st.text_area("Reason for Leave")
        submit = st.form_submit_button("Submit Request")
        if submit:
            st.success("Leave request submitted successfully!")
