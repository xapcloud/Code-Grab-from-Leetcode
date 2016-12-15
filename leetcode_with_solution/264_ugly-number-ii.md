###264 Ugly Number II

Write a program to find the n-th ugly number.


Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.


Note that 1 is typically treated as an ugly number.


The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
   public int nthUglyNumber(int n) {
        if (n <= 0) { return 0; }
        List<Integer> seq = new ArrayList<>();
        seq.add(1);
        int head2 = 2, head3 = 3, head5 = 5;
        int ptrGen2 = 1, ptrGen3 = 1, ptrGen5 = 1;
        while (seq.size() < n) {
            int min = Math.min(head2, Math.min(head3, head5));
            seq.add(min);
            if (min == head2) { head2 = seq.get(ptrGen2++) * 2; }
            if (min == head3) { head3 = seq.get(ptrGen3++) * 3; }
            if (min == head5) { head5 = seq.get(ptrGen5++) * 5; }
        }
        return seq.get(seq.size()-1);
    }

    
    
    
    
    
}