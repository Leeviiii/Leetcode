## [Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

>Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## 分析：

这道题的本质是一个二叉树的遍历问题。每一个左括号之后都跟着两种可能，继续跟一个左括号或者跟一个右括号。在遍历的时候深度广度都是可以实现的。下面是广度优先的一个遍历。其实就是按照树的层次就行遍历。

注：树的遍历一般只说先根，中根或者后根遍历。广度和深度是图遍历的说法，树可以理解为图的一种。

### [实现](../sourcecode/GenerateParentheses.py)

在分支p.leftcnt == maxlevel中，下面的实现一个优化后的实现。第一版的实现[在这里](../sourcecode/GenerateParentheses_slow.py)，这个效率不高的版本实现是:
```
t = ParenthesisNode(p.val + ')',p.level + 1, p.leftcnt, p.rightcnt + 1)
stack.append(t)
```
>第一版的实现跑完leetcode上的8个test花费了75ms,下面这个优化的实现花费了55ms


```
class ParenthesisNode(object):
    def __init__(self,c,l,left,right):
        self.val = c
        self.leftcnt = left
        self.rightcnt = right
        self.level = l

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        t = ParenthesisNode('(',1,1,0)
        maxlevel = n
        stack = [t]
        ret = []
        while len(stack) != 0:
            p = stack.pop(0)
            if p.leftcnt == p.rightcnt and p.leftcnt == maxlevel:
                ret.append(p.val)
            else:
                if p.leftcnt == p.rightcnt:
                    t = ParenthesisNode(p.val + '(',p.level + 1, p.leftcnt + 1, p.rightcnt)
                    stack.append(t)
                else:
                    if p.leftcnt == maxlevel:
                         val = p.val
                         for i in range(p.leftcnt - p.rightcnt):
                             val += ')'
                         ret.append(val)
                    else :
                         t = ParenthesisNode(p.val + ')',p.level + 1, p.leftcnt, p.rightcnt + 1)
                         stack.append(t)
                         t = ParenthesisNode(p.val + '(',p.level + 1, p.leftcnt + 1, p.rightcnt)
                         stack.append(t)
        return ret
```
