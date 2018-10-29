class while_statement(object):
	def __init__(self, condition, block):
		if(condition == None):
			raise ValueError("Null boolean expression argument")
		self.condition = condition
		if(block == None):
			raise ValueEror("Null block argument")
		self.block = block

	def execute(self):
		while (self.condition.evaluate()):
			self.block.execute()