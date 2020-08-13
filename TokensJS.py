############# SIMBOLOS ##########################################
S_ASTERISCO = "S_ASTERISCO"
S_DIAGONALINVERTIDA = "S_DIAGONALINVERTIDA"
S_IGUAL = "S_IGUAL"
S_COMILLASIMPLE = "S_COMILLASIMPLE"
S_PARENTESIS_A = "S_PARENTESIS_A"
S_PARENTESIS_C = "S_PARENTESIS_C"
S_MAYOR = "S_MAYOR"
S_LLAVE_A = "S_LLAVE_A"
S_LLAVE_C = "S_LLAVE_C"
S_PUNTO = "S_PUNTO"
S_PUNTOCOMA = "S_PUNTOCOMA"
S_COMILLASDOBLES = "S_COMILLASDOBLES"
S_MENOR = "S_MENOR"
S_MAS = "S_MAS"
S_AND = "S_AND"
S_OR = "S_OR"
S_DIAGONAL = "S_DIAGONAL"
S_MENOS = "S_MENOS"
S_DOSPUNTOS = "S_DOSPUNTOS"
S_COMA = "S_COMA"
S_EXCLAMACION = "S_ESCLAMACION"


###GENERICOS :V############################
NUMEROS = "NUMEROS"
ID = "ID"
COMENTARIOSIMPLE = "COMENTARIOUNILINEA"
COMENTARIOMULTILINEA = "COMENTARIOMULTILINEA"

#####---------------RESERVADAS---------------##################################################
RESERVADA_var = "RESERVADA_VAR"
RESERVADA_INT = "RESERVADA_INT"
RESERVADA_STRING = "RESERVADA_STRING"
RESERVADA_CHAR = "RESERVADA_CHAR"
RESERVADA_BOOLEAN = "RESERVADA_BOOLEAN"
RESERVADA_TYPE = "RESERVADA_TYPE" #pendiente :v 
RESERVADA_IF = "RESERVADA_IF"
RESERVADA_CONSOLE = "RESERVADA_CONSOLE"
RESERVADA_LOG = "RESERVADA_LOG"
RESERVADA_ELSE = "RESERVADA_ELSE"
RESERVADA_FOR = "RESERVADA_FOR"
RESERVADA_WHILE = "RESERVADA_WHILE"
RESERVADA_DO = "RESERVADA_DO"
RESERVADA_CONTINUE = "RESERVADA_CONTINUE"
RESERVADA_TRUE = "RESERVADA_TRUE"
RESERVADA_FALSE = "RESERVADA_FALSE"
RESERVADA_BREAK = "RESERVADA_BREAK"
RESERVADA_RETURN = "RESERVADA_RETURN"
RESERVADA_FUNTION = "RESERVADA_FUNTION"
RESERVADA_THIS = "RESERVADA_THIS"
RESERVADA_CONSTRUCTOR = "RESERVADA_CONSTRUCTOR"
RESERVADA_CLASS = "RESERVADA_CLASS"
RESERVADA_POW = "RESERVADA_POW"
RESERVADA_MATH = "RESERVADA_MATH"
RESERVADA_PATH = "RESERVADA_PATH"

class TokensJS:
    def __init__(self):
        pass
    def __init__(self,lex,tipo,columna,fila):
        self.lex = lex
        self.tipo = tipo
        self.columna = columna
        self.fila = fila
    def __repr__(self):
        if self.lex: return f'Token: { self.tipo} Lexema: {self.lex} Columna: {self.columna} Fila: {self.fila}'
        return f'{self.tipo}'
    def getLex(self):
        return self.__lex
    def setLex(self,lex):
        self.lex = lex
    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        self.tipo = tipo
    def getColumna(self):
        return self.columna
    def setColumna(self,columna):
        self.columna = columna
    def getFila(self):
        return self.fila
    def setFila(self,fila):
        self.fila = fila
