## [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/#/description)

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,

Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

## 分析：

用一个哈希表记录着每一个元素出现的次数。

### [实现](../sourcecode/RemoveDuplicatesfromSortedArrayII.py)
```
class Solution(object):
    def removeDuplicates(self, nums):
        l1 = 0
        l2 = 1
        dup = 0
        if len(nums) > 0:
            lastn = nums[0]
        nums_du = {}
        n = 0
        for i in range(len(nums)):
            if i != n:
                nums[n] = nums[i]
            if nums[i] in nums_du:
                cnt = nums_du[nums[i]]
                if cnt == 1:
                    n += 1
                nums_du[nums[i]] += 1
            else:
                nums_du[nums[i]] = 1
                n += 1
        return n
```
