###59 Spiral Matrix II
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example,
Given n = 3,

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int[][] generateMatrix(int n) {
        int [][] result = new int[n][n];
        
        int start = 0;
        int end = n - 1;
        int num = 1;
        
        while(start < end ){
            for(int i = start; i < end; i++){
                result[start][i] = num;
                num++;
            }
            for(int i = start; i < end; i++){
                result[i][end] = num;
                num++;
            }
            for(int i = end; i > start; i--){
                result[end][i] = num;
                num++;
            }
            for(int i = end; i > start; i--){
                result[i][start] = num;
                num++;
            }
            start++;
            end--;
        }
        if(start == end)
            result[start][end] = num;
        return result;
    }
}