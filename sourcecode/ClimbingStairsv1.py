class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.myclimbStairs(n)
    def myclimbStairs(self,n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.myclimbStairs(n-1) + self.myclimbStairs(n-2)
        
                                                    
if __name__ == "__main__":
    s = Solution()
    r = s.climbStairs(35)
    print r
