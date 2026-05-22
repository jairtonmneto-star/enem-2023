

import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Análise de Dados do ENEM 2023")

@st.cache_data
def carregar_dados():
    colunas = ["SG_UF_PROVA","TP_ESCOLA","TP_SEXO","Q006",  "NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC", "NU_NOTA_MT","NU_NOTA_REDACAO"]
    df = pd.read_csv("MICRODADOS_ENEM_2023.csv", sep=";", encoding="latin-1", usecols=colunas)
    df = df.dropna(subset=["NU_NOTA_MT","NU_NOTA_REDACAO"])
    df["MEDIA_GERAL"] = df[["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_LC","NU_NOTA_MT"]].mean(axis=1)
    df["TP_ESCOLA"] = df["TP_ESCOLA"].map({1:"Não Respondeu", 2:"Publica", 3:"Privada"})
    df["TP_SEXO"] = df["TP_SEXO"].map({"M":"Masculino", "F":"Feminino"})
    return df

df = carregar_dados()

# Filtro de estado — vem antes dos gráficos
estados = sorted(df["SG_UF_PROVA"].unique())
estado_selecionado = st.selectbox("Filtrar por Estado:", ["Todos"] + estados)
if estado_selecionado != "Todos":
    df = df[df["SG_UF_PROVA"] == estado_selecionado]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total de Participantes", f"{len(df):,}")
col2.metric("Média Geral Nacional", f"{df['MEDIA_GERAL'].mean():.1f}")
col3.metric("Melhor Estado", df.groupby('SG_UF_PROVA')['MEDIA_GERAL'].mean().idxmax())

# Gráfico 1 — Estado
st.subheader("Média por Estado")
media_por_estado = df.groupby("SG_UF_PROVA")["MEDIA_GERAL"].mean().sort_values(ascending=False).reset_index()
fig1 = px.bar(media_por_estado, x="SG_UF_PROVA", y="MEDIA_GERAL",color="MEDIA_GERAL", color_continuous_scale="blues",labels={"SG_UF_PROVA":"Estado", "MEDIA_GERAL":"Média Geral"}, title="Média Geral por Estado")
st.plotly_chart(fig1)

# Gráfico 2 — Escola
st.subheader("Média por Tipo de Escola")
media_por_escola = df.groupby("TP_ESCOLA")["MEDIA_GERAL"].mean().reset_index()
fig2 = px.bar(media_por_escola, x="TP_ESCOLA", y="MEDIA_GERAL",color="TP_ESCOLA",labels={"TP_ESCOLA":"Tipo de Escola", "MEDIA_GERAL":"Média Geral"},title="Média Geral por Tipo de Escola")
st.plotly_chart(fig2)

# Gráfico 3 — Renda
st.subheader("Média por Renda Familiar")
media_por_renda = df.groupby("Q006")["MEDIA_GERAL"].mean().reset_index().sort_values("Q006")
fig3 = px.line(media_por_renda, x="Q006", y="MEDIA_GERAL", markers=True,labels={"Q006":"Renda Familiar", "MEDIA_GERAL":"Média Geral"}, title="Média Geral por Renda Familiar")
st.plotly_chart(fig3)

# Gráfico 4 — Sexo
st.subheader("Média por Sexo")
media_por_sexo = df.groupby("TP_SEXO")["MEDIA_GERAL"].mean().reset_index()
fig4 = px.bar(media_por_sexo, x="TP_SEXO", y="MEDIA_GERAL",
color="TP_SEXO",labels={"TP_SEXO":"Sexo", "MEDIA_GERAL":"Média Geral"},title="Média Geral por Sexo")
st.plotly_chart(fig4)