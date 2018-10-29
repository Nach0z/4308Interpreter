import sys
import os.path
import julia_parser
from exceptions import *

def main():
	name = ""
	try:
		name = sys.argv[1]
	except IndexError:
		print("Please provide a file to be executed.") 
		sys.exit()
	if(not os.path.isfile(name)):
		print("Specified input file not found.")
		sys.exit()
	try:
		p = julia_parser.Parser(name)
		program = p.parse()
		program.execute()
	except ParseException as e:
		# Handle a parse exception
		pass
	except LexicalException as e:
		# handle lex exceptions
		pass
	except EmptyTokenListException as e:
		# handle empty token list
		pass



if(__name__ == "__main__"):
	main()