###313 Super Ugly Number

    Write a program to find the nth super ugly number.


    Super ugly numbers are positive numbers whose all prime factors are in the given prime list
    primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
 is the sequence of the first 12 super ugly numbers given primes
    = [2, 7, 13, 19] of size 4.


Note:
    (1) 1 is a super ugly number for any given primes.
    (2) The given numbers in primes are in ascending order.
    (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.

Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.
    Write a program to find the nth super ugly number.

    Super ugly numbers are positive numbers whose all prime factors are in the given prime list
    primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
 is the sequence of the first 12 super ugly numbers given primes
    = [2, 7, 13, 19] of size 4.

Note:
    (1) 1 is a super ugly number for any given primes.
    (2) The given numbers in primes are in ascending order.
    (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        
        int[] dp = new int[n], index = new int[primes.length];
        dp[0] = 1;
        int min;
        int minIndex = 0;
        for(int i = 1; i < n ; i ++){
            min = Integer.MAX_VALUE;
            for(int j = 0; j < primes.length; j ++){
                int temp = dp[index[j]]*primes[j];
                if(temp < min){
                    min = temp;
                    minIndex = j;
                }
            }
            
            index[minIndex]++;
            
            if(min != dp[i - 1]){
                dp[i] = min;
            }else{
                i--;
            }

        }
        
        return dp[n-1];
    }
}