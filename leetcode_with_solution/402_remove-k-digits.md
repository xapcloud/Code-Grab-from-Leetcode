###402 Remove K Digits
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Note:

The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.


###Solution
```java
public class Solution {
    public String removeKdigits(String num, int k) {
        
        
        if(k == num.length())
            return 0+"";
        
        //denote which digit to determine
        int cur = 0;
    
        while(k > 0 && cur+k < num.length()){
            
            int min = (int)(num.charAt(cur)-'0');
            int minIndex = cur;
            for(int i = cur+1; i <=cur+k ; i ++){
               // System.out.println(min+"\t"+(int)(num.charAt(cur)-'0'));
                if((int)(num.charAt(i)-'0')<min){
                    min = (int)(num.charAt(i)-'0');
                    minIndex = i;
                    //System.out.println("minIndex="+minIndex);
                }
            }
            
            if(minIndex == cur)
                cur++;
            else{
                //è¿ä¸ªå°æ¹éè¦æ³¨æï¼ä¸è½ç´æ¥num= num.substring(minIndex),
                //å ä¸ºä¹åå·²ç»ç¡®å®çæ°å­è¦ä¿ç
                k = k - (minIndex-cur);
                String pre = num.substring(0,cur);
                String post = num.substring(minIndex);
                num = pre+post;
                cur++;
            }
        }
        
        if(k>0)
            num = num.substring(0,num.length()-k);
        //å»æåé¢ç0   
        num = num.replaceFirst("^0*", "");  
        //ä¿è¯ä¸ä¼è¾åºç©º
        return num.equals("")?"0":num;
        
    }
}