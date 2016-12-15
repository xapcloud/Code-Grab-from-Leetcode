###283 Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.


For example, given nums  = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].


Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.


Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums  = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public void moveZeroes(int[] nums) {
        
        for(int i = 0 ;i < nums.length -1 ; i ++){
            if(nums[i] == 0){
                for(int j = i; j < nums.length - 1; j++){
                    int t = nums[j+1];
                    nums[j+1] = nums[j];
                    nums[j] = t;
                }
                
            }
        }
        ///////æ´åè§£å³ä¸¤ä¸ª 0 ç´§é»dç´§é»çæåµ 
        for(int i = 0 ;i < nums.length -1 ; i ++){
            if(nums[i] == 0){
                for(int j = i; j < nums.length - 1; j++){
                    int t = nums[j+1];
                    nums[j+1] = nums[j];
                    nums[j] = t;
                }
                
            }
        }
        
        
        
        
    }
}