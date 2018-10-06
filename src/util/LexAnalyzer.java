package util;

import java.util.*;
import java.util.function.IntSupplier;
import java.util.stream.Collectors;

public class LexAnalyzer {
	public static HashMap<String, Integer> Globals = new HashMap<String, Integer>();
	
	public static List<Lexeme> allLexes = new ArrayList<Lexeme>(Arrays.asList(new Lexeme[]{
		new Lexeme(null, -2), // Numerical constants
		new Lexeme(null, -1), // IDs
		new Lexeme("function", 1), // begin function
		new Lexeme("(", 2), // open paren
		new Lexeme(")", 3), // close paren
		new Lexeme("end", 4), // end statement
		new Lexeme("if", 5), // if statement
		new Lexeme("else", 6), // else statement
		new Lexeme("while", 7), // while statement
		new Lexeme("for", 8), // for statement
		new Lexeme("print", 9),// print statement
		new Lexeme(":", 10), // iterate operator
		new Lexeme("=", 11), // assign operator
		new Lexeme("<=", 12), // lessOrEq operator
		new Lexeme(">=", 13), // moreOrEq operator
		new Lexeme("<", 14), // lessThan operator
		new Lexeme(">", 15), // moreThan operator
		new Lexeme("==", 16), // equality operator
		new Lexeme("!=", 17), // inequality operator
		new Lexeme("+", 18), // addition operator
		new Lexeme("-", 19), // subtract operator
		new Lexeme("*", 20), // mult operator
		new Lexeme("/", 21), // divide operator
		new Lexeme("\\", 22), // typo'd divide operator
		new Lexeme("%", 23), // modulo operator
		new Lexeme("^", 24), // exponent operator
	}));
	public static LexNode GetNode(String token) {
		List<Lexeme> keywords = allLexes.stream().filter(x -> x.LexToken != null && x.LexToken.equalsIgnoreCase(token)).collect(Collectors.toList());
		LexNode ret = new LexNode();
		if(keywords.size() == 0)
		{
			// wasn't a matched reserved keyword - must be an ID or numerical constant.	
			if(token.matches("[a-zA-Z]")) {
				// ID, because alphanumeric.
				if(!Globals.containsKey(token))
					Globals.put(token, 0);
				ret.LexID = -1;
				ret.doAction = new IntSupplier() { // returns from the global variables list.
					@Override
					public int getAsInt() {
						return Globals.get(token); 
					}
				};
			} else {
				ret.LexID = -2;
				ret.doAction = new IntSupplier() { // returns a const value.
					
					@Override
					public int getAsInt() {
						return Integer.parseInt(token);
					}
				};
			}
		} else {
			ret.LexID = keywords.get(0).LexID;
		}
		return ret;
	}
}
