###51 N-Queens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.Given an integer n, return all distinct solutions to the n-queens puzzle.Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<List<String>> solveNQueens(int n) {
        int [] map = new int[n];
        List<List<String>> ret = new ArrayList<List<String>>();
    
        String aux = "";
        for(int i = 0; i < n; i ++)
            aux+=".";
        find(map,0,n,ret,aux); 
        
        return ret;
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