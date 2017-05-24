# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root != None:
            self.myinorderTraversal(root,ret)
        return ret
    def myinorderTraversal(self,node,ret):
        if node.left != None:
            self.myinorderTraversal(node.left,ret)
        ret.append(node.val)
        if node.right != None:
            self.myinorderTraversal(node.right,ret)
                                                    
if __name__ == "__main__":
    s = Solution()
    nums1 = [1,3,5,7,0,0,0,0,0,0,0]
    nums2 = [0,1,2,4,6,8,10]
    s.merge(nums1,4,nums2,7)
    print nums1
