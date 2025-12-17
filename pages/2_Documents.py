import streamlit as st
from streamlit_app import sidebar
import json

sidebar()

st.title("My Documents")

with open("data/documents.json") as f:
    docs = json.load(f)

for doc in docs:
    st.markdown(f"**{doc['name']}** — {doc['category']} — {doc['uploaded_at']}  \n"
                f"[View File](static/{doc['name']})")
