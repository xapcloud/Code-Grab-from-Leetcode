###326 Power of Three

    Given an integer, write a function to determine if it is a power of three.


Follow up:
    Could you do it without using any loop / recursion?

Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.
    Given an integer, write a function to determine if it is a power of three.

Follow up:
    Could you do it without using any loop / recursion?
Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isPowerOfThree(int n) {
       return ( n>0 &&  1162261467%n==0); 
    }
}