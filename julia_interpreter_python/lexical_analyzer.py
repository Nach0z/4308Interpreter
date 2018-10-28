import Token
import TokenType
import re

class lexical_analyzer:
    list_of_tokens = []
    def __init__(self, file_name):
        # Read file
        with open(file_name, 'r') as f:
            row = 1
            try:
                for line in f:
                    processLine(line, row)
                    row = row + 1
            finally:
                self.list_of_tokens.append(Token(TokenType.EOS, "EOS", row, 1))

    # Got rid of get lexeme since it just separated based on whitespace
    def processLine(line, row):
        assert line != null
        assert rowNum > 0
        # parse line into a list of ordered pairs (lexeme, starting index)
        # Note: Found how to do this on SO
        lexeme_pairs = [(m.group[0], m.start()) for m in re.finditer(r'\S+', line)]
        for (lex, index) in lexeme_pairs:
            # Process each lexeme into a token
            lex = getTokenID(lex, row, index)
            # Add processed token to the global token list


    def getTokenID(lex,row,column):
        assert lex != null
        tid
        # TODO: Make this actually check if this identifier is a literal integer or invalid
        if(lex[0].isdigit()):
            for c in lex:
                if(not c.isdigit()):
                    raise ValueError("expected an integer literal at the location " + str(row) + str(column))
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
                raise ValueError("invalid identifier at ", str(row), str(column))
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
            raise ValueError("Invalid lexeme at " + str(row) + str(column))
        return tid


    def noWhiteSpace(line, index):
        assert line != null
        assert index >= 0
        line
        current = index
        while(current < line(s) and line[current].isspace()):
            ++current
        return current

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


def test_function():


if(__name__ == "__main__"):
    test_function()