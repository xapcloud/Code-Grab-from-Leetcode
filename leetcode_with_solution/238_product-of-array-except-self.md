###238 Product of Array Except Self

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Solve it without division and in O(n).
For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

Subscribe to see which companies asked this question


Show Tags

Array



Show Similar Problems

 (H) Trapping Rain Water
 (M) Maximum Product Subarray
 (H) Paint House II



Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].Solve it without division and in O(n).For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        int [] result = new int [nums.length];
        
        for(int i = 0; i < nums.length ; i ++){
            result[i] = i == 0?1:result[i-1]*nums[i-1];
        }
        
        int right = 1;
        for(int i = nums.length -1 ; i >= 0; i --){
            result[i] *= right;
            right *= nums[i];
        }

        return result;
    }
}