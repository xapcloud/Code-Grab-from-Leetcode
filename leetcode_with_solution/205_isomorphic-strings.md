###205 Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.
Note:
You may assume both s and t have the same length.Given two strings s and t, determine if they are isomorphic.Two strings are isomorphic if the characters in s can be replaced to get t.All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.For example,
Given "egg", "add", return true.Given "foo", "bar", return false.Given "paper", "title", return true.Note:
You may assume both s and t have the same length.Subscribe to see which companies asked this question
###Solution
```java

import java.util.Hashtable;
public class Solution {
    public boolean isIsomorphic(String s, String t) {
       return check(s,t)&&check(t,s);
    }
    
    private static boolean check(String s, String t){
         Hashtable<Character,Character> ht = new Hashtable<Character,Character>();
        
        int l = s.length();
        
        for(int i = 0; i < l; i ++ ){
            char sc = s.charAt(i);
            char tc = t.charAt(i);
            
            if(ht.containsKey(sc) && ht.get(sc) != tc)
            	return false;
            else
            	ht.put(sc, tc);
        }
		return true;
    }
}