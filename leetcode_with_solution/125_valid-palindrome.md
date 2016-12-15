###125 Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.


For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.


Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isPalindrome(String s) {
        // int len = s.length();
            
        // String t = "";
        
        // for(int i = 0; i < len ; i ++){
        //     char c = s.charAt(i);
        //     if((c>='0'&&c<='9') || (c>='a'&&c<='z') ||(c>='A'&&c<='Z') )
        //         t+=c;
        // }
        
        // len = t.length();
    
        // if(len<=1)
        //     return true;
        
        // for(int i = 0; i < len/2; i++){
            
        //     if(t.charAt(i) != t.charAt(len-1-i))
        //         return false;
            
        // }
        // return true;
        
        
        
        if(s.length() == 0)
            return true;
        int a = 0; int b = s.length()-1;
        
        while(a<b){
            char c1 = s.charAt(a);
            char c2 = s.charAt(b);
            if(!((c1>='0'&&c1<='9') || (c1>='a'&&c1<='z') ||(c1>='A'&&c1<='Z') )){
                a = a+1;
                continue;
            }
            if(!((c2>='0'&&c2<='9') || (c2>='a'&&c2<='z') ||(c2>='A'&&c2<='Z') )){
                b = b-1;
                continue;
            }
            
            String s1 = (c1+"").toUpperCase();
            String s2 = (c2+"").toUpperCase();
            
            
            if(!s1.equals(s2))
                return false;
            else{
                a++;
                b--;
            }
        }
 
        return true;
    }
}