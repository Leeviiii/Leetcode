## [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/#/description)

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

## 分析：

两个数组从从后往前扫描，原因是数组1的容量足够。时间负责度O(m+n),没有额外空间消耗。

### [实现](../sourcecode/MergeSortedArray.py)
```
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0  and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j] 
            k -= 1
            j -= 1
```
