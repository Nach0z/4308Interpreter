with Ada.Text_IO; use Ada.Text_IO;
with Token; use Token;
with Token_Type; use Token_Type;
with Ada.Characters.Handling;
use Ada.Characters.Handling;
with Ada.Long_Float_Text_IO;
with Ada.Sequential_IO;
with Ada.Exceptions; use Ada.Exceptions;
with Ada.Strings; use Ada.Strings;
with Ada.Containers.Indefinite_Vectors;
use Ada.Containers; 
package body Lexical_Analyzer is

        
   --Using strings as a place holder until we can figure out how to include token as a type
   package list_of_tokens is new Ada.Containers.Indefinite_Vectors (Index_Type => Positive, Element_type => token_t);
   
   listoftokes : list_of_tokens;
   
   
   procedure getList is
      
      Input_Code : File_Type;  
      row : Integer;
     
   begin 
   
      Ada.Text_IO.Open (File => Input_Code, Mode => In_File,Name => "testcode.txt");
      row := 1;
      while not End_Of_File(Input_Code) loop 
         Put_Line (Get_Line (Input_Code));
         row := row + 1;
      end loop;
      
     list_of_tokens.Insert(listoftokes, New_Item => new Create(id_number(EOS), "EOS", row, 1));          
      
      Close (Input_Code);
                            
   
   end getList; 
   
   function has_tokens return Boolean is
      
   begin 
      
      if true then 
         return False;
         
      else 
         return True;
         
      end if;
      
   end has_tokens;
      
   function get_Token_ID  (row : Integer; column : Integer; lex : String) return String is 
      
      --TODO Finish the token ID method
      --Find a wyay to replace assertion
      --Assert (lex != null);
      
      tid : Integer;
     
      
   begin 
      tid := 0;
      
      if Is_Digit(lex(0)) then 
        
         --TODO: deal with scanning each chatracter in a string
         tid := id_number(LITERAL_INT);
         
      elsif Is_Letter(lex(0)) then 
         if lex(0) = 1 then
            tid := id_number(ID);
         elsif lex = "function" then
           tid := id_number(FUNCTION_STAT);
         elsif lex = "end" then 
            tid := id_number(END_STAT);
         elsif lex = "if" then 
            tid := id_number(FOR_STAT);
         elsif lex = "for" then 
            tid := id_number(FOR_STAT);
         elsif lex = "while" then 
            tid := id_number(WHILE_STAT);
         elsif lex = "print" then
            tid := id_number(PRINT_STAT);
         elsif lex = "else" then
            tid := id_number(ELSE_STAT);
         else 
            raise Argument_Error with ("invalid indentifier");
         end if;
         
      elsif lex = "=" then 
         tid := id_number(ASSIGN_OP);
      elsif lex = "<=" then 
         tid := id_number(LE_OP);
      elsif lex = "<" then 
         tid := id_number(LT_OP);
      elsif lex = ">" then 
         tid := id_number(GT_OP);
      elsif lex = ">=" then 
         tid := id_number(GE_OP);
      elsif lex = "==" then 
         tid := id_number(EQ_OP);
      elsif lex = "!=" then
         tid := id_number(NE_OP);
      elsif lex = "+" then 
         tid := id_number(ADD_OP);
      elsif lex = "-" then
         tid := id_number(SUB_OP);
      elsif lex = "*" then 
         tid := id_number(MUL_OP);
      elsif lex = "/" then 
         tid := id_number(DIV_OP);
      elsif lex = "%" then
         tid := id_number(MOD_OP);
      elsif lex = "\" then 
         tid := id_number(REV_DIV_OP);
      elsif lex = "(" then
         tid := id_number(LEFT_PAREN);
      elsif lex = ")" then 
         tid := id_number(RIGHT_PAREN);
      elsif lex = "^" then 
         tid := id_number(EXP_OP);
      elsif lex = ":" then 
         tid := id_number(COLON);
         
         
      else
         --Note edit this message
         raise Argument_Error with ("Invalid lexeme somewhere");
    
      end if;
        
        return lex;
   end get_Token_ID; 
   
   function get_Lexeme (line : String ; index : Integer) return String is 
      --Assert (line != null);
      --Assert index >= 0;
      --Assert Is_Space(line(index)) == False;
      location : Integer;
      
   begin 
      
      location := index + 1;
      
      --TODO: work with string size
      
      return line;
      
   end get_Lexeme;

end Lexical_Analyzer;
