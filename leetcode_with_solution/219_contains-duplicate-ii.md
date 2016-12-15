###219 Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
Subscribe to see which companies asked this question
###Solution
```java
import java.util.*;

public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        
        Hashtable<Integer,Integer> ht = new Hashtable<Integer,Integer>();
        
        for(int i = 0; i < nums.length; i++){
            int temp = nums[i];
            if(ht.containsKey(temp) && (i - ht.get(temp)) <= k)
                return true;
            else
                ht.put(temp,i);
        }
        return false;
    }
}