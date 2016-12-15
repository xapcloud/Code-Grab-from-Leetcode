###9 Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
click to show spoilers.
Some hints:
Could negative integers be palindromes? (ie, -1)
If you are thinking of converting the integer to string, note the restriction of using extra space.
You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
There is a more generic way of solving this problem.
Determine whether an integer is a palindrome. Do this without extra space.click to show spoilers.Could negative integers be palindromes? (ie, -1)If you are thinking of converting the integer to string, note the restriction of using extra space.You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?There is a more generic way of solving this problem.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isPalindrome(int x) {
       if (x < 0)
			return false;
		if (x < 10)
			return true;
		int count = 1;
		int y = x;
		while (y >= 10) {
			count++;
			y = y / 10;
		}
		
		System.out.println(count);

		for (int i = 0; i < count / 2; i++) {
			if (x % 10 == x / (int)(Math.pow(10, count - 1 - i * 2))) {
				x = (x % (int)(Math.pow(10, count - 1 - i * 2)))/10;

				continue;
			} else
				return false;
		}
		return true;
    }
}