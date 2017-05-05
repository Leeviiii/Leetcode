## [Search Insert Position](https://leetcode.com/problems/search-insert-position/#/description)

>Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

>You may assume no duplicates in the array.

## 分析：

标准二分

### [实现](../sourcecode/SearchInsertPosition.py)
```
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            middle = (begin + end)/2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                if middle == 0:
                    return 0
                if nums[middle - 1] < target:
                    return middle
                end = middle - 1
            else:
                if middle == len(nums) - 1:
                    return len(nums)
                if nums[middle + 1] > target:
                    return middle + 1
                begin = middle + 1
```

