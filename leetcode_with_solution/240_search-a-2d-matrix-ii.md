###240 Search a 2D Matrix II
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:


Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.



For example,

Consider the following matrix:


[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


For example,
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.Given target = 20, return false.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
     
        int r = matrix.length; 
        if(r < 1)
            return false;
        int c = matrix[0].length;
        
        return helpFunc(0,0,r-1,c-1,matrix,target);
    }
    
    //divide the matrix into 4 parts and then recursive call
    //start point and end point
    private Boolean helpFunc(int sx, int sy, int ex, int ey, int[][]m, int t){
        if(t < m[sx][sy] || t > m[ex][ey])
            return false;
        
        if(sx < ex || sy < ey){
            //middle point
            int mx = (ex-sx)/2+sx;
            int my = (ey-sy)/2+sy;
            
            boolean ret = false;
            if(my < ey)
                ret = ret || helpFunc(sx,my+1,mx,ey,m,t);
            if(mx < ex)
                ret = ret || helpFunc(mx+1,sy,ex,my,m,t);
            
            if(m[mx][my] > t)
                return helpFunc(sx,sy,mx,my,m,t)||ret;
            else if(m[mx][my]<t){
                if(mx< ex && my < ey)
                    return helpFunc(mx+1,my+1,ex,ey,m,t)||ret;
                else
                    return ret;
            }else
                return true;
        }else
            return m[sx][sy] == t;
    }
    
    
    // public boolean searchMatrix(int[][] matrix, int target) {
    //     int r = matrix.length; 
    //     if(r < 1)
    //         return false;
    //     int c = matrix[0].length;
        
    //     int i = 0, j = c-1;
    //     while(i < r && j >= 0){
    //         if(matrix[i][j] == target)
    //             return true;
    //         else if(matrix[i][j]  < target)
    //             i++;
    //         else
    //             j--;
    //     }
        
    //     return false;
    // }
}