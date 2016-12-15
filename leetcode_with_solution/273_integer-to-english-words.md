###273 Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
For example,

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public String numberToWords(int num) {
        String result = "";
        
        if(num == 0)
            return "Zero";
        
        int billion = num/(int)Math.pow(10,9);
        num = num%(int)Math.pow(10,9);
        if(billion>0)
            result+=numberToWords(billion)+" Billion ";
        
        int million = num/(int)Math.pow(10,6);
        num = num%(int)Math.pow(10,6);
        if(million>0)
            result+=numberToWords(million)+" Million ";
        
        int thousand = num/(int)Math.pow(10,3);
        num = num%(int)Math.pow(10,3);
        if(thousand>0)
            result+=numberToWords(thousand)+" Thousand ";
        
        int hundred = num/100;
        num = num%100;
        if(hundred>0)
            result+=numberToWords(hundred)+" Hundred ";
            
        if(num >= 20){
            int t1 = num/10;
            int t2 = num%10;
            
           switch (t1) {
            case 2:
                result+= "Twenty ";
                break;
            case 3:
                result+= "Thirty ";
                break;
            case 4:
                result+= "Forty ";
                break;
            case 5:
                result+= "Fifty ";
                break;
            case 6:
                result+= "Sixty ";
                break;
            case 7:
                result+= "Seventy ";
                break;
            case 8:
                result+= "Eighty ";
                break;
            case 9:
                result+= "Ninety ";
                break;
            default:
                result+= "";
            }
            switch (t2) {
            case 0:
                result+= "";
                break;
            case 1:
                result+= "One";
                break;
            case 2:
                result+= "Two";
                break;
            case 3:
                result+= "Three";
                break;
            case 4:
                result+= "Four";
                break;
            case 5:
                result+= "Five";
                break;
            case 6:
                result+= "Six";
                break;
            case 7:
                result+= "Seven";
                break;
            case 8:
                result+= "Eight";
                break;
            case 9:
                result+= "Nine";
                break;
            default:
                result+= "";
            }
        }else{
            switch(num){
             case 0:
                result+= "";
                break;
            case 1:
                result+= "One";
                break;
            case 2:
                result+= "Two";
                break;
            case 3:
                result+= "Three";
                break;
            case 4:
                result+= "Four";
                break;
            case 5:
                result+= "Five";
                break;
            case 6:
                result+= "Six";
                break;
            case 7:
                result+= "Seven";
                break;
            case 8:
                result+= "Eight";
                break;
            case 9:
                result+= "Nine";
                break;
            case 10:
                result+= "Ten";
                break;
            case 11:
                result+= "Eleven";
                break;
            case 12:
                result+= "Twelve";
                break;
            case 13:
                result+= "Thirteen";
                break;
            case 14:
                result+= "Fourteen";
                break;
            case 15:
                result+= "Fifteen";
                break;
            case 16:
                result+= "Sixteen";
                break;
            case 17:
                result+= "Seventeen";
                break;
            case 18:
                result+= "Eighteen";
                break;
            case 19:
                result+= "Nineteen";
                break;
            default:
                result+= "";  
                
                
            }
        }
        return result.trim();
    }
}