with Ada.Exceptions; use Ada.Exceptions;
with Token;
with Ada.Finalization; use Ada.Finalization;
  
package a_token is
   
   type a_token is new Controlled with private; 
  
   function Create(token_ID : Integer; lex : String; row : Integer; column : Integer) return a_token;
   
                          
   --TODO: Find a way to access the variables addressed below. Created a contructor like instance but need to 
   --      figure out how to use those variables created.
   function get_token_type return Integer;

   
   
   function get_row return Integer;
   
   
   function get_Col return Integer;
   
   
   function get_lex return String;
      
 
   
   --TODO: implement a str testing method like the one from the python version
   

end a_token;
