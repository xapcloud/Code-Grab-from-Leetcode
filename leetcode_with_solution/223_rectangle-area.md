###223 Rectangle Area
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.




Assume that the total area is never beyond the maximum possible value of int.

Credits:Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.Find the total area covered by two rectilinear rectangles in a 2D plane.Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.Assume that the total area is never beyond the maximum possible value of int.Credits:Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        
        int areaOfTwo = (C-A)*(D-B)+(G-E)*(H-F);
        
        int x1 = Math.max(A,E);
        int x2 = Math.max(B,F);
        int x3 = Math.min(H,D);
        int x4 = Math.min(G,C);
        
        if(x4<=x1||x3<=x2)
            return areaOfTwo;
        else
            return areaOfTwo-(x4-x1)*(x3-x2);
    }
}