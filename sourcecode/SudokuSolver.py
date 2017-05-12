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
        return False
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


if __name__ == "__main__":
    s = Solution()
    #a = ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]
    a = [[".",".","5",".",".",".",".",".","6"],[".",".",".",".","1","4",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".","9","2",".","."],["5",".",".",".",".","2",".",".","."],[".",".",".",".",".",".",".","3","."],[".",".",".","5","4",".",".",".","."],["3",".",".",".",".",".","4","2","."],[".",".",".","2","7",".","6",".","."]]
    s.solveSudoku(a)
    print a
