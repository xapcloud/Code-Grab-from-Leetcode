###419 Battleships in a Board
Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:


You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

Example:
X..X
...X
...X

In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X

This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

Subscribe to see which companies asked this question

Example:
X..X
...X
...X

In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X

This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

Subscribe to see which companies asked this question

X..X
...X
...X
Invalid Example:
...X
XXXX
...X

This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?...X
XXXX
...X
Follow up:Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int countBattleships(char[][] board) {
        
        int num = 0;
        
        int r = board.length;
        int c = board[0].length;
        
        for(int i = 0; i < r; i ++ ){
            for(int j = 0; j < c; j++){
                
                if(board[i][j] == 'X'){
                    num++;
                    board[i][j]='.';
                    
                    int ii = i+1;
                    int jj = j+1;
                    
                    while(jj < c && board[i][jj]=='X'){
                        board[i][jj]='.';
                        jj++;
                    }
                    
                    while(ii < r && board[ii][j]=='X'){
                        board[ii][j]='.';
                        ii++;
                    }
                    
                    
                }
            }
        }
        
        return num;
        
        
    }
}