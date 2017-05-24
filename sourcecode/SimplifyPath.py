class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ret = []
        wordslist = path.split('/')
        for i in wordslist:
            if len(i) == 0:
                continue
            if i == '.':
                continue;
            if i == '..':
                if len(ret) == 0:
                    continue
                ret.pop(len(ret)-1)
                continue
            ret.append(i)
        return "/" + "/".join(ret)
if __name__ == "__main__":
    s = Solution()
    r = s.simplifyPath("/")
    print r
