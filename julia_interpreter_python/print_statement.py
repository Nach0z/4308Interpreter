class print_statement(object):
	def __init__(self, arg):
		if(arg == None):
			raise ValueError("Null arithmetic expression argument, cannot print nothing")
		this.arg = arg

	def execute(self):
		print(self.arg.execute())

