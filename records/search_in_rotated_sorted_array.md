## [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/#/description)

>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

>(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

>You are given a target value to search. If found in the array return its index, otherwise return -1.

>You may assume no duplicate exists in the array.

## 分析：
题目中有一个很显眼的假设，在rotated的数组中是没有重复元素的，这道题有一个变形题，是没有这个假设的。这个假设可以让我们使用二分法来解决问题。

假设下面输入为下面的一个序列

>x1,x2...xj,y1,y2...yk

如何进行二分缩小范围取决于中间值是位于x这边还是y这边。由题目可以知道y1<y2<...<yk<x1<x1<..<xj,因此首先分为两种情况,每种情况又分为两种情况，即目标值与中间值的大小关系
- 第一种就是中间值落到了y这一范围内，即代码(nums[m] < nums[begin] and nums[m] < nums[end])成立
  - 如果目标值大于中间值,则目标值是可能在中间值的右边，也可能在中间值的左边，因此两个都要进行查找(如果一路这样下来时间复杂度就从O(logn)变成了O(n)了)
  - 否则目标值一定位于中间值的左边，这个时候二分大法才会发挥威力
- 第二种就是中间值落到了x这一范围内
  - 如果目标值小于中间值,则目标值是可能在中间值的右边，也可能在中间值的左边，因此两个都要进行查找
  - 否则目标值一定位于中间值的左边，这个时候二分大法才会发挥威力

>只有上面两种，中间值是不可能大于nums[begin]小于nums[end]或者小于nums[begin]大于nums[end]的。

### [实现](../sourcecode/SearchinRotatedSortedArray.py )
```
class Solution(object):
  def search(self, nums, target):
    if len(nums) == 0:
      return -1
    begin = 0
    end = len(nums) - 1
    return self.binarysearch(nums,begin,end,target)
  def binarysearch(self,nums,begin,end,target):
    if end == begin:
      if nums[begin] == target:
        return begin
      return -1
    if end - begin == 1:
      if nums[begin] == target:
        return begin
      if nums[end] == target:
        return end
       return -1
     m = (begin + end)/2
     if nums[m] == target:
       return m
     if nums[m] < nums[begin] and nums[m] < nums[end]:
       if target > nums[m]:
         x = self.binarysearch(nums,begin,m,target)
         if x == -1:
           return self.binarysearch(nums,m,end,target)
         return x
       else:
         return self.binarysearch(nums,begin,m,target)
     else:
       if target > nums[m]:
         return self.binarysearch(nums,m,end,target)
       else:
         x = self.binarysearch(nums,begin,m,target)
         if x == -1:
           return self.binarysearch(nums,m,end,target)
         return x
```
