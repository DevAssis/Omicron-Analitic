import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('covid-variants.csv')

countries = list(df['location'].unique())
variantVirus = list(df['variant'].unique())
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

coutry = st.sidebar.selectbox('Escolha o pais', [] + countries)
virus = st.sidebar.selectbox('Escolha a variante', [] + variantVirus)

st.header('Exibindo resultados referente do pais: ' + coutry)
df = df[df['location'] == coutry]

st.subheader('Exibindo resultados para a variante: ' + virus)
df = df[df['variant'] == virus]

dfShow = df.groupby(by=['date']).sum()

fig = px.line(dfShow, x=dfShow.index, y='num_sequences')
fig.update_layout(title='Casos diários de Covid-19')
st.plotly_chart(fig, use_container_width=True)

# O link do app: https://share.streamlit.io/devassis/omicron-analitic/omicron_streamlit.py
# foi atualizado para : https://devassis-omicron-analitic-omicron-streamlit-v9vkhc.streamlitapp.com/
