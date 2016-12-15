###392 Is Subsequence

Given a string s and a string t, check if s is subsequence of t.


You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).


A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"


Return true.

Example 2:
s = "axc", t = "ahbgdc"


Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
Credits:Special thanks to @pbrother for adding this problem and creating all test cases.
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
s = "abc", t = "ahbgdc"

Return true.
Example 2:
s = "axc", t = "ahbgdc"

Return false.
Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?Credits:Special thanks to @pbrother for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length() == 0)
            return true;
        
        int index = 0;
        int l = t.length();
        char c = s.charAt(index);
        for(int i = 0; i < l; i ++){
            char c1 = t.charAt(i);
            if(c == c1){
                index ++;
                if(index >= s.length())
                    return true;
                else
                    c = s.charAt(index);
            }
        }
        
        return false;
    }
}