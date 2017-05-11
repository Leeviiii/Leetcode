## [First Missing Positive](https://leetcode.com/problems/first-missing-positive/#/description)

>Given an unsorted integer array, find the first missing positive integer.

>Your algorithm should run in O(n) time and uses constant space.

## 分析：

这道题本身不难，难的是限制条件，要求O(n)，否则排序直接搞定。第二要求不能使用额外空间，否则一个哈希表O(n)直接搞定。因此其实挺容易想出来将数字i放在数字i-1的位置上，扫一遍数组后，就将所有合法的数字放在了他应该在的位置上，然后扫描数组，第一个不符合数字i在数字i-1的位置的就是缺失的那个数字

>思路其实不太难想，但是各种特殊情况的处理真是折杀老夫。我想着也是这道题是hard的原因，我是一次次提交一次次修正的，惭愧。

### [实现](../sourcecode/FirstMissingPositive.py)
```
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        l = 0
        r = len(nums)
        while l < r:
            if nums[l] >0 and nums[l] != l + 1 and nums[l] - 1 < r and nums[l] != nums[nums[l]-1]:
                self.swap(nums, l, nums[l] - 1)
            else:
                l += 1
        i = 0
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i +1 
        return i + 2
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
```
