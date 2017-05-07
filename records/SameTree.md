## [Same Tree](https://leetcode.com/problems/same-tree/#/description)

>Given two binary trees, write a function to check if they are equal or not.

>Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


## 分析：

遍历二叉树

### [实现](../sourcecode/SameTree.py)
```
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
```
