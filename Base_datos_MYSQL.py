import pymysql
import pandas as pd

# CREAR BASE DE DATOS

def crear_base():
    try:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd="admin",
        )
        cursor = conexion.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS brecha_digital")
        conexion.commit()
        print("Base de datos creada")
        conexion.close()
    except Exception as e:
        print("Error al crear base:", e)



# CREAR TABLAS

def crear_tablas():
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        passwd="admin",
        database="brecha_digital"
    )
    cursor = conexion.cursor()

# TABLA: categoria
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categoria (
        id_categoria INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL
    ) ENGINE=InnoDB;
    """)


#TABLA: periodo
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS periodo (
        id_periodo INT AUTO_INCREMENT PRIMARY KEY,
        anio INT NOT NULL
    ) ENGINE=InnoDB;
    """)

# TABLA: indicador
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS indicador (
        indicador_id VARCHAR(20) PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        id_categoria INT NOT NULL,
        FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
    ) ENGINE=InnoDB;
    """)


# TABLA: indicador_valor
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS indicador_valor (
        id_valor INT AUTO_INCREMENT PRIMARY KEY,
        indicador_id VARCHAR(20) NOT NULL,
        id_periodo INT NOT NULL,
        valor FLOAT NOT NULL,
        FOREIGN KEY (indicador_id) REFERENCES indicador(indicador_id),
        FOREIGN KEY (id_periodo) REFERENCES periodo(id_periodo)
    ) ENGINE=InnoDB;
    """)
    
    conexion.commit()
    conexion.close()
    print("Tablas creadas ")

#Insertar Datos
def insertar_datos():
    
    #Leemos cada uno de los archivos de cada .csv limpio
    archivos = {
        "TICS": "data/limpio_indicadores_tics_inegi.csv",
        "EDUCACION": "data/limpio_indicadores_educacion_inegi.csv",
        "EMPLEO": "data/limpio_indicadores_empleo_inegi.csv",
        "VIVIENDA": "data/limpio_indicadores_vivienda_inegi.csv",
        "POBLACION": "data/limpio_indicadores_poblacion_inegi.csv"
    }

    conexion = pymysql.connect(
        host="localhost",
        user="root",
        passwd="admin",
        database="brecha_digital"
    )
    cursor = conexion.cursor()

    # Insertamos categorías
    for categoria in archivos.keys():
        cursor.execute("INSERT IGNORE INTO categoria (nombre) VALUES (%s)", (categoria,))
    conexion.commit()

    # Obtener categorías de cada ID
    cursor.execute("SELECT id_categoria, nombre FROM categoria")
    categorias_dict = {nombre: idcat for (idcat, nombre) in cursor.fetchall()}

    # Procesamos el csv
    for categoria, archivo in archivos.items():
        df = pd.read_csv(archivo)
        id_categoria = categorias_dict[categoria]

        for _, row in df.iterrows():
            indicador_id = str(row["indicador_id"])
            nombre = str(row["nombre"])
            periodo = int(row["periodo"])
            valor = float(row["valor"])

            # Insertamos período si no existe
            cursor.execute("INSERT IGNORE INTO periodo (anio) VALUES (%s)", (periodo,))
            conexion.commit()

            cursor.execute("SELECT id_periodo FROM periodo WHERE anio=%s", (periodo,))
            id_periodo = cursor.fetchone()[0]

            #Insertamos indicador
            cursor.execute("""
                INSERT IGNORE INTO indicador (indicador_id, nombre, id_categoria)
                VALUES (%s, %s, %s)
            """, (indicador_id, nombre, id_categoria))
            conexion.commit()

            # Insertamos valor del indicador
            cursor.execute("""
                INSERT INTO indicador_valor (indicador_id, id_periodo, valor)
                VALUES (%s, %s, %s)
            """, (indicador_id, id_periodo, valor))

        conexion.commit()
    conexion.close()
    print("Datos insertados correctamente")


if __name__ == "__main__":
    crear_base()
    crear_tablas()
    insertar_datos()