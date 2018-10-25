package util;

import java.util.*;
import java.util.function.IntSupplier;
import java.util.stream.Collectors;

public class LexAnalyzer {
	ArrayList<LexNode> allNodes = new ArrayList<LexNode>();
	public LexAnalyzer(TokenProvider reader) {
		init(reader);
	}
	
	public void init(TokenProvider reader) {
		String token = null;
		while((token = reader.nextToken()) != null) {
			LexNode node = GetNode(token);
			if (node == null)
				break;
			System.out.println("Found node: " + node.LexID);
			allNodes.add(node);
		}
	}
	
	public int parse(LexNode currentNode, int index) {
		int nextNodeID = allNodes.get(index).LexID;
		searchSubtree(currentNode.LexID, nextNodeID)
		
		for(int i = index; i < allNodes.size(); i++) {
			i += parse(allNodes.get(i), i);
		}
	}
	
	public int searchSubtree(int nodeID, int target) {
		ArrayList<ArrayList<Integer>> allStatements = LexNode.NodeGrammar(nodeID);
		for(ArrayList<Integer> statement : allStatements) {
			int possible = statement.get(0); // we're specifically searching for the first item in the possible grammars.
			if(GetNode(possible).hasPrefix) {
				if(target == GetNode(possible).LexID)
					return possible;
			} else {
				return searchSubtree(possible, target);
			}
		}
		return -1;
	}
	
	public static HashMap<String, Integer> Globals = new HashMap<String, Integer>();
	
	
	
	public static List<Lexeme> allLexes = new ArrayList<Lexeme>(Arrays.asList(new Lexeme[]{
		new Lexeme(null, 0, false), // ROOT PROGRAM
		new Lexeme("function", 1, true), // begin function
		new Lexeme("(", 2, true), // open paren
		new Lexeme(")", 3, true), // close paren
		new Lexeme("end", 4, true), // end statement
		new Lexeme("if", 5, true), // if statement
		new Lexeme("else", 6, true), // else statement
		new Lexeme("while", 7, true), // while statement
		new Lexeme("for", 8, true), // for statement
		new Lexeme("print", 9, true),// print statement
		new Lexeme(":", 10, true), // iterate operator
		new Lexeme("=", 11, true), // assign operator
		new Lexeme("<=", 12, true), // lessOrEq operator
		new Lexeme(">=", 13, true), // moreOrEq operator
		new Lexeme("<", 14, true), // lessThan operator
		new Lexeme(">", 15, true), // moreThan operator
		new Lexeme("==", 16, true), // equality operator
		new Lexeme("!=", 17, true), // inequality operator
		new Lexeme("+", 18, true), // addition operator
		new Lexeme("-", 19, true), // subtract operator
		new Lexeme("*", 20, true), // mult operator
		new Lexeme("/", 21, true), // divide operator
		new Lexeme("\\", 22, true), // typo'd divide operator
		new Lexeme("%", 23, true), // modulo operator
		new Lexeme("^", 24, true), // exponent operator
		new Lexeme(null, 25, false), // Numerical constants
		new Lexeme(null, 26, false), // IDs
		new Lexeme(null, 27, false), // block 
		new Lexeme(null, 28, false), // statement
		new Lexeme(null, 29, false), // general boolean statement
		new Lexeme(null, 30, false), // iter
		new Lexeme(null, 31, false), // arith expression
		new Lexeme(null, 32, false), // assign statement
		new Lexeme(null, 33, false), // binary expression (not boolean stmt!)
		new Lexeme(null, 34, false), // arith OP (not arith expression!)
	}));
	
	public static Lexeme GetNode(int id) {
		
		return allLexes.stream().filter(x -> x.LexID == id).collect(Collectors.toList()).get(0);
	}
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
