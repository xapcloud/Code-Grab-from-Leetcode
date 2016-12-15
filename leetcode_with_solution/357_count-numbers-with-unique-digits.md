###357 Count Numbers with Unique Digits
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


A direct way is to use the backtracking approach.
Backtracking should contains three states which are (the current number, number of steps to get that number and a bitmask which represent which number is marked as visited so far in the current number). Start with state (0,0,0) and count all valid number till we reach number of steps equals to 10n.
This problem can also be solved using a dynamic programming approach and some knowledge of combinatorics.
Let f(k) = count of numbers with unique digits with length equals k.
f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) [The first factor is 9 because a number cannot start with 0].

Credits:Special thanks to @memoryless for adding this problem and creating all test cases.Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
Credits:Special thanks to @memoryless for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        //è¿ä¹ç®å¨æè§åï¼ å¹¶æ²¡æbackrackingåãããä¸è·¯èµ°å°åºåããã
        //æè·¯ï¼ Stringå­å½åçæ°å­ï¼ç¶åå¾åè¿½å æ°å­ï¼ä¿è¯unique
        //ä¸è·¯æ°ä¸å»ãã
     
        if(n == 0)
            return 1;
        if(n == 1)
            return 10;
            
        int result = 0;
        for(int i = 1; i < 10; i ++){
            result += helper(n-1,i+"");
        }
      
        return result+1;
    }
    
    
    private int helper(int n,String curStr){
        if(n < 1){
            return 1;
        }else{
            int result = 0;
            for(int i = 0; i < 10; i ++){
               if(!curStr.contains(i+""))
                    result+=helper(n-1,curStr+""+i);
            } 
            
           return result+1; 
        }
        
    }
}