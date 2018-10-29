class print_statement:
	def __init__(self, arg):
		if(arg == None):
			raise ValueError("Null arithmetic expression argument, cannot print nothing")
		self.arg = arg

	def execute(self):
		print(self.arg.evaluate())

