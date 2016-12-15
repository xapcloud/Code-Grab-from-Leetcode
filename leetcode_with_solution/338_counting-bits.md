###338 Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.


Example:Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
###Solution
```java
public class Solution {
    public int[] countBits(int num) {
        int [] ret = new int [num+1];
        
        for(int i = 0; i <= num; i ++){
            ret[i] = cot(i);
        }
        
        return ret;
    }
    
    private int cot(int n){
        int ret = 0;
        while(n!=0){
            ret++;
            n = n&(n-1);
        }
        
        return ret;
    }
    
}