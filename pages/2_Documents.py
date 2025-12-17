import streamlit as st
from components.sidebar import load_sidebar
load_sidebar()
import json

sidebar()

st.title("My Documents")

with open("data/documents.json") as f:
    docs = json.load(f)

for doc in docs:
    st.markdown(f"**{doc['name']}** — {doc['category']} — {doc['uploaded_at']}  \n"
                f"[View File](static/{doc['name']})")
