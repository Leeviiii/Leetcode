## [Multiply Strings](https://leetcode.com/problems/multiply-strings/#/description)

>Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.

Both num1 and num2 contains only digits 0-9.

Both num1 and num2 does not contain any leading zero.

You must not use any built-in BigInteger library or convert the inputs to integer directly.


## 分析：

这是一道大数乘法题目，我的做法是，先算每一位然后相加。有一个Karatsuba算法算法应该更好，有空看看实现一下。

最基本的先每一位乘然后相加思想比较简单，但是实现起来比较麻烦，要考虑好各种特殊情况。

### [实现](../sourcecode/MultiplyStrings.py)
```
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
```
