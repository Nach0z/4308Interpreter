class while_statement(object):
	def __init__(self, condition, block):
		if(condition == None):
			raise ValueError("Null boolean expression argument")
		self.block = condition
		if(block == None):
			raise ValueEror("Null block argument")
		self.block = block

	def execute():
		while (self.expr.evaluate()):
			self.block.execute()