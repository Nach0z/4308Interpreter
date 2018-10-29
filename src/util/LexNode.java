package util;

import java.util.ArrayList;
import java.util.Collections;
import java.util.function.*;

public class LexNode {
	public static ArrayList<ArrayList<Integer>> NodeGrammar(int thisNode) {
		// TODO deal with multi-option grammar blocks
		ArrayList<ArrayList<Integer>> grammar = new ArrayList<ArrayList<Integer>>();
		switch(thisNode) {
		case 0:
			Collections.addAll(grammar, new ArrayList<Integer>() {{ add(1); }});
		case 1:
			Collections.addAll(grammar, new ArrayList<Integer>() {{
				add(1); 
				add(26); 
				add(2);
				add(3);
				add(27);
				add(4);
			}});
			break;
		case 5:
			Collections.addAll(grammar, new ArrayList<Integer>(){{
				add(5);
				add(29);
				add(27);
				add(6);
				add(27);
				add(4);
			}});
			break;
		case 7: 
			Collections.addAll(grammar,  new ArrayList<Integer>() {{
				add(7);
				add(29);
				add(27);
				add(4);
			}});
			break;
		case 8: 
			Collections.addAll(grammar,  new ArrayList<Integer>() {{
				add(8);
				add(26);
				add(11);
				add(30);
				add(27);
				add(4);
			}});
			break;
		case 9:
			Collections.addAll(grammar,  new ArrayList<Integer>() {{
				add(9);
				add(2);
				add(31);
				add(3);
			}});
			break;
		case 28:
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(5);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(32);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(7);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(9);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(8);}});
			break;
			
		case 29:
			Collections.addAll(grammar,  new ArrayList<Integer>() {{
				add(35);
				add(31);
				add(31);
			}});
		case 31:
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(26);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(25);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(33);}});
			break;
		case 32:
			Collections.addAll(grammar, new ArrayList<Integer>() {{
				add(26);
				add(11);
				add(31);
			}});
			break;
		case 33:
			Collections.addAll(grammar, new ArrayList<Integer>() {{
				add(34);
				add(31);
				add(31); // duplicates! oh wow. Also, self-referencing.
			}});
			break;
		case 34:
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(18);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(19);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(20);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(21);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(22);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(23);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{add(24);}});
			break;
		case 35:
			Collections.addAll(grammar, new ArrayList<Integer>() {{ add(12);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{ add(13);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{ add(14);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{ add(15);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{ add(16);}});
			Collections.addAll(grammar, new ArrayList<Integer>() {{ add(17);}});
		case -1:
		case -2:
		case 4:
		default:
			break;
		}
		return grammar;
		
	}
	
	
	public int LexID;
	public int[] AvailableSubIDs;
	public ArrayList<LexNode> SubNodes;
	public IntSupplier doAction;
	
	
}
