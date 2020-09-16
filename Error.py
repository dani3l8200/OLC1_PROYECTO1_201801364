class Error:
    def __init__(self,char,description,columna,fila):
        self.char = char
        self.description = description
        self.columna = columna
        self.fila = fila
    def __repr__(self):
        if self.char: return f'Descripcion: { self.description} Char: {self.char} Columna: {self.columna} Fila: {self.fila}'
        return f'{self.description}'
    def getChar(self):
        return self.char
    def setChar(self,lex):
        self.char = lex
    def getDescription(self):
        return self.description
    def setDescription(self,tipo):
        self.description = tipo
    def getColumna(self):
        return self.columna
    def setColumna(self,columna):
        self.columna = columna
    def getFila(self):
        return self.fila
    def setFila(self,fila):
        self.fila = fila