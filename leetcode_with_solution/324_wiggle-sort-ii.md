###324 Wiggle Sort II

    Given an unsorted array nums, reorder it such that
    nums[0] < nums[1] > nums[2] < nums[3]....


Example:
    (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
    (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].


Note:
    You may assume all input has valid answer.


Follow Up:
    Can you do it in O(n) time and/or in-place with O(1) extra space?

Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.
    Given an unsorted array nums, reorder it such that
    nums[0] < nums[1] > nums[2] < nums[3]....

Example:
    (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
    (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
    You may assume all input has valid answer.

Follow Up:
    Can you do it in O(n) time and/or in-place with O(1) extra space?
Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public void wiggleSort(int[] nums) {
        Arrays.sort(nums);
        int l = nums.length;

        int[] ret = new int[l];
        
        for(int i = 0; i < (l+1)/2; i ++){
            ret[2*i] = nums[(l-1)/2-i];
            if(2*i+1<l)
                ret[2*i+1] = nums[l-i-1];
        }
        
        //æè·¯å°±æ¯åæåºï¼ç¶åå°æå¥½åºçæ°ç»åæå·¦å³ä¸¤å[a1,...,an,b1,...,bn]ï¼å·¦åä¸ä¸ªaxå³åä¸ä¸ªbxéæ°æ¼æ
        //æåç»æï¼éè¦æ³¨æçæ¯ä»ä¸­é´å¼å§åï¼å³æåçç»ææ¯[an,bn,an-1,bn-1....]
        //å¦æå¼å¤´å¼å§åï¼è¯¸å¦[4,5,5,6]çå½¢å¼ç­æ¡ä¼é
      
        for(int i = 0; i < l; i ++){
            nums[i] = ret[i];
        }
    }
}