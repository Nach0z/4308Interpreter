package Token is

   --TODO: ADD tokens all tokens to the token type
   type token_type is (ID, LITERAL_INT, LE_OP, LT_OP,
                       GE_OP, GT_OP, FUNCTION_STAT, ASSIGN_OP,
                       EQ_OP, NE_OP, ADD_OP, SUB_OP, MUL_OP, DIV_OP,
                       MOD_OP, REV_DIV_OP, EXP_OP, FOR_STAT, IF_STAT, END_STAT, 
                       WHILE_STAT, PRINT_STAT, LEFT_PAREN, RIGHT_PAREN, EOS, 
                       ELSE_STAT, COLON);
   
   for token_type use
   (ID => 1,
     LITERAL_INT => 2,
     LE_OP => 3,
     LT_OP => 4,
     GE_OP => 5,
     GT_OP => 6,
     FUNCTION_STAT => 7,
     ASSIGN_OP => 8,
     EQ_OP => 9,
     NE_OP => 10,
     ADD_OP => 11,
     SUB_OP => 12,
     MUL_OP => 13,
     DIV_OP => 14,
     MOD_OP => 15,
     REV_DIV_OP => 16,
     EXP_OP => 17,
     FOR_STAT => 18,
     IF_STAT => 19,
     END_STAT => 20,
     WHILE_STAT => 21,
     PRINT_STAT => 22,
     LEFT_PAREN => 23,
     RIGHT_PAREN => 24,
     EOS => 25,
     ELSE_STAT => 26,
     COLON => 27);
     

end Token;
