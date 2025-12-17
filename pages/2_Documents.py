import streamlit as st
from components.sidebar import load_sidebar
import json

load_sidebar()

st.title("My Documents")

# Load documents
with open("data/documents.json") as f:
    docs = json.load(f)

for doc in docs:
    st.markdown(f"""
        **📄 {doc['name']}**  
        *Category:* {doc['category']}  
        *Uploaded:* {doc['uploaded_at']}  
        [🔗 View File](static/{doc['name']})
        ---
    """)
