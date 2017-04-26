## [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/#/description)

>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

>(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

>Find the minimum element.

>You may assume no duplicate exists in the array.

## 分析：
题目中有一个很显眼的假设，在rotated的数组中是没有重复元素的，这道题有一个变形题，是没有这个假设的。这个假设可以让我们使用二分法来解决问题。


假设下面输入为下面的一个序列

>x1,x2...xj,y1,y2...yk

显然y1是最小的那个值，所以最小的值应该比他的两边值都小(如果最小值是最后一个元素或者第一个元素要特殊处理)

如何进行二分缩小范围取决于中间值是位于x这边还是y这边。由题目可以知道y1<y2<...<yk<x1<x1<..<xj,因此可以分为两种情况
- 第一种就是中间值落到了y这一范围内，即代码(nums[m] < nums[begin] and nums[m] < nums[end])成立,这是最小值一定在中间值的左边
- 第二种就是中间值落到了x这一范围内，这是最小值一定在中间值的右边

>只有上面两种，中间值是不可能大于nums[begin]小于nums[end]或者小于nums[begin]大于nums[end]的。

### [实现](../sourcecode/FindMinimuminRotatedSortedArray.py)
```
class Solution(object):
  def findMin(self, nums):
    if len(nums) == 0:
      return None
    if len(nums) == 1:
      return nums[0]
    begin = 0
    end = len(nums) - 1
    if nums[end] > nums[0]:
      return nums[0]
    while True:
      if end - begin == 1:
        return min(nums[begin],nums[begin + 1])
      m = (begin + end)/2
      if nums[m] < nums[m - 1] and nums[m] < nums[m + 1]:
        return nums[m]
      if nums[m] < nums[begin] and nums[m] < nums[end]:
        end = m
      else :
        begin = m
```
