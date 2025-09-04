# app.py
import streamlit as st
from streamlit_app.components.sidebar import create_sidebar
from streamlit_app.pages.Home import home_page
from streamlit_app.pages.Upload import upload_page
from streamlit_app.pages.Chatbot import chatbot_page

# Page configuration
st.set_page_config(
    page_title="Jewelry AI Assistant", 
    page_icon="💎", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page routing mapping
PAGE_MAPPING = {
    "Home": home_page,
    "Upload": upload_page,
    "Chatbot": chatbot_page
}

def main():
    """Main application entry point"""
    # Create sidebar and get current page
    current_page = create_sidebar()
    
    # Execute the current page function
    page_function = PAGE_MAPPING.get(current_page)
    if page_function:
        page_function()
    else:
        # Fallback to home page if unknown page
        home_page()

if __name__ == "__main__":
    main()