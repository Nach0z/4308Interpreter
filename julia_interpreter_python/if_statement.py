class if_statement:
	def __init(self, condition, if_block, else_block):
		if(condition == None):
			raise ValueError("Null condition argument")
		self.condition = condition
		if(if_block == None):
			raise ValueError("Null if block argument")
		self.if_block = if_block
		if(else_block == None):
			raise ValueError("Null else block argument")
		self.else_block = else_block

	def execute(self):
		if(self.expr.evaluate()):
			self.if_block.execute()
		else:
			self.else_block.execute()
