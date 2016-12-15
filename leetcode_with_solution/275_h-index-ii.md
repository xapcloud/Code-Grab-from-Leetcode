###275 H-Index II

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?


Expected runtime complexity is in O(log n) and the input is sorted.

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int hIndex(int[] citations) {
        
        if(citations.length == 0 || citations[citations.length-1] == 0)
            return 0;
        
        int ret = 0;
        int len = citations.length;
        for(int i = len - 1; i >= 0; i --){
           if(citations[i] >= len - i)
                ret++;
        }
        return ret;
    }
}