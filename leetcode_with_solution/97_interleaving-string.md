###97 Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.


For example,
Given:
s1 = "aabcc",
s2 = "dbbca",


When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
    
        
        int l1 = s1.length(), l2 = s2.length(), l3 = s3.length();
        
        if(l3 != l1 + l2)
            return false;
        
        boolean [][]dp = new boolean[l1+1][l2+1];
        
        dp[0][0] = true;
        
        for(int i = 1; i <= l1; i ++){
            if(s1.substring(0,i).equals(s3.substring(0,i)))
                dp[i][0] = true;
            else
                break;
        }
        
        for(int j = 1; j <= l2; j++){
            if(s2.substring(0,j).equals(s3.substring(0,j)))
                dp[0][j] = true;
            else
                break;
        }
        
        
        
        //i, j can only start by 1 so we should first solve i = 0 row and j = 0 colum
        for(int i = 1; i <= l1; i++ ){
            for(int j = 1; j <=l2 ; j++){
                
                char c1 = s1.charAt(i-1);
                char c2 = s2.charAt(j-1);
                char c3 = s3.charAt(i+j-1);
                
                if((dp[i-1][j]&&(c3==c1))||(dp[i][j-1]&&(c3==c2)))
                    dp[i][j] = true;
                
                
                
            }
            
        }
        
        return dp[l1][l2];
        
    }
}