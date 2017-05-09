class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = [0]*len(s)                                                
        maxLength = 0
        for i in range(1,len(s)):
            if s[i] == '(':
                continue
            j = i - l[i-1] - 1
            if j >= 0 and s[j] == '(':
                if j == 0:
                    l[i] = l[i-1] + 2 
                else :
                    l[i] = l[i-1] + 2  + l[j-1]
                maxLength = max(maxLength, l[i])
        return maxLength

if __name__ == "__main__":
    s = Solution()
    a = "(()())"
    r = s.longestValidParentheses(a)
    print r
