import streamlit as st

st.set_page_config(page_title="Microland HR Portal", layout="centered")

st.image("static/microland_logo_full.png", width=200)

st.title("Welcome to MICROLAND HR Portal")
st.subheader("Login to access your documents and apply for leave")

# Simulated login logic
username = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "alister.dsouza@microland.com" and password == "microland@123":
        st.success("Welcome Alister Dsouza!")
        st.markdown("### Your Documents")
        st.write("📄 Offer Letter
📄 Payslip - November 2025")
        st.markdown("### Leave Application")
        st.write("📝 Apply leave and track status here.")
    else:
        st.error("Invalid credentials")
