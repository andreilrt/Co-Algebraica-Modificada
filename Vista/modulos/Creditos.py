import tkinter as tk
from tkinter import *
from Vista.modulos.Widgets.Boton import Boton
from Vista.modulos.Widgets.Texto import Texto
import Vista.modulos.ViewFuntion.Common as Common

class Creditos:
    inicio = None

    def __init__(self, root, colorBotones, colorFondo):
        self.creditos = Frame(root)
        self.fondo = colorFondo
        self.color = colorBotones

    def setFrames(self, inicio):
        self.inicio = inicio

    def generar(self):
        self.creditos.config(bg=self.fondo, width='700', heigh='1000')
        # Textos
        textos = []
        textos.append(
            [Texto(self.creditos, 'Creditos 2020-2', self.fondo, 20), .4, .1])
        textos.append(
            [Texto(self.creditos, 'Sistemas De Telecomunicaciones II', self.fondo, 14), .3, .2])
        textos.append(
            [Texto(self.creditos, 'ING. Gustavo Alonso Chica Pedraza', self.fondo, 14), .3, .3])
        textos.append(
            [Texto(self.creditos, 'Integrantes :', self.fondo, 16), .4, .4])
        textos.append(
            [Texto(self.creditos, 'Andrei Lizandro Riaño Tuta', self.fondo, 14), .3, .5])
        textos.append(
            [Texto(self.creditos, 'Johann Stev Castellanos Gonzalez', self.fondo, 14), .3, .6])
        textos.append(
            [Texto(self.creditos, 'Andres Nicolas Linares Ch.', self.fondo, 14), .3, .7])
        Common.generarTextos(textos)
        # Botones
        botonRegresar = Boton(self.creditos, self.color, self.fondo, .7, .8, 'Regresar', lambda event: {
                              self.isOculto(), self.inicio.isVisible()})
        botonRegresar.generarOvalado()

    def isVisible(self):
        self.creditos.pack()

    def isOculto(self):
        self.creditos.pack_forget()
