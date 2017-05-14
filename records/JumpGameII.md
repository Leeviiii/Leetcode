## [Jump Game II](https://leetcode.com/problems/jump-game-ii/#/description)

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:

Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:

You can assume that you can always reach the last index.

## 分析：

动态规划的思想。跟Jump Game的思想基本一致。需要思考的是什么时候需要往前走一步？具体可以看代码实现

### [实现](../sourcecode/JumpGameII.md)
```
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxreach = 0
        lastreach = 0
        step = 0
        for i in range(len(nums)):
            if lastreach < i:
                step += 1
                lastreach = maxreach
            maxreach = max(nums[i] + i, maxreach)
        return step

```

