## [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/#/description)

>You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

## 分析：

第一思路肯定使用一个hashmap将word的list进行存储以便于进行与s对比。这里的关键是如何移动的问题。因为每个word都是相同长度的，所以可以一次移动一个word的长度，有word-1种可能，都需要遍历到。遍历过程中的字符串匹配过程如下:
- 如果字符串不匹配就很简单了，重置一些信息，然后向前移动一个word的长度就可以。
- 如果字符匹配，需要记录匹配的个数
  - 如果匹配到的个数达到了要求，这个时候说明找到了一个解。解的位置向前移动一个word的长度
  - 如果匹配的单个word个数超过了给出的word，这个时候的移动比较重要。需要将已经匹配到的个数减下去。


### [实现](../sourcecode/SubstringwithConcatenationofAllWords.py)
```
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        wl = len(words[0])
        if len(s) < wl:
            return []
        wmap = {}
        for t in words:
            if t in wmap:
                wmap[t] += 1
            else:
                wmap[t] = 1
        i = 0
        needmatchcnt = len(words)
        result = []
        for i in range(wl):
            j = i
            left = i
            ret = {}
            hasmatchcnt = 0
            while j < len(s):
                t = s[j:j+wl]
                if t in wmap:
                    if t in ret:
                        ret[t] += 1
                    else:
                        ret[t] = 1
                    #匹配到一个
                    if ret[t] <= wmap[t]:
                        hasmatchcnt += 1
                    else :
                        #匹配多了 需要重新赋值开始的位置
                        while ret[t] > wmap[t]:
                            tmp = s[left:left+wl]
                            if tmp in ret:
                                ret[tmp] -= 1
                                if ret[tmp] < wmap[tmp]:
                                    hasmatchcnt -= 1
                            left += wl
                    if hasmatchcnt == needmatchcnt:
                        result.append(left)
                        tmp = s[left:left+wl]
                        if tmp in ret:
                            ret[tmp] -= 1
                        hasmatchcnt -= 1
                        left += wl
                else:
                    ret = {}
                    hasmatchcnt = 0
                    left = j + wl
                j = j + wl
        return result
```
