class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        ret = []
        mi = 0
        while mi*2 < n:
            for i in range(mi,m-mi):
                ret.append(matrix[mi][i])
            if m-mi-1 >= mi:
                for i in range(mi+1,n-mi):
                    ret.append(matrix[i][m-mi-1])
            if n-mi-1 > mi:
                i = m-mi-2
                while i >= mi:
                    ret.append(matrix[n-mi-1][i])
                    i -= 1
            if m-mi-1 > mi:
                i = n-mi-2
                while i > mi:
                    ret.append(matrix[i][mi])
                    i -= 1
            mi += 1
        return ret



if __name__ == "__main__": 
    #s1 = [-2,1,-3,4,-1,2,1,-5,4]
    #s1 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
    #s1 = [[1,2],[3,4],[5,6]]
    s1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    s = Solution()
    ret = s.spiralOrder(s1)
    print ret
