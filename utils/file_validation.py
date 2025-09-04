# file_validation.py
import pandas as pd
from configs.constants import REQUIRED_COLUMNS

def validate_excel_columns(uploaded_df):
    """Validate the uploaded Excel file has exactly the required columns"""
    uploaded_columns = set(uploaded_df.columns.str.strip().str.lower())
    required_columns_lower = set(col.lower() for col in REQUIRED_COLUMNS)
    
    missing_columns = required_columns_lower - uploaded_columns
    missing_columns_original = [col for col in REQUIRED_COLUMNS 
                               if col.lower() in missing_columns]
    
    extra_columns = uploaded_columns - required_columns_lower
    extra_columns_original = [col for col in uploaded_df.columns 
                             if col.strip().lower() in extra_columns]
    
    return missing_columns_original, extra_columns_original

def validate_file_size(uploaded_file, max_size_mb=10):
    """Validate file size doesn't exceed limit"""
    return uploaded_file.size <= max_size_mb * 1024 * 1024

def is_valid_excel_file(filename):
    """Check if file has valid Excel extension"""
    return any(filename.lower().endswith(ext) for ext in ['.xlsx', '.xls'])