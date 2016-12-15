###263 Ugly Number

Write a program to check whether a given number is an ugly number.


Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.


Note that 1 is typically treated as an ugly number.

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isUgly(int num) {
        while(num>=5&&num%5==0){
            num/=5;
        }
        while(num>=3&&num%3==0){
            num/=3;
        }
         while(num>=2&&num%2==0){
            num/=2;
        }
        
        return num == 1;
        
    }
}