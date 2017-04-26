## [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description)

>Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

>Do not allocate extra space for another array, you must do this in place with constant memory.

>For example,Given input array nums = [1,1,2],

>Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the new length.

## 分析：

首尾哨兵移动就可以了

### [实现](../sourcecode/RemoveDuplicatesfromSortedArray.py)
```
class Solution(object):
  def removeDuplicates(self, nums):
    l1 = 0
    l2 = 1
    dup = 0
    if len(nums) > 0:
      lastn = nums[0]
    r = len(nums)
    while l2 < r:
      n = nums[l2]
      if n <= lastn:
        l2 += 1
        dup += 1
      else:
        if l2 - l1 > 1:
          nums[l2] = lastn
          nums[l1 + 1] = n
      l1 += 1
      l2 += 1
      lastn = n
  return len(nums) - dup
```
