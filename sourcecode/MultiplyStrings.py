class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = {}
        for i in range(10):
            m[str(i)] = i
        result = {}
        midresult = []
        for i in range(len(num1)):
            c = num1[len(num1)-i-1]
            c1 = m[c]               
            midr = []
            jinwei = 0
            for j in range(len(num2)):
                r = c1*m[num2[len(num2)-1-j]]
                if r%10 + jinwei >= 10:
                    midr.append(r%10 + jinwei - 10)
                    jinwei = r/10 + 1
                else:
                    midr.append(r%10 + jinwei)
                    jinwei = r/10
            for k in range(i):
                midr.insert(0,0)
            if jinwei != 0:
                midr.append(jinwei)
            midresult.append(midr)
        print midresult
        xx = self.addlist(midresult,0,len(midresult)-1)
        xx.reverse()
        if xx == None or len(xx) == 0:
            return "0"
        while xx[0] == 0 and len(xx) > 1:
            xx = xx[1:len(xx)]
        xt = []
        for x in xx:
            xt.append(str(x))
        return "".join(xt)
    def addlist(self, l, begin, end):
        if end < begin:
            return None
        if end == begin:
            return l[begin]
        if end - begin == 1:
            return self.addtwolist(l[begin],l[end])
        m = (begin+end)/2
        left = self.addlist(l,begin,m)
        right = self.addlist(l,m+1,end)
        return self.addtwolist(left,right)
    def addtwolist(self,l1,l2):
        l = []
        i = 0
        isadd = 0
        while i < len(l1) and i < len(l2):
            n = l1[i] + l2[i] + isadd
            if n/10 != 0:
                isadd = 1
            else:
                isadd = 0
            l.append(n%10)
            i += 1
        while i < len(l1):
            n = l1[i] + isadd
            if n/10 != 0:
                isadd = 1
            else:
                isadd = 0
            l.append(n%10)
            i += 1
        while i < len(l2):
            n = l2[i] + isadd
            if n/10 != 0:
                isadd = 1
            else:
                isadd = 0
            l.append(n%10)
            i += 1
        if isadd == 1:
            l.append(1)
        return l
                                                    
if __name__ == "__main__":
    s = Solution()
    a = "6"
    b = "501"
    r = s.multiply(a,b)
    print r
