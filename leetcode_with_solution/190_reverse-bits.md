###190 Reverse Bits
Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
Credits:Special thanks to @ts for adding this problem and creating all test cases.Reverse bits of a given 32 bits unsigned integer.For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
Follow up:
If this function is called many times, how would you optimize it?
Related problem: Reverse IntegerCredits:Special thanks to @ts for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        for(int i = 0; i < 16; i ++){
            int a = (n >> i)  & 1;
            int b = (n >> (31 - i) ) & 1;
            
            if((a^b) != 0)
               n ^= (1 << i) | (1 << (31-i));
        }
        
        return n;
    }
}