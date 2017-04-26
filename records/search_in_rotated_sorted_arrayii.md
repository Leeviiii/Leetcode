## [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/#/description)

>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

>(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

>Write a function to determine if a given target is in the array.

>The array may contain duplicates.

## 分析：
这道题目取消了元素不重复的假设。这个假设取消后导致没办法再用二分了，以下面的序列为例：
>8,8,8,8,1,8

上面的1可以出现在序列的任何位置，所以没有办法做二分必须遍历所有元素，时间复杂度下降到O(n)

### [实现](../sourcecode/SearchinRotatedSortedArrayII.py)
```
class Solution(object):
  def search(self, nums, target):
    if len(nums) == 0:
      return False
    for i in range(len(nums)):
      if nums[i] == target:
        return True
      return False

```
