class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None:
            return 0
        vals = s.split()
        if len(vals) == 0:
            return 0
        return len(vals[len(vals)-1])


if __name__ == "__main__": 
    s = Solution()
    strs = "Hello World"
    ret = s.lengthOfLastWord(strs)
    print ret
