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
        for i in range(len(s)):
            j = 1
            """
            枚举实现
            case1 两边相同，得到的为奇数长度
            case2 偶数长度，i与i-1扩展
            case3 偶数长度，i与i+1扩展
            """
            r = self.findlongest(s, i, i)
            begin = r[0]
            end = r[1]
            if end - begin + 1 > len(max_l_p):
                max_l_p = s[begin:end+1]

            if i != 0 and s[i-1] == s[i]:
                r = self.findlongest(s, i-1,i)
                begin = r[0]
                end = r[1]
                if end - begin + 1 > len(max_l_p):
                    max_l_p = s[begin:end+1]
            if i != len(s) - 1 and s[i+1] == s[i]:
                r = self.findlongest(s, i,i+1)
                begin = r[0]
                end = r[1]
                if end - begin + 1 > len(max_l_p):
                    max_l_p = s[begin:end+1]

        return max_l_p

    def findlongest(self, s, begin, end):
        while begin > 0 and end < len(s) - 1:
            if s[begin - 1] == s[end + 1]:
                begin -= 1
                end += 1
            else :
                break;
        return [begin, end]

			



if __name__ == "__main__":
	s = Solution()
	s1 = "babad"
	t = s.longestPalindrome(s1)
	print t
