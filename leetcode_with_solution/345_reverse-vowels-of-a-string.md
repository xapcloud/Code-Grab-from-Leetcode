###345 Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".


Example 2:
Given s = "leetcode", return "leotcede".


Note:
The vowels does not include the letter "y".
Write a function that takes a string as input and reverse only the vowels of a string.
Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String reverseVowels(String s) {
        
        List<Integer> indexs = new ArrayList<Integer>();
        char[] charArray = s.toCharArray();
        
        for(int i = 0;i < charArray.length; i ++){
            char c = charArray[i];
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U')
                indexs.add(i);
        }
        
        int length = indexs.size();
        
        for(int i = 0; i< length/2; i++){
            char c = charArray[indexs.get(i)];
            charArray[indexs.get(i)] = charArray[indexs.get(length-i-1)];
            charArray[indexs.get(length-i-1)] = c;
        }
        return new String(charArray);
    }
}