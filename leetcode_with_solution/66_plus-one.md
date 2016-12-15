###66 Plus One
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.Given a non-negative number represented as an array of digits, plus one to the number.The digits are stored such that the most significant digit is at the head of the list.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int[] plusOne(int[] digits) {
        
        boolean f = false;
        
        int i;
        for(i = digits.length - 1; i >= 0; i--){
            
            int temp = digits[i] + (i==(digits.length-1)?1:0) + (f?1:0);
            if(temp >= 10){
                f = true;
                digits[i] = temp%10;
            }else{
                f = false;
                digits[i] = temp;
            }
            if(!f)
                return digits;
        }
        
        
        if(++i == 0 && f){
            int[]result = new int[digits.length+1];
            result[0] = 1;
            for(int j = 1; j < result.length; j++){
                result[j] = digits[j-1];
            }
            System.out.println("~~~~");
            return result;
        }
        
        return digits;
    }
}