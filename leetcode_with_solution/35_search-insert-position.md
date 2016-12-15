###35 Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int searchInsert(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == target)
                return i;
        }
        
        for(int i = 0; i < nums.length - 1; i++){
            if(nums[i] < target && nums[i+1]>=target)
                return i+1;
        }
        
        if(target<nums[0])
            return 0;
        
        return target>nums[nums.length-1]?nums.length:(nums.length-1);
        
    }
}