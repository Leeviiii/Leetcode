class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        la = list(a)
        lb = list(b)
        la.reverse()
        lb.reverse()
        i = 0
        isadd = 0
        lc = []
        while i < len(la) and i < len(lb):
            n = int(la[i]) + int(lb[i]) + isadd
            if n <= 1:
                lc.append(str(n))
                isadd = 0
            else:
                lc.append(str(n-2))
                isadd = 1
            i += 1
        while i < len(la):
            n = int(la[i]) + isadd
            if n <= 1:
                isadd = 0
                lc.append(str(n))
            else:
                lc.append(str(n-2))
                isadd = 1
            i += 1
        while i < len(lb):
            n = int(lb[i]) + isadd
            if n <= 1:
                isadd = 0
                lc.append(str(n))
            else:
                lc.append(str(n-2))
                isadd = 1
            i += 1
        if isadd == 1:
            lc.append('1')
        lc.reverse()
        return "".join(lc)



                                                            
if __name__ == "__main__":
    s = Solution()
    a = "1010"
    b = "1011"
    print s.addBinary(a,b)

