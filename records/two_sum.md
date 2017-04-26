## [Two Sum](https://leetcode.com/problems/two-sum/#/description)

>Given an array of integers, return indices of the two numbers such that they add up to a specific target.

>You may assume that each input would have exactly one solution, and you may not use the same element twice.

>Example:Given nums = [2, 7, 11, 15], target = 9,

>Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].

## 分析：

- 解法一：排序，然后首尾哨兵扫数组时间复杂度O(nlgn)，但是要返回数据下标，排序就不好用了
- 解法二：哈希表O(n)
### [实现](../sourcecode/twosum.py)
```
class Solution(object):
  def twoSum(self, nums, target):
    tmp = {}
    i = 0
    #如果num有重复的，那么后面的num下标会被记录
    for num in nums:
      tmp[num] = i
      i+=1
    for i in range(len(nums)):
      num = nums[i]
      num1 = target - num
      if num1 in tmp.keys():
        k1 = tmp[num1]
        #防止出现 [3,5,11] 6的case
        if k1 == i:
          continue;
        return [i,k1]
    return None
```
