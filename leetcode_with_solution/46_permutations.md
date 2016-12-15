###46 Permutations

Given a collection of distinct numbers, return all possible permutations.


For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        
        List<List<Integer>> l = new ArrayList<List<Integer>>();
        
        List<Integer> ll = new ArrayList<Integer>();
        
        
        int product = 1;
        for(int i = 1; i <= nums.length; i++){
            product*=i;
            ll.add(nums[i-1]);
        }
        l.add(ll);
        
        if(nums.length < 2)
            return l;
        
        
        
        for(int i = 1; i < product; i++ ){
            int [] n = nextPermutation(nums); 
            ll = new ArrayList<Integer>();
            for(int j = 0; j <n.length; j ++ ){
                ll.add(n[j]);
            }
            l.add(ll);
        }
        
        return l;
        
        
    }
    
    public  int[] nextPermutation(int[] nums) {
    if(nums.length < 2)
        return nums;
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
    
    return nums;
    }
}