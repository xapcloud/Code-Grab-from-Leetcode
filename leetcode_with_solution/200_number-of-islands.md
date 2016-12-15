###200 Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
11110110101100000000
Answer: 1
Example 2:
11000110000010000011
Answer: 3
Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.Example 1:11110110101100000000Answer: 1Example 2:11000110000010000011Answer: 3Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int numIslands(char[][] grid) {
        int r = grid.length; 
        
        if(r == 0)
            return 0;
        
        int c = grid[0].length;
        

        int num=0;
        for(int i = 0; i < r; i ++){
            for(int j = 0; j < c; j ++){
                
                if(grid[i][j] == '1'){
                    num++;
                    helper(grid,i,j,r,c);
                }
                
            }
        }
        
        return num;
    }
    
    private void helper(char[][] grid, int i, int j, int r, int c){
        grid[i][j] = '0';
        if(i > 0 && grid[i-1][j]=='1')
            helper(grid,i-1,j,r,c);
        if(j > 0 && grid[i][j-1]=='1')
            helper(grid,i,j-1,r,c);
        if(i < r-1 && grid[i+1][j]=='1')
            helper(grid,i+1,j,r,c);
        if(j < c-1 && grid[i][j+1]=='1')
            helper(grid,i,j+1,r,c);
    }
    
}