## [Implement strStr](https://leetcode.com/problems/implement-strstr/#/description)

>Implement strStr().Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## 分析：

暴力搜索就可以

### [实现](../sourcecode/strStr.py)
```
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1

        for begin in range(len(haystack) - len(needle) + 1):
            isfound = True
            for i in range(len(needle)):
                if haystack[begin + i] != needle[i]:
                    isfound = False
                    break
            if isfound :
                return begin
        return -1
```
