###221 Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.

Credits:Special thanks to @Freezen for adding this problem and creating all test cases.
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Credits:Special thanks to @Freezen for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int maximalSquare(char[][] matrix) {
        int row = matrix.length;
        if(row == 0)
            return 0;
        int column = matrix[0].length;
        
        int [][] dp = new int [row][column];
        
        int ret = 0; 

        
        for(int i = 0; i < row ; i ++){
            dp[i][0] = matrix[i][0] - '0';
            if(matrix[i][0] == '1')
                ret = 1;
        }
        
         for(int i = 0; i < column ; i ++){
            dp[0][i] = matrix[0][i] - '0';
             if(matrix[0][i] == '1')
                ret = 1;
        }
        
        for(int i = 1; i < row ; i ++){
            for(int j = 1; j < column ; j ++){
                if(matrix[i][j] == '1'){
                    dp[i][j] = Math.min(Math.min(dp[i-1][j],dp[i-1][j-1]),dp[i][j-1])+1;
                    ret = Math.max(ret,dp[i][j]);
                }
                else
                    dp[i][j] = 0;
            }
        }
        return ret*ret;
    }
}