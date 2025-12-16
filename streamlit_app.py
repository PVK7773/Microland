
import streamlit as st

st.set_page_config(page_title="Microland HR Portal", layout="centered")
st.image("static/microland_logo_full.png", width=200)

st.title("Welcome to Microland HR Portal")

menu = st.sidebar.selectbox("Menu", ["Login", "Admin Dashboard"])

if menu == "Login":
    emp_id = st.text_input("Employee ID")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if emp_id == "ICON2135" and password == "alister123":
            st.success("Login successful! Welcome Alister Dsouza.")
        else:
            st.error("Invalid credentials. Please try again.")

elif menu == "Admin Dashboard":
    st.subheader("Admin Panel")
    st.write("Track leaves, approve documents, manage users...")
