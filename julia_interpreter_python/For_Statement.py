from Id import ID

class For_Statement:
	def __init__(self, var, loop, block):
		if(var == None):
			raise ValueError("Null loop control variable argument")
		self.var = var
		if(loop == None):
			raise ValueError("Null loop control argument")
		self.loop = loop
		if(block == None):
			raise ValueError("Null block argument for loop")
		self.body = block

	def execute(self):
		# Store the loop variable in the memory dictionary
		start = loop.get_start_expr().evaluate()
		ID.memory[self.var.get_lexeme()] = start
		end = loop 
		while(start <= end):
			self.body.execute()
			start = start + 1
			ID.memory[self.var.get_lexeme()] = start