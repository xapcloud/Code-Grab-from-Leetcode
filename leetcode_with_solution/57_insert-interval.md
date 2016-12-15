###57 Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].


Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].


This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).You may assume that the intervals were initially sorted according to their start times.
Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        
        List<Interval> result = new ArrayList<Interval>();
        
        if(intervals.isEmpty()){
            result.add(newInterval);
            return result;
        }
        
        int maxNum = Math.max(intervals.get(intervals.size()-1).end,newInterval.end)+1;
        //index i means i.5
        //such as mark[1]=1, means 1.5, means [1,2];
        int[]mark = new int[maxNum];
        intervals.add(newInterval);

        for(Interval inte: intervals){
            for(int i = inte.start;  i < inte.end;i++){
                mark[i]= 1;
            }
        }
        List<Integer> single= new ArrayList<Integer>();
        for(Interval inte: intervals){
            if(inte.start == inte.end){
               if((inte.start == 0||mark[inte.start-1]==0)&&(inte.end==maxNum-1||mark[inte.end]==0)){
                    single.add(inte.start);
               }
            }
        }
        // for(int i = 0;i < mark.length; i ++){
        //     System.out.print(mark[i]);
        // }
        
        // System.out.println("\n"+single);
        
        int start=0;
        int end=0;
        for(int i = 0; i < mark.length; i++){
            if(mark[i] == 1 && (i == 0 || mark[i-1]==0))
                start = i;
            if(mark[i] == 1 && (i == mark.length-1 || mark[i+1]== 0)){
                end = i+1;
                
                Interval temp = new Interval(start,end);
                result.add(temp);
            }
            if(single.contains(i)){
                result.add(new Interval(i,i));
            }
        }
        
        return result;
        
    }
}