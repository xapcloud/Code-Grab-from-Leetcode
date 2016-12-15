###151 Reverse Words in a String

Given an input string, reverse the string word by word.


For example,
Given s = "the sky is blue",
return "blue is sky the".


Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.
Clarification:


What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.



Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
click to show clarification.

What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String reverseWords(String s) {
        String [] sl = s.split("\\s+");
        String result = "";
        for(int i = 0; i < sl.length; i ++){
            result+=" "+sl[sl.length-1-i];
        }

        return result.trim();
    }
}