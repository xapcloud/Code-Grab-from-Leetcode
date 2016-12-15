###84 Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.



Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].



The largest rectangle is shown in the shaded area, which has area = 10 unit.


For example,
Given heights = [2,1,5,6,2,3],
return 10.

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.
The largest rectangle is shown in the shaded area, which has area = 10 unit.
For example,
Given heights = [2,1,5,6,2,3],
return 10.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
   public int largestRectangleArea(int[] height) {
       
       
        boolean sorted = true;
        int l = height.length;
        for (int i = 0; i < l; i++) {
            if (i > 0 && height[i] < height[i - 1]) 
                sorted = false;
        }
        if (sorted) {
            int max = 0;
            for (int i = 0; i < l; i++) {
                max = Math.max(max, height[i] * (l - i));
            }
            return max;
        }
       
       
       
        Stack<Integer> stack = new Stack<Integer>();
        int[] h = new int[height.length + 1];
        h = Arrays.copyOf(height, height.length + 1);
        
        int i = 0; 
        int maxArea = 0;
        
        while(i < h.length){
            if(stack.isEmpty() || h[i] >= h[stack.peek()])
                stack.push(i++);
            else{
                int temp = stack.pop();
                maxArea = Math.max(maxArea, h[temp]*(stack.isEmpty()?i:(i-stack.peek()-1)));
            }
        }
        
        return maxArea;
   }
}