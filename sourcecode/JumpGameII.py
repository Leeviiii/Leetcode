class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxreach = 0
        lastreach = 0
        step = 0
        for i in range(len(nums)):
            if lastreach < i:
                step += 1
                lastreach = maxreach
            maxreach = max(nums[i] + i, maxreach)
        return step
    

if __name__ == "__main__":
    s = Solution()
    nums = [1,2]
    r = s.jump(nums)
    print r
