from Id import ID

class assignment_statement:

	# expr must be a kind of arithmetic expression
	def __init__(self, value, expr):
		if(value == None):
			raise ValueError("Null ID argument")
		self.var = value
		if(expr == None):
			raise ValueError("Null expression argument")
		self.expr = expr

	def execute(self):
		ID.memory[self.var.get_lexeme()] = self.expr.evaluate()
