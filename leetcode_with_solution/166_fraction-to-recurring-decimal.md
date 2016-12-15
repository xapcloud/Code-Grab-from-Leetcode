###166 Fraction to Recurring Decimal
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".



No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

Credits:Special thanks to @Shangrila for adding this problem and creating all test cases.Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.If the fractional part is repeating, enclose the repeating part in parentheses.
For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

Credits:Special thanks to @Shangrila for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public  String fractionToDecimal(int numerator, int denominator) {
	        boolean f = false;
	        String ret = "";
	        if((numerator > 0 && denominator <0) ||(numerator < 0 && denominator >0))
	        	f = true;
	        long nu = (long)numerator;
	        long de = (long)denominator;
	        
	        long x = nu/de;
	        long rd = nu%de;
	        if(rd == 0){
	        
	                return x+"";
	        }
	          else{
	            ret = x+".";
	            ret = ret.replace("-","");
	        }  
	            
	        ArrayList<Long> d = new ArrayList<Long>();

	        while(rd != 0){
	            d.add(rd);
	            x = rd*10/de;
		        rd = (rd*10)%de;
		        
		        String temp = x+"";
		        temp = temp.replaceAll("-", "");
		        ret =ret+temp;	    

		        if(d.contains(rd)){
		           break;
		        }
	            
	        }
	        if(rd != 0){
	            int index = d.indexOf(rd);
	            ret = ret.substring(0,ret.indexOf('.')+1+index)+"("+ret.substring(ret.indexOf('.')+1+index)+")";
	        }
	        if(f)
	            ret = "-"+ret;
	        return ret;
	    }
}