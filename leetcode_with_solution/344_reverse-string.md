###344 Reverse String
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
Write a function that takes a string as input and returns the string reversed.
Example:
Given s = "hello", return "olleh".
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String reverseString(String s) {
        return new StringBuffer(s).reverse().toString();
    }
}