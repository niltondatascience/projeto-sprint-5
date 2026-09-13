"""Dashboard de anúncios de venda de carros nos EUA."""

import pandas as pd
import plotly.express as px
import streamlit as st

# leitura dos dados
car_data = pd.read_csv('vehicles_us.csv')

# cabeçalho do aplicativo
st.header('Análise de anúncios de venda de carros')
st.write(
    'Use as caixas de seleção abaixo para explorar o conjunto de dados '
    'de anúncios de veículos usados nos Estados Unidos.'
)

# caixa de seleção para o histograma
build_histogram = st.checkbox('Criar um histograma da quilometragem')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')

    fig = px.histogram(
        car_data,
        x='odometer',
        nbins=50,
        title='Distribuição da quilometragem dos veículos',
        labels={'odometer': 'Quilometragem (milhas)'},
    )
    st.plotly_chart(fig, width='stretch')

# caixa de seleção para o gráfico de dispersão
build_scatter = st.checkbox('Criar um gráfico de dispersão preço x quilometragem')

if build_scatter:
    st.write('Criando um gráfico de dispersão entre odometer e price')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        color='condition',
        opacity=0.5,
        title='Relação entre quilometragem e preço',
        labels={
            'odometer': 'Quilometragem (milhas)',
            'price': 'Preço (US$)',
            'condition': 'Condição',
        },
    )
    st.plotly_chart(fig, width='stretch')
