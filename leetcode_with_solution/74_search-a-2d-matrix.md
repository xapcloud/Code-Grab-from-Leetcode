###74 Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:


Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.



For example,

Consider the following matrix:


[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return true.Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


For example,
Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(target<matrix[0][0]&&target>matrix[matrix.length -1 ][matrix[0].length - 1])
            return false;
        
        
        int i;
        boolean f = false;
        for(i = 0; i < matrix.length - 1; i++){
            if(matrix[i][0]<=target && matrix[i+1][0] > target){
                f = true;
                break;
            }
        }
        
        if(!f){
            return isFound(matrix[matrix.length-1],target);
            
        }else{
            return isFound(matrix[i],target);
        }
    }
    
    private boolean isFound(int [] n, int target){
        int s = 0, e = n.length-1;
        
        while(s <= e){
            int t= (s+e)/2;
            if(n[t] == target)
                return true;
            else if(n[t]< target)
                s = t + 1;
            else
                e = t - 1;
        }
        
        return false;
    }
}