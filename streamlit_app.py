import streamlit as st

st.set_page_config(page_title="Microland HR Portal", layout="wide")
st.image("static/microland_logo_full.png", width=200)

st.title("Microland HR Portal")

menu = ["Home", "Employee Dashboard", "Admin Panel"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.header("Welcome to Microland HR Self-Service Portal")
    st.write("Access your documents, apply for leave, and more.")

elif choice == "Employee Dashboard":
    st.subheader("📄 Offer Letter")
    st.write("Preview and download your offer letter here.")

elif choice == "Admin Panel":
    st.subheader("Admin Access")
    st.write("Manage users, leave applications, and uploads.")