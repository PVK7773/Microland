import streamlit as st
from components.sidebar import load_sidebar

load_sidebar()

st.title("Leave Applications")

leave_type = st.selectbox("Leave Type", ["Casual Leave", "Sick Leave", "Annual Leave"])
days = st.number_input("Number of Days", 1, 30)
reason = st.text_area("Reason for Leave")

if st.button("Submit Leave Request"):
    st.success("Your leave request has been submitted!")
