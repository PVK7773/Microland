import streamlit as st

def main():
    st.set_page_config(page_title="Microland HR Portal", layout="wide", page_icon=":office:")
    st.markdown("<style>footer {visibility: hidden;} .css-1d391kg {visibility: hidden;} .css-hxt7ib {background-color: white;} .stApp {background-color: white;}</style>", unsafe_allow_html=True)
    st.title("Welcome to the Microland HR Portal")

if __name__ == "__main__":
    main()
