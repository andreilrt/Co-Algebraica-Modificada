import tkinter as tk
from tkinter import *
from Vista.modulos.Widgets.Texto import Texto
from Vista.modulos.Widgets.Boton import Boton
from Controlador.Controlador import Controlador
import Vista.modulos.ViewFuntion.Common as Common

class Resultados:
    Inicio = None
    controlador = Controlador()
    textos = []

    def __init__(self, root, colorBotones, colorFondo):
        self.resultados = Frame(root)
        self.color = colorBotones
        self.fondo = colorFondo

    def setFrames(self, inicio):
        self.Inicio = inicio

    def generar(self):    
        self.resultados.config(bg=self.fondo, width='700', heigh='500')
        # Textos
        self.textos = []
        self.textos.append(
            [Texto(self.resultados, 'Mensaje :', self.fondo, 20), .4, .2])
        self.textos.append(
            [Texto(self.resultados, f'{self.controlador.getMensaje()}', self.fondo, 16), .4, .3])
        self.textos.append(
            [Texto(self.resultados, 'Decimal : ', self.fondo, 20), .28, .4])
        self.textos.append(
            [Texto(self.resultados, f'{self.controlador.getDecimal()}', self.fondo, 16), .1, .5])
        Common.generarTextos(self.textos)
        #Botones
        botonDecimal = Boton(self.resultados, self.color,
                           self.fondo, .15, .65, 'Decimal', lambda event: {self.textos[2][0].setText('Decimal : '),
                                                                         self.textos[3][0].setText(f'{self.controlador.getDecimal()}')})
        botonDecimal.generarCuadrado()
        botonBinario = Boton(self.resultados, self.color,
                           self.fondo, .35, .65, 'Binario', lambda event: {self.textos[2][0].setText('Binario : '),
                                                                         self.textos[3][0].setText(f'{self.controlador.getBinario()}')})
        botonBinario.generarCuadrado()
        botonBaseN = Boton(self.resultados, self.color,
                           self.fondo, .55, .65, 'Base N', lambda event: {self.textos[2][0].setText(f'Base {self.controlador.getB()} : '),
                                                                         self.textos[3][0].setText(f'{self.controlador.getBaseN()}')})
        botonBaseN.generarCuadrado()
        botonRegresar = Boton(self.resultados, self.color, self.fondo, .7, .8, 'Regresar', lambda event: {
                                                                                        self.isOculto(), self.Inicio.isVisible() })
        botonRegresar.generarOvalado()

    def isVisible(self):
        self.resultados.pack()

    def isOculto(self):
        self.resultados.pack_forget()