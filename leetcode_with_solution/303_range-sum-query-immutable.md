###303 Range Sum Query - Immutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3


Note:

You may assume that the array does not change.
There are many calls to sumRange function.

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3


Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:

You may assume that the array does not change.
There are many calls to sumRange function.

Subscribe to see which companies asked this question
###Solution
```java
public class NumArray {
    int[] sum;
    int[] nums;

    public NumArray(int[] nums) {
        this.nums = nums;
        sum = new int[nums.length + 1];
        sum[0] = 0;
        for(int i = 1; i < sum.length; i ++){
            sum[i] = sum[i-1]+nums[i-1];
        }
    }

    public int sumRange(int i, int j) {
        if(i < 0 || j >= nums.length){
            return 0;
        }
        return sum[j+1]-sum[i];
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);