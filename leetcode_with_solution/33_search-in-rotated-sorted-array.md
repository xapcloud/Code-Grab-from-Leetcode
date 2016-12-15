###33 Search in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.Suppose a sorted array is rotated at some pivot unknown to you beforehand.(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).You are given a target value to search. If found in the array return its index, otherwise return -1.You may assume no duplicate exists in the array.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int search(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++){
            if(target == nums[i])
                return i;
        }
        return -1;
    }
}
//gaoæç¬ãããããããããæ²¡æè¦æ±æçï¼O(n)å®å¨å¯ä»¥åã