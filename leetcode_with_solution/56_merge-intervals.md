###56 Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        
        //æè·¯ï¼æå»ºä¸ä¸ªxè½´ï¼å¯¹äºææ[a,b]ï¼å° a å°b-1è®¾ç½®ä¸ºtrue,
        //ç¶åæ«ææ´ä¸ªxè½´ï¼æå»ºè¿åå¼

        List<Interval> result = new ArrayList<Interval>();
        
        int max = 0;
        for(int i = 0; i < intervals.size(); i ++){
            max = max > intervals.get(i).end ? max : intervals.get(i).end;
        }
        
        boolean [] line = new boolean [max+1];
        for(int i = 0; i < intervals.size(); i ++){
           Interval intr = intervals.get(i);
           int s = intr.start;
           int e = intr.end;
           for(int j = s; j < e ; j ++){
               line[j] = true;
           }
        }

        boolean isInter = false;
        int s = 0 ,e  = 0 ;
        for(int i = 0; i <= max; i ++){
            if(line[i]  && !isInter){
                s = i;
                isInter = true;
            }
            if(!line[i]  && isInter){
                e = i;
                isInter = false;
                
                result.add(new Interval(s,e));
            }
            
        }
 
        HashSet<Integer> hs = new HashSet<Integer>();
        for(int i = 0; i < intervals.size(); i ++){
             Interval intr = intervals.get(i);
             if(intr.start == intr.end && line[intr.start] ==false && !hs.contains(intr.start)){
                int temp = intr.start;
                if(temp == 0){
                    result.add(new Interval(0,0));
                    hs.add(temp);
                }
                else if(line[temp-1] == false){
                    result.add(new Interval(temp,temp));
                    hs.add(temp);
                }
                    
             }
        }
 
 
        return result;
    }
}