###47 Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.


For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        int f = fac(nums.length);
        int former = nums[0];
        int formerNum = 1;
        for(int i = 1; i < nums.length; i ++){
            if(nums[i] == former){
                formerNum++;
                if(i == nums.length-1)
               	f /= fac(formerNum);
            }
            else{
                former = nums[i];
                f/=fac(formerNum);
                formerNum = 1;
            }
        }
        
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        ret.add(conver(nums));
        for(int i = 1; i < f; i ++){
            nextPermutation(nums);
            ret.add(conver(nums));
        }
        return ret;
    }
    
    private List<Integer> conver(int[]nums){
        List<Integer> ret = new ArrayList<Integer>();
        for(int v:nums){
            ret.add(v);
        }
        
        return ret;
    }
    
    
    private int fac(int n){
        int ret = 1;
        for(int i = 1; i <=n; i ++)
            ret*=i;
            
        return ret;
    }
    
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