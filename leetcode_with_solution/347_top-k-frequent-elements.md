###347 Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.
For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Given a non-empty array of integers, return the k most frequent elements.For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].
Note: 

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        
        for(int x : nums){
            map.put(x,map.getOrDefault(x,0)+1);
        }
        
        
        int len = nums.length; 
        List<Integer>[] bucket = new List[len+1];
        
        
        for(int key: map.keySet()){
            int val = map.get(key);
            if(bucket[val]==null)
                bucket[val] = new ArrayList<Integer>();
                
            bucket[val].add(key);
        }
        
        List<Integer> result = new ArrayList<Integer>();
        for(int i = bucket.length-1; i >= 0 && result.size() < k; i --){
            if(bucket[i]!=null)
                result.addAll(bucket[i]);
        }
        
        return result;
    }
}