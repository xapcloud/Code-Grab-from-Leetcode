###171 Excel Sheet Column Number
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
Credits:Special thanks to @ts for adding this problem and creating all test cases.Related to question Excel Sheet Column TitleGiven a column title as appear in an Excel sheet, return its corresponding column number.For example:    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 Credits:Special thanks to @ts for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int titleToNumber(String s) {
        if(s.length() == 0)
            return 0;
        
        int difference = 'A' - 1;
        
        int result = 0;
        int l = s.length();
        
        for(int i = l -1; i >= 0; i --){
            char c = s.charAt(i);
            result = result + (c-difference)*(int)Math.pow(26,l-1-i); 
        }
        
        return result;
        
        
    }
}