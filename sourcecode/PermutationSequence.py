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
if __name__ == "__main__":
    s = Solution()
    r = s.getPermutation(3,5)
    print r
