import streamlit as st

def chatbot_page():
    """Chatbot page content"""
    st.title("🤖 Chatbot Page")
    st.write("---")
    
    st.header("AI Chatbot")
    st.write("This page will contain the chatbot functionality. Coming soon!")
    
    # Placeholder for chatbot functionality
    user_input = st.text_input("Type your message here:")
    
    if st.button("Send Message"):
        if user_input:
            st.write(f"**You**: {user_input}")
            st.write("**Bot**: This is a placeholder response. Real chatbot functionality coming soon!")
        else:
            st.warning("Please enter a message first!")