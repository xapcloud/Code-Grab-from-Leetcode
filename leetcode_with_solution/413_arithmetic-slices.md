###413 Arithmetic Slices
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
For example, these are arithmetic sequence:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic. 1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
A slice (P, Q) of array A is called arithmetic if the sequence:
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
The function should return the number of arithmetic slices in the array A. 

Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.


Subscribe to see which companies asked this question


Show Tags

Dynamic Programming
Math



Show Similar Problems

 (H) Arithmetic Slices II - Subsequence


A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.For example, these are arithmetic sequence:1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9The following sequence is not arithmetic.1, 1, 2, 5, 7A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.A slice (P, Q) of array A is called arithmetic if the sequence:
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.The function should return the number of arithmetic slices in the array A. Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        
        int l = A.length;
        if(l < 3)
            return 0;
        
        int result = 0;
        int diff = A[1]-A[0];   
        int n = 2;
        for(int i = 2; i < l; i ++){
            int temp = A[i]-A[i-1];
            if(temp == diff){
                n++;
            }else{
                result+=calcNum(n);
                n = 2;
                diff = temp;
            }
            
        }
        
        return result+calcNum(n);
        
    }
    
    private int calcNum(int n){
        if(n < 3)
            return 0;
        int sum = 0; 
        
        for(int i = 3; i <= n; i ++){
            sum = sum+n-i+1;
        }
        
        return sum;
    }
}