import tkinter as tk
from tkinter import *
from Vista.modulos.Inicio import Inicio
from Vista.modulos.Creditos import Creditos
from Vista.modulos.Resultados import Resultados

#########################################################################################################
# Configuracion de la raiz
raiz = Tk()
raiz.title('Codificación Aritmetica')
raiz.iconbitmap('./usta.ico')
raiz.geometry('700x500')
raiz.resizable(0, 0)
raiz.config(bg='#FFFFFF')
# Variables Globales
colorBotones = "#00E0E8"
colorFondo = '#FFFFFF'
########################################################################################################
# Creacion de los frames
inicio = Inicio(raiz, colorBotones, colorFondo)
inicio.generar()

creditos = Creditos(raiz, colorBotones, colorFondo)
creditos.generar()

resultados = Resultados(raiz, colorBotones, colorFondo)

# Navegacion
inicio.setFrames(resultados, creditos)
creditos.setFrames(inicio)
resultados.setFrames(inicio)

inicio.isVisible()
resultados.generar()

raiz.mainloop()