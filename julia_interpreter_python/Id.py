class ID:
	# Simulated memory using dictionary - may not work right
	# Note: ID.memory must be imported and referenced in the for loop and assignment stmt code
	memory = {}
	def __init__(self, lex):
		if(lex == None):
			raise ValueError("Null argument for ID")
		if(len(lex) != 1):
			raise ValueError("ID labels must be exactly one character long.")
		self.lex = lex

	def evaluate(self):
		return memory[self.lex]

	def get_lexeme(self):
		return self.lex