###55 Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.


Each element in the array represents your maximum jump length at that position. 


Determine if you are able to reach the last index.


For example:
A = [2,3,1,1,4], return true.


A = [3,2,1,0,4], return false.

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position. 

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean canJump(int[] nums) {
        
        //æè·¯ï¼å¦ææ²¡æ0ï¼è¯å®å¯ä»¥èµ°å°æåï¼å¦ææ0ï¼ä¸æ¯æåä¸ä¸ªï¼ï¼åéè¦å¯¹æ¯ä¸ª0è¿è¡å¤æ­æ¯å¦å¯ä»¥è·³è¿
        
        HashSet<Integer> hs = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i ++){
            if(nums[i] == 0)
                hs.add(i);
        }
        
        if(hs.isEmpty())
            return true;
        
        Iterator<Integer> ite=hs.iterator();

        while(ite.hasNext()){
            int index = ite.next();
            if(index == nums.length-1)
                continue;
            
            int i = index - 1;
            boolean re = false;
            while(i>=0){
                if(nums[i] > (index-i)){
                    re = true;
                    break;
                }else{
                    i--;
                }
            }
            if(!re)
                return false;
        }
        return true;
    }
}