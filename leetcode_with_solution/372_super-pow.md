###372 Super Pow

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8


Example2:

a = 2
b = [1,0]

Result: 1024


Credits:Special thanks to @Stomach_ache for adding this problem and creating all test cases.
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
Example1:

a = 2
b = [3]

Result: 8


a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024


a = 2
b = [1,0]

Result: 1024
Credits:Special thanks to @Stomach_ache for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int superPow(int a, int[] b) {
        a = a % 1337;
        return sp(a,b,b.length-1);
    }
    
    
    private int sp(int a, int[]b, int index){
        if (index == 0){
            int m = 1;
            for(int i = 0; i < b[index]; i ++){
                m = m * a % 1337;
            }
			return m;
        }
	    int x = 1;
		for(int i = 0; i < b[index]; i ++)
			x = x*a%1337;

	    int y = sp(a,b,index-1)%1337;
	    int y1 = 1;
		for(int i = 0; i < 10; i ++)
			y1 = (y1*y)%1337;
			
		return x*y1%1337;
        
    }
}