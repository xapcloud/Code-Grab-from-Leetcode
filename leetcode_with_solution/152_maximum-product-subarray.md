###152 Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.


For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int maxProduct(int[] nums) {
        if(nums == null || nums.length == 0)
            return 0;
        
        int result = nums[0];
        int max = nums[0];
        int min = nums[0];
        
        for(int i = 1; i < nums.length; i ++){
            int a = max*nums[i];
            int b = min*nums[i];
            
            max = Math.max(Math.max(a,b),nums[i]);
            min = Math.min(Math.min(a,b),nums[i]);
            result = Math.max(result,max);
        }
        
        return result;
    }
}