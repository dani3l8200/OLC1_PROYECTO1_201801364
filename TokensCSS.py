class TokensCSS:
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
        return self.lex
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