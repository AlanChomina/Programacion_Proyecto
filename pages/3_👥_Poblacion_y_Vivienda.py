import streamlit as st
import plotly.express as px
import pandas as pd


def render():
    st.title("👥 Brecha Digital Social – Riesgos de exclusión")

    df_p = pd.read_csv("data/limpio_indicadores_poblacion_inegi.csv")
    df_v = pd.read_csv("data/limpio_indicadores_vivienda_inegi.csv")

    indicador_p = st.selectbox("Indicador Poblacional", df_p["nombre"].unique())
    indicador_v = st.selectbox("Indicador Vivienda", df_v["nombre"].unique())

    df_fp = df_p[df_p["nombre"] == indicador_p]
    df_fv = df_v[df_v["nombre"] == indicador_v]

    # KPI Población
    st.subheader("📌 KPI Poblacional")
    st.metric(indicador_p, f"{df_fp['valor'].iloc[-1]:,.0f}")

    fig1 = px.line(df_fp, x="periodo", y="valor", markers=True,
                   title=f"Crecimiento poblacional: {indicador_p}")
    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

    # KPI Vivienda
    st.subheader("📌 KPI Vivienda")
    st.metric(indicador_v, f"{df_fv['valor'].iloc[-1]:,.0f}")

    fig2 = px.bar(df_fv, x="periodo", y="valor",
                  title=f"Evolución de vivienda: {indicador_v}")
    st.plotly_chart(fig2, use_container_width=True)


if __name__ == "__main__":
    render()