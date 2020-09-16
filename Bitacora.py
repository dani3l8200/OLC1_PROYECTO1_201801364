class Bitacora:
    def __init__(self,state,tokens,iteracion,aceptacion):
        self.state = state
        self.tokens = tokens
        self.iteracion = iteracion
        self.aceptacion = aceptacion
    def __repr__(self):
        return 'Estado: ' +  str(self.state)  + " Token/Error Aceptado: " + self.tokens  + " No. Iteraciones: " + str(self.iteracion) +  " Estado Aceptacion: "  + str(self.aceptacion)
        
    def getState(self):
        return self.state
    def setState(self,state):
        self.state = state
    def getTok(self):
        return self.tokens
    def setTok(self,tokens):
        self.tokens = tokens
    def getIteracion(self):
        return self.iteracion
    def setIteracion(self,iteracion):
        self.iteracion = iteracion
    def getAceptacion(self):
        return self.aceptacion
    def setAceptacion(self,aceptacion):
        self.aceptacion = aceptacion