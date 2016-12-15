###48 Rotate Image
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?You are given an n x n 2D matrix representing an image.Rotate the image by 90 degrees (clockwise).Follow up:
Could you do this in-place?Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int row = (n%2==0?(n/2):(n/2+1));
        
        
        for(int i = 0; i < n/2 ; i++){
            for(int j = 0; j < row; j++){
                int t = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][i];
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j]= matrix[j][n-1-i];
                matrix[j][n-1-i]=t;
            }
        }
    }
    
    
}