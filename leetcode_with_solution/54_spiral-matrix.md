###54 Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.


For example,
Given the following matrix:


[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]


You should return [1,2,3,6,9,8,7,4,5].
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
     //ç¹æ®æè·¯ï¼å³æç§ ï¼ä¸  å³  ä¸  å·¦  ä¸ï¼å¾ªç¯çä¼åçº§(å°èµ°è¿çè·¯å¾æ è®°)ï¼å³å¯æç§é¢ç®è¦æ±éåã
     //éè¦æ³¨æcontinue
     //éè¦æ³¨æï¼åæ¶æ»¡è¶³å¯ä»¥ å·¦èµ° å ä¸èµ°çæåµä¸ï¼ä¼åå·¦èµ°ã
     
        List<Integer> result = new ArrayList<Integer>();
        if(matrix.length == 0 || matrix[0].length == 0)
            return result;
        
        int rows = matrix.length;
        int columns = matrix[0].length;
        
        int totalNum = rows*columns;
        int[][] mark = new int[rows][columns];
     
     
        int x = 0;
        int y = 0;
        for(int i = 0; i < totalNum; i ++){
            result.add(matrix[x][y]);
            mark[x][y] = 1;
            
            
            //åæ¶æ»¡è¶³ï¼å·¦ ä¸ï¼ éè¦åå·¦èµ°
             if(x > 0 && mark[x-1][y] == 0 && y > 0 && mark[x][y-1] == 0){
                y = y -1;
                continue;
            }
            //åä¸èµ°
            if(x > 0 && mark[x-1][y] == 0){
                x = x-1;
                continue;
            }
            //åå³èµ°
            if(y < columns-1 && mark[x][y+1] == 0){
                y = y+1;
                continue;
            }
            //åä¸èµ° 
            if(x < rows-1 && mark[x+1][y] == 0){
                x = x+1;
                continue;
            }
            //åå·¦èµ°
            if(y > 0 && mark[x][y-1] == 0){
                y = y-1;
                continue;
            }
        }
        
        return result;
    }
}