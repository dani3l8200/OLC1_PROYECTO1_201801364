from TokensJS import *
from simpleList import *


myListTokens = SingleLinkedList()
myListErrors = SingleLinkedList()
class AnalizadorLexicoJS:
    state = 0
    auxLex = ""
    column = 0
    row = 1
    caracter = ""
    contID = 0



    def VerifyReservedToken(self):
        if self.auxLex == "var":
            return RESERVADA_var
        elif self.auxLex == "int":
            return RESERVADA_INT
        elif self.auxLex == "string":
            return RESERVADA_STRING
        elif self.auxLex == "char":
            return RESERVADA_CHAR
        elif self.auxLex == "boolean":
            return RESERVADA_BOOLEAN
        elif self.auxLex == "if":
            return RESERVADA_IF
        elif self.auxLex == "console":
            return RESERVADA_CONSOLE
        elif self.auxLex == "log":
            return RESERVADA_LOG
        elif self.auxLex == "else":
            return RESERVADA_ELSE
        elif self.auxLex == "for":
            return RESERVADA_FOR
        elif self.auxLex == "while":
            return RESERVADA_WHILE
        elif self.auxLex == "do":
            return RESERVADA_DO
        elif self.auxLex == "continue":
            return RESERVADA_CONTINUE
        elif self.auxLex == "true":
            return RESERVADA_TRUE
        elif self.auxLex == "false":
            return RESERVADA_FALSE
        elif self.auxLex == "break":
            return RESERVADA_BREAK
        elif self.auxLex == "return":
            return RESERVADA_RETURN
        elif self.auxLex == "funtion":
            return RESERVADA_FUNTION
        elif self.auxLex == "this":
            return RESERVADA_THIS
        elif self.auxLex == "constructor":
            return RESERVADA_CONSTRUCTOR
        elif self.auxLex == "class":
            return RESERVADA_CLASS
        elif self.auxLex == "pow":
            return RESERVADA_POW
        elif self.auxLex == "Math":
            return RESERVADA_MATH
        else:
            return ID
    
    def analizadorJS(self,entra):
        entra += "#"
        aux = ''
        extra = ''
        for i, c in enumerate(entra):
            self.letra = entra[i]

            if self.state == 0:

                if c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.state = 0
                
                elif c == '\n':
                    self.row += 1
                    self.state = 0
                    self.column = 0

                elif c.isalpha():
                    aux = entra[i+1]
                    self.auxLex += c
                    self.state = 1
                    self.column += 1
                    if(not (aux.isalpha())):
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
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_ASTERISCO)
                
                elif c == chr(92):
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_DIAGONALINVERTIDA)
                
                elif c == "=":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_IGUAL)
                
                elif c == "'":
                    self.auxLex += c
                    self.column += 1
                    self.state = 3

                elif c == "(":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_PARENTESIS_A)

                elif c == ")":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_PARENTESIS_C)

                elif c == ">":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_MAYOR)
                
                elif c == "{":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_LLAVE_A)

                elif c == "}":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_LLAVE_C)

                elif c == ".":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_PUNTO)
                
                elif c == ";":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_PUNTOCOMA)
                
                elif c == '"':
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == '"'):
                        self.state = 5
                    elif aux == '"':
                        self.state = 6
                
                elif c == "<":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_MENOR)
                
                elif c == "+":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_MAS)

                elif c == "&":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_AND)
                
                elif c == "|":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_OR)

                elif c == "/":
                    extra = ""
                    aux = entra[i+1]
                    self.auxLex += c
                    self.column += 1
                    if not (aux == "/") and not (aux == "*"):
                        self.addTokens(S_DIAGONAL)
                    elif aux == "/":
                        self.state = 7

                    elif aux == "*":
                        self.state = 9

                elif c == "-":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_MENOS)
                
                elif c == ":":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_DOSPUNTOS)
                
                elif c == ",":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_COMA)
                
                elif c == "!":
                    self.auxLex += c
                    self.column += 1
                    self.addTokens(S_EXCLAMACION)

                else:
                      if c == "#":
                          print("se finalizo el analisis lexico")
                      else:
                          self.auxLex += c
                          self.addTokensErros()
                          
            
            elif self.state == 1:
                aux = entra[i+1]
                if c.isalpha():
                    self.auxLex += c
                    self.state = 1
                    if(not (aux.isalpha() or aux.isnumeric())):
                        aux1 = self.VerifyReservedToken()
                        self.addTokens(aux1)
                elif c.isnumeric():
                    self.auxLex += c
                    self.state =1
                    if(not (aux.isalpha() or aux.isnumeric())):
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
                    self.state = 4
                elif c.isnumeric():
                    self.auxLex += c
                    self.state = 4
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    self.state = 4
                elif c.isascii():
                    self.auxLex += c
                    self.state = 4

            elif self.state == 4:
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
                self.auxLex += c
                self.addTokens("CONT_FOR_STRING")
            
            elif self.state == 7:
                if c == "/":
                    self.auxLex += c
                    self.state = 8

            elif self.state == 8:
                aux = entra[i+1]
                if c.isalpha():
                    extra += c
                    self.auxLex += c
                    self.state = 8
                    if aux == "\n":
                        self.state = 9
                    elif "PATHL" in extra:
                        self.state = 10
                    elif "PATHW" in extra:
                        self.state = 10
                elif c.isnumeric():
                    extra += c
                    self.auxLex += c
                    self.state = 8
                    if aux == "\n":
                        self.state = 9
                    elif extra == "PATHL":
                        self.state = 8
                    elif extra == "PATHW":
                        self.state = 8
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    extra += c
                    self.auxLex += c
                    self.state = 8
                    if aux == "\n":
                        self.state = 9
                    elif "PATHL" in extra:
                        self.state = 10
                    elif "PATHW" in extra:
                        self.state = 10
                elif c.isascii():
                    extra += c
                    self.auxLex += c
                    self.state = 8
                    if aux == "\n":
                        self.state = 9
                    elif "PATHL" == extra:
                        self.state = 8
                    elif "PATHW" == extra:
                        self.state = 8

            elif self.state == 9:
                self.auxLex += c
                self.addTokens(COMENTARIOSIMPLE)

            elif self.state == 10:
                aux = entra[i+1]
                if c == ":":
                    self.auxLex += c
                    if aux == '\t' or aux == '\r' or aux == '\b' or aux == '\f' or aux == ' ':
                        self.state = 10
                    elif aux == "/":
                        self.state = 11
                    elif aux == "c":
                        self.state = 13
                elif c == '\t' or c == '\r' or c == '\b' or c == '\f' or c == ' ':
                    self.auxLex += c
                    if aux == '\t' or aux == '\r' or aux == '\b' or aux == '\f' or aux == ' ':
                        self.state = 10
                    elif aux == "/":
                        self.state = 11
                    elif aux == "c":
                        self.state = 13
            elif self.state == 11:
                if c == "/":
                    self.auxLex += c
                    self.state = 12
            elif self.state == 12:
                if not (c == "\n"):
                    self.auxLex += c
                    self.state = 12
                else:
                    self.auxLex += c
                    self.addTokens("RESERVADA_PATHLINUX")
            elif self.state == 13:
                if not (c == "\n"):
                    self.auxLex += c
                    self.state = 13
                else:
                    self.auxLex += c
                    self.addTokens("RESERVADA_PATHWINDOWS")

    def addTokens(self, Type):
        myListTokens.InsertEnd(TokensJS(self.auxLex,Type,self.column,self.row))
        self.auxLex = ""
        self.state = 0
    
    def addTokensErros(self):
        myListErrors.InsertEnd(TokensJS(self.auxLex,"CARACTER DESCONOCIDO",self.column,self.row))
        self.auxLex = ""
        self.state = 0


myAnalisis = AnalizadorLexicoJS()



prueba = """//   PATHL: /dsadsa/\n
//sdadsak\n
// PATHW: c:\\usuarios\\user\\documents\\output\\js\n"""
myAnalisis.analizadorJS(prueba)
myListTokens.listPrint()

def reportHTMLTokens():
    printval = myListTokens.headval
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
            myFile.write('<TH> ID </TH>')
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

reportHTMLTokens()
reportHTMLTokensErrors()
