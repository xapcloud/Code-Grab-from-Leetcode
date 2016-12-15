###67 Add Binary

Given two binary strings, return their sum (also a binary string).


For example,
a = "11"
b = "1"
Return "100".

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String addBinary(String a, String b) {
        

        
        String temp = "";
        
        while(a.length() > 0 && b.length() > 0){
            temp = (a.charAt(a.length()-1) - '0' + b.charAt(b.length()-1) -'0')+temp;
            a = a.substring(0,a.length() - 1);
            b = b.substring(0,b.length() - 1);
        }
        
        
        temp = a + b + temp;
        
        System.out.println(temp);
        
        String result = "";
        boolean flag = false;
        for(int i = temp.length()-1; i>=0; i --){
            int t = temp.charAt(i)-'0' + (flag?1:0);
            if(t > 1){
                flag = true;
                result = t%2 + result;
            }else{
                flag = false;
                result = t+result;
            }
        }
        
        return flag?('1'+result):result;
        
    }
}