class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in range(len(s)):
            c = s[i]
            if c == '(' or c == '[' or c == '{':
                l.insert(0,c)
            else:
                if len(l) == 0:
                    return False
                c1 = l.pop(0)
                if c == ')' and c1 != '(':
                    return False
                if c == '}' and c1 != '{':
                    return False
                if c == ']' and c1 != '[':
                    return False
        if len(l) == 0:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    r = s.isValid("}]")
    print r
