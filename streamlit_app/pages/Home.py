import streamlit as st

def home_page():
    """Home page content for Jewelry Store AI System"""
    st.title("💎 Jewelry Store AI Assistant")
    st.write("---")
    
    # Welcome message
    st.markdown("### Welcome to your intelligent inventory management system!")
    st.write("Designed specifically for jewelry store staff and sales teams.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("🏪 About This System")
        st.write("""
        This AI-powered system helps jewelry store staff manage and query inventory efficiently:
        
        **📊 Excel Upload & Database Integration**
        - Upload supplier invoices (Excel files)
        - Automatic mapping to SQL database
        - Organized inventory management
        
        **🤖 Smart Inventory Assistant**
        - Ask questions about specific items
        - Search by item codes (e.g., "EL-1239")
        - Query by specifications and budget
        - Get detailed product information instantly
        """)
        
        st.info("💡 Perfect for sales teams to quickly find products and answer customer questions!")
    
    with col2:
        st.header("🚀 Quick Start Guide")
        st.write("**For Sales Staff & Store Management:**")
        
        # Upload section
        st.markdown("**1. Upload Supplier Data**")
        if st.button("📁 Upload Excel Files", use_container_width=True, type="primary"):
            st.session_state.page = "Upload"
            st.rerun()
        st.caption("Upload supplier invoices to update inventory database")
        
        st.write("")  # Space
        
        # Chatbot section  
        st.markdown("**2. Ask Inventory Questions**")
        if st.button("🤖 Ask AI Assistant", use_container_width=True, type="secondary"):
            st.session_state.page = "Chatbot"
            st.rerun()
        st.caption("Query inventory: 'Do we have men's rings under $5k with ruby?'")
    
    # Example queries section
    st.write("---")
    st.header("💬 Example Questions You Can Ask")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🔍 Item Details**
        - "Tell me about item EL-1239"
        - "Show specs for SKU AB-456"
        - "What's the price of item XYZ-789?"
        """)
    
    with col2:
        st.markdown("""
        **💰 Budget Searches**
        - "Men's rings under $5,000"
        - "Diamond earrings $1k-$3k range"
        - "Affordable wedding bands"
        """)
    
    with col3:
        st.markdown("""
        **💎 Gem & Style Queries**
        - "Ruby rings in stock"
        - "Gold necklaces available"
        - "Vintage style bracelets"
        """)
    
    # Stats or additional info
    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("System Status", "Online", delta="Active")
    
    with col2:
        st.metric("Database", "Connected", delta="Ready")
    
    with col3:
        st.metric("AI Assistant", "Ready", delta="Available")
    
    with col4:
        st.metric("File Uploads", "Enabled", delta="Working")