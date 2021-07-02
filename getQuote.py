import random

class Quote:
    def __init__(self, filename):
        self.name = str(filename)
        self.getQuote()

    def prepareList(self):
        temp = open(self.name, 'r')
        self.quotes = temp.readlines()
    
    def makeRandomline(self):
        running = True
        while running:
            foo = random.randint(0, len(self.quotes))
            if foo % 2 == 0:
                running = False
        self.line_number = foo

    def getQuote(self):
        self.prepareList()
        self.makeRandomline()
        self.text = self.quotes[self.line_number]
        self.author = self.quotes[self.line_number + 1]
