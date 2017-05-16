## [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/#/description)


>Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

## 分析：

按照螺旋方式进行数组遍历，类似于[Rotate Image](./RotateImage.md)这道题目，都是基本的数组操作。一层一层遍历就可以，每次遍历区分四个方向

以下图为例进行说明。假设数组的长度为m,宽度为n
```
-------------------------------->x
|
|
|      -----------------
|      |               |
|      |   |--------|  |
|      |   |        |  |
|      |   |        |  |
|      |   |--------|  |
|      |               |
|      |---------------|
|
V
y
```
加上上层的内图是第i层，则可以得出，四个端点的坐标信息
```
左上点坐标(i,i)
右上点坐标(i,m-i)
左下点坐标(m-i,i)
右下点坐标(n-i,m-i)
```

梳理好上面的四个点，然后一层层的遍历就可以。遍历过程中考虑好特殊处理，主要就是长宽不相等的两种情况，一种长大于宽，一种长小于宽。

### [实现](../sourcecode/SpiralMatrix.py)
```
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
```
