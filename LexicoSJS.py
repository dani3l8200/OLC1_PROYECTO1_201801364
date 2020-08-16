from TokensJS import *
from simpleList import * 
from SintacticoJS import *

listTokensL = SingleLinkedList()
listTokensE = SingleLinkedList()
class AnalizadorLexicoOJS:
    state = 0
    auxLex = ""
    column = 0
    row = 0
    def AnalizadorJS(self,entra):
        entra += "#"
        aux = ""
        for i, c in enumerate(entra):
            if self.state == 0:
                if c == "\t" or c == "\r" or c == "\b" or c == "\f" or c == " ":
                    self.state = 0
                elif c == "\n":
                    self.row += 1
                    self.column = 0
                    self.state = 0
                elif c.isalpha():
                    aux = entra[i+1]
                    self.auxLex += c
                    self.state = 1
                    self.column += 1
                    if(not (aux.isalpha())):
                        self.addTokens(ID)
                elif c.isnumeric():
                    aux = entra[i+1]
                    self.auxLex += c
                    self.state = 2
                    self.column += 1
                    if aux == ".":
                        self.state = 2
                    elif not(aux.isnumeric()):
                        self.addTokens(NUMEROS)

                elif c == "+":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_MAS)
                elif c == "-":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_MENOS)
                elif c == "*":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_ASTERISCO)
                elif c == "/":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_DIAGONAL)
                elif c == "(":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_PARENTESIS_A)
                elif c == ")":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_PARENTESIS_C)
                elif c == ";":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_PUNTOCOMA)
                else:
                    if c == "#":
                        print("se finalizo el analisis lexico")
                    else:
                        self.auxLex += c
                        self.addErrors("DESCONOCIDO")
            elif self.state == 1:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 1
                    if(not (aux.isalpha() or aux.isnumeric())):
                        self.addTokens(ID)
                elif c.isnumeric():
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric())):
                        self.addTokens(ID)
            elif self.state == 2:
                aux = entra[i+1]
                if c.isnumeric():
                    self.auxLex += c
                    self.state = 2
                    if aux == ".":
                        self.state = 2
                    elif not(aux.isnumeric()):
                        self.addTokens(NUMEROS)
                elif c == ".":
                    self.auxLex += c
                    self.state = 3
            elif self.state == 3:
                aux = entra[i+1]
                if c.isnumeric():
                    self.auxLex += c
                    self.state = 3
                    if (not (aux.isnumeric())):
                        self.addTokens("DECIMAL")
        self.addTokens("SIMBOLOACEPTACION")
        

    def addTokens(self, Type):
        listTokensL.InsertEnd(TokensJS(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0
    def addErrors(self,Type):
        listTokensE.InsertEnd(TokensJS(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0

tes = """5.5+(4.4-2.3)*0.5\n
7.36+(5.12/2.00)-(3.16*2.00))\n3.14*10.20+5.20/2.60\n(10*5)-(45/3)+5\n(num*1)"""
prueba = AnalizadorLexicoOJS()
prueba.AnalizadorJS(tes)
listTokensL.listPrint()
listTokensE.listPrint()
sintacti = SintacticoJS(listTokensL)
sintacti.ReportHTMLSintactico()