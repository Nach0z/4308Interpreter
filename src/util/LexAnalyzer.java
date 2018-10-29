package util;

import java.util.*;
import java.util.function.IntSupplier;
import java.util.stream.Collectors;

public class LexAnalyzer {
	ArrayList<LexNode> allNodes = new ArrayList<LexNode>();
	
	public int parseNodeIndex = 0;
	public int lookaheadIndex = 0;
	
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
	
	public int parse(LexNode currentNode) {
		while(subGrammars(GetNode(currentNode.LexID), parseNodeIndex).size() > 0)
		{
			LexNode funct = parseFunction(currentNode);
		}
	}
	
	public LexNode parseFunction(LexNode currentNode) {
		if(!allNodes.get(lookaheadIndex++).equals(1))
			throw new RuntimeException("Failed to parse function at index " + lookaheadIndex);
		if(!allNodes.get(lookaheadIndex++).equals(2))
			throw new RuntimeException("Failed to parse function at index " + lookaheadIndex);
		if(!allNodes.get(lookaheadIndex++).equals(3))
			throw new RuntimeException("Failed to parse function at index " + lookaheadIndex);
		if(subGrammars(GetNode(27), lookaheadIndex++).size() <= 0)
			throw new RuntimeException("Failed to parse block at index " + lookaheadIndex);
		LexNode block = parseBlock(allNodes.get(lookaheadIndex));
		currentNode.doAction = () -> {
			return block.doAction.getAsInt();
		};
		if(!allNodes.get(lookaheadIndex++).equals(4))
			throw new RuntimeException("Failed to parse function at index " + lookaheadIndex);
		return currentNode;
	}
	
	public LexNode parseBlock(LexNode currentNode) {
		List<LexNode> statements = new ArrayList<LexNode>();
		while(subGrammars(GetNode(currentNode.LexID), lookaheadIndex).size() > 0)
		{
			statements.add(parseStatement(allNodes.get(lookaheadIndex++)));
		}
		currentNode.doAction = () -> {
			for(LexNode statement : statements)
				statement.doAction.getAsInt();
			return 0;
		};
		
		return currentNode;
	}
	
	public LexNode parseStatement(LexNode currentNode) {
		int statementType = subGrammars(GetNode(currentNode.LexID), lookaheadIndex);
		LexNode subNode = null;
		if(statementType == 0) // if
		{
			subNode = parseIf(allNodes.get(lookaheadIndex));
		}
		else if (statementType == 1) // assign
		{
			subNode = parseAssign(allNodes.get(lookaheadIndex));
		}
		else if (statementType == 2) // while
		{
			subNode = parseWhile(allNodes.get(lookaheadIndex));
		}
		else if (statementType == 3) // print
		{
			subNode = parsePrint(allNodes.get(lookaheadIndex));
		}
		else if (statementType == 4) // for
		{
			subNode = parseFor(allNodes.get(lookaheadIndex));
		}
		
		currentNode.doAction = () -> {
			return subNode.doAction.getAsInt();
		};
		return currentNode;
	}
	
	public LexNode parseIf(LexNode currentNode) {
		if(!allNodes.get(lookaheadIndex++).equals(5))
			throw new RuntimeException("Failed to parse if_statement at index " + lookaheadIndex);
		LexNode conditional = parseBoolExpr(allNodes.get(lookaheadIndex++));
		LexNode block = parseBlock(allNodes.get(lookaheadIndex++));
		if(!allNodes.get(lookaheadIndex++).equals(6))
			throw new RuntimeException("Failed to parse else_statement at index " + lookaheadIndex);
		LexNode block2 = parseBlock(allNodes.get(lookaheadIndex++));
		currentNode.doAction = () -> {
			if(conditional.doAction.getAsInt() == 0)
				return block.doAction.getAsInt();
			else
				return block2.doAction.getAsInt();
		};
		
		return currentNode;
	}
	
	public LexNode parseBoolExpr(LexNode currentNode) {
		
	}
	
	public int parse(LexNode currentNode, int index) {
		Lexeme thisNode = GetNode(currentNode.LexID);
		ArrayList<Integer> grammarIndexes = subGrammars(thisNode, index);
		for(int grammarIdx = 0; grammarIdx < grammarIndexes.size(); grammarIdx++) {
			
		}		
	}
	
	
	
	
	
	public boolean validSubNode(Lexeme currentNode, LexNode lookahead) {
		int target = lookahead.LexID;
		ArrayList<ArrayList<Integer>> allStatements = LexNode.NodeGrammar(currentNode.LexID);
		for(int grammarIndex = 0; grammarIndex < allStatements.size(); grammarIndex++) {
			ArrayList<Integer> statement = allStatements.get(grammarIndex);
			int possible = statement.get(0);
			if(GetNode(possible).hasPrefix) {
				if(target == possible)
					return true;
			} else {
				return validSubNode(GetNode(possible), lookahead);
			}
		}
		return false;
	}
	
	public ArrayList<Integer> subGrammars(Lexeme currentNode, int index) {
		ArrayList<Integer> retVals = new ArrayList<Integer>();
		ArrayList<ArrayList<Integer>> allStatements = LexNode.NodeGrammar(currentNode.LexID);
		int target = allNodes.get(index).LexID;
		for(int grammarIndex = 0; grammarIndex < allStatements.size(); grammarIndex++) {
		// for(ArrayList<Integer> statement : allStatements) {
			ArrayList<Integer> statement = allStatements.get(grammarIndex);
			int possible = statement.get(0); // we're specifically searching for the first item in the possible grammars.
			if(GetNode(possible).hasPrefix) {
				if(target == GetNode(possible).LexID)
					retVals.add(grammarIndex);
			} else {
				if(subGrammars(GetNode(possible), index).size() > 0) {
					retVals.add(grammarIndex);
				}
			}
		}
		return retVals;
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
		new Lexeme(null, 35, false), // relative op
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
