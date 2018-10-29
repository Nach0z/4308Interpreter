class ID:
	# Simulated memory using dictionary - may not work right
	memory = {}
	def __init__(self, lex):
		if(lex == None):
			raise ValueError("Null argument for ID")
		if(len(lex) != 1):
			raise ValueError("ID labels must be exactly one character long.")
		self.lex = lex

	def evaluate(self):
		return ID.memory[self.lex]

	def get_lexeme(self):
		return self.lex