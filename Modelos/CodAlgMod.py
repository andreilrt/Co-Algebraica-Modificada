from Controlador.Controlador import Controlador
class CodAlgMod:
    controlador = Controlador()
    def mensaje2basen(self):
        BaseN = '0.'
        mensaje = self.controlador.getMensaje()
        mensaje = mensaje.lower()
        dicAlfabeto = self.controlador.getDicAlfabeto()
        for l in mensaje:
            BaseN = BaseN + str(dicAlfabeto[l])
        BaseN = float(BaseN)
        self.controlador.setBaseN(BaseN)

    def basen2decimal(self):
        B = self.controlador.getB()
        l = str(self.controlador.getBaseN())
        l = l[2:len(l)]
        decimal = 0.0
        x = 0
        while x < len(l):
            decimal = float(l[x])*float(pow(B,-(x+1))) + decimal
            x = x + 1
        self.controlador.setDecimal(decimal)

    def decimal2binario(self):
        dec = self.controlador.getDecimal()
        dec2 = dec
        val = 0
        ent = 0
        bina = '0.'
        i = 1
        while val < dec:
            dec2 = dec2*2
            ent = int(dec2)
            bina = bina + str(ent)
            dec2 = dec2 - ent
            val = round(((pow(2, -i))*ent) + val, len(str(dec))-1)
            i=i+1
        self.controlador.setBinario(bina)

