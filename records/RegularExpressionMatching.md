## [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/#/description)

>Implement regular expression matching with support for '.' and '*'.

>'.' Matches any single character.'*' Matches zero or more of the preceding element.

## 分析：

实现一个简单的正则。符号.是比较好实现的，匹配任意字符就可以，主要是符号*可以匹配0个或者多个前面字符，所以符号*必须跟前面的一个字符就行组合使用，并且出现了*符号就需要对字符串s的每一种情况都进行遍历。实现代码中的while循环就是实现这个用的。需要从0一直遍历到len(s)-1的所有情况，因为*号可以匹配0或者多个。可以使用递归实现。

### [实现](../sourcecode/RegularExpressionMatching.py)
```
class Solution(object):
    def isMatch(self, s, p):
        return self.isMatchL(s,0,p,0)
    def isMatchL(self, s, s_i, p ,p_i):
        if p_i == len(p):
            return s_i == len(s)
        if p_i + 1 == len(p):
            if s_i + 1 == len(s) and (p[p_i] == s[s_i] or p[p_i] == '.'):
                return True
            return False
        if p[p_i + 1] != '*':
            if s_i == len(s):
                return False
            if p[p_i] == '.' or p[p_i] == s[s_i]:
                return self.isMatchL(s, s_i + 1, p, p_i + 1)
            return False
        else :
            while s_i < len(s) and (s[s_i] == p[p_i] or p[p_i] == '.') :
                if self.isMatchL(s, s_i, p, p_i +2) == True:
                    return True
                s_i += 1
            return self.isMatchL(s, s_i, p, p_i +2)
```
