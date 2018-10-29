import TokenType

class Token:  
    def __init__(self, tokenid, lex, row, column):
        if(tokenid == None):
            raise ValueError("one of the token value is invalid")
        self.tokenid = tokenid
        if(lex == None):
            raise ValueError("one of the token value is invalid")
        self.lex = lex
        if(row == None):
            raise ValueError("the row number is invalid")
        self.row = row
        if(column == None):
            raise ValueError("invalid column number")
        self.column = column

    def get_token_type(self):
        return self.tokenid

    def get_row(self):
        return self.row

    def get_col(self):
        return self.column

    def get_lex(self):
        return self.lex

    # str method for testing
    def __repr__(self):
        return "ID: " + str(self.tokenid) + " Lex: " + str(self.lex) + " Line: " + str(self.row) + " Column: " + str(self.column) + "\n"