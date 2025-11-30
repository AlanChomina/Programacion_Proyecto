import streamlit as st
import plotly.express as px
import pandas as pd

def render():
    st.title("📡 Acceso Tecnológico – Brecha Digital Material")
    df_tics = pd.read_csv("data/limpio_indicadores_tics_inegi.csv")
    df_viv = pd.read_csv("data/limpio_indicadores_vivienda_inegi.csv")

    with st.expander("🔎 Filtros"):
        indicador_t = st.selectbox("Indicador TIC", df_tics["nombre"].unique())
        indicador_v = st.selectbox("Indicador Vivienda", df_viv["nombre"].unique())

    df_t = df_tics[df_tics["nombre"] == indicador_t]
    df_v = df_viv[df_viv["nombre"] == indicador_v]

    # KPI Tecnológico
    st.subheader("📌 KPI: Último valor TIC registrado")
    st.metric(indicador_t, f"{df_t['valor'].iloc[-1]:.2f}")

    # Línea TIC
    fig1 = px.line(df_t, x="periodo", y="valor", markers=True,
                   title=f"Evolución: {indicador_t}")
    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

    # KPI Vivienda
    st.subheader("🏠 KPI: Último valor de Vivienda")
    st.metric(indicador_v, f"{df_v['valor'].iloc[-1]:,.0f}")

    fig2 = px.bar(df_v, x="periodo", y="valor",
                  title=f"Vivienda – {indicador_v}")
    st.plotly_chart(fig2, use_container_width=True)


if __name__ == "__main__":
    render()
