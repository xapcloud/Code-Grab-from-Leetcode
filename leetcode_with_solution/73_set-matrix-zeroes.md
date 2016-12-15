###73 Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
click to show follow up.
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public void setZeroes(int[][] matrix) {
        HashSet<Integer> rows = new HashSet<Integer>(); 
        HashSet<Integer> columns = new HashSet<Integer>(); 
        
        for(int i = 0;i < matrix.length; i ++){
            for(int j =0; j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    rows.add(i);
                    columns.add(j);
                }
            }
        }
        //System.out.println(rows.size()+" "+columns.size());
        
        for(int x: rows){
            for(int j = 0;j < matrix[0].length; j ++){
                matrix[x][j] = 0;
            }
        }
        
        for(int y:columns){
            for(int i = 0; i < matrix.length; i ++){
                matrix[i][y] = 0;
            }
        }

        
    }
}