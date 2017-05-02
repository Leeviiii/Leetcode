## [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/#/description)

>Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

>The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

## 分析：

用栈解决就可以，扫描匹配

### [实现](../sourcecode/ValidParentheses.py)
```
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
```
