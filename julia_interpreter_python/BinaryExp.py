from ArithmeticOperators import ArithmeticOperators as ao

class BinaryExp(object):
    def __init__(self, operator, left, right):
    	if(operator == None):
    		raise ValueError("Null operator arg")
    	self.op = operator
    	if(left == None):
    		raise ValueError("No left argument given")
    	self.left = left
    	if(right == None):
    		raise ValueError("No right argument given")
    	self.right = right

    def evaluate(self):
    	if(self.op == ao.ADD):
    		return self.left.evaluate() + self.right.evaluate()
    	elif(self.op == ao.SUB):
    		return self.left.evaluate() - self.right.evaluate()
    	elif(self.op == ao.MUL):
    		return self.left.evaluate() * self.right.evaluate()
    	elif(self.op == ao.DIV):
    		return self.left.evaluate() / self.right.evaluate()
    	elif(self.op == ao.MOD):
    		return self.left.evaluate() % self.right.evaluate()
    	elif(self.op == ao.REV_DIV):
    		return self.right.evaluate() / self.left.evaluate()
    	elif(self.op == ao.EXP):
    		return self.left.evaluate() ** self.right.evaluate()
    	else:
    		return 0

