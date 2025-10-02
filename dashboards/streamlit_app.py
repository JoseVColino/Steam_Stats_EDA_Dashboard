import streamlit as st
import pandas as pd
from data.data_loader import load_steam_data


st.title('DASHBOARD STEAM 🎆')
st.write('Dashboard utilizando o dataset público disponível no Kaggle em: https://www.kaggle.com/datasets/artermiloff/steam-games-dataset?select=games_march2025_full.csv..')

st.header('Sessão principal')
st.subheader('subsessão de um dado específico')
st.text('texto simples sem formatação')
st.markdown('texto com formatação de **markdown** e *legal* ')

df = load_steam_data()

st.dataframe(df.head())