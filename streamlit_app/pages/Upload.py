# Upload.py
import streamlit as st
import pandas as pd

from configs.constants import REQUIRED_COLUMNS, ALLOWED_FILE_TYPES
from utils.file_validation import validate_excel_columns, validate_file_size, is_valid_excel_file
from utils.display_helper import (
    display_file_info, show_validation_results, show_data_preview,
    show_column_comparison, show_database_button, show_upload_instructions,
    show_error_message
)

def upload_page():
    """Main upload page function"""
    st.title("📤 Upload Jewelry Inventory")
    
    # File upload section
    uploaded_file = st.file_uploader(
        "**Upload Excel File with Jewelry Inventory**",
        type=ALLOWED_FILE_TYPES,
        help=f"Please upload an Excel file with {len(REQUIRED_COLUMNS)} required columns"
    )
    
    if uploaded_file is not None:
        process_uploaded_file(uploaded_file)
    else:
        show_upload_instructions()

def process_uploaded_file(uploaded_file):
    """
    Process and validate the uploaded Excel file
    """
    try:
        # Validate file type
        if not is_valid_excel_file(uploaded_file.name):
            st.error("❌ Invalid file type. Please upload an Excel file (.xlsx or .xls)")
            return
        
        # Validate file size
        if not validate_file_size(uploaded_file):
            st.error(f"❌ File too large. Maximum size is 10MB")
            return
        
        # Read and process the Excel file
        df = pd.read_excel(uploaded_file)
        
        # Display file information
        display_file_info(uploaded_file, df)
        
        # Validate columns
        missing_cols, extra_cols = validate_excel_columns(df)
        
        # Show validation results
        validation_passed = show_validation_results(missing_cols, extra_cols)
        
        # Show data preview and comparison
        show_data_preview(df)
        show_column_comparison(df)
        
        # Show database button based on validation
        show_database_button(validation_passed)
        
    except Exception as e:
        show_error_message(e)

