###377 Combination Sum IV
 Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7 Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7
###Solution
```java
public class Solution {
    public int combinationSum4(int[] nums, int target) {
        int [] dp = new int[target+1];
        dp[0] = 1; //dp[i-i] = dp[0] = 1 make sure contains every number in array self.
        
        for(int i  = 1 ; i <= target; i ++){
            for(int n:nums){
                dp[i] += (i >= n) ? dp[i-n] : 0;
            }
        }
        
        return dp[target];
    }
}