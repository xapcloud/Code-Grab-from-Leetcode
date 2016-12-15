###29 Divide Two Integers

Divide two integers without using multiplication, division and mod operator.


If it is overflow, return MAX_INT.

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int divide(int dividend, int divisor) {
        
        if (dividend == Integer.MIN_VALUE && divisor == 1)
			return Integer.MIN_VALUE;
	    if(dividend == divisor)
	        return 1;

		boolean b1 = dividend > 0;
		boolean b2 = divisor > 0;

		int v1 = Math.abs(dividend);
		int v2 = Math.abs(divisor);
		int result = 0;

		if (v1 == Integer.MIN_VALUE) {
			result++;
			v1 = v1 - divisor;
			v1 = Math.abs(v1);

		}
		if ((v1 < v2 || v1 == 0 || v2 == Integer.MIN_VALUE) && result == 0)
			return 0;
        //å¥½æ¶å¿çä»£ç ï¼ææåºè¯¥èçæ¯è¿ä¸ªå¾ªç¯é¨åï¼å©ç¨é¤æ° x 10å¹æ¬¡ï¼æ¥å¤§å¹åº¦ç¼©åè¿ç®æçï¼ä½æ¯æè½è¯¯æ¶é´çåèæ¯ç¹æ®æåµå¤ç
        //Core code
		while (v1 >= v2) {
			int t = findPower(v1, v2);

			result = result + (int) Math.pow(10, t);
			v1 = v1 - v2 * (int) Math.pow(10, t);
		}
		if (result == Integer.MIN_VALUE)
			return Integer.MAX_VALUE;

		return b1 == b2 ? result : (0 - result);
    }
    //Core function
    private int findPower(int d1, int d2){
        
        for(int i = 10; i >= 0; i --){
            if(d1 > d2*Math.pow(10,i))
                return i;
        }
        
        return 0;

    }
}