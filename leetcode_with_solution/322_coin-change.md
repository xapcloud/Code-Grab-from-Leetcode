###322 Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.


Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)


Example 2:
coins = [2], amount = 3
return -1.


Note:
You may assume that you have an infinite number of each kind of coin.

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int coinChange(int[] coins, int amount) {
      
      int min = Integer.MAX_VALUE;
      int cur = 1;
      int [] dp = new int [amount+1];
      dp[0] = 0;
      while(cur <= amount){
          min =  Integer.MAX_VALUE;
          for(int i = 0; i < coins.length; i ++){
              int diff = cur - coins[i];
              if(diff >= 0 && dp[diff]>=0)
                  min = Math.min(min, dp[diff] + 1);
         }
         dp[cur++] = (min == Integer.MAX_VALUE ? -1 : min);

      }
      
      return dp[amount];
    }
}