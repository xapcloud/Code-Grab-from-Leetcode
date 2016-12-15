###383 Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines ; otherwise, it will return false. 


Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.


canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true


Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines ; otherwise, it will return false. 

Each letter in the magazine string can only be used once in your ransom note.
Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] rn = new int[26];
        int[] ma = new int[26];
        
        for(int i = 0; i < ransomNote.length(); i ++){
            rn[ransomNote.charAt(i)-'a']++;
        }
        
        for(int i = 0; i < magazine.length(); i ++){
            ma[magazine.charAt(i)-'a']++;
        }
        
        for(int i = 0; i < 26; i ++){
            if(rn[i]>ma[i])
                return false;
        }
        
        return true;
    }
}