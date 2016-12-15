###268 Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.


Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    
     public int missingNumber(int[] nums) {
        int n = nums.length;
        
        int sum = 0;
        for(int i = 0; i <= n; i ++){
            sum+=i;
        }
     
        for(int i = 0; i < n; i ++){
            sum-=nums[i];
        }
     
        return sum;
     
         
     }
 
}