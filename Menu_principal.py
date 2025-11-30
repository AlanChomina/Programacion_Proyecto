import tkinter as tk
from tkinter import messagebox
import subprocess
import sys


def ejecutar_script(ruta_script):
    try:
        subprocess.run([sys.executable, ruta_script], check=True)
        messagebox.showinfo("Éxito", f"Script ejecutado:\n{ruta_script}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

def run_descarga():
    ejecutar_script("extraer_datos.pý")

def run_limpiar():
    ejecutar_script("limpiar_datos.py")

def run_bd():
    ejecutar_script("Base_datos_MYSQL.py")

def run_streamlit():
    try:
        subprocess.Popen(["streamlit", "run", ".\🏠_Inicio.py"], shell=True)
        messagebox.showinfo("Ejecutando", "Se abrió el Dashboard.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo iniciar Streamlit:\n{e}")

# Ventana principal

root = tk.Tk()
root.title("Menú – Brecha Digital")
root.geometry("420x350")
root.configure(bg="white")

# Estilo moderno
font_titulo = ("Arial", 14, "bold")
font_boton = ("Arial", 12)

titulo = tk.Label(root, text="Menú Principal", bg="white", font=font_titulo)
titulo.pack(pady=20)

# -----------------------------
# Botones
# -----------------------------

btn1 = tk.Button(
    root,
    text="Descargar datos INEGI",
    font=font_boton,
    width=25,
    height=2,
    command=run_descarga
)
btn1.pack(pady=10)

btn2 = tk.Button(
    root,
    text="Limpiar archivos CSV",
    font=font_boton,
    width=25,
    height=2,
    command=run_limpiar
)
btn2.pack(pady=10)

btn3 = tk.Button(
    root,
    text="Crear BD e insertar datos",
    font=font_boton,
    width=25,
    height=2,
    command=run_bd
)
btn3.pack(pady=10)

btn4 = tk.Button(
    root,
    text="Abrir Dashboard Streamlit",
    font=font_boton,
    width=25,
    height=2,
    command=run_streamlit
)
btn4.pack(pady=10)


# Ejecutar ventana
root.mainloop()
