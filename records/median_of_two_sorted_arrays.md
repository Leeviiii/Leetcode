## [Median of Two Sorted Arrays*](https://leetcode.com/problems/median-of-two-sorted-arrays/#/description)

>There are two sorted arrays nums1 and nums2 of size m and n respectively.

>Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

## 分析：
看到这种有序的一般都是二分。最后有一个明确的对时间复杂度的要求，那就肯定二分了。

### [实现](../sourcecode/MedianofTwoSortedArrays.py)
```
class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    k = len(nums1) + len(nums2)
    if k%2== 1:
      m = self.binaryseach(nums1,nums2,k/2 + 1)
    else:
      b = self.binaryseach(nums1,nums2,k/2)
      s = self.binaryseach(nums1,nums2,k/2+1)
      m = (b+s)/2.0
    return m
  def binaryseach(self, nums1,nums2,k):
    if len(nums1) == 0:
      return nums2[k-1]
    if len(nums2) == 0:
      return nums1[k-1]
    if k == 1 :
      return min(nums1[0],nums2[0])
    a = nums1[k/2-1] if len(nums1) >= k/2 else None
    b = nums2[k/2-1] if len(nums2) >= k/2 else None
    if b is None or (a is not None and a < b):
      return self.binaryseach(nums1[k / 2:], nums2, k - k / 2)
    return self.binaryseach(nums1, nums2[k / 2:], k - k / 2)
```
