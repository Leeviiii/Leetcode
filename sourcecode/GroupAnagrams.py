class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapt = {}
        retl = []
        i = 0
        for s in strs:
            l = list(s)
            l.sort()
            s1 = "".join(l)
            if s1 not in mapt:
                tmp = []
                tmp.append(s)
                retl.append(tmp)
                mapt[s1] = i
                i += 1
            else:
                pos = mapt[s1]
                retl[pos].append(s)
        return retl
                                                    
if __name__ == "__main__":
    s = Solution()
    a = ["eat", "tea", "tan", "ate", "nat", "bat"]
    r = s.groupAnagrams(a)
    print r
