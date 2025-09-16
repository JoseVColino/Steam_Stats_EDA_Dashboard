# 🎮 Steam Stats EDA Dashboard

College project to practice data analysis and dashboard creation using Steam game statistics from Kaggle.

## 📋 Project Overview

This project provides a comprehensive exploratory data analysis (EDA) and interactive dashboard for Steam game statistics. It includes data processing pipelines, visualization tools, and an interactive Streamlit dashboard for exploring gaming trends, pricing patterns, and genre popularity.

## 🏗️ Project Structure

```
Steam_Stats_EDA_Dashboard/
├── data/                     # Data storage
│   ├── raw/                  # Original datasets from Kaggle
│   ├── processed/            # Cleaned datasets
│   └── external/             # External data sources
├── notebooks/                # Jupyter notebooks for EDA
├── src/                      # Source code modules
│   ├── data/                 # Data loading and processing
│   ├── features/             # Feature engineering
│   ├── models/               # Statistical models
│   └── visualization/        # Plotting utilities
├── dashboards/               # Interactive dashboards
├── config/                   # Configuration files
├── tests/                    # Unit tests
└── docs/                     # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JoseVColino/Steam_Stats_EDA_Dashboard.git
   cd Steam_Stats_EDA_Dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Steam dataset**:
   - Download a Steam dataset from Kaggle (e.g., Steam games dataset)
   - Place the CSV file in `data/raw/`
   - Update the filename in `config/config_template.py`

### Usage

#### 📊 Exploratory Data Analysis
Run the Jupyter notebook for detailed analysis:
```bash
jupyter notebook notebooks/01_steam_eda.ipynb
```

#### 🎯 Interactive Dashboard
Launch the Streamlit dashboard:
```bash
streamlit run dashboards/streamlit_app.py
```

#### 🧪 Run Tests
Execute unit tests:
```bash
pytest tests/
```

## 📈 Features

### Data Analysis
- **Data Loading**: Robust CSV loading with error handling
- **Data Cleaning**: Remove duplicates, handle missing values
- **Statistical Analysis**: Descriptive statistics and distributions
- **Trend Analysis**: Time-based patterns and correlations

### Visualizations
- **Price Distribution**: Histogram and box plots of game prices
- **Genre Analysis**: Popularity and distribution of game genres
- **Interactive Plots**: Plotly-based interactive visualizations
- **Time Trends**: Release patterns over time

### Dashboard
- **Multi-page Interface**: Organized sections for different analyses
- **Interactive Filters**: Dynamic data filtering and exploration
- **Real-time Updates**: Responsive visualizations
- **Search Functionality**: Find specific games and details

## 📊 Recommended Datasets

Consider using these Kaggle datasets:
- [Steam Store Games (Clean dataset)](https://www.kaggle.com/datasets/nikdavis/steam-store-games)
- [Steam Games Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset)
- [Steam Video Games](https://www.kaggle.com/datasets/tamber/steam-video-games)

## 🛠️ Development

### Code Structure
- `src/data/`: Data loading and preprocessing utilities
- `src/visualization/`: Reusable plotting functions
- `dashboards/`: Interactive dashboard applications
- `notebooks/`: Analysis notebooks and experiments

### Adding New Features
1. Create new modules in appropriate `src/` subdirectories
2. Add corresponding tests in `tests/`
3. Update documentation in `docs/`
4. Follow the existing code style and structure

## 📝 Documentation

- [Project Structure](docs/project_structure.md): Detailed explanation of directories and files
- [API Documentation]: Auto-generated from code docstrings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Educational Purpose

This is a college project designed to practice:
- Data analysis and visualization techniques
- Python programming for data science
- Dashboard development with Streamlit
- Project organization and documentation
- Version control with Git

## 📞 Contact

- **Student**: Jose V. Colino
- **Project**: Steam Stats EDA Dashboard
- **Institution**: [Your College/University]

---
*Built with ❤️ for learning data science and dashboard development*
