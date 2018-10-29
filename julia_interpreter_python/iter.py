class Iter:
	def __init__(self, expr1, expr2):
		if(expr1 == None || expr2 == None):
			raise ValueError("Null arithmetic expression argument")
		self.start_expr = expr1
		self.end_expr = expr2

	def get_start_expr(self):
		return self.start_expr

	def get_end_expr(self):
		return self.end_expr

