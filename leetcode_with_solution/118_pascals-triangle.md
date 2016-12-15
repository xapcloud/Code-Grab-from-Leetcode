###118 Pascal's Triangle
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(numRows == 0)
            return result;
        List<Integer> l = new ArrayList<Integer>();
        l.add(1);
        result.add(l);
        if(numRows == 1)
            return result;
        
        for(int i = 2; i <= numRows ; i ++){
            List<Integer> ll = new ArrayList<Integer>();
            ll.add(1);
            for(int j = 1; j < l.size(); j ++){
                ll.add(l.get(j-1)+l.get(j));
            }
            ll.add(1);
            
            result.add(ll);
            l = ll;
        }
        
        
        return result;
    }
}