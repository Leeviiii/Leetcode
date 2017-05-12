## [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/#/description)

>Write a program to solve a Sudoku puzzle by filling the empty cells.

>Empty cells are indicated by the character '.'.

## 分析：

这道题是之前的Valid Sudoku题目的进阶问题。方法就是遍历每一个空位置，然后进行判断是否为合法的Sudoku。相对于Valid Sudoku的程序可以做一个优化，因为每一次对一个位置的值进行改变的时候，之前一定是一个Valid的，所以只要检查被修改的那个值影响的那一行，那一列，以及那个元素所在的九宫格就可以了。

### [实现](../sourcecode/SudokuSolver.py)
```
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solvesudoku1(board,0,0)

    def solvesudoku1(self, board, i, j):                                                    
        if j >= 9:
            return self.solvesudoku1(board,i+1,0)
        if i == 9: 
            return True
        if board[i][j] == '.':
            for k in range(1,10):
                board[i][j] = str(k)
                if self.isValidSudoku(board,i,j) == True:
                    if self.solvesudoku1(board,i,j+1) == True:
                        return True
                board[i][j] = '.'
        else:
            return self.solvesudoku1(board,i,j+1)
    def isValidSudoku(self, board,m,n):
        for j in range(9):
            if j != n and board[m][n] == board[m][j]:
                return False
        for j in range(9):
            if j != m and board[m][n] == board[j][n]:
                return False
        i = m/3 * 3
        j = n/3 * 3
        for k1 in range(i,i+3):
            for k2 in range(j,j+3):
                if board[m][n] == board[k1][k2] and (m != k1 or n != k2):
                    return False
       return True
```
