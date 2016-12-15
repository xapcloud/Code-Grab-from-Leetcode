###120 Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]



The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).


Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]


[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        
        if(triangle.isEmpty())
            return 0;
        int size = triangle.size();
        int [] sum = new int[size];
        
        List<Integer> temp = null;
        
        for(int i = 0; i < size; i ++){ 
            temp = triangle.get(i);
            int former = 0;
            int record = 0;
            for(int j = 0; j < temp.size(); j ++){
                record = sum[j];
                if(j == 0)
                    sum[j] = temp.get(j)+sum[0];
                else if(j == temp.size()-1)
                    sum[j] = temp.get(j)+former;
                else
                    sum[j] = Math.min(sum[j],former)+temp.get(j);
                former = record;
            }
        }
        int result = Integer.MAX_VALUE;
        for(int i = 0; i < size; i ++){
            result = Math.min(result,sum[i]);
        }
        
        return result;
    }
}