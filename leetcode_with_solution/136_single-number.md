###136 Single Number
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int singleNumber(int[] nums) {
        int ret = 0;
        for(int i = 0; i < nums.length;i ++){
            ret = ret^nums[i];
        }
        return ret;
    }
}