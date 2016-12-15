###228 Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Given a sorted integer array without duplicates, return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<String> summaryRanges(int[] nums) {

        
        // List<String> result = new ArrayList<String>();
        
        // int max = Integer.MIN_VALUE;
        // int min = Integer.MAX_VALUE;
        
        // for(int i = 0; i < nums.length;  i++){
        //     max = max > nums[i] ? max : nums[i];
        //     min = min < nums[i] ? min : nums[i];
        // }
        
        // boolean [] line = new boolean [max+2];
        
        // for(int i = 0 ; i < nums.length; i ++){
        //     line[nums[i]] = true;
        // }
        
        // boolean isIn = false;
        // String s = "";
        // for(int i = 0; i <= max+1; i ++){
        //     if(line[i]&&!isIn){
        //         isIn= true;
        //         s = ""+i;
        //         System.out.println("kkk");
        //     }else if(!line[i] && isIn){
        //         System.out.println(s);
        //         if(s.charAt(0) - (i-1) == ('0' - 0))
        //             result.add(s.charAt(0)+"");
        //         else
        //             result.add(s+"->"+(i-1));
        //         isIn = false;
        //     }
            
        // }
        
        // return result;
        
        
        
        List<String> result = new ArrayList<String>();
        
        if(nums.length == 0)
            return result;
        
        String s = ""+nums[0];
        
        for(int i = 1; i < nums.length; i ++){
            if(nums[i] - nums[i-1] > 1 || (nums[i] > 0 && nums[i-1]<0)){
                System.out.println(nums[i]+" "+nums[i-1]);
                if(!s.equals(nums[i-1]+""))
                    s = s + "->" + nums[i-1];
                result.add(s);
                s = "" + nums[i];
            }
        }
        
        if(s.equals(nums[nums.length-1]+""))
            result.add(s);
        else
            result.add(s+"->"+nums[nums.length-1]);
        
        return result;
        
    }
}