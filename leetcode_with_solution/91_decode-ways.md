###91 Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:


'A' -> 1
'B' -> 2
...
'Z' -> 26


Given an encoded message containing digits, determine the total number of ways to decode it.


For example,
Given encoded message "12",
it could be decoded as "AB" (1 2) or "L" (12).


The number of ways decoding "12" is 2.

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12",
it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int numDecodings(String s) {
        //if(s.length() == 0)
        //    return 0;
        //if(s.length() == 1)
        //    return 1;
        
        
        int t1 = 0;
        int t2 = 1;
        int result = 0;
        
        for(int i = 0 ; i < s.length() ; i ++){
            result = 0;
            if(i > 0){
                int t = (s.charAt(i-1)-'0')*10+(s.charAt(i)-'0');
                if(t < 27 && t > 9 )
                    result += t1;
            }
            if(s.charAt(i) != '0')
                result += t2;
            
            t1 = t2;
            t2 = result;
        }
        
        return result;
        
    }
}