###52 N-Queens II
Follow up for N-Queens problem.
Now, instead outputting board configurations, return the total number of distinct solutions.
Follow up for N-Queens problem.Now, instead outputting board configurations, return the total number of distinct solutions.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int totalNQueens(int n) {
        int [] map = new int[n];
        List<List<String>> ret = new ArrayList<List<String>>();
    
        String aux = "";
        for(int i = 0; i < n; i ++)
            aux+=".";
        find(map,0,n,ret,aux); 
        
        return ret.size();
    }
    
    private void find(int[] map, int curIndex, int size, List<List<String>> ret,String aux){
        if(curIndex == size){
            List<String> temp = new ArrayList<String>();
            for(int i = 0; i < size; i ++){
                temp.add(aux.substring(0,map[i])+"Q"+aux.substring(0,size-map[i]-1));
            }
            ret.add(temp);
        }
        
        for(int i = 0; i < size; i ++){
            if(check(map, curIndex,i)){
                map[curIndex] = i;
                find(map,curIndex+1,size,ret,aux);
            }
        }
    }
    
    private boolean check(int [] map, int index, int val){
         if(index == 0)
            return true;
        
        boolean ret = true;
        
        for(int i = 0; i < index; i ++){
            ret = ret && (map[i] != val) && (map[i] - i != val - index) && (map[i]+i != val+index);
            if(ret == false)
                return false;
        }
        
        return ret;
    }
}