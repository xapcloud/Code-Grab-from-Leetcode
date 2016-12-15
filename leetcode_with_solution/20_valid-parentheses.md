###20 Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
   	public  boolean isValid(String s) {

		if (s.length() % 2 != 0)
			return false;
		if (s.length() == 0)
			return true;
		
		char c = s.charAt(0);
		
		if(c ==')'|| c ==']' || c=='}')
			return false;
		
		
		int pairIndex = findNext(s.substring(1), c);
		
		//System.out.println(pairIndex);
		//System.out.println(s.substring(1, pairIndex + 1));
		//System.out.println(s.substring(pairIndex + 2));

		if (pairIndex == -1)
			return false;
		else
			return isValid(s.substring(1, pairIndex + 1))
					&& isValid(s.substring(pairIndex + 2));
	}

	private  int findNext(String s, char c) {
		//System.out.print("--------------\n");

		HashMap<Character, Character> h = new HashMap<Character, Character>();
		h.put('(', ')');
		h.put('[', ']');
		h.put('{', '}');
		
		int count = 1;

		for (int i = 0; i < s.length(); i++) {
			
			
			
			if(s.charAt(i) == c)
				count++;
			if(s.charAt(i) == h.get(c))
				count--;
			
			//System.out.println(s.charAt(i)+" "+count);
			if (count ==0 &&s.charAt(i) == h.get(c))
				return i;
		}
		return -1;
	}
}