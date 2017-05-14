class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.myjump(nums,0,0,None)

    def myjump(self,nums,begin,steps,currentMin):
        if currentMin != None and steps >= currentMin:
            return currentMin
        if begin >= len(nums) - 1:
            return steps
        i = nums[begin]
        while i >= 1:
            if currentMin != None and steps + 1 > currentMin:
                i -= 1
                continue
            step = self.myjump(nums,begin+i,steps+1,currentMin)
            if (currentMin == None or currentMin > step) and step != None:
                currentMin = step
            i -= 1
        return currentMin 
if __name__ == "__main__":
    s = Solution()
    nums = [2,3,1,1,4]
    r = s.jump(nums)
    print r
