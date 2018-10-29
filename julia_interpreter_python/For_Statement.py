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