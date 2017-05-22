## [Unique Paths](https://leetcode.com/problems/unique-paths/#/description)

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

## 分析：

解法一：这种题首先可以想到递归遍历的，从(0,0)点出发，要么往右边走到(0,1)，要么往下走到(1,0)，这样一直分两种情况走到(m-1,n-1)就是最后的答案。可以做但是会超时

解法二：既然递归会超时，要么就应该存在一个动态规划的思想来节省计算步骤。设L[i][j]表示从(0,0)点到(i,j)点的所有可能路径，可以得到递推公式
```
L[i][j] = 1 if i=0 or j=0
L[i][j] = L[i-1][j] + L[i][j] else
```
这个递归公式还是挺简单的，求(0,0)点到一个点的所有可能路径，只要将(0,0)点到这个点的正上方的点和正左边的点的可能路径加和就可以了，另外注意下特殊情况就OK了。

### [实现](../sourcecode/UniquePaths.py)
```
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
```
