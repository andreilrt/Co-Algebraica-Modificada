Mensaje = 'PAco'
L = 0
B = 1
DicAlfabeto = {'':0}
Decimal = 0.0
Binario = '0.'
BaseN = 0.0

class Controlador:
    def setMensaje(self, mensaje):
        global Mensaje
        Mensaje = mensaje

    def setL(self, l):
        global L
        L = l

    def setB(self, b):
        global B
        B = b

    def setDicAlfabeto(self, alfabeto):
        global DicAlfabeto
        DicAlfabeto = alfabeto

    def setDecimal(self, decimal):
        global Decimal
        Decimal = decimal

    def setBinario(self, binario):
        global Binario
        Binario = binario

    def setBaseN(self, basen):
        global BaseN
        BaseN = basen

    def getMensaje(self):
        return Mensaje

    def getL(self):
        return L

    def getB(self):
        return B

    def getDicAlfabeto(self):
        return DicAlfabeto

    def getDecimal(self):
        return Decimal

    def getBinario(self):
        return Binario

    def getBaseN(self):
        return BaseN
        