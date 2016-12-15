###343 Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.


For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).


Note: You may assume that n is not less than 2 and not larger than 58.


There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    // public int integerBreak(int n) {
    //     if(n<=2)
    //         return 1;
            
    //     int max = 0;
        
    //     for(int i = 1; i < n; i ++){
    //         max = Math.max(max,i*helper(n-i));
    //     }
        
    //     return max;
    // }
    
    // private int helper(int n ){
        
    //     int max = n; 
        
    //     for(int i = 1; i < n; i ++){
    //       max = Math.max(max,i*helper(n-i)); 
    //     }
        
    //     return max;
    // }
    //éå¤è®¡ç®å¤ªå¤ ï¼å¯¼è´è¶æ¶
    
    public int integerBreak(int n){
        if(n <= 2)
            return 1;
        if(n == 3)
            return 2;
        
        int [] max = new int [n];
        max[0] = 1;
        max[1] = 2;
        max[2] = 3;
        

        for(int i = 3; i < n ; i++){
            
            for(int j = 1; j <= i; j ++){
                max[i] = Math.max(max[i],j*max[i-j]);
            }
        }
        
        return max[n-1];
    }
}
