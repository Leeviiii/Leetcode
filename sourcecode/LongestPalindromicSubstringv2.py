#coding=utf-8 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return "";
        if s == None:
            return "";
        max_l_p = ""
        l = []
        for i in range(len(s)):
            l.append([])
            for j in range(len(s)):
                l[i].append("")
        for level in range(len(s)):
            for j in range(level,len(s)):
                """
                动态规划 其实也是三种情况
                按照对角线逼近l[0][len(s)-1]
                case1 两边相同，得到的为奇数长度
                case2 偶数长度，i与i-1扩展
                case3 偶数长度，i与i+1扩展
                """
                i = j - level
                if i == j:
                    l[i][j] = s[i]
                elif s[i] == s[j] and l[i+1][j-1] == s[i+1:j]:
                    l[i][j] = s[i] + l[i+1][j-1] + s[i]
                else:
                    l[i][j] = self.maxthreestr(l[i+1][j-1],l[i+1][j],l[i][j-1])
        return l[0][len(s)-1]
    def maxthreestr(self, str1,str2,str3):
        if len(str1) > len(str2) and len(str1) > len(str3):
            return str1
        elif len(str2) > len(str1) and len(str2) > len(str3):
            return str2
        return str3


if __name__ == "__main__":
	s = Solution()
	s1 = "babad"
	t = s.longestPalindrome(s1)
	print t
