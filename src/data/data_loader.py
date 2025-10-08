"""
Data loading and preprocessing utilities for Steam dataset.
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_steam_data(path: Path) -> pd.DataFrame:
    """
    Load Steam dataset from CSV file in path.
    
    Returns:
        pd.DataFrame: Loaded Steam dataset
    """
    file_path = path
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded dataset with {len(df)} rows and {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return pd.DataFrame()
    

def quick_load_steam_data(path: Path) -> pd.DataFrame:
    """
    Load first five lines from path csv
    
    Returns:
        pd.DataFrame: with only the first five lines
    """

    file_path = path
    try:
        df = pd.read_csv(file_path,nrows=5)
        print(f"Successfully loaded dataset with {len(df)} rows and {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return pd.DataFrame()

def clean_steam_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess Steam dataset.
    
    Args:
        df (pd.DataFrame): Raw Steam dataset
        
    Returns:
        pd.DataFrame: Cleaned dataset
    """
    # Create a copy to avoid modifying original data
    df_clean = df.copy()
    
    # Remove duplicates
    df_clean = df_clean.drop_duplicates()
    
    # Handle missing values
    # (Add specific logic based on the actual dataset structure)
    
    print(f"Data cleaned: {len(df_clean)} rows remaining after preprocessing")
    return df_clean

def save_processed_data(df: pd.DataFrame, file_path: str) -> None:
    """
    Save processed data to CSV file.
    
    Args:
        df (pd.DataFrame): Processed dataset
        file_path (str): Output file path
    """
    try:
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data: {str(e)}")
