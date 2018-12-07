with Ada.Text_IO;
with Token;
with Token_Type;
with Ada.Characters.Handling;
use Ada.Characters.Handling;
package body Lexical_Analyzer is

        ---TODO: Make the array below a dyanmic array to store values of Type Token
   --array (list_of_tokens range <>) of a_token;
   
   procedure getList is
      
      Input_Code : File_Type;   
      C : Character;
     
   begin 
   
      Ada.Text_IO.Open (File => Input_Code, Mode => In_File,Name => "testcode.txt");
      
      while not End_Of_File(Input_Code) loop 
         
         Ada.Text_IO.Get (File => Input, Item => C);
         Ada.Text_IO.Put (Item = C);

       
           Ada.Text_IO.New_Line;
         end loop;
      
      --Ada.Text_IO.Close;  
   
   end getList; 
   
   function has_tokens return Boolean is
      
   begin 
      
      if list_of_tokens.length = 0 then 
         return False;
         
      else 
         return True;
         
      end if;
      
   end has_tokens;
      
   function get_Token_ID  (row : Integer; column : Integer; lex : String) return Integer is 
      
      --TODO Finish the token ID method
      --Find a wyay to replace assertion
      --Assert (lex != null);
      
      tid : Integer;
     
      
   begin 
      tid := 0;
      
      if Is_Digit(lex(0)) then 
        
         --TODO: deal with scanning each chatracter in a string
         tid = 0;
         
      elsif Is_Character(lex(0)) then 
         if lex(0) = 1 then 
            tid := ID;
         elsif lex = "function" then
           tid := FUNCTION_STAT;
         elsif lex = "end" then 
            tid := END_STAT;
         elsif lex = "if" then 
            tid := FOR_STAT;
         elsif lex = "for" then 
            tid := FOR_STAT;
         elsif lex = "while" then 
            tid := WHILE_STAT;
         elsif lex = "print" then
            tid := PRINT_STAT;
         elsif lex = "else" then
            tid := ELSE_STAT;
         else 
            raise Argument_Error ("invalid indentifier");
         end if;
         
      elsif lex = "=" then 
         tid := ASSIGN_OP;
      elsif lex = "<=" then 
         tid := LE_OP;
      elsif lex = "<" then 
         tid := LT_OP;
      elsif lex = ">" then 
         tid := GT_OP;
      elsif lex = ">=" then 
         tid := GE_OP;
      elsif lex = "==" then 
         tid := EQ_OP;
      elsif lex = "!=" then
         tid := NE_OP;
      elsif lex = "+" then 
         tid := ADD_OP;
      elsif lex = "-" then
         tid := SUB_OP;
      elsif lex = "*" then 
         tid := MUL_OP;
      elsif lex = "/" then 
         tid := DIV_OP;
      elsif lex = "%" then
         tid := MOD_OP;
      elsif lex = "\" then 
         tid := REV_DIV_OP;
      elsif lex = "(" then
         tid := LEFT_PAREN;
      elsif lex = ")" then 
         tid := RIGHT_PAREN;
      elsif lex = "^" then 
         tid := EXP_OP;
      elsif lex = ":" then 
         tid := COLON;
         
         
      else
         --Note edit this message
         raise Argument_Error ("Invalid lexeme somewhere");
    
      end if;   
   end get_Token_ID; 
   
   function get_Lexeme (line : String , index : Integer) return String is 
      --Assert (line != null);
      --Assert index >= 0;
      --Assert Is_Space(line(index)) == False;
      location : Integer;
      
   begin 
      
      location := index + 1;
      
      --TODO: work with string size
      
   end get_Lexeme;

end Lexical_Analyzer;
