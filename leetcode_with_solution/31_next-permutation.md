###31 Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.


If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).


The replacement must be in-place, do not allocate extra memory.


Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
   public  void nextPermutation(int[] nums) {
    if(nums.length < 2)
        return;
    int len = nums.length;
    
    boolean f = true;
    for(int i = len - 1; i >= 1; i--){
        if(nums[i-1] >= nums[i])
            continue;
        else{
        	f= false;
            int j;
            for(j = len -1; j >= i; j --){
               if(nums[j] > nums[i-1])
                    break;
            }
            
            //System.out.println(j);
            int t = nums[i-1];
            nums[i-1] = nums[j];
            nums[j] = t;
            
           // System.out.println(nums[0]+" "+nums[1]+" "+nums[2]+" "+i );
            
            
            int[] temp = Arrays.copyOfRange(nums, i, len);
            Arrays.sort(temp);
           // System.out.println(temp.length+" "+temp[0]);
            
            for(j  = i; j < len; j++){
                nums[j] = temp[j-i];
            }
            break;
        }
    }
    
    if(f)
        Arrays.sort(nums);
    
}
}