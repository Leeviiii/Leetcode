class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d_s = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        l = []
        for i in range(len(digits)):
            c = digits[i]
            if c in d_s:
                l.append(d_s.get(c))
        return self.combin(l,0,len(l)- 1)
    def combin(self, strs,begin, end) :
        if begin > end:
            return [];
        if begin == end:
            return strs[begin]
        if end - begin == 1:
            return self.combin2(strs[begin],strs[end])
        middle = (begin + end)/2
        left = self.combin(strs,begin,middle)
        right = self.combin(strs,middle + 1,end)
        return self.combin2(left, right)


    def combin2(self,str1,str2):
        ret = []
        for s1 in str1:
            for s2 in str2:
                c = s1 + s2
                ret.append(c)
        return ret


        




if __name__ == "__main__":
    s = Solution()
    digits = "";
    r = s.letterCombinations(digits)
    print r
