from TokensJS import *
from simpleList import * 
from SintacticoJS import *

listTokensLSintactico = SingleLinkedList()
listTokensESintactico = SingleLinkedList()
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
                    self.addTokens("NUEVA_EXPRESION")
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
                    if(not (aux.isalpha() or aux.isnumeric()) or aux == "_"):
                        self.addTokens(ID)
                elif c.isnumeric():
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric()) or aux == "_"):
                        self.addTokens(ID)
                elif c == "_":
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric()) or aux == "_"):
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
        listTokensLSintactico.InsertEnd(TokensJS(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0
    def addErrors(self,Type):
        listTokensESintactico.InsertEnd(TokensJS(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0

tes = """(121)(3121)"""
prueba = AnalizadorLexicoOJS()
prueba.AnalizadorJS(tes)
x = tes.split("\n")
listTokensLSintactico.listPrint()
listTokensESintactico.listPrint()
sintacti = SintacticoJS(listTokensLSintactico)
listErrorSintactico.listPrint()
sintacti.ReportHTMLSintactico()
