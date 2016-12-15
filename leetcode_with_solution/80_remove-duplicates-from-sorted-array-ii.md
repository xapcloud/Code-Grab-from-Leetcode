###80 Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],


Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length < 3)
            return nums.length;
          
        int result = 2; 
        int removeNum = 0;
        for(int i = 2; i < nums.length; i ++){
            if(nums[i] != nums[i-1-removeNum]||nums[i] != nums[i-2-removeNum]){
                nums[result] = nums[i];
                result++;
            }else{
                removeNum++;
            }
            
        }
        
        return result;
    }
    
    
}