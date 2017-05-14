class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxreach = 0
        for i in range(len(nums)-1):
            if i > maxreach:
                continue
            maxreach = max(nums[i] + i, maxreach)
        if maxreach + 1 < len(nums):
            return False
        return True
if __name__ == "__main__":
    s = Solution()
    nums = [3,2,0,0,4]
    r = s.canJump(nums)
    print r
