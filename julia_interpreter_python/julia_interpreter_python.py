import sys
import os.path
from Id import ID
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
		print("Elements of memory dictionary: ")
		print(ID.memory.iter())
	except ParseException as e:
		print(str(e))
		pass
	except LexicalException as e:
		print(str(e))
		pass
	except EmptyTokenListException as e:
		print(str(e))
		pass



if(__name__ == "__main__"):
	main()