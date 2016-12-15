###79 Word Search

Given a 2D board and a word, find if the word exists in the grid.


The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.


For example,
Given board = 

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board = 

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean exist(char[][] board, String word) {
        
        boolean ret = false;
        boolean [][] isVisited = new boolean [board.length][board[0].length];
        
        for(int i = 0; i < board.length; i ++){
            for(int j = 0; j < board[0].length; j ++){
                if(board[i][j] == word.charAt(0))
                    ret = ret||auxiliary(word.substring(1),i,j,board,isVisited);
            }
            
        }
        return ret;
    }
    
    private boolean auxiliary(String s, int i, int j, char[][]board,boolean [][] isVisited){
        isVisited[i][j] = true;
        
        if(s.length() == 0)
            return true;
        
        boolean ret = false;
        char c = s.charAt(0);
        s = s.substring(1);
        
        if(i > 0 && isVisited[i-1][j] == false &&board[i-1][j] == c)
            ret = ret || auxiliary(s,i-1,j,board,isVisited);
        if(j > 0 && isVisited[i][j-1] == false &&board[i][j-1] == c)
            ret = ret || auxiliary(s,i,j-1,board,isVisited);
        if(i < board.length-1 && isVisited[i+1][j] == false&& board[i+1][j] == c)
            ret = ret || auxiliary(s,i+1,j,board,isVisited);
        if(j < board[0].length -1 &&isVisited[i][j+1] == false&& board[i][j+1] == c)
            ret = ret || auxiliary(s,i,j+1,board,isVisited);
        
        isVisited[i][j] = false;
            
        return ret;
            
    }
}