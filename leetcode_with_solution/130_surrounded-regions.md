###130 Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.


For example,

X X X X
X O O X
X X O X
X O X X



After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X


Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X


X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X


X X X X
X X X X
X X X X
X O X X
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    // public void solve(char[][] board) {

    //     if(!(board.length == 0 || board[0].length == 0)){
    //     int row = board.length;
    //     int column = board[0].length;
        
    //     boolean[][] vis = new boolean[row][column];
        
    //     for(int j = 0; j < column; j++){
    //         check(0,j,vis,board,row,column);
    //         check((row-1),j,vis,board,row,column);
    //     }
        
    //     for(int i = 1; i < row-1; i ++){
    //         check(i,0,vis,board,row,column);
    //         check(i,(column-1),vis,board,row,column);
    //     }
    //     for(int i = 0; i < row; i ++){
    //         for(int j = 0; j < column; j ++){
    //             if(vis[i][j] == false)
    //                 board[i][j] = 'X';
                
    //         }
    //     }
    //     }
    // }
    // private static void check(int i, int j, boolean [][] vis, char[][]board, int row, int column){
    //     if(board[i][j] == 'O' && vis[i][j] == false){
    //         vis[i][j] = true;
    //         if(i > 0){
    //             check(i-1,j,vis,board,row,column);
    //         }
            
    //         if(i < row -1 ){
    //             check(i+1,j,vis,board,row,column);
    //         }
    //         if(j > 0){
    //             check(i,j-1,vis,board,row,column);
    //         }
            
    //         if(j < column -1 ){
    //             check(i,j+1,vis,board,row,column);
    //         }
    //     }
        
    // }
    // java.lang.StackOverflowError
    public void solve(char[][] board) {
        if(board.length <= 2 || board[0].length <= 2){
         return;
        }
        int r = board.length;
        int c = board[0].length;
        boolean[][] mask = new boolean[r][c];
        for(int i = 0; i < (r+1)/2; i ++){
            if(i == 0){
                for(int j = i; j < c-i; j ++){
                    if(board[i][j] =='O'){
                        mask[i][j] = true;
                        if(board[i+1][j] == 'O')
                            mask[i+1][j] = true;
                    }
                    if(board[r-i-1][j] == 'O'){
                        mask[r-i-1][j] = true;
                        if(board[r-i-2][j] == 'O')
                            mask[r-i-2][j] = true;
                    }
                }
                for(int j = i ; j < r-i; j ++){
                    if(board[j][i] =='O'){
                        mask[j][i] = true;
                        if(board[j][i+1]=='O')
                            mask[j][i+1] = true;
                  
                    }
                    if(board[j][c-i-1] == 'O'){
                        mask[j][c-i-1] = true;
                        if(board[j][c-i-2] == 'O')
                            mask[j][c-i-2]= true;
                    }
                }
            }else{
                for(int j = i; j < c-i; j ++){
                    if(board[i][j] =='O'&&(mask[i-1][j] == true || mask[i][j-1]) == true){
                        mask[i][j] = true;
                        if(board[i+1][j] == 'O')
                            mask[i+1][j] = true;
                    }
                    if(board[r-i-1][j] == 'O' && (mask[r-i][j]==true || mask[r-i-1][j-1] == true)){
                        mask[r-i-1][j] = true;
                        if(board[r-i-2][j] == 'O')
                            mask[r-i-2][j] = true;
                    }
                }
                for(int j = c-i-1; j >= i; j --){
                    if(board[i][j] =='O'&&(mask[i-1][j] == true || mask[i][j+1]) == true){
                        mask[i][j] = true;
                        if(board[i+1][j] == 'O')
                            mask[i+1][j] = true;
                    }
                    if(board[r-i-1][j] == 'O' && (mask[r-i][j]==true || mask[r-i-1][j+1] == true)){
                        mask[r-i-1][j] = true;
                        if(board[r-i-2][j] == 'O')
                            mask[r-i-2][j] = true;
                    }
                }
                for(int j = i ; j < r-i; j ++){
                    if(board[j][i] =='O'&&(mask[j-1][i] == true || mask[j][i-1]== true)){
                        mask[j][i] = true;
                        if(board[j][i+1]=='O')
                            mask[j][i+1] = true;
                  
                    }
                    if(board[j][c-i-1] == 'O'&&(mask[j-1][c-i-1] == true|| mask[j][c-i]==true)){
                        mask[j][c-i-1] = true;
                        if(board[j][c-i-2] == 'O')
                            mask[j][c-i-2]= true;
                    }
                }
                 for(int j = r-i-1 ; j >=i; j --){
                    if(board[j][i] =='O'&&(mask[j+1][i] == true || mask[j][i-1]== true)){
                        mask[j][i] = true;
                        if(board[j][i+1]=='O')
                            mask[j][i+1] = true;
                  
                    }
                    if(board[j][c-i-1] == 'O'&&(mask[j][c-i] == true|| mask[j+1][c-i-1]==true)){
                        mask[j][c-i-1] = true;
                        if(board[j][c-i-2] == 'O')
                            mask[j][c-i-2]= true;
                    }
                }
            }
        }

        for(int i = (r+1)/2 -1 ; i > 0; i --){
                for(int j = i; j < c-i; j ++){
                    if(mask[i][j] == true){
                        mask[i-1][j] = board[i-1][j]=='O'?true:false;
                        mask[i][j+1] = board[i][j+1]=='O'?true:false;
                    }
                    if(mask[r-i-1][j] == true){
                        mask[r-i-1][j+1] = board[r-i-1][j+1]=='O'?true:false;
                        mask[r-i][j] = board[r-i][j]=='O'?true:false;
                    }
                }
                for(int j = c-i-1; j >= i; j --){
                    if(mask[i][j] == true){
                        mask[i-1][j] = board[i-1][j]=='O'?true:false;
                        mask[i][j-1] = board[i][j-1]=='O'?true:false;
                    }
                    if(mask[r-i-1][j] == true){
                        mask[r-i-1][j-1] = board[r-i-1][j-1]=='O'?true:false;
                        mask[r-i][j] = board[r-i][j]=='O'?true:false;
                    }
                }
                for(int j = i ; j < r-i; j ++){
                    if(mask[j][i]== true){
                        mask[j][i-1] = board[j][i-1]=='O'?true:false;
                        mask[j+1][i] = board[j+1][i]=='O'?true:false;
                    }
                    if(mask[j][c-i-1]==true){
                        mask[j][c-i] = board[j][c-i]=='O'?true:false;
                        mask[j+1][c-i-1] = board[j+1][c-i-1]=='O'?true:false;
                    }
                }
                for(int j = r-i-1 ; j >=i; j --){
                   if(mask[j][i]== true){
                        mask[j][i-1] = board[j][i-1]=='O'?true:false;
                        mask[j-1][i] = board[j-1][i]=='O'?true:false;
                    }
                    if(mask[j][c-i-1]==true){
                        mask[j][c-i] = board[j][c-i]=='O'?true:false;
                        mask[j-1][c-i-1] = board[j-1][c-i-1]=='O'?true:false;
                    }
                }
        }
        for(int i = 0; i < r; i ++){
            for(int j = 0; j < c ; j ++){
                if(mask[i][j] == false)
                    board[i][j] = 'X';
            }
        }
    }
}