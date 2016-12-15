###1 Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].



UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
Given an array of integers, return indices of the two numbers such that they add up to a specific target.You may assume that each input would have exactly one solution.
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int index1 = 0, index2= 0;
		int [] result = new int[2];
		
		boolean flag = false;
		
		for(int i = 0 ;i < nums.length; i ++){			
			for(int j = i+1 ; j < nums.length; j ++){
				
				if(nums[i]+nums[j]==target){
					index1 = i;
					index2 = j;
					flag = true;
					break;
				}
			}
			if(flag == true)
				break;
		}
			result[0]= index1+1;
			result[1]= index2+1;
			return result;
    }
}