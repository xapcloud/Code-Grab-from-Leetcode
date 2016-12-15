###137 Single Number II

Given an array of integers, every element appears three times except for one. Find that single one.


Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Subscribe to see which companies asked this question
###Solution
```java
import java.util.*;
public class Solution {
    public int singleNumber(int[] nums) {
        
        Hashtable<Integer,Integer> hs = new Hashtable<Integer,Integer>();
        
        for(int i = 0; i < nums.length; i ++){
            if(hs.containsKey(nums[i])){
                hs.put(nums[i],(hs.get(nums[i])+1));
            }else
                hs.put(nums[i],0);
        }
        
        int ret = 0;
        Iterator<Integer> it = hs.keySet().iterator();
        
        while(it.hasNext()){
            int temp = it.next();
            if(hs.get(temp) == 0)
                return temp;
            
            
        }
        
        
        
        return ret;
    }
}