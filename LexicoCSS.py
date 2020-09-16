from Error import * 
from simpleList import * 
from TokensCSS import *
from Bitacora import * 
listTokensLCSS = SingleLinkedList()
listTokensECSS = SingleLinkedList()
listReportBCSS = SingleLinkedList()

class AnalizadorLexicoCSS:
    state = 0
    auxLex = ""
    column = 0
    row = 0
    chain = ""
    myIterator = 0
    auxState = 1
    def VerifyReservedToken(self):
        if self.auxLex.lower() == "color".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "background-color".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "background-image":
            return "RESERVADA"
        elif self.auxLex.lower() == "border".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "Opacity".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "background".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "text-align".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "font-family".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "font-style".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "font-weight".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "font-size".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "font".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "padding-left".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "padding-right".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "padding-bottom".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "padding-top".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "padding".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "display".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "line-height".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "width".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "height".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "margin-top".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "margin-right".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "margin-bottom".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "margin-left".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "margin".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "border-style".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "display".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "position".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "bottom".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "top".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "right".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "left".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "float".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "clear".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "max-width".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "min-width".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "max-height".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "min-height".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "content".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "url".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "rgba".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "inline-block".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "relative".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "px".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "rem".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "em".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "vh".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "vw".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "in".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "cm".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "mm".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "pt".lower():
            return "RESERVADA"
        elif self.auxLex.lower() == "pc".lower():
            return "RESERVADA"
        else:
            return "ID"
    def AnalizadorCSS(self,entra):
        entra += "~"
        aux = ""
        self.auxLex = "ESTADO INICIAL"
        self.ReportBitacora(0,self.myIterator,False)
        self.auxLex = ""
        for i, c in enumerate(entra):
            if self.state == 0:
                if c == "\t" or c == "\r" or c == "\b" or c == "\f" or c == " ":
                    self.state = 0
                elif c == "\n":
                    self.row += 1
                    self.column = 0
                    self.state = 0
                
                elif c == "/":
                    extra = ""
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "*"):
                        self.myIterator += 1
                        self.ReportBitacora(21,self.myIterator,True)
                        self.myIterator = 0
                        self.addTokens("OPERADOR")
                        self.auxLex = "ESTADO INICIAL"
                        self.ReportBitacora(0,self.myIterator,False)
                        self.auxLex = ""
                    elif aux == "*":
                        self.myIterator += 1
                        self.ReportBitacora(1,self.myIterator,False)
                        self.state = 1
             
                elif c == "*":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(11,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OPERADOR")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""
               
                elif c == "{":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(12,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OTROS")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""

                elif c == "}":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(13,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OTROS")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""

                elif c == ":":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(14,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OTROS")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""


                elif c == ";":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(15,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OTROS")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""

                elif c == ",":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(16,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OTROS")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""

                elif c == "(":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(17,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OPERADOR")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""


                elif c == ")":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(18,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OPERADOR")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""

                elif c == "-":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(6,self.myIterator,False)
                    self.state = 6

                elif c.isalpha():
                    aux = entra[i+1]
                    self.column += 1
                    self.auxLex += c
                    if(not (aux.isalpha())):
                        self.myIterator += 1
                        self.ReportBitacora(4,self.myIterator,True)
                        self.myIterator = 0
                        aux1 = self.VerifyReservedToken()
                        self.addTokens(aux1)
                        self.auxLex = "ESTADO INICIAL"
                        self.ReportBitacora(0,self.myIterator,False)
                        self.auxLex = ""
                    else:
                        self.state = 4
                        self.myIterator += 1
                        self.ReportBitacora(4,self.myIterator,False)

                elif c.isnumeric():
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if aux == ".":
                        self.state = 6
                    elif not(aux.isnumeric()):
                        self.myIterator += 1
                        self.ReportBitacora(6,self.myIterator,True)
                        self.myIterator = 0
                        self.addTokens("NUMEROS")
                        self.auxLex = "ESTADO INICIAL"
                        self.ReportBitacora(0,self.myIterator,False)
                        self.auxLex = ""
                    else:
                        self.state = 6
                        self.myIterator += 1
                        self.ReportBitacora(6,self.myIterator,False)
                
                elif c == "#":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(19,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OTROS")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""

                
                elif c == '"':
                    self.auxLex += c
                    self.column += 1
                    self.state = 9
                    self.myIterator += 1
                    self.ReportBitacora(9,self.myIterator,False)
              
                elif c == ".":
                    self.auxLex += c
                    self.column += 1
                    self.myIterator += 1
                    self.ReportBitacora(20,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("OTROS")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""

            
                else:
                    if c == "~" and i == (len(entra)-1):
                        print("se finalizo el analisis lexico")
                    else:
                        self.auxLex += c
                        self.addErrors("DESCONOCIDO")
         
            elif self.state == 1:
                if c == "*":
                    self.auxLex += c
                    self.state = 2
                    self.myIterator += 1
                    self.ReportBitacora(2,self.myIterator,False)
            
            elif self.state == 2:
                if not (c == '*'):
                    self.auxLex += c
                    self.state = 2
                    self.myIterator += 1
                    self.ReportBitacora(2,self.myIterator,False)
                else:
                    self.auxLex += c
                    self.state = 3
                    self.myIterator += 1
                    self.ReportBitacora(2,self.myIterator,False)
                                 
            elif self.state == 3:
                if not (c == "/"):
                    self.auxLex += c
                    self.state = 3
                    self.myIterator += 1
                    self.ReportBitacora(3,self.myIterator,False)
                else:
                    self.auxLex += c
                    self.myIterator += 1
                    self.ReportBitacora(3,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("COMENTARIOS")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""
            
            elif self.state == 4:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 4
                    if(aux == "-"):
                        self.state = 4
                        self.myIterator += 1
                        self.ReportBitacora(4,self.myIterator,False)
                    elif(not (aux.isalpha() or aux.isnumeric() or aux == "-")):
                        self.myIterator += 1
                        self.ReportBitacora(4,self.myIterator,True)
                        self.myIterator = 0
                        aux1 = self.VerifyReservedToken()
                        self.addTokens(aux1)
                        self.auxLex = "ESTADO INICIAL"
                        self.ReportBitacora(0,self.myIterator,False)
                        self.auxLex = ""
                    else:
                        self.myIterator += 1
                        self.ReportBitacora(4,self.myIterator,False)
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 4
                    if(not (aux.isalpha() or aux.isnumeric())):
                        self.myIterator += 1
                        self.ReportBitacora(4,self.myIterator,True)
                        self.myIterator = 0
                        aux1 = self.VerifyReservedToken()
                        self.addTokens(aux1)
                        self.auxLex = "ESTADO INICIAL"
                        self.ReportBitacora(0,self.myIterator,False)
                        self.auxLex = ""
                    else:
                        self.myIterator += 1
                        self.ReportBitacora(4,self.myIterator,False)
                elif c == "-":
                    self.auxLex += c
                    self.state = 5
                    self.myIterator += 1
                    self.ReportBitacora(5,self.myIterator,False)
            
            elif self.state == 5:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 5
                    if(not (aux.isalpha())):
                        self.myIterator += 1
                        self.ReportBitacora(5,self.myIterator,True)
                        self.myIterator = 0
                        aux1 = self.VerifyReservedToken()
                        self.addTokens(aux1)
                        self.auxLex = "ESTADO INICIAL"
                        self.ReportBitacora(0,self.myIterator,False)
                        self.auxLex = ""
                    else:
                        self.myIterator += 1
                        self.ReportBitacora(5,self.myIterator,False)
                        
            
            elif self.state == 6:
                aux = entra[i+1]
                if c.isnumeric():
                    self.auxLex += c
                    self.state = 6
                    if aux == ".":
                        self.state = 6
                    elif aux == "%":
                        self.state = 8
                        self.myIterator += 1
                        self.ReportBitacora(6,self.myIterator,False)
                    elif not(aux.isnumeric()):
                        self.myIterator += 1
                        self.ReportBitacora(6,self.myIterator,True)
                        self.myIterator = 0
                        self.addTokens("NUMEROS")
                        self.auxLex = "ESTADO INICIAL"
                        self.ReportBitacora(0,self.myIterator,False)
                        self.auxLex = ""
                    else:
                        self.myIterator += 1
                        self.ReportBitacora(6,self.myIterator,False)
                elif c == ".":
                    self.auxLex += c
                    self.state = 7
                    self.myIterator += 1
                    self.ReportBitacora(7,self.myIterator,False)

            elif self.state == 7:
                aux = entra[i+1]
                if c.isnumeric():
                    self.auxLex += c
                    self.state = 7
                    if aux == "%":
                        self.state = 8
                    elif (not (aux.isnumeric())):
                        self.myIterator += 1
                        self.ReportBitacora(7,self.myIterator,False)
                        self.myIterator = 0
                        self.addTokens("NUMEROS")
                        self.auxLex = "ESTADO INICIAL"
                        self.ReportBitacora(0,self.myIterator,False)
                        self.auxLex = ""
                    else:
                        self.myIterator += 1
                        self.ReportBitacora(7,self.myIterator,False)
            
           
            elif self.state == 8:
                if c == "%":
                    self.auxLex += c
                    self.myIterator += 1
                    self.ReportBitacora(8,self.myIterator,True)
                    self.myIterator = 0
                    self.addTokens("PORCENTAJE")
                    self.auxLex = "ESTADO INICIAL"
                    self.ReportBitacora(0,self.myIterator,False)
                    self.auxLex = ""
            
            
            elif self.state == 9:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 9
                    self.myIterator += 1
                    self.ReportBitacora(9,self.myIterator,False)
                    if(aux == '"'):
                        self.state = 10
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 9
                    self.myIterator += 1
                    self.ReportBitacora(9,self.myIterator,False)
                    if(aux == '"'):
                        self.state = 10
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 9
                    self.myIterator += 1
                    self.ReportBitacora(9,self.myIterator,False)
                elif (  c == chr(33) or c == chr(35) or c == chr(36) or c == chr(37) or c == chr(38) or c == chr(39) or c == chr(40) or c == chr(41) or c == chr(42) 
                     or c == chr(43) or c == chr(44) or c == chr(45) or c == chr(46) or c == chr(47) or c == chr(58) or c == chr(59) or c == chr(60) or c == chr(61)
                     or c == chr(62) or c == chr(63) or c == chr(64) or c == chr(91) or c == chr(92) or c == chr(93) or c == chr(94) or c == chr(95) or c == chr(96)
                     or c == chr(93) or c == chr(94) or c == chr(95)):
                    self.auxLex += c
                    self.state = 9
                    self.myIterator += 1
                    self.ReportBitacora(9,self.myIterator,False)
                    if(aux == '"'):
                        self.state = 10
            
            elif self.state == 10:
                self.auxLex += c
                self.myIterator += 1
                self.ReportBitacora(10,self.myIterator,True)
                self.myIterator = 0 
                self.addTokens("CONT_FOR_STRING")     
                self.auxLex = "ESTADO INICIAL"
                self.ReportBitacora(0,self.myIterator,False)
                self.auxLex = ""
           
    def ReportBitacora(self,state,iteracion,aceptacion):
        listReportBCSS.InsertEnd(Bitacora(state,self.auxLex,iteracion,aceptacion))


    def addTokens(self, Type):
        listTokensLCSS.InsertEnd(TokensCSS(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0

    def addErrors(self,Type):
        listTokensECSS.InsertEnd(TokensCSS(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0

    def ReportTokensCSS(self):
        printval = listTokensLCSS.headval
        counter = 1
        with open('ReportTokensCSS.html', 'w') as myFile:
            myFile.write('<!DOCTYPE html>\n')
            myFile.write('<html lang="en">\n')
            myFile.write('<head>\n')
            myFile.write('\t<title>Report Tokens CSS</title>\t\n')
            myFile.write('<meta charset="utf-8">\n\t')
            myFile.write('<meta name="viewport" content="width=device-width, initial-scale=1">\n\t')
            myFile.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n\t')
            myFile.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n\t')
            myFile.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n\t')
            myFile.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n\t')
            myFile.write('</head>\n\t')
            myFile.write('<body>\n\t')
            myFile.write('<div class="container">\n\t')
            myFile.write('<h1 style="text-align: center;">Report Tokens CSS</h1>\n\t')
            myFile.write('<table class="table">\n\t')
            myFile.write('<thead class="thead-dark">\n\t')
            myFile.write('<tr>\n\t')    
            myFile.write('<th>ID</th>')
            myFile.write('<th>Token</th>')
            myFile.write('<th> Lexema </th>')
            myFile.write('<th> Columna </th>')
            myFile.write('<th> Fila </th>')
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

    def ReportTokensErrorCSS(self):
        printval = listTokensECSS.headval
        counter = 1
        with open('ReportTokensCSSError.html', 'w') as myFile:
            myFile.write('<!DOCTYPE html>\n')
            myFile.write('<html lang="en">\n')
            myFile.write('<head>\n')
            myFile.write('\t<title>Report Errors CSS</title>\t\n')
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

    def ReportBitacoraCSS(self):
        printval = listReportBCSS.headval
        counter = 1
        with open('ReportBitacoraCCS.html', 'w') as myFile:
            myFile.write('<!DOCTYPE html>\n')
            myFile.write('<html lang="en">\n')
            myFile.write('<head>\n')
            myFile.write('\t<title>Report Bitacora CSS</title>\t\n')
            myFile.write('<meta charset="utf-8">\n\t')
            myFile.write('<meta name="viewport" content="width=device-width, initial-scale=1">\n\t')
            myFile.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n\t')
            myFile.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>\n\t')
            myFile.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>\n\t')
            myFile.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n\t')
            myFile.write('</head>\n\t')
            myFile.write('<body>\n\t')
            myFile.write('<div class="container">\n\t')
            myFile.write('<h1 style="text-align: center;">Report Bitacora CSS</h1>\n\t')
            myFile.write('<table class="table">\n\t')
            myFile.write('<thead class="thead-dark">\n\t')
            myFile.write('<tr>\n\t') 
            myFile.write('<TH> ID </TH>')
            myFile.write('<TH> ESTADO </TH>')
            myFile.write('<TH> TOKEN/ERROR  </TH>')
            myFile.write('<TH> ITERACIONES </TH>')
            myFile.write('<TH> ESTADO ACEPTACION </TH>')
            myFile.write('</TR>')
            myFile.write('</thead>')
            myFile.write('<tbody>')
            while printval is not None:
                myFile.write('<TR>')
                myFile.write('<TH> ' + str(counter) + ' </TH>')
                myFile.write('<TH> ' + str(printval.getToken().getState()) + ' </TH>')
                myFile.write('<TH> ' + printval.getToken().getTok() + ' </TH>')
                myFile.write('<TH> ' + str(printval.getToken().getIteracion()) + ' </TH>')
                myFile.write('<TH> ' + str(printval.getToken().getAceptacion()) + ' </TH>')
                myFile.write("</TR>");
                counter += 1
                printval = printval.next
            myFile.write('</tbody>')
            myFile.write('</table>')
            myFile.write('</div>')
            myFile.write('</body>')
            myFile.write('</html>')
prueba  = """ .ejemplo{
margin-top: 0;
margin-bottom: 0.5em;
line-height: inherit;
position: relative;
font-size: 75%;
color: #333;
border-top: 2px solid rgba(0, 0, 0, 0.1);
content: "\\2014\\00A0";
position: absolute;
background-image: url("/home/documents/picture.png");
background-color: rgba(220, 53, 69, 0.9);
font: 76% arial, sans-serif;
background: 0 0 0 0.2rem rgba(51, 51, 51, 0.25);

}


"""
lexio = AnalizadorLexicoCSS()
lexio.AnalizadorCSS(prueba)
listReportBCSS.listPrint()
lexio.ReportBitacoraCSS()
lexio.ReportTokensCSS()
lexio.ReportTokensErrorCSS()