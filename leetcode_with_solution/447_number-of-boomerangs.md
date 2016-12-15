###447 Number of Boomerangs
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
Subscribe to see which companies asked this question
###Solution
```java

import java.util.*;
public class Solution {
    
    public int numberOfBoomerangs(int[][] points) {
       if(points.length<3)
            return 0;
        
        int result = 0;
        for(int i = 0; i < points.length; i ++){
            Hashtable<Long,Integer> dis= new Hashtable<Long,Integer>();
            for(int j = 0; j< points.length; j++){
                
                long distance = (points[i][0]-points[j][0])*(points[i][0]-points[j][0])+(points[i][1]-points[j][1])*(points[i][1]-points[j][1]);
                
                if(dis.containsKey(distance))
                    dis.put(distance,dis.get(distance)+1);
                else
                    dis.put(distance,1);
            }
            
            for(Map.Entry<Long,Integer> entry: dis.entrySet()){
                int val = entry.getValue();
                result += val*(val-1);
            }
        }
        
        
        
        return result;
    }
}