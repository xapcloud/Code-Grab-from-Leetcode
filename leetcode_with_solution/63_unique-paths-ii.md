###63 Unique Paths II
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.
Note: m and n will be at most 100.

Subscribe to see which companies asked this question


Show Tags

Array
Dynamic Programming



Show Similar Problems

 (M) Unique Paths


Follow up for "Unique Paths":Now consider if some obstacles are added to the grids. How many unique paths would there be?An obstacle and empty space is marked as 1 and 0 respectively in the grid.For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.
Note: m and n will be at most 100.There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.Note: m and n will be at most 100.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int row = obstacleGrid.length;
        int column = obstacleGrid[0].length;
        
   
        
        
        int[][]p = new int[row][column];
        
        for(int i = row -1; i >= 0; i--){
            for(int j = column -1; j >= 0 ; j--){
                if(obstacleGrid[i][j] == 1)
                    p[i][j] = 0;
                else if(i == row-1 && j == column -1)
                    p[i][j] = 1;
                else if(i == row - 1)
                    p[i][j] = p[i][j+1];
                else if(j == column -1)
                    p[i][j] = p[i+1][j];
                else
                    p[i][j]= p[i][j+1]+p[i+1][j];

                
            }
        }
        
        return p[0][0];
    }
}