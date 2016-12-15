###123 Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).Say you have an array for which the ith element is the price of a given stock on day i.Design an algorithm to find the maximum profit. You may complete at most two transactions.Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        if(n < 2)
            return 0;
        
        int[] preProfit = new int[n];
        int[] postProfit = new int[n];
        
        int curMin = prices[0];
        for(int i = 1; i< n; i++){
            curMin = Math.min(curMin, prices[i]);
            preProfit[i] = Math.max(preProfit[i-1], prices[i] - curMin);
        }
        
        int curMax = prices[n-1];
        for(int i = n-2; i >= 0 ; i --){
            curMax = Math.max(curMax, prices[i]);
            postProfit[i] = Math.max(postProfit[i+1],curMax-prices[i]);
        }
        
        int ret = 0; 
        for(int i = 0; i < n ; i++){
            ret = Math.max(ret, preProfit[i]+postProfit[i]);
        }
        
        return ret;
    }
}