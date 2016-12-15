###349 Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:

Each element in the result must be unique.
The result can be in any order.


Given two arrays, write a function to compute their intersection.
Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
Note:

Each element in the result must be unique.
The result can be in any order.

Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        if(nums1.length == 0 || nums2.length == 0)
            return new int[0];
        HashSet<Integer> hs1 = new HashSet<Integer>();
        HashSet<Integer> hs2 = new HashSet<Integer>();

        for(int i = 0; i < nums1.length; i ++){
            hs1.add(nums1[i]);
        }
        
        for(int i = 0; i < nums2.length; i ++){
            hs2.add(nums2[i]);
        }
        
        ArrayList<Integer> a = new ArrayList<Integer>();
        
        for(int val : hs1){
            if(hs2.contains(val))
                a.add(val);
        }
        
        int[] array= new int [a.size()];
        
        for(int i = 0; i < a.size(); i ++){
            array[i] = a.get(i);
        }
        
        return array;
        
    }
}