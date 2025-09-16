"""
Steam Stats Dashboard - Streamlit Application

A dashboard for visualizing Steam game statistics and insights.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from pathlib import Path
import sys

# Add src to path for imports
sys.path.append('../src')
from data.data_loader import load_steam_data, clean_steam_data
from visualization.plots import create_interactive_scatter

# Page configuration
st.set_page_config(
    page_title="Steam Stats Dashboard",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🎮 Steam Stats Dashboard")
st.markdown("Explore Steam game statistics and insights")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page:",
    ["Overview", "Price Analysis", "Genre Analysis", "Time Trends", "Game Details"]
)

# Load data function with caching
@st.cache_data
def load_data():
    """Load and cache the Steam dataset."""
    # TODO: Replace with actual dataset path
    data_path = "../data/processed/steam_clean.csv"
    try:
        df = pd.read_csv(data_path)
        return df
    except FileNotFoundError:
        # Return sample data for demonstration
        st.warning("Dataset not found. Using sample data for demonstration.")
        return create_sample_data()

def create_sample_data():
    """Create sample data for demonstration purposes."""
    np.random.seed(42)
    n_games = 1000
    
    genres = ['Action', 'Adventure', 'RPG', 'Strategy', 'Simulation', 'Sports', 'Racing', 'Puzzle']
    platforms = ['Windows', 'Mac', 'Linux']
    
    data = {
        'name': [f'Game_{i}' for i in range(n_games)],
        'price': np.random.exponential(15, n_games),
        'genre': np.random.choice(genres, n_games),
        'platform': np.random.choice(platforms, n_games),
        'rating': np.random.normal(7.5, 1.5, n_games),
        'release_year': np.random.randint(2010, 2024, n_games),
        'total_reviews': np.random.exponential(1000, n_games).astype(int)
    }
    
    # Ensure ratings are between 0 and 10
    data['rating'] = np.clip(data['rating'], 0, 10)
    
    return pd.DataFrame(data)

# Load the data
df = load_data()

# Display different pages based on selection
if page == "Overview":
    st.header("📊 Dataset Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Games", len(df))
    
    with col2:
        st.metric("Average Price", f"${df['price'].mean():.2f}")
    
    with col3:
        st.metric("Unique Genres", df['genre'].nunique())
    
    with col4:
        st.metric("Avg Rating", f"{df['rating'].mean():.1f}/10")
    
    # Dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10))
    
    # Basic statistics
    st.subheader("Basic Statistics")
    st.dataframe(df.describe())

elif page == "Price Analysis":
    st.header("💰 Price Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Price distribution
        fig_hist = px.histogram(df, x='price', nbins=50, 
                               title='Game Price Distribution')
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Price by genre
        fig_box = px.box(df, x='genre', y='price', 
                        title='Price by Genre')
        fig_box.update_xaxis(tickangle=45)
        st.plotly_chart(fig_box, use_container_width=True)
    
    # Price range filter
    st.subheader("Filter by Price Range")
    price_range = st.slider(
        "Select price range:",
        min_value=float(df['price'].min()),
        max_value=float(df['price'].max()),
        value=(float(df['price'].min()), float(df['price'].max()))
    )
    
    filtered_df = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]
    st.write(f"Games in price range ${price_range[0]:.2f} - ${price_range[1]:.2f}: {len(filtered_df)}")

elif page == "Genre Analysis":
    st.header("🎯 Genre Analysis")
    
    # Genre popularity
    genre_counts = df['genre'].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_pie = px.pie(values=genre_counts.values, names=genre_counts.index,
                        title='Game Distribution by Genre')
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        fig_bar = px.bar(x=genre_counts.index, y=genre_counts.values,
                        title='Number of Games by Genre')
        fig_bar.update_xaxis(tickangle=45)
        st.plotly_chart(fig_bar, use_container_width=True)

elif page == "Time Trends":
    st.header("📈 Time Trends")
    
    # Games released by year
    yearly_releases = df.groupby('release_year').size().reset_index(name='count')
    
    fig_line = px.line(yearly_releases, x='release_year', y='count',
                      title='Games Released by Year')
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Average rating by year
    yearly_ratings = df.groupby('release_year')['rating'].mean().reset_index()
    
    fig_rating = px.line(yearly_ratings, x='release_year', y='rating',
                        title='Average Game Rating by Year')
    st.plotly_chart(fig_rating, use_container_width=True)

elif page == "Game Details":
    st.header("🔍 Game Details")
    
    # Search functionality
    search_term = st.text_input("Search for a game:")
    
    if search_term:
        filtered_games = df[df['name'].str.contains(search_term, case=False, na=False)]
        st.dataframe(filtered_games)
    else:
        st.write("Enter a game name to search")
    
    # Interactive scatter plot
    st.subheader("Interactive Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        x_axis = st.selectbox("X-axis:", ['price', 'rating', 'total_reviews', 'release_year'])
    
    with col2:
        y_axis = st.selectbox("Y-axis:", ['rating', 'price', 'total_reviews', 'release_year'])
    
    if x_axis != y_axis:
        fig_scatter = px.scatter(df, x=x_axis, y=y_axis, color='genre',
                               title=f'{y_axis.title()} vs {x_axis.title()}',
                               hover_data=['name'])
        st.plotly_chart(fig_scatter, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit 🚀 | Steam Stats EDA Dashboard")