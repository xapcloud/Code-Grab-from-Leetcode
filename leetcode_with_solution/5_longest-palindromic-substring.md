###5 Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Example:

Input: "cbbd"

Output: "bb"

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"


Input: "cbbd"

Output: "bb"
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String longestPalindrome(String s) {
        int max = 0;
		String result = "";
		int length = s.length();
		char[] array = new char[length];
		array = s.toCharArray();

		for (int i = 0; i < length-1; i++) {
			if (array[i] == array[i + 1]) {
				if(max < 2){
					max = 2;
					result = array[i]+""+array[i+1];
				}
				int head = i;
				int tail = i + 1;
				while (head > 0 && tail < length - 1) {
					head = head - 1;
					tail = tail + 1;
					if (array[head] == array[tail]){
						if((tail-head+1)>max){
							max = tail-head+1;							
							result = s.substring(head,tail+1);
						}		
						continue;
					}
					else {
						if((tail-head-1)>max){
							max = tail-head-1;							
							result = s.substring(head+1,tail);
						}			
						break;
					}
				}

			}
			
			if(i<length-2&&array[i]==array[i+2]){
				if(max < 3){
					max = 3;
					result = array[i]+""+array[i+1]+array[i+2];
				}
				int head = i;
				int tail = i + 2;
				while (head > 0 && tail < length - 1) {
					head = head - 1;
					tail = tail + 1;
					if (array[head] == array[tail]){
						if((tail-head+1)>max){
							max = tail-head+1;							
							result = s.substring(head,tail+1);
						}		
						continue;
					}
					else {
						if((tail-head-1)>max){
							max = tail-head-1;							
							result = s.substring(head+1,tail);
						}			
						break;
					}
				}
			}	
		}
		if(max == 0)
			return s.charAt(0)+"";
		return result;
    }
}