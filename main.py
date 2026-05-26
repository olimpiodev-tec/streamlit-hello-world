import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Teste Streamlit + Pandas",
    layout="wide"
)

st.title("Teste do Streamlit com Pandas")

st.write("Aplicação simples para testar Streamlit no Render")

# Dados fixos
dados = {
    "Nome": ["Ana", "Carlos", "João", "Maria", "Pedro"],
    "Idade": [22, 30, 27, 35, 29],
    "Nota": [8.5, 7.2, 9.1, 8.8, 6.9]
}

df = pd.DataFrame(dados)

st.subheader("Tabela de Dados")
st.dataframe(df, use_container_width=True)

st.subheader("Resumo Estatístico")
st.write(df.describe())

st.subheader("Gráfico de Notas")
st.bar_chart(df["Nota"])

# Filtro simples
nome = st.selectbox(
    "Filtrar aluno",
    ["Todos"] + list(df["Nome"])
)

if nome != "Todos":
    st.write(df[df["Nome"] == nome])
