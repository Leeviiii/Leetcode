class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.isMatchL(s,0,p,0)
    def isMatchL(self, s, s_i, p ,p_i):
        if p_i == len(p):
            return s_i == len(s)
        if p[p_i] != '*':
            if s_i == len(s):
                return False
            if p[p_i] == '?' or p[p_i] == s[s_i]:
                return self.isMatchL(s, s_i + 1, p, p_i + 1)
            return False
        else :
            while s_i < len(s) and (s[s_i] == p[p_i] or p[p_i] == '*') :
                if self.isMatchL(s, s_i, p, p_i+1) == True:
                    return True
                s_i += 1
            return self.isMatchL(s, s_i, p, p_i+1)



if __name__ == "__main__": 
    s1 = "babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab"
    s2 = "***bba**a*bbba**aab**b"
    s = Solution()
    ret = s.isMatch(s1,s2)
    print ret
