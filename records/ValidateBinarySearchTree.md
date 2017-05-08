## [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/#/description)

>Given a binary tree, determine if it is a valid binary search tree (BST).

## 分析：

左中右遍历二叉树，然后做顺序校验

ps:也可以在遍历过程中进行校验，应该会更快，因为会提前发现BST，但是比较的次数应该会比上面的思路多一些，代码也麻烦一些.

### [实现](../sourcecode/ValidateBinarySearchTree.py)
```
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
```

