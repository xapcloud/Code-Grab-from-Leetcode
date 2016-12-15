###391 Perfect Rectangle

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.


Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.




Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.




Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.




Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.



Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.


rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.


rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.


rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.


rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
Subscribe to see which companies asked this question
###Solution
```java
import java.util.*;
public class Solution {

    public boolean isRectangleCover(int[][] rectangles) {
        
        //find the four vertices
        //[x1,y1,x2,y2]ææçç¹éæ¾åºæleftbottom rightbottom leftup rightup
        //leftbottom x1,y1æå°
        //rightup  x2,y2 æå¤§
        //leftup  x1æå° y2æå¤§
        //rightbottom  x2æå° y1æå¤§
        int [] node = new int[4];
        node = findVertices(rectangles);
        
        
        List<String> dingdian = new ArrayList<String>();
        dingdian.add(node[0]+" "+node[1]);
        dingdian.add(node[2]+" "+node[3]);
        dingdian.add(node[0]+" "+node[3]);
        dingdian.add(node[2]+" "+node[1]);

        
        
        Hashtable<String,String> nodes = new Hashtable<String,String>();
        for(int i = 0; i < rectangles.length; i ++){
            List<String> vs = new ArrayList<String>();
          
            vs.add(rectangles[i][0]+" "+rectangles[i][1]);
            vs.add(rectangles[i][2]+" "+rectangles[i][3]);
            vs.add(rectangles[i][2]+" "+rectangles[i][1]);
            vs.add(rectangles[i][0]+" "+rectangles[i][3]);
            
            int count = 0;
            for(String v: vs){
                if(nodes.containsKey(v))
                    nodes.put(v,nodes.get(v)+count);
                else
                    nodes.put(v,count+"");
                count++;
            }
        }

        Iterator<String> it = nodes.keySet().iterator();
        int flag = 4;
        HashSet<String> adj = new HashSet<String>();
        adj.add("01");
        adj.add("10");
        adj.add("23");
        adj.add("32");
        adj.add("00");
        adj.add("11");
        adj.add("22");
        adj.add("33");
        while(it.hasNext()){
        	String temp = it.next();
        	String mark = nodes.get(temp);
        	
        	if(mark.length() == 1){
        		if(!dingdian.contains(temp))
        			return false;
        		flag --;
        	}else if(mark.length() == 2){
        		if(adj.contains(mark))
        		    return false;
        	}else if (mark.length() == 4){
        	    for(int i = 0; i < 4; i ++){
        	        if(!mark.contains(i+""))
        	            return false;
        	    }
        	}else
        		return false;
        	
        	
        }
        
        
        
        if(flag == 0)
            return true;
        else 
            return false;
    }
    
    private int[] findVertices(int [][] rectangles){
        int [] ret = new int[4];
        ret[0]  = Integer.MAX_VALUE;
        ret[1]  = Integer.MAX_VALUE;
        ret[2]  = Integer.MIN_VALUE;
        ret[3]  = Integer.MIN_VALUE;

        for(int i = 0; i < rectangles.length; i ++){
            ret[0]  = Math.min(ret[0],rectangles[i][0]);
            ret[1]  = Math.min(ret[1],rectangles[i][1]);
            ret[2]  = Math.max(ret[2],rectangles[i][2]);
            ret[3]  = Math.max(ret[3],rectangles[i][3]);
        }
        return ret;
    }
    
    
    
}