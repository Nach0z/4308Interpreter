from relationop import relationop as bops

class BooleanExp:

    def __init__(self, op, a, b):
        if(op == None):
            raise ValueError("Null relational operator argument")
        self.op = op
        if(expr1 == None):
            raise ValueError("Null relational operator argument")
        self.first = expr1
        if(expr2 == None):
            raise ValueError("Null relational operator argument")
        self.second = expr2

    def evaluate():
        boolean = false 
        if(self.op == bops.EQ):
            boolean = self.first.evaluate() == self.second.evaluate()
        elif(self.op == bops.NE):
            boolean = self.first.evaluate() != self.second.evaluate()
        elif(self.op == bops.LT):
            boolean = self.first.evaluate() < self.second.evaluate()
        elif(self.op == bops.LE):
            boolean = self.first.evaluate() <= self.second.evaluate()
        elif(self.op == bops.GT):
            boolean = self.first.evaluate() > self.second.evaluate()
        elif(self.op == bops.GE):
            boolean = self.first.evaluate() >= self.second.evaluate()
        return boolean

