
import streamlit as st

st.title("🗓️ Leave Application")
st.date_input("Select Leave Dates")
st.text_area("Reason for Leave")
if st.button("Submit Leave Request"):
    st.success("Leave request submitted!")
