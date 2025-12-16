import streamlit as st

st.title("Leave Applications")

leave_type = st.selectbox("Leave Type", ["Casual Leave","Sick Leave","Annual Leave"])
days = st.number_input("Days", 1, 30)
reason = st.text_area("Reason")

if st.button("Apply Leave"):
    st.success("Leave request submitted!")
