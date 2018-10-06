package main;

import util.*;

public class Interpreter {

	public static void main(String[] args) {
		if(args.length == 0) {
			System.out.println("Please provide an input file to run.");
			return;
		}
			
		try {
			TokenProvider reader = new TokenProvider(args[0]);
			String token = null;
			LexNode rootNode = new LexNode();
			
			while((token = reader.nextToken()) != null) {
				LexAnalyzer analyzer = new LexAnalyzer();
				LexNode node = analyzer.GetNode(token);
				if (node == null)
					break;
				System.out.println("Found node: " + node.LexID);
			}
		} catch (Exception e) {
			System.out.println("Parsing broke! Something went wrong...");
			e.printStackTrace();
		}
	}

}
