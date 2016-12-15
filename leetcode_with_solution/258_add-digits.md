###258 Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. 


For example:


Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?


A naive implementation of the above process is trivial. Could you come up with other methods? 
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. 

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int addDigits(int num) {
        
        while(num>=10){
            int t = 0;
            
            while(num >=10){
                t += num%10;
                num = num/10;
            }
            t+=num;
            num = t;
        }
        return num;
    }
}