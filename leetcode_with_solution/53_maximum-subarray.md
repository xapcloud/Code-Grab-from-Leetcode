###53 Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.


For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
click to show more practice.If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int maxSubArray(int[] nums) {

        if(nums.length == 0)
            return 0;
        if(nums.length == 1)
            return nums[0];
        int maxSum = nums[0];
        int sum = nums[0];
    
    
        for(int i = 1; i < nums.length ; i ++){
            if(sum < 0)
                sum = 0;
            sum+=nums[i];
            maxSum = maxSum > sum ? maxSum: sum;
            
        }
        
        return maxSum;
        
    }
}