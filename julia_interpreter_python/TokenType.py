from enum import Enum

class TokenType(Enum):
    ID = 1
    LITERAL_INT = 2
    LE_OP = 3
    LT_OP = 4
    GE_OP = 5
    GT_OP = 6
    FUNCTION = 7
    ASSIGN_OP = 8
    EQ_OP = 9
    NE_OP= 10
    ADD_OP = 11
    SUB_OP = 12
    MUL_OP = 13
    DIV_OP = 14
    MOD_OP = 15
    REV_DIV_OP = 16
    EXP_OP = 17
    FOR = 18
    IF = 19
    END = 20
    WHILE = 21
    PRINT = 22
    LEFT_PAREN = 23
    RIGHT_PAREN = 24
    EOS = 25
    ELSE = 26
    COLON = 27




