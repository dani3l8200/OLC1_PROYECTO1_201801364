

class Node():

    def __init__(self,Token):
        self.data = Token
        self.next = None
        
    def getToken(self):
        return self.data
    

class SingleLinkedList():
    def __init__(self):
        self.headval = None
        self.cont = 0
    def InsertEnd(self,value):
        newNode = Node(value)
        if self.headval is None:
            self.headval = newNode
            self.cont += 1
            return
        laste = self.headval
        while(laste.next):
            laste = laste.next
        laste.next = newNode
        self.cont += 1

    def InsertBegin(self,value):
        newNode = Node(value)
        newNode.next = self.headval
        self.headval = newNode
        self.cont += 1

    def __len__(self):
        return self.cont

    def __getitem__(self, i):
        if i >= len(self):
            raise IndexError("Index out of range.")

        current = self.headval
        for _ in range(i):
            current = current.next

        return current
        
    def __iter__(self):
        current = self.headval

        while current:
            yield current
            current = current.next

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
            print(printval.data, end='\n')
            printval = printval.next
