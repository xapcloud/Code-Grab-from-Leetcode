###387 First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.



Note: You may assume the string contain only lowercase letters.

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.


s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
Subscribe to see which companies asked this question
###Solution
```java
import java.util.*;
public class Solution {
    public int firstUniqChar(String s) {
        int[][] num = new int[26][2];
        HashSet<Character> hs = new HashSet<Character>();
        for(int i = 0; i < s.length(); i ++){
            char c = s.charAt(i);
            num[c-'a'][0]++;
            if(!hs.contains(c))
                num[c-'a'][1]= i;
        }
        
        int ret = Integer.MAX_VALUE;
        for(int i = 0; i < 26; i ++){
            if(num[i][0]==1)
                ret = Math.min(num[i][1],ret);
        }
        if(ret == Integer.MAX_VALUE)
            return -1;
        else
            return ret;
    }
}