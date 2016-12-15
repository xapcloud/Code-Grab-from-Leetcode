###34 Search for a Range
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
Given a sorted array of integers, find the starting and ending position of a given target value.Your algorithm's runtime complexity must be in the order of O(log n).If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[2];
        boolean f = false;
        for(int i = 0; i < nums.length; i++){
            if(target == nums[i]){
                result[0] = i;
                f = true;
                break;
            }
        }
        if(!f){
            result[0] = -1;
            result[1] = -1;
            return result;
        }
        
        for(int i = nums.length - 1; i >= 0; i--){
            if(target == nums[i]){
                result[1] = i;
                break;
            }
        }
        
        return result;
        
        
    }
}