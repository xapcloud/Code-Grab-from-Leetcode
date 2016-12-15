###318 Maximum Product of Word Lengths

    Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
    You may assume that each word will contain only lower case letters.
    If no such two words exist, return 0.


Example 1:


    Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    Return 16
    The two words can be "abcw", "xtfn".


Example 2:


    Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    Return 4
    The two words can be "ab", "cd".


Example 3:


    Given ["a", "aa", "aaa", "aaaa"]
    Return 0
    No such pair of words.    

Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.
    Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
    You may assume that each word will contain only lower case letters.
    If no such two words exist, return 0.

Example 1:

    Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    Return 16
    The two words can be "abcw", "xtfn".

Example 2:

    Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    Return 4
    The two words can be "ab", "cd".

Example 3:

    Given ["a", "aa", "aaa", "aaaa"]
    Return 0
    No such pair of words.    
Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int maxProduct(String[] words) {
        
        int l = words.length;
        
        if(l < 2)
            return 0;
        
        int [] w = new int [l];
        
        for(int i = 0; i < l; i++){
            for(int j = 0; j < words[i].length(); j++){
                w[i] |= 1<<(words[i].charAt(j)-'a');
            }
        }
        
        int ret = 0;
        
        for(int i = 0; i < l-1 ; i ++){
            for(int j = i+1; j < l ;j ++){
                if((w[i]&w[j])==0)
                    ret =  Math.max(ret,words[i].length()*words[j].length());
            }
            
        }
        
        return ret;
    }
}