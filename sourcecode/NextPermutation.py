#! usr/bin/python
#coding=utf-8 

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


if __name__ == "__main__":
    s = Solution()
    nums = [2,3,1,3,3]
    r = s.nextPermutation(nums)
    print nums
