import pandas as pd


def limpiar_tics():
    archivo = "indicadores_tics_inegi.csv"
    df = pd.read_csv(archivo)

    df = df.drop_duplicates()
    df = df[df["valor"].notna()]
    df = df[df["valor"] >= 0]

    df["periodo"] = df["periodo"].astype(int)
    df["valor"] = df["valor"].astype(float)

    df.to_csv("limpio_indicadores_tics_inegi.csv", index=False)
    print("Archivo: limpio_indicadores_tics_inegi.csv")


def limpiar_educacion():
    archivo = "indicadores_educacion_inegi.csv"
    df = pd.read_csv(archivo)

    df = df.drop_duplicates()
    df = df[df["valor"].notna()]
    df = df[df["valor"] >= 0]
    df = df[~((df["indicador_id"].isin(["6207049066","6207049067"])) & (df["periodo"] == 2020))]

    df["periodo"] = df["periodo"].astype(int)
    df["valor"] = df["valor"].astype(float)

    df.to_csv("limpio_indicadores_educacion_inegi.csv", index=False)
    print("Archivo: limpio_indicadores_educacion_inegi.csv")


def limpiar_empleo():
    archivo = "indicadores_empleo_inegi.csv"
    df = pd.read_csv(archivo)

    df = df.drop_duplicates()
    df = df[df["valor"].notna()]
    df = df[df["valor"] >= 0]
    df = df.groupby(["indicador_id","nombre","periodo"], as_index=False)["valor"].mean()

    df["periodo"] = df["periodo"].astype(int)
    df["valor"] = df["valor"].astype(float)

    df.to_csv("limpio_indicadores_empleo_inegi.csv", index=False)
    print("Archivo: limpio_indicadores_empleo_inegi.csv")


def limpiar_vivienda():
    archivo = "indicadores_vivienda_inegi.csv"
    df = pd.read_csv(archivo)

    df = df.drop_duplicates()
    df = df[df["valor"].notna()]
    df = df[df["valor"] >= 0]

    df["periodo"] = df["periodo"].astype(int)
    df["valor"] = df["valor"].astype(float)

    df.to_csv("limpio_indicadores_vivienda_inegi.csv", index=False)
    print("Archivo: limpio_indicadores_vivienda_inegi.csv")


def limpiar_poblacion():
    archivo = "indicadores_poblacion_inegi.csv"
    df = pd.read_csv(archivo)

    df = df.drop_duplicates()
    df = df[df["valor"].notna()]
    df = df[df["valor"] >= 0]

    df["periodo"] = df["periodo"].astype(int)
    df["valor"] = df["valor"].astype(float)

    df.to_csv("limpio_indicadores_poblacion_inegi.csv", index=False)
    print("Archivo: limpio_indicadores_poblacion_inegi.csv")


if __name__ == "__main__":
    limpiar_tics()
    limpiar_educacion()
    limpiar_empleo()
    limpiar_vivienda()
    limpiar_poblacion()
