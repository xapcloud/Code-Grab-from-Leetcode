###90 Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.


For example,
If nums = [1,2,2], a solution is:


[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Given a collection of integers that might contain duplicates, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
          
        
        Arrays.sort(nums);
        
        int len = nums.length;
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        
        //å subset I ç¸æ¯ï¼å°±å¤äºä¸å¥ç¨hashsetä¿è¯ä¸éå¤
        HashSet<List<Integer>> hs = new HashSet<List<Integer>>();
        
        int setNum = (int)Math.pow(2,len);
        
        int [] bit = new int[len];
        
        for(int i = 0; i < len; i ++){
            bit[i] = 0;
        }
        
        result.add(new ArrayList<Integer>());
        
        
        for(int i = 1; i < setNum; i ++){
            List<Integer> l = new ArrayList<Integer>();
            bit = new int[len];
            int count = 0;
            int quo,rem;
            int b = i;
            
            while(b>=1){
                quo = b/2;
                rem = b%2;
                bit[count] = rem;
                count++;
                b = quo;
            }

            for(int j = 0; j < len; j++){
                if(bit[j]==1)
                    l.add(nums[j]);
            }
            if(hs.add(l))
                result.add(l);
            
        }
        
        return result;
    }
}