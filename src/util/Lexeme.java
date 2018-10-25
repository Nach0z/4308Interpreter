package util;

public class Lexeme {
	public String LexToken;
	public int LexID;
	public boolean hasPrefix;
	public Lexeme(String lexToken, int lexID, boolean hasPrefix) {
		this.LexToken = lexToken;
		this.LexID = lexID;
		this.hasPrefix = hasPrefix;
	}
}
