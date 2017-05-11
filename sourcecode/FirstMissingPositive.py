class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        l = 0
        r = len(nums)
        while l < r:
            if nums[l] >0 and nums[l] != l + 1 and nums[l] - 1 < r and nums[l] != nums[nums[l]-1]:
                self.swap(nums, l, nums[l] - 1)
            else:
                l += 1
        i = 0
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i +1 
        return i + 2
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

                                                        

if __name__ == "__main__":
    s = Solution()
    a = [0,2,2,4,0,1,0,1,3]
    r = s.firstMissingPositive(a)
    print r
