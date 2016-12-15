###43 Multiply Strings
Given two numbers represented as strings, return multiplication of the numbers as a string.
Note:

The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
Given two numbers represented as strings, return multiplication of the numbers as a string.Note:

The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String multiply(String num1, String num2) {
        if(num1.equals("0") || num2.equals("0"))
            return "0";
            
        num1 = new StringBuffer(num1).reverse().toString();
        num2 = new StringBuffer(num2).reverse().toString();
        //ä¹ç§¯æé¿æ¯ len1 + len2ï¼
        int[] d = new int[num1.length() + num2.length()];
        for (int i = 0; i < num1.length(); i++) {
            int a = num1.charAt(i) - '0';
            for (int j = 0; j < num2.length(); j++) {
                int b = num2.charAt(j) - '0';
                d[i + j] += a * b;
            }
        }
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < d.length; i++) {
            int digit = d[i] % 10;
            int carry = d[i] / 10;
            sb.insert(0, digit);
            if (i < d.length - 1)
                d[i + 1] += carry;
            }
            
        //å é¤å¤ä½ç 0
        while (sb.length() > 0 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }
        return sb.length() == 0 ? "0" : sb.toString();

    }
}