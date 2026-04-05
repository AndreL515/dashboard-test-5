import streamlit as st
import plotly.express as px
import pandas as pd
from utils.queries import carregar_dados_no_banco

st.set_page_config(
    page_title="Dashboard Acadêmico",
    page_icon="🎓",
    layout="wide"
)

carregar_dados_no_banco("data/dados_brutos.csv")

st.title("🎓 Dashboard de Dados Acadêmicos")
st.markdown("Painel de acompanhamento de alunos universitários")

df_full = pd.read_csv("data/dados_brutos.csv")

cursos = ["Todos"] + sorted(df_full["curso"].unique().tolist())
curso_sel = st.sidebar.selectbox("Filtrar por curso", cursos)

semestres = ["Todos"] + sorted(df_full["semestre"].unique().tolist())
sem_sel = st.sidebar.selectbox("Filtrar por semestre", semestres)

df = df_full.copy()
if curso_sel != "Todos":
    df = df[df["curso"] == curso_sel]
if sem_sel != "Todos":
    df = df[df["semestre"] == sem_sel]

col1, col2, col3, col4 = st.columns(4)
total = len(df)
ativos = len(df[df["situacao"] == "Ativo"])
evadidos = len(df[df["situacao"] == "Evadido"])
cr_medio = df["cr"].mean()

col1.metric("Total de Alunos", total)
col2.metric("Alunos Ativos", ativos)
col3.metric("Evasões", evadidos, delta=f"{100*evadidos/total:.1f}%", delta_color="inverse")
col4.metric("CR Médio", f"{cr_medio:.2f}")

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Distribuição por Situação")
    df_sit = df["situacao"].value_counts().reset_index()
    df_sit.columns = ["Situação", "Total"]
    fig = px.pie(df_sit, names="Situação", values="Total", hole=0.4,
                 color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig, use_container_width=True)

with col_b:
    st.subheader("CR Médio por Curso")
    df_cr = df.groupby("curso")["cr"].mean().round(2).reset_index()
    df_cr.columns = ["Curso", "CR Médio"]
    fig = px.bar(df_cr.sort_values("CR Médio"), x="CR Médio", y="Curso",
                 orientation="h", color="CR Médio",
                 color_continuous_scale="Blues")
    st.plotly_chart(fig, use_container_width=True)

col_c, col_d = st.columns(2)

with col_c:
    st.subheader("Taxa de Evasão por Curso")
    df_ev = df.groupby("curso").apply(
        lambda x: round(100 * (x["situacao"] == "Evadido").sum() / len(x), 1)
    ).reset_index()
    df_ev.columns = ["Curso", "Taxa de Evasão (%)"]
    fig = px.bar(df_ev.sort_values("Taxa de Evasão (%)"), x="Taxa de Evasão (%)", y="Curso",
                 orientation="h", color="Taxa de Evasão (%)",
                 color_continuous_scale="Reds")
    st.plotly_chart(fig, use_container_width=True)

with col_d:
    st.subheader("Alunos por Renda Familiar")
    df_renda = df["renda_familiar"].value_counts().reset_index()
    df_renda.columns = ["Renda", "Total"]
    fig = px.bar(df_renda, x="Renda", y="Total",
                 color="Renda", color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("📋 Dados Detalhados")
st.dataframe(df, use_container_width=True, hide_index=True)