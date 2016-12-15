###210 Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:
2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

click to show more hints.
Hints:

This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.


There are a total of n courses you have to take, labeled from 0 to n - 1.Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
For example:2, [[1,0]]There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]4, [[1,0],[2,0],[3,1],[3,2]]There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
click to show more hints.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
        // int[] result = new int[numCourses];
        // int[] index = new int[numCourses];
        
        
        // if(!canFinish(numCourses,prerequisites))
        //     return new int[0];
        
        
        // for(int i = 0; i < numCourses; i ++){
        //     result[i] = i;
        //     index[i] = i;
        // }
        
        // boolean flag = false;
        
        // do{
        //     flag = false;
        //     for(int i = 0; i < prerequisites.length; i ++){
        //         int pre = prerequisites[i][1];
        //         int aft = prerequisites[i][0];
                
        //         if(index[pre]>index[aft]){
        //             flag = true;
        //             int t = result[index[pre]];
        //             result[index[pre]] = result[index[aft]];
        //             result[index[aft]] = t;
                    
        //             t = index[pre];
        //             index[pre] = index[aft];
        //             index[aft]= t;
        //         }
        //     }
        // }while(flag);
        
        // return result;
        
        
        //éæºäº¤æ¢é¡ºåºä¸å¯¹çåºåç´å°ææçé¡ºåºé½æ­£ç¡®ï¼ä½æ¯Compile time limit exceeded.
        
         List<Set> g = new ArrayList<Set>(); 
         for(int i = 0; i < numCourses; i ++){
             g.add(new HashSet<Integer>());
         }
         
         for(int i = 0; i < prerequisites.length; i ++){
             g.get(prerequisites[i][1]).add(prerequisites[i][0]);
         }
         
         int[] inDegree = new int [numCourses];
         
         for(int i = 0; i < numCourses; i ++){
             Set set = g.get(i);
             Iterator<Integer> it = set.iterator();
             while(it.hasNext()){
                 inDegree[it.next()]++;
             }
         }
         
         List<Integer> result = new ArrayList<Integer>();
         
         for (int i = 0; i < numCourses; i++) {  
            int j = 0;  
            for ( ; j < numCourses; j++) {  
                if (inDegree[j] == 0) {
                    result.add(j);
                    break;  
                }
            }  
              
            if (j == numCourses) 
                return new int[0];  
              
            inDegree[j] = -1;  
              
            Set set = g.get(j);  
            Iterator<Integer> it = set.iterator();  
            while (it.hasNext()) {  
                inDegree[it.next()]--;  
            }  
        }  
          
        int[] ret = new int[numCourses];
        for(int i = 0; i < numCourses; i ++){
            ret[i] = result.get(i);
        }  
        
        return ret;
    }
}