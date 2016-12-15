###168 Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
Credits:Special thanks to @ifanchu for adding this problem and creating all test cases.Given a positive integer, return its corresponding column title as appear in an Excel sheet.For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB Credits:Special thanks to @ifanchu for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String convertToTitle(int n) {
        n  = n - 1 ;
        String result = "";
        while(n>=26){
            int reminder = n % 26;
            n = n/26-1;
            result = (char)('A'+reminder) + result;
        }
        
        result = (char)('A'+n)+result;
        
        return result;
    }
}