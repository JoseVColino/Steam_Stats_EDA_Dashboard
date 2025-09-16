# Project Structure

This document explains the folder structure and purpose of each component in the Steam Stats EDA Dashboard project.

## 📁 Directory Structure

```
Steam_Stats_EDA_Dashboard/
├── README.md                          # Project overview and setup instructions
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore file for Python projects
│
├── data/                             # Data directory
│   ├── raw/                          # Raw, immutable data from Kaggle
│   │   ├── .gitkeep                  # Keep directory in git
│   │   └── steam_dataset.csv         # Original Steam dataset (to be added)
│   ├── processed/                    # Cleaned and processed data
│   │   ├── .gitkeep                  # Keep directory in git
│   │   └── steam_clean.csv           # Processed Steam dataset
│   └── external/                     # External data sources
│       └── .gitkeep                  # Keep directory in git
│
├── notebooks/                        # Jupyter notebooks for analysis
│   └── 01_steam_eda.ipynb           # Main EDA notebook
│
├── src/                              # Source code modules
│   ├── __init__.py                   # Python package initialization
│   ├── data/                         # Data loading and processing
│   │   ├── __init__.py
│   │   └── data_loader.py            # Data loading utilities
│   ├── features/                     # Feature engineering
│   │   └── __init__.py
│   ├── models/                       # Statistical models (if needed)
│   │   └── __init__.py
│   └── visualization/                # Plotting utilities
│       ├── __init__.py
│       └── plots.py                  # Visualization functions
│
├── dashboards/                       # Dashboard applications
│   └── streamlit_app.py             # Streamlit dashboard
│
├── config/                           # Configuration files
│   └── config_template.py           # Configuration template
│
├── tests/                            # Unit tests
│   └── test_data_loader.py          # Tests for data loading
│
└── docs/                             # Documentation
    └── project_structure.md         # This file
```

## 🎯 Component Purposes

### `/data/`
- **`raw/`**: Store original, immutable datasets downloaded from Kaggle
- **`processed/`**: Store cleaned and processed datasets ready for analysis
- **`external/`**: Store any external data sources or supplementary datasets

### `/notebooks/`
- Contains Jupyter notebooks for exploratory data analysis
- Start with `01_steam_eda.ipynb` for initial data exploration
- Add numbered notebooks for different analysis phases

### `/src/`
- **`data/`**: Modules for data loading, cleaning, and preprocessing
- **`features/`**: Feature engineering and transformation functions
- **`models/`**: Statistical models or machine learning models (if applicable)
- **`visualization/`**: Reusable plotting and visualization functions

### `/dashboards/`
- Interactive dashboard applications
- `streamlit_app.py`: Main Streamlit dashboard for data visualization

### `/config/`
- Configuration files for project settings
- Database connections, API keys, file paths, etc.

### `/tests/`
- Unit tests for validating code functionality
- Run with `pytest` to ensure code quality

### `/docs/`
- Project documentation and guides
- API documentation, user guides, etc.

## 🚀 Getting Started

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Add Your Dataset**:
   - Download Steam dataset from Kaggle
   - Place in `data/raw/` directory
   - Update filename in configuration

3. **Run EDA**:
   ```bash
   jupyter notebook notebooks/01_steam_eda.ipynb
   ```

4. **Launch Dashboard**:
   ```bash
   streamlit run dashboards/streamlit_app.py
   ```

5. **Run Tests**:
   ```bash
   pytest tests/
   ```

## 📝 Best Practices

- Keep raw data immutable in `data/raw/`
- Save processed data in `data/processed/`
- Use version control for code, not large data files
- Document your analysis in notebooks
- Write reusable functions in `src/` modules
- Add tests for critical functionality
- Update this documentation as the project evolves