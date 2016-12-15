###172 Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
Credits:Special thanks to @ts for adding this problem and creating all test cases.Given an integer n, return the number of trailing zeroes in n!.Note: Your solution should be in logarithmic time complexity.Credits:Special thanks to @ts for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
     public int trailingZeroes(int n) {
        int num = 0;
        
        while(n>1){
            num+=(n/=5);
        }
        
        return num;
     }
    
    // public int trailingZeroes(int n) {
    //     int f = fac(n);
        
    //     int count = 0;
    //     while(f%10 == 0){
    //         count++;
    //         f = f/10;
    //     }
        
    //     return count;
    // }
    
    // private int fac(int n){
    //     if(n == 0)
    //         return 1;
            
    //     int result = 1;
    //     for(int i = 1; i <= n; i++ ){
    //         result*=i;
    //     }
        
    //     return result;
    // }
}