###367 Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True


Example 2:

Input: 14
Returns: False


Credits:Special thanks to @elmirap for adding this problem and creating all test cases.Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.
Example 1:

Input: 16
Returns: True


Input: 16
Returns: True
Example 2:

Input: 14
Returns: False


Input: 14
Returns: False
Credits:Special thanks to @elmirap for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isPerfectSquare(int num) {
        boolean ret = false;
        for(int i = 0;i <= num/2+1; i ++){
            if(i*i== num)
                ret = true;
        }
        
        return ret;
    }
}