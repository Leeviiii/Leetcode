class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        l = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(0)
            l.append(tmp)
        for j in range(1,n):
            l[0][j] = 1
        for i in range(1,m):
            l[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                l[i][j] = l[i-1][j] + l[i][j-1]
        return l[m-1][n-1]
                                                            
if __name__ == "__main__":
    s = Solution()
    r = s.uniquePaths(1,2)
    print r
