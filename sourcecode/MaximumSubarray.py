class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        currmentmax = nums[0]
        retmax = nums[0]
        for i in range(1,len(nums)):
            if nums[i] >= 0:
                if currmentmax > 0:
                    currmentmax += nums[i]
                else:
                    currmentmax = nums[i]
            else:
                if currmentmax > 0:
                    if currmentmax + nums[i] <= 0:
                        currmentmax = 0
                    else :
                        currmentmax = currmentmax + nums[i]
                else:
                    currmentmax = max(currmentmax,nums[i])
            if currmentmax > retmax:
                retmax = currmentmax

        return retmax



if __name__ == "__main__": 
    #s1 = [-2,1,-3,4,-1,2,1,-5,4]
    s1 = [-1,-2,-3]
    s = Solution()
    ret = s.maxSubArray(s1)
    print ret
