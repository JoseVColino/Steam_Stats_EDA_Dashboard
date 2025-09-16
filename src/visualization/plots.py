"""
Visualization utilities for Steam data analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Set style for consistent plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def plot_price_distribution(df: pd.DataFrame, price_column: str = 'price') -> None:
    """
    Plot the distribution of game prices.
    
    Args:
        df (pd.DataFrame): Steam dataset
        price_column (str): Name of the price column
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Histogram
    ax1.hist(df[price_column], bins=50, edgecolor='black', alpha=0.7)
    ax1.set_xlabel('Price ($)')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Distribution of Game Prices')
    
    # Box plot
    ax2.boxplot(df[price_column])
    ax2.set_ylabel('Price ($)')
    ax2.set_title('Price Box Plot')
    
    plt.tight_layout()
    plt.show()

def plot_genre_popularity(df: pd.DataFrame, genre_column: str = 'genres') -> None:
    """
    Plot the popularity of different game genres.
    
    Args:
        df (pd.DataFrame): Steam dataset
        genre_column (str): Name of the genre column
    """
    # Count games by genre (assuming genres might be comma-separated)
    genre_counts = df[genre_column].value_counts().head(10)
    
    plt.figure(figsize=(12, 8))
    genre_counts.plot(kind='barh')
    plt.xlabel('Number of Games')
    plt.ylabel('Genre')
    plt.title('Top 10 Most Popular Game Genres')
    plt.tight_layout()
    plt.show()

def create_interactive_scatter(df: pd.DataFrame, x_col: str, y_col: str, 
                             color_col: str = None, title: str = "Interactive Scatter Plot"):
    """
    Create an interactive scatter plot using Plotly.
    
    Args:
        df (pd.DataFrame): Steam dataset
        x_col (str): Column for x-axis
        y_col (str): Column for y-axis
        color_col (str): Column for color coding
        title (str): Plot title
        
    Returns:
        plotly.graph_objects.Figure: Interactive plot
    """
    fig = px.scatter(df, x=x_col, y=y_col, color=color_col,
                     title=title, hover_data=df.columns)
    fig.update_layout(
        xaxis_title=x_col.replace('_', ' ').title(),
        yaxis_title=y_col.replace('_', ' ').title()
    )
    return fig

def save_plot(filename: str, dpi: int = 300) -> None:
    """
    Save the current matplotlib plot.
    
    Args:
        filename (str): Output filename
        dpi (int): Image resolution
    """
    plt.savefig(filename, dpi=dpi, bbox_inches='tight')
    print(f"Plot saved as {filename}")