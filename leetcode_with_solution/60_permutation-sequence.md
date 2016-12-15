###60 Permutation Sequence
The set [1,2,3,…,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"


Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive.The set [1,2,3,…,n] contains a total of n! unique permutations.By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.Note: Given n will be between 1 and 9 inclusive.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String getPermutation(int n, int k) {
        //æè·¯å¾ç®åï¼å°±æ¯å©ç¨æ°æ°çæ¹æ³ï¼æ ¹æ®kè½æå¤å°ä¸ªï¼n-1ï¼ï¼æ¥å³å®æ¯ä¸ä½åç¬¬å å°çæ°å­
        //æ¯å¦ï¼3ï¼3ï¼å ä¸º3æ1ä¸ªå¤ç2ï¼ï¼æä»¥ç¬¬ä¸æ°å­åºè¯¥åç¬¬äºå°çæ°å­ï¼å³2.
        //å©ç¨Booleanç©éµè®°å½å·²ç»éè¿çæ°å­
        //æ¯è¾ç¹æ®çæ¯k/(n-1)!= 0 çæåµï¼è¿ä¸ªæ¶åä½æ°åºä¸ºï¼n-1ï¼!ï¼åæ¶åºæ¹ç¬¬ï¼åï¼å°çæ°å­ã
        //æ¯å¦ï¼3ï¼2ï¼ï¼ 2/2!=1...0ä½æ¯ï¼ç¬¬ä¸ä½å¾æ¯1.
        boolean [] hasOccur = new boolean[n];
        String result = "";
        
        for(int i = 0; i < n; i ++){
            int shang = k/fac(n-1-i);
            int remainder = k % fac(n-1-i);
            
            int temp = 0;
            if(remainder == 0){
                k = fac(n-1-i);
                temp = findKthMin(hasOccur,shang-1);
            }else{
                k = remainder;
                temp = findKthMin(hasOccur,shang);
            }
            result+=temp;
            hasOccur[temp-1] = true;
            
        }
        
        return result;
    }
    private int findKthMin(boolean[] hasOccur, int k){
        for(int i = 0; i < hasOccur.length; i ++){
            if(!hasOccur[i]){
                k--;
                
                if(k< 0)
                    return i+1;
            }
        }
        
        return 0;
    }
    
    
    private int fac(int n){
        int ret = 1;
        for(int i = 1; i <=n; i ++)
            ret*=i;
            
        return ret;
    }
    
    
}