# Configuration file for Steam Stats EDA Dashboard
# Copy this file to config.py and modify as needed

# Data paths
DATA_PATHS = {
    'raw_data': '../data/raw/',
    'processed_data': '../data/processed/',
    'external_data': '../data/external/'
}

# Dataset information
DATASET_CONFIG = {
    'steam_dataset': {
        'filename': 'steam_dataset.csv',  # Replace with actual filename
        'url': 'https://www.kaggle.com/datasets/...',  # Add Kaggle dataset URL
        'description': 'Steam game statistics dataset from Kaggle'
    }
}

# Visualization settings
PLOT_CONFIG = {
    'style': 'seaborn-v0_8',
    'palette': 'husl',
    'figure_size': (12, 8),
    'dpi': 300
}

# Dashboard settings
DASHBOARD_CONFIG = {
    'title': 'Steam Stats Dashboard',
    'icon': '🎮',
    'layout': 'wide',
    'sidebar_state': 'expanded'
}

# API keys and external services (if needed)
API_KEYS = {
    'steam_api_key': None,  # Add your Steam API key if using Steam API
    'kaggle_username': None,  # Add your Kaggle username
    'kaggle_key': None  # Add your Kaggle API key
}