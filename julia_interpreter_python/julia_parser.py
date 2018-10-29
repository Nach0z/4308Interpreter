from exceptions import *
from Id import ID
from Block import Block
from BinaryExp import BinaryExp
from BooleanExp import BooleanExp
from assignment_statement import assignment_statement as a_stmt
from print_statement import print_statement as p_stmt
from For_Statement import For_Statement as for_stmt
from if_statement import if_statement as if_stmt
from iter import Iter
from literal_int import literal_int as lit_int
from program import Program
from relationop import relationop as rops
from while_statement import while_statement as w_stmt
from ArithmeticOperators import ArithmeticOperators as ao
from TokenType import TokenType
from lexical_analyzer import lexical_analyzer

class Parser:
	def __init__(self, name):
		self.lex = lexical_analyzer(name)

	def parse(self):
		"""while True:
			print(self.lex.get_next_token())
			if not self.lex.has_tokens():
				break;"""
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.FUNCTION)
		function_name = self.__get_id__()
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.LEFT_PAREN)
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.RIGHT_PAREN)
		block = self.__get_block__()
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.END)
		token = self.lex.get_next_token()
		if (token.get_token_type() != TokenType.EOS):
			raise ParseException("Garbage at end of program at " + + str(row) + ":" + str(column))
		return Program(function_name, block)

	def __get_block__(self):
		token = None
		block = Block()
		while True:
			block.add(self.__get_stmt__())
			token = self.lex.get_lookahead_token()
			if(not self.__is_valid_start_of_stmt__(token.get_token_type())):
				break
		return block

	def __get_stmt__(self):
		stmt = None
		token = self.lex.get_lookahead_token()
		if(token.get_token_type() == TokenType.IF):
			stmt = self.__get_if_stmt__()
		elif(token.get_token_type() == TokenType.FOR):
			stmt = self.__get_for_stmt__()
		elif(token.get_token_type() == TokenType.PRINT):
			stmt = self.__get_print_stmt__()
		elif(token.get_token_type() == TokenType.WHILE):
			stmt = self.__get_while_stmt__()
		else:
			stmt = self.__get_assign_stmt__()
		return stmt

	def __get_assign_stmt__(self):
		id = self.__get_id__()
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.ASSIGN_OP)
		expr = self.__get_arith_expr__()
		return a_stmt(id, expr)

	def __get_while_stmt__(self):
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.WHILE)
		expr = self.__get_bool_expr__()
		block = self.__get_block__()
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.END)
		return w_stmt(expr, block)

	def __get_print_stmt__(self):
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.PRINT)
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.LEFT_PAREN)
		arg = self.__get_arith_expr__()
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.RIGHT_PAREN)
		return p_stmt(arg)


	def __get_for_stmt__(self):
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.FOR)
		loopvar = self.__get_id__()
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.ASSIGN_OP)
		loop = self.__get_iter__()
		block = self.__get_block__()
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.END)
		return for_stmt(loopvar, loop, block)


	def __get_if_stmt__(self):
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.IF)
		expr = self.__get_bool_expr__()
		block = self.__get_block__()
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.ELSE)
		elseblock = self.__get_block__()
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.END)
		return if_stmt(expr, block, elseblock)


	def __get_arith_expr__(self):
		expr = None
		token = self.lex.get_lookahead_token()
		if(token.get_token_type() == TokenType.ID):
			expr = self.__get_id__()
		elif(token.get_token_type() == TokenType.LITERAL_INT):
			expr = self.__get_literal_int__()
		else:
			expr = self.__get_binary_expr__()
		return expr

	def __get_binary_expr__(self):
		op = self.__get_arith_op__()
		left = self.__get_arith_expr__()
		right = self.__get_arith_expr__()
		return BinaryExp(op, left, right)

	def __get_arith_op__(self):
		token = self.lex.get_next_token()
		op = None
		if(not self.__is_arith_op__(token.get_token_type())):
			raise ParseException("Expected arithmetic operator at line: " + str(token.get_row) + ":" + str(token.get_col) )
		if(token.get_token_type() == TokenType.ADD):
			op = ao.ADD_OP
		elif(token.get_token_type() == TokenType.SUB):
			op = ao.SUB_OP
		elif(token.get_token_type() == TokenType.MUL):
			op = ao.MUL_OP
		elif(token.get_token_type() == TokenType.DIV):
			op = ao.DIV_OP
		elif(token.get_token_type() == TokenType.MOD):
			op = ao.MOD_OP
		elif(token.get_token_type() == TokenType.EXP):
			op = ao.EXP_OP
		else:
			op = ao.REV_DIV_OP
		return op

	def __is_arith_op__(self, op):
		return op == TokenType.ADD or op == TokenType.SUB or op == TokenType.MUL or op == TokenType.DIV or op == TokenType.MOD or op == TokenType.EXP or op == TokenType.REV_DIV

	def __get_literal_int__(self):
		token = self.lex.get_next_token()
		if(token.get_token_type() != TokenType.LITERAL_INT):
			raise ParseException("Literal integer expected at line: "+ str(token.get_row()) + ":" + str(token.get_col()) )
		return lit_int(int(token.get_lex())) 

	def __get_iter__(self):
		expr1 = self.__get_arith_expr__()
		token = lex.get_next_token()
		self.__match__(token, TokenType.COLON)
		expr2 = __get_arith_expr__()
		return Iter(expr1, expr2)

	def __get_bool_expr__(self):
		op = self.__get_relational_op__()
		expr1 = self.__get_arith_expr__()
		expr2 = self.__get_arith_expr__()
		return BooleanExp(op, expr1, expr2)

	def __get_relational_op__(self):
		token = self.lex.get_next_token()
		if(not self.__is_relational_op__(token.get_token_type())):
			raise ParseException("Expected relational operator at line: "+ str(token.get_row) + ":" + str(token.get_col) )
		op = None
		if(token.get_token_type() == TokenType.EQ):
			op = rops.EQ
		elif(token.get_token_type() == TokenType.NE):
			op = rops.NE
		elif(token.get_token_type() == TokenType.LT):
			op = rops.LT
		elif(token.get_token_type() == TokenType.LE):
			op = rops.LE
		elif(token.get_token_type() == TokenType.GT):
			op = rops.GT
		else:
			op = rops.GE
		return op

	def __is_relational_op__(self, op):
		return (op == TokenType.EQ or op == TokenType.NE or	op == TokenType.GT or op == TokenType.GE or op == TokenType.LT or op == TokenType.LE )


	def __is_valid_start_of_stmt__(self, op):
		return op == TokenType.IF or op == TokenType.FOR or op == TokenType.WHILE or op == TokenType.PRINT or op == TokenType.ID

	def __get_id__(self):
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.ID)
		return ID(token.get_lex())

	def __match__(self, token, tid):
		if(token.get_token_type() != tid):
			raise ParseException("Expected " + tid.name + " at: " + str(token.get_row()) + ":" + str(token.get_col()))