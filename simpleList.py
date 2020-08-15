

class Node():

    def __init__(self,Token):
        self.data = Token
        self.next = None
    def getToken(self):
        return self.data
    

class SingleLinkedList():
    def __init__(self):
        self.headval = None

    def InsertEnd(self,value):
        newNode = Node(value)
        if self.headval is None:
            self.headval = newNode
            return
        laste = self.headval
        while(laste.next):
            laste = laste.next
        laste.next = newNode

    def InsertBegin(self,value):
        newNode = Node(value)
        newNode.next = self.headval
        self.headval = newNode

    def RemoveItem(self,key):
        headVal = self.headval

        if headVal is not None:
            self.headval = headVal.next
            headVal = None
            return
        
        while headVal is not None:
            if headVal.data == key:
                break
            prev = headVal
            headVal = headVal.next 
        
        if headVal == None:
            return
        
        prev.next = headVal.next
        headVal = None

    def listPrint(self):
        printval = self.headval
        while printval is not None:
            print(printval.getToken().lex + " " + printval.getToken().tipo, end='\n')
            printval = printval.next

    def reportHTMLTokens(self):
        printval = self.headval
        with open('ReportTokensJS.html', 'w') as myFile:
            myFile.write('<html>')
            myFile.write('<body bgcolor=#1DF1F9>')
            myFile.write('<Center><h1>ANALIZADOR LEXICO JS</h1></Center>')
            myFile.write('<Center><TABLE border = 3.5 bordercolor = black bgcolor = #B4F91D></Center>')
            myFile.write('<TR>')
            myFile.write('<Center><TH COLSPAN = 4 > Tabla de Tokens Validos </TH></Center>')
            myFile.write('</TR>')
            myFile.write('<TR>')
            myFile.write('<TH> TOKEN </TH>')
            myFile.write('<TH> Lexema </TH>')
            myFile.write('<TH> Columna </TH>')
            myFile.write('<TH> Fila </TH>')
            myFile.write('</TR>')
            while printval is not None:
                myFile.write('<TR>')
                myFile.write('<TH> ' + printval.getToken().tipo + ' </TH>')
                myFile.write('<TH> ' + printval.getToken().lex + ' </TH>')
                myFile.write('<TH> ' + str(printval.getToken().columna) + ' </TH>')
                myFile.write('<TH> ' + str(printval.getToken().fila) + ' </TH>')
                myFile.write("</TR>");
                printval = printval.next
            myFile.write('</body>')
            myFile.write('</html>')