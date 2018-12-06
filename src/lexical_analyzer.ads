with Ada.Text_IO;
with Token;
use a_token;
use Ada.Characters.Handling;


package lexical_analyzer is
  
   
   procedure getList;
   
   function has_tokens return Boolean; 
      
   function get_Token_ID  (row : Integer; column : Integer; lex : String) return Integer;
   
   function get_Lexeme (line : String ; index : Integer) return String;
      
         
    
end lexical_analyzer;
