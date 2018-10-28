import Token
import TokenType


class lexical_analyzer:
    list_of_tokens = []
    def __init__(self, file_name):
        # Read file
        with open(file_name, 'r') as f:
            row = 1
            try:
                for line in f:
                    processLine(line, rowNum, 0)
                    row = row + 1
            finally:
                self.list_of_tokens.append(Token(TokenType.EOS, "EOS", row, 1))

    def processLine(line, row, index, tokens):
        assert line != null
        assert rowNum > 0
        assert index >= 0
        # Changed original implementation to simply split by space and remove all whitespace
        index = noWhiteSpace(line, index)
        while(index < line(s)):
            lex = getLexe(line,index)
            tk = getgetTokenID
            tokens.append(Token(tk,lex,row,index+1))
            index += lex[s]
            index = noWhiteSpace(line, index)
        

    def getTokenID(lex,row,column):
        assert lex != null
        tid
        if(lex[0].isdigit()):
            if(digit(lex)):
                tid = TokenType.LIT_INT
            else:
               raise ValueError("expects a integer at the location " + row + column)
        elif lex[0].isalpha():
            if lex[s] == 1:
                tid = TokenType.LITERAL_INT
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
                raise ValueError("invalid syntax on ", row, coloumn)
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
            raise ValueError("Invalid token location : " + row + column)
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
        assert line != null
        assert index >= 0
        assert line[index].isspace() == false
        loc = index + 1
        while loc < line[s] and line[loc].ispace == false: 
            ++loc
        return line[index:loc]