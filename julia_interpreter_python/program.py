class program:
	def __init__(self, name, block):
		if name == "" or name == None:
			raise ValueError("No function name.")
		self.fname = name
		if block == None:
			raise ValueError("No block provided")
		self.block = block

	def execute(self):
		self.block.execute()