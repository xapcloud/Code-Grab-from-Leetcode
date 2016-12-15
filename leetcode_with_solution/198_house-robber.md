###198 House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
Credits:Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.Credits:Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int rob(int[] nums) {
        
        int l = nums.length;
        if( l == 0)
            return 0;
        
        int [] money = new int [l];
        
        for(int i = 0; i < l; i ++){
            int ff = 0, f = 0;
            if(i > 0)
                f = money[i-1];
            if(i > 1)
                ff = money[i-2];
            
            money[i] = Math.max(f,ff+nums[i]);
        }
        return money[l-1];
    }
}