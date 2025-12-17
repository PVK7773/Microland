import streamlit as st

def load_sidebar():
    st.sidebar.markdown("<h2 style='color:#0057B7;'>Microland HR</h2>", unsafe_allow_html=True)

    pages = {
        "📊 Dashboard": "1_Dashboard.py",
        "📁 Documents": "2_Documents.py",
        "📝 Leave Applications": "3_Leave_Applications.py",
        "👥 Employee Directory": "4_Employee_Directory.py",
        "📢 HR Announcements": "5_HR_Announcements.py",
        "🚪 Logout": "LOGOUT"
    }

    choice = st.sidebar.radio("Navigation", list(pages.keys()))

    if choice == "🚪 Logout":
        st.session_state.logged_in = False
        st.experimental_rerun()
    elif choice != "📊 Dashboard":
        st.switch_page("pages/" + pages[choice])
