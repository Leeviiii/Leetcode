## [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/#/description)

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

## 分析：

这是一个从F(2)开始的斐波那契数列

### [实现](../sourcecode/ClimbingStairs.py)
```
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        l1 = 1
        l2 = 2
        l3 = 0
        for i in range(3,n+1):
            l3 = l1 + l2
            l1 = l2
            l2 = l3
        return l3
```
