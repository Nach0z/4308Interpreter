with Ada.Text_IO;
with Token;
with Token_Type;
with Ada.Characters.Handling;
use Ada.Characters.Handling;
package Lexical_Analyzer is

   procedure getList;
   
   function has_tokens return Boolean; 
      
   function get_Token_ID  (row : Integer; column : Integer; lex : String) return String;
   
   function get_Lexeme (line : String ; index : Integer) return String;

end Lexical_Analyzer;
