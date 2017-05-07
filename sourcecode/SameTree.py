# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        l = [p]
        r = [q]
        while len(l) != 0 and len(r) != 0:
            p1 = l.pop()
            q1 = r.pop()
            if p1 == None and q1 == None:
                continue
            if p1 == None or q1 == None:
                return False
            if p1.val != q1.val:
                return False
            l.append(p1.left)
            l.append(p1.right)
            r.append(q1.left)
            r.append(q1.right)
        if len(l) == 0 and len(r) == 0:
            return True
        return False
                                                            

if __name__ == "__main__":
    a = TreeNode(0)
    a1 = TreeNode(0)
    a2 = TreeNode(-5)
    a23 = TreeNode(-8)
    a.left = a2
    a1.left = a23
    s = Solution()
    print s.isSameTree(a,a1)

