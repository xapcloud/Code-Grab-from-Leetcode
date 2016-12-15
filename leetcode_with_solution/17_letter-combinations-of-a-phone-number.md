###17 Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that the number could represent.


A mapping of digit to letters (just like on the telephone buttons) is given below.


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public static List<String> letterCombinations(String digits) {

		List<String> result = new ArrayList<String>();

		HashMap<Character, String> dic = new HashMap<Character, String>();




		dic.put('2', "abc");

		dic.put('3', "def");

		dic.put('4', "ghi");

		dic.put('5', "jkl");

		dic.put('6', "mno");

		dic.put('7', "pqrs");

		dic.put('8', "tuv");

		dic.put('9', "wxyz");

		dic.put('0', " ");




		Queue<String> q = new LinkedList<String>();




		for (int i = 0; i < digits.length(); i++) {

			String temp = dic.get(digits.charAt(i));

			if (q.size() == 0) {

				for (int j = 0; j < temp.length(); j++) {

					q.offer(temp.charAt(j) + "");

				}

			} else {

				int count = q.size();

				for(int j = 0; j < count; j ++){

					String x = q.poll();

					for(int k = 0; k < temp.length(); k ++){

						q.offer(x+temp.charAt(k));

					}

				}

			}

		}


        int t = q.size();

		for (int i = 0; i < t; i++) {

			result.add(q.poll());

		}




		// for(int i = 0; i < digits.length(); i ++){

		// String temp = dic.get(digits.charAt(i));

		// for(int j = 0; j < temp.length(); j ++){

		//

		// }

		//

		// }




		return result;




	}

}