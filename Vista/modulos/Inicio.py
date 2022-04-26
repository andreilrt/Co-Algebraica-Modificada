import tkinter as tk
from tkinter import *
from Vista.modulos.Widgets.Texto import Texto
from Vista.modulos.Widgets.Boton import Boton
from Vista.modulos.Widgets.IngresoData import IngresoData
import Vista.modulos.ViewFuntion.Common as Common
from Controlador.Controlador import Controlador
from Modelos.CodAlgMod import CodAlgMod

class Inicio:
    Resultado = None
    creditos  = None
    Error = ''
    mensaje = None
    controlador = Controlador()
    modelo = CodAlgMod()
    
    def __init__(self, root, colorBotones, colorFondo):
        self.inicio = Frame(root)
        self.color = colorBotones
        self.fondo = colorFondo

    def setFrames(self, Resultados, creditos):
        self.Resultado = Resultados
        self.creditos = creditos

    def generar(self):
        self.inicio.config(bg=self.fondo, width='700', heigh='500')
        # Textos
        textos = []
        textos.append(
            [Texto(self.inicio, 'Codificacion Algebraica Modificada', self.fondo, 30), .1, .2])
        textos.append(
            [Texto(self.inicio, 'Ingresar mensaje', self.fondo, 14), .4, .3])
        textos.append(
            [Texto(self.inicio, 'Mensaje maximo de 15 caracteres y 2-9 simbolos :', self.fondo, 12), .28, .35])
        Common.generarTextos(textos)
        textoError = Texto(self.inicio, self.Error, self.fondo, 14)
        textoError.Generar()
        # input
        self.mensaje = IngresoData(self.inicio, .1, .45, .8)
        self.mensaje.ingreso()
        # Botones
        def Comenzar(event):
            Mensaje = self.mensaje.getData()
            self.controlador.setMensaje(Mensaje)
            validacion = Common.validarMensaje(Mensaje)
            textoError.isOculto()
            if  validacion == 1:
                textoError.setText('Tamaño Invalido')
                textoError.isVisible(.35, .75)
                self.mensaje.Limpiar()
            elif validacion == 2:
                textoError.setText('Numero de Simbolos Invalido')
                textoError.isVisible(.35, .75)
                self.mensaje.Limpiar()
            elif validacion == 3:
                textoError.setText('Caracteres Especiales')
                textoError.isVisible(.35, .75)
                self.mensaje.Limpiar()
            else:
                self.modelo.mensaje2basen()
                self.modelo.basen2decimal()
                self.modelo.decimal2binario()
                self.Resultado.textos[1][0].setText(f'{self.controlador.getMensaje()}')
                self.Resultado.textos[2][0].setText('Decimal')
                self.Resultado.textos[3][0].setText(f'{self.controlador.getDecimal()}')
                self.isOculto()
                self.Resultado.isVisible()

        botonCalcular = Boton(self.inicio, self.color, self.fondo, .37, .6,
                              'Comenzar', Comenzar)
        botonCalcular.generarOvalado()
        botonCreditos = Boton(self.inicio, self.color, self.fondo, .05, .85,
                              'Creditos', lambda event: {self.isOculto(), self.creditos.isVisible()})
        botonCreditos.generarCuadrado()
        botonSalir = Boton(self.inicio, self.color,
                           self.fondo, .65, .85, 'Salir', lambda event: exit())
        botonSalir.generarCuadrado()

    def isVisible(self):
        self.inicio.pack()

    def isOculto(self):
        self.inicio.pack_forget()