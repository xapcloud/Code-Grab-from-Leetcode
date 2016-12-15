###290 Word Pattern
Given a pattern and a string str, find if str follows the same pattern.
 Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:

pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.



Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:Special thanks to @minglotus6 for adding this problem and creating all test cases.Given a pattern and a string str, find if str follows the same pattern. Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Examples:

pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.


Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
Credits:Special thanks to @minglotus6 for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean wordPattern(String pattern, String str) {
        HashMap<Character, String> h = new HashMap<Character, String>();
        
        for(int i = 0; i < pattern.length(); i++){
            char c = pattern.charAt(i);
            String t1;
            if(str.indexOf(" ") == -1){
                t1 = str;
                if(i != pattern.length()-1)
                    return false;
            }else
                t1 = str.substring(0,str.indexOf(" "));
            
            if(h.get(c) == null)
                h.put(c,t1);
            else{
                String t2 = h.get(c);
                System.out.println(t2+" "+ h.get(c));
                if(!t2.equals(t1))
                    return false;
            }
            
            System.out.println(i+" "+c+" "+ t1);
            
            if(str.indexOf(" ") == -1)
                str = "";
            else
                str = str.substring(str.indexOf(" ")+1);
            
        }
        
        if(!str.equals("")){
            return false;   
        }
        for(int i = 0; i < pattern.length(); i++){
            for(int j = i+1; j < pattern.length(); j++){
                System.out.println(pattern.charAt(i));
                System.out.println(pattern.charAt(j));
                System.out.println(h.get(pattern.charAt(i)));
                System.out.println(h.get(pattern.charAt(j)));
                
                if(pattern.charAt(i) != pattern.charAt(j) && h.get(pattern.charAt(i)).equals(h.get(pattern.charAt(j))))
                    return false;
            }
        }
        
        
        return true;
        
    }
}