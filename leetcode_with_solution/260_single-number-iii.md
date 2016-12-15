###260 Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.


For example:


Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].


Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?


Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int[] singleNumber(int[] nums) {
      //å©ç¨singleNumber 1çæè·¯ï¼åªè½å¾å° c=a^b
      //ç¶åå©ç¨ c&-cè·å¾ä¸º1çæä½ä½ï¼ä¾æ¬¡å°æ°ç»åä¸ºä¸¤ç±»
      //å¯ä»¥ç¡®ä¿å°a båå¨ä¸¤ç±»ä¸­
      
      int diff = 0;
      for(int num: nums){
          diff^=num;
      }
      
      diff = Integer.highestOneBit(diff);
      
      int []result = new int[2];
      Arrays.fill(result,0);

      for(int num: nums){
          if((num&diff)==0)
            result[0]^=num;
          else
            result[1]^=num;
      }
        return result;
    }
}