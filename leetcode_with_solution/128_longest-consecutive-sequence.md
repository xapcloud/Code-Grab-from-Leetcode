###128 Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.


For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.


Your algorithm should run in O(n) complexity.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int longestConsecutive(int[] nums) {
        
      	Arrays.sort(nums);


		int maxCons = Integer.MIN_VALUE;
		int tempL = 1;
		for (int i = 0; i < nums.length; i++) {
			if (i == 0) {
				tempL = 1;
			} else if (nums[i] - nums[i - 1] == 1) {
				tempL++;
			}

			else if (nums[i] == nums[i - 1]) {
			} else {
				maxCons = Math.max(tempL, maxCons);
				tempL = 1;
			}
		}
		maxCons = Math.max(tempL, maxCons);

		return maxCons;

        
    }
}