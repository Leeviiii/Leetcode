## [Next Permutation](https://leetcode.com/problems/next-permutation/#/description)

>Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

>If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

>The replacement must be in-place, do not allocate extra memory.

## 分析：

这道题目应该属于一个排序题，比较特殊的排序题，暂且放到链表里吧，更多的还是一个逻辑题。

在寻找下一个比当前大的最小序列时，应该尽可能的在低位进行重组，这样变化后的序列比原序列大的值最小。所以我们从后往前寻找一个升序点，找到这个升序点也就是说，把这个点替换比这个点大的一个数一定会得到一个比原序列大的数。那么应该用这个升序点后面的那个数进行替换呢？当然是比这个升序点大但是最小的那个数。交换后从升序点到末尾，一定保持着原始降序的性质，为了得到最小值，把后面这个序列做一个reverse就可以。下面看一下例子：
>序列为[5,4,7,5,3,2]。首先找到升序点为下标1只等于4的这个数，用这个升序点与比他大但是最小的数进行替换，这个数下标为3值为5，交换后得到序列[5,5,7,4,3,2],从下标2开始一直到最后仍然保持着降序的性质，进行reverse操作。

>如果是一个本身就是一个完整降序的序列那么久不存在题目要求的组合了，直接reverse就可以。

### [实现](../sourcecode/NextPermutation.py)
```
class Solution(object):
    def nextPermutation(self, nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            if len(nums) < 1:
                return
            #找到第一个升序,从后往前
            i = len(nums) - 1
            while i > 0 and nums[i] <= nums[i-1]:
                i -= 1
            if i != 0:
                pos = i - 1
                #找到最小替换值
                minn = None
                minp = 0
                for j in range(pos + 1,len(nums)):
                    # 这里必须有等号，要保证swap后，从pos一直到end的序列为降序序列
                    if nums[j] > nums[pos] and (nums[j] <= minn or minn == None):
                        minn = nums[j]
                        minp = j
                self.swap(nums,pos,minp)
                self.reverse(nums,i,len(nums)-1)
            else:
                self.reverse(nums,0,len(nums)-1)

    def swap(self,nums,i,j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    def reverse(self, nums, i, j):
        while i < j:
        self.swap(nums,i,j)
        i += 1
        j -= 1
```
