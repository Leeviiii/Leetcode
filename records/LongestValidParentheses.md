## [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/#/description)

>Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

>For "(()", the longest valid parentheses substring is "()", which has length = 2.

>Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

## 分析：

使用动态规划进行求解L[i]表示以i为结尾的最长合法括号字符串长度。当对L[i]求值的时候，首先看s[i]的值，如果是一个左括号直接等于0，如果是一个右括号需要向前检索找到一个左括号与之匹配，假设位置位j，如果s[j]='(',则L[i]=L[i-1]+2+L[j-1]。找到一个j与右括号匹配说明应该在L[i-1]的基础上+2，同时需要加上j前面的合法括号长度。

这里的j=i-L[i-1]-1。从i的位置向前跳过L[i-1]个位置，因为L[i-1]个长度的s一定是合法的括号字符串。跳过L[i-1]个长度后再往前跳过一个的字符就是需要跟当前的右括号进行匹配的字符。因此递推公式如下

```
if s[i] == '(' L[i]=0
else  j=i-L[i-1]-1   L[i]=L[i-1]+2+L[j]   if j>0 and s[j]=='('
                     L[i]=L[i-1]+2        if j==0 and s[j]=='('
                     L[i]=0               else
```
### [实现](../sourcecode/LongestValidParentheses.py)
```
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = [0]*len(s)                                                
        maxLength = 0
        for i in range(1,len(s)):
            if s[i] == '(':
                continue
            j = i - l[i-1] - 1
            if j >= 0 and s[j] == '(':
                if j == 0:
                    l[i] = l[i-1] + 2 
                else :
                    l[i] = l[i-1] + 2  + l[j-1]
                maxLength = max(maxLength, l[i])
        return maxLength
```
