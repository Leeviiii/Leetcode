## [Permutations](https://leetcode.com/problems/permutations/#/description)

>Given a collection of distinct numbers, return all possible permutations.

## 分析：

分治法，进行子问题分解。假设数组nums的长度为n，则初始问题可以分解为分别为n个数字开头子排列组合的n个子问题。递归实现就可以。

### [实现](../sourcecode/Permutations.py)
```
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        self.mypermute(nums,l,None)
        return l
    def mypermute(self, nums, l, last):
        if len(nums) == 0:
            return ;
        if last == None:
            last = []
        if len(nums) == 1:
            last.append(nums[0])
            l.append(last)
            return
        for i in range(len(nums)):
            num = nums[i]
            lastt = last[0:len(last)]
            lastt.append(num)
            newnums = self.getslicearray(nums,i)
            self.mypermute(newnums,l,lastt)
    def getslicearray(self,nums,i):
        newnums = []
        for j in range(len(nums)):
            if j == i:
                continue;
            newnums.append(nums[j])
        return newnums
```                                                                                                                                                                                                                                                                                                                                                          
