###350 Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.


Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


Given two arrays, write a function to compute their intersection.
Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Subscribe to see which companies asked this question
###Solution
```java
import java.util.*;

public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        

        if(nums1.length == 0 || nums2.length == 0)
            return new int[0];

        Hashtable<Integer,Integer> n1 = new Hashtable<Integer,Integer>();
        Hashtable<Integer,Integer> n2 = new Hashtable<Integer,Integer>();
        
        genTable(nums1,n1);
        genTable(nums2,n2);
        
        ArrayList<Integer> ret;
        
        if(n1.size() < n2.size())
            ret = inters(n1,n2);
        else
            ret = inters(n2,n1);
        
        int[] array= new int [ret.size()];
        
        for(int i = 0; i < ret.size(); i ++){
            array[i] = ret.get(i);
        }
        
        return array;
    }
    
    private ArrayList<Integer> inters(Hashtable<Integer,Integer> n1, Hashtable<Integer,Integer> n2){
        
        ArrayList<Integer> ret = new ArrayList<Integer>();
        
        Iterator<Integer> it = n1.keySet().iterator();
        
        while(it.hasNext()){
            int val = it.next();
            
            if(n2.containsKey(val)){
                int t1 = n1.get(val);
                int t2 = n2.get(val);
                int min = Math.min(t1,t2);
                
                for(int i = 0; i < min; i ++){
                    ret.add(val);
                }
            }
            
        }
        
        return ret;
    }
    
    private void genTable(int[] nums,Hashtable<Integer,Integer> n){
        int l = nums.length;
        
        for(int i = 0; i < l; i ++){
            if(n.containsKey(nums[i]))
                n.put(nums[i],(n.get(nums[i])+1));
            else
                n.put(nums[i],1);
        }
        
    }
}