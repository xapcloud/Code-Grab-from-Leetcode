###22 Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


For example, given n = 3, a solution set is:


[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> l = new ArrayList<String>();
		if (n == 0) {
			l.add("");
			return l;
		}

		if (n == 1) {
			l.add("()");
			return l;
		}

		if (n == 2) {
			l.add("()()");
			l.add("(())");
			return l;
		}

		for (int i = 0; i < n; i++) {

			List<String> l1 = generateParenthesis(i);
			List<String> l2 = generateParenthesis(n - 1 - i);

			for (int j = 0; j < l1.size(); j++) {
				for (int k = 0; k < l2.size(); k++) {
					String temp = "(" + l1.get(j) + ")" + l2.get(k);
					l.add(temp);
				}
			}

		}

		return l;
    }
}