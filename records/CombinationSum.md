## [Combination Sum](https://leetcode.com/problems/combination-sum/#/description)

>Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

>The same repeated number may be chosen from C unlimited number of times.

>Note:All numbers (including target) will be positive integers.  The solution set must not contain duplicate combinations.

## 分析：

这道题是之前的Sudoku Solver题目的思想基本类似，都是将问题分解为更小的子问题来解决。我的思路是从后往前扫描，遇到第一个比target小于或者等于的数开始进行问题分解。这个问题可以这样描述：在数组candidates中，从0到n(假设数组candidates的长度为n+1)的位置中找到数字组合的和等于target。因此这个问题可以拆解为三个子问题
- 在数组candidates中，从0到n-1的位置中找到数字组合的和等于target-candidates[n]
- 在数组candidates中，从0到n-1的位置中找到数字组合的和等于target
- 在数组candidates中，从0到n的位置中找到数字组合的和等于target-candidates[n]

然后不停的进行子问题拆解，递归寻找解。

下面以在[2, 3, 6, 7] 寻找组合和等于7为例子进行说明，因为最后一个元素为7所以可以立即得到一个解，因此问题变成了从[2,3,6]找7，这个子问题被分解为三个子问题
- [2,3,6]匹配1  这种情况无解
- [2,3]匹配1  这种情况无解
- [2,3]匹配7
  - [2,3]匹配4
    - [2,3]匹配1 无解
    - [2]匹配1 无解
    - [2]匹配4  得到一个解[3,2,2]
  - [2]匹配4 得到一个解[3,2,2]
  - [2]匹配7 无解

>上面的思想是可以稍微优化一下的。因为在实际的实现过程中，会有重复的子问题出现。可以将子问题的解缓存起来，这样就可以避免不必要的操作，坏处是带来了一些额外的空间开销。可以看到上面的[2]匹配4这个子问题遇到了两次，理论上应该可以优化一下。

### [实现](../sourcecode/CombinationSum.py)
```
class Solution(object):
    def combinationSum(self, candidates, target):
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
            if i not in r:
                r.append(i)
        return r
    def getCombinationSum(self,candidates,end,target,l,last):
        if last == None:
            last = []
        if target == 0:
            l.append(last)
            return
        num = candidates[end]
        if end == 0 :
            if target%num != 0:
                return 
            else:
                cnt = target/num
                for i in range(cnt):
                    last.append(num)
                    l.append(last)
                    return
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
            self.getCombinationSum(candidates,end, target - num, l, last1)
            last2.append(num)
            self.getCombinationSum(candidates,end - 1, target - num, l, last2)
            self.getCombinationSum(candidates,end - 1, target, l, last)
```
