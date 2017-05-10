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


if __name__ == "__main__":
    s = Solution()
    #a = ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]
    a = ["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]
    r = s.isValidSudoku(a)
    print r
