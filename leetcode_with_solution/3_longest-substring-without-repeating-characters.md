###3 Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.Given a string, find the length of the longest substring without repeating characters.Examples:Given "abcabcbb", the answer is "abc", which the length is 3.Given "bbbbb", the answer is "b", with the length of 1.Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    static int[] last = new int[128];
	public static int lengthOfLongestSubstring(String s) {
	    int start = 0;
        int len = 0;
        char[] w = new char[s.length()];
        w = s.toCharArray();
        for(int i = 0; i < 128; i++)
            last[i] = -1;//lastæ°ç»ç¨äºä¿å­æ°åºç°çå­ç¬¦çä¸æ ï¼ä¸å¼å§å¨é¨åå§åä¸º-1
        for(int i = 0; i < s.length(); ++ i){
            if(last[w[i]-' '] >= start){ //å½åè¿ä¸ªå­ç¬¦åºç°è¿
                if(i-start > len)
                    len = i-start;
                start = last[w[i]-' '] + 1; //ä»è¿ä¸ªå­ç¬¦é¦æ¬¡åºç°çä½ç½®+1ï¼éæ°æ«æï¼ç¸å½äºæåé¢æå¼åé¢çå­ç¬¦ä¸²ä¸è°
            }
                last[w[i]-' '] = i;//æ´æ°å½åå­ç¬¦çä¸æ 
        }
        if(len > s.length() - start)//éå¯¹æ²¡æéå¤å­ç¬¦çå­ç¬¦ä¸²
            return len;
        else
            return s.length() - start;
	}
}