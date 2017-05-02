## [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/#/description)

>Write a function to find the longest common prefix string amongst an array of strings.

## 分析：

求一组字符串的最长公共前缀，按照列遍历就可以

### [实现](../sourcecode/LongestCommonPrefix.py)
```
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
```

