import streamlit as st
from components.sidebar import load_sidebar

load_sidebar()

st.title("HR Announcements")

st.success("🎉 Annual appraisal cycle will begin next month.")
st.info("📢 Microland Townhall scheduled for Friday at 4 PM.")
st.warning("⚠️ Please update your personal information in the HR portal.")
