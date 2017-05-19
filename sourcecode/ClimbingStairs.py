class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        l1 = 1
        l2 = 2
        l3 = 0
        for i in range(3,n+1):
            l3 = l1 + l2
            l1 = l2
            l2 = l3
        return l3
        
                                                    
if __name__ == "__main__":
    s = Solution()
    r = s.climbStairs(4)
    print r
