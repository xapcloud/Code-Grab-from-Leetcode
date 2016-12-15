###39 Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. 

The same repeated number may be chosen from C unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.



For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 

[
  [7],
  [2, 2, 3]
]


Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. 
The same repeated number may be chosen from C unlimited number of times.
Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.


For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 

[
  [7],
  [2, 2, 3]
]


[
  [7],
  [2, 2, 3]
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    
   
    
    //ä¸è¿°ç­æ¡æ²¡æèèå¯éå¤
  public static List<List<Integer>> combinationSum(int[] candidates, int target) {
	        
	        List<List<Integer>> result = new ArrayList<List<Integer>>();
	        int [] mark = new int [candidates.length];
	        helpFunc(candidates,target,0,0,mark,result);
	        return result;
	   
	    }
	    
	    private static void helpFunc(int [] can, int target, int curIndex, int curSum ,int [] mark, List<List<Integer>> result){
	    	
	    	if(curSum == target){
	            List<Integer> l = new ArrayList<Integer>();
	            for(int i = 0; i < mark.length; i ++){
	                if(mark[i] > 0){
	                	for(int j = 0; j < mark[i]; j ++){
	                		l.add(can[i]);
	                	}
	                }	
	            }
	 
	            result.add(l);
	        }else if (curSum> target){
	            
	        }else{
	            if(curIndex < mark.length){
	            	
	            	int count = 0;
	            	while(curSum+count*can[curIndex]<=target){
	            		mark[curIndex] = count;
	 	                helpFunc(can,target,curIndex+1,curSum+can[curIndex]*count,mark,result);
	 	                count++;
	            	}
	                mark[curIndex]=0;
	            }
	        }
	    }

    
}