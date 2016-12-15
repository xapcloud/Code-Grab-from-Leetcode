###154 Find Minimum in Rotated Sorted Array II

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array may contain duplicates.Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?Would this affect the run-time complexity? How and why?Suppose a sorted array is rotated at some pivot unknown to you beforehand.(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).Find the minimum element.The array may contain duplicates.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int findMin(int[] nums) {
          int len = nums.length;
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < len ; i ++){
            min = min<nums[i]?min:nums[i];
        }
        
        return min;
    }
}