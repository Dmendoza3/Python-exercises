class InOutString:
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())
    
x = InOutString()

x.getString()
x.printString()