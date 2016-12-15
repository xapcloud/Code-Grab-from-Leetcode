###88 Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        int [] mt = new int[m];
        
        mt = Arrays.copyOf(nums1,m);
        
        int i = 0, j = 0, k= 0;
        while(i < m || j < n){
            if(i<m && j < n){
                if(mt[i]<nums2[j]){
                    nums1[k] = mt[i];
                    i++;
                    k++;
                }else{
                    nums1[k] = nums2[j];
                    j++;
                    k++;
                }
            }else if(i<m){
                nums1[k] = mt[i];
                i++;
                k++;
            }else{
                nums1[k] = nums2[j];
                j++;
                k++;
            }
        }
    }
}