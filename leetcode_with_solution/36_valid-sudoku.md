###36 Valid Sudoku
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A partially filled sudoku which is valid.
A partially filled sudoku which is valid.Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isValidSudoku(char[][] board) {
        //check row & column
        HashSet<Character> h1;
        HashSet<Character> h2; 
        for(int i = 0; i < 9; i++){
            h1 = new HashSet<Character>();
            h2 = new HashSet<Character>();
            for(int j = 0; j < 9; j++ ){
                if(h1.contains(board[i][j]))
                    return false;
                if(h2.contains(board[j][i]))
                    return false;
                if(board[i][j]!='.')
                h1.add(board[i][j]);
                if(board[j][i]!='.')
                h2.add(board[j][i]);
                
            }
        }
        
        //checkgrid
        for(int i = 0; i < 3; i++){
            for(int j = 0; j <3; j++){
                h1 = new HashSet<Character>();
                for(int m = 0; m < 3; m++){
                    for(int n = 0; n < 3; n++){
                        if(h1.contains(board[i*3+m][j*3+n]))
                            return false;
                        if(board[i*3+m][j*3+n] != '.')
                        h1.add(board[i*3+m][j*3+n]);
                    }
                }
            }
        }
        return true;
    }
}