
import streamlit as st

st.set_page_config(page_title="Microland HR Portal", layout="centered")

st.image("static/microland_logo_full.png", width=200)
st.title("Welcome to the Microland HR Portal")
st.subheader("Login to continue")

username = st.text_input("Email")
emp_id = st.text_input("Employee ID")
if st.button("Login"):
    if username == "alister.dsouza@microland.com" and emp_id == "ICON2135":
        st.success("Logged in successfully as Alister Dsouza")
        st.write("### My Documents")
        st.write("- [Offer Letter](uploads/Offer_Letter.pdf)")
        st.write("- [Salary Slip - November 2025](uploads/November_2025.pdf)")
        st.write("### Apply for Leave")
        st.text_area("Reason for Leave")
        st.date_input("Leave Start Date")
        st.date_input("Leave End Date")
        st.button("Submit Leave Request")
    else:
        st.error("Invalid credentials")
