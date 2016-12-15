###220 Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    // public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        
    //     // for(int i = 0 ; i < nums.length; i ++){
    //     //     for(int j = i + 1; j < nums.length && j < (i + k + 1); j ++){
    //     //         if(Math.abs(nums[i]-nums[j]) <= t)
    //     //             return true;
    //     //     }
            
    //     // }
    //     // return false;
        
    //     HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();

    //     int n = nums.length;
    //     for(int i = 0; i < n ; i ++){
    //         if (i > k) 
    //             hm.remove(getKey(nums[i-k-1],t));
    //         int key = getKey(nums[i],t);
    //         if(hm.containsKey(key))
    //             return true;
    //         if (hm.containsKey(key - 1) && Math.abs(nums[i] - hm.get(key - 1)) < t) 
    //             return true;
    //         if (hm.containsKey(key + 1) && Math.abs(nums[i] - hm.get(key + 1)) < t) 
    //             return true;
    //         hm.put(key, nums[i]);

    //     }
    //     return false;
    // }
    // // [-2n...-n-1] [-n...-1] [0... n-1] [n...2n+1]
    // int getKey(int a, int t){
    //     return a < 0 ? ((a-t+1)/t) : a/t;
    // }
    
    
    private int getID(int i, int t) {
    return i < 0 ? (i + 1) / t - 1 : i / t;
}

public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
    if (t < 0) return false;
    int n = nums.length;
    Map<Integer, Integer> d = new HashMap<>();
    t++;
    for (int i = 0; i < n; ++i) {
        if (i > k) d.remove(getID(nums[i - k - 1], t));
        int m = getID(nums[i], t);
        if (d.containsKey(m)) return true;
        if (d.containsKey(m - 1) && Math.abs(nums[i] - d.get(m - 1)) < t) return true;
        if (d.containsKey(m + 1) && Math.abs(nums[i] - d.get(m + 1)) < t) return true;
        d.put(m, nums[i]);
    }
    return false;
}
}