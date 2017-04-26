## [Remove Element](https://leetcode.com/problems/remove-element/#/description)

>Given an array and a value, remove all instances of that value in place and return the new length.

>Do not allocate extra space for another array, you must do this in place with constant memory.

>The order of elements can be changed. It does not matter what you leave beyond the new length.

>Example:Given input array nums = [3,2,2,3], val = 3 

>Your function should return length = 2, with the first two elements of nums being 2.

## 分析：

首尾哨兵移动就可以了

### [实现](../sourcecode/RemoveElement.py)
```
class Solution(object):
  def removeElement(self, nums, val):
    l = 0
    r = len(nums) -1
    dup = 0
    while l <= r:
      n = nums[l]
      if n == val:
        nums[l] = nums[r]
        nums[r] = n
        dup += 1
        r -= 1
      else:
        l += 1
    return len(nums) - dup
```
