class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1

        for begin in range(len(haystack) - len(needle) + 1):
            isfound = True
            for i in range(len(needle)):
                if haystack[begin + i] != needle[i]:
                    isfound = False
                    break
            if isfound :
                return begin
        return -1
if __name__ == "__main__":
    s = Solution()
    r = s.strStr("abcd","d")
    print r
