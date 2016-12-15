###16 3Sum Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
       int result = nums[0] + nums[1] + nums[2];
		Arrays.sort(nums);
		
		for(int i = 0; i < nums.length -2; i ++){
			int h = i+1;
			int t = nums.length-1;
			while(h < t){
				int sum = nums[i] + nums[h] + nums[t];

				if(sum == target)
					return target;
				else if (sum < target)
					h++;
				else
					t--;
				
				result = Math.abs(result-target)<Math.abs(sum-target)?result:sum;
			}
		}
		return result;	
        
    }
}