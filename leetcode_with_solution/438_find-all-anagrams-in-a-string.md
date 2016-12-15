###438 Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.
Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.The order of output does not matter.Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        
        List<Integer> result = new ArrayList<Integer>();
        
        char [] charArray1 = p.toCharArray();
        int[] count1 = new int[26];
        for(char c: charArray1){
            count1[c-'a']++;
        }
        for(int i = 0; i <= s.length()-p.length(); i ++){
            String temp = s.substring(i,i+p.length());
            
            
            char [] charArray2 = temp.toCharArray();
            // Arrays.sort(charArray1);
            // Arrays.sort(charArray2);
            
            // if(new String(charArray1).equals(new String(charArray2)))
            //     result.add(i);
            //è¶æ¶
            
            int []count2 = new int[26];
            for(char c: charArray2){
                count2[c-'a']++;
            }
            
            boolean flag = true;
            for(int j = 0; j < 26; j ++){
                if(count1[j]!=count2[j]){
                    flag = false;
                    break;
                }
            }
            
            if(flag)
                result.add(i);
            
        }
        
        return result;
    }
}