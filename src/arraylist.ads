package arraylist is
   
   type arraylist is array (Object range <>) of Object; 

   procedure addat (index : Integer; element : Object); 
   
   procedure removeat (index : Integer);
     
   procedure add (index : Integer; element : Object);

end arraylist;
