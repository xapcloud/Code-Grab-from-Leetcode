###62 Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Subscribe to see which companies asked this question


Show Tags

Array
Dynamic Programming



Show Similar Problems

 (M) Unique Paths II
 (M) Minimum Path Sum
 (H) Dungeon Game


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).How many possible unique paths are there?

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.Above is a 3 x 7 grid. How many possible unique paths are there?
Note: m and n will be at most 100.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
//     public int uniquePaths(int m, int n) {
//         if(m == 1|| n == 1)
// 			return 1;
// 		return uniquePaths(m-1,n) + uniquePaths(m,n-1);
        
//     }
    
    public int uniquePaths(int m,int n){
        int [][] p = new int[m][n];
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(i == 0 || j == 0)
                    p[i][j] = 1;
                else
                    p[i][j] = p[i-1][j] + p[i][j-1];
            }
        }
        
        return p[m-1][n-1];
        
    }
    
}