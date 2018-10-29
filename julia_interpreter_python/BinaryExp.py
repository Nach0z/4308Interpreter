from ArithmeticOperators import ArithmeticOperators as ao

class BinaryExp(object):
    def __init__(self, operator, left, right):
    	if(operator == None):
    		raise ValueError("Null operator arg")
    	this.op = operator
    	if(left == None):
    		raise ValueError("No left argument given")
    	this.left = left
    	if(right == None):
    		raise ValueError("No right argument given")
    	this.right = right

    def evaluate(self):
    	if(self.op == ao.ADD_OP):
    		return self.left + self.right
    	elif(self.op == ao.SUB_OP):
    		return self.left - self.right
    	elif(self.op == ao.MUL_OP):
    		return self.left * self.right
    	elif(self.op == ao.DIV_OP):
    		return self.left / self.right
    	elif(self.op == ao.MOD_OP):
    		return self.left % self.right
    	elif(self.op == ao.REV_DIV_OP):
    		return self.right / self.left
    	elif(self.op == ao.EXP_OP):
    		return self.left ** self.right
    	else:
    		return 0

