import streamlit as st
import pandas as pd
import plotly.express as px

def render():
    st.title("🎓 Capital Humano – Habilidades para el mundo digital")
    df_e = pd.read_csv("data/limpio_indicadores_educacion_inegi.csv")
    df_em = pd.read_csv("data/limpio_indicadores_empleo_inegi.csv")

    col1, col2 = st.columns(2)

    with col1:
        indicador_edu = st.selectbox("Indicador Educativo", df_e["nombre"].unique())
    with col2:
        indicador_emp = st.selectbox("Indicador de Empleo", df_em["nombre"].unique())

    df_edu = df_e[df_e["nombre"] == indicador_edu]
    df_emp = df_em[df_em["nombre"] == indicador_emp]

    # KPI Educación
    st.subheader("📘 KPI Educación")
    st.metric(indicador_edu, f"{df_edu['valor'].iloc[-1]:.2f}")

    fig1 = px.line(df_edu, x="periodo", y="valor", markers=True,
                   title=f"Evolución Educativa: {indicador_edu}")
    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

    # KPI Empleo
    st.subheader("💼 KPI Empleo")
    st.metric(indicador_emp, f"{df_emp['valor'].iloc[-1]:,.0f}")

    fig2 = px.area(df_emp, x="periodo", y="valor", markers=True,
                   title=f"Evolución Laboral: {indicador_emp}")
    st.plotly_chart(fig2, use_container_width=True)

if __name__ == "__main__":
    render()