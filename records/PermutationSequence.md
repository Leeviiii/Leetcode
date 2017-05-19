## [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/#/description)

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,

We get the following sequence (ie, for n = 3):
```
"123"
"132"
"213"
"231"
"312"
"321"
```
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

## 分析：

分治法，进行子问题分解。我们知道一个[1,2,3,...n]最多有n!(n的阶乘)中组合，如果确定了开头，比如以2位开头的组合，那么就有(n-1)!个组合，依次类推，我们就可以知道第k个位置的每一位的数字:

如果k<(n-1)!的阶乘，说明第k个组合的第一个数字一定为1；如果(n-1)!<k<(n-1)!*2说明第k个组合的第一个数字一定为2(这里的2应该是剩下数字可能的第二个，如果剩下的数字为[1,3,...n]即第一个为2，那么这里的第2个数字应该是3)，注意考虑去重的问题......这里假设(n-1)!<k<(n-1)!*2,因此原问题就分解成了一个开头数字为2，数字组合为[1,3,4...n],找到第k-(n-1)!个排列组合......依次类推就可以根据k得到第k个排列组合的每一个数字。

### [实现](../sourcecode/PermutationSequence.py)
```
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = []
        length = n
        while length > 0:
            step = self.getCnt(length-1)
            for i in range(1,n+1):
                if str(i) in nums:
                    continue
                if k > step:
                    k -= step
                    continue
                nums.append(str(i))
                length-=1
                break
            if k > step:
                return 0
        return ''.join(nums)
    def getCnt(self, n):
        t = 1
        for i in range(2,n+1):
            t *= i
        return t
```
