import requests
import pandas as pd
import numpy as np


url_tics = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/6206972689,6206972690,6206972691,6206972692,6206972693,6206972694,6206972695,6206972697,6207129517,8999998854/es/00/false/BISE/2.0/0e38e4f2-697c-6b5b-0a3e-d7b0b2e55bcb?type=json"
url_educacion = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000041,3108001001,6200240391,6207019024,6207019026,6207019028,6207019029,6207049066,6207049067,1005000038/es/00/false/BISE/2.0/0e38e4f2-697c-6b5b-0a3e-d7b0b2e55bcb?type=json"
url_empleo = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/6200032080,6200032083,6200093709,6200032095,6200093973,6200032078,6200093960,6207019047/es/00/false/BISE/2.0/0e38e4f2-697c-6b5b-0a3e-d7b0b2e55bcb?type=json"
url_vivienda = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1003000024,6207019046,6207019042,6207019055,6207019052,1003000017,3114006001/es/00/false/BISE/2.0/0e38e4f2-697c-6b5b-0a3e-d7b0b2e55bcb?type=json"
url_poblacion = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000073,1002000070,1002000067,1002000061,8999998745,8999998752,8999998757,8999998741,8999998738/es/00/false/BISE/2.0/0e38e4f2-697c-6b5b-0a3e-d7b0b2e55bcb?type=json"

def tics_hogar():
    DESCRIPCIONES = {
        "6206972689": "Hogares con televisor (%)",
        "6206972690": "Hogares con televisor (%)",
        "6206972691": "Usuarios de televisión abierta (%)",
        "6206972692": "Hogares con computadora (%)",
        "6206972693": "Hogares con televisión de paga (%)",
        "6206972694": "Hogares con conexión a internet (%)",
        "6206972695": "Usuarios de radio (%)",
        "6206972697": "Usuarios de internet (%)",
        "6207129517": "Usuarios de teléfono celular (%)",
        "8999998854": "Usuarios que se conectan fuera del hogar (%)"
    }

    response = requests.get(url_tics)
    data = response.json()

    registros = []

    for serie in data["Series"]:
        id_indicador = serie["INDICADOR"]
        nombre = DESCRIPCIONES.get(id_indicador, "Indicador desconocido")

        for obs in serie["OBSERVATIONS"]:

            valor = obs["OBS_VALUE"]

            if valor is None:
                continue

            registros.append({
                "indicador_id": id_indicador,
                "nombre": nombre,
                "periodo": int(obs["TIME_PERIOD"]),
                "valor": float(valor)
            })

    df = pd.DataFrame(registros)
    df.to_csv("archivos_crudos/indicadores_tics_inegi.csv", index=False)

def educacion():

    DESCRIPCIONES = {
        "1002000041": "Porcentaje de personas de 15 años y más alfabetas",
        "1005000038": "Grado promedio de escolaridad (15 años y más)",
        "3108001001": "Porcentaje de analfabetas total",
        "6200240391": "Porcentaje de la población de 15 años y más con rezago educativo",
        "6207019024": "Porcentaje de la población de 3 a 5 años que asiste a la escuela",
        "6207019026": "Porcentaje de la población de 6 a 11 años que asiste a la escuela",
        "6207019028": "Porcentaje de la población de 12 a 14 años que asiste a la escuela",
        "6207019029": "Porcentaje de la población de 15 a 24 años que asiste a la escuela",
        "6207049066": "Población de 6 a 14 años que sabe leer y escribir",
        "6207049067": "Población de 6 a 14 años que no sabe leer y escribir"
    }
    response = requests.get(url_educacion)
    data = response.json()

    registros = []

    for serie in data["Series"]:
        id_indicador = serie["INDICADOR"]
        nombre = DESCRIPCIONES.get(id_indicador, "Indicador desconocido")

        for obs in serie["OBSERVATIONS"]:
            valor = obs["OBS_VALUE"]

            if valor is None:
                continue

            registros.append({
                "indicador_id": id_indicador,
                "nombre": nombre,
                "periodo": int(obs["TIME_PERIOD"]),
                "valor": float(valor)
            })

    df = pd.DataFrame(registros)
    df.to_csv("archivos_crudos/indicadores_educacion_inegi.csv", index=False)
    print("Archivo generado: indicadores_educacion_inegi.csv")

def empleo():
    DESCRIPCIONES = {
        "6200032080": "Población no económicamente activa disponible - 15 años y más",
        "6200032083": "Población ocupada con ingresos de hasta un salario mínimo - 15 años y más",
        "6200093709": "Población ocupada con ingresos de más de 1 hasta 2 salarios mínimos - 15 años y más",
        "6200032095": "Población ocupada que no recibe ingresos - 15 años y más",
        "6200093973": "Población ocupada en el sector informal - 15 años y más",
        "6200032078": "Población económicamente activa - 15 años y más",
        "6200093960": "Población desocupada - 15 años y más",
        "6207019047": "Porcentaje de la población de 12 años y más no económicamente activa que estudia"
    }
    response = requests.get(url_empleo)
    data = response.json()

    registros = []

    for serie in data["Series"]:
        id_indicador = serie["INDICADOR"]
        nombre = DESCRIPCIONES.get(id_indicador, "Indicador desconocido")

        for obs in serie["OBSERVATIONS"]:
            valor = obs["OBS_VALUE"]
            if valor is None:
                continue

            periodo_raw = obs["TIME_PERIOD"]
            periodo = int(periodo_raw.split("/")[0])

            registros.append({
                "indicador_id": id_indicador,
                "nombre": nombre,
                "periodo": periodo,
                "valor": float(valor)
            })

    df = pd.DataFrame(registros)
    df.to_csv("archivos_crudos/indicadores_empleo_inegi.csv", index=False)
    print("Archivo generado: indicadores_empleo_inegi.csv")

def vivienda():
    
    DESCRIPCIONES = {
        "1003000017": "Viviendas particulares habitadas",
        "1003000024": "Viviendas particulares habitadas que disponen de computadora",
        "3114006001": "Porcentaje de viviendas con electricidad",
        "6207019042": "Porcentaje de viviendas particulares habitadas que disponen de Internet",
        "6207019046": "Porcentaje de viviendas particulares habitadas que disponen de computadora",
        "6207019052": "Porcentaje de viviendas particulares habitadas que disponen de pantalla plana",
        "6207019055": "Porcentaje de viviendas particulares habitadas que disponen de teléfono celular"
    }
    response = requests.get(url_vivienda)
    data = response.json()

    registros = []
    for serie in data["Series"]:
        id_indicador = serie["INDICADOR"]
        nombre = DESCRIPCIONES.get(id_indicador, "Indicador desconocido")

        for obs in serie["OBSERVATIONS"]:
            valor = obs["OBS_VALUE"]

            if valor is None:
                continue

            registros.append({
                "indicador_id": id_indicador,
                "nombre": nombre,
                "periodo": int(obs["TIME_PERIOD"]),
                "valor": float(valor)
            })

    df = pd.DataFrame(registros)
    df.to_csv("archivos_crudos/indicadores_vivienda_inegi.csv", index=False)
    print("Archivo generado: indicadores_vivienda_inegi.csv")

def poblacion():
    DESCRIPCIONES = {
        "1002000061": "Población total",
        "1002000067": "Población total hombres",
        "1002000070": "Población total mujeres",
        "1002000073": "Población de 0 a 14 años",

        "8999998738": "Población de 15 a 29 años",
        "8999998741": "Población de 30 a 44 años",
        "8999998745": "Población de 45 a 59 años",
        "8999998752": "Población de 60 años y más",
        "8999998757": "Relación de dependencia (población dependiente vs activa)"
    }
    response = requests.get(url_poblacion)
    data = response.json()

    registros = []
    for serie in data["Series"]:
        id_indicador = serie["INDICADOR"]
        nombre = DESCRIPCIONES.get(id_indicador, "Indicador desconocido")

        for obs in serie["OBSERVATIONS"]:
            valor = obs["OBS_VALUE"]

            if valor is None:
                continue

            registros.append({
                "indicador_id": id_indicador,
                "nombre": nombre,
                "periodo": int(obs["TIME_PERIOD"]),
                "valor": float(valor)
            })

    df = pd.DataFrame(registros)
    df.to_csv("archivos_crudos/indicadores_poblacion_inegi.csv", index=False)
    print("Archivo generado: indicadores_poblacion_inegi.csv")


if __name__ == "__main__":
    tics_hogar()
    educacion()
    empleo()
    vivienda()
    poblacion()