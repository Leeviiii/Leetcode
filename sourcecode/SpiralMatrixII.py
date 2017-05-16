class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [] 
        matrix = []
        for i in range(n):
            l = []
            for i in range(n):
                l.append(0)
            matrix.append(l)
        n = len(matrix)
        m = n
        mi = 0
        num = 1
        while num <= n*n:
            for i in range(mi,m-mi):
                matrix[mi][i] = num
                num += 1
            if m-mi-1 >= mi:
                for i in range(mi+1,n-mi):
                    matrix[i][m-mi-1] = num
                    num += 1
            if n-mi-1 > mi:
                i = m-mi-2
                while i >= mi:
                    matrix[n-mi-1][i] = num
                    num += 1
                    i -= 1
            if m-mi-1 > mi:
                i = n-mi-2
                while i > mi:
                    matrix[i][mi] = num
                    num += 1
                    i -= 1
            mi += 1
        return matrix



if __name__ == "__main__": 
    s = Solution()
    n = 4
    ret = s.generateMatrix(n)
    print ret
