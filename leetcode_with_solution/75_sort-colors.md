###75 Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.


Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.


Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with an one-pass algorithm using only constant space?


Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
click to show follow up.Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.Could you come up with an one-pass algorithm using only constant space?
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public void sortColors(int[] nums) {
        
        //Arrays.sort(nums);
        
        int red = 0;
        int white = 0; 
        int blue = 0;
        
        for(int i = 0; i < nums.length; i ++){
            switch (nums[i]){
                case 0: red++;
                    break;
                case 1: white++;
                    break;
                case 2: blue++;
 
            }
        }
        
        for(int i = 0; i < nums.length; i ++){
            if(i < red)
                nums[i] = 0;
            else if (i < red + white)
                nums[i] = 1;
            else
                nums[i] = 2;
            
            
        }
        
    }
}