###231 Power of Two

Given an integer, write a function to determine if it is a power of two.

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Given an integer, write a function to determine if it is a power of two.
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isPowerOfTwo(int n) {
        
        while(n>=2&&n%2==0)
            n/=2;
            
        return n == 1;
        
    }
}