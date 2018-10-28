from Token import Token
from TokenType import TokenType
import re
from enum import Enum

class lexical_analyzer:
    list_of_tokens = []
    def __init__(self, file_name):
        # Read file, keep track of which line we're on
        with open(file_name, 'r') as f:
            row = 1
            try:
                for line in f:
                    self.processLine(line, row)
                    row = row + 1
            finally:
                self.list_of_tokens.append(Token(TokenType.EOS, "EOS", row, 1))

    def get_next_token(self):
        if(not self.has_tokens()):
            raise EmptyTokenListException("No more tokens")


    def get_lookahead_token(self):
        pass

    def has_tokens(self):
        if(len self.list_of_tokens == 0):
            return false
        return true
    # Got rid of get lexeme since it just separated based on whitespace
    def processLine(self, line, row):
        assert line != None
        assert row > 0
        # parse line into a list of ordered pairs (lexeme, starting index)
        # Note: Found how to do this at: 
        #    https://stackoverflow.com/questions/13734451/string-split-with-indices-in-python 
        lexeme_pairs = [(m.group(0), m.start() + 1) for m in re.finditer(r'\S+', line)]
        for (lex, index) in lexeme_pairs:
            # Process each lexeme into a token
            tid = self.getTokenID(lex, row, index)
            # Add processed token to the global token list
            self.list_of_tokens.append(Token(tid, lex, row, index))


    def getTokenID(self, lex,row,column):
        assert lex != None
        tid = 0
        # TODO: Make this actually check if this identifier is a literal integer or invalid
        if(lex[0].isdigit()):
            for c in lex:
                if(not c.isdigit()):
                    raise ValueError("expected an integer literal at line " + str(row) + ":" + str(column))
                tid = TokenType.LITERAL_INT
        elif lex[0].isalpha():
            if len(lex) == 1:
                tid = TokenType.ID
            elif lex is "function":
                tid = TokenType.FUNCTION
            elif lex is "end":
                tid = TokenType.END
            elif lex is "if":
                tid = TokenType.IF
            elif lex is "for":
                tid = TokenType.FOR
            elif lex is "while": 
                tid = TokenType.WHILE
            elif lex is "print": 
                tid = TokenType.PRINT
            elif lex is "else": 
                tid = TokenType.ELSE
            else:
                raise ValueError("invalid identifier at line " + str(row) + ":" + str(column))
        elif lex is "=":
            tid = TokenType.ASSIGN_OP
        elif lex is "<=":
            tid = TokenType.LE_OP
        elif lex is "<":
            tid = TokenType.LT_OP
        elif lex is ">=":
            tid = TokenType.GE_OP
        elif lex is "==":
            tid = TokenType.EQ_OP
        elif lex is "!=":
            tid = TokenType.NE_OP
        elif lex is "+":
            tid = TokenType.ADD_OP
        elif lex is "-":
            tid = TokenType.SUB_OP
        elif lex is "*":
            tid = TokenType.MUL_OP
        elif lex is "/":
            tid = TokenType.DIV_OP
        elif lex is "%":
            tid = TokenType.MOD_OP
        elif lex is "\\":
            tid = TokenType.REV_DIV_OPP
        elif lex is "^": 
            tid = TokenType.EXP_OP
        else: 
            raise ValueError("Invalid lexeme at line " + str(row) + ":" + str(column))
        return tid

    def digit(lex):
        assert lexeme != null
        i = 0
        while i < lex[s] and lex[i].isdigit():
            ++i
        return i == lex[s]

    def getLexe(line, index):
        # TODO: Change this to take a single string
        assert line != null
        assert index >= 0
        assert line[index].isspace() == false
        loc = index + 1
        while loc < line[s] and line[loc].ispace == false: 
            ++loc
        return line[index:loc]

def main():
    lexan = lexical_analyzer("test.txt")
    print(lexan.list_of_tokens)

if __name__ == "__main__":
    main()