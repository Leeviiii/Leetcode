## [Text Justification](https://leetcode.com/problems/text-justification/#/description)

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
```
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
"This    is    an",
"example  of text",
"justification.  "
]
```
Note: Each word is guaranteed not to exceed L in length.

## 分析：

按照题目要求写好逻辑就可以，唯一需要说一下的就是，如何确定除了第一行之外的那些行的单词直接的空格数量。题目要求是尽量的平均，否则就左边的大于右边的。因此平均就是需要的总空格数除以(单词数量-1)，应该还剩下需要的总空格数%(单词数量-1),这个空格数从左到右依次在单词后面加一个空格就可以了。

### [实现](../sourcecode/TextJustification.py)
```
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return
        ret = []
        leftwidth = maxWidth
        tmpret = []
        begin = 0
        end = 0
        for word in words:
            if len(word) <= leftwidth:
                leftwidth -= len(word)
                leftwidth -= 1
                if leftwidth == 0:
                    tmpret = self.childfullJustify(words, begin, end, maxWidth,leftwidth)
                    ret.append(tmpret)
                    begin = end + 1
                    leftwidth = maxWidth
                end += 1
            else:
                tmpret = self.childfullJustify(words, begin, end-1, maxWidth,leftwidth)
                ret.append(tmpret)
                begin = end
                leftwidth = maxWidth
                leftwidth -= len(word)
                leftwidth -= 1
                end += 1
        if begin != end:
            tmpret = self.childfullJustify(words,begin,end-1,maxWidth,leftwidth)
            ret.append(tmpret)
        return ret
    def childfullJustify(self,words,begin,end,maxWidth,leftwidth):
        tmpret = [' ']*maxWidth
        space = leftwidth + end - begin + 1
        extraspace = 0
        avgspace = 0
        if end == len(words) - 1:
            extraspace = 0
            avgspace = 1
        elif end != begin:
            avgspace = space/(end - begin)
            extraspace = space%(end - begin)
        else:
            extraspace = 0
        j = 0
        extrak = 0
        for i in range(begin,end+1):
            word = words[i]
            for k in word:
                tmpret[j] = str(k)
                j += 1
            if i == end:
                break
            for i in range(avgspace):
                j += 1
            if extrak < extraspace:
                j += 1
                extrak += 1
        return "".join(tmpret)
```
