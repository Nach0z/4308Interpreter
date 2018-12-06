use Token;
use a_token;


package lexical_Analyzer is
   ---TODO: Make the array below a dyanmic array to store values of Type Token
   array (list_of_tokens range <>) of a_token;
   
   procedure getList is
      
      Input_Code : File_Type;   
      C : Character;
     
   begin 
   
      Ada.Text_IO.Open (File => Input_Code, Mode => In_File,Name => "testcode.txt");
      
      while not End_Of_File(Input_Code) loop 
         
         Ada.Text_IO.Get (File => Input, Item => C);
         Ada.Text_IO.Put (Item = C);
         
         list_of_tokens.ff
       
         Ada.Text_IO.New_Line;
         
      end;
      
      Ada.Text_IO.Close;  
   
   end; 
   
   function has_tokens return Boolean is
      
   begin 
      
      if list_of_tokens.length == 0 then 
         return False;
         
      else 
         return True;
         
      end if;
      
   end;
      
   function get_Token_ID  (row : Integer, column : Integer, lex : String) return Integer is 
      
      --TODO Finish the token ID method
      
      Assert lex != null;
      
      tid : Integer;
      
   begin 
      tid = 0;
      
   end;      
         

end lexical_Analyzer;
