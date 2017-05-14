## [Jump Game](https://leetcode.com/problems/jump-game/#/description)

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:

A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

## 分析：

动态规划的思想。记录当前可以达到的最大距离，最后判断最大距离跟终点的差距。

### [实现](../sourcecode/JumpGame.py)
```
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxreach = 0
        for i in range(len(nums)-1):
            if i > maxreach:
                continue
            maxreach = max(nums[i] + i, maxreach)
        if maxreach + 1 < len(nums):
            return False
        return True
```

