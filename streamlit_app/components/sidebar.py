# sidebar.py
import streamlit as st

def create_sidebar():
    """Create and return the sidebar navigation"""
    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    st.sidebar.title("🧭 Navigation")
    st.sidebar.write("---")

    # Navigation buttons
    pages = {
        "🏠 Home": "Home",
        "📁 Upload": "Upload", 
        "🤖 Chatbot": "Chatbot"
    }
    
    for icon_name, page_name in pages.items():
        if st.sidebar.button(icon_name, use_container_width=True, key=page_name):
            st.session_state.page = page_name

    st.sidebar.write("---")
    st.sidebar.info(f"📍 Current Page: {st.session_state.page}")
    
    return st.session_state.page