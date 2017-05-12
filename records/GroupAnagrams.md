## [Group Anagrams](https://leetcode.com/problems/anagrams/#/description)

>Given an array of strings, group anagrams together.

## 分析：

将每一个单词按照字母序重新排列，然后找重复就可以了

### [实现](../sourcecode/GroupAnagrams.py)
```
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
```
