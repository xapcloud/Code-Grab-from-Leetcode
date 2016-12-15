###342 Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true.
Given num = 5, return false.


Follow up: Could you solve it without loops/recursion?

Credits:Special thanks to @yukuairoy  for adding this problem and creating all test cases.
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Example:
Given num = 16, return true.
Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
Credits:Special thanks to @yukuairoy  for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isPowerOfFour(int num) {
        return num > 0 && (num & (num - 1)) == 0 && (num & 0x55555555) == num;
    }
}