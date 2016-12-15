###28 Implement strStr()

Implement strStr().


Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length()==0)
            return 0;
        
        
        
        for(int i = 0; i < haystack.length(); i ++){
            if(i+needle.length() > haystack.length())
                return -1;
            for(int j = 0; j < needle.length(); j++){
                if(haystack.charAt(i+j) == needle.charAt(j)){
                }else
                    break;
                if(j == needle.length()- 1)
                    return i;
            }
        
    }
    return -1;
}
}