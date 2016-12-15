###11 Container With Most Water
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
   	public int maxArea(int[] height) {
		int h = 0, t = height.length-1, max = 0;
		while( h < t){
			int he = height[h]> height[t]?height[t]:height[h];
			max = max > (t-h)*he? max: (t-h)*he;
			
			if(height[h]< height[t]){
				int k = h;
				while(k < t && height[k]<=height[h])
					k++;
				h = k;				
			}else{
				int k = t;
				while(k > h && height[k]<=height[t])
					k--;
				t = k;		
			}
		}
		return max;

	}
}