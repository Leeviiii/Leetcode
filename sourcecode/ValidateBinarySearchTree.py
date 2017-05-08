# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        l = []
        self.leftOrderTree(root, l)
        for i in range(0,len(l) - 1):
            if l[i] >= l[i+1]:
                return False
        return True
    def isLeaf(self, p):
        if p.left == None and p.right == None:
            return True
        return False
    def leftOrderTree(self, p, l):
        if p == None:
            return
        self.leftOrderTree(p.left, l)
        l.append(p.val)
        self.leftOrderTree(p.right, l)

if __name__ == "__main__":
    a = TreeNode(1)
    a1 = TreeNode(1)
    a.right= a1
    s = Solution()
    print s.isValidBST(a)

