class Solution(object):
    def longestCommonPrefix(self, strs):
        k = 0
        ret = "";
        if strs == None or len(strs) == 0:
            return ""
        while True: 
            c = None
            isbreak = 0
            for i in range(len(strs)):
                if c == None and k != len(strs[i]):
                    c = strs[i][k]
                else :
                    if k == len(strs[i]) or c != strs[i][k]:
                        isbreak = 1
                        break
            if isbreak == 1:
                break
            ret = ret + c
            k += 1
        return ret



        




if __name__ == "__main__":
    s = Solution()
    strs = ["","abcd","abcde"]
    r = s.longestCommonPrefix(strs)
    print r
