###27 Remove Element
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Try two pointers.
Did you use the property of "the order of elements can be changed"?
What happens when the elements to remove are rare?
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        
        for(int i = 0; i < nums.length; i ++){
            
          if(nums[i] != val){
              nums[count] = nums[i];
              count++;
          }  
        }
        
        return count;
        
    }
}