## [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/#/description)

>Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

## 分析：

- 解法一：暴力枚举，遍历每一个字符，考虑奇偶两种情况进行遍历，取出最大回文字串，时间复杂度O(n*n),可以accepted
- 解法二：动态规划，记住历史的搜索信息,用l[i,j]表示i到j之间的最长回文字串,递归公式如下

          if i == j, l[i,j] = s[i]

          elif s[i] == s[j] and s[i+1:j-1] == l[i+1,j-1] , l[i,j] = s[i] + l[i+1,j-1] + s[i]

          else l[i,j] = max(l[i+1,j-1],l[i+1,j],l[i,j+1])

          实现的时候需要对角线扫描，这种方法的时间复杂度是O(n*n)，空间复杂度是O(n*n),会超时
- 解法三*: [Manacher算法](http://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/), 时间复杂度O(n)

### [暴力枚举实现](../sourcecode/LongestPalindromicSubstringv1.py)
```
#coding=utf-8 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return "";
        if s == None:
            return "";
        max_l_p = ""
        for i in range(len(s)):
            j = 1
            """
            枚举实现
            case1 两边相同，得到的为奇数长度
            case2 偶数长度，i与i-1扩展
            case3 偶数长度，i与i+1扩展
            """
            r = self.findlongest(s, i, i)
            begin = r[0]
            end = r[1]
            if end - begin + 1 > len(max_l_p):
                max_l_p = s[begin:end+1]

            if i != 0 and s[i-1] == s[i]:
                r = self.findlongest(s, i-1,i)
                begin = r[0]
                end = r[1]
                if end - begin + 1 > len(max_l_p):
                    max_l_p = s[begin:end+1]

            if i != len(s) - 1 and s[i+1] == s[i]:
               r = self.findlongest(s, i,i+1)
               begin = r[0]
               end = r[1]
               if end - begin + 1 > len(max_l_p):
                   max_l_p = s[begin:end+1]

        return max_l_p

    def findlongest(self, s, begin, end):
        while begin > 0 and end < len(s) - 1:
            if s[begin - 1] == s[end + 1]:
                begin -= 1
                end += 1
            else :
                break;
        return [begin, end]
```


### [解法二:动态规划](../sourcecode/LongestPalindromicSubstringv2.py)
```
#coding=utf-8 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return "";
        if s == None:
            return "";
        max_l_p = ""
        l = []
        for i in range(len(s)):
            l.append([])
            for j in range(len(s)):
                l[i].append("")
        for level in range(len(s)):
            for j in range(level,len(s)):
                """
                动态规划 其实也是三种情况
                按照对角线逼近l[0][len(s)-1]
                case1 两边相同，得到的为奇数长度
                case2 偶数长度，i与i-1扩展
                case3 偶数长度，i与i+1扩展
                """
                i = j - level
                if i == j:
                    l[i][j] = s[i]
                elif s[i] == s[j] and l[i+1][j-1] == s[i+1:j]:
                    l[i][j] = s[i] + l[i+1][j-1] + s[i]
                else:
                    l[i][j] = self.maxthreestr(l[i+1][j-1],l[i+1][j],l[i][j-1])
        return l[0][len(s)-1]
    def maxthreestr(self, str1,str2,str3):
        if len(str1) > len(str2) and len(str1) > len(str3):
            return str1
        elif len(str2) > len(str1) and len(str2) > len(str3):
            return str2
        return str3
```
### [解法三:Manacher算法](../sourcecode/LongestPalindromicSubstringv3.py)

这个算法很巧妙，主要思想是利用回文的对称性。看一下效果，用这个算法在Leetcode上提交可以打败98%的用户。
![Manacher算法提交结果](../imgs/longest_substring_without_repeating_characters.png "Manacher算法提交结果")

我们考虑字符串**abababa**，这个字符串有一个以b为中心长度为7的最长回文字串，就是在第四个字符，第三个位置产生最长回文。我们考虑字符串**abaaba**，这个字符串有一个以aa为中心长度为6的最长回文字串，第二三位置产生最长回文。所以我们不得不考虑奇数偶数的情况，如果将字符串**abaaba**变为字符串**aba|aba**，那么这个新的字符串就变成了以位置3位中心，长度为6的最长回文字串，我们就不比在考虑奇偶的问题，从一个字符向左右两边扩展就可以得到最长回文字串。按照这种方法，将**abababa**和**abaaba**改造为每个字符中间都加一个|字符的模式。

![图1-1](../imgs/lps3.jpg "abababa")
![图1-2](../imgs/lps4.jpg "abaaba")

在上面的两个字符串的中心位置(第一个字符串的中心位置位7，第二个字符串的中心位置为6)，左右两边的字符都是对称的，原因是整个大的字符串就是一个回文字符串。如果一个字符串的长度为N，那么需要从左到右计算2*N+1个位置，这种对称性是否可以帮助我们减少字符的对比计算呢？如果我们知道位置p的最长回文字串长度，那么是否可以不通过字符的比较直接知道p+1的最长回文字串长度呢？

我们用L(i)表示以位置i为中心的最长回文字串长度，那么上面两个字符串经过计算可以得到。
![图1-3](../imgs/lps12.jpg "abababa")
![图1-4](../imgs/lps13.jpg "abaaba")

>Position and index for the string are two different things here. For a given string S of length N, indexes will be from 0 to N-1 (total N indexes) and positions will be from 0 to 2*N (total 2*N+1 positions).

这里有一个概念的问题，位置跟索引的区别，对于一个给定的长度为N的字符串S，索引是从0到N-1的，位置是从0到2*N的，即索引是在原始字符串中的位置下标，位置是字符在变幻之后的字符串的位置下标。因此**L[i]=d**意味着
- 从位置i-d到i+d是一个长度为d的回文子串
- 从索引(i-d)/2到[(i+d)/2 +-1]是一个长度为d的回文子串

以字符串**abaaba**为例，**L[3]=3**意味着从位置0到6是(索引0到2)一个**aba**的回文字串:
![图1-5](../imgs/lps52.jpg "abaaba")

因此只要将数组L计算完毕，就可以知道最长的回文子串了。
![图1-6](../imgs/lps6.jpg "abaaba")

对于上图如果我们观察位置3的周围可以发现
- 在位置2跟4，L[]的值是相同的
- 在位置1跟5，L[]的值是相同的

我们从位置0开始左到右遍历字符串，如果我们计算出了位置0,1,2,3的值，我们就不需要进行字符比较可以直接算出位置4，5的值了。如果我们观察位置6也可以得出类似的结论

下面是代码实现:
```
#coding=utf-8 
class Solution(object):
    def longestPalindrome(self, text):
        N = len(text)
        if N == 0:
            return
        if N == 1:
            return text
        N = 2*N+1    # Position count
        L = [0] * N
        L[0] = 0
        L[1] = 1
        C = 1     # centerPosition
        R = 2     # centerRightPosition
        i = 0     # currentRightPosition
        iMirror = 0     # currentLeftPosition
        maxLPSLength = 0
        maxLPSCenterPosition = 0
        start = -1
        end = -1
        diff = -1
        
        # Uncomment it to print LPS Length array
        for i in xrange(2,N):
            # get currentLeftPosition iMirror for currentRightPosition i
            iMirror = 2*C-i
            L[i] = 0
            diff = R - i
            # If currentRightPosition i is within centerRightPosition R
            if diff > 0:
                L[i] = min(L[iMirror], diff)
            
            # Attempt to expand palindrome centered at currentRightPosition i
            # Here for odd positions, we compare characters and
            # if match then increment LPS Length by ONE
            # If even position, we just increment LPS by ONE without
            # any character comparison
            try:
                while ((i+L[i]) < N and (i-L[i]) > 0) and (((i+L[i]+1) % 2 == 0) or (text[(i+L[i]+1)/2] == text[(i-L[i]-1)/2])):
                    L[i]+=1
            except Exception as e:
                pass
            
            if L[i] > maxLPSLength:        # Track maxLPSLength
                maxLPSLength = L[i]
                maxLPSCenterPosition = i
            
            # If palindrome centered at currentRightPosition i
            # expand beyond centerRightPosition R,
            # adjust centerPosition C based on expanded palindrome.
            if i + L[i] > R:
                C = i
                R = i + L[i]
            
        start = (maxLPSCenterPosition - maxLPSLength) / 2
        end = start + maxLPSLength - 1
        return text[start:end+1]
```
