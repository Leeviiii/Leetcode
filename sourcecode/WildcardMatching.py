class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        res = [False]*(len(s) + 1) 
        res[0] = True
        for j in range(len(p)):
            if p[j] != '*' :
                i = len(s) - 1
                while i >= 0:
                    res[i+1] = (res[i] and (p[j] == '?' or p[j] == s[i]))
                    i -= 1
            else:
                i = 0
                while i <= len(s) and res[i] == False:
                    i += 1
                while i <= len(s):
                    res[i] = True
                    i += 1
            res[0] = (res[0] and p[j] == '*')
        return res[len(s)]



if __name__ == "__main__": 
    s1 = "zacabz"
    s2 = "*a?b*"
    s = Solution()
    ret = s.isMatch(s1,s2)
    print ret
