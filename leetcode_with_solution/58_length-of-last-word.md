###58 Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.If the last word does not exist, return 0.Note: A word is defined as a character sequence consists of non-space characters only.
For example, 
Given s = "Hello World",
return 5.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        if(s.length() == 0)
            return 0;
        int x = s.lastIndexOf(" ");
        if(x == -1)
            return s.length();
        return s.length() - x - 1;
        
        
    }
}