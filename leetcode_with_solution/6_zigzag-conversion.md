###6 ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R


And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R


And then read line by line: "PAHNAPLSIIGYIR"
P   A   H   N
A P L S I I G
Y   I   R

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
string convert(string text, int nRows);Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1)
			return s;
      	String result = "";
		for (int i = 0; i < numRows; i++) {
			for (int j = i; j < s.length(); j += (numRows - 1) * 2) {
				result += s.charAt(j);
				if (i != 0 && i != numRows - 1) {
					if (j + (numRows - 1 - i) * 2 < s.length())
						result += s.charAt(j + (numRows - 1 - i) * 2);
				}
			}
		}
		return result;
    }
}