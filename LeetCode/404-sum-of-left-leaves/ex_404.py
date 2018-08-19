# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        if root:
            if root.left and not root.left.left and not root.left.right:
                # a valid node must to be the left child of its parent and has no children of its own 
                ans += root.left.val
            ans += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return ans