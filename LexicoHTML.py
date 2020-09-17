from Error import *
from simpleList import *
from TokensHTML import * 
import os 
listTokensLHTML = SingleLinkedList()
listTokensEHTML = SingleLinkedList()
listTokensCHTML = SingleLinkedList()

class AnalizadorLexicoHTML:
    state = 0
    auxLex = ""
    column = 0
    row = 1
    def VerifyReservedToken(self):
        if self.auxLex.lower() == "HTML".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "HEAD".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "TITLE".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "body".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "p".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "br".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "tfoot".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "tbody".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "thead".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "col".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "colgroup".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "caption".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "td".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "tr".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "th".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "table".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "ol".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "ul".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "li".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "!DOCTYPE".lower():
            return "RESERVADA"
        else:
            return "ID HTML"
    
    def AnalizadorHTML(self,entra):
        entra += "#"
        aux = ""
        aux1 = ""
        for i, c in enumerate(entra):
            if self.state == 0:
                if c == "\t" or c == "\r" or c == "\b" or c == "\f" or c == " ":
                    self.state = 0
                    self.auxLex += c
                    self.addTokens("ESPACIOS")
                elif c == "\n":
                    self.row += 1
                    self.column = 0
                    self.state = 0
                    self.auxLex += c
                    self.addTokens("ESPACIOS")
                elif c.isalpha() or c.isnumeric():
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    self.state = 1
                    if(not (aux.isalpha() or aux.isnumeric())):
                        aux1 = self.VerifyReservedToken()
                        self.addTokens(aux1)
                elif c == "<":
                    aux = entra[i+1]
                    self.auxLex += c 
                    self.column += 1
                    if aux == "!":
                        self.state = 7
                    elif not (aux == "!"):
                        self.addTokens("OPERADOR")
                elif c == ">":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if (aux.isalpha() or aux.isnumeric() or aux == "\t" or aux == "\r" or aux == "\b" or aux == "\f" or aux == " "):
                        self.addTokens("OPERADOR")
                        self.state = 6
                    else: 
                        self.addTokens("OPERADOR")
                elif c == "/":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OPERADOR")
                elif c == '"':
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == '"'):
                        self.state = 2
                    elif aux == '"':
                        self.state = 3
                elif c == "'":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "'"):
                        self.state = 4
                    elif aux == "'":
                        self.state = 5
                elif c == ".":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OPERADOR")
                elif c == "=":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens("OPERADOR")

                else:
                    if c == "#" and i == (len(entra)-1):
                        print("se finalizo el analisis lexico")
                    else:
                        self.auxLex += c
                        self.addErrors("DESCONOCIDO")
            
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
                    if(not (aux.isalpha() or aux.isnumeric())):
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
                if c.isalpha():
                    self.auxLex += c
                    self.state = 2
                    if(aux == '"'):
                        self.state = 3
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 2
                    if(aux == '"'):
                        self.state = 3
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 2
                elif (  c == chr(33) or c == chr(35) or c == chr(36) or c == chr(37) or c == chr(38) or c == chr(39) or c == chr(40) or c == chr(41) or c == chr(42) 
                     or c == chr(43) or c == chr(44) or c == chr(45) or c == chr(46) or c == chr(47) or c == chr(58) or c == chr(59) or c == chr(60) or c == chr(61)
                     or c == chr(62) or c == chr(63) or c == chr(64) or c == chr(91) or c == chr(92) or c == chr(93) or c == chr(94) or c == chr(95) or c == chr(96)
                     or c == chr(93) or c == chr(94) or c == chr(95)):
                    self.auxLex += c
                    self.state = 2
                    if(aux == '"'):
                        self.state = 3
                        
            elif self.state == 3:
                self.auxLex += c
                self.addTokens("CONT_FOR_STRING")

            elif self.state == 4:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 4
                    if(aux == '"'):
                        self.state = 5
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 4
                    if(aux == '"'):
                        self.state = 5
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 4
                elif (  c == chr(33) or c == chr(35) or c == chr(36) or c == chr(37) or c == chr(38) or c == chr(39) or c == chr(40) or c == chr(41) or c == chr(42) 
                     or c == chr(43) or c == chr(44) or c == chr(45) or c == chr(46) or c == chr(47) or c == chr(58) or c == chr(59) or c == chr(60) or c == chr(61)
                     or c == chr(62) or c == chr(63) or c == chr(64) or c == chr(91) or c == chr(92) or c == chr(93) or c == chr(94) or c == chr(95) or c == chr(96)
                     or c == chr(93) or c == chr(94) or c == chr(95)):
                    self.auxLex += c
                    self.state = 4
                    if(aux == '"'):
                        self.state = 5 
            
            elif self.state == 5:
                self.auxLex += c
                self.addTokens("CONT_FOR_CHAR")

            elif self.state == 6:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 6
                    if(aux == '<'):
                        self.addTokens("ID")
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 6
                    if(aux == '<'):
                        self.addTokens("ID")
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 6
                    if aux == '<':
                        self.addTokens("ID")
                elif c.isascii():
                    self.auxLex += c
                    self.state = 6
                    if(aux == '<'):
                        self.addTokens("ID")
            elif self.state == 7:
                aux = entra[i+1]
                if c == "!" and aux == "-":
                    self.auxLex += c
                    self.state = 8
                else:
                    self.addTokens("OPERADOR")
                    self.auxLex += c
                    self.state = 1

            elif self.state == 8:
                if c == "-":
                    self.auxLex += c
                    self.state = 9
            elif self.state == 9:
                if not(c == ">"):
                    self.auxLex += c
                    self.state = 9
                else: 
                    self.auxLex += c
                    self.addTokens("COMENTARIO")

    def ColoresHTML(self,entra):
        entra += "#"
        aux = ""
        aux1 = ""
        for i, c in enumerate(entra):
            if self.state == 0:
                if c == "\t" or c == "\r" or c == "\b" or c == "\f" or c == " ":
                    self.state = 0
                    self.auxLex += c
                    self.addColors("ESPACIOS")
                elif c == "\n":
                    self.row += 1
                    self.column = 0
                    self.state = 0
                    self.auxLex += c
                    self.addColors("ESPACIOS")
                elif c.isalpha() or c.isnumeric():
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    self.state = 1
                    if(not (aux.isalpha() or aux.isnumeric())):
                        aux1 = self.VerifyReservedToken()
                        self.addColors(aux1)
                elif c == "<":
                    aux = entra[i+1]
                    self.auxLex += c 
                    self.column += 1
                    if aux == "!":
                        self.state = 7
                    elif not (aux == "!"):
                        self.addColors("OPERADOR")
                elif c == ">":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if (aux.isalpha() or aux.isnumeric() or aux == "\t" or aux == "\r" or aux == "\b" or aux == "\f" or aux == " "):
                        self.addColors("OPERADOR")
                        self.state = 6
                    else: 
                        self.addColors("OPERADOR")
                elif c == "/":
                    self.auxLex += c
                    self.column += 1
                    self.addColors("OPERADOR")
                elif c == '"':
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == '"'):
                        self.state = 2
                    elif aux == '"':
                        self.state = 3
                elif c == "'":
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "'"):
                        self.state = 4
                    elif aux == "'":
                        self.state = 5
                elif c == ".":
                    self.auxLex += c
                    self.column += 1
                    self.addColors("OPERADOR")
                elif c == "=":
                    self.auxLex += c
                    self.column += 1
                    self.addColors("OPERADOR")

                else:
                    if c == "#" and i == (len(entra)-1):
                        print("se finalizo el analisis lexico")
                    else:
                        self.auxLex += c
                        self.addColors("ERRORES")
            
            elif self.state == 1:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 1
                    if(not (aux.isalpha() or aux.isnumeric() or aux == "_")):
                        aux1 = self.VerifyReservedToken()
                        self.addColors(aux1)
                elif c.isnumeric():
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric())):
                        aux1 = self.VerifyReservedToken()
                        
                        self.addColors(aux1)
                elif c == "_":
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric()) or aux == "_"):
                        aux1 = self.VerifyReservedToken()
                        self.addColors(aux1)

            elif self.state == 2:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 2
                    if(aux == '"'):
                        self.state = 3
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 2
                    if(aux == '"'):
                        self.state = 3
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 2
                elif (  c == chr(33) or c == chr(35) or c == chr(36) or c == chr(37) or c == chr(38) or c == chr(39) or c == chr(40) or c == chr(41) or c == chr(42) 
                     or c == chr(43) or c == chr(44) or c == chr(45) or c == chr(46) or c == chr(47) or c == chr(58) or c == chr(59) or c == chr(60) or c == chr(61)
                     or c == chr(62) or c == chr(63) or c == chr(64) or c == chr(91) or c == chr(92) or c == chr(93) or c == chr(94) or c == chr(95) or c == chr(96)
                     or c == chr(93) or c == chr(94) or c == chr(95)):
                    self.auxLex += c
                    self.state = 2
                    if(aux == '"'):
                        self.state = 3
                        
            elif self.state == 3:
                self.auxLex += c
                self.addColors("CONT_FOR_STRING")

            elif self.state == 4:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 4
                    if(aux == '"'):
                        self.state = 5
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 4
                    if(aux == '"'):
                        self.state = 5
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 4
                elif (  c == chr(33) or c == chr(35) or c == chr(36) or c == chr(37) or c == chr(38) or c == chr(39) or c == chr(40) or c == chr(41) or c == chr(42) 
                     or c == chr(43) or c == chr(44) or c == chr(45) or c == chr(46) or c == chr(47) or c == chr(58) or c == chr(59) or c == chr(60) or c == chr(61)
                     or c == chr(62) or c == chr(63) or c == chr(64) or c == chr(91) or c == chr(92) or c == chr(93) or c == chr(94) or c == chr(95) or c == chr(96)
                     or c == chr(93) or c == chr(94) or c == chr(95)):
                    self.auxLex += c
                    self.state = 4
                    if(aux == '"'):
                        self.state = 5 
            
            elif self.state == 5:
                self.auxLex += c
                self.addColors("CONT_FOR_CHAR")

            elif self.state == 6:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 6
                    if(aux == '<'):
                        self.addColors("ID")
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 6
                    if(aux == '<'):
                        self.addColors("ID")
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 6
                    if aux == '<':
                        self.addTokens("ID")
                elif c.isascii():
                    self.auxLex += c
                    self.state = 6
                    if(aux == '<'):
                        self.addColors("ID")
            elif self.state == 7:
                aux = entra[i+1]
                if c == "!" and aux == "-":
                    self.auxLex += c
                    self.state = 8
                else:
                    self.addColors("OPERADOR")
                    self.auxLex += c
                    self.state = 1

            elif self.state == 8:
                if c == "-":
                    self.auxLex += c
                    self.state = 9
            elif self.state == 9:
                if not(c == ">"):
                    self.auxLex += c
                    self.state = 9
                else: 
                    self.auxLex += c
                    self.addColors("COMENTARIO")

    def addTokens(self,Type):
        listTokensLHTML.InsertEnd(TokensHTML(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0
    
    def addErrors(self,Type):
        listTokensEHTML.InsertEnd(TokensHTML(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0
    
    def addColors(self, Type):
        listTokensCHTML.InsertEnd(TokensHTML(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0

    def ReportLErrorsHTML(self):
        printval = listTokensEHTML.headval
        counter = 1
        with open('ReportTokensHTMLErrorss.html', 'w') as myFile:
            myFile.write('<!DOCTYPE html>\n')
            myFile.write('<html lang="en">\n')
            myFile.write('<head>\n')
            myFile.write('\t<title>Report Errors HTML</title>\t\n')
            myFile.write('<meta charset="utf-8">\n\t')
            myFile.write('<meta name="viewport" content="width=device-width, initial-scale=1">\n\t')
            myFile.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n\t')
            myFile.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n\t')
            myFile.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n\t')
            myFile.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n\t')
            myFile.write('</head>\n\t')
            myFile.write('<body>\n\t')
            myFile.write('<div class="container">\n\t')
            myFile.write('<h1 style="text-align: center;">Report Errors CSS</h1>\n\t')
            myFile.write('<table class="table">\n\t')
            myFile.write('<thead class="thead-dark">\n\t')
            myFile.write('<tr>\n\t') 
            myFile.write('<TH> ID </TH>')
            myFile.write('<TH> Token</TH>')
            myFile.write('<TH> Lexema  </TH>')
            myFile.write('<TH> Columna </TH>')
            myFile.write('<TH> Fila </TH>')
            myFile.write('</TR>')
            myFile.write('</thead>')
            myFile.write('<tbody>')
            while printval is not None:
                myFile.write('<TR>')
                myFile.write('<TH> ' + str(counter) + ' </TH>')
                myFile.write('<TH> ' + printval.getToken().getTipo() + ' </TH>')
                myFile.write('<TH> ' + printval.getToken().getLex() + ' </TH>')
                myFile.write('<TH> ' + str(printval.getToken().getColumna()) + ' </TH>')
                myFile.write('<TH> ' + str(printval.getToken().getFila()) + ' </TH>')
                myFile.write("</TR>");
                counter += 1
                printval = printval.next
            myFile.write('</tbody>')
            myFile.write('</table>')
            myFile.write('</div>')
            myFile.write('</body>')
            myFile.write('</html>')
        os.system('xdg-open ReportTokensHTMLErrorss.html')


