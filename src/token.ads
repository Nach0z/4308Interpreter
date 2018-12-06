package Token is

   --TODO: ADD tokens all tokens to the token type
   type token_type is (ID, LITERAL_INT, LE_OP, LT_OP
                       GE_OP, GT_OP, FUNCTION_STAT, ASSIGN_OP,
                       EQ_OP, NE_OP, ADD_OP, SUB_OP, MUL_OP, DIV_OP,
                       MOD_OP, REV_DIV_OP, EXP_OP, FOR_STAT, IF_STAT, END_STAT, 
                       WHILE_STAT, PRINT_STAT, LEFT_PAREN, RIGHT_PAREN, EOS, 
                       ELSE_STAT, COLON);
   
   token_type'Pos (ID) = 1
     token_type'Pos (LITERAL_INT) = 2
     token_type'Pos (LE_OP) = 3
     token_type'Pos (LT_OP) = 4
     token_type'Pos (GE_OP) = 5
     token_type'Pos (GT_OP) = 6
     token_type'Pos (FUNCTION_STAT) = 7
     token_type'Pos (ASSIGN_OP) = 8
     token_type'Pos (EQ_OP) = 9
     token_type'Pos (NE_OP) = 10
     token_type'Pos (ADD_OP) = 11
     token_type'Pos (SUB_OP) = 12
     token_type'Pos (MUL_OP) = 13
     token_type'Pos (DIV_OP) = 14
     token_type'Pos (MOD_OP) = 15
     token_type'Pos (REV_DIV_OP) = 16
     token_type'Pos (EXP_OP) = 17
     token_type'Pos (FOR_STAT) = 18
     token_type'Pos (IF_STAT) = 19
     token_type'Pos (END_STAT) = 20
     token_type'Pos (WHILE_STAT) = 21
     token_type'Pos (PRINT_STAT) = 22
     token_type'Pos (LEFT_PAREN) = 23
     token_type'Pos (RIGHT_PAREN) = 24
     token_type'Pos (EOS) = 25
     token_type'Pos (ELSE_STAT) = 26
     token_type'Pos (COLON) = 27
     
   

end Token;