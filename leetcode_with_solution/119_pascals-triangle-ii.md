###119 Pascal's Triangle II
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].


Note:
Could you optimize your algorithm to use only O(k) extra space?
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> result = new ArrayList<Integer>();
        if(rowIndex == 0){
            result.add(1);
            return result;
        }else{
            
            result.add(1);
            
            List<Integer> l = getRow(rowIndex-1);
            
            for(int i = 1; i < l.size(); i++){
                result.add(l.get(i-1)+l.get(i));
            }
            
            result.add(1);
            
            
            
        }
        
        return result;
        
    }
}