###42 Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. 


For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.



The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Subscribe to see which companies asked this question


Show Tags

Array
Stack
Two Pointers



Show Similar Problems

 (M) Container With Most Water
 (M) Product of Array Except Self
 (H) Trapping Rain Water II



Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. 

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int trap(int[] height) {
        
        if(height.length < 3)
            return 0;
        
        int maxIndex = -1;
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < height.length; i ++){
            if(height[i]>max){
                maxIndex = i;
                max = height[i];
            }
        }
        
        int result = 0;
        
        int cur = height[0];
        for(int i = 0; i < maxIndex ; i ++){
            if(height[i] < cur){
                result = result + (cur - height[i]);
            }else{
                cur = height[i];
            }
        }
        
        cur = height[height.length -1 ];
        for(int i = height.length -1 ; i > maxIndex; i --){
             if(height[i] < cur){
                result = result + (cur - height[i]);
            }else{
                cur = height[i];
            }
        }
        
        return result;
        
    }
}