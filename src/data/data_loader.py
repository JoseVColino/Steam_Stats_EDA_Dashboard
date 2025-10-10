"""
Data loading and preprocessing utilities for Steam dataset.
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_steam_data(file_path: str) -> pd.DataFrame:
    """
    Load Steam dataset from CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded Steam dataset
    """
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
    
def quick_load_steam_data(file_path: str) -> pd.DataFrame:
    """
    Load 5 lines from Steam dataset at CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded Steam dataset
    """
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


def clean_steam_data(df: pd.DataFrame):
    df['genres'] = df['genres'].str.strip("[]").str.replace("'", "").str.split(", ")
    df['release_date'] = pd.to_datetime(df['release_date'],format="%Y-%m-%d").apply(lambda x:x.date())
    df = df.drop_duplicates(subset='name', keep='last')

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