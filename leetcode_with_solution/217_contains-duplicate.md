###217 Contains Duplicate

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        // if(nums.length == 0)
        //     return false;
        
        // HashSet<Integer> hs = new HashSet<Integer>();
        
        // for(int i = 0; i < nums.length; i ++){
        //     if(hs.contains(nums[i]))
        //         return false;
        //     hs.add(nums[i]);
            
            
        // }
        
        // return true;
        Arrays.sort(nums);
        for(int i=0; i<nums.length-1; i++){
            if(nums[i]==nums[i+1]) return true;
        }
        return false;

    }
}