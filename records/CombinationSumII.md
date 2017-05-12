## [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/#/description)

>Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

>Each number in C may only be used once in the combination.

>Note:All numbers (including target) will be positive integers.  The solution set must not contain duplicate combinations.

## 分析：

这道题是之前的Combination Sum题目的思想一样只做一小点的修改就可以，因为不允许一个元素使用多次，使用Combination Sum题目分解出来的三个子问题，这个问题只能分解出来两个。
- 在数组candidates中，从0到n-1的位置中找到数字组合的和等于target-candidates[n]
- 在数组candidates中，从0到n-1的位置中找到数字组合的和等于target

然后不停的进行子问题拆解，递归寻找解。

### [实现](../sourcecode/CombinationSumII.py)
```
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        end = len(candidates) - 1
        if end < 0 :
            return None
        l = []
        self.getCombinationSum(candidates,end,target,l,None)
        r = []
        for i in l:
            i.sort()
            if i not in r:
                r.append(i)
        return r
    def getCombinationSum(self,candidates,end,target,l,last):
        if end == -1:
            return 
        if last == None:
            last = []
        num = candidates[end]
        if target < num:
            return self.getCombinationSum(candidates,end - 1, target, l, last)
        elif target == num:
            last1 = last[0:len(last)]
            last.append(num)
            l.append(last)
            self.getCombinationSum(candidates,end-1, target, l, last1)
        else:
            last1 = last[0:len(last)]
            last2 = last[0:len(last)]
            last1.append(num)
            self.getCombinationSum(candidates,end - 1, target - num, l, last1)
            self.getCombinationSum(candidates,end - 1, target, l, last)
```
