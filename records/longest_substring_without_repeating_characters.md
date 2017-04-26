## [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description)

>Given a string, find the length of the longest substring without repeating characters.

## 分析：

我们用Index记录着一个字符的最大下标，依次来尽可能的加快扫描字符串的速度,以下面的字符串为例
>abcdedklklkl

当我们扫描到第二个d的时候，应该从e重开开始统计最长的非重复字串，而不应该从b开始.


### [实现](../sourcecode/LongestSubstringWithoutRepeatingCharacters.py)
```
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    if len(s) <= 1:
      return len(s)
    index = {}
    index[s[0]] = 0
    begin = 0
    end = 0
    maxbegin = 0
    maxend = 0;
    for i in range(1,len(s)):
      c = s[i]
      if c not in index:
        index[c] = i
        end += 1
        continue
      p = index[c]
      if p >= begin and p <= end:
        if maxend - maxbegin < end - begin:
          maxend = end
          maxbegin = begin;
        begin = p + 1
        end = i
      else:
        end+=1
      index[c] = i
    if end > len(s) - 1:
      end = len(s) - 1
    if maxend - maxbegin < end - begin:
      maxend = end
      maxbegin = begin;
    return maxend - maxbegin + 1
```

