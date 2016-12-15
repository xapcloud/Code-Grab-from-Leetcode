###415 Add Strings
Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.
Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String addStrings(String num1, String num2) {
        
        int l1 = num1.length();
        int l2 = num2.length();
        
        int l = Math.max(l1,l2);
        
        String result = "";
        int ca = 0,n1=0,n2=0;
        for(int i = 0; i < l; i ++ ){
            if(i < l1)
                n1 = Integer.parseInt(num1.charAt(l1-i-1)+"");
            if(i < l2)
                n2 = Integer.parseInt(num2.charAt(l2-i-1)+"");
            
            int temp = n1+n2+ca;
            ca = temp/10;
            result = temp%10+result;
            n1 = 0;
            n2 = 0;
        }
        
        if(ca!=0)
            result = ca+result;
        
        return result;
        
    }
}