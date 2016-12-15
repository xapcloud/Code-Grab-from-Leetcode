###40 Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.



For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]


Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.


For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]


[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    // public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        
    //     ArrayList<Integer> can = new ArrayList<Integer>();
        
    //     for(int i = 0; i < candidates.length; i ++){
    //         if(candidates[i] <= target)
    //             can.add(candidates[i]);
    //     }
        
    //     List<List<Integer>> result = new ArrayList<List<Integer>>();
        
    //     if(can.size() == 0)
    //         return result;
        
    //     List<Integer> path = new ArrayList<Integer>();
        
    //     findAll(can,target,path,result);
    //     HashSet<String> hs = new HashSet<String>();
        
    //     for(int i = 0; i < result.size();){
    //         Collections.sort(result.get(i));
    //         if(hs.contains(result.get(i).toString())){
    //             result.remove(i);
    //         }else{
    //             hs.add(result.get(i).toString());
    //             i++;
    //         }
            
    //     }
        
    //     return result;
    // }
    // private void findAll(List<Integer> can, int target, List<Integer> path, List<List<Integer>> result){
    //     if(target == 0){
    //         //result.add(path);
    //         
            result.add(new ArrayList(path));
            return;
        }else if(target < 0){
            return;
        }else{
            for(int i = cur; i< can.size(); i ++){
                if(i > cur && can.get(i)==can.get(i-1))
            		continue;
                int r = can.remove(i);
                path.add(r);
                findAll(can,target-r,path,result,i++);
                path.remove(path.size()-1);
                can.add(--i,r);
            }
        }
    }
    
    
    
}