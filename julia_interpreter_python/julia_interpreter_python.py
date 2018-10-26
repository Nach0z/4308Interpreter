import sys
import os.path
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
		p = Parser()
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
	except:
		print("Unknown error occered.")
		sys.exit()



if(__name__ == "__main__"):
	main()