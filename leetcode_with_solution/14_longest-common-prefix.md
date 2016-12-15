###14 Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
Write a function to find the longest common prefix string amongst an array of strings.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        if(strs.length ==0)
            return "";
        
        int len = strs.length;
        int [] lens = new int[len];
        for(int i = 0; i < len; i ++)
            lens[i] = strs[i].length();
        Arrays.sort(lens);
        
        int r = 0;
        boolean flag = true;
        
        for(int i = 0; i < lens[0]; i ++){
            String temp = strs[0].substring(0,i+1);
            
            for(int j = 0; j < len; j ++ ){
                if(!strs[j].substring(0,i+1).equals(temp))
                    flag = false;
            }
            
            if(flag)
                r++;
            else
                break;
            
        }
        return r>0?strs[0].substring(0,r):"";
        
        
    }
}