import streamlit as st
from streamlit_app import sidebar

sidebar()

user = st.session_state.get("user")

st.title("Welcome to the Microland HR Portal")
st.write(f"Hello, **{user['name']}** ({user['role']})")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='tile'><div class='tile-number'>2</div><div class='tile-label'>My Documents</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='tile'><div class='tile-number'>8</div><div class='tile-label'>Leave Balance</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='tile'><div class='tile-number'>1</div><div class='tile-label'>Leave Requests</div></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='tile'><div class='tile-number'>0</div><div class='tile-label'>Pending Approvals</div></div>", unsafe_allow_html=True)
