class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = []
        self.mypermute(nums,l,None)
        return l
    def mypermute(self, nums, l, last):
        if len(nums) == 0:
            return ;
        if last == None:
            last = []
        if len(nums) == 1:
            last.append(nums[0])
            l.append(last)
            return
        for i in range(len(nums)):
            num = nums[i]
            lastt = last[0:len(last)]
            lastt.append(num)
            newnums = self.getslicearray(nums,i)
            self.mypermute(newnums,l,lastt)
    def getslicearray(self,nums,i):
        newnums = []
        for j in range(len(nums)):
            if j == i:
                continue;
            newnums.append(nums[j])
        return newnums
                                                    
if __name__ == "__main__":
    s = Solution()
    a = [1,2,3]
    r = s.permute(a)
    print r
