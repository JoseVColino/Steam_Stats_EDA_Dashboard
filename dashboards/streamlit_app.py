import streamlit as st
import pandas as pd
from pathlib import Path
from data.data_loader import load_steam_data, quick_load_steam_data

col1,col2 = st.tabs(['visualização inicial', 'publicando um jogo'])
with col1:
    file_path = Path.cwd() / 'data' / 'raw' / 'games_march2025_full.csv'
    st.title('DASHBOARD STEAM 🎆')
    st.write('Dashboard utilizando o dataset público disponível no Kaggle em: https://www.kaggle.com/datasets/artermiloff/steam-games-dataset?select=games_march2025_full.csv..')

    st.header('Sessão principal')
    st.subheader('subsessão de um dado específico')
    st.text('texto simples sem formatação')
    st.markdown('texto com formatação de **markdown** e *legal* ')


    load_full_data = st.checkbox("Load full dataset")

    if load_full_data:
        st.info("Loading the full dataset...")
        df = load_steam_data(file_path)
    else:
        st.info("Loading a 5-row sample. Select the checkbox to load the full dataset.")
        df = quick_load_steam_data(file_path)

    st.dataframe(df)