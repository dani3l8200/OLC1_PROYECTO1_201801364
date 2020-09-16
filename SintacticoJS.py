
from TokensJS import *
from Error import * 
from simpleList import *
listErrorSintactico = SingleLinkedList()

class SintacticoJS:
    indice = 0
    preaAnalisis = None
    errorSintactico = False
    def __init__(self,ListTokens):
        self.listTokens = ListTokens
        self.indice = 0
        self.preaAnalisis = ListTokens[self.indice]
        self.inicio()
        self.Parea("SIMBOLOACEPTACION")
            
    
    def inicio(self):
        self.Lista()
    
    def Lista(self):
        self.Expresion()
        self.ListaP()
    
    def ListaP(self):
        if not (self.preaAnalisis.getToken().getTipo() == "SIMBOLOACEPTACION"):
            self.Parea("NUEVA_EXPRESION")
            self.Expresion() 
            self.ListaP()
        else:
            pass 
    def Expresion(self):
        self.E()

    def E(self):
        self.T()
        self.EP()
    
    def EP(self):
        if self.preaAnalisis.getToken().getTipo() == S_MAS:
            self.Parea(S_MAS)
            self.T()
            self.EP()
        elif self.preaAnalisis.getToken().getTipo() == S_MENOS:
            self.Parea(S_MENOS)
            self. T()
            self.EP()
        else:
            pass      
    
    def T(self):
        self.F()
        self.TP()
    
    def TP(self):
        if self.preaAnalisis.getToken().getTipo() == S_ASTERISCO:
            self.Parea(S_ASTERISCO)
            self.F()
            self.TP()
        elif self.preaAnalisis.getToken().getTipo() == S_DIAGONAL:
            self.Parea(S_DIAGONAL)
            self.F()
            self.TP()
        else:
            pass
    
    def F(self):
        if self.preaAnalisis.getToken().getTipo() == NUMEROS:
            self.Parea(NUMEROS)
        elif self.preaAnalisis.getToken().getTipo() == "DECIMAL":
            self.Parea("DECIMAL")
        elif self.preaAnalisis.getToken().getTipo() == ID:
            self.Parea(ID)
        elif self.preaAnalisis.getToken().getTipo() == S_PARENTESIS_A:
                self.Parea(S_PARENTESIS_A)
                self.E()
                self.Parea(S_PARENTESIS_C)
          
        else:
            self.addError(self.preaAnalisis.getToken().getFila(),self.preaAnalisis.getToken().getColumna(),"No Aceptado",self.CadenaCompleta(self.listTokens))
            
    
    def Parea(self,Tipo):
        if self.errorSintactico:
            if(self.indice < self.listTokens.cont - 1):
                self.indice += 1
                self.preaAnalisis = self.listTokens[self.indice]
                if self.preaAnalisis.getToken().getTipo() == "SIMBOLOACEPTACION":
                    self.errorSintactico = False
        else:
            if self.preaAnalisis.getToken().getTipo() == Tipo:
                if self.indice < self.listTokens.cont - 1:
                    self.indice += 1
                    self.preaAnalisis = self.listTokens[self.indice]
            else:
                self.addError(self.preaAnalisis.getToken().getFila(),self.preaAnalisis.getToken().getColumna(),"No Aceptado",self.CadenaCompleta(self.listTokens))
    

    def addError(self,row,column,chain,description):
        listErrorSintactico.InsertEnd(Error(chain,description,column,row))

    def CadenaCompleta(self,mylist):
        xa = mylist.headval
        aux = ""
        while xa is not None: 
            aux += xa.getToken().getLex()
            xa = xa.next
        return aux

    def ReportHTMLSintactico(self):
        xa = listErrorSintactico.headval
        counter = 1
        with open('ReportSintacticoJS.html', 'w') as myFile:
            myFile.write('<html>')
            myFile.write('<body bgcolor=#FFDEAD>')
            myFile.write('<Center><h1>ANALIZADOR SINTACTICO JS</h1></Center>')
            myFile.write('<Center><TABLE border = 3.5 bordercolor = black bgcolor = #B0E0E6></Center>')
            myFile.write('<TR>')
            myFile.write('<Center><TH COLSPAN = 5 > Tabla de Error Sintactico </TH></Center>')
            myFile.write('</TR>')
            myFile.write('<TR>')
            myFile.write('<TH> ID </TH>')
            myFile.write('<TH> Operacion Aritmetica</TH>')
            myFile.write('<TH> Valido  </TH>')
            myFile.write('<TH> Columna </TH>')
            myFile.write('<TH> Fila </TH>')
            myFile.write('</TR>')
            while xa is not None:
                myFile.write('<TR>')
                myFile.write('<TH> ' + str(counter) + ' </TH>')
                myFile.write('<TH> ' + xa.getToken().getDescription() + ' </TH>')
                myFile.write('<TH> ' + xa.getToken().getChar() + ' </TH>')
                myFile.write('<TH> ' + str(xa.getToken().getColumna()) + ' </TH>')
                myFile.write('<TH> ' + str(xa.getToken().getFila()) + ' </TH>')
                myFile.write("</TR>");
                counter += 1
                xa = xa.next
            myFile.write('</body>')
            myFile.write('</html>')