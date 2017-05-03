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
                        #t = ParenthesisNode(p.val + ')',p.level + 1, p.leftcnt, p.rightcnt + 1)
                        for i in range(p.leftcnt - p.rightcnt):
                            val += ')'
                        ret.append(val)
                    else :
                        t = ParenthesisNode(p.val + ')',p.level + 1, p.leftcnt, p.rightcnt + 1)
                        stack.append(t)
                        t = ParenthesisNode(p.val + '(',p.level + 1, p.leftcnt + 1, p.rightcnt)
                        stack.append(t)
        return ret

if __name__ == "__main__":
    s = Solution()
    r = s.generateParenthesis(3)
    print r
