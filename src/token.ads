with Ada.Exceptions; use Ada.Exceptions;
with Token_Type;
with Ada.Finalization; use Ada.Finalization;
package Token is
   
   --TODO: Find a way to access the variables addressed below. Created a contructor like instance but need to 
   --      figure out how to use those variables created
   
   function get_token_type return Integer;

   
   
   function get_row return Integer;
   
   
   function get_Col return Integer;
   
   
   function get_lex return String;
     
   --TODO: implement a str testing method like the one from the python version 

end Token;
