## [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/#/submissions/1)

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

## 分析：

线性扫描就可以，遇到正数就加，遇到负数有两种情况，如果负数太大导致加上负数后为负数，那么当前就是临时最大值，从下一个位置开始累积;否则继续往后查找。

### [实现](../sourcecode/MaximumSubarray.py)
```
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        currmentmax = nums[0]
        retmax = nums[0]
        for i in range(1,len(nums)):
            if nums[i] >= 0:
                if currmentmax > 0:
                    currmentmax += nums[i]
                else:
                    currmentmax = nums[i]
            else:
                if currmentmax > 0:
                    if currmentmax + nums[i] <= 0:
                        currmentmax = 0
                    else :
                        currmentmax = currmentmax + nums[i]
                else:
                    currmentmax = max(currmentmax,nums[i])
                if currmentmax > retmax:
                    retmax = currmentmax
        return retmax
```
