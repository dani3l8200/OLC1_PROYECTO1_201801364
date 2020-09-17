class Error:
    def __init__(self,char,description,columna,fila,valo):
        self.char = char
        self.description = description
        self.columna = columna
        self.fila = fila
        self.valo = valo
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
    def getValo(self):
        return self.valo
    def setValo(self,valo):
        self.valo = valo