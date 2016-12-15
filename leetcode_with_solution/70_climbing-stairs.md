###70 Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
You are climbing a stair case. It takes n steps to reach to the top.Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    
    
     public int climbStairs(int n) {
        if(n == 0)
            return 0;
        if(n == 1)
            return 1;
        if(n == 2)
            return 2;
            
        int t1 = 1;
        int t2 = 2;

        for(int i = 2; i < n; i ++){
            int temp = t2;
            t2 = t1+t2;
            t1 = temp;

        }
        return t2;
    }
    
    
}