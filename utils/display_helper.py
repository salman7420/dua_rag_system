# display_helpers.py
import streamlit as st
import pandas as pd
from configs.constants import REQUIRED_COLUMNS

def display_file_info(uploaded_file, df):
    """Display file information and validation results"""
    st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")
    
    # File metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("File Size", f"{uploaded_file.size / 1024:.1f} KB")
    with col2:
        st.metric("Total Rows", df.shape[0])
    with col3:
        st.metric("Total Columns", df.shape[1])
    with col4:
        st.metric("Required Columns", len(REQUIRED_COLUMNS))
    
    return col1, col2, col3, col4

def show_validation_results(missing_cols, extra_cols):
    """Display validation results to user"""
    st.subheader("🔍 Validation Results")
    
    if not missing_cols and not extra_cols:
        st.success("✅ Perfect! All required columns are present with no extra columns.")
        return True
    else:
        validation_passed = False
        
        if missing_cols:
            st.error(f"❌ Missing {len(missing_cols)} required columns:")
            for col in missing_cols:
                st.write(f"   - **{col}**")
            validation_passed = False
        
        if extra_cols:
            st.warning(f"⚠️ Found {len(extra_cols)} extra columns that shouldn't be in the file:")
            for col in extra_cols:
                st.write(f"   - **{col}**")
            validation_passed = False
            
        return validation_passed

def show_data_preview(df):
    """Display data preview"""
    st.subheader("📊 Data Preview")
    st.dataframe(df.head(), use_container_width=True)

def show_column_comparison(df):
    """Display column comparison table"""
    st.subheader("📋 Column Comparison")
    col_comparison = pd.DataFrame({
        'Required Columns': REQUIRED_COLUMNS,
        'Present in File': [col in df.columns.str.strip().str.lower() 
                          for col in [c.lower() for c in REQUIRED_COLUMNS]]
    })
    st.dataframe(col_comparison, use_container_width=True)

def show_database_button(validation_passed):
    """Show database mapping button based on validation"""
    if validation_passed:
        if st.button("🗂️ Map to Database", type="primary", use_container_width=True):
            st.info("🚀 Database mapping feature coming soon!")
            st.write("This will store your data in SQL database and generate vector embeddings.")
    else:
        st.button("🗂️ Map to Database", disabled=True, help="Fix column issues first")

def show_upload_instructions():
    """Show instructions when no file is uploaded"""
    st.info("👆 Please upload an Excel file to get started")
    
    # Display required columns
    st.subheader("📋 Required Columns")
    st.write("Your Excel file must contain exactly these 16 columns:")
    
    cols_per_row = 4
    required_cols = REQUIRED_COLUMNS.copy()
    
    for i in range(0, len(required_cols), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            if i + j < len(required_cols):
                with col:
                    st.markdown(f"**{i + j + 1}.** {required_cols[i + j]}")
                    st.caption("Required column")

def show_error_message(error):
    """Display error message"""
    st.error(f"❌ Error reading file: {str(error)}")
    st.info("Please make sure you're uploading a valid Excel file (.xlsx or .xls)")