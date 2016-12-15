###216 Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.



 Example 1:
Input:  k = 3,  n = 7
Output: 

[[1,2,4]]


 Example 2:
Input:  k = 3,  n = 9
Output: 

[[1,2,6], [1,3,5], [2,3,4]]


Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers. Example 1:Input:  k = 3,  n = 7Output: 
[[1,2,4]]

[[1,2,4]]
 Example 2:Input:  k = 3,  n = 9Output: 
[[1,2,6], [1,3,5], [2,3,4]]

[[1,2,6], [1,3,5], [2,3,4]]
Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        helper(k,k,n,"",result);
        return result;
        
    }
    
    private void helper(int k, int invK, int n, String curStr, List<List<Integer>> result){
        if(k == 0){
            int sum = 0; 
            List<Integer> temp = new ArrayList<Integer>();
            for(int i = 0; i < curStr.length(); i ++){
                int tempI = Integer.parseInt(curStr.charAt(i)+"");
                sum+= tempI;
                temp.add(tempI);
            }
            
            if(sum == n)
                result.add(temp);
            
        }else{
            
            int start = k==invK?1:Integer.parseInt(curStr.charAt(curStr.length()-1)+"");
            
            for(int i = start; i<10; i ++){
                if(!curStr.contains(i+""))
                    helper(k-1,invK,n,curStr+""+i,result);
            }
        }
        
    }
}