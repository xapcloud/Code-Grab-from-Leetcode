###41 First Missing Positive

Given an unsorted integer array, find the first missing positive integer.


For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.


Your algorithm should run in O(n) time and uses constant space.

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int firstMissingPositive(int[] nums) {
        
        if(nums.length == 0)
            return 1;
        if(nums.length == 1)
            return nums[0]==1?2:1;
        
        int i ;
        for(i = 0; i < nums.length;){
            if(nums[i] <= 0 || nums[i] >= nums.length || nums[i] == i+1  || nums[i] == nums[nums[i]-1]){
                i++;
            }else{
                int temp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = temp;
            }
        }
        for(i = 0; i < nums.length; i ++){
            if(nums[i] != i+1)
                break;
            
        }
        
        return ++i;
    }
}