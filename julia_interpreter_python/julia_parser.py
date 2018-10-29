from exceptions import *
from Id import ID
from Block import Block
from TokenType import TokenType
from lexical_analyzer import lexical_analyzer

class Parser:
	def __init__(self, name):
		self.lex = lexical_analyzer(name)

	def parse(self):
		token = self.lex.get_next_token()
		self.__match__(token, TokenType.FUNCTION)
		function_name = get_id()
		token = lex.get_next_token()
		self.__match__(tok, TokenType.LEFT_PAREN)
		token = lex.get_next_token()
		self.__match__(tok, TokenType.RIGHT_PAREN)
		block = getBlock()
		tok = lex.get_next_token()
		self.__match__(tok, TokenType.END)
		tok = lex.getNextToken
		if (tok.getTokenType != TokenType.EOS):
			raise ParseException("Garbage at end of program at " + + str(row) + ":" + str(column))

	def __get_block__():
		token = None
		block = Block()
		while True:
			block.add(self.__get_stmt__())
			token = self.lex.get_lookahead_token()
			if(not self.__is_valid_start_of_stmt__(token.get_token_type())):
				break
		return block

	def __get_stmt__():
		stmt = None
		token = self.lex.get_lookahead_token()
		if(token.get_token_type == TokenType.IF):
			stmt = self.__get_if_stmt__()
		elif(token.get_token_type == TokenType.FOR):
			stmt = self.__get_for_stmt__()
		elif(token.get_token_type == TokenType.PRINT)
			stmt = self.__get_print_stmt__()
		elif(token.get_token_type == TokenType.WHILE):
			stmt = self.__get_while_stmt__()
		else:
			stmt = self.__get_assign_stmt__()
		return stmt

	def __get_assign_stmt__():
		id = self.__get_id__()
		token = self.lex.get_next_token()
		match(token, TokenType.ASSIGN_OP)
		expr = self.__get_arith_expr__()
		return Assignment

	def __get_while_stmt__():
		pass

	def __get_print_stmt__():
		pass

	def __get_for_stmt__():
		pass

	def __get_if_stmt__():
		pass

	def __get_arith_expr__():
		pass

	def __get_binary_expr__():
		pass

	def __get_arith_op__():
		pass

	def __is_arith_op__():
		return false

	def __get_literal_int__():
		pass

	def __get_iter__():
		pass

	def __get_bool_expr__():
		pass

	def __get_relational_op__():
		pass

	def __is_relational_op__():
		pass

	def __is_valid_start_of_stmt__():
		pass

	def __get_id__():
		token = lex.get_next_token()
		self.__match__(token, TokenType.ID)
		return ID(token.get_lex)

	def __match__(self, token, tid):
		if(token.get_token_type != tid):
			raise ParseException("Expected " + tid.name + " at: " + str(token.get_row()) + ":" + str(token.get_col()))