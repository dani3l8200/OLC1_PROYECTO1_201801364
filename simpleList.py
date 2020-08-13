

class Node:

    def __init__(self,data=None):
        self.data = data
        self.next = None

class SingleLinkedList:
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
            print(printval.data, end='\n')
            printval = printval.next


