## [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/#/description)

>Determine if a Sudoku is valid, according to: [Sudoku Puzzles - The Rules.](http://sudoku.com.au/TheRules.aspx)

>The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

## 分析：

之前并不明白数独的规则，可以看一下上面的那个Sudoku Puzzles来了解。解法就是按照规则进行遍历，先看每一行，再看每一列，最后看每一个3*3的正方形。

### [实现](../sourcecode/ValidSudoku.py)
```
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9:
            return False;
        for l in board:
            if len(l) != 9:
                return False
        
        for i in range(9):
            sign = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in sign:
                        return False
                    sign[board[i][j]] = 1
        for i in range(9):
            sign = {}
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in sign:
                        return False
                    sign[board[j][i]] = 1

        for i in [0,3,6]:
            for j in [0,3,6]:
                sign = {}
                for k in range(i,i+3):
                    for m in range(j,j+3):
                        c = board[k][m]
                        if c != ".":
                            if c in sign:
                                return False
                            sign[c] = 1
        return True
```
