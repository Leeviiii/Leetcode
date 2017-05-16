## [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/#/description)


>Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

## 分析：

这道题目我觉得比[Spiral Matrix](./SpiralMatrix.md)这道题目要简单一点，因为这道题目只涉及到正方形，即长宽相同，直接在Spiral Matrix的代码上稍微修改一下，改为逆向的过程就可以了，不太难。

### [实现](../sourcecode/SpiralMatrixII.py)
```
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
```
