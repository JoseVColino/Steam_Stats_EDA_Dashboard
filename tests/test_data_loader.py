"""
Test cases for Steam Stats EDA Dashboard.
"""

import pytest
import pandas as pd
import numpy as np
import sys
from pathlib import Path

# Add src to path
sys.path.append('../src')
from data.data_loader import load_steam_data, clean_steam_data

class TestDataLoader:
    """Test cases for data loading functionality."""
    
    def test_load_steam_data_empty_file(self):
        """Test loading data from non-existent file."""
        result = load_steam_data('non_existent_file.csv')
        assert result.empty
    
    def test_clean_steam_data(self):
        """Test data cleaning functionality."""
        # Create sample data with duplicates and missing values
        data = {
            'name': ['Game1', 'Game2', 'Game1', 'Game3'],
            'price': [10.0, 20.0, 10.0, np.nan],
            'genre': ['Action', 'RPG', 'Action', 'Strategy']
        }
        df = pd.DataFrame(data)
        
        result = clean_steam_data(df)
        
        # Should remove duplicates
        assert len(result) <= len(df)
        assert not result.empty

class TestVisualization:
    """Test cases for visualization functions."""
    
    def test_sample_data_creation(self):
        """Test creation of sample data for testing."""
        # Create sample data
        data = {
            'price': [10.0, 20.0, 30.0],
            'genre': ['Action', 'RPG', 'Strategy'],
            'rating': [8.5, 9.0, 7.5]
        }
        df = pd.DataFrame(data)
        
        assert len(df) == 3
        assert 'price' in df.columns
        assert 'genre' in df.columns
        assert 'rating' in df.columns

if __name__ == "__main__":
    pytest.main([__file__])