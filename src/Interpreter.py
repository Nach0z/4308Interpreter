import sys
from util import LexNode, LexAnalyzer

def main():
	input = ""
	try:
		input = sys.argv[1]
	except(IndexError):
		print("Please provide an input file.")
		sys.exit()
	try:
		root_node = LexNode()
		analyzer = LexAnalyzer(TokenProvider(input))
		analyzer.parse(root_node, 0)
	except:
		Print("Parsing broke, something went wrong.")

if(__name__ == "__main__"):
	main()