###139 Word Break

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].


Return true because "leetcode" can be segmented as "leet code".

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    // public boolean wordBreak(String s, Set<String> wordDict) {
    //     if(s.length() == 0)
    //         return true;
    //     boolean ret = false;
    //     for(int i = 0; i < s.length(); i ++){
    //         String pre = s.substring(0,i+1);
    //         String aft = s.substring(i+1);
    //         if(wordDict.contains(pre) && wordBreak(aft,wordDict))
    //             return true;
    //     }
    //     return ret;
    // }
    //Time Limit Exceeded
     public boolean wordBreak(String s, Set<String> wordDict) {
       
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        

        for(int i=1; i <= s.length(); i++){
            for(int j=0; j < i; j++){
                if(dp[j] && wordDict.contains(s.substring(j, i))){
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[s.length()];
    }
}