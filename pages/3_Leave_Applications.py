import streamlit as st
from streamlit_app import sidebar

sidebar()

st.title("Leave Applications")

leave_type = st.selectbox("Leave Type", ["Casual", "Sick", "Annual"])
days = st.number_input("Days", 1, 30)
reason = st.text_area("Reason")

if st.button("Submit Leave Request"):
    st.success("Leave request submitted!")
