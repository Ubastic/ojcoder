# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    s = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.s = 0
        return self.helper(root)
        
    def helper(self, node):
        if not node:    return
        self.helper(node.right)
        self.s += node.val
        node.val = self.s
        self.helper(node.left)
        return node