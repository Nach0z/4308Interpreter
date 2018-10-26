from julia_interpreter_python import TokenType

class Token(object):
    tokenid
    lexeme
    row
    column
    
    def __init__(self, tokenid, lex, row, column):
        if(tokenid == null):
            raise ValueError("one of the token value is invalid")
        self.tokenid = tokenid
        if(lex == null):
            raise ValueError("one of the token value is invalid")
        self.lex = lex
        if(row == null):
            raise ValueError("the row number is invalid")
        self.row = tokenid
        if(column == null):
            raise ValueError("invalid column number")
        self.column = column

    def getTokenID():
        return tokenid

    def getRow():
        return row
    def getColumn():
        return column

    def getLex():
        return lex




        
   
    



