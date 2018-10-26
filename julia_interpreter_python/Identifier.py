class Identifier(self):
    lex

    def __init__(self, lex):
        if lex == null : 
            raise ValueError("there is not identifier")
        if lex[s] != 1 :
            raise ValueError("incorrect size for the identifier")
        self.lex = lex 


"""may need to deal with memory late dont know if it needs"""
"""to be added yet. There could be another way"""



