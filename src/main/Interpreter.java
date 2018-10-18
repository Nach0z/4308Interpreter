package main;

import util.*;

public class Interpreter {

	public static void main(String[] args) {
		if(args.length == 0) {
			System.out.println("Please provide an input file to run.");
			return;
		}
			
		try {
			LexNode rootNode = new LexNode();
			LexAnalyzer analyzer = new LexAnalyzer(new TokenProvider(args[0]));
			
			analyzer.parse(rootNode, 0);
			
			
		} catch (Exception e) {
			System.out.println("Parsing broke! Something went wrong...");
			e.printStackTrace();
		}
	}

}
