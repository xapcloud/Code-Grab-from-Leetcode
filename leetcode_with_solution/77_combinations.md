###77 Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.


For example,
If n = 4 and k = 2, a solution is:


[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(n < k)
            return result;
        myCombine(result, new ArrayList<Integer>(), n, k, 1);
        
        return result;
    }
    
    
    private void myCombine(List<List<Integer>> l, List<Integer> c, int n, int k, int start){
        if(c.size() == k){
            l.add(c);
            return;
        }
        for(int i = start; i <= n; i++){
            List<Integer> cc = new ArrayList<Integer>(c);
            cc.add(i);
            myCombine(l,cc,n,k,i+1);
        }
        
    }
}