package body Token is

   
   type token is new Controlled with private; 
   
   --type a_token is new Controlled with public;
   
   token_ID : Integer;
   lex : String;
   row : Integer;
   column : Integer;
   
   function Create(token_ID : Integer; lex : String; row : Integer; column : Integer) return token is 
      
      if token_ID == null then 
         raise Invalid_Argument with "one of the token value is invalid!";
         
      elsif lex == null then 
         raise Invalid_Argument with "one of the token value is invalid!";
          
      elsif row == null then
         raise Invalid_Argument with "invalid row!";
                 
      elsif column == null then
         raise Invalid_Argument with "invalid column";
         
      else
         token_ID := token_ID;
         lex := String;
         row := Integer;
         column := Integer;
      end if;
      
   end Create;
   
                          
   --TODO: Find a way to access the variables addressed below. Created a contructor like instance but need to 
   --      figure out how to use those variables created.
   function get_token_type return Integer is 
      
      return token_type'Val(token_ID);
      
   end get_token_type;
   
   
   function get_row return Integer is 
      
      return row;
      
   end get_row;
   
   
   function get_Col return Integer is
      
      return column;
      
   end get_Col;
   
   
   function get_lex return String is 
      
      return lex;
      
   end get_lex;
   
   --TODO: implement a str testing method like the one from the python version

end Token;
