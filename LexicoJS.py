from TokensJS import *
from simpleList import *
import os 
myListTokens = SingleLinkedList()
myListErrors = SingleLinkedList()
myListColores = SingleLinkedList()
flagJS = False
class AnalizadorLexicoJS:
    state = 0
    auxLex = ""
    column = 0
    row = 1
    caracter = ""
    contID = 0
    flagJS = False



    def VerifyReservedToken(self):
        if self.auxLex == "var":
            return "RESERVADA"
        elif self.auxLex == "if":
            return "RESERVADA"
        elif self.auxLex == "console":
            return "RESERVADA"
        elif self.auxLex == "log":
            return "RESERVADA"
        elif self.auxLex == "else":
            return "RESERVADA"
        elif self.auxLex == "for":
            return "RESERVADA"
        elif self.auxLex == "while":
            return "RESERVADA"
        elif self.auxLex == "do":
            return "RESERVADA"
        elif self.auxLex == "continue":
            return "RESERVADA"
        elif self.auxLex == "true":
            return "BOOLEAN"
        elif self.auxLex == "false":
            return "BOOLEAN"
        elif self.auxLex == "break":
            return "RESERVADA"
        elif self.auxLex == "return":
            return "RESERVADA"
        elif self.auxLex == "funtion":
            return "RESERVADA"
        elif self.auxLex == "this":
            return "RESERVADA"
        elif self.auxLex == "constructor":
            return "RESERVADA"
        elif self.auxLex == "class":
            return "RESERVADA"
        elif self.auxLex == "pow":
            return "RESERVADA"
        elif self.auxLex == "Math":
            return "RESERVADA"
        else:
            return "ID"
    
    def analizadorColoresJS(self,entra):
        entra += "#"
        aux = ''
        ruta = ''
        for i, c in enumerate(entra):
            self.letra = entra[i]
            if self.state == 0:

                if c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.state = 0
                    self.auxLex += c
                    self.addColores("ESPACIOS")
                
                elif c == '\n':
                    self.row += 1
                    self.state = 0
                    self.column = 0
                    self.auxLex += c
                    self.addColores("ESPACIOS")

                elif c.isalpha():
                    aux = entra[i+1]
                    self.auxLex += c
                    self.state = 1
                    self.column += 1
                    if(not (aux.isalpha())):
                        aux1 = self.VerifyReservedToken()
                        self.addColores(aux1)
                        
                elif c.isdigit():
                    aux = entra[i+1]
                    self.auxLex += c
                    self.state = 2
                    self.column += 1
                    
                    if (not aux.isnumeric()):
                        
                        self.addColores(NUMEROS)
                
                elif c == '*':
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "="):
                        self.addColores("OPERADORES")
                    elif aux == "=":
                        self.state = 22
                
                elif c == chr(92):
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OPERADORES")
                
                elif c == "=":
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OPERADORES")
                
                elif c == "'":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "'"):
                        self.state = 3
                    elif aux == "'":
                        self.state = 4

                elif c == "(":
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OTROS")

                elif c == ")":
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OTROS")

                elif c == ">":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "="):
                        self.addColores("OPERADORES")
                    elif aux == "=":
                        self.state = 21
                
                elif c == "{":
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OTROS")

                elif c == "}":
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OTROS")

                elif c == ".":
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OTROS")
                
                elif c == ";":
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OTROS")
                
                elif c == '"':
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == '"'):
                        self.state = 5
                    elif aux == '"':
                        self.state = 6
                
                elif c == "<":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "="):
                        self.addColores("OPERADORES")
                    elif aux == "=":
                        self.state = 20
                
                elif c == "+":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "+") and not (aux == "="):
                        self.addColores("OPERADORES")
                    elif aux == "+" or aux == "=":
                        self.state = 19

                elif c == "&":
                    aux = entra[i+1]
                    if aux == "&":
                        self.auxLex += c
                        self.column += 1
                        self.state = 18
                    else:
                        self.auxLex += c
                        self.addColores("OTROS")
                    
                    
                
                elif c == "|":
                    self.auxLex += c
                    self.column += 1
                    self.state = 17

                elif c == "/":
                    extra = ""
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "/") and not (aux == "*"):
                        self.addColores("OPERADORES")
                    elif aux == "/":
                        self.state = 7

                    elif aux == "*":
                        self.state = 23

                elif c == "-":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "-"):
                        self.addColores("OPERADORES")
                    elif aux == "-":
                        self.state = 14
                    elif aux == "=":
                        self.state = 15
                
                elif c == ":":
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OTROS")
                
                elif c == ",":
                    self.auxLex += c
                    self.column += 1
                    self.addColores("OTROS")
                
                elif c == "!":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "="):
                        self.addColores("OPERADORES")
                    elif aux == "=":
                        self.state = 16

                else:
                    print(len(entra))
                    if c == "#" and i == (len(entra) - 1):
                        print("se finalizo el analisis lexico")
                    else:
                        self.auxLex += c
                        self.addColores("OTROS")
                          
            
            elif self.state == 1:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 1
                    if(not (aux.isalpha() or aux.isnumeric() or aux == "_")):
                        aux1 = self.VerifyReservedToken()
                        
                        self.addColores(aux1)
                elif c.isnumeric():
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric())):
                        aux1 = self.VerifyReservedToken()
                        
                        self.addColores(aux1)
                elif c == "_":
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric())):
                        aux1 = self.VerifyReservedToken()
                        self.addColores(aux1)
            
            elif self.state == 2:
                aux = entra[i+1]
                if c.isnumeric():
                    self.auxLex += c
                    self.state = 2
                    if (not aux.isnumeric()):
                       
                        self.addColores(NUMEROS)
            
            elif self.state == 3:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 3
                    if(aux == "'"):
                        self.state = 4
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 3
                    if(aux == "'"):
                        self.state = 4
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 3
                elif (  c == chr(33) or c == chr(35) or c == chr(36) or c == chr(37) or c == chr(38) or c == chr(39) or c == chr(40) or c == chr(41) or c == chr(42) 
                     or c == chr(43) or c == chr(44) or c == chr(45) or c == chr(46) or c == chr(47) or c == chr(58) or c == chr(59) or c == chr(60) or c == chr(61)
                     or c == chr(62) or c == chr(63) or c == chr(64) or c == chr(91) or c == chr(92) or c == chr(93) or c == chr(94) or c == chr(95) or c == chr(96)
                     or c == chr(93) or c == chr(94) or c == chr(95)):
                    self.auxLex += c
                    self.state = 3
                    if(aux == "'"):
                        self.state = 4

            elif self.state == 4:
                aux = entra[i+1]
                if c == "'":
                    self.auxLex += c
                    
                    self.addColores("CONT_FOR_CHAR")
            
            elif self.state == 5:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 5
                    if(aux == '"'):
                        self.state = 6
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 5
                    if(aux == '"'):
                        self.state = 6
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 5
                elif (  c == chr(33) or c == chr(35) or c == chr(36) or c == chr(37) or c == chr(38) or c == chr(39) or c == chr(40) or c == chr(41) or c == chr(42) 
                     or c == chr(43) or c == chr(44) or c == chr(45) or c == chr(46) or c == chr(47) or c == chr(58) or c == chr(59) or c == chr(60) or c == chr(61)
                     or c == chr(62) or c == chr(63) or c == chr(64) or c == chr(91) or c == chr(92) or c == chr(93) or c == chr(94) or c == chr(95) or c == chr(96)
                     or c == chr(93) or c == chr(94) or c == chr(95)):
                    self.auxLex += c
                    self.state = 5
                    if(aux == '"'):
                        self.state = 6
            
            elif self.state == 6:
                aux = entra[i+1]
                self.auxLex += c
                self.addColores("CONT_FOR_STRING")
            
            elif self.state == 7:
                if c == "/":
                    self.auxLex += c
                    self.state = 8

            elif self.state == 8:
                if not (c == "\n"):
                    self.auxLex += c
                    ruta += c
                    self.state = 8
                elif "PATHL" in ruta and c == '\n':
                    self.auxLex += c
                    self.addTokens("COMENTARIO_ESPECIAL")
                    self.flagJS = True
                    print(ruta)
                    ruta = ''
                elif "PATHW" in ruta and c == '\n':
                    self.auxLex += c
                    self.addTokens("COMENTARIO_ESPECIAL")
                    self.flagJS = True
                    print(ruta)
                    ruta = ''
                else:
                   self.auxLex += c
                   self.addTokens("COMENTARIOS")

           
            elif self.state == 14:
                if c == "-":
                    self.auxLex += c
                    self.addColores("OPERADORES")
            elif self.state == 15:
                if c == "=":
                    self.auxLex += c
                    self.addColores("OPERADORES")
            elif self.state == 16:
                if c == "=":
                    self.auxLex += c
                    self.addColores("OPERADORES")
            elif self.state == 17:
                if c == "|":
                    self.auxLex += c
                    self.addColores("OPERADORES")
            elif self.state == 18:
                if c == "&":
                    self.auxLex += c
                    self.addColores("OPERADORES")
            elif self.state == 19:
                if c == "+":
                    self.auxLex += c
                    self.addColores("OPERADORES")
                elif c == "=":
                    self.auxLex += c
                    self.addColores("OPERADORES")
            elif self.state == 20:
                if c == "=":
                    self.auxLex += c
                    self.addColores("OPERADORES")
            elif self.state == 21:
                self.auxLex += c
                self.addColores("OPERADORES")
            elif self.state == 22:
                self.auxLex += c
                self.addColores("OPERADORES")
            elif self.state == 23:
                if c == "*":
                    self.auxLex += c
                    self.state = 24
            
            elif self.state == 24:
                if not (c == '*'):
                    self.auxLex += c
                    self.state = 24
                else:
                    self.auxLex += c
                    self.state = 25
                                 
            elif self.state == 25:
                if not (c == "/"):
                    self.auxLex += c
                    self.state = 25
                else:
                    self.auxLex += c
                    self.addColores("COMENTARIOS")
            
    def analizadorJS(self,entra):
        self.auxLex = ""
        entra += "#"
        aux = ''
        extra = ''
        ruta = ''
        for i, c in enumerate(entra):
            self.letra = entra[i]

            if self.state == 0:

                if c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.state = 0
                    self.auxLex += c
                    self.addTokens("ESPACIOS")
                elif c == '\n':
                    self.row += 1
                    self.state = 0
                    self.column = 0
                    self.auxLex += c
                    self.addTokens("ESPACIOS")

                elif c.isalpha():
                    aux = entra[i+1]
                    self.auxLex += c
                    self.state = 1
                    self.column += 1
                    if(not (aux.isalpha() or aux.isnumeric())):
                        aux1 = self.VerifyReservedToken()
                        self.addTokens(aux1)
                elif c.isdigit():
                        
                    aux = entra[i+1]
                    self.auxLex += c
                    self.state = 2
                    self.column += 1
                    
                    if (not aux.isnumeric()):
                        
                        self.addTokens(NUMEROS)
                
                elif c == '*':
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "="):    
                        self.addTokens("OPERADORES")
                    elif aux == "=":
                        self.state = 22
                
                elif c == chr(92):
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OPERADORES")
                
                elif c == "=":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OPERADORES")
                
                elif c == "'":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "'"):
                        self.state = 3
                    elif aux == "'":
                        self.state = 4

                elif c == "(":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OTROS")

                elif c == ")":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OTROS")

                elif c == ">":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "="):
                        self.addTokens("OPERADORES")
                    elif aux == "=":
                        self.state = 21
                
                elif c == "{":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OTROS")

                elif c == "}":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OTROS")

                elif c == ".":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OTROS")
                
                elif c == ";":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OTROS")
                
                elif c == '"':
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == '"'):
                        self.state = 5
                    elif aux == '"':
                        self.state = 6
                
                elif c == "<":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "="):
                        self.addTokens("OPERADORES")
                    elif aux == "=":
                        self.state = 20
                
                elif c == "+":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "+") and not (aux == "="):
                        self.addTokens("OPERADORES")
                    elif aux == "+" or aux == "=":
                        self.state = 19

                elif c == "&":
                    aux = entra[i+1]
                    if aux == "&":
                        self.auxLex += c
                        self.column += 1
                        self.state = 18
                    else:
                        self.auxLex += c
                        self.addTokensErros()
                        
                elif c == "|":
                    self.auxLex += c
                    self.column += 1
                    self.state = 17

                elif c == "/":
                    extra = ""
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "/") and not (aux == "*"):
                        self.addTokens("OPERADORES")
                    elif aux == "/":
                        self.state = 7

                    elif aux == "*":
                        self.state = 23

                elif c == "-":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "-"):
                        self.addTokens("OPERADORES")
                    elif aux == "-":
                        self.state = 14
                    elif aux == "=":
                        self.state = 15
                
                elif c == ":":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OTROS")
                
                elif c == ",":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OTROS")
                
                elif c == "!":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "="):
                        self.addTokens("OPERADORES")
                    elif aux == "=":
                        self.state = 16

                else:
                      if c == "#" and i == (len(entra)-1):
                          print("se finalizo el analisis lexico")
                      else:
                          self.auxLex += c
                          self.addTokensErros()
                          
            
            elif self.state == 1:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 1
                    if(not (aux.isalpha() or aux.isnumeric() or aux == "_")):
                        aux1 = self.VerifyReservedToken()
                        
                        self.addTokens(aux1)
                elif c.isnumeric():
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric()) or aux == "_"):
                        aux1 = self.VerifyReservedToken()
                        
                        self.addTokens(aux1)
                elif c == "_":
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric()) or aux == "_"):
                        aux1 = self.VerifyReservedToken()
                        self.addTokens(aux1)
            
            elif self.state == 2:
                aux = entra[i+1]
                if c.isnumeric():
                    self.auxLex += c
                    self.state = 2
                    if (not aux.isnumeric()):
                       
                        self.addTokens(NUMEROS)
            
            elif self.state == 3:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 3
                    if(aux == "'"):
                        self.state = 4
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 3
                    if(aux == "'"):
                        self.state = 4
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 3
                elif (  c == chr(33) or c == chr(35) or c == chr(36) or c == chr(37) or c == chr(38) or c == chr(39) or c == chr(40) or c == chr(41) or c == chr(42) 
                     or c == chr(43) or c == chr(44) or c == chr(45) or c == chr(46) or c == chr(47) or c == chr(58) or c == chr(59) or c == chr(60) or c == chr(61)
                     or c == chr(62) or c == chr(63) or c == chr(64) or c == chr(91) or c == chr(92) or c == chr(93) or c == chr(94) or c == chr(95) or c == chr(96)
                     or c == chr(93) or c == chr(94) or c == chr(95)):
                    self.auxLex += c
                    self.state = 3
                    if(aux == "'"):
                        self.state = 4

            elif self.state == 4:
                aux = entra[i+1]
                if c == "'":
                    self.auxLex += c
                    
                    self.addTokens("CONT_FOR_CHAR")
            
            elif self.state == 5:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 5
                    if(aux == '"'):
                        self.state = 6
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 5
                    if(aux == '"'):
                        self.state = 6
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 5
                elif (  c == chr(33) or c == chr(35) or c == chr(36) or c == chr(37) or c == chr(38) or c == chr(39) or c == chr(40) or c == chr(41) or c == chr(42) 
                     or c == chr(43) or c == chr(44) or c == chr(45) or c == chr(46) or c == chr(47) or c == chr(58) or c == chr(59) or c == chr(60) or c == chr(61)
                     or c == chr(62) or c == chr(63) or c == chr(64) or c == chr(91) or c == chr(92) or c == chr(93) or c == chr(94) or c == chr(95) or c == chr(96)
                     or c == chr(93) or c == chr(94) or c == chr(95)):
                    self.auxLex += c
                    self.state = 5
                    if(aux == '"'):
                        self.state = 6
            
            elif self.state == 6:
                aux = entra[i+1]
                self.auxLex += c
                self.addTokens("CONT_FOR_STRING")
            
            elif self.state == 7:
                if c == "/":
                    self.auxLex += c
                    self.state = 8

            elif self.state == 8:
                if not (c == "\n"):
                    self.auxLex += c
                    ruta += c
                    self.state = 8
                elif "PATHL" in ruta and c == '\n':
                    self.auxLex += c
                    self.addTokens("COMENTARIO_ESPECIAL")
                    
                    flagJS = True
                    ruta = ''
                elif "PATHW" in ruta and c == '\n':
                    self.auxLex += c
                    self.addTokens("COMENTARIO_ESPECIAL")
                    flagJS = True
                    
                    ruta = ''
                else:
                   self.auxLex += c
                   self.addTokens("COMENTARIOS")
               
            elif self.state == 14:
                if c == "-":
                    self.auxLex += c
                    self.addTokens("OPERADORES")
            elif self.state == 15:
                if c == "=":
                    self.auxLex += c
                    self.addTokens("OPERADORES")
            elif self.state == 16:
                if c == "=":
                    self.auxLex += c
                    self.addTokens("OPERADORES")
            elif self.state == 17:
                if c == "|":
                    self.auxLex += c
                    self.addTokens("OPERADORES")
            elif self.state == 18:
                if c == "&":
                    self.auxLex += c
                    self.addTokens("OPERADORES")
            elif self.state == 19:
                if c == "+":
                    self.auxLex += c
                    self.addTokens("OPERADORES")
                elif c == "=":
                    self.auxLex += c
                    self.addTokens("OPERADORES")
            elif self.state == 20:
                if c == "=":
                    self.auxLex += c
                    self.addTokens("OPERADORES")
            elif self.state == 21:
                self.auxLex += c
                self.addTokens("OPERADORES")
            elif self.state == 22:
                self.auxLex += c
                self.addTokens("OPERADORES")
            elif self.state == 23:
                if c == "*":
                    self.auxLex += c
                    self.state = 24
            
            elif self.state == 24:
                if not (c == '*'):
                    self.auxLex += c
                    self.state = 24
                else:
                    self.auxLex += c
                    self.state = 25
                                 
            elif self.state == 25:
                if not (c == "/"):
                    self.auxLex += c
                    self.state = 25
                else:
                    self.auxLex += c
                    self.addTokens("COMENTARIOS")
        self.addTokens("SIMBOLOACEPTACION")
    
    def addTokens(self, Type):
        myListTokens.InsertEnd(TokensJS(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0

    def Graficar(self):
        a = open('AutomataJS.dot',"w")
        a.write('digraph finite_state_machine {\n\t')
        a.write('rankdir=LR;\n\t')
        a.write('size=\"8,5\"\n\t')
        a.write('graph[bgcolor = lemonchiffon1, label=\"AFD\"];\n\t')
        a.write('node [shape=record];a [label="{ <data> Expresiones Regulares\\nIdentificador: ID(ID\|Digito)*\\nNumeros o Decimal: Digito+(.Digito+)?\\nComentario Unilinea: (//)(any)*(line break)}"];\n\t')
        a.write('node [shape = doublecircle,fillcolor=olivedrab1,style=filled,fixedsize=true]; S1, S3, S4, S7;\n\t')
        a.write('node [shape= rarrow,fillcolor=gold,style=filled]; start; \n\t')
        a.write('node [shape = circle,fillcolor=white,style=filled];\n\t')
        a.write('start -> S0;\n\t')
        a.write('S0 -> S1 [label = \"Digito\" ];\n\t')
        a.write('S1 -> S1 [ label = \"Digito\" ];\n\t')
        a.write('S1 -> S2 [ label = \".\" ];\n\t')
        a.write('S2 -> S3 [ label = \"Digito\"];\n\t')
        a.write('S3 -> S3 [ label = \"Digito\"];\n\t')
        a.write('S0 -> S4 [ label = \"ID\"];\n\t')
        a.write('S4 -> S4 [ label = \"ID, Digito\"];\n\t')
        a.write('S0 -> S5 [label = \"/\"];\n\t')
        a.write('S5 -> S6 [label = \"/\"];\n\t')
        a.write('S6 -> S6 [label = \"any content\"];\n\t')
        a.write('S6 -> S7 [label = \"line break\"];\n')
        a.write('}')
        a.close()
        os.system('dot -Tpdf AutomataJS.dot -o AutomataJS.pdf')
        os.system('xdg-open AutomataJS.pdf')
    def addColores(self, Type):
        myListColores.InsertEnd(TokensJS(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0

    def addTokensErros(self):
        myListErrors.InsertEnd(TokensJS(self.auxLex,"CARACTER DESCONOCIDO",self.column,self.row))
        self.auxLex = ""
        self.state = 0
    






def reportHTMLTokens():
        xa = myListTokens.headval
        counter = 1
        with open('ReportTokensJS.html', 'w') as myFile:
            myFile.write('<html>')
            myFile.write('<body bgcolor=#1DF1F9>')
            myFile.write('<Center><h1>ANALIZADOR LEXICO JS</h1></Center>')
            myFile.write('<Center><TABLE border = 3.5 bordercolor = black bgcolor = #B4F91D></Center>')
            myFile.write('<TR>')
            myFile.write('<Center><TH COLSPAN = 4 > Tabla de Tokens Validos </TH></Center>')
            myFile.write('</TR>')
            myFile.write('<TR>')
            myFile.write('<TH> ID </TH>')
            myFile.write('<TH> TOKEN </TH>')
            myFile.write('<TH> Lexema </TH>')
            myFile.write('<TH> Columna </TH>')
            myFile.write('<TH> Fila </TH>')
            myFile.write('</TR>')
            while xa is not None:
                myFile.write('<TR>')
                myFile.write('<TH> ' + str(counter) + ' </TH>')
                myFile.write('<TH> ' + xa.getToken().getTipo() + ' </TH>')
                myFile.write('<TH> ' + xa.getToken().getLex() + ' </TH>')
                myFile.write('<TH> ' + str(xa.getToken().getColumna()) + ' </TH>')
                myFile.write('<TH> ' + str(xa.getToken().getFila()) + ' </TH>')
                myFile.write("</TR>");
                counter += 1
                xa = xa.next
            myFile.write('</body>')
            myFile.write('</html>')
        os.system('xdg-open ReportTokensJS.html') 

def reportHTMLTokensErrors():
    printval = myListErrors.headval
    counter = 1
    with open('ReportTokensErrosJS.html', 'w') as myFile:
            myFile.write('<html>')
            myFile.write('<body bgcolor=yellow>')
            myFile.write('<Center><h1>ANALIZADOR LEXICO JS ERRORES</h1></Center>')
            myFile.write('<Center><TABLE border = 3.5 bordercolor = black bgcolor = red ></Center>')
            myFile.write('<TR>')
            myFile.write('<Center><TH COLSPAN = 4 > Tabla de Tokens Invalidos </TH></Center>')
            myFile.write('</TR>')
            myFile.write('<TR>')
            myFile.write('<TH> ID < </TH>')
            myFile.write('<TH> TOKEN </TH>')
            myFile.write('<TH> Lexema </TH>')
            myFile.write('<TH> Columna </TH>')
            myFile.write('<TH> Fila </TH>')
            myFile.write('</TR>')
            while printval is not None:
                myFile.write('<TR>')
                myFile.write('<TH> ' + str(counter) + ' </TH>')
                myFile.write('<TH> ' + printval.getToken().tipo + ' </TH>')
                myFile.write('<TH> ' + printval.getToken().lex + ' </TH>')
                myFile.write('<TH> ' + str(printval.getToken().columna) + ' </TH>')
                myFile.write('<TH> ' + str(printval.getToken().fila) + ' </TH>')
                myFile.write("</TR>");
                counter += 1
                printval = printval.next
            myFile.write('</body>')
            myFile.write('</html>')
    os.system('xdg-open ReportTokensErrosJS.html')

