from enum import Enum
class TokenType(Enum):

    def __init__(self):
        self.ID = 1
        self.LITERAL_INT = 2
        self.LE_OP = 3
        self.LT_OP = 4
        self.GE_OP = 5
        self.GT_OP = 6
        self.FUNCTION = 7
        self.ASSIGN_OP = 8
        self.EQ_OP = 9
        self.NE_OP = 10
        self.ADD_OP = 11
        self.SUB_OP = 12
        self.MUL_OP = 13
        self.DIV_OP = 14
        self.MOD_OP = 15
        self.REV_DIV_OP = 16
        self.EXP_OP = 17
        self.FOR = 18
        self.IF = 19
        self.END = 20
        self.WHILE = 21
        self.LEFT_PAREN = 22
        self.RIGHT_PAREN = 23
        self.EOS = 24



