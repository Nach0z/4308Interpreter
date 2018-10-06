package util;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

public class TokenProvider {
	protected BufferedReader buf;
	protected ArrayList<String> currentLine = new ArrayList<String>();
	public TokenProvider(String fileName) throws FileNotFoundException {
		buf = new BufferedReader(new FileReader(fileName));
	}
	
	public String nextToken() {
		System.out.println("Begin nextToken");
		String tmp = null; // this is just to store the next line of the file
		try {
			if(currentLine.size() == 0 && (tmp = buf.readLine()) == null) { // if we have nothing to return and the file is empty, return null
				return null;
			} else {
				if(currentLine.size() == 0) // we've already reached the end of this line
					currentLine = new ArrayList<String>(Arrays.asList(tmp.split(" "))); // woo. we already read the next line. Turn it into an arraylist.
				String word = currentLine.get(0); // store the first lex
				currentLine.remove(0); // remove it from the line buffer
				System.out.println("Popped " + word);
				if(LexAnalyzer.allLexes.stream().filter(x -> x.LexToken != null && x.LexToken.equals(word)).collect(Collectors.toList()).size() > 0)
					return word; // shortcut for full-word known lexes
				String ret = "";
				for(int ic : word.chars().toArray()) {
					char cc = (char)ic; // need a char
					if(ret.length() == 0) {
						ret += cc;
						continue; // skip the first iteration. 
					}
					String retP = ret + cc;
					if(LexAnalyzer.allLexes.stream().filter(x -> x.LexToken != null && x.LexToken.startsWith(retP)).collect(Collectors.toList()).size() > 0) // 1-char lookahead for longest match
					{
						ret += cc;
						continue;
					}
					else
					{
						if(ret.equals(word)) // we're returning this entire word.
							break;
						else // not returning the whole word (i.e., in spaceless math statements
							// currentLine.add(0, word.replaceFirst(ret, ""));
							{
								currentLine.add(0, word.substring(ret.length(), word.length()));
								System.out.println("Word not used up, re-pushing " + currentLine.get(0));
								break;
							}
					}
				}
				System.out.println("Returning " + ret);
				return ret; // give lex pls
			}
		} catch(IOException e) {
			e.printStackTrace();
			return null;
		} finally {
			System.out.println("End nextToken");
		}
	}
}
