import streamlit as st
import pandas as pd
from data.data_loader import load_steam_data, clean_steam_data
from pathlib import Path
from datetime import datetime, date
import plotly.express as px

file_path = Path.cwd() / 'data' / 'raw' / 'games_march2025_full.csv'
df = load_steam_data(file_path)
clean_steam_data(df)

tabs = st.tabs(['EDA','Developer','Publisher','Investor'])

def filter_by_genre_list(df,genres_to_filter: list):
    df = df[df.explode('genres',ignore_index=True)['genres'].isin(genres_to_filter)]

with tabs[0]:
    col1, col2 = st.columns([1, 1.5])
    with col1:
        multiselection = st.multiselect(
            'Filtrar por Gêneros',
            options=sorted(df.explode('genres', ignore_index=True)['genres'].unique())
        )
    with col2:
        date_range = st.date_input(
            "Filtrar por Período de Lançamento",
            [date(2010, 1, 1), date(2025, 1, 1)]
        )

    if multiselection:
        df = df[df['genres'].apply(lambda g_list: any(g in g_list for g in multiselection))]

    if len(date_range) > 1:
        start_dt, end_dt = date_range
        df = df[(df["release_date"] >= start_dt) & (df["release_date"] <= end_dt)]

    st.subheader("Estatísticas Gerais")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Jogos", f"{len(df):,}")
    col2.metric("Gêneros Selecionados", len(multiselection) if multiselection else "Todos")
    col3.metric("Média de Reviews", f"{df['num_reviews_total'].mean():,.0f}")

    st.subheader("Jogos em Destaque")
    for idx, row in df.head(10).iterrows():
        with st.expander(f"{row['name']}"):
            st.image(row['header_image'], width=500)
            st.write(f"**Data de lançamento:** {row['release_date']}")
            st.write(f"**Gêneros:** {', '.join(row['genres'])}")
            st.write(f"**Preço:** ${row.get('price', 0):.2f}")
            st.write(f"**Avaliações:** {row['num_reviews_total']:,}")
            st.write(row.get('short_description', 'Sem descrição disponível.'))

    st.subheader("Gêneros mais populares")
    genre_counts = (
        df.explode('genres')
        .groupby('genres')['num_reviews_total']
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(10)
    )
    fig = px.bar(
        genre_counts,
        x='genres',
        y='num_reviews_total',
        text='num_reviews_total',
        color='genres',
        title='Top 10 Gêneros por Total de Reviews',
    )
    fig.update_traces(texttemplate='%{text:,}', textposition='outside')
    fig.update_layout(
        xaxis_title='Gênero',
        yaxis_title='Total de Reviews',
        xaxis={'categoryorder':'total descending'},
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

with tabs[1]:
    
    
    top10 = df.nlargest(10, 'num_reviews_total')
    fig = px.bar(
        top10,
        x='name',
        y='peak_ccu',
        title='Top 10 Games by Total Reviews (Peak CCU)',
        text='peak_ccu',
        color='peak_ccu',
        color_continuous_scale='viridis'
    )

    
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(xaxis_title='Game', yaxis_title='Peak CCU', showlegend=False)

    
    st.plotly_chart(fig, use_container_width=True)

    multiselection = st.multiselect('Gêneros', options=df.explode('genres',ignore_index=True)['genres'].unique())
    if len(multiselection) != 0:
        filter_by_genre_list(df, multiselection)

    date_range = st.date_input("Select date range", [date(1997, 6, 30), date(2025, 3, 10)])
    if len(date_range) > 1:
        start_dt = date_range[0]
        end_dt = date_range[1]
        df = df[(df["release_date"] >= start_dt) & (df["release_date"] <= end_dt)]

    for idx, row in df.head(10).iterrows():
        st.write(row['name'])
        st.image(row['header_image'], width=400)
        if st.button("Show info", key=f"btn_{idx}"):
            st.write(row)  

with tabs[2]:
    all_genres = sorted({g for sub in df['genres'] for g in sub})
    selected_genre = st.selectbox("Selecione um gênero:", all_genres)

    filtered = df[df.explode('genres',ignore_index=True)['genres']==selected_genre]


    platform_cols = ['windows', 'mac', 'linux']
    platform_ranking = (
        filtered.melt(id_vars=['name', 'num_reviews_total'], value_vars=platform_cols,
                    var_name='platform', value_name='available')
        .query("available == True")
        .groupby('platform')['num_reviews_total']
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        platform_ranking,
        x='platform',
        y='num_reviews_total',
        text='num_reviews_total',
        color='platform',
        title=f"Plataformas mais relevantes para o gênero: {selected_genre}",
    )

    fig.update_traces(texttemplate='%{text:,}', textposition='outside')
    fig.update_layout(
        xaxis_title="Plataforma",
        yaxis_title="Total de Reviews (proxy de audiência)",
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(showgrid=True, gridcolor='rgba(200,200,200,0.3)')
    )

    st.plotly_chart(fig, use_container_width=True)

with tabs[3]:
    ranking = (
        filtered.groupby('developers')['num_reviews_total']
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(20)
    )

    fig = px.bar(
        ranking,
        x='developers',
        y='num_reviews_total',
        text='num_reviews_total',
        color='num_reviews_total',
        title='Desenvolvedores independentes mais promissores',
    )

    fig.update_traces(texttemplate='%{text:,}', textposition='outside')
    fig.update_layout(
        xaxis_title='Desenvolvedor',
        yaxis_title='Total de Reviews',
        xaxis={'categoryorder':'total descending'},
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)