package util;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

public class TokenProvider {
	protected BufferedReader buf;
	protected ArrayList<String> currentLine = new ArrayList<String>();
	public TokenProvider(String fileName) throws FileNotFoundException {
		buf = new BufferedReader(new FileReader(fileName));
	}
	
	public String nextToken() {
		String tmp = null; // this is just to store the next line of the file
		try {
			if(currentLine.size() == 0 && (tmp = buf.readLine()) == null) { // if we have nothing to return and the file is empty, return null
				return null;
			} else {
				if(currentLine.size() == 0) // we've already reached the end of this line
					currentLine = new ArrayList<String>(Arrays.asList(tmp.split(" "))); // woo. we already read the next line. Turn it into an arraylist.
				String ret = currentLine.get(0); // store the first lex
				currentLine.remove(0); // remove it from the line buffer
				return ret; // give lex pls
			}
		} catch(IOException e) {
			return null;
		}
	}
}
