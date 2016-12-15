###378 Kth Smallest Element in a Sorted Matrix
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.


Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        
        if(matrix.length == 0)  
            return 0;
            
        int r = matrix.length; 
        int c = matrix[0].length; 
        
        int [] array = new int[r*c];
        
        for(int i = 0; i < r; i ++){
            for(int j = 0; j < c;j ++){
                array[i*c+j] = matrix[i][j];
            }
        }
        
        Arrays.sort(array);
        
        return array[k-1];
    }
}