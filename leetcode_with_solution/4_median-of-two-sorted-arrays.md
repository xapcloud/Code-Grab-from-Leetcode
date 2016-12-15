###4 Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0


Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

There are two sorted arrays nums1 and nums2 of size m and n respectively.Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0


nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int [] sum = new int[nums1.length+ nums2.length];
		System.arraycopy(nums1, 0, sum, 0, nums1.length);
		System.arraycopy(nums2, 0, sum, nums1.length, nums2.length);
		
		Arrays.sort(sum);
		
		if(sum.length%2 == 0)
			return (sum[sum.length/2]+sum[sum.length/2-1])/2d;
		else
			return sum[(sum.length-1)/2];

        
    }
}